from ensurepip import version
from gettext import install
import setuptools 

setuptools.setup(
    name="portfolio_vision",
    version="0.1",
    description="Portfolio Analysis library for Cadence practice",
    homepage="#",
    author="Michael A. Ballard",
    author_email="ballard.michael@columbia.edu",
    install_requires=["requests","pandas","numpy","pandas-datareader","matplotlib", "scipy","yfinance","beautifulsoup4"],
    packages=setuptools.find_packages(include=["portVision"]),
    )
    

# python3 -m pip install -e.