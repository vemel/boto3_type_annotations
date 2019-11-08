from setuptools import setup, find_packages

from mypy_boto3.version import __version__ as version

with open("../README.md", "r") as f:
    long_description = f.read()

setup(
    name="mypy-boto3",
    version=version,
    packages=find_packages(),
    url="https://github.com/vemel/mypy_boto3",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Mypy-friendly boto3 type annotations.",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Typing :: Typed",
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"mypy_boto3": ["py.typed"]},
)
