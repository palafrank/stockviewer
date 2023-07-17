"""Package configuration."""
from setuptools import find_packages, setup

setup(
    name="stockviewer",
    version="0.1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
          'yfinance',
          'numpy',
          'bs4',
          'pandas',
          'pytest'
      ]
    )