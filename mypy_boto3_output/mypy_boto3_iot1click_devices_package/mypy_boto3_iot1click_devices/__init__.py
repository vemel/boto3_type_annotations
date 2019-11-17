"Main interface for iot1click-devices service"

from mypy_boto3_iot1click_devices.client import Client
from mypy_boto3_iot1click_devices.helpers import (
    boto3_client,
    get_list_device_events_paginator,
    get_list_devices_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_device_events_paginator",
    "get_list_devices_paginator",
)
