from pathlib import Path

from setuptools import setup, find_packages

from mypy_boto3_builder.version import __version__ as version


ROOT_PATH = Path(__file__).absolute().parent
README_PATH = ROOT_PATH.parent / "README.md"

long_description = README_PATH.read_text()

setup(
    name="mypy-boto3-builder",
    version=version,
    packages=find_packages(),
    url="https://github.com/vemel/mypy_boto3",
    license="MIT License",
    package_data={"mypy_boto3_builder": ["mypy_boto3_builder/assets/*.template"]},
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Builder for mypy-boto3.",
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
    entry_points={
        "console_scripts": ["mypy_boto3_builder = mypy_boto3_builder.main:main"]
    },
    install_requires=["mypy>=0.740", "docstring-parser>=0.3", "boto3"],
)
