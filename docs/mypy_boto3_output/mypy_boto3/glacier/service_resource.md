# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.glacier.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Glacier](index.md#glacier) / ServiceResource
    - [Account](#account)
        - [Account().create_vault](#accountcreate_vault)
        - [Account().get_available_subresources](#accountget_available_subresources)
    - [Archive](#archive)
        - [Archive().delete](#archivedelete)
        - [Archive().get_available_subresources](#archiveget_available_subresources)
        - [Archive().initiate_archive_retrieval](#archiveinitiate_archive_retrieval)
    - [Job](#job)
        - [Job().get_available_subresources](#jobget_available_subresources)
        - [Job().get_output](#jobget_output)
        - [Job().load](#jobload)
        - [Job().reload](#jobreload)
    - [MultipartUpload](#multipartupload)
        - [MultipartUpload().abort](#multipartuploadabort)
        - [MultipartUpload().complete](#multipartuploadcomplete)
        - [MultipartUpload().get_available_subresources](#multipartuploadget_available_subresources)
        - [MultipartUpload().parts](#multipartuploadparts)
        - [MultipartUpload().upload_part](#multipartuploadupload_part)
    - [Notification](#notification)
        - [Notification().delete](#notificationdelete)
        - [Notification().get_available_subresources](#notificationget_available_subresources)
        - [Notification().load](#notificationload)
        - [Notification().reload](#notificationreload)
        - [Notification().set](#notificationset)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().Account](#serviceresourceaccount)
        - [ServiceResource().Archive](#serviceresourcearchive)
        - [ServiceResource().Job](#serviceresourcejob)
        - [ServiceResource().MultipartUpload](#serviceresourcemultipartupload)
        - [ServiceResource().Notification](#serviceresourcenotification)
        - [ServiceResource().Vault](#serviceresourcevault)
        - [ServiceResource().create_vault](#serviceresourcecreate_vault)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
    - [Vault](#vault)
        - [Vault().create](#vaultcreate)
        - [Vault().delete](#vaultdelete)
        - [Vault().get_available_subresources](#vaultget_available_subresources)
        - [Vault().initiate_inventory_retrieval](#vaultinitiate_inventory_retrieval)
        - [Vault().initiate_multipart_upload](#vaultinitiate_multipart_upload)
        - [Vault().load](#vaultload)
        - [Vault().reload](#vaultreload)
        - [Vault().upload_archive](#vaultupload_archive)
    - [completed_jobs](#completed_jobs)
        - [completed_jobs.all](#completed_jobsall)
        - [completed_jobs.filter](#completed_jobsfilter)
        - [completed_jobs.iterator](#completed_jobsiterator)
        - [completed_jobs.limit](#completed_jobslimit)
        - [completed_jobs.page_size](#completed_jobspage_size)
        - [completed_jobs.pages](#completed_jobspages)
    - [failed_jobs](#failed_jobs)
        - [failed_jobs.all](#failed_jobsall)
        - [failed_jobs.filter](#failed_jobsfilter)
        - [failed_jobs.iterator](#failed_jobsiterator)
        - [failed_jobs.limit](#failed_jobslimit)
        - [failed_jobs.page_size](#failed_jobspage_size)
        - [failed_jobs.pages](#failed_jobspages)
    - [jobs](#jobs)
        - [jobs.all](#jobsall)
        - [jobs.filter](#jobsfilter)
        - [jobs.iterator](#jobsiterator)
        - [jobs.limit](#jobslimit)
        - [jobs.page_size](#jobspage_size)
        - [jobs.pages](#jobspages)
    - [jobs_in_progress](#jobs_in_progress)
        - [jobs_in_progress.all](#jobs_in_progressall)
        - [jobs_in_progress.filter](#jobs_in_progressfilter)
        - [jobs_in_progress.iterator](#jobs_in_progressiterator)
        - [jobs_in_progress.limit](#jobs_in_progresslimit)
        - [jobs_in_progress.page_size](#jobs_in_progresspage_size)
        - [jobs_in_progress.pages](#jobs_in_progresspages)
    - [multipart_uplaods](#multipart_uplaods)
        - [multipart_uplaods.all](#multipart_uplaodsall)
        - [multipart_uplaods.filter](#multipart_uplaodsfilter)
        - [multipart_uplaods.iterator](#multipart_uplaodsiterator)
        - [multipart_uplaods.limit](#multipart_uplaodslimit)
        - [multipart_uplaods.page_size](#multipart_uplaodspage_size)
        - [multipart_uplaods.pages](#multipart_uplaodspages)
    - [multipart_uploads](#multipart_uploads)
        - [multipart_uploads.all](#multipart_uploadsall)
        - [multipart_uploads.filter](#multipart_uploadsfilter)
        - [multipart_uploads.iterator](#multipart_uploadsiterator)
        - [multipart_uploads.limit](#multipart_uploadslimit)
        - [multipart_uploads.page_size](#multipart_uploadspage_size)
        - [multipart_uploads.pages](#multipart_uploadspages)
    - [succeeded_jobs](#succeeded_jobs)
        - [succeeded_jobs.all](#succeeded_jobsall)
        - [succeeded_jobs.filter](#succeeded_jobsfilter)
        - [succeeded_jobs.iterator](#succeeded_jobsiterator)
        - [succeeded_jobs.limit](#succeeded_jobslimit)
        - [succeeded_jobs.page_size](#succeeded_jobspage_size)
        - [succeeded_jobs.pages](#succeeded_jobspages)
    - [vaults](#vaults)
        - [vaults.all](#vaultsall)
        - [vaults.filter](#vaultsfilter)
        - [vaults.iterator](#vaultsiterator)
        - [vaults.limit](#vaultslimit)
        - [vaults.page_size](#vaultspage_size)
        - [vaults.pages](#vaultspages)

## Account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L62)

```python
class Account(Boto3ServiceResource):
```

### Account().create_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L67)

```python
def create_vault(vaultName: str) -> glacier_service_resource_scope.Vault:
```

### Account().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L71)

```python
def get_available_subresources() -> List[str]:
```

## Archive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L75)

```python
class Archive(Boto3ServiceResource):
```

### Archive().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L81)

```python
def delete() -> None:
```

### Archive().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L85)

```python
def get_available_subresources() -> List[str]:
```

### Archive().initiate_archive_retrieval

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L89)

```python
def initiate_archive_retrieval() -> glacier_service_resource_scope.Job:
```

## Job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L93)

```python
class Job(Boto3ServiceResource):
```

### Job().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L120)

```python
def get_available_subresources() -> List[str]:
```

### Job().get_output

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L124)

```python
def get_output(range: str = None) -> Dict[str, Any]:
```

### Job().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L128)

```python
def load() -> None:
```

### Job().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L132)

```python
def reload() -> None:
```

## MultipartUpload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L136)

```python
class MultipartUpload(Boto3ServiceResource):
```

### MultipartUpload().abort

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L147)

```python
def abort() -> None:
```

### MultipartUpload().complete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L151)

```python
def complete(archiveSize: str = None, checksum: str = None) -> Dict[str, Any]:
```

### MultipartUpload().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L155)

```python
def get_available_subresources() -> List[str]:
```

### MultipartUpload().parts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L159)

```python
def parts(marker: str = None, limit: str = None) -> Dict[str, Any]:
```

### MultipartUpload().upload_part

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L163)

```python
def upload_part(
    checksum: str = None,
    range: str = None,
    body: Union[bytes, IO] = None,
) -> Dict[str, Any]:
```

## Notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L169)

```python
class Notification(Boto3ServiceResource):
```

### Notification().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L176)

```python
def delete() -> None:
```

### Notification().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L180)

```python
def get_available_subresources() -> List[str]:
```

### Notification().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L184)

```python
def load() -> None:
```

### Notification().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L188)

```python
def reload() -> None:
```

### Notification().set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L192)

```python
def set(vaultNotificationConfig: Dict[str, Any] = None) -> None:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L16)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().Account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L20)

```python
def Account(id: str = None) -> glacier_service_resource_scope.Account:
```

### ServiceResource().Archive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L24)

```python
def Archive(
    account_id: str = None,
    vault_name: str = None,
    id: str = None,
) -> glacier_service_resource_scope.Archive:
```

### ServiceResource().Job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L30)

```python
def Job(
    account_id: str = None,
    vault_name: str = None,
    id: str = None,
) -> glacier_service_resource_scope.Job:
```

### ServiceResource().MultipartUpload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L36)

```python
def MultipartUpload(
    account_id: str = None,
    vault_name: str = None,
    id: str = None,
) -> glacier_service_resource_scope.MultipartUpload:
```

### ServiceResource().Notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L42)

```python
def Notification(
    account_id: str = None,
    vault_name: str = None,
) -> glacier_service_resource_scope.Notification:
```

### ServiceResource().Vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L48)

```python
def Vault(
    account_id: str = None,
    name: str = None,
) -> glacier_service_resource_scope.Vault:
```

### ServiceResource().create_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L54)

```python
def create_vault(vaultName: str) -> glacier_service_resource_scope.Vault:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L58)

```python
def get_available_subresources() -> List[str]:
```

## Vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L196)

```python
class Vault(Boto3ServiceResource):
```

### Vault().create

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L214)

```python
def create() -> Dict[str, Any]:
```

### Vault().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L218)

```python
def delete() -> None:
```

### Vault().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L222)

```python
def get_available_subresources() -> List[str]:
```

### Vault().initiate_inventory_retrieval

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L226)

```python
def initiate_inventory_retrieval() -> glacier_service_resource_scope.Job:
```

### Vault().initiate_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L230)

```python
def initiate_multipart_upload(
    archiveDescription: str = None,
    partSize: str = None,
) -> glacier_service_resource_scope.MultipartUpload:
```

### Vault().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L236)

```python
def load() -> None:
```

### Vault().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L240)

```python
def reload() -> None:
```

### Vault().upload_archive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L244)

```python
def upload_archive(
    archiveDescription: str = None,
    checksum: str = None,
    body: Union[bytes, IO] = None,
) -> glacier_service_resource_scope.Archive:
```

## completed_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L287)

```python
class completed_jobs(ResourceCollection):
```

### completed_jobs.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L288)

```python
@classmethod
def all() -> List[glacier_service_resource_scope.Job]:
```

### completed_jobs.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L293)

```python
@classmethod
def filter(
    limit: str = None,
    marker: str = None,
    statuscode: str = None,
) -> List[glacier_service_resource_scope.Job]:
```

### completed_jobs.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L300)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### completed_jobs.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L305)

```python
@classmethod
def limit(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### completed_jobs.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L310)

```python
@classmethod
def page_size(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### completed_jobs.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L315)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## failed_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L321)

```python
class failed_jobs(ResourceCollection):
```

### failed_jobs.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L322)

```python
@classmethod
def all() -> List[glacier_service_resource_scope.Job]:
```

### failed_jobs.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L327)

```python
@classmethod
def filter(
    limit: str = None,
    marker: str = None,
    completed: str = None,
) -> List[glacier_service_resource_scope.Job]:
```

### failed_jobs.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L334)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### failed_jobs.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L339)

```python
@classmethod
def limit(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### failed_jobs.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L344)

```python
@classmethod
def page_size(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### failed_jobs.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L349)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L355)

```python
class jobs(ResourceCollection):
```

### jobs.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L356)

```python
@classmethod
def all() -> List[glacier_service_resource_scope.Job]:
```

### jobs.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L361)

```python
@classmethod
def filter(
    limit: str = None,
    marker: str = None,
    statuscode: str = None,
    completed: str = None,
) -> List[glacier_service_resource_scope.Job]:
```

### jobs.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L372)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### jobs.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L377)

```python
@classmethod
def limit(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### jobs.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L382)

```python
@classmethod
def page_size(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### jobs.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L387)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## jobs_in_progress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L393)

```python
class jobs_in_progress(ResourceCollection):
```

### jobs_in_progress.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L394)

```python
@classmethod
def all() -> List[glacier_service_resource_scope.Job]:
```

### jobs_in_progress.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L399)

```python
@classmethod
def filter(
    limit: str = None,
    marker: str = None,
    completed: str = None,
) -> List[glacier_service_resource_scope.Job]:
```

### jobs_in_progress.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L406)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### jobs_in_progress.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L411)

```python
@classmethod
def limit(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### jobs_in_progress.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L416)

```python
@classmethod
def page_size(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### jobs_in_progress.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L421)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## multipart_uplaods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L427)

```python
class multipart_uplaods(ResourceCollection):
```

### multipart_uplaods.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L428)

```python
@classmethod
def all() -> List[glacier_service_resource_scope.MultipartUpload]:
```

### multipart_uplaods.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L433)

```python
@classmethod
def filter(
    marker: str = None,
    limit: str = None,
) -> List[glacier_service_resource_scope.MultipartUpload]:
```

### multipart_uplaods.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L440)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### multipart_uplaods.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L445)

```python
@classmethod
def limit(
    count: int = None,
) -> List[glacier_service_resource_scope.MultipartUpload]:
```

### multipart_uplaods.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L452)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[glacier_service_resource_scope.MultipartUpload]:
```

### multipart_uplaods.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L459)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## multipart_uploads

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L465)

```python
class multipart_uploads(ResourceCollection):
```

### multipart_uploads.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L466)

```python
@classmethod
def all() -> List[glacier_service_resource_scope.MultipartUpload]:
```

### multipart_uploads.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L471)

```python
@classmethod
def filter(
    marker: str = None,
    limit: str = None,
) -> List[glacier_service_resource_scope.MultipartUpload]:
```

### multipart_uploads.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L478)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### multipart_uploads.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L483)

```python
@classmethod
def limit(
    count: int = None,
) -> List[glacier_service_resource_scope.MultipartUpload]:
```

### multipart_uploads.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L490)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[glacier_service_resource_scope.MultipartUpload]:
```

### multipart_uploads.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L497)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## succeeded_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L503)

```python
class succeeded_jobs(ResourceCollection):
```

### succeeded_jobs.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L504)

```python
@classmethod
def all() -> List[glacier_service_resource_scope.Job]:
```

### succeeded_jobs.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L509)

```python
@classmethod
def filter(
    limit: str = None,
    marker: str = None,
    completed: str = None,
) -> List[glacier_service_resource_scope.Job]:
```

### succeeded_jobs.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L516)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### succeeded_jobs.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L521)

```python
@classmethod
def limit(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### succeeded_jobs.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L526)

```python
@classmethod
def page_size(count: int = None) -> List[glacier_service_resource_scope.Job]:
```

### succeeded_jobs.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L531)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## vaults

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L253)

```python
class vaults(ResourceCollection):
```

### vaults.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L254)

```python
@classmethod
def all() -> List[glacier_service_resource_scope.Vault]:
```

### vaults.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L259)

```python
@classmethod
def filter(
    marker: str = None,
    limit: str = None,
) -> List[glacier_service_resource_scope.Vault]:
```

### vaults.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L266)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### vaults.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L271)

```python
@classmethod
def limit(count: int = None) -> List[glacier_service_resource_scope.Vault]:
```

### vaults.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L276)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[glacier_service_resource_scope.Vault]:
```

### vaults.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/service_resource.py#L281)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
