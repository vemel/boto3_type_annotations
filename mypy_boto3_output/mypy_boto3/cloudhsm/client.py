from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_tags_to_resource(
        self, ResourceArn: str, TagList: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_hapg(self, Label: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_hsm(
        self,
        SubnetId: str,
        SshKey: str,
        IamRoleArn: str,
        SubscriptionType: str,
        EniIp: str = None,
        ExternalId: str = None,
        ClientToken: str = None,
        SyslogIp: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_luna_client(self, Certificate: str, Label: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_hapg(self, HapgArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_hsm(self, HsmArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_luna_client(self, ClientArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_hapg(self, HapgArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_hsm(
        self, HsmArn: str = None, HsmSerialNumber: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_luna_client(
        self, ClientArn: str = None, CertificateFingerprint: str = None
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
    def get_config(
        self, ClientArn: str, ClientVersion: str, HapgList: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_available_zones(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_hapgs(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_hsms(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_luna_clients(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_hapg(
        self, HapgArn: str, Label: str = None, PartitionSerialList: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_hsm(
        self,
        HsmArn: str,
        SubnetId: str = None,
        EniIp: str = None,
        IamRoleArn: str = None,
        ExternalId: str = None,
        SyslogIp: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_luna_client(self, ClientArn: str, Certificate: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_resource(
        self, ResourceArn: str, TagKeyList: List[Any]
    ) -> Dict[str, Any]:
        pass
