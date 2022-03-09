from ensurepip import version
from gettext import install
import setuptools 

setuptools.setup(
    name="portolioVision",
    version="0.1",
    description="Portfolio Analysis library for Cadence practice",
    homepage="#",
    author="Michael A. Ballard",
    author_email="ballard.michael@columbia.edu",
    packages=setuptools.find_packages("portVision",include=["handler","portfolio","analysis"]),
    install_requires=["requests","pandas","numpy","pandas-datareader","matplotlib", "scipy","yfinance","beautifulsoup4"],
    )
    

# python3 -m pip install -e.