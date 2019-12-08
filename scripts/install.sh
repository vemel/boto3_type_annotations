#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output
PACKAGES=${OUTPUT_PATH}/mypy_boto3_$1_package
if [[ "$1" == "" ]]; then
    PACKAGES=${OUTPUT_PATH}/mypy_boto3_*
fi

if [[ "$1" == "master" ]]; then
    echo Installing master package
    cd ${OUTPUT_PATH}/master_package
    python -m pip install .

    echo Installing boto3-stubs package
    cd ${OUTPUT_PATH}/boto3_stubs_package
    python -m pip install .[master]
    python -m mypy_boto3
    exit
fi

for package in $PACKAGES
do
    echo Installing $(basename ${package})
    cd ${package}
    python -m pip install .
done

python -m mypy_boto3
