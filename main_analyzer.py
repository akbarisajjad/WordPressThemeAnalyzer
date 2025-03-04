import os
import re
import json
import subprocess
import shutil
from bs4 import BeautifulSoup
import pdfkit
from typing import List, Dict, Optional, TypedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
import gettext
import unittest
import logging
import configparser
import sqlite3
from dataclasses import dataclass
import asyncio
from ui import ThemeAnalyzerUI

# تنظیمات چندزبانه‌سازی
gettext.install('messages', localedir='locales', names=('gettext',))

# تعریف ساختار TypedDict برای نتایج
class AnalysisResults(TypedDict):
    errors: List[str]
    warnings: List[str]
    info: List[str]
    security: List[str]
    performance: List[str]
    seo: List[str]

# کلاس Singleton برای مدیریت گزارش‌ها
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class WordPressThemeAnalyzer(metaclass=SingletonMeta):
    def __init__(self, theme_path: str):
        self.theme_path = theme_path
        self.results: AnalysisResults = {
            "errors": [],
            "warnings": [],
            "info": [],
            "security": [],
            "performance": [],
            "seo": []
        }
        self.setup_logging()
        self.load_config()

    def setup_logging(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.FileHandler("theme_analysis.log"), logging.StreamHandler()]
        )

    def load_config(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def validate_theme_path(self) -> bool:
        if not os.path.exists(self.theme_path) or not os.path.isdir(self.theme_path):
            self.results["errors"].append(gettext("Invalid theme path."))
            logging.error(gettext("Invalid theme path."))
            return False
        return True

    def analyze_style_css(self) -> None:
        style_path = os.path.join(self.theme_path, "style.css")
        if not os.path.exists(style_path):
            self.results["errors"].append(gettext("style.css file not found."))
            logging.error(gettext("style.css file not found."))
            return

        try:
            with open(style_path, "r", encoding="utf-8") as f:
                content = f.read()
                required_fields = ["Theme Name", "Version", "Description", "License"]
                for field in required_fields:
                    if f"{field}:" not in content:
                        self.results["warnings"].append(gettext(f"{field} is missing in style.css."))
                        logging.warning(gettext(f"{field} is missing in style.css."))
        except IOError as e:
            self.results["errors"].append(gettext(f"Error reading style.css: {e}"))
            logging.error(gettext(f"Error reading style.css: {e}"))

    def check_php_syntax(self) -> None:
        for root, _, files in os.walk(self.theme_path):
            for file in files:
                if file.endswith(".php"):
                    file_path = os.path.join(root, file)
                    result = subprocess.run(["php", "-l", file_path], capture_output=True, text=True)
                    if result.returncode != 0:
                        self.results["errors"].append(gettext(f"Syntax error in {file}: {result.stderr}"))
                        logging.error(gettext(f"Syntax error in {file}: {result.stderr}"))

    def check_security_issues(self) -> None:
        dangerous_functions = ["eval", "exec", "shell_exec", "system", "passthru", "popen"]
        for root, _, files in os.walk(self.theme_path):
            for file in files:
                if file.endswith(".php"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            for func in dangerous_functions:
                                if func in content:
                                    self.results["security"].append(gettext(f"Dangerous function {func} found in {file}."))
                                    logging.warning(gettext(f"Dangerous function {func} found in {file}."))
                            if "SELECT *" in content:
                                self.results["security"].append(gettext(f"Potential SQL injection in {file}."))
                                logging.warning(gettext(f"Potential SQL injection in {file}."))
                            if "echo $_GET" in content or "echo $_POST" in content:
                                self.results["security"].append(gettext(f"Potential XSS vulnerability in {file}."))
                                logging.warning(gettext(f"Potential XSS vulnerability in {file}."))
                    except IOError as e:
                        self.results["errors"].append(gettext(f"Error reading {file}: {e}"))
                        logging.error(gettext(f"Error reading {file}: {e}"))

    def check_performance_issues(self) -> None:
        for root, _, files in os.walk(self.theme_path):
            for file in files:
                if file.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg")):
                    file_path = os.path.join(root, file)
                    if os.path.getsize(file_path) > 500 * 1024:  # بیش از 500 کیلوبایت
                        self.results["performance"].append(gettext(f"Image {file} is larger than optimal size."))
                        logging.warning(gettext(f"Image {file} is larger than optimal size."))

    def check_seo_issues(self) -> None:
        index_path = os.path.join(self.theme_path, "header.php")
        if not os.path.exists(index_path):
            self.results["warnings"].append(gettext("header.php file not found."))
            logging.warning(gettext("header.php file not found."))
            return

        try:
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()
                soup = BeautifulSoup(content, "html.parser")
                meta_tags = soup.find_all("meta")
                if not any(tag.get("name") == "description" for tag in meta_tags):
                    self.results["seo"].append(gettext("Meta description tag is missing."))
                    logging.warning(gettext("Meta description tag is missing."))
                if not any(tag.get("name") == "keywords" for tag in meta_tags):
                    self.results["seo"].append(gettext("Meta keywords tag is missing."))
                    logging.warning(gettext("Meta keywords tag is missing."))
        except IOError as e:
            self.results["errors"].append(gettext(f"Error reading header.php: {e}"))
            logging.error(gettext(f"Error reading header.php: {e}"))

    def generate_report(self) -> None:
        report_path = os.path.join(self.theme_path, "analysis_report.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=4, ensure_ascii=False)

        html_report = "<html><head><meta charset='UTF-8'><title>Theme Analysis Report</title></head><body>"
        html_report += "<h1>WordPress Theme Analysis Report</h1>"
        for category, issues in self.results.items():
            html_report += f"<h2>{category}</h2><ul>"
            for issue in issues:
                html_report += f"<li>{issue}</li>"
            html_report += "</ul>"
        html_report += "</body></html>"

        pdf_path = os.path.join(self.theme_path, "analysis_report.pdf")
        pdfkit.from_string(html_report, pdf_path)

    def run_analysis(self) -> None:
        if not self.validate_theme_path():
            return
        self.analyze_style_css()
        self.check_php_syntax()
        self.check_security_issues()
        self.check_performance_issues()
        self.check_seo_issues()
        self.generate_report()

if __name__ == "__main__":
    ui = ThemeAnalyzerUI()
    ui.run()
