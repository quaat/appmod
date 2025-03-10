# setup.py
from setuptools import setup, find_packages

setup(
    name="appmod",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    author="Thomas F. Hagelien",
    description="A short description of your package",
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/quaat/appmod",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',  # Minimum Python version required
)