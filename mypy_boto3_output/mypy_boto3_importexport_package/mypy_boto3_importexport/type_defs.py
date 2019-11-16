"Main interface for importexport type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCancelJobResponseTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientGetShippingLabelResponseTypeDef",
    "ClientGetStatusResponseTypeDef",
    "ClientListJobsResponseJobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientUpdateJobResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponseJobsTypeDef",
    "ListJobsPaginateResponseTypeDef",
)


_ClientCancelJobResponseTypeDef = TypedDict(
    "_ClientCancelJobResponseTypeDef", {"Success": bool}, total=False
)


class ClientCancelJobResponseTypeDef(_ClientCancelJobResponseTypeDef):
    """
    Type definition for `ClientCancelJob` `Response`

    - **Success** *(boolean) --* Specifies whether (true) or not (false) AWS Import/Export updated
    your job.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef",
    {
        "JobId": str,
        "JobType": str,
        "Signature": str,
        "SignatureFileContents": str,
        "WarningMessage": str,
        "ArtifactList": List[Dict],
    },
    total=False,
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    Type definition for `ClientCreateJob` `Response`

    - **JobId** *(string) --* A unique identifier which refers to a particular job.

    - **JobType** *(string) --* Specifies whether the job to initiate is an import or export job.

    - **Signature** *(string) --* An encrypted code used to authenticate the request and response,
    for example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to create the
    signature file yourself. Generally you should use the SignatureFileContents value.

    - **SignatureFileContents** *(string) --* The actual text of the SIGNATURE file to be written
    to disk.

    - **WarningMessage** *(string) --* An optional message notifying you of non-fatal issues with
    the job, such as use of an incompatible Amazon S3 bucket name.

    - **ArtifactList** *(list) --* A collection of artifacts.

      - *(dict) --* A discrete item that contains the description and URL of an artifact (such as a
      PDF).

        - **Description** *(string) --* The associated description for this object.

        - **URL** *(string) --* The URL for a given Artifact.
    """


_ClientGetShippingLabelResponseTypeDef = TypedDict(
    "_ClientGetShippingLabelResponseTypeDef",
    {"ShippingLabelURL": str, "Warning": str},
    total=False,
)


class ClientGetShippingLabelResponseTypeDef(_ClientGetShippingLabelResponseTypeDef):
    """
    Type definition for `ClientGetShippingLabel` `Response`

    - **ShippingLabelURL** *(string) --*

    - **Warning** *(string) --*
    """


_ClientGetStatusResponseTypeDef = TypedDict(
    "_ClientGetStatusResponseTypeDef",
    {
        "JobId": str,
        "JobType": str,
        "LocationCode": str,
        "LocationMessage": str,
        "ProgressCode": str,
        "ProgressMessage": str,
        "Carrier": str,
        "TrackingNumber": str,
        "LogBucket": str,
        "LogKey": str,
        "ErrorCount": int,
        "Signature": str,
        "SignatureFileContents": str,
        "CurrentManifest": str,
        "CreationDate": datetime,
        "ArtifactList": List[Dict],
    },
    total=False,
)


class ClientGetStatusResponseTypeDef(_ClientGetStatusResponseTypeDef):
    """
    Type definition for `ClientGetStatus` `Response`

    - **JobId** *(string) --* A unique identifier which refers to a particular job.

    - **JobType** *(string) --* Specifies whether the job to initiate is an import or export job.

    - **LocationCode** *(string) --* A token representing the location of the storage device, such
    as "AtAWS".

    - **LocationMessage** *(string) --* A more human readable form of the physical location of the
    storage device.

    - **ProgressCode** *(string) --* A token representing the state of the job, such as "Started".

    - **ProgressMessage** *(string) --* A more human readable form of the job status.

    - **Carrier** *(string) --* Name of the shipping company. This value is included when the
    LocationCode is "Returned".

    - **TrackingNumber** *(string) --* The shipping tracking number assigned by AWS Import/Export
    to the storage device when it's returned to you. We return this value when the LocationCode is
    "Returned".

    - **LogBucket** *(string) --* Amazon S3 bucket for user logs.

    - **LogKey** *(string) --* The key where the user logs were stored.

    - **ErrorCount** *(integer) --* Number of errors. We return this value when the ProgressCode is
    Success or SuccessWithErrors.

    - **Signature** *(string) --* An encrypted code used to authenticate the request and response,
    for example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to create the
    signature file yourself. Generally you should use the SignatureFileContents value.

    - **SignatureFileContents** *(string) --* An encrypted code used to authenticate the request
    and response, for example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to
    create the signature file yourself. Generally you should use the SignatureFileContents value.

    - **CurrentManifest** *(string) --* The last manifest submitted, which will be used to process
    the job.

    - **CreationDate** *(datetime) --* Timestamp of the CreateJob request in ISO8601 date format.
    For example "2010-03-28T20:27:35Z".

    - **ArtifactList** *(list) --* A collection of artifacts.

      - *(dict) --* A discrete item that contains the description and URL of an artifact (such as a
      PDF).

        - **Description** *(string) --* The associated description for this object.

        - **URL** *(string) --* The URL for a given Artifact.
    """


