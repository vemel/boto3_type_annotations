#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd ${ROOT_PATH}

VERSION="$1"

if [[ "$GITHUB_ACTOR" == "" ]]; then
    echo "No GITHUB_ACTOR specified"
    exit 1
fi

if [[ "$VERSION" == "" ]]; then
    echo "No version specified"
    exit 1
fi

echo "Bumping version to ${VERSION}"
echo '"Source of truth for version."' > builder/mypy_boto3_builder/version.py
echo "__version__ = \"${VERSION}\"" >> builder/mypy_boto3_builder/version.py

if [[ `git diff-index HEAD --` != "" ]]; then
    echo "There are changes: `git diff`"
    git add builder/mypy_boto3_builder/version.py
    git commit -m "Bump version to ${VERSION}"
    git tag ${VERSION}
    git push https://${GITHUB_ACTOR}:${GITHUB_TOKEN}@github.com/vemel/mypy_boto3.git --tags
    git push https://${GITHUB_ACTOR}:${GITHUB_TOKEN}@github.com/vemel/mypy_boto3.git HEAD:master
fi