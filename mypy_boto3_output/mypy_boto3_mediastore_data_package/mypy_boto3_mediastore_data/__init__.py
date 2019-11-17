"Main interface for mediastore-data service"

from mypy_boto3_mediastore_data.client import Client
from mypy_boto3_mediastore_data.helpers import boto3_client, get_list_items_paginator


__all__ = ("Client", "boto3_client", "get_list_items_paginator")
