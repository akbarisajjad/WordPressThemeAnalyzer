import os
import re
import json
import subprocess
import logging
import configparser
import pdfkit
from typing import List, Dict, TypedDict
from bs4 import BeautifulSoup

class WordPressThemeAnalyzer(metaclass=SingletonMeta):
    def __init__(self, theme_path: str):
        self.theme_path = theme_path
        self.results: AnalysisResults = AnalysisResults(
            errors=[],
            warnings=[],
            info=[],
            security=[],
            performance=[],
            seo=[]
        )
        self.setup_logging()
        self.load_config()
# پیاده‌سازی Singleton
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
        if not logging.getLogger().hasHandlers():
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
                handlers=[logging.FileHandler("theme_analysis.log"), logging.StreamHandler()]
            )

    def load_config(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def validate_theme_path(self) -> bool:
        if not os.path.isdir(self.theme_path):
            self.results["errors"].append("Invalid theme path.")
            logging.error("Invalid theme path.")
            return False
        return True

    def analyze_style_css(self) -> None:
        style_path = os.path.join(self.theme_path, "style.css")
        if not os.path.exists(style_path):
            self.results["errors"].append("style.css file not found.")
            logging.error("style.css file not found.")
            return

        try:
            with open(style_path, "r", encoding="utf-8") as f:
                content = f.read()
                for field in ["Theme Name", "Version", "Description", "License"]:
                    if f"{field}:" not in content:
                        self.results["warnings"].append(f"{field} is missing in style.css.")
                        logging.warning(f"{field} is missing in style.css.")
        except IOError as e:
            self.results["errors"].append(f"Error reading style.css: {e}")
            logging.error(f"Error reading style.css: {e}")

    def check_php_syntax(self) -> None:
        for root, _, files in os.walk(self.theme_path):
            for file in files:
                if file.endswith(".php"):
                    file_path = os.path.join(root, file)
                    result = subprocess.run(["php", "-l", file_path], capture_output=True, text=True)
                    if result.returncode != 0:
                        self.results["errors"].append(f"Syntax error in {file}: {result.stderr}")
                        logging.error(f"Syntax error in {file}: {result.stderr}")

    def check_security_issues(self) -> None:
        dangerous_patterns = [r"\beval\s*
