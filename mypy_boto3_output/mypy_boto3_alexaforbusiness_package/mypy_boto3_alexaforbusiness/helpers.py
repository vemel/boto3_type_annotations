"Helper functions for alexaforbusiness service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_alexaforbusiness.client import Client
from mypy_boto3_alexaforbusiness.paginator import (
    ListBusinessReportSchedulesPaginator,
    ListConferenceProvidersPaginator,
    ListDeviceEventsPaginator,
    ListSkillsPaginator,
    ListSkillsStoreCategoriesPaginator,
    ListSkillsStoreSkillsByCategoryPaginator,
    ListSmartHomeAppliancesPaginator,
    ListTagsPaginator,
    SearchDevicesPaginator,
    SearchProfilesPaginator,
    SearchRoomsPaginator,
    SearchSkillGroupsPaginator,
    SearchUsersPaginator,
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
    Equivalent of `boto3.client('alexaforbusiness')`, returns a correct type.
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
        return session.client("alexaforbusiness", **kwargs)
    return boto3.client("alexaforbusiness", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_business_report_schedules_paginator(
    client: Client,
) -> ListBusinessReportSchedulesPaginator:
    """
    Equivalent of `client.get_paginator('list_business_report_schedules')`, returns a correct type.
    """
    return client.get_paginator("list_business_report_schedules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_conference_providers_paginator(
    client: Client,
) -> ListConferenceProvidersPaginator:
    """
    Equivalent of `client.get_paginator('list_conference_providers')`, returns a correct type.
    """
    return client.get_paginator("list_conference_providers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_device_events_paginator(client: Client) -> ListDeviceEventsPaginator:
    """
    Equivalent of `client.get_paginator('list_device_events')`, returns a correct type.
    """
    return client.get_paginator("list_device_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_skills_paginator(client: Client) -> ListSkillsPaginator:
    """
    Equivalent of `client.get_paginator('list_skills')`, returns a correct type.
    """
    return client.get_paginator("list_skills")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_skills_store_categories_paginator(
    client: Client,
) -> ListSkillsStoreCategoriesPaginator:
    """
    Equivalent of `client.get_paginator('list_skills_store_categories')`, returns a correct type.
    """
    return client.get_paginator("list_skills_store_categories")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_skills_store_skills_by_category_paginator(
    client: Client,
) -> ListSkillsStoreSkillsByCategoryPaginator:
    """
    Equivalent of `client.get_paginator('list_skills_store_skills_by_category')`, returns a correct type.
    """
    return client.get_paginator("list_skills_store_skills_by_category")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_smart_home_appliances_paginator(
    client: Client,
) -> ListSmartHomeAppliancesPaginator:
    """
    Equivalent of `client.get_paginator('list_smart_home_appliances')`, returns a correct type.
    """
    return client.get_paginator("list_smart_home_appliances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_paginator(client: Client) -> ListTagsPaginator:
    """
    Equivalent of `client.get_paginator('list_tags')`, returns a correct type.
    """
    return client.get_paginator("list_tags")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_devices_paginator(client: Client) -> SearchDevicesPaginator:
    """
    Equivalent of `client.get_paginator('search_devices')`, returns a correct type.
    """
    return client.get_paginator("search_devices")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_profiles_paginator(client: Client) -> SearchProfilesPaginator:
    """
    Equivalent of `client.get_paginator('search_profiles')`, returns a correct type.
    """
    return client.get_paginator("search_profiles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_rooms_paginator(client: Client) -> SearchRoomsPaginator:
    """
    Equivalent of `client.get_paginator('search_rooms')`, returns a correct type.
    """
    return client.get_paginator("search_rooms")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_skill_groups_paginator(client: Client) -> SearchSkillGroupsPaginator:
    """
    Equivalent of `client.get_paginator('search_skill_groups')`, returns a correct type.
    """
    return client.get_paginator("search_skill_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_users_paginator(client: Client) -> SearchUsersPaginator:
    """
    Equivalent of `client.get_paginator('search_users')`, returns a correct type.
    """
    return client.get_paginator("search_users")
