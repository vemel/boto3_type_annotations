"Helper functions for lex-models service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_lex_models.client import Client
from mypy_boto3_lex_models.paginator import (
    GetBotAliasesPaginator,
    GetBotChannelAssociationsPaginator,
    GetBotVersionsPaginator,
    GetBotsPaginator,
    GetBuiltinIntentsPaginator,
    GetBuiltinSlotTypesPaginator,
    GetIntentVersionsPaginator,
    GetIntentsPaginator,
    GetSlotTypeVersionsPaginator,
    GetSlotTypesPaginator,
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
    Equivalent of `boto3.client('lex-models')`, returns a correct type.
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
        return session.client("lex-models", **kwargs)
    return boto3.client("lex-models", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_bot_aliases_paginator(client: Client) -> GetBotAliasesPaginator:
    """
    Equivalent of `client.get_paginator('get_bot_aliases')`, returns a correct type.
    """
    return client.get_paginator("get_bot_aliases")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_bot_channel_associations_paginator(
    client: Client,
) -> GetBotChannelAssociationsPaginator:
    """
    Equivalent of `client.get_paginator('get_bot_channel_associations')`, returns a correct type.
    """
    return client.get_paginator("get_bot_channel_associations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_bot_versions_paginator(client: Client) -> GetBotVersionsPaginator:
    """
    Equivalent of `client.get_paginator('get_bot_versions')`, returns a correct type.
    """
    return client.get_paginator("get_bot_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_bots_paginator(client: Client) -> GetBotsPaginator:
    """
    Equivalent of `client.get_paginator('get_bots')`, returns a correct type.
    """
    return client.get_paginator("get_bots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_builtin_intents_paginator(client: Client) -> GetBuiltinIntentsPaginator:
    """
    Equivalent of `client.get_paginator('get_builtin_intents')`, returns a correct type.
    """
    return client.get_paginator("get_builtin_intents")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_builtin_slot_types_paginator(
    client: Client,
) -> GetBuiltinSlotTypesPaginator:
    """
    Equivalent of `client.get_paginator('get_builtin_slot_types')`, returns a correct type.
    """
    return client.get_paginator("get_builtin_slot_types")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_intent_versions_paginator(client: Client) -> GetIntentVersionsPaginator:
    """
    Equivalent of `client.get_paginator('get_intent_versions')`, returns a correct type.
    """
    return client.get_paginator("get_intent_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_intents_paginator(client: Client) -> GetIntentsPaginator:
    """
    Equivalent of `client.get_paginator('get_intents')`, returns a correct type.
    """
    return client.get_paginator("get_intents")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_slot_type_versions_paginator(
    client: Client,
) -> GetSlotTypeVersionsPaginator:
    """
    Equivalent of `client.get_paginator('get_slot_type_versions')`, returns a correct type.
    """
    return client.get_paginator("get_slot_type_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_slot_types_paginator(client: Client) -> GetSlotTypesPaginator:
    """
    Equivalent of `client.get_paginator('get_slot_types')`, returns a correct type.
    """
    return client.get_paginator("get_slot_types")
