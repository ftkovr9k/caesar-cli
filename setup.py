from setuptools import setup, find_packages

setup(
    name="caesar",  # Package name
    version="0.1",  # Version
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'caesar = caesar.cli:main',
        ],
    },
    install_requires=[],  # External dependencies (none for this case)
    author="Farhan Khan",
    author_email="ftkover9k@gmail.com",
    description="A Caesar Cipher encryption and decryption program",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ftkovr9k/Caesar-Encryption-Program",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
