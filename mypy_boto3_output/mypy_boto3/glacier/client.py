from __future__ import annotations

from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Union

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def abort_multipart_upload(
        self, vaultName: str, uploadId: str, accountId: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def abort_vault_lock(self, vaultName: str, accountId: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def add_tags_to_vault(
        self, vaultName: str, accountId: str = None, Tags: Dict[str, Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def complete_multipart_upload(
        self,
        vaultName: str,
        uploadId: str,
        accountId: str = None,
        archiveSize: str = None,
        checksum: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def complete_vault_lock(
        self, vaultName: str, lockId: str, accountId: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_vault(self, vaultName: str, accountId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_archive(
        self, vaultName: str, archiveId: str, accountId: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_vault(self, vaultName: str, accountId: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_vault_access_policy(self, vaultName: str, accountId: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_vault_notifications(self, vaultName: str, accountId: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_job(
        self, vaultName: str, jobId: str, accountId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_vault(self, vaultName: str, accountId: str = None) -> Dict[str, Any]:
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
    def get_data_retrieval_policy(self, accountId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job_output(
        self, vaultName: str, jobId: str, accountId: str = None, range: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_vault_access_policy(
        self, vaultName: str, accountId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_vault_lock(self, vaultName: str, accountId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_vault_notifications(
        self, vaultName: str, accountId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def initiate_job(
        self,
        vaultName: str,
        accountId: str = None,
        jobParameters: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def initiate_multipart_upload(
        self,
        vaultName: str,
        accountId: str = None,
        archiveDescription: str = None,
        partSize: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def initiate_vault_lock(
        self, vaultName: str, accountId: str = None, policy: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self,
        vaultName: str,
        accountId: str = None,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_multipart_uploads(
        self,
        vaultName: str,
        accountId: str = None,
        marker: str = None,
        limit: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_parts(
        self,
        vaultName: str,
        uploadId: str,
        accountId: str = None,
        marker: str = None,
        limit: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_provisioned_capacity(self, accountId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_vault(
        self, vaultName: str, accountId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_vaults(
        self, accountId: str = None, marker: str = None, limit: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def purchase_provisioned_capacity(self, accountId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_vault(
        self, vaultName: str, accountId: str = None, TagKeys: List[Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_data_retrieval_policy(
        self, accountId: str = None, Policy: Dict[str, Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_vault_access_policy(
        self, vaultName: str, accountId: str = None, policy: Dict[str, Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_vault_notifications(
        self,
        vaultName: str,
        accountId: str = None,
        vaultNotificationConfig: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def upload_archive(
        self,
        vaultName: str,
        accountId: str = None,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def upload_multipart_part(
        self,
        vaultName: str,
        uploadId: str,
        accountId: str = None,
        checksum: str = None,
        range: str = None,
        body: Union[bytes, IO] = None,
    ) -> Dict[str, Any]:
        pass
