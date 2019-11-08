from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_tags(self, ARN: str, TagList: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_elasticsearch_domain(
        self,
        DomainName: str,
        ElasticsearchVersion: str = None,
        ElasticsearchClusterConfig: Dict[str, Any] = None,
        EBSOptions: Dict[str, Any] = None,
        AccessPolicies: str = None,
        SnapshotOptions: Dict[str, Any] = None,
        VPCOptions: Dict[str, Any] = None,
        CognitoOptions: Dict[str, Any] = None,
        EncryptionAtRestOptions: Dict[str, Any] = None,
        NodeToNodeEncryptionOptions: Dict[str, Any] = None,
        AdvancedOptions: Dict[str, Any] = None,
        LogPublishingOptions: Dict[str, Any] = None,
        DomainEndpointOptions: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_elasticsearch_domain(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_elasticsearch_service_role(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_elasticsearch_domain(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_elasticsearch_domain_config(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_elasticsearch_domains(self, DomainNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_elasticsearch_instance_type_limits(
        self, InstanceType: str, ElasticsearchVersion: str, DomainName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_reserved_elasticsearch_instance_offerings(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_reserved_elasticsearch_instances(
        self,
        ReservedElasticsearchInstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_compatible_elasticsearch_versions(
        self, DomainName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_upgrade_history(
        self, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_upgrade_status(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_domain_names(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_elasticsearch_instance_types(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_elasticsearch_versions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags(self, ARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def purchase_reserved_elasticsearch_instance_offering(
        self,
        ReservedElasticsearchInstanceOfferingId: str,
        ReservationName: str,
        InstanceCount: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags(self, ARN: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def start_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_elasticsearch_domain_config(
        self,
        DomainName: str,
        ElasticsearchClusterConfig: Dict[str, Any] = None,
        EBSOptions: Dict[str, Any] = None,
        SnapshotOptions: Dict[str, Any] = None,
        VPCOptions: Dict[str, Any] = None,
        CognitoOptions: Dict[str, Any] = None,
        AdvancedOptions: Dict[str, Any] = None,
        AccessPolicies: str = None,
        LogPublishingOptions: Dict[str, Any] = None,
        DomainEndpointOptions: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def upgrade_elasticsearch_domain(
        self, DomainName: str, TargetVersion: str, PerformCheckOnly: bool = None
    ) -> Dict[str, Any]:
        pass
