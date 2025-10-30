from setuptools import setup, find_packages
import os

setup(
    name="ai_phishing_detector",   # The name of your Python package
    version="1.0.0",               # Initial version of the package
    packages=find_packages(),
    include_package_data=True,
    data_files=[('phishing_detector/model', ['model/phishing_model.pkl'])],
    install_requires=[
        "scikit-learn",
        "joblib",
        "tldextract",
    ],
    entry_points={
        "console_scripts": [
            "phishing-detector=cli_tool.cli:main",
        ],
    },
)