"Main interface for resourcegroupstaggingapi Client"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_resourcegroupstaggingapi.client as client_scope

# pylint: disable=import-self
import mypy_boto3_resourcegroupstaggingapi.paginator as paginator_scope
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    ClientGetResourcesResponseTypeDef,
    ClientGetResourcesTagFiltersTypeDef,
    ClientGetTagKeysResponseTypeDef,
    ClientGetTagValuesResponseTypeDef,
    ClientTagResourcesResponseTypeDef,
    ClientUntagResourcesResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resources(
        self,
        PaginationToken: str = None,
        TagFilters: List[ClientGetResourcesTagFiltersTypeDef] = None,
        ResourcesPerPage: int = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
    ) -> ClientGetResourcesResponseTypeDef:
        """
        Returns all the tagged or previously tagged resources that are located in the specified region for
        the AWS account. You can optionally specify *filters* (tags and resource types) in your request,
        depending on what information you want returned. The response includes all tags that are associated
        with the requested resources.

        .. note::

          You can check the ``PaginationToken`` response parameter to determine if a query completed.
          Queries can occasionally return fewer results on a page than allowed. The ``PaginationToken``
          response parameter value is ``null``  *only* when there are no more results to display.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetResources>`_

        **Request Syntax**
        ::

          response = client.get_resources(
              PaginationToken='string',
              TagFilters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ResourcesPerPage=123,
              TagsPerPage=123,
              ResourceTypeFilters=[
                  'string',
              ]
          )
        :type PaginationToken: string
        :param PaginationToken:

          A string that indicates that additional data is available. Leave this value empty for your
          initial request. If the response includes a ``PaginationToken`` , use that string for this value
          to request an additional page of data.

        :type TagFilters: list
        :param TagFilters:

          A list of TagFilters (keys and values). Each TagFilter specified must contain a key with values
          as optional. A request can include up to 50 keys, and each key can include up to 20 values.

          Note the following when deciding how to use TagFilters:

          * If you *do* specify a TagFilter, the response returns only those resources that are currently
          associated with the specified tag.

          * If you *don't* specify a TagFilter, the response includes all resources that were ever
          associated with tags. Resources that currently don't have associated tags are shown with an empty
          tag set, like this: ``"Tags": []`` .

          * If you specify more than one filter in a single request, the response returns only those
          resources that satisfy all specified filters.

          * If you specify a filter that contains more than one value for a key, the response returns
          resources that match any of the specified values for that key.

          * If you don't specify any values for a key, the response returns resources that are tagged with
          that key irrespective of the value. For example, for filters: filter1 = {key1, {value1}}, filter2
          = {key2, {value2,value3,value4}} , filter3 = {key3}:

            * GetResources( {filter1} ) returns resources tagged with key1=value1

            * GetResources( {filter2} ) returns resources tagged with key2=value2 or key2=value3 or
            key2=value4

            * GetResources( {filter3} ) returns resources tagged with any tag containing key3 as its tag
            key, irrespective of its value

            * GetResources( {filter1,filter2,filter3} ) returns resources tagged with ( key1=value1) and (
            key2=value2 or key2=value3 or key2=value4) and (key3, irrespective of the value)

          - *(dict) --*

            A list of tags (keys and values) that are used to specify the associated resources.

            - **Key** *(string) --*

              One part of a key-value pair that make up a tag. A key is a general label that acts like a
              category for more specific tag values.

            - **Values** *(list) --*

              The optional part of a key-value pair that make up a tag. A value acts as a descriptor within
              a tag category (key).

              - *(string) --*

        :type ResourcesPerPage: integer
        :param ResourcesPerPage:

          A limit that restricts the number of resources returned by GetResources in paginated output. You
          can set ResourcesPerPage to a minimum of 1 item and the maximum of 100 items.

        :type TagsPerPage: integer
        :param TagsPerPage:

          A limit that restricts the number of tags (key and value pairs) returned by GetResources in
          paginated output. A resource with no tags is counted as having one tag (one key and value pair).

           ``GetResources`` does not split a resource and its associated tags across pages. If the
           specified ``TagsPerPage`` would cause such a break, a ``PaginationToken`` is returned in place
           of the affected resource and its tags. Use that token in another request to get the remaining
           data. For example, if you specify a ``TagsPerPage`` of ``100`` and the account has 22 resources
           with 10 tags each (meaning that each resource has 10 key and value pairs), the output will
           consist of 3 pages, with the first page displaying the first 10 resources, each with its 10
           tags, the second page displaying the next 10 resources each with its 10 tags, and the third page
           displaying the remaining 2 resources, each with its 10 tags.

          You can set ``TagsPerPage`` to a minimum of 100 items and the maximum of 500 items.

        :type ResourceTypeFilters: list
        :param ResourceTypeFilters:

          The constraints on the resources that you want returned. The format of each resource type is
          ``service[:resourceType]`` . For example, specifying a resource type of ``ec2`` returns all
          Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of
          ``ec2:instance`` returns only EC2 instances.

          The string for each service name and resource type is the same as that embedded in a resource's
          Amazon Resource Name (ARN). Consult the *AWS General Reference* for the following:

          * For a list of service name strings, see `AWS Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          .

          * For resource type strings, see `Example ARNs
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax>`__ .

          * For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

          You can specify multiple resource types by using an array. The array can include up to 100 items.
          Note that the length constraint requirement applies to each resource type filter.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PaginationToken': 'string',
                'ResourceTagMappingList': [
                    {
                        'ResourceARN': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PaginationToken** *(string) --*

              A string that indicates that the response contains more data than can be returned in a single
              response. To receive additional data, specify this string for the ``PaginationToken`` value
              in a subsequent request.

            - **ResourceTagMappingList** *(list) --*

              A list of resource ARNs and the tags (keys and values) associated with each.

              - *(dict) --*

                A list of resource ARNs and the tags (keys and values) that are associated with each.

                - **ResourceARN** *(string) --*

                  The ARN of the resource.

                - **Tags** *(list) --*

                  The tags that have been applied to one or more AWS resources.

                  - *(dict) --*

                    The metadata that you apply to AWS resources to help you categorize and organize them.
                    Each tag consists of a key and an optional value, both of which you define. For more
                    information, see `Tag Basics
                    <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in
                    the *Amazon EC2 User Guide for Linux Instances* .

                    - **Key** *(string) --*

                      One part of a key-value pair that make up a tag. A key is a general label that acts
                      like a category for more specific tag values.

                    - **Value** *(string) --*

                      The optional part of a key-value pair that make up a tag. A value acts as a
                      descriptor within a tag category (key).

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tag_keys(
        self, PaginationToken: str = None
    ) -> ClientGetTagKeysResponseTypeDef:
        """
        Returns all tag keys in the specified region for the AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetTagKeys>`_

        **Request Syntax**
        ::

          response = client.get_tag_keys(
              PaginationToken='string'
          )
        :type PaginationToken: string
        :param PaginationToken:

          A string that indicates that additional data is available. Leave this value empty for your
          initial request. If the response includes a PaginationToken, use that string for this value to
          request an additional page of data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PaginationToken': 'string',
                'TagKeys': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PaginationToken** *(string) --*

              A string that indicates that the response contains more data than can be returned in a single
              response. To receive additional data, specify this string for the ``PaginationToken`` value
              in a subsequent request.

            - **TagKeys** *(list) --*

              A list of all tag keys in the AWS account.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tag_values(
        self, Key: str, PaginationToken: str = None
    ) -> ClientGetTagValuesResponseTypeDef:
        """
        Returns all tag values for the specified key in the specified region for the AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetTagValues>`_

        **Request Syntax**
        ::

          response = client.get_tag_values(
              PaginationToken='string',
              Key='string'
          )
        :type PaginationToken: string
        :param PaginationToken:

          A string that indicates that additional data is available. Leave this value empty for your
          initial request. If the response includes a PaginationToken, use that string for this value to
          request an additional page of data.

        :type Key: string
        :param Key: **[REQUIRED]**

          The key for which you want to list all existing values in the specified region for the AWS
          account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PaginationToken': 'string',
                'TagValues': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PaginationToken** *(string) --*

              A string that indicates that the response contains more data than can be returned in a single
              response. To receive additional data, specify this string for the ``PaginationToken`` value
              in a subsequent request.

            - **TagValues** *(list) --*

              A list of all tag values for the specified key in the AWS account.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resources(
        self, ResourceARNList: List[str], Tags: List[str]
    ) -> ClientTagResourcesResponseTypeDef:
        """
        Applies one or more tags to the specified resources. Note the following:

        * Not all resources can have tags. For a list of resources that support tagging, see `Supported
        Resources <http://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html>`__ in the *AWS
        Resource Groups User Guide* .

        * Each resource can have up to 50 tags. For other limits, see `Tag Restrictions
        <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions>`__ in the
        *Amazon EC2 User Guide for Linux Instances* .

        * You can only tag resources that are located in the specified region for the AWS account.

        * To add tags to a resource, you need the necessary permissions for the service that the resource
        belongs to as well as permissions for adding tags. For more information, see `Obtaining Permissions
        for Tagging
        <http://docs.aws.amazon.com/ARG/latest/userguide/obtaining-permissions-for-tagging.html>`__ in the
        *AWS Resource Groups User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/TagResources>`_

        **Request Syntax**
        ::

          response = client.tag_resources(
              ResourceARNList=[
                  'string',
              ],
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceARNList: list
        :param ResourceARNList: **[REQUIRED]**

          A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. You can specify a
          minimum of 1 and a maximum of 20 ARNs (resources) to tag. An ARN can be set to a maximum of 1600
          characters. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS
          General Reference* .

          - *(string) --*

        :type Tags: dict
        :param Tags: **[REQUIRED]**

          The tags that you want to add to the specified resources. A tag consists of a key and a value
          that you define.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FailedResourcesMap': {
                    'string': {
                        'StatusCode': 123,
                        'ErrorCode': 'InternalServiceException'|'InvalidParameterException',
                        'ErrorMessage': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **FailedResourcesMap** *(dict) --*

              Details of resources that could not be tagged. An error code, status code, and error message
              are returned for each failed item.

              - *(string) --*

                - *(dict) --*

                  Details of the common errors that all actions return.

                  - **StatusCode** *(integer) --*

                    The HTTP status code of the common error.

                  - **ErrorCode** *(string) --*

                    The code of the common error. Valid values include ``InternalServiceException`` ,
                    ``InvalidParameterException`` , and any valid error code returned by the AWS service
                    that hosts the resource that you want to tag.

                  - **ErrorMessage** *(string) --*

                    The message of the common error.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resources(
        self, ResourceARNList: List[str], TagKeys: List[str]
    ) -> ClientUntagResourcesResponseTypeDef:
        """
        Removes the specified tags from the specified resources. When you specify a tag key, the action
        removes both that key and its associated value. The operation succeeds even if you attempt to
        remove tags from a resource that were already removed. Note the following:

        * To remove tags from a resource, you need the necessary permissions for the service that the
        resource belongs to as well as permissions for removing tags. For more information, see `Obtaining
        Permissions for Tagging
        <http://docs.aws.amazon.com/ARG/latest/userguide/obtaining-permissions-for-tagging.html>`__ in the
        *AWS Resource Groups User Guide* .

        * You can only tag resources that are located in the specified region for the AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/UntagResources>`_

        **Request Syntax**
        ::

          response = client.untag_resources(
              ResourceARNList=[
                  'string',
              ],
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceARNList: list
        :param ResourceARNList: **[REQUIRED]**

          A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. You can specify a
          minimum of 1 and a maximum of 20 ARNs (resources) to untag. An ARN can be set to a maximum of
          1600 characters. For more information, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

          - *(string) --*

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          A list of the tag keys that you want to remove from the specified resources.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FailedResourcesMap': {
                    'string': {
                        'StatusCode': 123,
                        'ErrorCode': 'InternalServiceException'|'InvalidParameterException',
                        'ErrorMessage': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **FailedResourcesMap** *(dict) --*

              Details of resources that could not be untagged. An error code, status code, and error
              message are returned for each failed item.

              - *(string) --*

                - *(dict) --*

                  Details of the common errors that all actions return.

                  - **StatusCode** *(integer) --*

                    The HTTP status code of the common error.

                  - **ErrorCode** *(string) --*

                    The code of the common error. Valid values include ``InternalServiceException`` ,
                    ``InvalidParameterException`` , and any valid error code returned by the AWS service
                    that hosts the resource that you want to tag.

                  - **ErrorMessage** *(string) --*

                    The message of the common error.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_resources"]
    ) -> paginator_scope.GetResourcesPaginator:
        """
        Get Paginator for `get_resources` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_tag_keys"]
    ) -> paginator_scope.GetTagKeysPaginator:
        """
        Get Paginator for `get_tag_keys` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_tag_values"]
    ) -> paginator_scope.GetTagValuesPaginator:
        """
        Get Paginator for `get_tag_values` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    PaginationTokenExpiredException: Boto3ClientError
    ThrottledException: Boto3ClientError
