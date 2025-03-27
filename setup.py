from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'A simple tool to declutter and organize your files.'
LONG_DESCRIPTION = 'FileTidy helps you sort and clean up your messy folders by automatically categorizing files.'

setup(
        name="FileScape", 
        version=VERSION,
        author="Rodrigo Tallar",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        url='https://github.com/rtallarr/FileScape',
        install_requires=[],
        keywords=['files', 'sort', 'organize'],
        classifiers= [
            "Programming Language :: Python :: 3",
        ]
)