from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="caesar",
    version="0.1.4",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'caesar = caesar.cli:main',
        ],
    },
    install_requires=[],
    author="Farhan Khan",
    author_email="ftkover9k@gmail.com",
    description="A Caesar Cipher encryption and decryption program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ftkovr9k/Caesar-Encryption-Program",
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
