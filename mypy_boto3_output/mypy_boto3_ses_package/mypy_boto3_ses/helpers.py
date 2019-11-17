"Helper functions for ses service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_ses.client import Client
from mypy_boto3_ses.paginator import (
    ListConfigurationSetsPaginator,
    ListCustomVerificationEmailTemplatesPaginator,
    ListIdentitiesPaginator,
    ListReceiptRuleSetsPaginator,
    ListTemplatesPaginator,
)
from mypy_boto3_ses.waiter import IdentityExistsWaiter

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
    Equivalent of `boto3.client('ses')`, returns a correct type.
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
        return session.client("ses", **kwargs)
    return boto3.client("ses", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_configuration_sets_paginator(
    client: Client,
) -> ListConfigurationSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_configuration_sets')`, returns a correct type.
    """
    return client.get_paginator("list_configuration_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_custom_verification_email_templates_paginator(
    client: Client,
) -> ListCustomVerificationEmailTemplatesPaginator:
    """
    Equivalent of `client.get_paginator('list_custom_verification_email_templates')`, returns a correct type.
    """
    return client.get_paginator("list_custom_verification_email_templates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_identities_paginator(client: Client) -> ListIdentitiesPaginator:
    """
    Equivalent of `client.get_paginator('list_identities')`, returns a correct type.
    """
    return client.get_paginator("list_identities")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_receipt_rule_sets_paginator(
    client: Client,
) -> ListReceiptRuleSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_receipt_rule_sets')`, returns a correct type.
    """
    return client.get_paginator("list_receipt_rule_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_templates_paginator(client: Client) -> ListTemplatesPaginator:
    """
    Equivalent of `client.get_paginator('list_templates')`, returns a correct type.
    """
    return client.get_paginator("list_templates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_identity_exists_waiter(client: Client) -> IdentityExistsWaiter:
    """
    Equivalent of `client.get_waiter('identity_exists')`, returns a correct type.
    """
    return client.get_waiter("identity_exists")
