import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="whoissearch",
    version="0.1.0",
    author="Guzman Cernadas Perez",
    author_email="guzman.cernadas@protonmail.com",
    description="Get network blocks from whois from a list of words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hackliza/WhoisSearch",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "whoissearch = whoissearch.main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
