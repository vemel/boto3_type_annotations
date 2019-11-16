"Main interface for snowball type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAddressAddressTypeDef",
    "ClientCreateAddressResponseTypeDef",
    "ClientCreateClusterNotificationTypeDef",
    "ClientCreateClusterResourcesEc2AmiResourcesTypeDef",
    "ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientCreateClusterResourcesLambdaResourcesTypeDef",
    "ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef",
    "ClientCreateClusterResourcesS3ResourcesTypeDef",
    "ClientCreateClusterResourcesTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateJobNotificationTypeDef",
    "ClientCreateJobResourcesEc2AmiResourcesTypeDef",
    "ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientCreateJobResourcesLambdaResourcesTypeDef",
    "ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef",
    "ClientCreateJobResourcesS3ResourcesTypeDef",
    "ClientCreateJobResourcesTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientDescribeAddressResponseAddressTypeDef",
    "ClientDescribeAddressResponseTypeDef",
    "ClientDescribeAddressesResponseAddressesTypeDef",
    "ClientDescribeAddressesResponseTypeDef",
    "ClientDescribeClusterResponseClusterMetadataNotificationTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef",
    "ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef",
    "ClientDescribeJobResponseJobMetadataNotificationTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef",
    "ClientDescribeJobResponseJobMetadataTypeDef",
    "ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef",
    "ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef",
    "ClientDescribeJobResponseSubJobMetadataNotificationTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef",
    "ClientDescribeJobResponseSubJobMetadataTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientGetJobManifestResponseTypeDef",
    "ClientGetJobUnlockCodeResponseTypeDef",
    "ClientGetSnowballUsageResponseTypeDef",
    "ClientGetSoftwareUpdatesResponseTypeDef",
    "ClientListClusterJobsResponseJobListEntriesTypeDef",
    "ClientListClusterJobsResponseTypeDef",
    "ClientListClustersResponseClusterListEntriesTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListCompatibleImagesResponseCompatibleImagesTypeDef",
    "ClientListCompatibleImagesResponseTypeDef",
    "ClientListJobsResponseJobListEntriesTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientUpdateClusterNotificationTypeDef",
    "ClientUpdateClusterResourcesEc2AmiResourcesTypeDef",
    "ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientUpdateClusterResourcesLambdaResourcesTypeDef",
    "ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef",
    "ClientUpdateClusterResourcesS3ResourcesTypeDef",
    "ClientUpdateClusterResourcesTypeDef",
    "ClientUpdateJobNotificationTypeDef",
    "ClientUpdateJobResourcesEc2AmiResourcesTypeDef",
    "ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientUpdateJobResourcesLambdaResourcesTypeDef",
    "ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef",
    "ClientUpdateJobResourcesS3ResourcesTypeDef",
    "ClientUpdateJobResourcesTypeDef",
    "DescribeAddressesPaginatePaginationConfigTypeDef",
    "DescribeAddressesPaginateResponseAddressesTypeDef",
    "DescribeAddressesPaginateResponseTypeDef",
    "ListClusterJobsPaginatePaginationConfigTypeDef",
    "ListClusterJobsPaginateResponseJobListEntriesTypeDef",
    "ListClusterJobsPaginateResponseTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseClusterListEntriesTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListCompatibleImagesPaginatePaginationConfigTypeDef",
    "ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef",
    "ListCompatibleImagesPaginateResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponseJobListEntriesTypeDef",
    "ListJobsPaginateResponseTypeDef",
)


_ClientCreateAddressAddressTypeDef = TypedDict(
    "_ClientCreateAddressAddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)


class ClientCreateAddressAddressTypeDef(_ClientCreateAddressAddressTypeDef):
    """
    Type definition for `ClientCreateAddress` `Address`

    The address that you want the Snowball shipped to.

    - **AddressId** *(string) --*

      The unique ID for an address.

    - **Name** *(string) --*

      The name of a person to receive a Snowball at an address.

    - **Company** *(string) --*

      The name of the company to receive a Snowball at an address.

    - **Street1** *(string) --*

      The first line in a street address that a Snowball is to be delivered to.

    - **Street2** *(string) --*

      The second line in a street address that a Snowball is to be delivered to.

    - **Street3** *(string) --*

      The third line in a street address that a Snowball is to be delivered to.

    - **City** *(string) --*

      The city in an address that a Snowball is to be delivered to.

    - **StateOrProvince** *(string) --*

      The state or province in an address that a Snowball is to be delivered to.

    - **PrefectureOrDistrict** *(string) --*

      This field is no longer used and the value is ignored.

    - **Landmark** *(string) --*

      This field is no longer used and the value is ignored.

    - **Country** *(string) --*

      The country in an address that a Snowball is to be delivered to.

    - **PostalCode** *(string) --*

      The postal code in an address that a Snowball is to be delivered to.

    - **PhoneNumber** *(string) --*

      The phone number associated with an address that a Snowball is to be delivered to.

    - **IsRestricted** *(boolean) --*

      If the address you are creating is a primary address, then set this option to true. This field
      is not supported in most regions.
    """


_ClientCreateAddressResponseTypeDef = TypedDict(
    "_ClientCreateAddressResponseTypeDef", {"AddressId": str}, total=False
)


class ClientCreateAddressResponseTypeDef(_ClientCreateAddressResponseTypeDef):
    """
    Type definition for `ClientCreateAddress` `Response`

    - **AddressId** *(string) --*

      The automatically generated ID for a specific address. You'll use this ID when you create a
      job to specify which address you want the Snowball for that job shipped to.
    """


_ClientCreateClusterNotificationTypeDef = TypedDict(
    "_ClientCreateClusterNotificationTypeDef",
    {"SnsTopicARN": str, "JobStatesToNotify": List[str], "NotifyAll": bool},
    total=False,
)


class ClientCreateClusterNotificationTypeDef(_ClientCreateClusterNotificationTypeDef):
    """
    Type definition for `ClientCreateCluster` `Notification`

    The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.

    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.

      You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or
      by using the `Subscribe <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS
      Simple Notification Service (SNS) API action.

    - **JobStatesToNotify** *(list) --*

      The list of job states that will trigger a notification for this job.

      - *(string) --*

    - **NotifyAll** *(boolean) --*

      Any change in job state will trigger a notification for this job.
    """


_RequiredClientCreateClusterResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_RequiredClientCreateClusterResourcesEc2AmiResourcesTypeDef", {"AmiId": str}
)
_OptionalClientCreateClusterResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_OptionalClientCreateClusterResourcesEc2AmiResourcesTypeDef",
    {"SnowballAmiId": str},
    total=False,
)


class ClientCreateClusterResourcesEc2AmiResourcesTypeDef(
    _RequiredClientCreateClusterResourcesEc2AmiResourcesTypeDef,
    _OptionalClientCreateClusterResourcesEc2AmiResourcesTypeDef,
):
    """
    Type definition for `ClientCreateClusterResources` `Ec2AmiResources`

    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including
    the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify
    identifying the AMI in both the AWS Cloud and on the device.

    - **AmiId** *(string) --* **[REQUIRED]**

      The ID of the AMI in Amazon EC2.

    - **SnowballAmiId** *(string) --*

      The ID of the AMI on the Snowball Edge device.
    """


_ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef
):
    """
    Type definition for `ClientCreateClusterResourcesLambdaResources` `EventTriggers`

    The container for the  EventTriggerDefinition$EventResourceARN .

    - **EventResourceARN** *(string) --*

      The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
      function's event trigger associated with this job.
    """


_ClientCreateClusterResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientCreateClusterResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientCreateClusterResourcesLambdaResourcesTypeDef(
    _ClientCreateClusterResourcesLambdaResourcesTypeDef
):
    """
    Type definition for `ClientCreateClusterResources` `LambdaResources`

    Identifies

    - **LambdaArn** *(string) --*

      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT
      object actions on the associated local Amazon S3 resource.

    - **EventTriggers** *(list) --*

      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated
      with this job.

      - *(dict) --*

        The container for the  EventTriggerDefinition$EventResourceARN .

        - **EventResourceARN** *(string) --*

          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
          function's event trigger associated with this job.
    """


_ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef(
    _ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef
):
    """
    Type definition for `ClientCreateClusterResourcesS3Resources` `KeyRange`

    For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
    bucket. The length of the range is defined at job creation, and has either an inclusive
    ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

    - **BeginMarker** *(string) --*

      The key that starts an optional key range for an export job. Ranges are inclusive and
      UTF-8 binary sorted.

    - **EndMarker** *(string) --*

      The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
      binary sorted.
    """


_ClientCreateClusterResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientCreateClusterResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)


class ClientCreateClusterResourcesS3ResourcesTypeDef(
    _ClientCreateClusterResourcesS3ResourcesTypeDef
):
    """
    Type definition for `ClientCreateClusterResources` `S3Resources`

    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
    exported from or imported into. For export jobs, this object can have an optional
    ``KeyRange`` value. The length of the range is defined at job creation, and has either an
    inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
    sorted.

    - **BucketArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon S3 bucket.

    - **KeyRange** *(dict) --*

      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
      bucket. The length of the range is defined at job creation, and has either an inclusive
      ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

      - **BeginMarker** *(string) --*

        The key that starts an optional key range for an export job. Ranges are inclusive and
        UTF-8 binary sorted.

      - **EndMarker** *(string) --*

        The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
        binary sorted.
    """


_ClientCreateClusterResourcesTypeDef = TypedDict(
    "_ClientCreateClusterResourcesTypeDef",
    {
        "S3Resources": List[ClientCreateClusterResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientCreateClusterResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientCreateClusterResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)


class ClientCreateClusterResourcesTypeDef(_ClientCreateClusterResourcesTypeDef):
    """
    Type definition for `ClientCreateCluster` `Resources`

    The resources associated with the cluster job. These resources include Amazon S3 buckets and
    optional AWS Lambda functions written in the Python language.

    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.

      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
        exported from or imported into. For export jobs, this object can have an optional
        ``KeyRange`` value. The length of the range is defined at job creation, and has either an
        inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
        sorted.

        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.

        - **KeyRange** *(dict) --*

          For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
          bucket. The length of the range is defined at job creation, and has either an inclusive
          ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

          - **BeginMarker** *(string) --*

            The key that starts an optional key range for an export job. Ranges are inclusive and
            UTF-8 binary sorted.

          - **EndMarker** *(string) --*

            The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
            binary sorted.

    - **LambdaResources** *(list) --*

      The Python-language Lambda functions for this job.

      - *(dict) --*

        Identifies

        - **LambdaArn** *(string) --*

          An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT
          object actions on the associated local Amazon S3 resource.

        - **EventTriggers** *(list) --*

          The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated
          with this job.

          - *(dict) --*

            The container for the  EventTriggerDefinition$EventResourceARN .

            - **EventResourceARN** *(string) --*

              The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
              function's event trigger associated with this job.

    - **Ec2AmiResources** *(list) --*

      The Amazon Machine Images (AMIs) associated with this job.

      - *(dict) --*

        A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including
        the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify
        identifying the AMI in both the AWS Cloud and on the device.

        - **AmiId** *(string) --* **[REQUIRED]**

          The ID of the AMI in Amazon EC2.

        - **SnowballAmiId** *(string) --*

          The ID of the AMI on the Snowball Edge device.
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef", {"ClusterId": str}, total=False
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    Type definition for `ClientCreateCluster` `Response`

    - **ClusterId** *(string) --*

      The automatically generated ID for a cluster.
    """


_ClientCreateJobNotificationTypeDef = TypedDict(
    "_ClientCreateJobNotificationTypeDef",
    {"SnsTopicARN": str, "JobStatesToNotify": List[str], "NotifyAll": bool},
    total=False,
)


class ClientCreateJobNotificationTypeDef(_ClientCreateJobNotificationTypeDef):
    """
    Type definition for `ClientCreateJob` `Notification`

    Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.

    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.

      You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or
      by using the `Subscribe <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS
      Simple Notification Service (SNS) API action.

    - **JobStatesToNotify** *(list) --*

      The list of job states that will trigger a notification for this job.

      - *(string) --*

    - **NotifyAll** *(boolean) --*

      Any change in job state will trigger a notification for this job.
    """


_RequiredClientCreateJobResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_RequiredClientCreateJobResourcesEc2AmiResourcesTypeDef", {"AmiId": str}
)
_OptionalClientCreateJobResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_OptionalClientCreateJobResourcesEc2AmiResourcesTypeDef",
    {"SnowballAmiId": str},
    total=False,
)


class ClientCreateJobResourcesEc2AmiResourcesTypeDef(
    _RequiredClientCreateJobResourcesEc2AmiResourcesTypeDef,
    _OptionalClientCreateJobResourcesEc2AmiResourcesTypeDef,
):
    """
    Type definition for `ClientCreateJobResources` `Ec2AmiResources`

    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including
    the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify
    identifying the AMI in both the AWS Cloud and on the device.

    - **AmiId** *(string) --* **[REQUIRED]**

      The ID of the AMI in Amazon EC2.

    - **SnowballAmiId** *(string) --*

      The ID of the AMI on the Snowball Edge device.
    """


_ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef
):
    """
    Type definition for `ClientCreateJobResourcesLambdaResources` `EventTriggers`

    The container for the  EventTriggerDefinition$EventResourceARN .

    - **EventResourceARN** *(string) --*

      The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
      function's event trigger associated with this job.
    """


_ClientCreateJobResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientCreateJobResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientCreateJobResourcesLambdaResourcesTypeDef(
    _ClientCreateJobResourcesLambdaResourcesTypeDef
):
    """
    Type definition for `ClientCreateJobResources` `LambdaResources`

    Identifies

    - **LambdaArn** *(string) --*

      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT
      object actions on the associated local Amazon S3 resource.

    - **EventTriggers** *(list) --*

      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated
      with this job.

      - *(dict) --*

        The container for the  EventTriggerDefinition$EventResourceARN .

        - **EventResourceARN** *(string) --*

          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
          function's event trigger associated with this job.
    """


_ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef(
    _ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef
):
    """
    Type definition for `ClientCreateJobResourcesS3Resources` `KeyRange`

    For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
    bucket. The length of the range is defined at job creation, and has either an inclusive
    ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

    - **BeginMarker** *(string) --*

      The key that starts an optional key range for an export job. Ranges are inclusive and
      UTF-8 binary sorted.

    - **EndMarker** *(string) --*

      The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
      binary sorted.
    """


_ClientCreateJobResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientCreateJobResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)


class ClientCreateJobResourcesS3ResourcesTypeDef(
    _ClientCreateJobResourcesS3ResourcesTypeDef
):
    """
    Type definition for `ClientCreateJobResources` `S3Resources`

    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
    exported from or imported into. For export jobs, this object can have an optional
    ``KeyRange`` value. The length of the range is defined at job creation, and has either an
    inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
    sorted.

    - **BucketArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon S3 bucket.

    - **KeyRange** *(dict) --*

      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
      bucket. The length of the range is defined at job creation, and has either an inclusive
      ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

      - **BeginMarker** *(string) --*

        The key that starts an optional key range for an export job. Ranges are inclusive and
        UTF-8 binary sorted.

      - **EndMarker** *(string) --*

        The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
        binary sorted.
    """


