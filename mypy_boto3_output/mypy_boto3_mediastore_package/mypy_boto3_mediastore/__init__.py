"Main interface for mediastore service"

from mypy_boto3_mediastore.client import Client
from mypy_boto3_mediastore.helpers import boto3_client, get_list_containers_paginator


__all__ = ("Client", "boto3_client", "get_list_containers_paginator")
