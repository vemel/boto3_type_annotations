from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_ledger(
        self,
        Name: str,
        PermissionsMode: str,
        Tags: Dict[str, Any] = None,
        DeletionProtection: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_ledger(self, Name: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_journal_s3_export(self, Name: str, ExportId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_ledger(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def export_journal_to_s3(
        self,
        Name: str,
        InclusiveStartTime: datetime,
        ExclusiveEndTime: datetime,
        S3ExportConfiguration: Dict[str, Any],
        RoleArn: str,
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
    def get_block(
        self,
        Name: str,
        BlockAddress: Dict[str, Any],
        DigestTipAddress: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_digest(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_revision(
        self,
        Name: str,
        BlockAddress: Dict[str, Any],
        DocumentId: str,
        DigestTipAddress: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_journal_s3_exports(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_journal_s3_exports_for_ledger(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_ledgers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_ledger(
        self, Name: str, DeletionProtection: bool = None
    ) -> Dict[str, Any]:
        pass
