#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd ${ROOT_PATH}/mypy_boto3_output

rm -rf build *.egg-info dist/*
python setup.py sdist bdist_wheel 2>&1

pipenv run twine upload dist/*

rm -rf build *.egg-info dist/*
