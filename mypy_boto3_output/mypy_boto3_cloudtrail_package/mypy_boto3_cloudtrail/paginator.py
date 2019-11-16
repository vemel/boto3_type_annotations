"Main interface for cloudtrail Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudtrail.type_defs import (
    ListPublicKeysPaginatePaginationConfigTypeDef,
    ListPublicKeysPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
    ListTrailsPaginatePaginationConfigTypeDef,
    ListTrailsPaginateResponseTypeDef,
    LookupEventsPaginateLookupAttributesTypeDef,
    LookupEventsPaginatePaginationConfigTypeDef,
    LookupEventsPaginateResponseTypeDef,
)


__all__ = (
    "ListPublicKeysPaginator",
    "ListTagsPaginator",
    "ListTrailsPaginator",
    "LookupEventsPaginator",
)


class ListPublicKeysPaginator(Boto3Paginator):
    """
    Paginator for `list_public_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: ListPublicKeysPaginatePaginationConfigTypeDef = None,
    ) -> ListPublicKeysPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CloudTrail.Client.list_public_keys`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/ListPublicKeys>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type StartTime: datetime
        :param StartTime:

          Optionally specifies, in UTC, the start of the time range to look up public keys for CloudTrail
          digest files. If not specified, the current time is used, and the current public key is returned.

        :type EndTime: datetime
        :param EndTime:

          Optionally specifies, in UTC, the end of the time range to look up public keys for CloudTrail
          digest files. If not specified, the current time is used.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PublicKeyList': [
                    {
                        'Value': b'bytes',
                        'ValidityStartTime': datetime(2015, 1, 1),
                        'ValidityEndTime': datetime(2015, 1, 1),
                        'Fingerprint': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

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


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceIdList: List[str],
        PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None,
    ) -> ListTagsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CloudTrail.Client.list_tags`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/ListTags>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ResourceIdList=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type ResourceIdList: list
        :param ResourceIdList: **[REQUIRED]**

          Specifies a list of trail ARNs whose tags will be listed. The list has a limit of 20 ARNs. The
          format of a trail ARN is:

           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceTagList': [
                    {
                        'ResourceId': 'string',
                        'TagsList': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

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


class ListTrailsPaginator(Boto3Paginator):
    """
    Paginator for `list_trails`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListTrailsPaginatePaginationConfigTypeDef = None
    ) -> ListTrailsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CloudTrail.Client.list_trails`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/ListTrails>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Trails': [
                    {
                        'TrailARN': 'string',
                        'Name': 'string',
                        'HomeRegion': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

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


class LookupEventsPaginator(Boto3Paginator):
    """
    Paginator for `lookup_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LookupAttributes: List[LookupEventsPaginateLookupAttributesTypeDef] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: LookupEventsPaginatePaginationConfigTypeDef = None,
    ) -> LookupEventsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CloudTrail.Client.lookup_events`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/LookupEvents>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              LookupAttributes=[
                  {
                      'AttributeKey':
                      'EventId'|'EventName'|'ReadOnly'|'Username'|'ResourceType'|'ResourceName'
                      |'EventSource'|'AccessKeyId',
                      'AttributeValue': 'string'
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type LookupAttributes: list
        :param LookupAttributes:

          Contains a list of lookup attributes. Currently the list can contain only one item.

          - *(dict) --*

            Specifies an attribute and value that filter the events returned.

            - **AttributeKey** *(string) --* **[REQUIRED]**

              Specifies an attribute on which to filter the events returned.

            - **AttributeValue** *(string) --* **[REQUIRED]**

              Specifies a value for the specified AttributeKey.

        :type StartTime: datetime
        :param StartTime:

          Specifies that only events that occur after or at the specified time are returned. If the
          specified start time is after the specified end time, an error is returned.

        :type EndTime: datetime
        :param EndTime:

          Specifies that only events that occur before or at the specified time are returned. If the
          specified end time is before the specified start time, an error is returned.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Events': [
                    {
                        'EventId': 'string',
                        'EventName': 'string',
                        'ReadOnly': 'string',
                        'AccessKeyId': 'string',
                        'EventTime': datetime(2015, 1, 1),
                        'EventSource': 'string',
                        'Username': 'string',
                        'Resources': [
                            {
                                'ResourceType': 'string',
                                'ResourceName': 'string'
                            },
                        ],
                        'CloudTrailEvent': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

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
