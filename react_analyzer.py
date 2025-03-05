import os
import logging
from typing import Dict, List

class ReactAnalyzer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze(self) -> None:
        for root, _, files in os.walk(self.analyzer.theme_path):
            for file in files:
                if file.endswith(".jsx") or file.endswith(".tsx"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if "dangerouslySetInnerHTML" in content:
                                self.analyzer.results["security"].append(f"Use of dangerouslySetInnerHTML found in {file}.")
                                logging.warning(f"Use of dangerouslySetInnerHTML found in {file}.")
                    except IOError as e:
                        self.analyzer.results["errors"].append(f"Error reading React file {file}: {e}")
                        logging.error(f"Error reading React file {file}: {e}")
