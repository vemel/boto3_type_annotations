"Main interface for mediatailor service"

from mypy_boto3_mediatailor.client import Client
from mypy_boto3_mediatailor.helpers import (
    boto3_client,
    get_list_playback_configurations_paginator,
)


__all__ = ("Client", "boto3_client", "get_list_playback_configurations_paginator")
