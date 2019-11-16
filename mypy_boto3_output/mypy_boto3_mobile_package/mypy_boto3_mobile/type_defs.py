"Main interface for mobile type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateProjectResponsedetailsresourcesTypeDef",
    "ClientCreateProjectResponsedetailsTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientDeleteProjectResponsedeletedResourcesTypeDef",
    "ClientDeleteProjectResponseorphanedResourcesTypeDef",
    "ClientDeleteProjectResponseTypeDef",
    "ClientDescribeBundleResponsedetailsTypeDef",
    "ClientDescribeBundleResponseTypeDef",
    "ClientDescribeProjectResponsedetailsresourcesTypeDef",
    "ClientDescribeProjectResponsedetailsTypeDef",
    "ClientDescribeProjectResponseTypeDef",
    "ClientExportBundleResponseTypeDef",
    "ClientExportProjectResponseTypeDef",
    "ClientListBundlesResponsebundleListTypeDef",
    "ClientListBundlesResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientUpdateProjectResponsedetailsresourcesTypeDef",
    "ClientUpdateProjectResponsedetailsTypeDef",
    "ClientUpdateProjectResponseTypeDef",
    "ListBundlesPaginatePaginationConfigTypeDef",
    "ListBundlesPaginateResponsebundleListTypeDef",
    "ListBundlesPaginateResponseTypeDef",
    "ListProjectsPaginatePaginationConfigTypeDef",
    "ListProjectsPaginateResponseprojectsTypeDef",
    "ListProjectsPaginateResponseTypeDef",
)


