#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output

uninstall_package() {
    cd $1
    echo "Uninstalling $1"

    python setup.py develop -u > /dev/null
}
export -f uninstall_package

ls -d ${OUTPUT_PATH}/mypy_boto3_$1* | xargs -I % bash -c 'uninstall_package "%"'
