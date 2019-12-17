#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

vulture builder/mypy_boto3_builder vulture_whitelist.txt
mypy builder/mypy_boto3_builder
pylint builder/mypy_boto3_builder
pytest

./scripts/docs.sh
