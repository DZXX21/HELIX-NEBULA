from setuptools import setup, find_packages

setup(
    name="thehackernews-summarizer",
    version="1.0.0",
    description="The Hacker News haberlerini özetleyen bir araç",
    author="Tahas",
    packages=find_packages(),
    install_requires=["requests", "beautifulsoup4", "google-generativeai"],
)