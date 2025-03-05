import os
import logging
from typing import Dict, List

class TypeScriptAnalyzer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze(self) -> None:
        for root, _, files in os.walk(self.analyzer.theme_path):
            for file in files:
                if file.endswith(".ts"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if "any" in content:
                                self.analyzer.results["warnings"].append(f"Use of 'any' type found in {file}.")
                                logging.warning(f"Use of 'any' type found in {file}.")
                    except IOError as e:
                        self.analyzer.results["errors"].append(f"Error reading TypeScript file {file}: {e}")
                        logging.error(f"Error reading TypeScript file {file}: {e}")
