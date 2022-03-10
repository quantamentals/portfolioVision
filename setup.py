import setuptools 

setuptools.setup(
    name="portVision",
    version="0.6",
    description="Portfolio Analysis library for Cadence practice",
    homepage="#",
    author="Michael A. Ballard",
    author_email="ballard.michael@columbia.edu",
    packages=['portVision','portVision.handler','portVision.portfolio','portVision.types'],
    install_requires=[
        "requests",
        "pandas",
        "numpy",
        "pandas-datareader",
        "matplotlib",
         "scipy",
         "yfinance",
         "beautifulsoup4",
         "html5lib"

         ],
    zip_safe=False
    )
    

# python3 -m pip install -e.

# python setup.py sdist  

# twine upload dist/*  