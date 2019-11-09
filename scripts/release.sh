#!/usr/bin/env bash

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output

release_package() {
    cd $1
    echo "Releasing $1"

    rm -rf build *.egg-info dist/* > /dev/null
    python setup.py build sdist bdist_wheel 1>/dev/null 2>/dev/null
    twine upload dist/* > /dev/null
    rm -rf build *.egg-info dist/* > /dev/null
}
export -f release_package

ls -d ${OUTPUT_PATH}/mypy_boto3_$1* | xargs -I % -P 10 bash -c 'release_package "%"'