_ClientListJobsResponseJobsTypeDef = TypedDict(
    "_ClientListJobsResponseJobsTypeDef",
    {"JobId": str, "CreationDate": datetime, "IsCanceled": bool, "JobType": str},
    total=False,
)


class ClientListJobsResponseJobsTypeDef(_ClientListJobsResponseJobsTypeDef):
    """
    Type definition for `ClientListJobsResponse` `Jobs`

    - **JobId** *(string) --* A unique identifier which refers to a particular job.

    - **CreationDate** *(datetime) --* Timestamp of the CreateJob request in ISO8601 date
    format. For example "2010-03-28T20:27:35Z".

    - **IsCanceled** *(boolean) --* Indicates whether the job was canceled.

    - **JobType** *(string) --* Specifies whether the job to initiate is an import or export
    job.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"Jobs": List[ClientListJobsResponseJobsTypeDef], "IsTruncated": bool},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    Type definition for `ClientListJobs` `Response`

    - **Jobs** *(list) --* A list container for Jobs returned by the ListJobs operation.

      - *(dict) --* Representation of a job returned by the ListJobs operation.

        - **JobId** *(string) --* A unique identifier which refers to a particular job.

        - **CreationDate** *(datetime) --* Timestamp of the CreateJob request in ISO8601 date
        format. For example "2010-03-28T20:27:35Z".

        - **IsCanceled** *(boolean) --* Indicates whether the job was canceled.

        - **JobType** *(string) --* Specifies whether the job to initiate is an import or export
        job.

    - **IsTruncated** *(boolean) --* Indicates whether the list of jobs was truncated. If true,
    then call ListJobs again using the last JobId element as the marker.
    """


_ClientUpdateJobResponseTypeDef = TypedDict(
    "_ClientUpdateJobResponseTypeDef",
    {"Success": bool, "WarningMessage": str, "ArtifactList": List[Dict]},
    total=False,
)


class ClientUpdateJobResponseTypeDef(_ClientUpdateJobResponseTypeDef):
    """
    Type definition for `ClientUpdateJob` `Response`

    - **Success** *(boolean) --* Specifies whether (true) or not (false) AWS Import/Export updated
    your job.

    - **WarningMessage** *(string) --* An optional message notifying you of non-fatal issues with
    the job, such as use of an incompatible Amazon S3 bucket name.

    - **ArtifactList** *(list) --* A collection of artifacts.

      - *(dict) --* A discrete item that contains the description and URL of an artifact (such as a
      PDF).

        - **Description** *(string) --* The associated description for this object.

        - **URL** *(string) --* The URL for a given Artifact.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListJobsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListJobsPaginateResponseJobsTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobsTypeDef",
    {"JobId": str, "CreationDate": datetime, "IsCanceled": bool, "JobType": str},
    total=False,
)


class ListJobsPaginateResponseJobsTypeDef(_ListJobsPaginateResponseJobsTypeDef):
    """
    Type definition for `ListJobsPaginateResponse` `Jobs`

    - **JobId** *(string) --* A unique identifier which refers to a particular job.

    - **CreationDate** *(datetime) --* Timestamp of the CreateJob request in ISO8601 date
    format. For example "2010-03-28T20:27:35Z".

    - **IsCanceled** *(boolean) --* Indicates whether the job was canceled.

    - **JobType** *(string) --* Specifies whether the job to initiate is an import or export
    job.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {
        "Jobs": List[ListJobsPaginateResponseJobsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    Type definition for `ListJobsPaginate` `Response`

    - **Jobs** *(list) --* A list container for Jobs returned by the ListJobs operation.

      - *(dict) --* Representation of a job returned by the ListJobs operation.

        - **JobId** *(string) --* A unique identifier which refers to a particular job.

        - **CreationDate** *(datetime) --* Timestamp of the CreateJob request in ISO8601 date
        format. For example "2010-03-28T20:27:35Z".

        - **IsCanceled** *(boolean) --* Indicates whether the job was canceled.

        - **JobType** *(string) --* Specifies whether the job to initiate is an import or export
        job.

    - **IsTruncated** *(boolean) --* Indicates whether the list of jobs was truncated. If true,
    then call ListJobs again using the last JobId element as the marker.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