_ClientCreateProjectResponsedetailsresourcesTypeDef = TypedDict(
    "_ClientCreateProjectResponsedetailsresourcesTypeDef",
    {
        "type": str,
        "name": str,
        "arn": str,
        "feature": str,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientCreateProjectResponsedetailsresourcesTypeDef(
    _ClientCreateProjectResponsedetailsresourcesTypeDef
):
    """
    Type definition for `ClientCreateProjectResponsedetails` `resources`

    Information about an instance of an AWS resource associated with a project.

    - **type** *(string) --*

      Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

    - **name** *(string) --*

      Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

    - **arn** *(string) --*

      AWS resource name which uniquely identifies the resource in AWS systems.

    - **feature** *(string) --*

      Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

    - **attributes** *(dict) --*

      Key-value attribute pairs.

      - *(string) --*

        Key part of key-value attribute pairs.

        - *(string) --*

          Value part of key-value attribute pairs.
    """


_ClientCreateProjectResponsedetailsTypeDef = TypedDict(
    "_ClientCreateProjectResponsedetailsTypeDef",
    {
        "name": str,
        "projectId": str,
        "region": str,
        "state": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "consoleUrl": str,
        "resources": List[ClientCreateProjectResponsedetailsresourcesTypeDef],
    },
    total=False,
)


class ClientCreateProjectResponsedetailsTypeDef(
    _ClientCreateProjectResponsedetailsTypeDef
):
    """
    Type definition for `ClientCreateProjectResponse` `details`

    Detailed information about the created AWS Mobile Hub project.

    - **name** *(string) --*

      Name of the project.

    - **projectId** *(string) --*

      Unique project identifier.

    - **region** *(string) --*

      Default region to use for AWS resource creation in the AWS Mobile Hub project.

    - **state** *(string) --*

      Synchronization state for a project.

    - **createdDate** *(datetime) --*

      Date the project was created.

    - **lastUpdatedDate** *(datetime) --*

      Date of the last modification of the project.

    - **consoleUrl** *(string) --*

      Website URL for this project in the AWS Mobile Hub console.

    - **resources** *(list) --*

      List of AWS resources associated with a project.

      - *(dict) --*

        Information about an instance of an AWS resource associated with a project.

        - **type** *(string) --*

          Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

        - **name** *(string) --*

          Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

        - **arn** *(string) --*

          AWS resource name which uniquely identifies the resource in AWS systems.

        - **feature** *(string) --*

          Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

        - **attributes** *(dict) --*

          Key-value attribute pairs.

          - *(string) --*

            Key part of key-value attribute pairs.

            - *(string) --*

              Value part of key-value attribute pairs.
    """


_ClientCreateProjectResponseTypeDef = TypedDict(
    "_ClientCreateProjectResponseTypeDef",
    {"details": ClientCreateProjectResponsedetailsTypeDef},
    total=False,
)


class ClientCreateProjectResponseTypeDef(_ClientCreateProjectResponseTypeDef):
    """
    Type definition for `ClientCreateProject` `Response`

    Result structure used in response to a request to create a project.

    - **details** *(dict) --*

      Detailed information about the created AWS Mobile Hub project.

      - **name** *(string) --*

        Name of the project.

      - **projectId** *(string) --*

        Unique project identifier.

      - **region** *(string) --*

        Default region to use for AWS resource creation in the AWS Mobile Hub project.

      - **state** *(string) --*

        Synchronization state for a project.

      - **createdDate** *(datetime) --*

        Date the project was created.

      - **lastUpdatedDate** *(datetime) --*

        Date of the last modification of the project.

      - **consoleUrl** *(string) --*

        Website URL for this project in the AWS Mobile Hub console.

      - **resources** *(list) --*

        List of AWS resources associated with a project.

        - *(dict) --*

          Information about an instance of an AWS resource associated with a project.

          - **type** *(string) --*

            Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

          - **name** *(string) --*

            Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

          - **arn** *(string) --*

            AWS resource name which uniquely identifies the resource in AWS systems.

          - **feature** *(string) --*

            Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

          - **attributes** *(dict) --*

            Key-value attribute pairs.

            - *(string) --*

              Key part of key-value attribute pairs.

              - *(string) --*

                Value part of key-value attribute pairs.
    """


_ClientDeleteProjectResponsedeletedResourcesTypeDef = TypedDict(
    "_ClientDeleteProjectResponsedeletedResourcesTypeDef",
    {
        "type": str,
        "name": str,
        "arn": str,
        "feature": str,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientDeleteProjectResponsedeletedResourcesTypeDef(
    _ClientDeleteProjectResponsedeletedResourcesTypeDef
):
    """
    Type definition for `ClientDeleteProjectResponse` `deletedResources`

    Information about an instance of an AWS resource associated with a project.

    - **type** *(string) --*

      Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

    - **name** *(string) --*

      Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

    - **arn** *(string) --*

      AWS resource name which uniquely identifies the resource in AWS systems.

    - **feature** *(string) --*

      Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

    - **attributes** *(dict) --*

      Key-value attribute pairs.

      - *(string) --*

        Key part of key-value attribute pairs.

        - *(string) --*

          Value part of key-value attribute pairs.
    """


_ClientDeleteProjectResponseorphanedResourcesTypeDef = TypedDict(
    "_ClientDeleteProjectResponseorphanedResourcesTypeDef",
    {
        "type": str,
        "name": str,
        "arn": str,
        "feature": str,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientDeleteProjectResponseorphanedResourcesTypeDef(
    _ClientDeleteProjectResponseorphanedResourcesTypeDef
):
    """
    Type definition for `ClientDeleteProjectResponse` `orphanedResources`

    Information about an instance of an AWS resource associated with a project.

    - **type** *(string) --*

      Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

    - **name** *(string) --*

      Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

    - **arn** *(string) --*

      AWS resource name which uniquely identifies the resource in AWS systems.

    - **feature** *(string) --*

      Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

    - **attributes** *(dict) --*

      Key-value attribute pairs.

      - *(string) --*

        Key part of key-value attribute pairs.

        - *(string) --*

          Value part of key-value attribute pairs.
    """


_ClientDeleteProjectResponseTypeDef = TypedDict(
    "_ClientDeleteProjectResponseTypeDef",
    {
        "deletedResources": List[ClientDeleteProjectResponsedeletedResourcesTypeDef],
        "orphanedResources": List[ClientDeleteProjectResponseorphanedResourcesTypeDef],
    },
    total=False,
)


class ClientDeleteProjectResponseTypeDef(_ClientDeleteProjectResponseTypeDef):
    """
    Type definition for `ClientDeleteProject` `Response`

    Result structure used in response to request to delete a project.

    - **deletedResources** *(list) --*

      Resources which were deleted.

      - *(dict) --*

        Information about an instance of an AWS resource associated with a project.

        - **type** *(string) --*

          Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

        - **name** *(string) --*

          Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

        - **arn** *(string) --*

          AWS resource name which uniquely identifies the resource in AWS systems.

        - **feature** *(string) --*

          Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

        - **attributes** *(dict) --*

          Key-value attribute pairs.

          - *(string) --*

            Key part of key-value attribute pairs.

            - *(string) --*

              Value part of key-value attribute pairs.

    - **orphanedResources** *(list) --*

      Resources which were not deleted, due to a risk of losing potentially important data or files.

      - *(dict) --*

        Information about an instance of an AWS resource associated with a project.

        - **type** *(string) --*

          Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

        - **name** *(string) --*

          Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

        - **arn** *(string) --*

          AWS resource name which uniquely identifies the resource in AWS systems.

        - **feature** *(string) --*

          Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

        - **attributes** *(dict) --*

          Key-value attribute pairs.

          - *(string) --*

            Key part of key-value attribute pairs.

            - *(string) --*

              Value part of key-value attribute pairs.
    """


_ClientDescribeBundleResponsedetailsTypeDef = TypedDict(
    "_ClientDescribeBundleResponsedetailsTypeDef",
    {
        "bundleId": str,
        "title": str,
        "version": str,
        "description": str,
        "iconUrl": str,
        "availablePlatforms": List[str],
    },
    total=False,
)


class ClientDescribeBundleResponsedetailsTypeDef(
    _ClientDescribeBundleResponsedetailsTypeDef
):
    """
    Type definition for `ClientDescribeBundleResponse` `details`

    The details of the bundle.

    - **bundleId** *(string) --*

      Unique bundle identifier.

    - **title** *(string) --*

      Title of the download bundle.

    - **version** *(string) --*

      Version of the download bundle.

    - **description** *(string) --*

      Description of the download bundle.

    - **iconUrl** *(string) --*

      Icon for the download bundle.

    - **availablePlatforms** *(list) --*

      Developer desktop or mobile app or website platforms.

      - *(string) --*

        Developer desktop or target mobile app or website platform.
    """


_ClientDescribeBundleResponseTypeDef = TypedDict(
    "_ClientDescribeBundleResponseTypeDef",
    {"details": ClientDescribeBundleResponsedetailsTypeDef},
    total=False,
)


class ClientDescribeBundleResponseTypeDef(_ClientDescribeBundleResponseTypeDef):
    """
    Type definition for `ClientDescribeBundle` `Response`

    Result structure contains the details of the bundle.

    - **details** *(dict) --*

      The details of the bundle.

      - **bundleId** *(string) --*

        Unique bundle identifier.

      - **title** *(string) --*

        Title of the download bundle.

      - **version** *(string) --*

        Version of the download bundle.

      - **description** *(string) --*

        Description of the download bundle.

      - **iconUrl** *(string) --*

        Icon for the download bundle.

      - **availablePlatforms** *(list) --*

        Developer desktop or mobile app or website platforms.

        - *(string) --*

          Developer desktop or target mobile app or website platform.
    """


_ClientDescribeProjectResponsedetailsresourcesTypeDef = TypedDict(
    "_ClientDescribeProjectResponsedetailsresourcesTypeDef",
    {
        "type": str,
        "name": str,
        "arn": str,
        "feature": str,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientDescribeProjectResponsedetailsresourcesTypeDef(
    _ClientDescribeProjectResponsedetailsresourcesTypeDef
):
    """
    Type definition for `ClientDescribeProjectResponsedetails` `resources`

    Information about an instance of an AWS resource associated with a project.

    - **type** *(string) --*

      Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

    - **name** *(string) --*

      Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

    - **arn** *(string) --*

      AWS resource name which uniquely identifies the resource in AWS systems.

    - **feature** *(string) --*

      Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

    - **attributes** *(dict) --*

      Key-value attribute pairs.

      - *(string) --*

        Key part of key-value attribute pairs.

        - *(string) --*

          Value part of key-value attribute pairs.
    """


_ClientDescribeProjectResponsedetailsTypeDef = TypedDict(
    "_ClientDescribeProjectResponsedetailsTypeDef",
    {
        "name": str,
        "projectId": str,
        "region": str,
        "state": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "consoleUrl": str,
        "resources": List[ClientDescribeProjectResponsedetailsresourcesTypeDef],
    },
    total=False,
)


class ClientDescribeProjectResponsedetailsTypeDef(
    _ClientDescribeProjectResponsedetailsTypeDef
):
    """
    Type definition for `ClientDescribeProjectResponse` `details`

    Detailed information about an AWS Mobile Hub project.

    - **name** *(string) --*

      Name of the project.

    - **projectId** *(string) --*

      Unique project identifier.

    - **region** *(string) --*

      Default region to use for AWS resource creation in the AWS Mobile Hub project.

    - **state** *(string) --*

      Synchronization state for a project.

    - **createdDate** *(datetime) --*

      Date the project was created.

    - **lastUpdatedDate** *(datetime) --*

      Date of the last modification of the project.

    - **consoleUrl** *(string) --*

      Website URL for this project in the AWS Mobile Hub console.

    - **resources** *(list) --*

      List of AWS resources associated with a project.

      - *(dict) --*

        Information about an instance of an AWS resource associated with a project.

        - **type** *(string) --*

          Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

        - **name** *(string) --*

          Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

        - **arn** *(string) --*

          AWS resource name which uniquely identifies the resource in AWS systems.

        - **feature** *(string) --*

          Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

        - **attributes** *(dict) --*

          Key-value attribute pairs.

          - *(string) --*

            Key part of key-value attribute pairs.

            - *(string) --*

              Value part of key-value attribute pairs.
    """


_ClientDescribeProjectResponseTypeDef = TypedDict(
    "_ClientDescribeProjectResponseTypeDef",
    {"details": ClientDescribeProjectResponsedetailsTypeDef},
    total=False,
)


class ClientDescribeProjectResponseTypeDef(_ClientDescribeProjectResponseTypeDef):
    """
    Type definition for `ClientDescribeProject` `Response`

    Result structure used for requests of project details.

    - **details** *(dict) --*

      Detailed information about an AWS Mobile Hub project.

      - **name** *(string) --*

        Name of the project.

      - **projectId** *(string) --*

        Unique project identifier.

      - **region** *(string) --*

        Default region to use for AWS resource creation in the AWS Mobile Hub project.

      - **state** *(string) --*

        Synchronization state for a project.

      - **createdDate** *(datetime) --*

        Date the project was created.

      - **lastUpdatedDate** *(datetime) --*

        Date of the last modification of the project.

      - **consoleUrl** *(string) --*

        Website URL for this project in the AWS Mobile Hub console.

      - **resources** *(list) --*

        List of AWS resources associated with a project.

        - *(dict) --*

          Information about an instance of an AWS resource associated with a project.

          - **type** *(string) --*

            Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

          - **name** *(string) --*

            Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

          - **arn** *(string) --*

            AWS resource name which uniquely identifies the resource in AWS systems.

          - **feature** *(string) --*

            Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

          - **attributes** *(dict) --*

            Key-value attribute pairs.

            - *(string) --*

              Key part of key-value attribute pairs.

              - *(string) --*

                Value part of key-value attribute pairs.
    """


_ClientExportBundleResponseTypeDef = TypedDict(
    "_ClientExportBundleResponseTypeDef", {"downloadUrl": str}, total=False
)


class ClientExportBundleResponseTypeDef(_ClientExportBundleResponseTypeDef):
    """
    Type definition for `ClientExportBundle` `Response`

    Result structure which contains link to download custom-generated SDK and tool packages used to
    integrate mobile web or app clients with backed AWS resources.

    - **downloadUrl** *(string) --*

      URL which contains the custom-generated SDK and tool packages used to integrate the client
      mobile app or web app with the AWS resources created by the AWS Mobile Hub project.
    """


_ClientExportProjectResponseTypeDef = TypedDict(
    "_ClientExportProjectResponseTypeDef",
    {"downloadUrl": str, "shareUrl": str, "snapshotId": str},
    total=False,
)


class ClientExportProjectResponseTypeDef(_ClientExportProjectResponseTypeDef):
    """
    Type definition for `ClientExportProject` `Response`

    Result structure used for requests to export project configuration details.

    - **downloadUrl** *(string) --*

      URL which can be used to download the exported project configuation file(s).

    - **shareUrl** *(string) --*

      URL which can be shared to allow other AWS users to create their own project in AWS Mobile
      Hub with the same configuration as the specified project. This URL pertains to a snapshot in
      time of the project configuration that is created when this API is called. If you want to
      share additional changes to your project configuration, then you will need to create and
      share a new snapshot by calling this method again.

    - **snapshotId** *(string) --*

      Unique identifier for the exported snapshot of the project configuration. This snapshot
      identifier is included in the share URL.
    """


_ClientListBundlesResponsebundleListTypeDef = TypedDict(
    "_ClientListBundlesResponsebundleListTypeDef",
    {
        "bundleId": str,
        "title": str,
        "version": str,
        "description": str,
        "iconUrl": str,
        "availablePlatforms": List[str],
    },
    total=False,
)


class ClientListBundlesResponsebundleListTypeDef(
    _ClientListBundlesResponsebundleListTypeDef
):
    """
    Type definition for `ClientListBundlesResponse` `bundleList`

    The details of the bundle.

    - **bundleId** *(string) --*

      Unique bundle identifier.

    - **title** *(string) --*

      Title of the download bundle.

    - **version** *(string) --*

      Version of the download bundle.

    - **description** *(string) --*

      Description of the download bundle.

    - **iconUrl** *(string) --*

      Icon for the download bundle.

    - **availablePlatforms** *(list) --*

      Developer desktop or mobile app or website platforms.

      - *(string) --*

        Developer desktop or target mobile app or website platform.
    """


_ClientListBundlesResponseTypeDef = TypedDict(
    "_ClientListBundlesResponseTypeDef",
    {"bundleList": List[ClientListBundlesResponsebundleListTypeDef], "nextToken": str},
    total=False,
)


class ClientListBundlesResponseTypeDef(_ClientListBundlesResponseTypeDef):
    """
    Type definition for `ClientListBundles` `Response`

    Result structure contains a list of all available bundles with details.

    - **bundleList** *(list) --*

      A list of bundles.

      - *(dict) --*

        The details of the bundle.

        - **bundleId** *(string) --*

          Unique bundle identifier.

        - **title** *(string) --*

          Title of the download bundle.

        - **version** *(string) --*

          Version of the download bundle.

        - **description** *(string) --*

          Description of the download bundle.

        - **iconUrl** *(string) --*

          Icon for the download bundle.

        - **availablePlatforms** *(list) --*

          Developer desktop or mobile app or website platforms.

          - *(string) --*

            Developer desktop or target mobile app or website platform.

    - **nextToken** *(string) --*

      Pagination token. If non-null pagination token is returned in a result, then pass its value
      in another request to fetch more entries.
    """


_ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientListProjectsResponseprojectsTypeDef",
    {"name": str, "projectId": str},
    total=False,
)


class ClientListProjectsResponseprojectsTypeDef(
    _ClientListProjectsResponseprojectsTypeDef
):
    """
    Type definition for `ClientListProjectsResponse` `projects`

    Summary information about an AWS Mobile Hub project.

    - **name** *(string) --*

      Name of the project.

    - **projectId** *(string) --*

      Unique project identifier.
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    Type definition for `ClientListProjects` `Response`

    Result structure used for requests to list projects in AWS Mobile Hub.

    - **projects** *(list) --*

      List of projects.

      - *(dict) --*

        Summary information about an AWS Mobile Hub project.

        - **name** *(string) --*

          Name of the project.

        - **projectId** *(string) --*

          Unique project identifier.

    - **nextToken** *(string) --*

      Pagination token. Set to null to start listing records from start. If non-null pagination
      token is returned in a result, then pass its value in here in another request to list more
      entries.
    """


_ClientUpdateProjectResponsedetailsresourcesTypeDef = TypedDict(
    "_ClientUpdateProjectResponsedetailsresourcesTypeDef",
    {
        "type": str,
        "name": str,
        "arn": str,
        "feature": str,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientUpdateProjectResponsedetailsresourcesTypeDef(
    _ClientUpdateProjectResponsedetailsresourcesTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponsedetails` `resources`

    Information about an instance of an AWS resource associated with a project.

    - **type** *(string) --*

      Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

    - **name** *(string) --*

      Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

    - **arn** *(string) --*

      AWS resource name which uniquely identifies the resource in AWS systems.

    - **feature** *(string) --*

      Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

    - **attributes** *(dict) --*

      Key-value attribute pairs.

      - *(string) --*

        Key part of key-value attribute pairs.

        - *(string) --*

          Value part of key-value attribute pairs.
    """


_ClientUpdateProjectResponsedetailsTypeDef = TypedDict(
    "_ClientUpdateProjectResponsedetailsTypeDef",
    {
        "name": str,
        "projectId": str,
        "region": str,
        "state": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "consoleUrl": str,
        "resources": List[ClientUpdateProjectResponsedetailsresourcesTypeDef],
    },
    total=False,
)


class ClientUpdateProjectResponsedetailsTypeDef(
    _ClientUpdateProjectResponsedetailsTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponse` `details`

    Detailed information about the updated AWS Mobile Hub project.

    - **name** *(string) --*

      Name of the project.

    - **projectId** *(string) --*

      Unique project identifier.

    - **region** *(string) --*

      Default region to use for AWS resource creation in the AWS Mobile Hub project.

    - **state** *(string) --*

      Synchronization state for a project.

    - **createdDate** *(datetime) --*

      Date the project was created.

    - **lastUpdatedDate** *(datetime) --*

      Date of the last modification of the project.

    - **consoleUrl** *(string) --*

      Website URL for this project in the AWS Mobile Hub console.

    - **resources** *(list) --*

      List of AWS resources associated with a project.

      - *(dict) --*

        Information about an instance of an AWS resource associated with a project.

        - **type** *(string) --*

          Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

        - **name** *(string) --*

          Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

        - **arn** *(string) --*

          AWS resource name which uniquely identifies the resource in AWS systems.

        - **feature** *(string) --*

          Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

        - **attributes** *(dict) --*

          Key-value attribute pairs.

          - *(string) --*

            Key part of key-value attribute pairs.

            - *(string) --*

              Value part of key-value attribute pairs.
    """


_ClientUpdateProjectResponseTypeDef = TypedDict(
    "_ClientUpdateProjectResponseTypeDef",
    {"details": ClientUpdateProjectResponsedetailsTypeDef},
    total=False,
)


class ClientUpdateProjectResponseTypeDef(_ClientUpdateProjectResponseTypeDef):
    """
    Type definition for `ClientUpdateProject` `Response`

    Result structure used for requests to updated project configuration.

    - **details** *(dict) --*

      Detailed information about the updated AWS Mobile Hub project.

      - **name** *(string) --*

        Name of the project.

      - **projectId** *(string) --*

        Unique project identifier.

      - **region** *(string) --*

        Default region to use for AWS resource creation in the AWS Mobile Hub project.

      - **state** *(string) --*

        Synchronization state for a project.

      - **createdDate** *(datetime) --*

        Date the project was created.

      - **lastUpdatedDate** *(datetime) --*

        Date of the last modification of the project.

      - **consoleUrl** *(string) --*

        Website URL for this project in the AWS Mobile Hub console.

      - **resources** *(list) --*

        List of AWS resources associated with a project.

        - *(dict) --*

          Information about an instance of an AWS resource associated with a project.

          - **type** *(string) --*

            Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

          - **name** *(string) --*

            Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

          - **arn** *(string) --*

            AWS resource name which uniquely identifies the resource in AWS systems.

          - **feature** *(string) --*

            Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

          - **attributes** *(dict) --*

            Key-value attribute pairs.

            - *(string) --*

              Key part of key-value attribute pairs.

              - *(string) --*

                Value part of key-value attribute pairs.
    """


_ListBundlesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBundlesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBundlesPaginatePaginationConfigTypeDef(
    _ListBundlesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBundlesPaginate` `PaginationConfig`

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


_ListBundlesPaginateResponsebundleListTypeDef = TypedDict(
    "_ListBundlesPaginateResponsebundleListTypeDef",
    {
        "bundleId": str,
        "title": str,
        "version": str,
        "description": str,
        "iconUrl": str,
        "availablePlatforms": List[str],
    },
    total=False,
)


class ListBundlesPaginateResponsebundleListTypeDef(
    _ListBundlesPaginateResponsebundleListTypeDef
):
    """
    Type definition for `ListBundlesPaginateResponse` `bundleList`

    The details of the bundle.

    - **bundleId** *(string) --*

      Unique bundle identifier.

    - **title** *(string) --*

      Title of the download bundle.

    - **version** *(string) --*

      Version of the download bundle.

    - **description** *(string) --*

      Description of the download bundle.

    - **iconUrl** *(string) --*

      Icon for the download bundle.

    - **availablePlatforms** *(list) --*

      Developer desktop or mobile app or website platforms.

      - *(string) --*

        Developer desktop or target mobile app or website platform.
    """


_ListBundlesPaginateResponseTypeDef = TypedDict(
    "_ListBundlesPaginateResponseTypeDef",
    {
        "bundleList": List[ListBundlesPaginateResponsebundleListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListBundlesPaginateResponseTypeDef(_ListBundlesPaginateResponseTypeDef):
    """
    Type definition for `ListBundlesPaginate` `Response`

    Result structure contains a list of all available bundles with details.

    - **bundleList** *(list) --*

      A list of bundles.

      - *(dict) --*

        The details of the bundle.

        - **bundleId** *(string) --*

          Unique bundle identifier.

        - **title** *(string) --*

          Title of the download bundle.

        - **version** *(string) --*

          Version of the download bundle.

        - **description** *(string) --*

          Description of the download bundle.

        - **iconUrl** *(string) --*

          Icon for the download bundle.

        - **availablePlatforms** *(list) --*

          Developer desktop or mobile app or website platforms.

          - *(string) --*

            Developer desktop or target mobile app or website platform.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProjectsPaginatePaginationConfigTypeDef(
    _ListProjectsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListProjectsPaginate` `PaginationConfig`

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


_ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "_ListProjectsPaginateResponseprojectsTypeDef",
    {"name": str, "projectId": str},
    total=False,
)


class ListProjectsPaginateResponseprojectsTypeDef(
    _ListProjectsPaginateResponseprojectsTypeDef
):
    """
    Type definition for `ListProjectsPaginateResponse` `projects`

    Summary information about an AWS Mobile Hub project.

    - **name** *(string) --*

      Name of the project.

    - **projectId** *(string) --*

      Unique project identifier.
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    Type definition for `ListProjectsPaginate` `Response`

    Result structure used for requests to list projects in AWS Mobile Hub.

    - **projects** *(list) --*

      List of projects.

      - *(dict) --*

        Summary information about an AWS Mobile Hub project.

        - **name** *(string) --*

          Name of the project.

        - **projectId** *(string) --*

          Unique project identifier.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
