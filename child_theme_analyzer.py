import os
import re
import logging
from typing import Dict, List

class ChildThemeAnalyzer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze(self) -> None:
        style_path = os.path.join(self.analyzer.theme_path, "style.css")
        if not os.path.exists(style_path):
            self.analyzer.results["errors"].append("style.css file not found.")
            logging.error("style.css file not found.")
            return

        try:
            with open(style_path, "r", encoding="utf-8") as f:
                content = f.read()
                if "Template:" in content:
                    parent_theme = re.search(r"Template:\s*(\S+)", content).group(1)
                    parent_theme_path = os.path.join(os.path.dirname(self.analyzer.theme_path), parent_theme)
                    if not os.path.exists(parent_theme_path):
                        self.analyzer.results["errors"].append(f"Parent theme '{parent_theme}' not found.")
                        logging.error(f"Parent theme '{parent_theme}' not found.")
                    else:
                        self.analyzer.results["info"].append(f"Child theme is using parent theme '{parent_theme}'.")
                        logging.info(f"Child theme is using parent theme '{parent_theme}'.")
                        required_files = ["style.css", "functions.php", "index.php"]
                        for file in required_files:
                            file_path = os.path.join(parent_theme_path, file)
                            if not os.path.exists(file_path):
                                self.analyzer.results["warnings"].append(f"Required file {file} not found in parent theme.")
                                logging.warning(f"Required file {file} not found in parent theme.")
                else:
                    self.analyzer.results["info"].append("This is not a child theme.")
                    logging.info("This is not a child theme.")
        except IOError as e:
            self.analyzer.results["errors"].append(f"Error reading style.css: {e}")
            logging.error(f"Error reading style.css: {e}")
