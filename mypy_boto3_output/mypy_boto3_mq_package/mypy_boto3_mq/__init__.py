"Main interface for mq service"

from mypy_boto3_mq.client import Client
from mypy_boto3_mq.helpers import boto3_client, get_list_brokers_paginator


__all__ = ("Client", "boto3_client", "get_list_brokers_paginator")
