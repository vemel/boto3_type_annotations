"Main interface for license-manager service"

from mypy_boto3_license_manager.client import Client
from mypy_boto3_license_manager.helpers import (
    boto3_client,
    get_list_associations_for_license_configuration_paginator,
    get_list_license_configurations_paginator,
    get_list_license_specifications_for_resource_paginator,
    get_list_resource_inventory_paginator,
    get_list_usage_for_license_configuration_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_associations_for_license_configuration_paginator",
    "get_list_license_configurations_paginator",
    "get_list_license_specifications_for_resource_paginator",
    "get_list_resource_inventory_paginator",
    "get_list_usage_for_license_configuration_paginator",
)
