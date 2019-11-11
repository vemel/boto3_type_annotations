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
    rm -rf build *.egg-info dist/* > /dev/null
    python setup.py build sdist bdist_wheel 1>/dev/null 2>/dev/null
    twine upload dist/* > /dev/null
    rm -rf build *.egg-info dist/* > /dev/null
done

cd ${OUTPUT_PATH}/master_package
rm -rf build *.egg-info dist/* > /dev/null
python setup.py build sdist bdist_wheel 1>/dev/null 2>/dev/null
twine upload dist/* > /dev/null
rm -rf build *.egg-info dist/* > /dev/null

cd ${OUTPUT_PATH}/boto3_stubs_package
rm -rf build *.egg-info dist/* > /dev/null
python setup.py build sdist bdist_wheel 1>/dev/null 2>/dev/null
twine upload dist/* > /dev/null
rm -rf build *.egg-info dist/* > /dev/null
