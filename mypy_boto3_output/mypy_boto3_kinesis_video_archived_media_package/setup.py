from setuptools import setup


LONG_DESCRIPTION = """
See [mypy_boto3](https://pypi.org/project/mypy-boto3/) for more info.
"""


setup(
    name="mypy-boto3-kinesis-video-archived-media",
    version="0.2.2",
    packages=["mypy_boto3_kinesis_video_archived_media"],
    url="https://github.com/vemel/mypy_boto3",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Mypy-friendly boto3 1.10.18 type annotations for kinesis-video-archived-media service.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
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
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"mypy_boto3_kinesis_video_archived_media": ["py.typed"]},
    zip_safe=False,
)
