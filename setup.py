# setup.py
from setuptools import setup, find_packages

setup(
    name="appmod",  # Name of your package
    version="0.1.0",  # Initial version
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[  # Dependencies of your package
        'numpy',
        'pandas',
        # Example: 'requests',
    ],
    author="Thomas F. Hagelien",
    description="A short description of your package",
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/quaat/appmod",  # URL to the package's source code
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',  # Minimum Python version required
)