"Helper functions for acm-pca service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_acm_pca.client import Client
from mypy_boto3_acm_pca.paginator import (
    ListCertificateAuthoritiesPaginator,
    ListPermissionsPaginator,
    ListTagsPaginator,
)
from mypy_boto3_acm_pca.waiter import (
    AuditReportCreatedWaiter,
    CertificateAuthorityCSRCreatedWaiter,
    CertificateIssuedWaiter,
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
    Equivalent of `boto3.client('acm-pca')`, returns a correct type.
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
        return session.client("acm-pca", **kwargs)
    return boto3.client("acm-pca", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_certificate_authorities_paginator(
    client: Client,
) -> ListCertificateAuthoritiesPaginator:
    """
    Equivalent of `client.get_paginator('list_certificate_authorities')`, returns a correct type.
    """
    return client.get_paginator("list_certificate_authorities")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_permissions_paginator(client: Client) -> ListPermissionsPaginator:
    """
    Equivalent of `client.get_paginator('list_permissions')`, returns a correct type.
    """
    return client.get_paginator("list_permissions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_paginator(client: Client) -> ListTagsPaginator:
    """
    Equivalent of `client.get_paginator('list_tags')`, returns a correct type.
    """
    return client.get_paginator("list_tags")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_audit_report_created_waiter(client: Client) -> AuditReportCreatedWaiter:
    """
    Equivalent of `client.get_waiter('audit_report_created')`, returns a correct type.
    """
    return client.get_waiter("audit_report_created")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_certificate_authority_csr_created_waiter(
    client: Client,
) -> CertificateAuthorityCSRCreatedWaiter:
    """
    Equivalent of `client.get_waiter('certificate_authority_csr_created')`, returns a correct type.
    """
    return client.get_waiter("certificate_authority_csr_created")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_certificate_issued_waiter(client: Client) -> CertificateIssuedWaiter:
    """
    Equivalent of `client.get_waiter('certificate_issued')`, returns a correct type.
    """
    return client.get_waiter("certificate_issued")
