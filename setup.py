from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A Python package for creating a unique file name within a directory'
LONG_DESCRIPTION = 'A Python package which will check that a proposed file path would be unique. If not unique, it will make it unique by concatenating a hyphen and integer. Handy to avoid overwriting files.'

setup(
    name="curlywaffle",
    version=VERSION,
    author="notteddydev",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'curlywaffle']
)