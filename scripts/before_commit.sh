#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

mypy builder/mypy_boto3_builder
pylint builder/mypy_boto3_builder
pytest

./scripts/docs.sh
