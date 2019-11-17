"Main interface for groundstation service"

from mypy_boto3_groundstation.client import Client
from mypy_boto3_groundstation.helpers import (
    boto3_client,
    get_list_configs_paginator,
    get_list_contacts_paginator,
    get_list_dataflow_endpoint_groups_paginator,
    get_list_ground_stations_paginator,
    get_list_mission_profiles_paginator,
    get_list_satellites_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_configs_paginator",
    "get_list_contacts_paginator",
    "get_list_dataflow_endpoint_groups_paginator",
    "get_list_ground_stations_paginator",
    "get_list_mission_profiles_paginator",
    "get_list_satellites_paginator",
)
