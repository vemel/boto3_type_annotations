#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output

install_package() {
    cd $1
    python setup.py develop
}
export -f install_package

find ${OUTPUT_PATH} -mindepth 1 -maxdepth 1 -name 'mypy_boto3_*' -type d -exec bash -c 'install_package "$@"' bash {} \;
