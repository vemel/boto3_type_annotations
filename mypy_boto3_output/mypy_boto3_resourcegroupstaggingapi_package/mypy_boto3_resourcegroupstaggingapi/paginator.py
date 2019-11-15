"Main interface for resourcegroupstaggingapi Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    GetResourcesPaginatePaginationConfigTypeDef,
    GetResourcesPaginateResponseTypeDef,
    GetResourcesPaginateTagFiltersTypeDef,
    GetTagKeysPaginatePaginationConfigTypeDef,
    GetTagKeysPaginateResponseTypeDef,
    GetTagValuesPaginatePaginationConfigTypeDef,
    GetTagValuesPaginateResponseTypeDef,
)


class GetResources(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        TagFilters: List[GetResourcesPaginateTagFiltersTypeDef] = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        PaginationConfig: GetResourcesPaginatePaginationConfigTypeDef = None,
    ) -> GetResourcesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ResourceGroupsTaggingAPI.Client.get_resources`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetResources>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              TagFilters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              TagsPerPage=123,
              ResourceTypeFilters=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
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
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class GetTagKeys(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self, PaginationConfig: GetTagKeysPaginatePaginationConfigTypeDef = None
    ) -> GetTagKeysPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ResourceGroupsTaggingAPI.Client.get_tag_keys`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetTagKeys>`_

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
                'TagKeys': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TagKeys** *(list) --*

              A list of all tag keys in the AWS account.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class GetTagValues(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        Key: str,
        PaginationConfig: GetTagValuesPaginatePaginationConfigTypeDef = None,
    ) -> GetTagValuesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ResourceGroupsTaggingAPI.Client.get_tag_values`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetTagValues>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Key='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type Key: string
        :param Key: **[REQUIRED]**

          The key for which you want to list all existing values in the specified region for the AWS
          account.

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
                'TagValues': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TagValues** *(list) --*

              A list of all tag values for the specified key in the AWS account.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
