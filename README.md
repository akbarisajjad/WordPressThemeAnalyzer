
# WordPress Theme Analyzer

![GitHub](https://img.shields.io/github/license/sajjadakbari/wordpress-theme-analyzer)
![GitHub stars](https://img.shields.io/github/stars/sajjadakbari/wordpress-theme-analyzer)
![GitHub issues](https://img.shields.io/github/issues/sajjadakbari/wordpress-theme-analyzer)
![GitHub pull requests](https://img.shields.io/github/issues-pr/sajjadakbari/wordpress-theme-analyzer)
![GitHub contributors](https://img.shields.io/github/contributors/sajjadakbari/wordpress-theme-analyzer)

## 📝 Overview
**WordPress Theme Analyzer** is a powerful tool designed to analyze WordPress themes for **security**, **performance**, **SEO**, and **code quality** issues. It supports multiple file types, including PHP, JavaScript, CSS, TypeScript, SCSS, React, Vue, Tailwind CSS, Alpine.js, Blade, Twig, Markdown, YAML, JSON, and XML.

This tool is developed by **Sajjad Akbari** from **SEO Kar** (https://seokar.click) and is intended to help developers and website owners ensure their WordPress themes are optimized, secure, and follow best practices.

---

## 🚀 Features
- **Security Analysis**: Detects dangerous functions (e.g., `eval`, `exec`) and vulnerabilities (e.g., XSS, SQL Injection).
- **Performance Analysis**: Identifies large files, unoptimized queries, and performance bottlenecks.
- **SEO Analysis**: Checks for missing meta tags (e.g., description, keywords) in the theme.
- **Code Quality Analysis**: Analyzes JavaScript, CSS, TypeScript, SCSS, React, Vue, Tailwind CSS, Alpine.js, Blade, Twig, Markdown, YAML, JSON, and XML files.
- **Reporting**: Generates detailed reports in JSON and PDF formats.
- **User-Friendly UI**: A graphical user interface (GUI) for easy interaction.
- **Multilingual Support**: Supports multiple languages using `gettext`.

---

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- wkhtmltopdf (for PDF report generation)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sajjadakbari/wordpress-theme-analyzer.git
   cd wordpress-theme-analyzer
---

### **فایل `README.md` کامل و جامع:**

```markdown
# WordPress Theme Analyzer

![GitHub](https://img.shields.io/github/license/sajjadakbari/wordpress-theme-analyzer)
![GitHub stars](https://img.shields.io/github/stars/sajjadakbari/wordpress-theme-analyzer)
![GitHub issues](https://img.shields.io/github/issues/sajjadakbari/wordpress-theme-analyzer)
![GitHub pull requests](https://img.shields.io/github/issues-pr/sajjadakbari/wordpress-theme-analyzer)
![GitHub contributors](https://img.shields.io/github/contributors/sajjadakbari/wordpress-theme-analyzer)

## 📝 Overview
**WordPress Theme Analyzer** is a powerful tool designed to analyze WordPress themes for **security**, **performance**, **SEO**, and **code quality** issues. It supports multiple file types, including PHP, JavaScript, CSS, TypeScript, SCSS, React, Vue, Tailwind CSS, Alpine.js, Blade, Twig, Markdown, YAML, JSON, and XML.

This tool is developed by **Sajjad Akbari** from **SEO Kar** (https://seokar.click) and is intended to help developers and website owners ensure their WordPress themes are optimized, secure, and follow best practices.

---

## 🚀 Features
- **Security Analysis**: Detects dangerous functions (e.g., `eval`, `exec`) and vulnerabilities (e.g., XSS, SQL Injection).
- **Performance Analysis**: Identifies large files, unoptimized queries, and performance bottlenecks.
- **SEO Analysis**: Checks for missing meta tags (e.g., description, keywords) in the theme.
- **Code Quality Analysis**: Analyzes JavaScript, CSS, TypeScript, SCSS, React, Vue, Tailwind CSS, Alpine.js, Blade, Twig, Markdown, YAML, JSON, and XML files.
- **Reporting**: Generates detailed reports in JSON and PDF formats.
- **User-Friendly UI**: A graphical user interface (GUI) for easy interaction.
- **Multilingual Support**: Supports multiple languages using `gettext`.

---

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- wkhtmltopdf (for PDF report generation)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sajjadakbari/wordpress-theme-analyzer.git
   cd wordpress-theme-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install wkhtmltopdf:
   - On Ubuntu:
     ```bash
     sudo apt-get install wkhtmltopdf
     ```
   - On macOS:
     ```bash
     brew install wkhtmltopdf
     ```

4. Run the analyzer:
   ```bash
   python run.py
   ```

---

## 🛠️ Usage

### Command Line Interface (CLI)
1. Navigate to the project directory.
2. Run the analyzer:
   ```bash
   python main_analyzer.py
   ```

### Graphical User Interface (GUI)
1. Run the UI:
   ```bash
   python run.py
   ```
2. Select the theme directory and click "Analyze".

---

## ⚙️ Configuration
Edit the `config.ini` file to customize settings:
```ini
[settings]
language = en  # Language for reports (en, fa, etc.)
report_format = json  # Report format (json, pdf)
max_file_size = 500000  # Maximum file size in bytes (e.g., 500 KB)
```

---

## 📂 Project Structure
```
/wordpress-theme-analyzer/
    ├── main_analyzer.py          # Core analyzer logic
    ├── plugin_analyzer.py        # Plugin analysis
    ├── child_theme_analyzer.py   # Child theme analysis
    ├── js_css_analyzer.py        # JavaScript and CSS analysis
    ├── typescript_analyzer.py    # TypeScript analysis
    ├── scss_analyzer.py          # SCSS analysis
    ├── react_analyzer.py         # React analysis
    ├── vue_analyzer.py           # Vue analysis
    ├── tailwind_analyzer.py      # Tailwind CSS analysis
    ├── alpine_analyzer.py        # Alpine.js analysis
    ├── blade_analyzer.py         # Blade template analysis
    ├── twig_analyzer.py          # Twig template analysis
    ├── markdown_analyzer.py      # Markdown analysis
    ├── yaml_analyzer.py          # YAML analysis
    ├── json_analyzer.py          # JSON analysis
    ├── xml_analyzer.py           # XML analysis
    ├── ui.py                     # Graphical user interface
    ├── config.ini                # Configuration file
    ├── test_analyzer.py          # Unit tests
    ├── README.md                 # Project documentation
    ├── requirements.txt          # Dependencies list
    ├── setup.py                  # Setup script
    └── run.py                    # Entry point for the application
```

---

## 🧪 Testing
To run the unit tests:
```bash
python -m unittest test_analyzer.py
```

---

## 🤝 Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## 📄 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact
- **Developer**: Sajjad Akbari
- **Website**: [sajjadakbari.ir](https://sajjadakbari.ir)
- **Company**: [SEO Kar](https://seokar.click)
- **Email**: sajjad@seokar.click

---

## 🙏 Acknowledgments
- Thanks to the open-source community for their invaluable contributions.
- Special thanks to [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) and [pdfkit](https://pypi.org/project/pdfkit/) for their amazing libraries.
```

---

### **فایل `LICENSE`:**

```plaintext
MIT License

Copyright (c) 2023 Sajjad Akbari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### **فایل `CONTRIBUTING.md`:**

```markdown
# Contributing to WordPress Theme Analyzer

Thank you for your interest in contributing to WordPress Theme Analyzer! Here are some guidelines to help you get started.

## How to Contribute
1. **Fork the repository**.
2. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes** with a clear and descriptive message:
   ```bash
   git commit -m "Add your feature"
   ```
4. **Push your changes** to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request** and describe your changes.

## Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Use descriptive variable and function names.
- Add comments where necessary to explain complex logic.

## Reporting Issues
If you find a bug or have a feature request, please open an issue on GitHub. Include:
- A clear description of the problem or feature.
- Steps to reproduce the issue (if applicable).
- Screenshots or error logs (if applicable).

## License
By contributing, you agree that your contributions will be licensed under the MIT License.
```

---

### **نتیجه:**
این مستندات کامل و جامع است و برای انتشار در گیت‌هاب آماده است. اگر نیاز به تغییرات یا افزودن بخش‌های دیگری دارید، خوشحال می‌شوم کمک کنم! 😊
# Contributing to WordPress Theme Analyzer

Thank you for your interest in contributing to WordPress Theme Analyzer! Here are some guidelines to help you get started.

## How to Contribute
1. **Fork the repository**.
2. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
