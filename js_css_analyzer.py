import os
import logging
from typing import Dict, List

class JsCssAnalyzer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze(self) -> None:
        for root, _, files in os.walk(self.analyzer.theme_path):
            for file in files:
                if file.endswith(".js"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if "eval(" in content:
                                self.analyzer.results["security"].append(f"Use of eval() found in {file}.")
                                logging.warning(f"Use of eval() found in {file}.")
                            if "console.log(" in content:
                                self.analyzer.results["warnings"].append(f"Use of console.log() found in {file}.")
                                logging.warning(f"Use of console.log() found in {file}.")
                    except IOError as e:
                        self.analyzer.results["errors"].append(f"Error reading JavaScript file {file}: {e}")
                        logging.error(f"Error reading JavaScript file {file}: {e}")
                elif file.endswith(".css"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if "!important" in content:
                                self.analyzer.results["warnings"].append(f"Use of !important found in {file}.")
                                logging.warning(f"Use of !important found in {file}.")
                            if "@import" in content:
                                self.analyzer.results["warnings"].append(f"Use of @import found in {file}.")
                                logging.warning(f"Use of @import found in {file}.")
                    except IOError as e:
                        self.analyzer.results["errors"].append(f"Error reading CSS file {file}: {e}")
                        logging.error(f"Error reading CSS file {file}: {e}")
