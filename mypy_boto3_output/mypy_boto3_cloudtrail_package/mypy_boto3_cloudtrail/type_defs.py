"Main interface for cloudtrail type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsTagsListTypeDef",
    "ClientCreateTrailResponseTypeDef",
    "ClientCreateTrailTagsListTypeDef",
    "ClientDescribeTrailsResponsetrailListTypeDef",
    "ClientDescribeTrailsResponseTypeDef",
    "ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    "ClientGetEventSelectorsResponseEventSelectorsTypeDef",
    "ClientGetEventSelectorsResponseTypeDef",
    "ClientGetTrailResponseTrailTypeDef",
    "ClientGetTrailResponseTypeDef",
    "ClientGetTrailStatusResponseTypeDef",
    "ClientListPublicKeysResponsePublicKeyListTypeDef",
    "ClientListPublicKeysResponseTypeDef",
    "ClientListTagsResponseResourceTagListTagsListTypeDef",
    "ClientListTagsResponseResourceTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListTrailsResponseTrailsTypeDef",
    "ClientListTrailsResponseTypeDef",
    "ClientLookupEventsLookupAttributesTypeDef",
    "ClientLookupEventsResponseEventsResourcesTypeDef",
    "ClientLookupEventsResponseEventsTypeDef",
    "ClientLookupEventsResponseTypeDef",
    "ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef",
    "ClientPutEventSelectorsEventSelectorsTypeDef",
    "ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    "ClientPutEventSelectorsResponseEventSelectorsTypeDef",
    "ClientPutEventSelectorsResponseTypeDef",
    "ClientRemoveTagsTagsListTypeDef",
    "ClientUpdateTrailResponseTypeDef",
    "ListPublicKeysPaginatePaginationConfigTypeDef",
    "ListPublicKeysPaginateResponsePublicKeyListTypeDef",
    "ListPublicKeysPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseResourceTagListTagsListTypeDef",
    "ListTagsPaginateResponseResourceTagListTypeDef",
    "ListTagsPaginateResponseTypeDef",
    "ListTrailsPaginatePaginationConfigTypeDef",
    "ListTrailsPaginateResponseTrailsTypeDef",
    "ListTrailsPaginateResponseTypeDef",
    "LookupEventsPaginateLookupAttributesTypeDef",
    "LookupEventsPaginatePaginationConfigTypeDef",
    "LookupEventsPaginateResponseEventsResourcesTypeDef",
    "LookupEventsPaginateResponseEventsTypeDef",
    "LookupEventsPaginateResponseTypeDef",
)


_RequiredClientAddTagsTagsListTypeDef = TypedDict(
    "_RequiredClientAddTagsTagsListTypeDef", {"Key": str}
)
_OptionalClientAddTagsTagsListTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsListTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsListTypeDef(
    _RequiredClientAddTagsTagsListTypeDef, _OptionalClientAddTagsTagsListTypeDef
):
    """
    Type definition for `ClientAddTags` `TagsList`

    A custom key-value pair associated with a resource such as a CloudTrail trail.

    - **Key** *(string) --* **[REQUIRED]**

      The key in a key-value pair. The key must be must be no longer than 128 Unicode characters.
      The key must be unique for the resource to which it applies.

    - **Value** *(string) --*

      The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
      characters.
    """


