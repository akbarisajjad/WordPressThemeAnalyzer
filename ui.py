import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from main_analyzer import WordPressThemeAnalyzer

class ThemeAnalyzerUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WordPress Theme Analyzer - Developed by Sajjad Akbari (SEO Kar)")
        self.root.geometry("800x600")
        self.setup_ui()

    def setup_ui(self):
        # Header
        header = ttk.Label(self.root, text="WordPress Theme Analyzer", font=("Arial", 20))
        header.pack(pady=20)

        # Developer Info
        dev_info = ttk.Label(self.root, text="Developed by Sajjad Akbari - SEO Kar (seokar.click)", font=("Arial", 12))
        dev_info.pack(pady=10)

        # Theme Path Input
        path_frame = ttk.Frame(self.root)
        path_frame.pack(pady=10)
        ttk.Label(path_frame, text="Theme Path:").pack(side=tk.LEFT)
        self.path_entry = ttk.Entry(path_frame, width=50)
        self.path_entry.pack(side=tk.LEFT, padx=10)
        ttk.Button(path_frame, text="Browse", command=self.browse_theme_path).pack(side=tk.LEFT)

        # Analyze Button
        ttk.Button(self.root, text="Analyze", command=self.run_analysis).pack(pady=20)

        # Results Display
        self.results_text = tk.Text(self.root, wrap=tk.WORD, height=20, width=90)
        self.results_text.pack(pady=10)

    def browse_theme_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)

    def run_analysis(self):
        theme_path = self.path_entry.get()
        if not theme_path:
            messagebox.showerror("Error", "Please select a theme path.")
            return

        analyzer = WordPressThemeAnalyzer(theme_path)
        analyzer.run_analysis()

        # Display Results
        self.results_text.delete(1.0, tk.END)
        for category, issues in analyzer.results.items():
            self.results_text.insert(tk.END, f"{category.upper()}:\n")
            for issue in issues:
                self.results_text.insert(tk.END, f"- {issue}\n")
            self.results_text.insert(tk.END, "\n")

        messagebox.showinfo("Success", "Analysis completed. Reports saved in the theme directory.")

    def run(self):
        self.root.mainloop()
