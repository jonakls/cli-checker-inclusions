from setuptools import setup, find_packages

setup(
    name='radix-organizer',
    version='2.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'openpyxl',
        'xlrd'
    ],
    author='Jonathan Narvaez',
    author_email='asmot54@gmail.com'
)
