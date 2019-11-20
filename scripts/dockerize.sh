#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd ${ROOT_PATH}

if [[ "$VERSION" == "" ]]; then
    echo "No VERSION specified"
    exit 1
fi

echo "Dockerizing mypy_boto3_builder ${VERSION}"
docker login docker.pkg.github.com --username vemel -p ${GITHUB_TOKEN}
docker build . --tag mypy_boto3_builder
docker tag mypy_boto3_builder docker.pkg.github.com/vemel/mypy_boto3/mypy_boto3_builder:${VERSION}
docker push docker.pkg.github.com/vemel/mypy_boto3/mypy_boto3_builder:${VERSION}
