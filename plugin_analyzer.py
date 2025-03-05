import os
import logging
from typing import Dict, List

class PluginAnalyzer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze(self) -> None:
        plugins_path = os.path.join(self.analyzer.theme_path, "plugins")
        if not os.path.exists(plugins_path):
            self.analyzer.results["info"].append("No plugins directory found.")
            logging.info("No plugins directory found.")
            return

        for root, _, files in os.walk(plugins_path):
            for file in files:
                if file.endswith(".php"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            dangerous_functions = ["eval", "exec", "shell_exec", "system", "passthru", "popen"]
                            for func in dangerous_functions:
                                if func in content:
                                    self.analyzer.results["security"].append(f"Dangerous function {func} found in plugin {file}.")
                                    logging.warning(f"Dangerous function {func} found in plugin {file}.")
                            deprecated_functions = ["mysql_", "ereg_", "split"]
                            for func in deprecated_functions:
                                if func in content:
                                    self.analyzer.results["warnings"].append(f"Deprecated function {func} found in plugin {file}.")
                                    logging.warning(f"Deprecated function {func} found in plugin {file}.")
                    except IOError as e:
                        self.analyzer.results["errors"].append(f"Error reading plugin file {file}: {e}")
                        logging.error(f"Error reading plugin file {file}: {e}")
