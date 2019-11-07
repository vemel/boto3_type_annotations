from typing import Dict
from typing import IO
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def abort_multipart_upload(
        self,
        vaultName: str,
        uploadId: str,
        accountId: Optional[str] = None,
    ):
        pass


    def abort_vault_lock(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ):
        pass


    def add_tags_to_vault(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def complete_multipart_upload(
        self,
        vaultName: str,
        uploadId: str,
        accountId: Optional[str] = None,
        archiveSize: Optional[str] = None,
        checksum: Optional[str] = None,
    ) -> Dict:
        pass


    def complete_vault_lock(
        self,
        vaultName: str,
        lockId: str,
        accountId: Optional[str] = None,
    ):
        pass


    def create_vault(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_archive(
        self,
        vaultName: str,
        archiveId: str,
        accountId: Optional[str] = None,
    ):
        pass


    def delete_vault(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ):
        pass


    def delete_vault_access_policy(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ):
        pass


    def delete_vault_notifications(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ):
        pass


    def describe_job(
        self,
        vaultName: str,
        jobId: str,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_vault(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_data_retrieval_policy(
        self,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_job_output(
        self,
        vaultName: str,
        jobId: str,
        accountId: Optional[str] = None,
        range: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_vault_access_policy(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_vault_lock(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_vault_notifications(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def initiate_job(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        jobParameters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def initiate_multipart_upload(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        archiveDescription: Optional[str] = None,
        partSize: Optional[str] = None,
    ) -> Dict:
        pass


    def initiate_vault_lock(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        policy: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_jobs(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        limit: Optional[str] = None,
        marker: Optional[str] = None,
        statuscode: Optional[str] = None,
        completed: Optional[str] = None,
    ) -> Dict:
        pass


    def list_multipart_uploads(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        marker: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict:
        pass


    def list_parts(
        self,
        vaultName: str,
        uploadId: str,
        accountId: Optional[str] = None,
        marker: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict:
        pass


    def list_provisioned_capacity(
        self,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_vault(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_vaults(
        self,
        accountId: Optional[str] = None,
        marker: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict:
        pass


    def purchase_provisioned_capacity(
        self,
        accountId: Optional[str] = None,
    ) -> Dict:
        pass


    def remove_tags_from_vault(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        TagKeys: Optional[List] = None,
    ):
        pass


    def set_data_retrieval_policy(
        self,
        accountId: Optional[str] = None,
        Policy: Optional[Dict] = None,
    ):
        pass


    def set_vault_access_policy(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        policy: Optional[Dict] = None,
    ):
        pass


    def set_vault_notifications(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        vaultNotificationConfig: Optional[Dict] = None,
    ):
        pass


    def upload_archive(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        archiveDescription: Optional[str] = None,
        checksum: Optional[str] = None,
        body: Optional[Union[bytes, IO]] = None,
    ) -> Dict:
        pass


    def upload_multipart_part(
        self,
        vaultName: str,
        uploadId: str,
        accountId: Optional[str] = None,
        checksum: Optional[str] = None,
        range: Optional[str] = None,
        body: Optional[Union[bytes, IO]] = None,
    ) -> Dict:
        pass

