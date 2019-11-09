#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output

install_package() {
    cd $1
    echo "Installing $1"
    rm -rf build __pycache__
    python setup.py develop > /dev/null
}
export -f install_package

ls -d ${OUTPUT_PATH}/$1* | xargs -I % bash -c 'install_package "%"'
