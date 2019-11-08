from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_delete_attributes(self, DomainName: str, Items: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def batch_put_attributes(self, DomainName: str, Items: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_domain(self, DomainName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_attributes(
        self,
        DomainName: str,
        ItemName: str,
        Attributes: List[Any] = None,
        Expected: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_domain(self, DomainName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def domain_metadata(self, DomainName: str) -> Dict[str, Any]:
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
    def get_attributes(
        self,
        DomainName: str,
        ItemName: str,
        AttributeNames: List[Any] = None,
        ConsistentRead: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_domains(
        self, MaxNumberOfDomains: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_attributes(
        self,
        DomainName: str,
        ItemName: str,
        Attributes: List[Any],
        Expected: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def select(
        self, SelectExpression: str, NextToken: str = None, ConsistentRead: bool = None
    ) -> Dict[str, Any]:
        pass
