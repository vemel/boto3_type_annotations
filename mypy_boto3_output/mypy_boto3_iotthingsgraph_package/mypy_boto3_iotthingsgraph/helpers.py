"Helper functions for iotthingsgraph service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_iotthingsgraph.client import Client
from mypy_boto3_iotthingsgraph.paginator import (
    GetFlowTemplateRevisionsPaginator,
    GetSystemTemplateRevisionsPaginator,
    ListFlowExecutionMessagesPaginator,
    ListTagsForResourcePaginator,
    SearchEntitiesPaginator,
    SearchFlowExecutionsPaginator,
    SearchFlowTemplatesPaginator,
    SearchSystemInstancesPaginator,
    SearchSystemTemplatesPaginator,
    SearchThingsPaginator,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('iotthingsgraph')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("iotthingsgraph", **kwargs)
    return boto3.client("iotthingsgraph", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_flow_template_revisions_paginator(
    client: Client,
) -> GetFlowTemplateRevisionsPaginator:
    """
    Equivalent of `client.get_paginator('get_flow_template_revisions')`, returns a correct type.
    """
    return client.get_paginator("get_flow_template_revisions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_system_template_revisions_paginator(
    client: Client,
) -> GetSystemTemplateRevisionsPaginator:
    """
    Equivalent of `client.get_paginator('get_system_template_revisions')`, returns a correct type.
    """
    return client.get_paginator("get_system_template_revisions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_flow_execution_messages_paginator(
    client: Client,
) -> ListFlowExecutionMessagesPaginator:
    """
    Equivalent of `client.get_paginator('list_flow_execution_messages')`, returns a correct type.
    """
    return client.get_paginator("list_flow_execution_messages")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_for_resource_paginator(
    client: Client,
) -> ListTagsForResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_for_resource')`, returns a correct type.
    """
    return client.get_paginator("list_tags_for_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_entities_paginator(client: Client) -> SearchEntitiesPaginator:
    """
    Equivalent of `client.get_paginator('search_entities')`, returns a correct type.
    """
    return client.get_paginator("search_entities")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_flow_executions_paginator(
    client: Client,
) -> SearchFlowExecutionsPaginator:
    """
    Equivalent of `client.get_paginator('search_flow_executions')`, returns a correct type.
    """
    return client.get_paginator("search_flow_executions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_flow_templates_paginator(client: Client) -> SearchFlowTemplatesPaginator:
    """
    Equivalent of `client.get_paginator('search_flow_templates')`, returns a correct type.
    """
    return client.get_paginator("search_flow_templates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_system_instances_paginator(
    client: Client,
) -> SearchSystemInstancesPaginator:
    """
    Equivalent of `client.get_paginator('search_system_instances')`, returns a correct type.
    """
    return client.get_paginator("search_system_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_system_templates_paginator(
    client: Client,
) -> SearchSystemTemplatesPaginator:
    """
    Equivalent of `client.get_paginator('search_system_templates')`, returns a correct type.
    """
    return client.get_paginator("search_system_templates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_things_paginator(client: Client) -> SearchThingsPaginator:
    """
    Equivalent of `client.get_paginator('search_things')`, returns a correct type.
    """
    return client.get_paginator("search_things")