_ClientCreateJobResourcesTypeDef = TypedDict(
    "_ClientCreateJobResourcesTypeDef",
    {
        "S3Resources": List[ClientCreateJobResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientCreateJobResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientCreateJobResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)


class ClientCreateJobResourcesTypeDef(_ClientCreateJobResourcesTypeDef):
    """
    Type definition for `ClientCreateJob` `Resources`

    Defines the Amazon S3 buckets associated with this job.

    With ``IMPORT`` jobs, you specify the bucket or buckets that your transferred data will be
    imported into.

    With ``EXPORT`` jobs, you specify the bucket or buckets that your transferred data will be
    exported from. Optionally, you can also specify a ``KeyRange`` value. If you choose to export a
    range, you define the length of the range by providing either an inclusive ``BeginMarker`` value,
    an inclusive ``EndMarker`` value, or both. Ranges are UTF-8 binary sorted.

    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.

      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
        exported from or imported into. For export jobs, this object can have an optional
        ``KeyRange`` value. The length of the range is defined at job creation, and has either an
        inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
        sorted.

        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.

        - **KeyRange** *(dict) --*

          For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
          bucket. The length of the range is defined at job creation, and has either an inclusive
          ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

          - **BeginMarker** *(string) --*

            The key that starts an optional key range for an export job. Ranges are inclusive and
            UTF-8 binary sorted.

          - **EndMarker** *(string) --*

            The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
            binary sorted.

    - **LambdaResources** *(list) --*

      The Python-language Lambda functions for this job.

      - *(dict) --*

        Identifies

        - **LambdaArn** *(string) --*

          An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT
          object actions on the associated local Amazon S3 resource.

        - **EventTriggers** *(list) --*

          The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated
          with this job.

          - *(dict) --*

            The container for the  EventTriggerDefinition$EventResourceARN .

            - **EventResourceARN** *(string) --*

              The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
              function's event trigger associated with this job.

    - **Ec2AmiResources** *(list) --*

      The Amazon Machine Images (AMIs) associated with this job.

      - *(dict) --*

        A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including
        the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify
        identifying the AMI in both the AWS Cloud and on the device.

        - **AmiId** *(string) --* **[REQUIRED]**

          The ID of the AMI in Amazon EC2.

        - **SnowballAmiId** *(string) --*

          The ID of the AMI on the Snowball Edge device.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef", {"JobId": str}, total=False
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    Type definition for `ClientCreateJob` `Response`

    - **JobId** *(string) --*

      The automatically generated ID for a job, for example
      ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientDescribeAddressResponseAddressTypeDef = TypedDict(
    "_ClientDescribeAddressResponseAddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)


class ClientDescribeAddressResponseAddressTypeDef(
    _ClientDescribeAddressResponseAddressTypeDef
):
    """
    Type definition for `ClientDescribeAddressResponse` `Address`

    The address that you want the Snowball or Snowballs associated with a specific job to be
    shipped to.

    - **AddressId** *(string) --*

      The unique ID for an address.

    - **Name** *(string) --*

      The name of a person to receive a Snowball at an address.

    - **Company** *(string) --*

      The name of the company to receive a Snowball at an address.

    - **Street1** *(string) --*

      The first line in a street address that a Snowball is to be delivered to.

    - **Street2** *(string) --*

      The second line in a street address that a Snowball is to be delivered to.

    - **Street3** *(string) --*

      The third line in a street address that a Snowball is to be delivered to.

    - **City** *(string) --*

      The city in an address that a Snowball is to be delivered to.

    - **StateOrProvince** *(string) --*

      The state or province in an address that a Snowball is to be delivered to.

    - **PrefectureOrDistrict** *(string) --*

      This field is no longer used and the value is ignored.

    - **Landmark** *(string) --*

      This field is no longer used and the value is ignored.

    - **Country** *(string) --*

      The country in an address that a Snowball is to be delivered to.

    - **PostalCode** *(string) --*

      The postal code in an address that a Snowball is to be delivered to.

    - **PhoneNumber** *(string) --*

      The phone number associated with an address that a Snowball is to be delivered to.

    - **IsRestricted** *(boolean) --*

      If the address you are creating is a primary address, then set this option to true. This
      field is not supported in most regions.
    """


_ClientDescribeAddressResponseTypeDef = TypedDict(
    "_ClientDescribeAddressResponseTypeDef",
    {"Address": ClientDescribeAddressResponseAddressTypeDef},
    total=False,
)


class ClientDescribeAddressResponseTypeDef(_ClientDescribeAddressResponseTypeDef):
    """
    Type definition for `ClientDescribeAddress` `Response`

    - **Address** *(dict) --*

      The address that you want the Snowball or Snowballs associated with a specific job to be
      shipped to.

      - **AddressId** *(string) --*

        The unique ID for an address.

      - **Name** *(string) --*

        The name of a person to receive a Snowball at an address.

      - **Company** *(string) --*

        The name of the company to receive a Snowball at an address.

      - **Street1** *(string) --*

        The first line in a street address that a Snowball is to be delivered to.

      - **Street2** *(string) --*

        The second line in a street address that a Snowball is to be delivered to.

      - **Street3** *(string) --*

        The third line in a street address that a Snowball is to be delivered to.

      - **City** *(string) --*

        The city in an address that a Snowball is to be delivered to.

      - **StateOrProvince** *(string) --*

        The state or province in an address that a Snowball is to be delivered to.

      - **PrefectureOrDistrict** *(string) --*

        This field is no longer used and the value is ignored.

      - **Landmark** *(string) --*

        This field is no longer used and the value is ignored.

      - **Country** *(string) --*

        The country in an address that a Snowball is to be delivered to.

      - **PostalCode** *(string) --*

        The postal code in an address that a Snowball is to be delivered to.

      - **PhoneNumber** *(string) --*

        The phone number associated with an address that a Snowball is to be delivered to.

      - **IsRestricted** *(boolean) --*

        If the address you are creating is a primary address, then set this option to true. This
        field is not supported in most regions.
    """


_ClientDescribeAddressesResponseAddressesTypeDef = TypedDict(
    "_ClientDescribeAddressesResponseAddressesTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)


class ClientDescribeAddressesResponseAddressesTypeDef(
    _ClientDescribeAddressesResponseAddressesTypeDef
):
    """
    Type definition for `ClientDescribeAddressesResponse` `Addresses`

    The address that you want the Snowball or Snowballs associated with a specific job to be
    shipped to. Addresses are validated at the time of creation. The address you provide must
    be located within the serviceable area of your region. Although no individual elements of
    the ``Address`` are required, if the address is invalid or unsupported, then an exception
    is thrown.

    - **AddressId** *(string) --*

      The unique ID for an address.

    - **Name** *(string) --*

      The name of a person to receive a Snowball at an address.

    - **Company** *(string) --*

      The name of the company to receive a Snowball at an address.

    - **Street1** *(string) --*

      The first line in a street address that a Snowball is to be delivered to.

    - **Street2** *(string) --*

      The second line in a street address that a Snowball is to be delivered to.

    - **Street3** *(string) --*

      The third line in a street address that a Snowball is to be delivered to.

    - **City** *(string) --*

      The city in an address that a Snowball is to be delivered to.

    - **StateOrProvince** *(string) --*

      The state or province in an address that a Snowball is to be delivered to.

    - **PrefectureOrDistrict** *(string) --*

      This field is no longer used and the value is ignored.

    - **Landmark** *(string) --*

      This field is no longer used and the value is ignored.

    - **Country** *(string) --*

      The country in an address that a Snowball is to be delivered to.

    - **PostalCode** *(string) --*

      The postal code in an address that a Snowball is to be delivered to.

    - **PhoneNumber** *(string) --*

      The phone number associated with an address that a Snowball is to be delivered to.

    - **IsRestricted** *(boolean) --*

      If the address you are creating is a primary address, then set this option to true. This
      field is not supported in most regions.
    """


_ClientDescribeAddressesResponseTypeDef = TypedDict(
    "_ClientDescribeAddressesResponseTypeDef",
    {
        "Addresses": List[ClientDescribeAddressesResponseAddressesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAddressesResponseTypeDef(_ClientDescribeAddressesResponseTypeDef):
    """
    Type definition for `ClientDescribeAddresses` `Response`

    - **Addresses** *(list) --*

      The Snowball shipping addresses that were created for this account.

      - *(dict) --*

        The address that you want the Snowball or Snowballs associated with a specific job to be
        shipped to. Addresses are validated at the time of creation. The address you provide must
        be located within the serviceable area of your region. Although no individual elements of
        the ``Address`` are required, if the address is invalid or unsupported, then an exception
        is thrown.

        - **AddressId** *(string) --*

          The unique ID for an address.

        - **Name** *(string) --*

          The name of a person to receive a Snowball at an address.

        - **Company** *(string) --*

          The name of the company to receive a Snowball at an address.

        - **Street1** *(string) --*

          The first line in a street address that a Snowball is to be delivered to.

        - **Street2** *(string) --*

          The second line in a street address that a Snowball is to be delivered to.

        - **Street3** *(string) --*

          The third line in a street address that a Snowball is to be delivered to.

        - **City** *(string) --*

          The city in an address that a Snowball is to be delivered to.

        - **StateOrProvince** *(string) --*

          The state or province in an address that a Snowball is to be delivered to.

        - **PrefectureOrDistrict** *(string) --*

          This field is no longer used and the value is ignored.

        - **Landmark** *(string) --*

          This field is no longer used and the value is ignored.

        - **Country** *(string) --*

          The country in an address that a Snowball is to be delivered to.

        - **PostalCode** *(string) --*

          The postal code in an address that a Snowball is to be delivered to.

        - **PhoneNumber** *(string) --*

          The phone number associated with an address that a Snowball is to be delivered to.

        - **IsRestricted** *(boolean) --*

          If the address you are creating is a primary address, then set this option to true. This
          field is not supported in most regions.

    - **NextToken** *(string) --*

      HTTP requests are stateless. If you use the automatically generated ``NextToken`` value in
      your next ``DescribeAddresses`` call, your list of returned addresses will start from this
      point in the array.
    """


_ClientDescribeClusterResponseClusterMetadataNotificationTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataNotificationTypeDef",
    {"SnsTopicARN": str, "JobStatesToNotify": List[str], "NotifyAll": bool},
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataNotificationTypeDef(
    _ClientDescribeClusterResponseClusterMetadataNotificationTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterMetadata` `Notification`

    The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.

    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
      action.

      You can subscribe email addresses to an Amazon SNS topic through the AWS Management
      Console, or by using the `Subscribe
      <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
      Notification Service (SNS) API action.

    - **JobStatesToNotify** *(list) --*

      The list of job states that will trigger a notification for this job.

      - *(string) --*

    - **NotifyAll** *(boolean) --*

      Any change in job state will trigger a notification for this job.
    """


_ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterMetadataResources` `Ec2AmiResources`

    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
    including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
    IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

    - **AmiId** *(string) --*

      The ID of the AMI in Amazon EC2.

    - **SnowballAmiId** *(string) --*

      The ID of the AMI on the Snowball Edge device.
    """


_ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterMetadataResourcesLambdaResources` `EventTriggers`

    The container for the  EventTriggerDefinition$EventResourceARN .

    - **EventResourceARN** *(string) --*

      The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
      Lambda function's event trigger associated with this job.
    """


_ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterMetadataResources` `LambdaResources`

    Identifies

    - **LambdaArn** *(string) --*

      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered
      by PUT object actions on the associated local Amazon S3 resource.

    - **EventTriggers** *(list) --*

      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
      associated with this job.

      - *(dict) --*

        The container for the  EventTriggerDefinition$EventResourceARN .

        - **EventResourceARN** *(string) --*

          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
          Lambda function's event trigger associated with this job.
    """


_ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterMetadataResourcesS3Resources` `KeyRange`

    For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
    bucket. The length of the range is defined at job creation, and has either an
    inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
    binary sorted.

    - **BeginMarker** *(string) --*

      The key that starts an optional key range for an export job. Ranges are inclusive
      and UTF-8 binary sorted.

    - **EndMarker** *(string) --*

      The key that ends an optional key range for an export job. Ranges are inclusive and
      UTF-8 binary sorted.
    """


_ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterMetadataResources` `S3Resources`

    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
    will be exported from or imported into. For export jobs, this object can have an
    optional ``KeyRange`` value. The length of the range is defined at job creation, and
    has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges
    are UTF-8 binary sorted.

    - **BucketArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon S3 bucket.

    - **KeyRange** *(dict) --*

      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
      bucket. The length of the range is defined at job creation, and has either an
      inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
      binary sorted.

      - **BeginMarker** *(string) --*

        The key that starts an optional key range for an export job. Ranges are inclusive
        and UTF-8 binary sorted.

      - **EndMarker** *(string) --*

        The key that ends an optional key range for an export job. Ranges are inclusive and
        UTF-8 binary sorted.
    """


_ClientDescribeClusterResponseClusterMetadataResourcesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesTypeDef",
    {
        "S3Resources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef
        ],
        "LambdaResources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterMetadata` `Resources`

    The arrays of  JobResource objects that can include updated  S3Resource objects or
    LambdaResource objects.

    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.

      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
        will be exported from or imported into. For export jobs, this object can have an
        optional ``KeyRange`` value. The length of the range is defined at job creation, and
        has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges
        are UTF-8 binary sorted.

        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.

        - **KeyRange** *(dict) --*

          For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
          bucket. The length of the range is defined at job creation, and has either an
          inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
          binary sorted.

          - **BeginMarker** *(string) --*

            The key that starts an optional key range for an export job. Ranges are inclusive
            and UTF-8 binary sorted.

          - **EndMarker** *(string) --*

            The key that ends an optional key range for an export job. Ranges are inclusive and
            UTF-8 binary sorted.

    - **LambdaResources** *(list) --*

      The Python-language Lambda functions for this job.

      - *(dict) --*

        Identifies

        - **LambdaArn** *(string) --*

          An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered
          by PUT object actions on the associated local Amazon S3 resource.

        - **EventTriggers** *(list) --*

          The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
          associated with this job.

          - *(dict) --*

            The container for the  EventTriggerDefinition$EventResourceARN .

            - **EventResourceARN** *(string) --*

              The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
              Lambda function's event trigger associated with this job.

    - **Ec2AmiResources** *(list) --*

      The Amazon Machine Images (AMIs) associated with this job.

      - *(dict) --*

        A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
        including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
        IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

        - **AmiId** *(string) --*

          The ID of the AMI in Amazon EC2.

        - **SnowballAmiId** *(string) --*

          The ID of the AMI on the Snowball Edge device.
    """


_ClientDescribeClusterResponseClusterMetadataTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataTypeDef",
    {
        "ClusterId": str,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "ClusterState": str,
        "JobType": str,
        "SnowballType": str,
        "CreationDate": datetime,
        "Resources": ClientDescribeClusterResponseClusterMetadataResourcesTypeDef,
        "AddressId": str,
        "ShippingOption": str,
        "Notification": ClientDescribeClusterResponseClusterMetadataNotificationTypeDef,
        "ForwardingAddressId": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataTypeDef(
    _ClientDescribeClusterResponseClusterMetadataTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponse` `ClusterMetadata`

    Information about a specific cluster, including shipping information, cluster status, and
    other important metadata.

    - **ClusterId** *(string) --*

      The automatically generated ID for a cluster.

    - **Description** *(string) --*

      The optional description of the cluster.

    - **KmsKeyARN** *(string) --*

      The ``KmsKeyARN`` Amazon Resource Name (ARN) associated with this cluster. This ARN was
      created using the `CreateKey
      <https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in
      AWS Key Management Service (AWS KMS).

    - **RoleARN** *(string) --*

      The role ARN associated with this cluster. This ARN was created using the `CreateRole
      <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in
      AWS Identity and Access Management (IAM).

    - **ClusterState** *(string) --*

      The current status of the cluster.

    - **JobType** *(string) --*

      The type of job for this cluster. Currently, the only job type supported for clusters is
      ``LOCAL_USE`` .

    - **SnowballType** *(string) --*

      The type of AWS Snowball device to use for this cluster. Currently, the only supported
      device type for cluster jobs is ``EDGE`` .

    - **CreationDate** *(datetime) --*

      The creation date for this cluster.

    - **Resources** *(dict) --*

      The arrays of  JobResource objects that can include updated  S3Resource objects or
      LambdaResource objects.

      - **S3Resources** *(list) --*

        An array of ``S3Resource`` objects.

        - *(dict) --*

          Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
          will be exported from or imported into. For export jobs, this object can have an
          optional ``KeyRange`` value. The length of the range is defined at job creation, and
          has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges
          are UTF-8 binary sorted.

          - **BucketArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon S3 bucket.

          - **KeyRange** *(dict) --*

            For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
            bucket. The length of the range is defined at job creation, and has either an
            inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
            binary sorted.

            - **BeginMarker** *(string) --*

              The key that starts an optional key range for an export job. Ranges are inclusive
              and UTF-8 binary sorted.

            - **EndMarker** *(string) --*

              The key that ends an optional key range for an export job. Ranges are inclusive and
              UTF-8 binary sorted.

      - **LambdaResources** *(list) --*

        The Python-language Lambda functions for this job.

        - *(dict) --*

          Identifies

          - **LambdaArn** *(string) --*

            An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered
            by PUT object actions on the associated local Amazon S3 resource.

          - **EventTriggers** *(list) --*

            The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
            associated with this job.

            - *(dict) --*

              The container for the  EventTriggerDefinition$EventResourceARN .

              - **EventResourceARN** *(string) --*

                The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
                Lambda function's event trigger associated with this job.

      - **Ec2AmiResources** *(list) --*

        The Amazon Machine Images (AMIs) associated with this job.

        - *(dict) --*

          A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
          including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
          IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

          - **AmiId** *(string) --*

            The ID of the AMI in Amazon EC2.

          - **SnowballAmiId** *(string) --*

            The ID of the AMI on the Snowball Edge device.

    - **AddressId** *(string) --*

      The automatically generated ID for a specific address.

    - **ShippingOption** *(string) --*

      The shipping speed for each node in this cluster. This speed doesn't dictate how soon
      you'll get each Snowball Edge device, rather it represents how quickly each device moves to
      its destination while in transit. Regional shipping speeds are as follows:

      * In Australia, you have access to express shipping. Typically, devices shipped express are
      delivered in about a day.

      * In the European Union (EU), you have access to express shipping. Typically, Snowball
      Edges shipped express are delivered in about a day. In addition, most countries in the EU
      have access to standard shipping, which typically takes less than a week, one way.

      * In India, Snowball Edges are delivered in one to seven days.

      * In the US, you have access to one-day shipping and two-day shipping.

    - **Notification** *(dict) --*

      The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.

      - **SnsTopicARN** *(string) --*

        The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
        Resource Names (ARNs) for topics by using the `CreateTopic
        <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
        action.

        You can subscribe email addresses to an Amazon SNS topic through the AWS Management
        Console, or by using the `Subscribe
        <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
        Notification Service (SNS) API action.

      - **JobStatesToNotify** *(list) --*

        The list of job states that will trigger a notification for this job.

        - *(string) --*

      - **NotifyAll** *(boolean) --*

        Any change in job state will trigger a notification for this job.

    - **ForwardingAddressId** *(string) --*

      The ID of the address that you want a cluster shipped to, after it will be shipped to its
      primary address. This field is not supported in most regions.
    """


_ClientDescribeClusterResponseTypeDef = TypedDict(
    "_ClientDescribeClusterResponseTypeDef",
    {"ClusterMetadata": ClientDescribeClusterResponseClusterMetadataTypeDef},
    total=False,
)


class ClientDescribeClusterResponseTypeDef(_ClientDescribeClusterResponseTypeDef):
    """
    Type definition for `ClientDescribeCluster` `Response`

    - **ClusterMetadata** *(dict) --*

      Information about a specific cluster, including shipping information, cluster status, and
      other important metadata.

      - **ClusterId** *(string) --*

        The automatically generated ID for a cluster.

      - **Description** *(string) --*

        The optional description of the cluster.

      - **KmsKeyARN** *(string) --*

        The ``KmsKeyARN`` Amazon Resource Name (ARN) associated with this cluster. This ARN was
        created using the `CreateKey
        <https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in
        AWS Key Management Service (AWS KMS).

      - **RoleARN** *(string) --*

        The role ARN associated with this cluster. This ARN was created using the `CreateRole
        <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in
        AWS Identity and Access Management (IAM).

      - **ClusterState** *(string) --*

        The current status of the cluster.

      - **JobType** *(string) --*

        The type of job for this cluster. Currently, the only job type supported for clusters is
        ``LOCAL_USE`` .

      - **SnowballType** *(string) --*

        The type of AWS Snowball device to use for this cluster. Currently, the only supported
        device type for cluster jobs is ``EDGE`` .

      - **CreationDate** *(datetime) --*

        The creation date for this cluster.

      - **Resources** *(dict) --*

        The arrays of  JobResource objects that can include updated  S3Resource objects or
        LambdaResource objects.

        - **S3Resources** *(list) --*

          An array of ``S3Resource`` objects.

          - *(dict) --*

            Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
            will be exported from or imported into. For export jobs, this object can have an
            optional ``KeyRange`` value. The length of the range is defined at job creation, and
            has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges
            are UTF-8 binary sorted.

            - **BucketArn** *(string) --*

              The Amazon Resource Name (ARN) of an Amazon S3 bucket.

            - **KeyRange** *(dict) --*

              For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
              bucket. The length of the range is defined at job creation, and has either an
              inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
              binary sorted.

              - **BeginMarker** *(string) --*

                The key that starts an optional key range for an export job. Ranges are inclusive
                and UTF-8 binary sorted.

              - **EndMarker** *(string) --*

                The key that ends an optional key range for an export job. Ranges are inclusive and
                UTF-8 binary sorted.

        - **LambdaResources** *(list) --*

          The Python-language Lambda functions for this job.

          - *(dict) --*

            Identifies

            - **LambdaArn** *(string) --*

              An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered
              by PUT object actions on the associated local Amazon S3 resource.

            - **EventTriggers** *(list) --*

              The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
              associated with this job.

              - *(dict) --*

                The container for the  EventTriggerDefinition$EventResourceARN .

                - **EventResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
                  Lambda function's event trigger associated with this job.

        - **Ec2AmiResources** *(list) --*

          The Amazon Machine Images (AMIs) associated with this job.

          - *(dict) --*

            A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
            including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
            IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

            - **AmiId** *(string) --*

              The ID of the AMI in Amazon EC2.

            - **SnowballAmiId** *(string) --*

              The ID of the AMI on the Snowball Edge device.

      - **AddressId** *(string) --*

        The automatically generated ID for a specific address.

      - **ShippingOption** *(string) --*

        The shipping speed for each node in this cluster. This speed doesn't dictate how soon
        you'll get each Snowball Edge device, rather it represents how quickly each device moves to
        its destination while in transit. Regional shipping speeds are as follows:

        * In Australia, you have access to express shipping. Typically, devices shipped express are
        delivered in about a day.

        * In the European Union (EU), you have access to express shipping. Typically, Snowball
        Edges shipped express are delivered in about a day. In addition, most countries in the EU
        have access to standard shipping, which typically takes less than a week, one way.

        * In India, Snowball Edges are delivered in one to seven days.

        * In the US, you have access to one-day shipping and two-day shipping.

      - **Notification** *(dict) --*

        The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.

        - **SnsTopicARN** *(string) --*

          The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
          Resource Names (ARNs) for topics by using the `CreateTopic
          <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
          action.

          You can subscribe email addresses to an Amazon SNS topic through the AWS Management
          Console, or by using the `Subscribe
          <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
          Notification Service (SNS) API action.

        - **JobStatesToNotify** *(list) --*

          The list of job states that will trigger a notification for this job.

          - *(string) --*

        - **NotifyAll** *(boolean) --*

          Any change in job state will trigger a notification for this job.

      - **ForwardingAddressId** *(string) --*

        The ID of the address that you want a cluster shipped to, after it will be shipped to its
        primary address. This field is not supported in most regions.
    """


_ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef",
    {
        "BytesTransferred": int,
        "ObjectsTransferred": int,
        "TotalBytes": int,
        "TotalObjects": int,
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef(
    _ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadata` `DataTransferProgress`

    A value that defines the real-time status of a Snowball's data transfer while the device is
    at AWS. This data is only available while a job has a ``JobState`` value of ``InProgress``
    , for both import and export jobs.

    - **BytesTransferred** *(integer) --*

      The number of bytes transferred between a Snowball and Amazon S3.

    - **ObjectsTransferred** *(integer) --*

      The number of objects transferred between a Snowball and Amazon S3.

    - **TotalBytes** *(integer) --*

      The total bytes of data for a transfer between a Snowball and Amazon S3. This value is
      set to 0 (zero) until all the keys that will be transferred have been listed.

    - **TotalObjects** *(integer) --*

      The total number of objects for a transfer between a Snowball and Amazon S3. This value
      is set to 0 (zero) until all the keys that will be transferred have been listed.
    """


_ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef",
    {"JobCompletionReportURI": str, "JobSuccessLogURI": str, "JobFailureLogURI": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef(
    _ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadata` `JobLogInfo`

    Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job
    report becomes available at the end of the import process. For export jobs, your job report
    typically becomes available while the Snowball for your job part is being delivered to you.

    - **JobCompletionReportURI** *(string) --*

      A link to an Amazon S3 presigned URL where the job completion report is located.

    - **JobSuccessLogURI** *(string) --*

      A link to an Amazon S3 presigned URL where the job success log is located.

    - **JobFailureLogURI** *(string) --*

      A link to an Amazon S3 presigned URL where the job failure log is located.
    """


_ClientDescribeJobResponseJobMetadataNotificationTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataNotificationTypeDef",
    {"SnsTopicARN": str, "JobStatesToNotify": List[str], "NotifyAll": bool},
    total=False,
)


class ClientDescribeJobResponseJobMetadataNotificationTypeDef(
    _ClientDescribeJobResponseJobMetadataNotificationTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadata` `Notification`

    The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a
    specific job. The ``Notification`` object is returned as a part of the response syntax of
    the ``DescribeJob`` action in the ``JobMetadata`` data type.

    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
      action.

      You can subscribe email addresses to an Amazon SNS topic through the AWS Management
      Console, or by using the `Subscribe
      <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
      Notification Service (SNS) API action.

    - **JobStatesToNotify** *(list) --*

      The list of job states that will trigger a notification for this job.

      - *(string) --*

    - **NotifyAll** *(boolean) --*

      Any change in job state will trigger a notification for this job.
    """


_ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadataResources` `Ec2AmiResources`

    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
    including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
    IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

    - **AmiId** *(string) --*

      The ID of the AMI in Amazon EC2.

    - **SnowballAmiId** *(string) --*

      The ID of the AMI on the Snowball Edge device.
    """


_ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadataResourcesLambdaResources` `EventTriggers`

    The container for the  EventTriggerDefinition$EventResourceARN .

    - **EventResourceARN** *(string) --*

      The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
      Lambda function's event trigger associated with this job.
    """


_ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadataResources` `LambdaResources`

    Identifies

    - **LambdaArn** *(string) --*

      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered
      by PUT object actions on the associated local Amazon S3 resource.

    - **EventTriggers** *(list) --*

      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
      associated with this job.

      - *(dict) --*

        The container for the  EventTriggerDefinition$EventResourceARN .

        - **EventResourceARN** *(string) --*

          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
          Lambda function's event trigger associated with this job.
    """


_ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadataResourcesS3Resources` `KeyRange`

    For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
    bucket. The length of the range is defined at job creation, and has either an
    inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
    binary sorted.

    - **BeginMarker** *(string) --*

      The key that starts an optional key range for an export job. Ranges are inclusive
      and UTF-8 binary sorted.

    - **EndMarker** *(string) --*

      The key that ends an optional key range for an export job. Ranges are inclusive and
      UTF-8 binary sorted.
    """


_ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadataResources` `S3Resources`

    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
    will be exported from or imported into. For export jobs, this object can have an
    optional ``KeyRange`` value. The length of the range is defined at job creation, and
    has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges
    are UTF-8 binary sorted.

    - **BucketArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon S3 bucket.

    - **KeyRange** *(dict) --*

      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
      bucket. The length of the range is defined at job creation, and has either an
      inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
      binary sorted.

      - **BeginMarker** *(string) --*

        The key that starts an optional key range for an export job. Ranges are inclusive
        and UTF-8 binary sorted.

      - **EndMarker** *(string) --*

        The key that ends an optional key range for an export job. Ranges are inclusive and
        UTF-8 binary sorted.
    """


_ClientDescribeJobResponseJobMetadataResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesTypeDef",
    {
        "S3Resources": List[
            ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef
        ],
        "LambdaResources": List[
            ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadata` `Resources`

    An array of ``S3Resource`` objects. Each ``S3Resource`` object represents an Amazon S3
    bucket that your transferred data will be exported from or imported into.

    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.

      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
        will be exported from or imported into. For export jobs, this object can have an
        optional ``KeyRange`` value. The length of the range is defined at job creation, and
        has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges
        are UTF-8 binary sorted.

        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.

        - **KeyRange** *(dict) --*

          For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
          bucket. The length of the range is defined at job creation, and has either an
          inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
          binary sorted.

          - **BeginMarker** *(string) --*

            The key that starts an optional key range for an export job. Ranges are inclusive
            and UTF-8 binary sorted.

          - **EndMarker** *(string) --*

            The key that ends an optional key range for an export job. Ranges are inclusive and
            UTF-8 binary sorted.

    - **LambdaResources** *(list) --*

      The Python-language Lambda functions for this job.

      - *(dict) --*

        Identifies

        - **LambdaArn** *(string) --*

          An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered
          by PUT object actions on the associated local Amazon S3 resource.

        - **EventTriggers** *(list) --*

          The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
          associated with this job.

          - *(dict) --*

            The container for the  EventTriggerDefinition$EventResourceARN .

            - **EventResourceARN** *(string) --*

              The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
              Lambda function's event trigger associated with this job.

    - **Ec2AmiResources** *(list) --*

      The Amazon Machine Images (AMIs) associated with this job.

      - *(dict) --*

        A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
        including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
        IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

        - **AmiId** *(string) --*

          The ID of the AMI in Amazon EC2.

        - **SnowballAmiId** *(string) --*

          The ID of the AMI on the Snowball Edge device.
    """


_ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef(
    _ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadataShippingDetails` `InboundShipment`

    The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a
    particular job.

    - **Status** *(string) --*

      Status information for a shipment.

    - **TrackingNumber** *(string) --*

      The tracking number for this job. Using this tracking number with your region's
      carrier's website, you can track a Snowball as the carrier transports it.

      For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
    """


_ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef(
    _ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadataShippingDetails` `OutboundShipment`

    The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the
    address that you specified for a particular job.

    - **Status** *(string) --*

      Status information for a shipment.

    - **TrackingNumber** *(string) --*

      The tracking number for this job. Using this tracking number with your region's
      carrier's website, you can track a Snowball as the carrier transports it.

      For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
    """


_ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef",
    {
        "ShippingOption": str,
        "InboundShipment": ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef,
        "OutboundShipment": ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef(
    _ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobMetadata` `ShippingDetails`

    A job's shipping information, including inbound and outbound tracking numbers and shipping
    speed options.

    - **ShippingOption** *(string) --*

      The shipping speed for a particular job. This speed doesn't dictate how soon you'll get
      the Snowball from the job's creation date. This speed represents how quickly it moves to
      its destination while in transit. Regional shipping speeds are as follows:

      * In Australia, you have access to express shipping. Typically, Snowballs shipped express
      are delivered in about a day.

      * In the European Union (EU), you have access to express shipping. Typically, Snowballs
      shipped express are delivered in about a day. In addition, most countries in the EU have
      access to standard shipping, which typically takes less than a week, one way.

      * In India, Snowballs are delivered in one to seven days.

      * In the United States of America (US), you have access to one-day shipping and two-day
      shipping.

    - **InboundShipment** *(dict) --*

      The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a
      particular job.

      - **Status** *(string) --*

        Status information for a shipment.

      - **TrackingNumber** *(string) --*

        The tracking number for this job. Using this tracking number with your region's
        carrier's website, you can track a Snowball as the carrier transports it.

        For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

    - **OutboundShipment** *(dict) --*

      The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the
      address that you specified for a particular job.

      - **Status** *(string) --*

        Status information for a shipment.

      - **TrackingNumber** *(string) --*

        The tracking number for this job. Using this tracking number with your region's
        carrier's website, you can track a Snowball as the carrier transports it.

        For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
    """


_ClientDescribeJobResponseJobMetadataTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": str,
        "JobType": str,
        "SnowballType": str,
        "CreationDate": datetime,
        "Resources": ClientDescribeJobResponseJobMetadataResourcesTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef,
        "SnowballCapacityPreference": str,
        "Notification": ClientDescribeJobResponseJobMetadataNotificationTypeDef,
        "DataTransferProgress": ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef,
        "JobLogInfo": ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef,
        "ClusterId": str,
        "ForwardingAddressId": str,
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataTypeDef(
    _ClientDescribeJobResponseJobMetadataTypeDef
):
    """
    Type definition for `ClientDescribeJobResponse` `JobMetadata`

    Information about a specific job, including shipping information, job status, and other
    important metadata.

    - **JobId** *(string) --*

      The automatically generated ID for a job, for example
      ``JID123e4567-e89b-12d3-a456-426655440000`` .

    - **JobState** *(string) --*

      The current status of the jobs.

    - **JobType** *(string) --*

      The type of job.

    - **SnowballType** *(string) --*

      The type of device used with this job.

    - **CreationDate** *(datetime) --*

      The creation date for this job.

    - **Resources** *(dict) --*

      An array of ``S3Resource`` objects. Each ``S3Resource`` object represents an Amazon S3
      bucket that your transferred data will be exported from or imported into.

      - **S3Resources** *(list) --*

        An array of ``S3Resource`` objects.

        - *(dict) --*

          Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
          will be exported from or imported into. For export jobs, this object can have an
          optional ``KeyRange`` value. The length of the range is defined at job creation, and
          has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges
          are UTF-8 binary sorted.

          - **BucketArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon S3 bucket.

          - **KeyRange** *(dict) --*

            For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
            bucket. The length of the range is defined at job creation, and has either an
            inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
            binary sorted.

            - **BeginMarker** *(string) --*

              The key that starts an optional key range for an export job. Ranges are inclusive
              and UTF-8 binary sorted.

            - **EndMarker** *(string) --*

              The key that ends an optional key range for an export job. Ranges are inclusive and
              UTF-8 binary sorted.

      - **LambdaResources** *(list) --*

        The Python-language Lambda functions for this job.

        - *(dict) --*

          Identifies

          - **LambdaArn** *(string) --*

            An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered
            by PUT object actions on the associated local Amazon S3 resource.

          - **EventTriggers** *(list) --*

            The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
            associated with this job.

            - *(dict) --*

              The container for the  EventTriggerDefinition$EventResourceARN .

              - **EventResourceARN** *(string) --*

                The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
                Lambda function's event trigger associated with this job.

      - **Ec2AmiResources** *(list) --*

        The Amazon Machine Images (AMIs) associated with this job.

        - *(dict) --*

          A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
          including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
          IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

          - **AmiId** *(string) --*

            The ID of the AMI in Amazon EC2.

          - **SnowballAmiId** *(string) --*

            The ID of the AMI on the Snowball Edge device.

    - **Description** *(string) --*

      The description of the job, provided at job creation.

    - **KmsKeyARN** *(string) --*

      The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated
      with this job. This ARN was created using the `CreateKey
      <https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in
      AWS KMS.

    - **RoleARN** *(string) --*

      The role ARN associated with this job. This ARN was created using the `CreateRole
      <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in
      AWS Identity and Access Management (IAM).

    - **AddressId** *(string) --*

      The ID for the address that you want the Snowball shipped to.

    - **ShippingDetails** *(dict) --*

      A job's shipping information, including inbound and outbound tracking numbers and shipping
      speed options.

      - **ShippingOption** *(string) --*

        The shipping speed for a particular job. This speed doesn't dictate how soon you'll get
        the Snowball from the job's creation date. This speed represents how quickly it moves to
        its destination while in transit. Regional shipping speeds are as follows:

        * In Australia, you have access to express shipping. Typically, Snowballs shipped express
        are delivered in about a day.

        * In the European Union (EU), you have access to express shipping. Typically, Snowballs
        shipped express are delivered in about a day. In addition, most countries in the EU have
        access to standard shipping, which typically takes less than a week, one way.

        * In India, Snowballs are delivered in one to seven days.

        * In the United States of America (US), you have access to one-day shipping and two-day
        shipping.

      - **InboundShipment** *(dict) --*

        The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a
        particular job.

        - **Status** *(string) --*

          Status information for a shipment.

        - **TrackingNumber** *(string) --*

          The tracking number for this job. Using this tracking number with your region's
          carrier's website, you can track a Snowball as the carrier transports it.

          For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

      - **OutboundShipment** *(dict) --*

        The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the
        address that you specified for a particular job.

        - **Status** *(string) --*

          Status information for a shipment.

        - **TrackingNumber** *(string) --*

          The tracking number for this job. Using this tracking number with your region's
          carrier's website, you can track a Snowball as the carrier transports it.

          For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

    - **SnowballCapacityPreference** *(string) --*

      The Snowball capacity preference for this job, specified at job creation. In US regions,
      you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity
      Snowballs.

    - **Notification** *(dict) --*

      The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a
      specific job. The ``Notification`` object is returned as a part of the response syntax of
      the ``DescribeJob`` action in the ``JobMetadata`` data type.

      - **SnsTopicARN** *(string) --*

        The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
        Resource Names (ARNs) for topics by using the `CreateTopic
        <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
        action.

        You can subscribe email addresses to an Amazon SNS topic through the AWS Management
        Console, or by using the `Subscribe
        <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
        Notification Service (SNS) API action.

      - **JobStatesToNotify** *(list) --*

        The list of job states that will trigger a notification for this job.

        - *(string) --*

      - **NotifyAll** *(boolean) --*

        Any change in job state will trigger a notification for this job.

    - **DataTransferProgress** *(dict) --*

      A value that defines the real-time status of a Snowball's data transfer while the device is
      at AWS. This data is only available while a job has a ``JobState`` value of ``InProgress``
      , for both import and export jobs.

      - **BytesTransferred** *(integer) --*

        The number of bytes transferred between a Snowball and Amazon S3.

      - **ObjectsTransferred** *(integer) --*

        The number of objects transferred between a Snowball and Amazon S3.

      - **TotalBytes** *(integer) --*

        The total bytes of data for a transfer between a Snowball and Amazon S3. This value is
        set to 0 (zero) until all the keys that will be transferred have been listed.

      - **TotalObjects** *(integer) --*

        The total number of objects for a transfer between a Snowball and Amazon S3. This value
        is set to 0 (zero) until all the keys that will be transferred have been listed.

    - **JobLogInfo** *(dict) --*

      Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job
      report becomes available at the end of the import process. For export jobs, your job report
      typically becomes available while the Snowball for your job part is being delivered to you.

      - **JobCompletionReportURI** *(string) --*

        A link to an Amazon S3 presigned URL where the job completion report is located.

      - **JobSuccessLogURI** *(string) --*

        A link to an Amazon S3 presigned URL where the job success log is located.

      - **JobFailureLogURI** *(string) --*

        A link to an Amazon S3 presigned URL where the job failure log is located.

    - **ClusterId** *(string) --*

      The 39-character ID for the cluster, for example
      ``CID123e4567-e89b-12d3-a456-426655440000`` .

    - **ForwardingAddressId** *(string) --*

      The ID of the address that you want a job shipped to, after it will be shipped to its
      primary address. This field is not supported in most regions.
    """


_ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef",
    {
        "BytesTransferred": int,
        "ObjectsTransferred": int,
        "TotalBytes": int,
        "TotalObjects": int,
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef(
    _ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadata` `DataTransferProgress`

    A value that defines the real-time status of a Snowball's data transfer while the device
    is at AWS. This data is only available while a job has a ``JobState`` value of
    ``InProgress`` , for both import and export jobs.

    - **BytesTransferred** *(integer) --*

      The number of bytes transferred between a Snowball and Amazon S3.

    - **ObjectsTransferred** *(integer) --*

      The number of objects transferred between a Snowball and Amazon S3.

    - **TotalBytes** *(integer) --*

      The total bytes of data for a transfer between a Snowball and Amazon S3. This value is
      set to 0 (zero) until all the keys that will be transferred have been listed.

    - **TotalObjects** *(integer) --*

      The total number of objects for a transfer between a Snowball and Amazon S3. This value
      is set to 0 (zero) until all the keys that will be transferred have been listed.
    """


_ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef",
    {"JobCompletionReportURI": str, "JobSuccessLogURI": str, "JobFailureLogURI": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef(
    _ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadata` `JobLogInfo`

    Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF
    job report becomes available at the end of the import process. For export jobs, your job
    report typically becomes available while the Snowball for your job part is being
    delivered to you.

    - **JobCompletionReportURI** *(string) --*

      A link to an Amazon S3 presigned URL where the job completion report is located.

    - **JobSuccessLogURI** *(string) --*

      A link to an Amazon S3 presigned URL where the job success log is located.

    - **JobFailureLogURI** *(string) --*

      A link to an Amazon S3 presigned URL where the job failure log is located.
    """


_ClientDescribeJobResponseSubJobMetadataNotificationTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataNotificationTypeDef",
    {"SnsTopicARN": str, "JobStatesToNotify": List[str], "NotifyAll": bool},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataNotificationTypeDef(
    _ClientDescribeJobResponseSubJobMetadataNotificationTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadata` `Notification`

    The Amazon Simple Notification Service (Amazon SNS) notification settings associated with
    a specific job. The ``Notification`` object is returned as a part of the response syntax
    of the ``DescribeJob`` action in the ``JobMetadata`` data type.

    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create
      Amazon Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
      action.

      You can subscribe email addresses to an Amazon SNS topic through the AWS Management
      Console, or by using the `Subscribe
      <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
      Notification Service (SNS) API action.

    - **JobStatesToNotify** *(list) --*

      The list of job states that will trigger a notification for this job.

      - *(string) --*

    - **NotifyAll** *(boolean) --*

      Any change in job state will trigger a notification for this job.
    """


_ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadataResources` `Ec2AmiResources`

    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
    including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
    IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

    - **AmiId** *(string) --*

      The ID of the AMI in Amazon EC2.

    - **SnowballAmiId** *(string) --*

      The ID of the AMI on the Snowball Edge device.
    """


_ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadataResourcesLambdaResources` `EventTriggers`

    The container for the  EventTriggerDefinition$EventResourceARN .

    - **EventResourceARN** *(string) --*

      The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
      Lambda function's event trigger associated with this job.
    """


_ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadataResources` `LambdaResources`

    Identifies

    - **LambdaArn** *(string) --*

      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be
      triggered by PUT object actions on the associated local Amazon S3 resource.

    - **EventTriggers** *(list) --*

      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
      associated with this job.

      - *(dict) --*

        The container for the  EventTriggerDefinition$EventResourceARN .

        - **EventResourceARN** *(string) --*

          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
          Lambda function's event trigger associated with this job.
    """


_ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadataResourcesS3Resources` `KeyRange`

    For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon
    S3 bucket. The length of the range is defined at job creation, and has either an
    inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
    binary sorted.

    - **BeginMarker** *(string) --*

      The key that starts an optional key range for an export job. Ranges are inclusive
      and UTF-8 binary sorted.

    - **EndMarker** *(string) --*

      The key that ends an optional key range for an export job. Ranges are inclusive
      and UTF-8 binary sorted.
    """


_ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadataResources` `S3Resources`

    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
    will be exported from or imported into. For export jobs, this object can have an
    optional ``KeyRange`` value. The length of the range is defined at job creation, and
    has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both.
    Ranges are UTF-8 binary sorted.

    - **BucketArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon S3 bucket.

    - **KeyRange** *(dict) --*

      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon
      S3 bucket. The length of the range is defined at job creation, and has either an
      inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
      binary sorted.

      - **BeginMarker** *(string) --*

        The key that starts an optional key range for an export job. Ranges are inclusive
        and UTF-8 binary sorted.

      - **EndMarker** *(string) --*

        The key that ends an optional key range for an export job. Ranges are inclusive
        and UTF-8 binary sorted.
    """


_ClientDescribeJobResponseSubJobMetadataResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesTypeDef",
    {
        "S3Resources": List[
            ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef
        ],
        "LambdaResources": List[
            ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadata` `Resources`

    An array of ``S3Resource`` objects. Each ``S3Resource`` object represents an Amazon S3
    bucket that your transferred data will be exported from or imported into.

    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.

      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
        will be exported from or imported into. For export jobs, this object can have an
        optional ``KeyRange`` value. The length of the range is defined at job creation, and
        has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both.
        Ranges are UTF-8 binary sorted.

        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.

        - **KeyRange** *(dict) --*

          For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon
          S3 bucket. The length of the range is defined at job creation, and has either an
          inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
          binary sorted.

          - **BeginMarker** *(string) --*

            The key that starts an optional key range for an export job. Ranges are inclusive
            and UTF-8 binary sorted.

          - **EndMarker** *(string) --*

            The key that ends an optional key range for an export job. Ranges are inclusive
            and UTF-8 binary sorted.

    - **LambdaResources** *(list) --*

      The Python-language Lambda functions for this job.

      - *(dict) --*

        Identifies

        - **LambdaArn** *(string) --*

          An Amazon Resource Name (ARN) that represents an AWS Lambda function to be
          triggered by PUT object actions on the associated local Amazon S3 resource.

        - **EventTriggers** *(list) --*

          The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
          associated with this job.

          - *(dict) --*

            The container for the  EventTriggerDefinition$EventResourceARN .

            - **EventResourceARN** *(string) --*

              The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
              Lambda function's event trigger associated with this job.

    - **Ec2AmiResources** *(list) --*

      The Amazon Machine Images (AMIs) associated with this job.

      - *(dict) --*

        A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
        including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
        IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

        - **AmiId** *(string) --*

          The ID of the AMI in Amazon EC2.

        - **SnowballAmiId** *(string) --*

          The ID of the AMI on the Snowball Edge device.
    """


_ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef(
    _ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadataShippingDetails` `InboundShipment`

    The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a
    particular job.

    - **Status** *(string) --*

      Status information for a shipment.

    - **TrackingNumber** *(string) --*

      The tracking number for this job. Using this tracking number with your region's
      carrier's website, you can track a Snowball as the carrier transports it.

      For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
    """


_ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef(
    _ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadataShippingDetails` `OutboundShipment`

    The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the
    address that you specified for a particular job.

    - **Status** *(string) --*

      Status information for a shipment.

    - **TrackingNumber** *(string) --*

      The tracking number for this job. Using this tracking number with your region's
      carrier's website, you can track a Snowball as the carrier transports it.

      For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
    """


_ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef",
    {
        "ShippingOption": str,
        "InboundShipment": ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef,
        "OutboundShipment": ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef(
    _ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSubJobMetadata` `ShippingDetails`

    A job's shipping information, including inbound and outbound tracking numbers and
    shipping speed options.

    - **ShippingOption** *(string) --*

      The shipping speed for a particular job. This speed doesn't dictate how soon you'll get
      the Snowball from the job's creation date. This speed represents how quickly it moves
      to its destination while in transit. Regional shipping speeds are as follows:

      * In Australia, you have access to express shipping. Typically, Snowballs shipped
      express are delivered in about a day.

      * In the European Union (EU), you have access to express shipping. Typically, Snowballs
      shipped express are delivered in about a day. In addition, most countries in the EU
      have access to standard shipping, which typically takes less than a week, one way.

      * In India, Snowballs are delivered in one to seven days.

      * In the United States of America (US), you have access to one-day shipping and two-day
      shipping.

    - **InboundShipment** *(dict) --*

      The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a
      particular job.

      - **Status** *(string) --*

        Status information for a shipment.

      - **TrackingNumber** *(string) --*

        The tracking number for this job. Using this tracking number with your region's
        carrier's website, you can track a Snowball as the carrier transports it.

        For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

    - **OutboundShipment** *(dict) --*

      The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the
      address that you specified for a particular job.

      - **Status** *(string) --*

        Status information for a shipment.

      - **TrackingNumber** *(string) --*

        The tracking number for this job. Using this tracking number with your region's
        carrier's website, you can track a Snowball as the carrier transports it.

        For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
    """


_ClientDescribeJobResponseSubJobMetadataTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": str,
        "JobType": str,
        "SnowballType": str,
        "CreationDate": datetime,
        "Resources": ClientDescribeJobResponseSubJobMetadataResourcesTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef,
        "SnowballCapacityPreference": str,
        "Notification": ClientDescribeJobResponseSubJobMetadataNotificationTypeDef,
        "DataTransferProgress": ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef,
        "JobLogInfo": ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef,
        "ClusterId": str,
        "ForwardingAddressId": str,
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataTypeDef(
    _ClientDescribeJobResponseSubJobMetadataTypeDef
):
    """
    Type definition for `ClientDescribeJobResponse` `SubJobMetadata`

    Contains information about a specific job including shipping information, job status, and
    other important metadata. This information is returned as a part of the response syntax of
    the ``DescribeJob`` action.

    - **JobId** *(string) --*

      The automatically generated ID for a job, for example
      ``JID123e4567-e89b-12d3-a456-426655440000`` .

    - **JobState** *(string) --*

      The current status of the jobs.

    - **JobType** *(string) --*

      The type of job.

    - **SnowballType** *(string) --*

      The type of device used with this job.

    - **CreationDate** *(datetime) --*

      The creation date for this job.

    - **Resources** *(dict) --*

      An array of ``S3Resource`` objects. Each ``S3Resource`` object represents an Amazon S3
      bucket that your transferred data will be exported from or imported into.

      - **S3Resources** *(list) --*

        An array of ``S3Resource`` objects.

        - *(dict) --*

          Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
          will be exported from or imported into. For export jobs, this object can have an
          optional ``KeyRange`` value. The length of the range is defined at job creation, and
          has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both.
          Ranges are UTF-8 binary sorted.

          - **BucketArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon S3 bucket.

          - **KeyRange** *(dict) --*

            For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon
            S3 bucket. The length of the range is defined at job creation, and has either an
            inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
            binary sorted.

            - **BeginMarker** *(string) --*

              The key that starts an optional key range for an export job. Ranges are inclusive
              and UTF-8 binary sorted.

            - **EndMarker** *(string) --*

              The key that ends an optional key range for an export job. Ranges are inclusive
              and UTF-8 binary sorted.

      - **LambdaResources** *(list) --*

        The Python-language Lambda functions for this job.

        - *(dict) --*

          Identifies

          - **LambdaArn** *(string) --*

            An Amazon Resource Name (ARN) that represents an AWS Lambda function to be
            triggered by PUT object actions on the associated local Amazon S3 resource.

          - **EventTriggers** *(list) --*

            The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
            associated with this job.

            - *(dict) --*

              The container for the  EventTriggerDefinition$EventResourceARN .

              - **EventResourceARN** *(string) --*

                The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
                Lambda function's event trigger associated with this job.

      - **Ec2AmiResources** *(list) --*

        The Amazon Machine Images (AMIs) associated with this job.

        - *(dict) --*

          A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
          including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
          IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

          - **AmiId** *(string) --*

            The ID of the AMI in Amazon EC2.

          - **SnowballAmiId** *(string) --*

            The ID of the AMI on the Snowball Edge device.

    - **Description** *(string) --*

      The description of the job, provided at job creation.

    - **KmsKeyARN** *(string) --*

      The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key
      associated with this job. This ARN was created using the `CreateKey
      <https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in
      AWS KMS.

    - **RoleARN** *(string) --*

      The role ARN associated with this job. This ARN was created using the `CreateRole
      <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action
      in AWS Identity and Access Management (IAM).

    - **AddressId** *(string) --*

      The ID for the address that you want the Snowball shipped to.

    - **ShippingDetails** *(dict) --*

      A job's shipping information, including inbound and outbound tracking numbers and
      shipping speed options.

      - **ShippingOption** *(string) --*

        The shipping speed for a particular job. This speed doesn't dictate how soon you'll get
        the Snowball from the job's creation date. This speed represents how quickly it moves
        to its destination while in transit. Regional shipping speeds are as follows:

        * In Australia, you have access to express shipping. Typically, Snowballs shipped
        express are delivered in about a day.

        * In the European Union (EU), you have access to express shipping. Typically, Snowballs
        shipped express are delivered in about a day. In addition, most countries in the EU
        have access to standard shipping, which typically takes less than a week, one way.

        * In India, Snowballs are delivered in one to seven days.

        * In the United States of America (US), you have access to one-day shipping and two-day
        shipping.

      - **InboundShipment** *(dict) --*

        The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a
        particular job.

        - **Status** *(string) --*

          Status information for a shipment.

        - **TrackingNumber** *(string) --*

          The tracking number for this job. Using this tracking number with your region's
          carrier's website, you can track a Snowball as the carrier transports it.

          For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

      - **OutboundShipment** *(dict) --*

        The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the
        address that you specified for a particular job.

        - **Status** *(string) --*

          Status information for a shipment.

        - **TrackingNumber** *(string) --*

          The tracking number for this job. Using this tracking number with your region's
          carrier's website, you can track a Snowball as the carrier transports it.

          For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

    - **SnowballCapacityPreference** *(string) --*

      The Snowball capacity preference for this job, specified at job creation. In US regions,
      you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity
      Snowballs.

    - **Notification** *(dict) --*

      The Amazon Simple Notification Service (Amazon SNS) notification settings associated with
      a specific job. The ``Notification`` object is returned as a part of the response syntax
      of the ``DescribeJob`` action in the ``JobMetadata`` data type.

      - **SnsTopicARN** *(string) --*

        The new SNS ``TopicArn`` that you want to associate with this job. You can create
        Amazon Resource Names (ARNs) for topics by using the `CreateTopic
        <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
        action.

        You can subscribe email addresses to an Amazon SNS topic through the AWS Management
        Console, or by using the `Subscribe
        <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
        Notification Service (SNS) API action.

      - **JobStatesToNotify** *(list) --*

        The list of job states that will trigger a notification for this job.

        - *(string) --*

      - **NotifyAll** *(boolean) --*

        Any change in job state will trigger a notification for this job.

    - **DataTransferProgress** *(dict) --*

      A value that defines the real-time status of a Snowball's data transfer while the device
      is at AWS. This data is only available while a job has a ``JobState`` value of
      ``InProgress`` , for both import and export jobs.

      - **BytesTransferred** *(integer) --*

        The number of bytes transferred between a Snowball and Amazon S3.

      - **ObjectsTransferred** *(integer) --*

        The number of objects transferred between a Snowball and Amazon S3.

      - **TotalBytes** *(integer) --*

        The total bytes of data for a transfer between a Snowball and Amazon S3. This value is
        set to 0 (zero) until all the keys that will be transferred have been listed.

      - **TotalObjects** *(integer) --*

        The total number of objects for a transfer between a Snowball and Amazon S3. This value
        is set to 0 (zero) until all the keys that will be transferred have been listed.

    - **JobLogInfo** *(dict) --*

      Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF
      job report becomes available at the end of the import process. For export jobs, your job
      report typically becomes available while the Snowball for your job part is being
      delivered to you.

      - **JobCompletionReportURI** *(string) --*

        A link to an Amazon S3 presigned URL where the job completion report is located.

      - **JobSuccessLogURI** *(string) --*

        A link to an Amazon S3 presigned URL where the job success log is located.

      - **JobFailureLogURI** *(string) --*

        A link to an Amazon S3 presigned URL where the job failure log is located.

    - **ClusterId** *(string) --*

      The 39-character ID for the cluster, for example
      ``CID123e4567-e89b-12d3-a456-426655440000`` .

    - **ForwardingAddressId** *(string) --*

      The ID of the address that you want a job shipped to, after it will be shipped to its
      primary address. This field is not supported in most regions.
    """


_ClientDescribeJobResponseTypeDef = TypedDict(
    "_ClientDescribeJobResponseTypeDef",
    {
        "JobMetadata": ClientDescribeJobResponseJobMetadataTypeDef,
        "SubJobMetadata": List[ClientDescribeJobResponseSubJobMetadataTypeDef],
    },
    total=False,
)


class ClientDescribeJobResponseTypeDef(_ClientDescribeJobResponseTypeDef):
    """
    Type definition for `ClientDescribeJob` `Response`

    - **JobMetadata** *(dict) --*

      Information about a specific job, including shipping information, job status, and other
      important metadata.

      - **JobId** *(string) --*

        The automatically generated ID for a job, for example
        ``JID123e4567-e89b-12d3-a456-426655440000`` .

      - **JobState** *(string) --*

        The current status of the jobs.

      - **JobType** *(string) --*

        The type of job.

      - **SnowballType** *(string) --*

        The type of device used with this job.

      - **CreationDate** *(datetime) --*

        The creation date for this job.

      - **Resources** *(dict) --*

        An array of ``S3Resource`` objects. Each ``S3Resource`` object represents an Amazon S3
        bucket that your transferred data will be exported from or imported into.

        - **S3Resources** *(list) --*

          An array of ``S3Resource`` objects.

          - *(dict) --*

            Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
            will be exported from or imported into. For export jobs, this object can have an
            optional ``KeyRange`` value. The length of the range is defined at job creation, and
            has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges
            are UTF-8 binary sorted.

            - **BucketArn** *(string) --*

              The Amazon Resource Name (ARN) of an Amazon S3 bucket.

            - **KeyRange** *(dict) --*

              For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
              bucket. The length of the range is defined at job creation, and has either an
              inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
              binary sorted.

              - **BeginMarker** *(string) --*

                The key that starts an optional key range for an export job. Ranges are inclusive
                and UTF-8 binary sorted.

              - **EndMarker** *(string) --*

                The key that ends an optional key range for an export job. Ranges are inclusive and
                UTF-8 binary sorted.

        - **LambdaResources** *(list) --*

          The Python-language Lambda functions for this job.

          - *(dict) --*

            Identifies

            - **LambdaArn** *(string) --*

              An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered
              by PUT object actions on the associated local Amazon S3 resource.

            - **EventTriggers** *(list) --*

              The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
              associated with this job.

              - *(dict) --*

                The container for the  EventTriggerDefinition$EventResourceARN .

                - **EventResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
                  Lambda function's event trigger associated with this job.

        - **Ec2AmiResources** *(list) --*

          The Amazon Machine Images (AMIs) associated with this job.

          - *(dict) --*

            A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
            including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
            IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

            - **AmiId** *(string) --*

              The ID of the AMI in Amazon EC2.

            - **SnowballAmiId** *(string) --*

              The ID of the AMI on the Snowball Edge device.

      - **Description** *(string) --*

        The description of the job, provided at job creation.

      - **KmsKeyARN** *(string) --*

        The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated
        with this job. This ARN was created using the `CreateKey
        <https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in
        AWS KMS.

      - **RoleARN** *(string) --*

        The role ARN associated with this job. This ARN was created using the `CreateRole
        <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in
        AWS Identity and Access Management (IAM).

      - **AddressId** *(string) --*

        The ID for the address that you want the Snowball shipped to.

      - **ShippingDetails** *(dict) --*

        A job's shipping information, including inbound and outbound tracking numbers and shipping
        speed options.

        - **ShippingOption** *(string) --*

          The shipping speed for a particular job. This speed doesn't dictate how soon you'll get
          the Snowball from the job's creation date. This speed represents how quickly it moves to
          its destination while in transit. Regional shipping speeds are as follows:

          * In Australia, you have access to express shipping. Typically, Snowballs shipped express
          are delivered in about a day.

          * In the European Union (EU), you have access to express shipping. Typically, Snowballs
          shipped express are delivered in about a day. In addition, most countries in the EU have
          access to standard shipping, which typically takes less than a week, one way.

          * In India, Snowballs are delivered in one to seven days.

          * In the United States of America (US), you have access to one-day shipping and two-day
          shipping.

        - **InboundShipment** *(dict) --*

          The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a
          particular job.

          - **Status** *(string) --*

            Status information for a shipment.

          - **TrackingNumber** *(string) --*

            The tracking number for this job. Using this tracking number with your region's
            carrier's website, you can track a Snowball as the carrier transports it.

            For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

        - **OutboundShipment** *(dict) --*

          The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the
          address that you specified for a particular job.

          - **Status** *(string) --*

            Status information for a shipment.

          - **TrackingNumber** *(string) --*

            The tracking number for this job. Using this tracking number with your region's
            carrier's website, you can track a Snowball as the carrier transports it.

            For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

      - **SnowballCapacityPreference** *(string) --*

        The Snowball capacity preference for this job, specified at job creation. In US regions,
        you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity
        Snowballs.

      - **Notification** *(dict) --*

        The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a
        specific job. The ``Notification`` object is returned as a part of the response syntax of
        the ``DescribeJob`` action in the ``JobMetadata`` data type.

        - **SnsTopicARN** *(string) --*

          The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
          Resource Names (ARNs) for topics by using the `CreateTopic
          <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
          action.

          You can subscribe email addresses to an Amazon SNS topic through the AWS Management
          Console, or by using the `Subscribe
          <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
          Notification Service (SNS) API action.

        - **JobStatesToNotify** *(list) --*

          The list of job states that will trigger a notification for this job.

          - *(string) --*

        - **NotifyAll** *(boolean) --*

          Any change in job state will trigger a notification for this job.

      - **DataTransferProgress** *(dict) --*

        A value that defines the real-time status of a Snowball's data transfer while the device is
        at AWS. This data is only available while a job has a ``JobState`` value of ``InProgress``
        , for both import and export jobs.

        - **BytesTransferred** *(integer) --*

          The number of bytes transferred between a Snowball and Amazon S3.

        - **ObjectsTransferred** *(integer) --*

          The number of objects transferred between a Snowball and Amazon S3.

        - **TotalBytes** *(integer) --*

          The total bytes of data for a transfer between a Snowball and Amazon S3. This value is
          set to 0 (zero) until all the keys that will be transferred have been listed.

        - **TotalObjects** *(integer) --*

          The total number of objects for a transfer between a Snowball and Amazon S3. This value
          is set to 0 (zero) until all the keys that will be transferred have been listed.

      - **JobLogInfo** *(dict) --*

        Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job
        report becomes available at the end of the import process. For export jobs, your job report
        typically becomes available while the Snowball for your job part is being delivered to you.

        - **JobCompletionReportURI** *(string) --*

          A link to an Amazon S3 presigned URL where the job completion report is located.

        - **JobSuccessLogURI** *(string) --*

          A link to an Amazon S3 presigned URL where the job success log is located.

        - **JobFailureLogURI** *(string) --*

          A link to an Amazon S3 presigned URL where the job failure log is located.

      - **ClusterId** *(string) --*

        The 39-character ID for the cluster, for example
        ``CID123e4567-e89b-12d3-a456-426655440000`` .

      - **ForwardingAddressId** *(string) --*

        The ID of the address that you want a job shipped to, after it will be shipped to its
        primary address. This field is not supported in most regions.

    - **SubJobMetadata** *(list) --*

      Information about a specific job part (in the case of an export job), including shipping
      information, job status, and other important metadata.

      - *(dict) --*

        Contains information about a specific job including shipping information, job status, and
        other important metadata. This information is returned as a part of the response syntax of
        the ``DescribeJob`` action.

        - **JobId** *(string) --*

          The automatically generated ID for a job, for example
          ``JID123e4567-e89b-12d3-a456-426655440000`` .

        - **JobState** *(string) --*

          The current status of the jobs.

        - **JobType** *(string) --*

          The type of job.

        - **SnowballType** *(string) --*

          The type of device used with this job.

        - **CreationDate** *(datetime) --*

          The creation date for this job.

        - **Resources** *(dict) --*

          An array of ``S3Resource`` objects. Each ``S3Resource`` object represents an Amazon S3
          bucket that your transferred data will be exported from or imported into.

          - **S3Resources** *(list) --*

            An array of ``S3Resource`` objects.

            - *(dict) --*

              Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data
              will be exported from or imported into. For export jobs, this object can have an
              optional ``KeyRange`` value. The length of the range is defined at job creation, and
              has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both.
              Ranges are UTF-8 binary sorted.

              - **BucketArn** *(string) --*

                The Amazon Resource Name (ARN) of an Amazon S3 bucket.

              - **KeyRange** *(dict) --*

                For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon
                S3 bucket. The length of the range is defined at job creation, and has either an
                inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8
                binary sorted.

                - **BeginMarker** *(string) --*

                  The key that starts an optional key range for an export job. Ranges are inclusive
                  and UTF-8 binary sorted.

                - **EndMarker** *(string) --*

                  The key that ends an optional key range for an export job. Ranges are inclusive
                  and UTF-8 binary sorted.

          - **LambdaResources** *(list) --*

            The Python-language Lambda functions for this job.

            - *(dict) --*

              Identifies

              - **LambdaArn** *(string) --*

                An Amazon Resource Name (ARN) that represents an AWS Lambda function to be
                triggered by PUT object actions on the associated local Amazon S3 resource.

              - **EventTriggers** *(list) --*

                The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects
                associated with this job.

                - *(dict) --*

                  The container for the  EventTriggerDefinition$EventResourceARN .

                  - **EventResourceARN** *(string) --*

                    The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS
                    Lambda function's event trigger associated with this job.

          - **Ec2AmiResources** *(list) --*

            The Amazon Machine Images (AMIs) associated with this job.

            - *(dict) --*

              A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
              including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two
              IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

              - **AmiId** *(string) --*

                The ID of the AMI in Amazon EC2.

              - **SnowballAmiId** *(string) --*

                The ID of the AMI on the Snowball Edge device.

        - **Description** *(string) --*

          The description of the job, provided at job creation.

        - **KmsKeyARN** *(string) --*

          The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key
          associated with this job. This ARN was created using the `CreateKey
          <https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in
          AWS KMS.

        - **RoleARN** *(string) --*

          The role ARN associated with this job. This ARN was created using the `CreateRole
          <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action
          in AWS Identity and Access Management (IAM).

        - **AddressId** *(string) --*

          The ID for the address that you want the Snowball shipped to.

        - **ShippingDetails** *(dict) --*

          A job's shipping information, including inbound and outbound tracking numbers and
          shipping speed options.

          - **ShippingOption** *(string) --*

            The shipping speed for a particular job. This speed doesn't dictate how soon you'll get
            the Snowball from the job's creation date. This speed represents how quickly it moves
            to its destination while in transit. Regional shipping speeds are as follows:

            * In Australia, you have access to express shipping. Typically, Snowballs shipped
            express are delivered in about a day.

            * In the European Union (EU), you have access to express shipping. Typically, Snowballs
            shipped express are delivered in about a day. In addition, most countries in the EU
            have access to standard shipping, which typically takes less than a week, one way.

            * In India, Snowballs are delivered in one to seven days.

            * In the United States of America (US), you have access to one-day shipping and two-day
            shipping.

          - **InboundShipment** *(dict) --*

            The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a
            particular job.

            - **Status** *(string) --*

              Status information for a shipment.

            - **TrackingNumber** *(string) --*

              The tracking number for this job. Using this tracking number with your region's
              carrier's website, you can track a Snowball as the carrier transports it.

              For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

          - **OutboundShipment** *(dict) --*

            The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the
            address that you specified for a particular job.

            - **Status** *(string) --*

              Status information for a shipment.

            - **TrackingNumber** *(string) --*

              The tracking number for this job. Using this tracking number with your region's
              carrier's website, you can track a Snowball as the carrier transports it.

              For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.

        - **SnowballCapacityPreference** *(string) --*

          The Snowball capacity preference for this job, specified at job creation. In US regions,
          you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity
          Snowballs.

        - **Notification** *(dict) --*

          The Amazon Simple Notification Service (Amazon SNS) notification settings associated with
          a specific job. The ``Notification`` object is returned as a part of the response syntax
          of the ``DescribeJob`` action in the ``JobMetadata`` data type.

          - **SnsTopicARN** *(string) --*

            The new SNS ``TopicArn`` that you want to associate with this job. You can create
            Amazon Resource Names (ARNs) for topics by using the `CreateTopic
            <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API
            action.

            You can subscribe email addresses to an Amazon SNS topic through the AWS Management
            Console, or by using the `Subscribe
            <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple
            Notification Service (SNS) API action.

          - **JobStatesToNotify** *(list) --*

            The list of job states that will trigger a notification for this job.

            - *(string) --*

          - **NotifyAll** *(boolean) --*

            Any change in job state will trigger a notification for this job.

        - **DataTransferProgress** *(dict) --*

          A value that defines the real-time status of a Snowball's data transfer while the device
          is at AWS. This data is only available while a job has a ``JobState`` value of
          ``InProgress`` , for both import and export jobs.

          - **BytesTransferred** *(integer) --*

            The number of bytes transferred between a Snowball and Amazon S3.

          - **ObjectsTransferred** *(integer) --*

            The number of objects transferred between a Snowball and Amazon S3.

          - **TotalBytes** *(integer) --*

            The total bytes of data for a transfer between a Snowball and Amazon S3. This value is
            set to 0 (zero) until all the keys that will be transferred have been listed.

          - **TotalObjects** *(integer) --*

            The total number of objects for a transfer between a Snowball and Amazon S3. This value
            is set to 0 (zero) until all the keys that will be transferred have been listed.

        - **JobLogInfo** *(dict) --*

          Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF
          job report becomes available at the end of the import process. For export jobs, your job
          report typically becomes available while the Snowball for your job part is being
          delivered to you.

          - **JobCompletionReportURI** *(string) --*

            A link to an Amazon S3 presigned URL where the job completion report is located.

          - **JobSuccessLogURI** *(string) --*

            A link to an Amazon S3 presigned URL where the job success log is located.

          - **JobFailureLogURI** *(string) --*

            A link to an Amazon S3 presigned URL where the job failure log is located.

        - **ClusterId** *(string) --*

          The 39-character ID for the cluster, for example
          ``CID123e4567-e89b-12d3-a456-426655440000`` .

        - **ForwardingAddressId** *(string) --*

          The ID of the address that you want a job shipped to, after it will be shipped to its
          primary address. This field is not supported in most regions.
    """


_ClientGetJobManifestResponseTypeDef = TypedDict(
    "_ClientGetJobManifestResponseTypeDef", {"ManifestURI": str}, total=False
)


class ClientGetJobManifestResponseTypeDef(_ClientGetJobManifestResponseTypeDef):
    """
    Type definition for `ClientGetJobManifest` `Response`

    - **ManifestURI** *(string) --*

      The Amazon S3 presigned URL for the manifest file associated with the specified ``JobId``
      value.
    """


_ClientGetJobUnlockCodeResponseTypeDef = TypedDict(
    "_ClientGetJobUnlockCodeResponseTypeDef", {"UnlockCode": str}, total=False
)


class ClientGetJobUnlockCodeResponseTypeDef(_ClientGetJobUnlockCodeResponseTypeDef):
    """
    Type definition for `ClientGetJobUnlockCode` `Response`

    - **UnlockCode** *(string) --*

      The ``UnlockCode`` value for the specified job. The ``UnlockCode`` value can be accessed for
      up to 90 days after the job has been created.
    """


_ClientGetSnowballUsageResponseTypeDef = TypedDict(
    "_ClientGetSnowballUsageResponseTypeDef",
    {"SnowballLimit": int, "SnowballsInUse": int},
    total=False,
)


class ClientGetSnowballUsageResponseTypeDef(_ClientGetSnowballUsageResponseTypeDef):
    """
    Type definition for `ClientGetSnowballUsage` `Response`

    - **SnowballLimit** *(integer) --*

      The service limit for number of Snowballs this account can have at once. The default service
      limit is 1 (one).

    - **SnowballsInUse** *(integer) --*

      The number of Snowballs that this account is currently using.
    """


_ClientGetSoftwareUpdatesResponseTypeDef = TypedDict(
    "_ClientGetSoftwareUpdatesResponseTypeDef", {"UpdatesURI": str}, total=False
)


class ClientGetSoftwareUpdatesResponseTypeDef(_ClientGetSoftwareUpdatesResponseTypeDef):
    """
    Type definition for `ClientGetSoftwareUpdates` `Response`

    - **UpdatesURI** *(string) --*

      The Amazon S3 presigned URL for the update file associated with the specified ``JobId``
      value. The software update will be available for 2 days after this request is made. To access
      an update after the 2 days have passed, you'll have to make another call to
      ``GetSoftwareUpdates`` .
    """


_ClientListClusterJobsResponseJobListEntriesTypeDef = TypedDict(
    "_ClientListClusterJobsResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": str,
        "IsMaster": bool,
        "JobType": str,
        "SnowballType": str,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListClusterJobsResponseJobListEntriesTypeDef(
    _ClientListClusterJobsResponseJobListEntriesTypeDef
):
    """
    Type definition for `ClientListClusterJobsResponse` `JobListEntries`

    Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
    whether the job is a job part, in the case of an export job.

    - **JobId** *(string) --*

      The automatically generated ID for a job, for example
      ``JID123e4567-e89b-12d3-a456-426655440000`` .

    - **JobState** *(string) --*

      The current state of this job.

    - **IsMaster** *(boolean) --*

      A value that indicates that this job is a master job. A master job represents a
      successful request to create an export job. Master jobs aren't associated with any
      Snowballs. Instead, each master job will have at least one job part, and each job part is
      associated with a Snowball. It might take some time before the job parts associated with
      a particular master job are listed, because they are created after the master job is
      created.

    - **JobType** *(string) --*

      The type of job.

    - **SnowballType** *(string) --*

      The type of device used with this job.

    - **CreationDate** *(datetime) --*

      The creation date for this job.

    - **Description** *(string) --*

      The optional description of this specific job, for example ``Important Photos
      2016-08-11`` .
    """


_ClientListClusterJobsResponseTypeDef = TypedDict(
    "_ClientListClusterJobsResponseTypeDef",
    {
        "JobListEntries": List[ClientListClusterJobsResponseJobListEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListClusterJobsResponseTypeDef(_ClientListClusterJobsResponseTypeDef):
    """
    Type definition for `ClientListClusterJobs` `Response`

    - **JobListEntries** *(list) --*

      Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
      whether the job is a job part, in the case of export jobs.

      - *(dict) --*

        Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
        whether the job is a job part, in the case of an export job.

        - **JobId** *(string) --*

          The automatically generated ID for a job, for example
          ``JID123e4567-e89b-12d3-a456-426655440000`` .

        - **JobState** *(string) --*

          The current state of this job.

        - **IsMaster** *(boolean) --*

          A value that indicates that this job is a master job. A master job represents a
          successful request to create an export job. Master jobs aren't associated with any
          Snowballs. Instead, each master job will have at least one job part, and each job part is
          associated with a Snowball. It might take some time before the job parts associated with
          a particular master job are listed, because they are created after the master job is
          created.

        - **JobType** *(string) --*

          The type of job.

        - **SnowballType** *(string) --*

          The type of device used with this job.

        - **CreationDate** *(datetime) --*

          The creation date for this job.

        - **Description** *(string) --*

          The optional description of this specific job, for example ``Important Photos
          2016-08-11`` .

    - **NextToken** *(string) --*

      HTTP requests are stateless. If you use the automatically generated ``NextToken`` value in
      your next ``ListClusterJobsResult`` call, your list of returned jobs will start from this
      point in the array.
    """


_ClientListClustersResponseClusterListEntriesTypeDef = TypedDict(
    "_ClientListClustersResponseClusterListEntriesTypeDef",
    {
        "ClusterId": str,
        "ClusterState": str,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListClustersResponseClusterListEntriesTypeDef(
    _ClientListClustersResponseClusterListEntriesTypeDef
):
    """
    Type definition for `ClientListClustersResponse` `ClusterListEntries`

    Contains a cluster's state, a cluster's ID, and other important information.

    - **ClusterId** *(string) --*

      The 39-character ID for the cluster that you want to list, for example
      ``CID123e4567-e89b-12d3-a456-426655440000`` .

    - **ClusterState** *(string) --*

      The current state of this cluster. For information about the state of a specific node,
      see  JobListEntry$JobState .

    - **CreationDate** *(datetime) --*

      The creation date for this cluster.

    - **Description** *(string) --*

      Defines an optional description of the cluster, for example ``Environmental Data
      Cluster-01`` .
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef",
    {
        "ClusterListEntries": List[ClientListClustersResponseClusterListEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    Type definition for `ClientListClusters` `Response`

    - **ClusterListEntries** *(list) --*

      Each ``ClusterListEntry`` object contains a cluster's state, a cluster's ID, and other
      important status information.

      - *(dict) --*

        Contains a cluster's state, a cluster's ID, and other important information.

        - **ClusterId** *(string) --*

          The 39-character ID for the cluster that you want to list, for example
          ``CID123e4567-e89b-12d3-a456-426655440000`` .

        - **ClusterState** *(string) --*

          The current state of this cluster. For information about the state of a specific node,
          see  JobListEntry$JobState .

        - **CreationDate** *(datetime) --*

          The creation date for this cluster.

        - **Description** *(string) --*

          Defines an optional description of the cluster, for example ``Environmental Data
          Cluster-01`` .

    - **NextToken** *(string) --*

      HTTP requests are stateless. If you use the automatically generated ``NextToken`` value in
      your next ``ClusterListEntry`` call, your list of returned clusters will start from this
      point in the array.
    """


_ClientListCompatibleImagesResponseCompatibleImagesTypeDef = TypedDict(
    "_ClientListCompatibleImagesResponseCompatibleImagesTypeDef",
    {"AmiId": str, "Name": str},
    total=False,
)


class ClientListCompatibleImagesResponseCompatibleImagesTypeDef(
    _ClientListCompatibleImagesResponseCompatibleImagesTypeDef
):
    """
    Type definition for `ClientListCompatibleImagesResponse` `CompatibleImages`

    A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including
    the ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
    hardware requirements, and it should be able to be run in an SBE1 instance on the device.

    - **AmiId** *(string) --*

      The unique identifier for an individual Snowball Edge AMI.

    - **Name** *(string) --*

      The optional name of a compatible image.
    """


_ClientListCompatibleImagesResponseTypeDef = TypedDict(
    "_ClientListCompatibleImagesResponseTypeDef",
    {
        "CompatibleImages": List[
            ClientListCompatibleImagesResponseCompatibleImagesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCompatibleImagesResponseTypeDef(
    _ClientListCompatibleImagesResponseTypeDef
):
    """
    Type definition for `ClientListCompatibleImages` `Response`

    - **CompatibleImages** *(list) --*

      A JSON-formatted object that describes a compatible AMI, including the ID and name for a
      Snowball Edge AMI.

      - *(dict) --*

        A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including
        the ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
        hardware requirements, and it should be able to be run in an SBE1 instance on the device.

        - **AmiId** *(string) --*

          The unique identifier for an individual Snowball Edge AMI.

        - **Name** *(string) --*

          The optional name of a compatible image.

    - **NextToken** *(string) --*

      Because HTTP requests are stateless, this is the starting point for your next list of
      returned images.
    """


_ClientListJobsResponseJobListEntriesTypeDef = TypedDict(
    "_ClientListJobsResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": str,
        "IsMaster": bool,
        "JobType": str,
        "SnowballType": str,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListJobsResponseJobListEntriesTypeDef(
    _ClientListJobsResponseJobListEntriesTypeDef
):
    """
    Type definition for `ClientListJobsResponse` `JobListEntries`

    Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
    whether the job is a job part, in the case of an export job.

    - **JobId** *(string) --*

      The automatically generated ID for a job, for example
      ``JID123e4567-e89b-12d3-a456-426655440000`` .

    - **JobState** *(string) --*

      The current state of this job.

    - **IsMaster** *(boolean) --*

      A value that indicates that this job is a master job. A master job represents a
      successful request to create an export job. Master jobs aren't associated with any
      Snowballs. Instead, each master job will have at least one job part, and each job part is
      associated with a Snowball. It might take some time before the job parts associated with
      a particular master job are listed, because they are created after the master job is
      created.

    - **JobType** *(string) --*

      The type of job.

    - **SnowballType** *(string) --*

      The type of device used with this job.

    - **CreationDate** *(datetime) --*

      The creation date for this job.

    - **Description** *(string) --*

      The optional description of this specific job, for example ``Important Photos
      2016-08-11`` .
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {
        "JobListEntries": List[ClientListJobsResponseJobListEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    Type definition for `ClientListJobs` `Response`

    - **JobListEntries** *(list) --*

      Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
      whether the job is a job part, in the case of export jobs.

      - *(dict) --*

        Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
        whether the job is a job part, in the case of an export job.

        - **JobId** *(string) --*

          The automatically generated ID for a job, for example
          ``JID123e4567-e89b-12d3-a456-426655440000`` .

        - **JobState** *(string) --*

          The current state of this job.

        - **IsMaster** *(boolean) --*

          A value that indicates that this job is a master job. A master job represents a
          successful request to create an export job. Master jobs aren't associated with any
          Snowballs. Instead, each master job will have at least one job part, and each job part is
          associated with a Snowball. It might take some time before the job parts associated with
          a particular master job are listed, because they are created after the master job is
          created.

        - **JobType** *(string) --*

          The type of job.

        - **SnowballType** *(string) --*

          The type of device used with this job.

        - **CreationDate** *(datetime) --*

          The creation date for this job.

        - **Description** *(string) --*

          The optional description of this specific job, for example ``Important Photos
          2016-08-11`` .

    - **NextToken** *(string) --*

      HTTP requests are stateless. If you use this automatically generated ``NextToken`` value in
      your next ``ListJobs`` call, your returned ``JobListEntry`` objects will start from this
      point in the array.
    """


_ClientUpdateClusterNotificationTypeDef = TypedDict(
    "_ClientUpdateClusterNotificationTypeDef",
    {"SnsTopicARN": str, "JobStatesToNotify": List[str], "NotifyAll": bool},
    total=False,
)


class ClientUpdateClusterNotificationTypeDef(_ClientUpdateClusterNotificationTypeDef):
    """
    Type definition for `ClientUpdateCluster` `Notification`

    The new or updated  Notification object.

    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.

      You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or
      by using the `Subscribe <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS
      Simple Notification Service (SNS) API action.

    - **JobStatesToNotify** *(list) --*

      The list of job states that will trigger a notification for this job.

      - *(string) --*

    - **NotifyAll** *(boolean) --*

      Any change in job state will trigger a notification for this job.
    """


_RequiredClientUpdateClusterResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_RequiredClientUpdateClusterResourcesEc2AmiResourcesTypeDef", {"AmiId": str}
)
_OptionalClientUpdateClusterResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_OptionalClientUpdateClusterResourcesEc2AmiResourcesTypeDef",
    {"SnowballAmiId": str},
    total=False,
)


class ClientUpdateClusterResourcesEc2AmiResourcesTypeDef(
    _RequiredClientUpdateClusterResourcesEc2AmiResourcesTypeDef,
    _OptionalClientUpdateClusterResourcesEc2AmiResourcesTypeDef,
):
    """
    Type definition for `ClientUpdateClusterResources` `Ec2AmiResources`

    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including
    the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify
    identifying the AMI in both the AWS Cloud and on the device.

    - **AmiId** *(string) --* **[REQUIRED]**

      The ID of the AMI in Amazon EC2.

    - **SnowballAmiId** *(string) --*

      The ID of the AMI on the Snowball Edge device.
    """


_ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef
):
    """
    Type definition for `ClientUpdateClusterResourcesLambdaResources` `EventTriggers`

    The container for the  EventTriggerDefinition$EventResourceARN .

    - **EventResourceARN** *(string) --*

      The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
      function's event trigger associated with this job.
    """


_ClientUpdateClusterResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientUpdateClusterResourcesLambdaResourcesTypeDef(
    _ClientUpdateClusterResourcesLambdaResourcesTypeDef
):
    """
    Type definition for `ClientUpdateClusterResources` `LambdaResources`

    Identifies

    - **LambdaArn** *(string) --*

      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT
      object actions on the associated local Amazon S3 resource.

    - **EventTriggers** *(list) --*

      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated
      with this job.

      - *(dict) --*

        The container for the  EventTriggerDefinition$EventResourceARN .

        - **EventResourceARN** *(string) --*

          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
          function's event trigger associated with this job.
    """


_ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef(
    _ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef
):
    """
    Type definition for `ClientUpdateClusterResourcesS3Resources` `KeyRange`

    For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
    bucket. The length of the range is defined at job creation, and has either an inclusive
    ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

    - **BeginMarker** *(string) --*

      The key that starts an optional key range for an export job. Ranges are inclusive and
      UTF-8 binary sorted.

    - **EndMarker** *(string) --*

      The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
      binary sorted.
    """


_ClientUpdateClusterResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)


class ClientUpdateClusterResourcesS3ResourcesTypeDef(
    _ClientUpdateClusterResourcesS3ResourcesTypeDef
):
    """
    Type definition for `ClientUpdateClusterResources` `S3Resources`

    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
    exported from or imported into. For export jobs, this object can have an optional
    ``KeyRange`` value. The length of the range is defined at job creation, and has either an
    inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
    sorted.

    - **BucketArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon S3 bucket.

    - **KeyRange** *(dict) --*

      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
      bucket. The length of the range is defined at job creation, and has either an inclusive
      ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

      - **BeginMarker** *(string) --*

        The key that starts an optional key range for an export job. Ranges are inclusive and
        UTF-8 binary sorted.

      - **EndMarker** *(string) --*

        The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
        binary sorted.
    """


_ClientUpdateClusterResourcesTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesTypeDef",
    {
        "S3Resources": List[ClientUpdateClusterResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientUpdateClusterResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientUpdateClusterResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)


class ClientUpdateClusterResourcesTypeDef(_ClientUpdateClusterResourcesTypeDef):
    """
    Type definition for `ClientUpdateCluster` `Resources`

    The updated arrays of  JobResource objects that can include updated  S3Resource objects or
    LambdaResource objects.

    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.

      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
        exported from or imported into. For export jobs, this object can have an optional
        ``KeyRange`` value. The length of the range is defined at job creation, and has either an
        inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
        sorted.

        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.

        - **KeyRange** *(dict) --*

          For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
          bucket. The length of the range is defined at job creation, and has either an inclusive
          ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

          - **BeginMarker** *(string) --*

            The key that starts an optional key range for an export job. Ranges are inclusive and
            UTF-8 binary sorted.

          - **EndMarker** *(string) --*

            The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
            binary sorted.

    - **LambdaResources** *(list) --*

      The Python-language Lambda functions for this job.

      - *(dict) --*

        Identifies

        - **LambdaArn** *(string) --*

          An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT
          object actions on the associated local Amazon S3 resource.

        - **EventTriggers** *(list) --*

          The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated
          with this job.

          - *(dict) --*

            The container for the  EventTriggerDefinition$EventResourceARN .

            - **EventResourceARN** *(string) --*

              The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
              function's event trigger associated with this job.

    - **Ec2AmiResources** *(list) --*

      The Amazon Machine Images (AMIs) associated with this job.

      - *(dict) --*

        A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including
        the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify
        identifying the AMI in both the AWS Cloud and on the device.

        - **AmiId** *(string) --* **[REQUIRED]**

          The ID of the AMI in Amazon EC2.

        - **SnowballAmiId** *(string) --*

          The ID of the AMI on the Snowball Edge device.
    """


_ClientUpdateJobNotificationTypeDef = TypedDict(
    "_ClientUpdateJobNotificationTypeDef",
    {"SnsTopicARN": str, "JobStatesToNotify": List[str], "NotifyAll": bool},
    total=False,
)


class ClientUpdateJobNotificationTypeDef(_ClientUpdateJobNotificationTypeDef):
    """
    Type definition for `ClientUpdateJob` `Notification`

    The new or updated  Notification object.

    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.

      You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or
      by using the `Subscribe <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS
      Simple Notification Service (SNS) API action.

    - **JobStatesToNotify** *(list) --*

      The list of job states that will trigger a notification for this job.

      - *(string) --*

    - **NotifyAll** *(boolean) --*

      Any change in job state will trigger a notification for this job.
    """


_RequiredClientUpdateJobResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_RequiredClientUpdateJobResourcesEc2AmiResourcesTypeDef", {"AmiId": str}
)
_OptionalClientUpdateJobResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_OptionalClientUpdateJobResourcesEc2AmiResourcesTypeDef",
    {"SnowballAmiId": str},
    total=False,
)


class ClientUpdateJobResourcesEc2AmiResourcesTypeDef(
    _RequiredClientUpdateJobResourcesEc2AmiResourcesTypeDef,
    _OptionalClientUpdateJobResourcesEc2AmiResourcesTypeDef,
):
    """
    Type definition for `ClientUpdateJobResources` `Ec2AmiResources`

    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including
    the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify
    identifying the AMI in both the AWS Cloud and on the device.

    - **AmiId** *(string) --* **[REQUIRED]**

      The ID of the AMI in Amazon EC2.

    - **SnowballAmiId** *(string) --*

      The ID of the AMI on the Snowball Edge device.
    """


_ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef
):
    """
    Type definition for `ClientUpdateJobResourcesLambdaResources` `EventTriggers`

    The container for the  EventTriggerDefinition$EventResourceARN .

    - **EventResourceARN** *(string) --*

      The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
      function's event trigger associated with this job.
    """


_ClientUpdateJobResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientUpdateJobResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientUpdateJobResourcesLambdaResourcesTypeDef(
    _ClientUpdateJobResourcesLambdaResourcesTypeDef
):
    """
    Type definition for `ClientUpdateJobResources` `LambdaResources`

    Identifies

    - **LambdaArn** *(string) --*

      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT
      object actions on the associated local Amazon S3 resource.

    - **EventTriggers** *(list) --*

      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated
      with this job.

      - *(dict) --*

        The container for the  EventTriggerDefinition$EventResourceARN .

        - **EventResourceARN** *(string) --*

          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
          function's event trigger associated with this job.
    """


_ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef(
    _ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef
):
    """
    Type definition for `ClientUpdateJobResourcesS3Resources` `KeyRange`

    For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
    bucket. The length of the range is defined at job creation, and has either an inclusive
    ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

    - **BeginMarker** *(string) --*

      The key that starts an optional key range for an export job. Ranges are inclusive and
      UTF-8 binary sorted.

    - **EndMarker** *(string) --*

      The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
      binary sorted.
    """


_ClientUpdateJobResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientUpdateJobResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)


class ClientUpdateJobResourcesS3ResourcesTypeDef(
    _ClientUpdateJobResourcesS3ResourcesTypeDef
):
    """
    Type definition for `ClientUpdateJobResources` `S3Resources`

    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
    exported from or imported into. For export jobs, this object can have an optional
    ``KeyRange`` value. The length of the range is defined at job creation, and has either an
    inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
    sorted.

    - **BucketArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon S3 bucket.

    - **KeyRange** *(dict) --*

      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
      bucket. The length of the range is defined at job creation, and has either an inclusive
      ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

      - **BeginMarker** *(string) --*

        The key that starts an optional key range for an export job. Ranges are inclusive and
        UTF-8 binary sorted.

      - **EndMarker** *(string) --*

        The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
        binary sorted.
    """


_ClientUpdateJobResourcesTypeDef = TypedDict(
    "_ClientUpdateJobResourcesTypeDef",
    {
        "S3Resources": List[ClientUpdateJobResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientUpdateJobResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientUpdateJobResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)


class ClientUpdateJobResourcesTypeDef(_ClientUpdateJobResourcesTypeDef):
    """
    Type definition for `ClientUpdateJob` `Resources`

    The updated ``JobResource`` object, or the updated  JobResource object.

    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.

      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
        exported from or imported into. For export jobs, this object can have an optional
        ``KeyRange`` value. The length of the range is defined at job creation, and has either an
        inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
        sorted.

        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.

        - **KeyRange** *(dict) --*

          For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3
          bucket. The length of the range is defined at job creation, and has either an inclusive
          ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.

          - **BeginMarker** *(string) --*

            The key that starts an optional key range for an export job. Ranges are inclusive and
            UTF-8 binary sorted.

          - **EndMarker** *(string) --*

            The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8
            binary sorted.

    - **LambdaResources** *(list) --*

      The Python-language Lambda functions for this job.

      - *(dict) --*

        Identifies

        - **LambdaArn** *(string) --*

          An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT
          object actions on the associated local Amazon S3 resource.

        - **EventTriggers** *(list) --*

          The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated
          with this job.

          - *(dict) --*

            The container for the  EventTriggerDefinition$EventResourceARN .

            - **EventResourceARN** *(string) --*

              The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda
              function's event trigger associated with this job.

    - **Ec2AmiResources** *(list) --*

      The Amazon Machine Images (AMIs) associated with this job.

      - *(dict) --*

        A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including
        the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify
        identifying the AMI in both the AWS Cloud and on the device.

        - **AmiId** *(string) --* **[REQUIRED]**

          The ID of the AMI in Amazon EC2.

        - **SnowballAmiId** *(string) --*

          The ID of the AMI on the Snowball Edge device.
    """


_DescribeAddressesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAddressesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAddressesPaginatePaginationConfigTypeDef(
    _DescribeAddressesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAddressesPaginate` `PaginationConfig`

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


_DescribeAddressesPaginateResponseAddressesTypeDef = TypedDict(
    "_DescribeAddressesPaginateResponseAddressesTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)


class DescribeAddressesPaginateResponseAddressesTypeDef(
    _DescribeAddressesPaginateResponseAddressesTypeDef
):
    """
    Type definition for `DescribeAddressesPaginateResponse` `Addresses`

    The address that you want the Snowball or Snowballs associated with a specific job to be
    shipped to. Addresses are validated at the time of creation. The address you provide must
    be located within the serviceable area of your region. Although no individual elements of
    the ``Address`` are required, if the address is invalid or unsupported, then an exception
    is thrown.

    - **AddressId** *(string) --*

      The unique ID for an address.

    - **Name** *(string) --*

      The name of a person to receive a Snowball at an address.

    - **Company** *(string) --*

      The name of the company to receive a Snowball at an address.

    - **Street1** *(string) --*

      The first line in a street address that a Snowball is to be delivered to.

    - **Street2** *(string) --*

      The second line in a street address that a Snowball is to be delivered to.

    - **Street3** *(string) --*

      The third line in a street address that a Snowball is to be delivered to.

    - **City** *(string) --*

      The city in an address that a Snowball is to be delivered to.

    - **StateOrProvince** *(string) --*

      The state or province in an address that a Snowball is to be delivered to.

    - **PrefectureOrDistrict** *(string) --*

      This field is no longer used and the value is ignored.

    - **Landmark** *(string) --*

      This field is no longer used and the value is ignored.

    - **Country** *(string) --*

      The country in an address that a Snowball is to be delivered to.

    - **PostalCode** *(string) --*

      The postal code in an address that a Snowball is to be delivered to.

    - **PhoneNumber** *(string) --*

      The phone number associated with an address that a Snowball is to be delivered to.

    - **IsRestricted** *(boolean) --*

      If the address you are creating is a primary address, then set this option to true. This
      field is not supported in most regions.
    """


_DescribeAddressesPaginateResponseTypeDef = TypedDict(
    "_DescribeAddressesPaginateResponseTypeDef",
    {"Addresses": List[DescribeAddressesPaginateResponseAddressesTypeDef]},
    total=False,
)


class DescribeAddressesPaginateResponseTypeDef(
    _DescribeAddressesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAddressesPaginate` `Response`

    - **Addresses** *(list) --*

      The Snowball shipping addresses that were created for this account.

      - *(dict) --*

        The address that you want the Snowball or Snowballs associated with a specific job to be
        shipped to. Addresses are validated at the time of creation. The address you provide must
        be located within the serviceable area of your region. Although no individual elements of
        the ``Address`` are required, if the address is invalid or unsupported, then an exception
        is thrown.

        - **AddressId** *(string) --*

          The unique ID for an address.

        - **Name** *(string) --*

          The name of a person to receive a Snowball at an address.

        - **Company** *(string) --*

          The name of the company to receive a Snowball at an address.

        - **Street1** *(string) --*

          The first line in a street address that a Snowball is to be delivered to.

        - **Street2** *(string) --*

          The second line in a street address that a Snowball is to be delivered to.

        - **Street3** *(string) --*

          The third line in a street address that a Snowball is to be delivered to.

        - **City** *(string) --*

          The city in an address that a Snowball is to be delivered to.

        - **StateOrProvince** *(string) --*

          The state or province in an address that a Snowball is to be delivered to.

        - **PrefectureOrDistrict** *(string) --*

          This field is no longer used and the value is ignored.

        - **Landmark** *(string) --*

          This field is no longer used and the value is ignored.

        - **Country** *(string) --*

          The country in an address that a Snowball is to be delivered to.

        - **PostalCode** *(string) --*

          The postal code in an address that a Snowball is to be delivered to.

        - **PhoneNumber** *(string) --*

          The phone number associated with an address that a Snowball is to be delivered to.

        - **IsRestricted** *(boolean) --*

          If the address you are creating is a primary address, then set this option to true. This
          field is not supported in most regions.
    """


_ListClusterJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClusterJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClusterJobsPaginatePaginationConfigTypeDef(
    _ListClusterJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListClusterJobsPaginate` `PaginationConfig`

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


_ListClusterJobsPaginateResponseJobListEntriesTypeDef = TypedDict(
    "_ListClusterJobsPaginateResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": str,
        "IsMaster": bool,
        "JobType": str,
        "SnowballType": str,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ListClusterJobsPaginateResponseJobListEntriesTypeDef(
    _ListClusterJobsPaginateResponseJobListEntriesTypeDef
):
    """
    Type definition for `ListClusterJobsPaginateResponse` `JobListEntries`

    Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
    whether the job is a job part, in the case of an export job.

    - **JobId** *(string) --*

      The automatically generated ID for a job, for example
      ``JID123e4567-e89b-12d3-a456-426655440000`` .

    - **JobState** *(string) --*

      The current state of this job.

    - **IsMaster** *(boolean) --*

      A value that indicates that this job is a master job. A master job represents a
      successful request to create an export job. Master jobs aren't associated with any
      Snowballs. Instead, each master job will have at least one job part, and each job part is
      associated with a Snowball. It might take some time before the job parts associated with
      a particular master job are listed, because they are created after the master job is
      created.

    - **JobType** *(string) --*

      The type of job.

    - **SnowballType** *(string) --*

      The type of device used with this job.

    - **CreationDate** *(datetime) --*

      The creation date for this job.

    - **Description** *(string) --*

      The optional description of this specific job, for example ``Important Photos
      2016-08-11`` .
    """


_ListClusterJobsPaginateResponseTypeDef = TypedDict(
    "_ListClusterJobsPaginateResponseTypeDef",
    {"JobListEntries": List[ListClusterJobsPaginateResponseJobListEntriesTypeDef]},
    total=False,
)


class ListClusterJobsPaginateResponseTypeDef(_ListClusterJobsPaginateResponseTypeDef):
    """
    Type definition for `ListClusterJobsPaginate` `Response`

    - **JobListEntries** *(list) --*

      Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
      whether the job is a job part, in the case of export jobs.

      - *(dict) --*

        Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
        whether the job is a job part, in the case of an export job.

        - **JobId** *(string) --*

          The automatically generated ID for a job, for example
          ``JID123e4567-e89b-12d3-a456-426655440000`` .

        - **JobState** *(string) --*

          The current state of this job.

        - **IsMaster** *(boolean) --*

          A value that indicates that this job is a master job. A master job represents a
          successful request to create an export job. Master jobs aren't associated with any
          Snowballs. Instead, each master job will have at least one job part, and each job part is
          associated with a Snowball. It might take some time before the job parts associated with
          a particular master job are listed, because they are created after the master job is
          created.

        - **JobType** *(string) --*

          The type of job.

        - **SnowballType** *(string) --*

          The type of device used with this job.

        - **CreationDate** *(datetime) --*

          The creation date for this job.

        - **Description** *(string) --*

          The optional description of this specific job, for example ``Important Photos
          2016-08-11`` .
    """


_ListClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClustersPaginatePaginationConfigTypeDef(
    _ListClustersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListClustersPaginate` `PaginationConfig`

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


_ListClustersPaginateResponseClusterListEntriesTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterListEntriesTypeDef",
    {
        "ClusterId": str,
        "ClusterState": str,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ListClustersPaginateResponseClusterListEntriesTypeDef(
    _ListClustersPaginateResponseClusterListEntriesTypeDef
):
    """
    Type definition for `ListClustersPaginateResponse` `ClusterListEntries`

    Contains a cluster's state, a cluster's ID, and other important information.

    - **ClusterId** *(string) --*

      The 39-character ID for the cluster that you want to list, for example
      ``CID123e4567-e89b-12d3-a456-426655440000`` .

    - **ClusterState** *(string) --*

      The current state of this cluster. For information about the state of a specific node,
      see  JobListEntry$JobState .

    - **CreationDate** *(datetime) --*

      The creation date for this cluster.

    - **Description** *(string) --*

      Defines an optional description of the cluster, for example ``Environmental Data
      Cluster-01`` .
    """


_ListClustersPaginateResponseTypeDef = TypedDict(
    "_ListClustersPaginateResponseTypeDef",
    {"ClusterListEntries": List[ListClustersPaginateResponseClusterListEntriesTypeDef]},
    total=False,
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    Type definition for `ListClustersPaginate` `Response`

    - **ClusterListEntries** *(list) --*

      Each ``ClusterListEntry`` object contains a cluster's state, a cluster's ID, and other
      important status information.

      - *(dict) --*

        Contains a cluster's state, a cluster's ID, and other important information.

        - **ClusterId** *(string) --*

          The 39-character ID for the cluster that you want to list, for example
          ``CID123e4567-e89b-12d3-a456-426655440000`` .

        - **ClusterState** *(string) --*

          The current state of this cluster. For information about the state of a specific node,
          see  JobListEntry$JobState .

        - **CreationDate** *(datetime) --*

          The creation date for this cluster.

        - **Description** *(string) --*

          Defines an optional description of the cluster, for example ``Environmental Data
          Cluster-01`` .
    """


_ListCompatibleImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCompatibleImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCompatibleImagesPaginatePaginationConfigTypeDef(
    _ListCompatibleImagesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCompatibleImagesPaginate` `PaginationConfig`

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


_ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef = TypedDict(
    "_ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef",
    {"AmiId": str, "Name": str},
    total=False,
)


class ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef(
    _ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef
):
    """
    Type definition for `ListCompatibleImagesPaginateResponse` `CompatibleImages`

    A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including
    the ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
    hardware requirements, and it should be able to be run in an SBE1 instance on the device.

    - **AmiId** *(string) --*

      The unique identifier for an individual Snowball Edge AMI.

    - **Name** *(string) --*

      The optional name of a compatible image.
    """


_ListCompatibleImagesPaginateResponseTypeDef = TypedDict(
    "_ListCompatibleImagesPaginateResponseTypeDef",
    {
        "CompatibleImages": List[
            ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef
        ]
    },
    total=False,
)


class ListCompatibleImagesPaginateResponseTypeDef(
    _ListCompatibleImagesPaginateResponseTypeDef
):
    """
    Type definition for `ListCompatibleImagesPaginate` `Response`

    - **CompatibleImages** *(list) --*

      A JSON-formatted object that describes a compatible AMI, including the ID and name for a
      Snowball Edge AMI.

      - *(dict) --*

        A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including
        the ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
        hardware requirements, and it should be able to be run in an SBE1 instance on the device.

        - **AmiId** *(string) --*

          The unique identifier for an individual Snowball Edge AMI.

        - **Name** *(string) --*

          The optional name of a compatible image.
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


_ListJobsPaginateResponseJobListEntriesTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": str,
        "IsMaster": bool,
        "JobType": str,
        "SnowballType": str,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListEntriesTypeDef(
    _ListJobsPaginateResponseJobListEntriesTypeDef
):
    """
    Type definition for `ListJobsPaginateResponse` `JobListEntries`

    Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
    whether the job is a job part, in the case of an export job.

    - **JobId** *(string) --*

      The automatically generated ID for a job, for example
      ``JID123e4567-e89b-12d3-a456-426655440000`` .

    - **JobState** *(string) --*

      The current state of this job.

    - **IsMaster** *(boolean) --*

      A value that indicates that this job is a master job. A master job represents a
      successful request to create an export job. Master jobs aren't associated with any
      Snowballs. Instead, each master job will have at least one job part, and each job part is
      associated with a Snowball. It might take some time before the job parts associated with
      a particular master job are listed, because they are created after the master job is
      created.

    - **JobType** *(string) --*

      The type of job.

    - **SnowballType** *(string) --*

      The type of device used with this job.

    - **CreationDate** *(datetime) --*

      The creation date for this job.

    - **Description** *(string) --*

      The optional description of this specific job, for example ``Important Photos
      2016-08-11`` .
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"JobListEntries": List[ListJobsPaginateResponseJobListEntriesTypeDef]},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    Type definition for `ListJobsPaginate` `Response`

    - **JobListEntries** *(list) --*

      Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
      whether the job is a job part, in the case of export jobs.

      - *(dict) --*

        Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
        whether the job is a job part, in the case of an export job.

        - **JobId** *(string) --*

          The automatically generated ID for a job, for example
          ``JID123e4567-e89b-12d3-a456-426655440000`` .

        - **JobState** *(string) --*

          The current state of this job.

        - **IsMaster** *(boolean) --*

          A value that indicates that this job is a master job. A master job represents a
          successful request to create an export job. Master jobs aren't associated with any
          Snowballs. Instead, each master job will have at least one job part, and each job part is
          associated with a Snowball. It might take some time before the job parts associated with
          a particular master job are listed, because they are created after the master job is
          created.

        - **JobType** *(string) --*

          The type of job.

        - **SnowballType** *(string) --*

          The type of device used with this job.

        - **CreationDate** *(datetime) --*

          The creation date for this job.

        - **Description** *(string) --*

          The optional description of this specific job, for example ``Important Photos
          2016-08-11`` .
    """
