#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

# pytest --cov-report term --cov=handsdown
mypy builder/mypy_boto3_builder
pylint builder/mypy_boto3_builder

./scripts/docs.sh

cp README.md builder/mypy_boto3_builder/templates/boto3-stubs/README.md.jinja2
cp README.md builder/mypy_boto3_builder/templates/master/README.md.jinja2
