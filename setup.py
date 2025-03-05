from setuptools import setup, find_packages

setup(
    name="wordpress_theme_analyzer",
    version="1.0.0",
    author="Sajjad Akbari",
    author_email="sajjad@seokar.click",
    description="A tool to analyze WordPress themes for security, performance, SEO, and code quality issues.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sajjadakbari/wordpress-theme-analyzer",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.9.3",
        "pdfkit==1.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
