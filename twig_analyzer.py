import os
import logging
from typing import Dict, List

class TwigAnalyzer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze(self) -> None:
        for root, _, files in os.walk(self.analyzer.theme_path):
            for file in files:
                if file.endswith(".twig"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if "{{ }}" in content:
                                self.analyzer.results["info"].append(f"Twig template used in {file}.")
                                logging.info(f"Twig template used in {file}.")
                    except IOError as e:
                        self.analyzer.results["errors"].append(f"Error reading Twig file {file}: {e}")
                        logging.error(f"Error reading Twig file {file}: {e}")
