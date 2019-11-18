#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output
PACKAGES=${OUTPUT_PATH}/mypy_boto3_$1_package
if [[ "$1" == "" ]]; then
    PACKAGES=${OUTPUT_PATH}/mypy_boto3_*
fi

for package in $PACKAGES
do
    echo Installing $(basename ${package})
    cd ${package}
    python setup.py install 1>/dev/null 2>/dev/null
done

echo Installing master package
cd ${OUTPUT_PATH}/master_package
python setup.py install 1>/dev/null 2>/dev/null

echo Installing boto3-stubs package
cd ${OUTPUT_PATH}/boto3_stubs_package
python setup.py install 1>/dev/null 2>/dev/null