_ClientCreateTrailResponseTypeDef = TypedDict(
    "_ClientCreateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class ClientCreateTrailResponseTypeDef(_ClientCreateTrailResponseTypeDef):
    """
    Type definition for `ClientCreateTrail` `Response`

    Returns the objects or data listed below if successful. Otherwise, returns an error.

    - **Name** *(string) --*

      Specifies the name of the trail.

    - **S3BucketName** *(string) --*

      Specifies the name of the Amazon S3 bucket designated for publishing log files.

    - **S3KeyPrefix** *(string) --*

      Specifies the Amazon S3 key prefix that comes after the name of the bucket you have
      designated for log file delivery. For more information, see `Finding Your CloudTrail Log
      Files
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__
      .

    - **SnsTopicName** *(string) --*

      This field is no longer in use. Use SnsTopicARN.

    - **SnsTopicARN** *(string) --*

      Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log
      files are delivered. The format of a topic ARN is:

       ``arn:aws:sns:us-east-2:123456789012:MyTopic``

    - **IncludeGlobalServiceEvents** *(boolean) --*

      Specifies whether the trail is publishing events from global services such as IAM to the log
      files.

    - **IsMultiRegionTrail** *(boolean) --*

      Specifies whether the trail exists in one region or in all regions.

    - **TrailARN** *(string) --*

      Specifies the ARN of the trail that was created. The format of a trail ARN is:

       ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

    - **LogFileValidationEnabled** *(boolean) --*

      Specifies whether log file integrity validation is enabled.

    - **CloudWatchLogsLogGroupArn** *(string) --*

      Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be
      delivered.

    - **CloudWatchLogsRoleArn** *(string) --*

      Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

    - **KmsKeyId** *(string) --*

      Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully
      specified ARN to a KMS key in the format:

       ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``

    - **IsOrganizationTrail** *(boolean) --*

      Specifies whether the trail is an organization trail.
    """


_RequiredClientCreateTrailTagsListTypeDef = TypedDict(
    "_RequiredClientCreateTrailTagsListTypeDef", {"Key": str}
)
_OptionalClientCreateTrailTagsListTypeDef = TypedDict(
    "_OptionalClientCreateTrailTagsListTypeDef", {"Value": str}, total=False
)


class ClientCreateTrailTagsListTypeDef(
    _RequiredClientCreateTrailTagsListTypeDef, _OptionalClientCreateTrailTagsListTypeDef
):
    """
    Type definition for `ClientCreateTrail` `TagsList`

    A custom key-value pair associated with a resource such as a CloudTrail trail.

    - **Key** *(string) --* **[REQUIRED]**

      The key in a key-value pair. The key must be must be no longer than 128 Unicode characters.
      The key must be unique for the resource to which it applies.

    - **Value** *(string) --*

      The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
      characters.
    """


_ClientDescribeTrailsResponsetrailListTypeDef = TypedDict(
    "_ClientDescribeTrailsResponsetrailListTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class ClientDescribeTrailsResponsetrailListTypeDef(
    _ClientDescribeTrailsResponsetrailListTypeDef
):
    """
    Type definition for `ClientDescribeTrailsResponse` `trailList`

    The settings for a trail.

    - **Name** *(string) --*

      Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.

    - **S3BucketName** *(string) --*

      Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See `Amazon
      S3 Bucket Naming Requirements
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__
      .

    - **S3KeyPrefix** *(string) --*

      Specifies the Amazon S3 key prefix that comes after the name of the bucket you have
      designated for log file delivery. For more information, see `Finding Your CloudTrail Log
      Files
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__
      .The maximum length is 200 characters.

    - **SnsTopicName** *(string) --*

      This field is no longer in use. Use SnsTopicARN.

    - **SnsTopicARN** *(string) --*

      Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when
      log files are delivered. The format of a topic ARN is:

       ``arn:aws:sns:us-east-2:123456789012:MyTopic``

    - **IncludeGlobalServiceEvents** *(boolean) --*

      Set to **True** to include AWS API calls from AWS global services such as IAM. Otherwise,
      **False** .

    - **IsMultiRegionTrail** *(boolean) --*

      Specifies whether the trail exists only in one region or exists in all regions.

    - **HomeRegion** *(string) --*

      The region in which the trail was created.

    - **TrailARN** *(string) --*

      Specifies the ARN of the trail. The format of a trail ARN is:

       ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

    - **LogFileValidationEnabled** *(boolean) --*

      Specifies whether log file validation is enabled.

    - **CloudWatchLogsLogGroupArn** *(string) --*

      Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log
      group to which CloudTrail logs will be delivered.

    - **CloudWatchLogsRoleArn** *(string) --*

      Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log
      group.

    - **KmsKeyId** *(string) --*

      Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a
      fully specified ARN to a KMS key in the format:

       ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``

    - **HasCustomEventSelectors** *(boolean) --*

      Specifies if the trail has custom event selectors.

    - **IsOrganizationTrail** *(boolean) --*

      Specifies whether the trail is an organization trail.
    """


_ClientDescribeTrailsResponseTypeDef = TypedDict(
    "_ClientDescribeTrailsResponseTypeDef",
    {"trailList": List[ClientDescribeTrailsResponsetrailListTypeDef]},
    total=False,
)


class ClientDescribeTrailsResponseTypeDef(_ClientDescribeTrailsResponseTypeDef):
    """
    Type definition for `ClientDescribeTrails` `Response`

    Returns the objects or data listed below if successful. Otherwise, returns an error.

    - **trailList** *(list) --*

      The list of trail objects.

      - *(dict) --*

        The settings for a trail.

        - **Name** *(string) --*

          Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.

        - **S3BucketName** *(string) --*

          Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See `Amazon
          S3 Bucket Naming Requirements
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__
          .

        - **S3KeyPrefix** *(string) --*

          Specifies the Amazon S3 key prefix that comes after the name of the bucket you have
          designated for log file delivery. For more information, see `Finding Your CloudTrail Log
          Files
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__
          .The maximum length is 200 characters.

        - **SnsTopicName** *(string) --*

          This field is no longer in use. Use SnsTopicARN.

        - **SnsTopicARN** *(string) --*

          Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when
          log files are delivered. The format of a topic ARN is:

           ``arn:aws:sns:us-east-2:123456789012:MyTopic``

        - **IncludeGlobalServiceEvents** *(boolean) --*

          Set to **True** to include AWS API calls from AWS global services such as IAM. Otherwise,
          **False** .

        - **IsMultiRegionTrail** *(boolean) --*

          Specifies whether the trail exists only in one region or exists in all regions.

        - **HomeRegion** *(string) --*

          The region in which the trail was created.

        - **TrailARN** *(string) --*

          Specifies the ARN of the trail. The format of a trail ARN is:

           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

        - **LogFileValidationEnabled** *(boolean) --*

          Specifies whether log file validation is enabled.

        - **CloudWatchLogsLogGroupArn** *(string) --*

          Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log
          group to which CloudTrail logs will be delivered.

        - **CloudWatchLogsRoleArn** *(string) --*

          Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log
          group.

        - **KmsKeyId** *(string) --*

          Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a
          fully specified ARN to a KMS key in the format:

           ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``

        - **HasCustomEventSelectors** *(boolean) --*

          Specifies if the trail has custom event selectors.

        - **IsOrganizationTrail** *(boolean) --*

          Specifies whether the trail is an organization trail.
    """


_ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef = TypedDict(
    "_ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)


class ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef(
    _ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef
):
    """
    Type definition for `ClientGetEventSelectorsResponseEventSelectors` `DataResources`

    The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors
    for your trail to log data events. Data events provide insight into the resource
    operations performed on or within a resource itself. These are also known as data plane
    operations. You can specify up to 250 data resources for a trail.

    .. note::

      The total number of allowed data resources is 250. This number can be distributed
      between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

    The following example demonstrates how logging works when you configure logging of all
    data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user
    specified an empty prefix, and the option to log both ``Read`` and ``Write`` data
    events.

    * A user uploads an image file to ``bucket-1`` .

    * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a
    data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an
    empty prefix, events that occur on any object in that bucket are logged. The trail
    processes and logs the event.

    * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .

    * The ``PutObject`` API operation occurred for an object in an S3 bucket that the
    CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

    The following example demonstrates how logging works when you configure logging of AWS
    Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS
    Lambda functions.

    * A user runs a script that includes a call to the *MyLambdaFunction* function and the
    *MyOtherLambdaFunction* function.

    * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is
    recorded as a data event in CloudTrail. Because the CloudTrail user specified logging
    data events for *MyLambdaFunction* , any invocations of that function are logged. The
    trail processes and logs the event.

    * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because
    the CloudTrail user did not specify logging data events for all Lambda functions, the
    ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified
    for the trail. The trail doesn’t log the event.

    - **Type** *(string) --*

      The resource type in which you want to log data events. You can specify
      ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.

    - **Values** *(list) --*

      An array of Amazon Resource Name (ARN) strings or partial ARN strings for the
      specified objects.

      * To log data events for all objects in all S3 buckets in your AWS account, specify
      the prefix as ``arn:aws:s3:::`` .

      .. note::

         This will also enable logging of data event activity performed by any user or role
         in your AWS account, even if that activity is performed on a bucket that belongs
         to another AWS account.

      * To log data events for all objects in an S3 bucket, specify the bucket and an empty
      object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all
      objects in this S3 bucket.

      * To log data events for specific objects, specify the S3 bucket and object prefix
      such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for
      objects in this S3 bucket that match the prefix.

      * To log data events for all functions in your AWS account, specify the prefix as
      ``arn:aws:lambda`` .

      .. note::

         This will also enable logging of ``Invoke`` activity performed by any user or role
         in your AWS account, even if that activity is performed on a function that belongs
         to another AWS account.

      * To log data events for a specific Lambda function, specify the function ARN.

      .. note::

         Lambda function ARNs are exact. For example, if you specify a function ARN
         *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will
         only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* .
         They will not be logged for
         *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

      - *(string) --*
    """


_ClientGetEventSelectorsResponseEventSelectorsTypeDef = TypedDict(
    "_ClientGetEventSelectorsResponseEventSelectorsTypeDef",
    {
        "ReadWriteType": str,
        "IncludeManagementEvents": bool,
        "DataResources": List[
            ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef
        ],
    },
    total=False,
)


class ClientGetEventSelectorsResponseEventSelectorsTypeDef(
    _ClientGetEventSelectorsResponseEventSelectorsTypeDef
):
    """
    Type definition for `ClientGetEventSelectorsResponse` `EventSelectors`

    Use event selectors to further specify the management and data event settings for your
    trail. By default, trails created without specific event selectors will be configured to
    log all read and write management events, and no data events. When an event occurs in your
    account, CloudTrail evaluates the event selector for all trails. For each trail, if the
    event matches any event selector, the trail processes and logs the event. If the event
    doesn't match any event selector, the trail doesn't log the event.

    You can configure up to five event selectors for a trail.

    - **ReadWriteType** *(string) --*

      Specify if you want your trail to log read-only events, write-only events, or all. For
      example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances``
      is a write-only API operation.

      By default, the value is ``All`` .

    - **IncludeManagementEvents** *(boolean) --*

      Specify if you want your event selector to include management events for your trail.

      For more information, see `Management Events
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__
      in the *AWS CloudTrail User Guide* .

      By default, the value is ``true`` .

    - **DataResources** *(list) --*

      CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions.
      You can specify up to 250 resources for an individual event selector, but the total
      number of data resources cannot exceed 250 across all event selectors in a trail. This
      limit does not apply if you configure resource logging for all data events.

      For more information, see `Data Events
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__
      and `Limits in AWS CloudTrail
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__
      in the *AWS CloudTrail User Guide* .

      - *(dict) --*

        The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors
        for your trail to log data events. Data events provide insight into the resource
        operations performed on or within a resource itself. These are also known as data plane
        operations. You can specify up to 250 data resources for a trail.

        .. note::

          The total number of allowed data resources is 250. This number can be distributed
          between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

        The following example demonstrates how logging works when you configure logging of all
        data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user
        specified an empty prefix, and the option to log both ``Read`` and ``Write`` data
        events.

        * A user uploads an image file to ``bucket-1`` .

        * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a
        data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an
        empty prefix, events that occur on any object in that bucket are logged. The trail
        processes and logs the event.

        * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .

        * The ``PutObject`` API operation occurred for an object in an S3 bucket that the
        CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

        The following example demonstrates how logging works when you configure logging of AWS
        Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS
        Lambda functions.

        * A user runs a script that includes a call to the *MyLambdaFunction* function and the
        *MyOtherLambdaFunction* function.

        * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is
        recorded as a data event in CloudTrail. Because the CloudTrail user specified logging
        data events for *MyLambdaFunction* , any invocations of that function are logged. The
        trail processes and logs the event.

        * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because
        the CloudTrail user did not specify logging data events for all Lambda functions, the
        ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified
        for the trail. The trail doesn’t log the event.

        - **Type** *(string) --*

          The resource type in which you want to log data events. You can specify
          ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.

        - **Values** *(list) --*

          An array of Amazon Resource Name (ARN) strings or partial ARN strings for the
          specified objects.

          * To log data events for all objects in all S3 buckets in your AWS account, specify
          the prefix as ``arn:aws:s3:::`` .

          .. note::

             This will also enable logging of data event activity performed by any user or role
             in your AWS account, even if that activity is performed on a bucket that belongs
             to another AWS account.

          * To log data events for all objects in an S3 bucket, specify the bucket and an empty
          object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all
          objects in this S3 bucket.

          * To log data events for specific objects, specify the S3 bucket and object prefix
          such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for
          objects in this S3 bucket that match the prefix.

          * To log data events for all functions in your AWS account, specify the prefix as
          ``arn:aws:lambda`` .

          .. note::

             This will also enable logging of ``Invoke`` activity performed by any user or role
             in your AWS account, even if that activity is performed on a function that belongs
             to another AWS account.

          * To log data events for a specific Lambda function, specify the function ARN.

          .. note::

             Lambda function ARNs are exact. For example, if you specify a function ARN
             *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will
             only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* .
             They will not be logged for
             *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

          - *(string) --*
    """


_ClientGetEventSelectorsResponseTypeDef = TypedDict(
    "_ClientGetEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List[ClientGetEventSelectorsResponseEventSelectorsTypeDef],
    },
    total=False,
)


class ClientGetEventSelectorsResponseTypeDef(_ClientGetEventSelectorsResponseTypeDef):
    """
    Type definition for `ClientGetEventSelectors` `Response`

    - **TrailARN** *(string) --*

      The specified trail ARN that has the event selectors.

    - **EventSelectors** *(list) --*

      The event selectors that are configured for the trail.

      - *(dict) --*

        Use event selectors to further specify the management and data event settings for your
        trail. By default, trails created without specific event selectors will be configured to
        log all read and write management events, and no data events. When an event occurs in your
        account, CloudTrail evaluates the event selector for all trails. For each trail, if the
        event matches any event selector, the trail processes and logs the event. If the event
        doesn't match any event selector, the trail doesn't log the event.

        You can configure up to five event selectors for a trail.

        - **ReadWriteType** *(string) --*

          Specify if you want your trail to log read-only events, write-only events, or all. For
          example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances``
          is a write-only API operation.

          By default, the value is ``All`` .

        - **IncludeManagementEvents** *(boolean) --*

          Specify if you want your event selector to include management events for your trail.

          For more information, see `Management Events
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__
          in the *AWS CloudTrail User Guide* .

          By default, the value is ``true`` .

        - **DataResources** *(list) --*

          CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions.
          You can specify up to 250 resources for an individual event selector, but the total
          number of data resources cannot exceed 250 across all event selectors in a trail. This
          limit does not apply if you configure resource logging for all data events.

          For more information, see `Data Events
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__
          and `Limits in AWS CloudTrail
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__
          in the *AWS CloudTrail User Guide* .

          - *(dict) --*

            The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors
            for your trail to log data events. Data events provide insight into the resource
            operations performed on or within a resource itself. These are also known as data plane
            operations. You can specify up to 250 data resources for a trail.

            .. note::

              The total number of allowed data resources is 250. This number can be distributed
              between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

            The following example demonstrates how logging works when you configure logging of all
            data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user
            specified an empty prefix, and the option to log both ``Read`` and ``Write`` data
            events.

            * A user uploads an image file to ``bucket-1`` .

            * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a
            data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an
            empty prefix, events that occur on any object in that bucket are logged. The trail
            processes and logs the event.

            * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .

            * The ``PutObject`` API operation occurred for an object in an S3 bucket that the
            CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

            The following example demonstrates how logging works when you configure logging of AWS
            Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS
            Lambda functions.

            * A user runs a script that includes a call to the *MyLambdaFunction* function and the
            *MyOtherLambdaFunction* function.

            * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is
            recorded as a data event in CloudTrail. Because the CloudTrail user specified logging
            data events for *MyLambdaFunction* , any invocations of that function are logged. The
            trail processes and logs the event.

            * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because
            the CloudTrail user did not specify logging data events for all Lambda functions, the
            ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified
            for the trail. The trail doesn’t log the event.

            - **Type** *(string) --*

              The resource type in which you want to log data events. You can specify
              ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.

            - **Values** *(list) --*

              An array of Amazon Resource Name (ARN) strings or partial ARN strings for the
              specified objects.

              * To log data events for all objects in all S3 buckets in your AWS account, specify
              the prefix as ``arn:aws:s3:::`` .

              .. note::

                 This will also enable logging of data event activity performed by any user or role
                 in your AWS account, even if that activity is performed on a bucket that belongs
                 to another AWS account.

              * To log data events for all objects in an S3 bucket, specify the bucket and an empty
              object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all
              objects in this S3 bucket.

              * To log data events for specific objects, specify the S3 bucket and object prefix
              such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for
              objects in this S3 bucket that match the prefix.

              * To log data events for all functions in your AWS account, specify the prefix as
              ``arn:aws:lambda`` .

              .. note::

                 This will also enable logging of ``Invoke`` activity performed by any user or role
                 in your AWS account, even if that activity is performed on a function that belongs
                 to another AWS account.

              * To log data events for a specific Lambda function, specify the function ARN.

              .. note::

                 Lambda function ARNs are exact. For example, if you specify a function ARN
                 *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will
                 only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* .
                 They will not be logged for
                 *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

              - *(string) --*
    """


_ClientGetTrailResponseTrailTypeDef = TypedDict(
    "_ClientGetTrailResponseTrailTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class ClientGetTrailResponseTrailTypeDef(_ClientGetTrailResponseTrailTypeDef):
    """
    Type definition for `ClientGetTrailResponse` `Trail`

    The settings for a trail.

    - **Name** *(string) --*

      Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.

    - **S3BucketName** *(string) --*

      Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See `Amazon
      S3 Bucket Naming Requirements
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__
      .

    - **S3KeyPrefix** *(string) --*

      Specifies the Amazon S3 key prefix that comes after the name of the bucket you have
      designated for log file delivery. For more information, see `Finding Your CloudTrail Log
      Files
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__
      .The maximum length is 200 characters.

    - **SnsTopicName** *(string) --*

      This field is no longer in use. Use SnsTopicARN.

    - **SnsTopicARN** *(string) --*

      Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when
      log files are delivered. The format of a topic ARN is:

       ``arn:aws:sns:us-east-2:123456789012:MyTopic``

    - **IncludeGlobalServiceEvents** *(boolean) --*

      Set to **True** to include AWS API calls from AWS global services such as IAM. Otherwise,
      **False** .

    - **IsMultiRegionTrail** *(boolean) --*

      Specifies whether the trail exists only in one region or exists in all regions.

    - **HomeRegion** *(string) --*

      The region in which the trail was created.

    - **TrailARN** *(string) --*

      Specifies the ARN of the trail. The format of a trail ARN is:

       ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

    - **LogFileValidationEnabled** *(boolean) --*

      Specifies whether log file validation is enabled.

    - **CloudWatchLogsLogGroupArn** *(string) --*

      Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group
      to which CloudTrail logs will be delivered.

    - **CloudWatchLogsRoleArn** *(string) --*

      Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log
      group.

    - **KmsKeyId** *(string) --*

      Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a
      fully specified ARN to a KMS key in the format:

       ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``

    - **HasCustomEventSelectors** *(boolean) --*

      Specifies if the trail has custom event selectors.

    - **IsOrganizationTrail** *(boolean) --*

      Specifies whether the trail is an organization trail.
    """


_ClientGetTrailResponseTypeDef = TypedDict(
    "_ClientGetTrailResponseTypeDef",
    {"Trail": ClientGetTrailResponseTrailTypeDef},
    total=False,
)


class ClientGetTrailResponseTypeDef(_ClientGetTrailResponseTypeDef):
    """
    Type definition for `ClientGetTrail` `Response`

    - **Trail** *(dict) --*

      The settings for a trail.

      - **Name** *(string) --*

        Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.

      - **S3BucketName** *(string) --*

        Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See `Amazon
        S3 Bucket Naming Requirements
        <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__
        .

      - **S3KeyPrefix** *(string) --*

        Specifies the Amazon S3 key prefix that comes after the name of the bucket you have
        designated for log file delivery. For more information, see `Finding Your CloudTrail Log
        Files
        <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__
        .The maximum length is 200 characters.

      - **SnsTopicName** *(string) --*

        This field is no longer in use. Use SnsTopicARN.

      - **SnsTopicARN** *(string) --*

        Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when
        log files are delivered. The format of a topic ARN is:

         ``arn:aws:sns:us-east-2:123456789012:MyTopic``

      - **IncludeGlobalServiceEvents** *(boolean) --*

        Set to **True** to include AWS API calls from AWS global services such as IAM. Otherwise,
        **False** .

      - **IsMultiRegionTrail** *(boolean) --*

        Specifies whether the trail exists only in one region or exists in all regions.

      - **HomeRegion** *(string) --*

        The region in which the trail was created.

      - **TrailARN** *(string) --*

        Specifies the ARN of the trail. The format of a trail ARN is:

         ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

      - **LogFileValidationEnabled** *(boolean) --*

        Specifies whether log file validation is enabled.

      - **CloudWatchLogsLogGroupArn** *(string) --*

        Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group
        to which CloudTrail logs will be delivered.

      - **CloudWatchLogsRoleArn** *(string) --*

        Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log
        group.

      - **KmsKeyId** *(string) --*

        Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a
        fully specified ARN to a KMS key in the format:

         ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``

      - **HasCustomEventSelectors** *(boolean) --*

        Specifies if the trail has custom event selectors.

      - **IsOrganizationTrail** *(boolean) --*

        Specifies whether the trail is an organization trail.
    """


_ClientGetTrailStatusResponseTypeDef = TypedDict(
    "_ClientGetTrailStatusResponseTypeDef",
    {
        "IsLogging": bool,
        "LatestDeliveryError": str,
        "LatestNotificationError": str,
        "LatestDeliveryTime": datetime,
        "LatestNotificationTime": datetime,
        "StartLoggingTime": datetime,
        "StopLoggingTime": datetime,
        "LatestCloudWatchLogsDeliveryError": str,
        "LatestCloudWatchLogsDeliveryTime": datetime,
        "LatestDigestDeliveryTime": datetime,
        "LatestDigestDeliveryError": str,
        "LatestDeliveryAttemptTime": str,
        "LatestNotificationAttemptTime": str,
        "LatestNotificationAttemptSucceeded": str,
        "LatestDeliveryAttemptSucceeded": str,
        "TimeLoggingStarted": str,
        "TimeLoggingStopped": str,
    },
    total=False,
)


class ClientGetTrailStatusResponseTypeDef(_ClientGetTrailStatusResponseTypeDef):
    """
    Type definition for `ClientGetTrailStatus` `Response`

    Returns the objects or data listed below if successful. Otherwise, returns an error.

    - **IsLogging** *(boolean) --*

      Whether the CloudTrail is currently logging AWS API calls.

    - **LatestDeliveryError** *(string) --*

      Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver log files
      to the designated bucket. For more information see the topic `Error Responses
      <https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html>`__ in the Amazon S3 API
      Reference.

      .. note::

        This error occurs only when there is a problem with the destination S3 bucket and will not
        occur for timeouts. To resolve the issue, create a new bucket and call ``UpdateTrail`` to
        specify the new bucket, or fix the existing objects so that CloudTrail can again write to
        the bucket.

    - **LatestNotificationError** *(string) --*

      Displays any Amazon SNS error that CloudTrail encountered when attempting to send a
      notification. For more information about Amazon SNS errors, see the `Amazon SNS Developer
      Guide <https://docs.aws.amazon.com/sns/latest/dg/welcome.html>`__ .

    - **LatestDeliveryTime** *(datetime) --*

      Specifies the date and time that CloudTrail last delivered log files to an account's Amazon
      S3 bucket.

    - **LatestNotificationTime** *(datetime) --*

      Specifies the date and time of the most recent Amazon SNS notification that CloudTrail has
      written a new log file to an account's Amazon S3 bucket.

    - **StartLoggingTime** *(datetime) --*

      Specifies the most recent date and time when CloudTrail started recording API calls for an
      AWS account.

    - **StopLoggingTime** *(datetime) --*

      Specifies the most recent date and time when CloudTrail stopped recording API calls for an
      AWS account.

    - **LatestCloudWatchLogsDeliveryError** *(string) --*

      Displays any CloudWatch Logs error that CloudTrail encountered when attempting to deliver
      logs to CloudWatch Logs.

    - **LatestCloudWatchLogsDeliveryTime** *(datetime) --*

      Displays the most recent date and time when CloudTrail delivered logs to CloudWatch Logs.

    - **LatestDigestDeliveryTime** *(datetime) --*

      Specifies the date and time that CloudTrail last delivered a digest file to an account's
      Amazon S3 bucket.

    - **LatestDigestDeliveryError** *(string) --*

      Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver a digest
      file to the designated bucket. For more information see the topic `Error Responses
      <https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html>`__ in the Amazon S3 API
      Reference.

      .. note::

        This error occurs only when there is a problem with the destination S3 bucket and will not
        occur for timeouts. To resolve the issue, create a new bucket and call ``UpdateTrail`` to
        specify the new bucket, or fix the existing objects so that CloudTrail can again write to
        the bucket.

    - **LatestDeliveryAttemptTime** *(string) --*

      This field is no longer in use.

    - **LatestNotificationAttemptTime** *(string) --*

      This field is no longer in use.

    - **LatestNotificationAttemptSucceeded** *(string) --*

      This field is no longer in use.

    - **LatestDeliveryAttemptSucceeded** *(string) --*

      This field is no longer in use.

    - **TimeLoggingStarted** *(string) --*

      This field is no longer in use.

    - **TimeLoggingStopped** *(string) --*

      This field is no longer in use.
    """


_ClientListPublicKeysResponsePublicKeyListTypeDef = TypedDict(
    "_ClientListPublicKeysResponsePublicKeyListTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)


class ClientListPublicKeysResponsePublicKeyListTypeDef(
    _ClientListPublicKeysResponsePublicKeyListTypeDef
):
    """
    Type definition for `ClientListPublicKeysResponse` `PublicKeyList`

    Contains information about a returned public key.

    - **Value** *(bytes) --*

      The DER encoded public key value in PKCS#1 format.

    - **ValidityStartTime** *(datetime) --*

      The starting time of validity of the public key.

    - **ValidityEndTime** *(datetime) --*

      The ending time of validity of the public key.

    - **Fingerprint** *(string) --*

      The fingerprint of the public key.
    """


_ClientListPublicKeysResponseTypeDef = TypedDict(
    "_ClientListPublicKeysResponseTypeDef",
    {
        "PublicKeyList": List[ClientListPublicKeysResponsePublicKeyListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListPublicKeysResponseTypeDef(_ClientListPublicKeysResponseTypeDef):
    """
    Type definition for `ClientListPublicKeys` `Response`

    Returns the objects or data listed below if successful. Otherwise, returns an error.

    - **PublicKeyList** *(list) --*

      Contains an array of PublicKey objects.

      .. note::

        The returned public keys may have validity time ranges that overlap.

      - *(dict) --*

        Contains information about a returned public key.

        - **Value** *(bytes) --*

          The DER encoded public key value in PKCS#1 format.

        - **ValidityStartTime** *(datetime) --*

          The starting time of validity of the public key.

        - **ValidityEndTime** *(datetime) --*

          The ending time of validity of the public key.

        - **Fingerprint** *(string) --*

          The fingerprint of the public key.

    - **NextToken** *(string) --*

      Reserved for future use.
    """


_ClientListTagsResponseResourceTagListTagsListTypeDef = TypedDict(
    "_ClientListTagsResponseResourceTagListTagsListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsResponseResourceTagListTagsListTypeDef(
    _ClientListTagsResponseResourceTagListTagsListTypeDef
):
    """
    Type definition for `ClientListTagsResponseResourceTagList` `TagsList`

    A custom key-value pair associated with a resource such as a CloudTrail trail.

    - **Key** *(string) --*

      The key in a key-value pair. The key must be must be no longer than 128 Unicode
      characters. The key must be unique for the resource to which it applies.

    - **Value** *(string) --*

      The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
      characters.
    """


_ClientListTagsResponseResourceTagListTypeDef = TypedDict(
    "_ClientListTagsResponseResourceTagListTypeDef",
    {
        "ResourceId": str,
        "TagsList": List[ClientListTagsResponseResourceTagListTagsListTypeDef],
    },
    total=False,
)


class ClientListTagsResponseResourceTagListTypeDef(
    _ClientListTagsResponseResourceTagListTypeDef
):
    """
    Type definition for `ClientListTagsResponse` `ResourceTagList`

    A resource tag.

    - **ResourceId** *(string) --*

      Specifies the ARN of the resource.

    - **TagsList** *(list) --*

      A list of tags.

      - *(dict) --*

        A custom key-value pair associated with a resource such as a CloudTrail trail.

        - **Key** *(string) --*

          The key in a key-value pair. The key must be must be no longer than 128 Unicode
          characters. The key must be unique for the resource to which it applies.

        - **Value** *(string) --*

          The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
          characters.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {
        "ResourceTagList": List[ClientListTagsResponseResourceTagListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    Returns the objects or data listed below if successful. Otherwise, returns an error.

    - **ResourceTagList** *(list) --*

      A list of resource tags.

      - *(dict) --*

        A resource tag.

        - **ResourceId** *(string) --*

          Specifies the ARN of the resource.

        - **TagsList** *(list) --*

          A list of tags.

          - *(dict) --*

            A custom key-value pair associated with a resource such as a CloudTrail trail.

            - **Key** *(string) --*

              The key in a key-value pair. The key must be must be no longer than 128 Unicode
              characters. The key must be unique for the resource to which it applies.

            - **Value** *(string) --*

              The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
              characters.

    - **NextToken** *(string) --*

      Reserved for future use.
    """


_ClientListTrailsResponseTrailsTypeDef = TypedDict(
    "_ClientListTrailsResponseTrailsTypeDef",
    {"TrailARN": str, "Name": str, "HomeRegion": str},
    total=False,
)


class ClientListTrailsResponseTrailsTypeDef(_ClientListTrailsResponseTrailsTypeDef):
    """
    Type definition for `ClientListTrailsResponse` `Trails`

    Information about a CloudTrail trail, including the trail's name, home region, and Amazon
    Resource Name (ARN).

    - **TrailARN** *(string) --*

      The ARN of a trail.

    - **Name** *(string) --*

      The name of a trail.

    - **HomeRegion** *(string) --*

      The AWS region in which a trail was created.
    """


_ClientListTrailsResponseTypeDef = TypedDict(
    "_ClientListTrailsResponseTypeDef",
    {"Trails": List[ClientListTrailsResponseTrailsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTrailsResponseTypeDef(_ClientListTrailsResponseTypeDef):
    """
    Type definition for `ClientListTrails` `Response`

    - **Trails** *(list) --*

      Returns the name, ARN, and home region of trails in the current account.

      - *(dict) --*

        Information about a CloudTrail trail, including the trail's name, home region, and Amazon
        Resource Name (ARN).

        - **TrailARN** *(string) --*

          The ARN of a trail.

        - **Name** *(string) --*

          The name of a trail.

        - **HomeRegion** *(string) --*

          The AWS region in which a trail was created.

    - **NextToken** *(string) --*
    """


_ClientLookupEventsLookupAttributesTypeDef = TypedDict(
    "_ClientLookupEventsLookupAttributesTypeDef",
    {"AttributeKey": str, "AttributeValue": str},
)


class ClientLookupEventsLookupAttributesTypeDef(
    _ClientLookupEventsLookupAttributesTypeDef
):
    """
    Type definition for `ClientLookupEvents` `LookupAttributes`

    Specifies an attribute and value that filter the events returned.

    - **AttributeKey** *(string) --* **[REQUIRED]**

      Specifies an attribute on which to filter the events returned.

    - **AttributeValue** *(string) --* **[REQUIRED]**

      Specifies a value for the specified AttributeKey.
    """


_ClientLookupEventsResponseEventsResourcesTypeDef = TypedDict(
    "_ClientLookupEventsResponseEventsResourcesTypeDef",
    {"ResourceType": str, "ResourceName": str},
    total=False,
)


class ClientLookupEventsResponseEventsResourcesTypeDef(
    _ClientLookupEventsResponseEventsResourcesTypeDef
):
    """
    Type definition for `ClientLookupEventsResponseEvents` `Resources`

    Specifies the type and name of a resource referenced by an event.

    - **ResourceType** *(string) --*

      The type of a resource referenced by the event returned. When the resource type
      cannot be determined, null is returned. Some examples of resource types are:
      **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and
      **AccessKey** for IAM. To learn more about how to look up and filter events by the
      resource types supported for a service, see `Filtering CloudTrail Events
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html#filtering-cloudtrail-events>`__
      .

    - **ResourceName** *(string) --*

      The name of the resource referenced by the event returned. These are user-created
      names whose values will depend on the environment. For example, the resource name
      might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an
      EC2 Instance.
    """


_ClientLookupEventsResponseEventsTypeDef = TypedDict(
    "_ClientLookupEventsResponseEventsTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List[ClientLookupEventsResponseEventsResourcesTypeDef],
        "CloudTrailEvent": str,
    },
    total=False,
)


class ClientLookupEventsResponseEventsTypeDef(_ClientLookupEventsResponseEventsTypeDef):
    """
    Type definition for `ClientLookupEventsResponse` `Events`

    Contains information about an event that was returned by a lookup request. The result
    includes a representation of a CloudTrail event.

    - **EventId** *(string) --*

      The CloudTrail ID of the event returned.

    - **EventName** *(string) --*

      The name of the event returned.

    - **ReadOnly** *(string) --*

      Information about whether the event is a write event or a read event.

    - **AccessKeyId** *(string) --*

      The AWS access key ID that was used to sign the request. If the request was made with
      temporary security credentials, this is the access key ID of the temporary credentials.

    - **EventTime** *(datetime) --*

      The date and time of the event returned.

    - **EventSource** *(string) --*

      The AWS service that the request was made to.

    - **Username** *(string) --*

      A user name or role name of the requester that called the API in the event returned.

    - **Resources** *(list) --*

      A list of resources referenced by the event returned.

      - *(dict) --*

        Specifies the type and name of a resource referenced by an event.

        - **ResourceType** *(string) --*

          The type of a resource referenced by the event returned. When the resource type
          cannot be determined, null is returned. Some examples of resource types are:
          **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and
          **AccessKey** for IAM. To learn more about how to look up and filter events by the
          resource types supported for a service, see `Filtering CloudTrail Events
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html#filtering-cloudtrail-events>`__
          .

        - **ResourceName** *(string) --*

          The name of the resource referenced by the event returned. These are user-created
          names whose values will depend on the environment. For example, the resource name
          might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an
          EC2 Instance.

    - **CloudTrailEvent** *(string) --*

      A JSON string that contains a representation of the event returned.
    """


_ClientLookupEventsResponseTypeDef = TypedDict(
    "_ClientLookupEventsResponseTypeDef",
    {"Events": List[ClientLookupEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientLookupEventsResponseTypeDef(_ClientLookupEventsResponseTypeDef):
    """
    Type definition for `ClientLookupEvents` `Response`

    Contains a response to a LookupEvents action.

    - **Events** *(list) --*

      A list of events returned based on the lookup attributes specified and the CloudTrail event.
      The events list is sorted by time. The most recent event is listed first.

      - *(dict) --*

        Contains information about an event that was returned by a lookup request. The result
        includes a representation of a CloudTrail event.

        - **EventId** *(string) --*

          The CloudTrail ID of the event returned.

        - **EventName** *(string) --*

          The name of the event returned.

        - **ReadOnly** *(string) --*

          Information about whether the event is a write event or a read event.

        - **AccessKeyId** *(string) --*

          The AWS access key ID that was used to sign the request. If the request was made with
          temporary security credentials, this is the access key ID of the temporary credentials.

        - **EventTime** *(datetime) --*

          The date and time of the event returned.

        - **EventSource** *(string) --*

          The AWS service that the request was made to.

        - **Username** *(string) --*

          A user name or role name of the requester that called the API in the event returned.

        - **Resources** *(list) --*

          A list of resources referenced by the event returned.

          - *(dict) --*

            Specifies the type and name of a resource referenced by an event.

            - **ResourceType** *(string) --*

              The type of a resource referenced by the event returned. When the resource type
              cannot be determined, null is returned. Some examples of resource types are:
              **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and
              **AccessKey** for IAM. To learn more about how to look up and filter events by the
              resource types supported for a service, see `Filtering CloudTrail Events
              <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html#filtering-cloudtrail-events>`__
              .

            - **ResourceName** *(string) --*

              The name of the resource referenced by the event returned. These are user-created
              names whose values will depend on the environment. For example, the resource name
              might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an
              EC2 Instance.

        - **CloudTrailEvent** *(string) --*

          A JSON string that contains a representation of the event returned.

    - **NextToken** *(string) --*

      The token to use to get the next page of results after a previous API call. If the token does
      not appear, there are no more results to return. The token must be passed in with the same
      parameters as the previous call. For example, if the original call specified an AttributeKey
      of 'Username' with a value of 'root', the call with NextToken should include those same
      parameters.
    """


_ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef = TypedDict(
    "_ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)


class ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef(
    _ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef
):
    """
    Type definition for `ClientPutEventSelectorsEventSelectors` `DataResources`

    The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for
    your trail to log data events. Data events provide insight into the resource operations
    performed on or within a resource itself. These are also known as data plane operations.
    You can specify up to 250 data resources for a trail.

    .. note::

      The total number of allowed data resources is 250. This number can be distributed between
      1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

    The following example demonstrates how logging works when you configure logging of all data
    events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user specified
    an empty prefix, and the option to log both ``Read`` and ``Write`` data events.

    * A user uploads an image file to ``bucket-1`` .

    * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a
    data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty
    prefix, events that occur on any object in that bucket are logged. The trail processes and
    logs the event.

    * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .

    * The ``PutObject`` API operation occurred for an object in an S3 bucket that the
    CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

    The following example demonstrates how logging works when you configure logging of AWS
    Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS
    Lambda functions.

    * A user runs a script that includes a call to the *MyLambdaFunction* function and the
    *MyOtherLambdaFunction* function.

    * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is recorded
    as a data event in CloudTrail. Because the CloudTrail user specified logging data events
    for *MyLambdaFunction* , any invocations of that function are logged. The trail processes
    and logs the event.

    * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because the
    CloudTrail user did not specify logging data events for all Lambda functions, the
    ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified for
    the trail. The trail doesn’t log the event.

    - **Type** *(string) --*

      The resource type in which you want to log data events. You can specify
      ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.

    - **Values** *(list) --*

      An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified
      objects.

      * To log data events for all objects in all S3 buckets in your AWS account, specify the
      prefix as ``arn:aws:s3:::`` .

      .. note::

         This will also enable logging of data event activity performed by any user or role in
         your AWS account, even if that activity is performed on a bucket that belongs to
         another AWS account.

      * To log data events for all objects in an S3 bucket, specify the bucket and an empty
      object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all
      objects in this S3 bucket.

      * To log data events for specific objects, specify the S3 bucket and object prefix such
      as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in
      this S3 bucket that match the prefix.

      * To log data events for all functions in your AWS account, specify the prefix as
      ``arn:aws:lambda`` .

      .. note::

         This will also enable logging of ``Invoke`` activity performed by any user or role in
         your AWS account, even if that activity is performed on a function that belongs to
         another AWS account.

      * To log data events for a specific Lambda function, specify the function ARN.

      .. note::

         Lambda function ARNs are exact. For example, if you specify a function ARN
         *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be
         logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not
         be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

      - *(string) --*
    """


_ClientPutEventSelectorsEventSelectorsTypeDef = TypedDict(
    "_ClientPutEventSelectorsEventSelectorsTypeDef",
    {
        "ReadWriteType": str,
        "IncludeManagementEvents": bool,
        "DataResources": List[
            ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef
        ],
    },
    total=False,
)


class ClientPutEventSelectorsEventSelectorsTypeDef(
    _ClientPutEventSelectorsEventSelectorsTypeDef
):
    """
    Type definition for `ClientPutEventSelectors` `EventSelectors`

    Use event selectors to further specify the management and data event settings for your trail.
    By default, trails created without specific event selectors will be configured to log all read
    and write management events, and no data events. When an event occurs in your account,
    CloudTrail evaluates the event selector for all trails. For each trail, if the event matches
    any event selector, the trail processes and logs the event. If the event doesn't match any
    event selector, the trail doesn't log the event.

    You can configure up to five event selectors for a trail.

    - **ReadWriteType** *(string) --*

      Specify if you want your trail to log read-only events, write-only events, or all. For
      example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a
      write-only API operation.

      By default, the value is ``All`` .

    - **IncludeManagementEvents** *(boolean) --*

      Specify if you want your event selector to include management events for your trail.

      For more information, see `Management Events
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__
      in the *AWS CloudTrail User Guide* .

      By default, the value is ``true`` .

    - **DataResources** *(list) --*

      CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You
      can specify up to 250 resources for an individual event selector, but the total number of
      data resources cannot exceed 250 across all event selectors in a trail. This limit does not
      apply if you configure resource logging for all data events.

      For more information, see `Data Events
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__
      and `Limits in AWS CloudTrail
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__
      in the *AWS CloudTrail User Guide* .

      - *(dict) --*

        The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for
        your trail to log data events. Data events provide insight into the resource operations
        performed on or within a resource itself. These are also known as data plane operations.
        You can specify up to 250 data resources for a trail.

        .. note::

          The total number of allowed data resources is 250. This number can be distributed between
          1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

        The following example demonstrates how logging works when you configure logging of all data
        events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user specified
        an empty prefix, and the option to log both ``Read`` and ``Write`` data events.

        * A user uploads an image file to ``bucket-1`` .

        * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a
        data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty
        prefix, events that occur on any object in that bucket are logged. The trail processes and
        logs the event.

        * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .

        * The ``PutObject`` API operation occurred for an object in an S3 bucket that the
        CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

        The following example demonstrates how logging works when you configure logging of AWS
        Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS
        Lambda functions.

        * A user runs a script that includes a call to the *MyLambdaFunction* function and the
        *MyOtherLambdaFunction* function.

        * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is recorded
        as a data event in CloudTrail. Because the CloudTrail user specified logging data events
        for *MyLambdaFunction* , any invocations of that function are logged. The trail processes
        and logs the event.

        * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because the
        CloudTrail user did not specify logging data events for all Lambda functions, the
        ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified for
        the trail. The trail doesn’t log the event.

        - **Type** *(string) --*

          The resource type in which you want to log data events. You can specify
          ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.

        - **Values** *(list) --*

          An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified
          objects.

          * To log data events for all objects in all S3 buckets in your AWS account, specify the
          prefix as ``arn:aws:s3:::`` .

          .. note::

             This will also enable logging of data event activity performed by any user or role in
             your AWS account, even if that activity is performed on a bucket that belongs to
             another AWS account.

          * To log data events for all objects in an S3 bucket, specify the bucket and an empty
          object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all
          objects in this S3 bucket.

          * To log data events for specific objects, specify the S3 bucket and object prefix such
          as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in
          this S3 bucket that match the prefix.

          * To log data events for all functions in your AWS account, specify the prefix as
          ``arn:aws:lambda`` .

          .. note::

             This will also enable logging of ``Invoke`` activity performed by any user or role in
             your AWS account, even if that activity is performed on a function that belongs to
             another AWS account.

          * To log data events for a specific Lambda function, specify the function ARN.

          .. note::

             Lambda function ARNs are exact. For example, if you specify a function ARN
             *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be
             logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not
             be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

          - *(string) --*
    """


_ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef = TypedDict(
    "_ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)


class ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef(
    _ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef
):
    """
    Type definition for `ClientPutEventSelectorsResponseEventSelectors` `DataResources`

    The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors
    for your trail to log data events. Data events provide insight into the resource
    operations performed on or within a resource itself. These are also known as data plane
    operations. You can specify up to 250 data resources for a trail.

    .. note::

      The total number of allowed data resources is 250. This number can be distributed
      between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

    The following example demonstrates how logging works when you configure logging of all
    data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user
    specified an empty prefix, and the option to log both ``Read`` and ``Write`` data
    events.

    * A user uploads an image file to ``bucket-1`` .

    * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a
    data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an
    empty prefix, events that occur on any object in that bucket are logged. The trail
    processes and logs the event.

    * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .

    * The ``PutObject`` API operation occurred for an object in an S3 bucket that the
    CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

    The following example demonstrates how logging works when you configure logging of AWS
    Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS
    Lambda functions.

    * A user runs a script that includes a call to the *MyLambdaFunction* function and the
    *MyOtherLambdaFunction* function.

    * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is
    recorded as a data event in CloudTrail. Because the CloudTrail user specified logging
    data events for *MyLambdaFunction* , any invocations of that function are logged. The
    trail processes and logs the event.

    * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because
    the CloudTrail user did not specify logging data events for all Lambda functions, the
    ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified
    for the trail. The trail doesn’t log the event.

    - **Type** *(string) --*

      The resource type in which you want to log data events. You can specify
      ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.

    - **Values** *(list) --*

      An array of Amazon Resource Name (ARN) strings or partial ARN strings for the
      specified objects.

      * To log data events for all objects in all S3 buckets in your AWS account, specify
      the prefix as ``arn:aws:s3:::`` .

      .. note::

         This will also enable logging of data event activity performed by any user or role
         in your AWS account, even if that activity is performed on a bucket that belongs
         to another AWS account.

      * To log data events for all objects in an S3 bucket, specify the bucket and an empty
      object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all
      objects in this S3 bucket.

      * To log data events for specific objects, specify the S3 bucket and object prefix
      such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for
      objects in this S3 bucket that match the prefix.

      * To log data events for all functions in your AWS account, specify the prefix as
      ``arn:aws:lambda`` .

      .. note::

         This will also enable logging of ``Invoke`` activity performed by any user or role
         in your AWS account, even if that activity is performed on a function that belongs
         to another AWS account.

      * To log data events for a specific Lambda function, specify the function ARN.

      .. note::

         Lambda function ARNs are exact. For example, if you specify a function ARN
         *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will
         only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* .
         They will not be logged for
         *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

      - *(string) --*
    """


_ClientPutEventSelectorsResponseEventSelectorsTypeDef = TypedDict(
    "_ClientPutEventSelectorsResponseEventSelectorsTypeDef",
    {
        "ReadWriteType": str,
        "IncludeManagementEvents": bool,
        "DataResources": List[
            ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef
        ],
    },
    total=False,
)


class ClientPutEventSelectorsResponseEventSelectorsTypeDef(
    _ClientPutEventSelectorsResponseEventSelectorsTypeDef
):
    """
    Type definition for `ClientPutEventSelectorsResponse` `EventSelectors`

    Use event selectors to further specify the management and data event settings for your
    trail. By default, trails created without specific event selectors will be configured to
    log all read and write management events, and no data events. When an event occurs in your
    account, CloudTrail evaluates the event selector for all trails. For each trail, if the
    event matches any event selector, the trail processes and logs the event. If the event
    doesn't match any event selector, the trail doesn't log the event.

    You can configure up to five event selectors for a trail.

    - **ReadWriteType** *(string) --*

      Specify if you want your trail to log read-only events, write-only events, or all. For
      example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances``
      is a write-only API operation.

      By default, the value is ``All`` .

    - **IncludeManagementEvents** *(boolean) --*

      Specify if you want your event selector to include management events for your trail.

      For more information, see `Management Events
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__
      in the *AWS CloudTrail User Guide* .

      By default, the value is ``true`` .

    - **DataResources** *(list) --*

      CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions.
      You can specify up to 250 resources for an individual event selector, but the total
      number of data resources cannot exceed 250 across all event selectors in a trail. This
      limit does not apply if you configure resource logging for all data events.

      For more information, see `Data Events
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__
      and `Limits in AWS CloudTrail
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__
      in the *AWS CloudTrail User Guide* .

      - *(dict) --*

        The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors
        for your trail to log data events. Data events provide insight into the resource
        operations performed on or within a resource itself. These are also known as data plane
        operations. You can specify up to 250 data resources for a trail.

        .. note::

          The total number of allowed data resources is 250. This number can be distributed
          between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

        The following example demonstrates how logging works when you configure logging of all
        data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user
        specified an empty prefix, and the option to log both ``Read`` and ``Write`` data
        events.

        * A user uploads an image file to ``bucket-1`` .

        * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a
        data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an
        empty prefix, events that occur on any object in that bucket are logged. The trail
        processes and logs the event.

        * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .

        * The ``PutObject`` API operation occurred for an object in an S3 bucket that the
        CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

        The following example demonstrates how logging works when you configure logging of AWS
        Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS
        Lambda functions.

        * A user runs a script that includes a call to the *MyLambdaFunction* function and the
        *MyOtherLambdaFunction* function.

        * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is
        recorded as a data event in CloudTrail. Because the CloudTrail user specified logging
        data events for *MyLambdaFunction* , any invocations of that function are logged. The
        trail processes and logs the event.

        * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because
        the CloudTrail user did not specify logging data events for all Lambda functions, the
        ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified
        for the trail. The trail doesn’t log the event.

        - **Type** *(string) --*

          The resource type in which you want to log data events. You can specify
          ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.

        - **Values** *(list) --*

          An array of Amazon Resource Name (ARN) strings or partial ARN strings for the
          specified objects.

          * To log data events for all objects in all S3 buckets in your AWS account, specify
          the prefix as ``arn:aws:s3:::`` .

          .. note::

             This will also enable logging of data event activity performed by any user or role
             in your AWS account, even if that activity is performed on a bucket that belongs
             to another AWS account.

          * To log data events for all objects in an S3 bucket, specify the bucket and an empty
          object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all
          objects in this S3 bucket.

          * To log data events for specific objects, specify the S3 bucket and object prefix
          such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for
          objects in this S3 bucket that match the prefix.

          * To log data events for all functions in your AWS account, specify the prefix as
          ``arn:aws:lambda`` .

          .. note::

             This will also enable logging of ``Invoke`` activity performed by any user or role
             in your AWS account, even if that activity is performed on a function that belongs
             to another AWS account.

          * To log data events for a specific Lambda function, specify the function ARN.

          .. note::

             Lambda function ARNs are exact. For example, if you specify a function ARN
             *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will
             only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* .
             They will not be logged for
             *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

          - *(string) --*
    """


_ClientPutEventSelectorsResponseTypeDef = TypedDict(
    "_ClientPutEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List[ClientPutEventSelectorsResponseEventSelectorsTypeDef],
    },
    total=False,
)


class ClientPutEventSelectorsResponseTypeDef(_ClientPutEventSelectorsResponseTypeDef):
    """
    Type definition for `ClientPutEventSelectors` `Response`

    - **TrailARN** *(string) --*

      Specifies the ARN of the trail that was updated with event selectors. The format of a trail
      ARN is:

       ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

    - **EventSelectors** *(list) --*

      Specifies the event selectors configured for your trail.

      - *(dict) --*

        Use event selectors to further specify the management and data event settings for your
        trail. By default, trails created without specific event selectors will be configured to
        log all read and write management events, and no data events. When an event occurs in your
        account, CloudTrail evaluates the event selector for all trails. For each trail, if the
        event matches any event selector, the trail processes and logs the event. If the event
        doesn't match any event selector, the trail doesn't log the event.

        You can configure up to five event selectors for a trail.

        - **ReadWriteType** *(string) --*

          Specify if you want your trail to log read-only events, write-only events, or all. For
          example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances``
          is a write-only API operation.

          By default, the value is ``All`` .

        - **IncludeManagementEvents** *(boolean) --*

          Specify if you want your event selector to include management events for your trail.

          For more information, see `Management Events
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__
          in the *AWS CloudTrail User Guide* .

          By default, the value is ``true`` .

        - **DataResources** *(list) --*

          CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions.
          You can specify up to 250 resources for an individual event selector, but the total
          number of data resources cannot exceed 250 across all event selectors in a trail. This
          limit does not apply if you configure resource logging for all data events.

          For more information, see `Data Events
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__
          and `Limits in AWS CloudTrail
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__
          in the *AWS CloudTrail User Guide* .

          - *(dict) --*

            The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors
            for your trail to log data events. Data events provide insight into the resource
            operations performed on or within a resource itself. These are also known as data plane
            operations. You can specify up to 250 data resources for a trail.

            .. note::

              The total number of allowed data resources is 250. This number can be distributed
              between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

            The following example demonstrates how logging works when you configure logging of all
            data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user
            specified an empty prefix, and the option to log both ``Read`` and ``Write`` data
            events.

            * A user uploads an image file to ``bucket-1`` .

            * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a
            data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an
            empty prefix, events that occur on any object in that bucket are logged. The trail
            processes and logs the event.

            * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .

            * The ``PutObject`` API operation occurred for an object in an S3 bucket that the
            CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

            The following example demonstrates how logging works when you configure logging of AWS
            Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS
            Lambda functions.

            * A user runs a script that includes a call to the *MyLambdaFunction* function and the
            *MyOtherLambdaFunction* function.

            * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is
            recorded as a data event in CloudTrail. Because the CloudTrail user specified logging
            data events for *MyLambdaFunction* , any invocations of that function are logged. The
            trail processes and logs the event.

            * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because
            the CloudTrail user did not specify logging data events for all Lambda functions, the
            ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified
            for the trail. The trail doesn’t log the event.

            - **Type** *(string) --*

              The resource type in which you want to log data events. You can specify
              ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.

            - **Values** *(list) --*

              An array of Amazon Resource Name (ARN) strings or partial ARN strings for the
              specified objects.

              * To log data events for all objects in all S3 buckets in your AWS account, specify
              the prefix as ``arn:aws:s3:::`` .

              .. note::

                 This will also enable logging of data event activity performed by any user or role
                 in your AWS account, even if that activity is performed on a bucket that belongs
                 to another AWS account.

              * To log data events for all objects in an S3 bucket, specify the bucket and an empty
              object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all
              objects in this S3 bucket.

              * To log data events for specific objects, specify the S3 bucket and object prefix
              such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for
              objects in this S3 bucket that match the prefix.

              * To log data events for all functions in your AWS account, specify the prefix as
              ``arn:aws:lambda`` .

              .. note::

                 This will also enable logging of ``Invoke`` activity performed by any user or role
                 in your AWS account, even if that activity is performed on a function that belongs
                 to another AWS account.

              * To log data events for a specific Lambda function, specify the function ARN.

              .. note::

                 Lambda function ARNs are exact. For example, if you specify a function ARN
                 *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will
                 only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* .
                 They will not be logged for
                 *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

              - *(string) --*
    """


_RequiredClientRemoveTagsTagsListTypeDef = TypedDict(
    "_RequiredClientRemoveTagsTagsListTypeDef", {"Key": str}
)
_OptionalClientRemoveTagsTagsListTypeDef = TypedDict(
    "_OptionalClientRemoveTagsTagsListTypeDef", {"Value": str}, total=False
)


class ClientRemoveTagsTagsListTypeDef(
    _RequiredClientRemoveTagsTagsListTypeDef, _OptionalClientRemoveTagsTagsListTypeDef
):
    """
    Type definition for `ClientRemoveTags` `TagsList`

    A custom key-value pair associated with a resource such as a CloudTrail trail.

    - **Key** *(string) --* **[REQUIRED]**

      The key in a key-value pair. The key must be must be no longer than 128 Unicode characters.
      The key must be unique for the resource to which it applies.

    - **Value** *(string) --*

      The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
      characters.
    """


_ClientUpdateTrailResponseTypeDef = TypedDict(
    "_ClientUpdateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class ClientUpdateTrailResponseTypeDef(_ClientUpdateTrailResponseTypeDef):
    """
    Type definition for `ClientUpdateTrail` `Response`

    Returns the objects or data listed below if successful. Otherwise, returns an error.

    - **Name** *(string) --*

      Specifies the name of the trail.

    - **S3BucketName** *(string) --*

      Specifies the name of the Amazon S3 bucket designated for publishing log files.

    - **S3KeyPrefix** *(string) --*

      Specifies the Amazon S3 key prefix that comes after the name of the bucket you have
      designated for log file delivery. For more information, see `Finding Your CloudTrail Log
      Files
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__
      .

    - **SnsTopicName** *(string) --*

      This field is no longer in use. Use SnsTopicARN.

    - **SnsTopicARN** *(string) --*

      Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log
      files are delivered. The format of a topic ARN is:

       ``arn:aws:sns:us-east-2:123456789012:MyTopic``

    - **IncludeGlobalServiceEvents** *(boolean) --*

      Specifies whether the trail is publishing events from global services such as IAM to the log
      files.

    - **IsMultiRegionTrail** *(boolean) --*

      Specifies whether the trail exists in one region or in all regions.

    - **TrailARN** *(string) --*

      Specifies the ARN of the trail that was updated. The format of a trail ARN is:

       ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

    - **LogFileValidationEnabled** *(boolean) --*

      Specifies whether log file integrity validation is enabled.

    - **CloudWatchLogsLogGroupArn** *(string) --*

      Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be
      delivered.

    - **CloudWatchLogsRoleArn** *(string) --*

      Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

    - **KmsKeyId** *(string) --*

      Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully
      specified ARN to a KMS key in the format:

       ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``

    - **IsOrganizationTrail** *(boolean) --*

      Specifies whether the trail is an organization trail.
    """


_ListPublicKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPublicKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPublicKeysPaginatePaginationConfigTypeDef(
    _ListPublicKeysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPublicKeysPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListPublicKeysPaginateResponsePublicKeyListTypeDef = TypedDict(
    "_ListPublicKeysPaginateResponsePublicKeyListTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)


class ListPublicKeysPaginateResponsePublicKeyListTypeDef(
    _ListPublicKeysPaginateResponsePublicKeyListTypeDef
):
    """
    Type definition for `ListPublicKeysPaginateResponse` `PublicKeyList`

    Contains information about a returned public key.

    - **Value** *(bytes) --*

      The DER encoded public key value in PKCS#1 format.

    - **ValidityStartTime** *(datetime) --*

      The starting time of validity of the public key.

    - **ValidityEndTime** *(datetime) --*

      The ending time of validity of the public key.

    - **Fingerprint** *(string) --*

      The fingerprint of the public key.
    """


_ListPublicKeysPaginateResponseTypeDef = TypedDict(
    "_ListPublicKeysPaginateResponseTypeDef",
    {"PublicKeyList": List[ListPublicKeysPaginateResponsePublicKeyListTypeDef]},
    total=False,
)


class ListPublicKeysPaginateResponseTypeDef(_ListPublicKeysPaginateResponseTypeDef):
    """
    Type definition for `ListPublicKeysPaginate` `Response`

    Returns the objects or data listed below if successful. Otherwise, returns an error.

    - **PublicKeyList** *(list) --*

      Contains an array of PublicKey objects.

      .. note::

        The returned public keys may have validity time ranges that overlap.

      - *(dict) --*

        Contains information about a returned public key.

        - **Value** *(bytes) --*

          The DER encoded public key value in PKCS#1 format.

        - **ValidityStartTime** *(datetime) --*

          The starting time of validity of the public key.

        - **ValidityEndTime** *(datetime) --*

          The ending time of validity of the public key.

        - **Fingerprint** *(string) --*

          The fingerprint of the public key.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListTagsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListTagsPaginateResponseResourceTagListTagsListTypeDef = TypedDict(
    "_ListTagsPaginateResponseResourceTagListTagsListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsPaginateResponseResourceTagListTagsListTypeDef(
    _ListTagsPaginateResponseResourceTagListTagsListTypeDef
):
    """
    Type definition for `ListTagsPaginateResponseResourceTagList` `TagsList`

    A custom key-value pair associated with a resource such as a CloudTrail trail.

    - **Key** *(string) --*

      The key in a key-value pair. The key must be must be no longer than 128 Unicode
      characters. The key must be unique for the resource to which it applies.

    - **Value** *(string) --*

      The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
      characters.
    """


_ListTagsPaginateResponseResourceTagListTypeDef = TypedDict(
    "_ListTagsPaginateResponseResourceTagListTypeDef",
    {
        "ResourceId": str,
        "TagsList": List[ListTagsPaginateResponseResourceTagListTagsListTypeDef],
    },
    total=False,
)


class ListTagsPaginateResponseResourceTagListTypeDef(
    _ListTagsPaginateResponseResourceTagListTypeDef
):
    """
    Type definition for `ListTagsPaginateResponse` `ResourceTagList`

    A resource tag.

    - **ResourceId** *(string) --*

      Specifies the ARN of the resource.

    - **TagsList** *(list) --*

      A list of tags.

      - *(dict) --*

        A custom key-value pair associated with a resource such as a CloudTrail trail.

        - **Key** *(string) --*

          The key in a key-value pair. The key must be must be no longer than 128 Unicode
          characters. The key must be unique for the resource to which it applies.

        - **Value** *(string) --*

          The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
          characters.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"ResourceTagList": List[ListTagsPaginateResponseResourceTagListTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    Type definition for `ListTagsPaginate` `Response`

    Returns the objects or data listed below if successful. Otherwise, returns an error.

    - **ResourceTagList** *(list) --*

      A list of resource tags.

      - *(dict) --*

        A resource tag.

        - **ResourceId** *(string) --*

          Specifies the ARN of the resource.

        - **TagsList** *(list) --*

          A list of tags.

          - *(dict) --*

            A custom key-value pair associated with a resource such as a CloudTrail trail.

            - **Key** *(string) --*

              The key in a key-value pair. The key must be must be no longer than 128 Unicode
              characters. The key must be unique for the resource to which it applies.

            - **Value** *(string) --*

              The value in a key-value pair of a tag. The value must be no longer than 256 Unicode
              characters.
    """


_ListTrailsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTrailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTrailsPaginatePaginationConfigTypeDef(
    _ListTrailsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTrailsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListTrailsPaginateResponseTrailsTypeDef = TypedDict(
    "_ListTrailsPaginateResponseTrailsTypeDef",
    {"TrailARN": str, "Name": str, "HomeRegion": str},
    total=False,
)


class ListTrailsPaginateResponseTrailsTypeDef(_ListTrailsPaginateResponseTrailsTypeDef):
    """
    Type definition for `ListTrailsPaginateResponse` `Trails`

    Information about a CloudTrail trail, including the trail's name, home region, and Amazon
    Resource Name (ARN).

    - **TrailARN** *(string) --*

      The ARN of a trail.

    - **Name** *(string) --*

      The name of a trail.

    - **HomeRegion** *(string) --*

      The AWS region in which a trail was created.
    """


_ListTrailsPaginateResponseTypeDef = TypedDict(
    "_ListTrailsPaginateResponseTypeDef",
    {"Trails": List[ListTrailsPaginateResponseTrailsTypeDef]},
    total=False,
)


class ListTrailsPaginateResponseTypeDef(_ListTrailsPaginateResponseTypeDef):
    """
    Type definition for `ListTrailsPaginate` `Response`

    - **Trails** *(list) --*

      Returns the name, ARN, and home region of trails in the current account.

      - *(dict) --*

        Information about a CloudTrail trail, including the trail's name, home region, and Amazon
        Resource Name (ARN).

        - **TrailARN** *(string) --*

          The ARN of a trail.

        - **Name** *(string) --*

          The name of a trail.

        - **HomeRegion** *(string) --*

          The AWS region in which a trail was created.
    """


_LookupEventsPaginateLookupAttributesTypeDef = TypedDict(
    "_LookupEventsPaginateLookupAttributesTypeDef",
    {"AttributeKey": str, "AttributeValue": str},
)


class LookupEventsPaginateLookupAttributesTypeDef(
    _LookupEventsPaginateLookupAttributesTypeDef
):
    """
    Type definition for `LookupEventsPaginate` `LookupAttributes`

    Specifies an attribute and value that filter the events returned.

    - **AttributeKey** *(string) --* **[REQUIRED]**

      Specifies an attribute on which to filter the events returned.

    - **AttributeValue** *(string) --* **[REQUIRED]**

      Specifies a value for the specified AttributeKey.
    """


_LookupEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_LookupEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class LookupEventsPaginatePaginationConfigTypeDef(
    _LookupEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `LookupEventsPaginate` `PaginationConfig`

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


_LookupEventsPaginateResponseEventsResourcesTypeDef = TypedDict(
    "_LookupEventsPaginateResponseEventsResourcesTypeDef",
    {"ResourceType": str, "ResourceName": str},
    total=False,
)


class LookupEventsPaginateResponseEventsResourcesTypeDef(
    _LookupEventsPaginateResponseEventsResourcesTypeDef
):
    """
    Type definition for `LookupEventsPaginateResponseEvents` `Resources`

    Specifies the type and name of a resource referenced by an event.

    - **ResourceType** *(string) --*

      The type of a resource referenced by the event returned. When the resource type
      cannot be determined, null is returned. Some examples of resource types are:
      **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and
      **AccessKey** for IAM. To learn more about how to look up and filter events by the
      resource types supported for a service, see `Filtering CloudTrail Events
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html#filtering-cloudtrail-events>`__
      .

    - **ResourceName** *(string) --*

      The name of the resource referenced by the event returned. These are user-created
      names whose values will depend on the environment. For example, the resource name
      might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an
      EC2 Instance.
    """


_LookupEventsPaginateResponseEventsTypeDef = TypedDict(
    "_LookupEventsPaginateResponseEventsTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List[LookupEventsPaginateResponseEventsResourcesTypeDef],
        "CloudTrailEvent": str,
    },
    total=False,
)


class LookupEventsPaginateResponseEventsTypeDef(
    _LookupEventsPaginateResponseEventsTypeDef
):
    """
    Type definition for `LookupEventsPaginateResponse` `Events`

    Contains information about an event that was returned by a lookup request. The result
    includes a representation of a CloudTrail event.

    - **EventId** *(string) --*

      The CloudTrail ID of the event returned.

    - **EventName** *(string) --*

      The name of the event returned.

    - **ReadOnly** *(string) --*

      Information about whether the event is a write event or a read event.

    - **AccessKeyId** *(string) --*

      The AWS access key ID that was used to sign the request. If the request was made with
      temporary security credentials, this is the access key ID of the temporary credentials.

    - **EventTime** *(datetime) --*

      The date and time of the event returned.

    - **EventSource** *(string) --*

      The AWS service that the request was made to.

    - **Username** *(string) --*

      A user name or role name of the requester that called the API in the event returned.

    - **Resources** *(list) --*

      A list of resources referenced by the event returned.

      - *(dict) --*

        Specifies the type and name of a resource referenced by an event.

        - **ResourceType** *(string) --*

          The type of a resource referenced by the event returned. When the resource type
          cannot be determined, null is returned. Some examples of resource types are:
          **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and
          **AccessKey** for IAM. To learn more about how to look up and filter events by the
          resource types supported for a service, see `Filtering CloudTrail Events
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html#filtering-cloudtrail-events>`__
          .

        - **ResourceName** *(string) --*

          The name of the resource referenced by the event returned. These are user-created
          names whose values will depend on the environment. For example, the resource name
          might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an
          EC2 Instance.

    - **CloudTrailEvent** *(string) --*

      A JSON string that contains a representation of the event returned.
    """


_LookupEventsPaginateResponseTypeDef = TypedDict(
    "_LookupEventsPaginateResponseTypeDef",
    {"Events": List[LookupEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class LookupEventsPaginateResponseTypeDef(_LookupEventsPaginateResponseTypeDef):
    """
    Type definition for `LookupEventsPaginate` `Response`

    Contains a response to a LookupEvents action.

    - **Events** *(list) --*

      A list of events returned based on the lookup attributes specified and the CloudTrail event.
      The events list is sorted by time. The most recent event is listed first.

      - *(dict) --*

        Contains information about an event that was returned by a lookup request. The result
        includes a representation of a CloudTrail event.

        - **EventId** *(string) --*

          The CloudTrail ID of the event returned.

        - **EventName** *(string) --*

          The name of the event returned.

        - **ReadOnly** *(string) --*

          Information about whether the event is a write event or a read event.

        - **AccessKeyId** *(string) --*

          The AWS access key ID that was used to sign the request. If the request was made with
          temporary security credentials, this is the access key ID of the temporary credentials.

        - **EventTime** *(datetime) --*

          The date and time of the event returned.

        - **EventSource** *(string) --*

          The AWS service that the request was made to.

        - **Username** *(string) --*

          A user name or role name of the requester that called the API in the event returned.

        - **Resources** *(list) --*

          A list of resources referenced by the event returned.

          - *(dict) --*

            Specifies the type and name of a resource referenced by an event.

            - **ResourceType** *(string) --*

              The type of a resource referenced by the event returned. When the resource type
              cannot be determined, null is returned. Some examples of resource types are:
              **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and
              **AccessKey** for IAM. To learn more about how to look up and filter events by the
              resource types supported for a service, see `Filtering CloudTrail Events
              <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html#filtering-cloudtrail-events>`__
              .

            - **ResourceName** *(string) --*

              The name of the resource referenced by the event returned. These are user-created
              names whose values will depend on the environment. For example, the resource name
              might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an
              EC2 Instance.

        - **CloudTrailEvent** *(string) --*

          A JSON string that contains a representation of the event returned.
    """
