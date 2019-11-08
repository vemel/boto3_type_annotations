#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output

release_package() {
    cd $1
    echo $1
    rm -rf build *.egg-info dist/* 2>&1 > /dev/null
    python setup.py sdist bdist_wheel 2>&1 > /dev/null
    pipenv run twine upload dist/* 2>&1 > /dev/null
    rm -rf build *.egg-info dist/* 2>&1 > /dev/null
}
export -f release_package

find ${OUTPUT_PATH} -mindepth 1 -maxdepth 1 -name 'mypy_boto3_*' -type d | xargs -n 10 bash -c 'release_package "$@"'
