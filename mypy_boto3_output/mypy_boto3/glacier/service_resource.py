from __future__ import annotations

from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Union

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3.glacier.service_resource as glacier_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    vaults: glacier_service_resource_scope.vaults

    # pylint: disable=arguments-differ
    def Account(self, id: str = None) -> glacier_service_resource_scope.Account:
        pass

    # pylint: disable=arguments-differ
    def Archive(
        self, account_id: str = None, vault_name: str = None, id: str = None
    ) -> glacier_service_resource_scope.Archive:
        pass

    # pylint: disable=arguments-differ
    def Job(
        self, account_id: str = None, vault_name: str = None, id: str = None
    ) -> glacier_service_resource_scope.Job:
        pass

    # pylint: disable=arguments-differ
    def MultipartUpload(
        self, account_id: str = None, vault_name: str = None, id: str = None
    ) -> glacier_service_resource_scope.MultipartUpload:
        pass

    # pylint: disable=arguments-differ
    def Notification(
        self, account_id: str = None, vault_name: str = None
    ) -> glacier_service_resource_scope.Notification:
        pass

    # pylint: disable=arguments-differ
    def Vault(
        self, account_id: str = None, name: str = None
    ) -> glacier_service_resource_scope.Vault:
        pass

    # pylint: disable=arguments-differ
    def create_vault(self, vaultName: str) -> glacier_service_resource_scope.Vault:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Account(Boto3ServiceResource):
    id: str
    vaults: glacier_service_resource_scope.vaults

    # pylint: disable=arguments-differ
    def create_vault(self, vaultName: str) -> glacier_service_resource_scope.Vault:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Archive(Boto3ServiceResource):
    account_id: str
    vault_name: str
    id: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def initiate_archive_retrieval(self) -> glacier_service_resource_scope.Job:
        pass


class Job(Boto3ServiceResource):
    job_id: str
    job_description: str
    action: str
    archive_id: str
    vault_arn: str
    creation_date: str
    completed: bool
    status_code: str
    status_message: str
    archive_size_in_bytes: int
    inventory_size_in_bytes: int
    sns_topic: str
    completion_date: str
    sha256_tree_hash: str
    archive_sha256_tree_hash: str
    retrieval_byte_range: str
    tier: str
    inventory_retrieval_parameters: Dict
    job_output_path: str
    select_parameters: Dict
    output_location: Dict
    account_id: str
    vault_name: str
    id: str

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def get_output(self, range: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class MultipartUpload(Boto3ServiceResource):
    multipart_upload_id: str
    vault_arn: str
    archive_description: str
    part_size_in_bytes: int
    creation_date: str
    account_id: str
    vault_name: str
    id: str

    # pylint: disable=arguments-differ
    def abort(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def complete(self, archiveSize: str = None, checksum: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def parts(self, marker: str = None, limit: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def upload_part(
        self, checksum: str = None, range: str = None, body: Union[bytes, IO] = None
    ) -> Dict[str, Any]:
        pass


class Notification(Boto3ServiceResource):
    sns_topic: str
    events: List
    account_id: str
    vault_name: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def set(self, vaultNotificationConfig: Dict[str, Any] = None) -> None:
        pass


class Vault(Boto3ServiceResource):
    vault_arn: str
    vault_name: str
    creation_date: str
    last_inventory_date: str
    number_of_archives: int
    size_in_bytes: int
    account_id: str
    name: str
    completed_jobs: glacier_service_resource_scope.completed_jobs
    failed_jobs: glacier_service_resource_scope.failed_jobs
    jobs: glacier_service_resource_scope.jobs
    jobs_in_progress: glacier_service_resource_scope.jobs_in_progress
    multipart_uplaods: glacier_service_resource_scope.multipart_uplaods
    multipart_uploads: glacier_service_resource_scope.multipart_uploads
    succeeded_jobs: glacier_service_resource_scope.succeeded_jobs

    # pylint: disable=arguments-differ
    def create(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def initiate_inventory_retrieval(self) -> glacier_service_resource_scope.Job:
        pass

    # pylint: disable=arguments-differ
    def initiate_multipart_upload(
        self, archiveDescription: str = None, partSize: str = None
    ) -> glacier_service_resource_scope.MultipartUpload:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def upload_archive(
        self,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO] = None,
    ) -> glacier_service_resource_scope.Archive:
        pass


class vaults(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[glacier_service_resource_scope.Vault]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, marker: str = None, limit: str = None
    ) -> List[glacier_service_resource_scope.Vault]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[glacier_service_resource_scope.Vault]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[glacier_service_resource_scope.Vault]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class completed_jobs(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, limit: str = None, marker: str = None, statuscode: str = None
    ) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class failed_jobs(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, limit: str = None, marker: str = None, completed: str = None
    ) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class jobs(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class jobs_in_progress(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, limit: str = None, marker: str = None, completed: str = None
    ) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class multipart_uplaods(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[glacier_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, marker: str = None, limit: str = None
    ) -> List[glacier_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[glacier_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[glacier_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class multipart_uploads(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[glacier_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, marker: str = None, limit: str = None
    ) -> List[glacier_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[glacier_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[glacier_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class succeeded_jobs(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, limit: str = None, marker: str = None, completed: str = None
    ) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[glacier_service_resource_scope.Job]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
