"Main interface for appmesh service"

from mypy_boto3_appmesh.client import Client
from mypy_boto3_appmesh.helpers import (
    boto3_client,
    get_list_meshes_paginator,
    get_list_routes_paginator,
    get_list_tags_for_resource_paginator,
    get_list_virtual_nodes_paginator,
    get_list_virtual_routers_paginator,
    get_list_virtual_services_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_meshes_paginator",
    "get_list_routes_paginator",
    "get_list_tags_for_resource_paginator",
    "get_list_virtual_nodes_paginator",
    "get_list_virtual_routers_paginator",
    "get_list_virtual_services_paginator",
)
