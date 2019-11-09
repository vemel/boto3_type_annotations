#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd ${ROOT_PATH}

mypy_boto3_builder mypy_boto3_output -f --skip-master $@
mypy_boto3_builder mypy_boto3_output -f --skip-services

# mypy mypy_boto3_output/mypy_boto3_package
