"Main interface for resource-groups type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateGroupResourceQueryTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseResourceQueryTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientDeleteGroupResponseGroupTypeDef",
    "ClientDeleteGroupResponseTypeDef",
    "ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef",
    "ClientGetGroupQueryResponseGroupQueryTypeDef",
    "ClientGetGroupQueryResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientListGroupResourcesFiltersTypeDef",
    "ClientListGroupResourcesResponseQueryErrorsTypeDef",
    "ClientListGroupResourcesResponseResourceIdentifiersTypeDef",
    "ClientListGroupResourcesResponseTypeDef",
    "ClientListGroupsFiltersTypeDef",
    "ClientListGroupsResponseGroupIdentifiersTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientSearchResourcesResourceQueryTypeDef",
    "ClientSearchResourcesResponseQueryErrorsTypeDef",
    "ClientSearchResourcesResponseResourceIdentifiersTypeDef",
    "ClientSearchResourcesResponseTypeDef",
    "ClientTagResponseTypeDef",
    "ClientUntagResponseTypeDef",
    "ClientUpdateGroupQueryResourceQueryTypeDef",
    "ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef",
    "ClientUpdateGroupQueryResponseGroupQueryTypeDef",
    "ClientUpdateGroupQueryResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ListGroupResourcesPaginateFiltersTypeDef",
    "ListGroupResourcesPaginatePaginationConfigTypeDef",
    "ListGroupResourcesPaginateResponseQueryErrorsTypeDef",
    "ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef",
    "ListGroupResourcesPaginateResponseTypeDef",
    "ListGroupsPaginateFiltersTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupIdentifiersTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "SearchResourcesPaginatePaginationConfigTypeDef",
    "SearchResourcesPaginateResourceQueryTypeDef",
    "SearchResourcesPaginateResponseQueryErrorsTypeDef",
    "SearchResourcesPaginateResponseResourceIdentifiersTypeDef",
    "SearchResourcesPaginateResponseTypeDef",
)


_ClientCreateGroupResourceQueryTypeDef = TypedDict(
    "_ClientCreateGroupResourceQueryTypeDef", {"Type": str, "Query": str}
)


class ClientCreateGroupResourceQueryTypeDef(_ClientCreateGroupResourceQueryTypeDef):
    """
    Type definition for `ClientCreateGroup` `ResourceQuery`

    The resource query that determines which AWS resources are members of this group.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

       * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
       filters for resource types and tags, as supported by the AWS Tagging API `GetResources
       <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
       operation. If you specify more than one tag key, only resources that match all tag keys, and
       at least one value of each specified tag key, are returned in your query. If you specify more
       than one value for a tag key, a resource matches the filter if it has a tag key value that
       matches *any* of the specified values.

      For example, consider the following sample query for resources that have two tags, ``Stage``
      and ``Version`` , with two values each.
      (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` ) The
      results of this query might include the following.

      * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` , and
      ``{"Key":"Version","Value":"2"}``

      * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
      {"Key":"Version","Value":"1"}

      The query would not return the following results, however. The following EC2 instance does not
      have all tag keys specified in the filter, so it is rejected. The RDS database has all of the
      tag keys, but no values that match at least one of the specified tag key values in the filter.

      * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

      * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}`` , and
      ``{"Key":"Version","Value":"4"}``

       * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation stack
       ARN.

    - **Query** *(string) --* **[REQUIRED]**

      The query that defines a group or a search.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientCreateGroupResponse` `Group`

    A full description of the resource group after it is created.

    - **GroupArn** *(string) --*

      The ARN of a resource group.

    - **Name** *(string) --*

      The name of a resource group.

    - **Description** *(string) --*

      The description of the resource group.
    """


_ClientCreateGroupResponseResourceQueryTypeDef = TypedDict(
    "_ClientCreateGroupResponseResourceQueryTypeDef",
    {"Type": str, "Query": str},
    total=False,
)


class ClientCreateGroupResponseResourceQueryTypeDef(
    _ClientCreateGroupResponseResourceQueryTypeDef
):
    """
    Type definition for `ClientCreateGroupResponse` `ResourceQuery`

    The resource query associated with the group.

    - **Type** *(string) --*

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

       * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
       filters for resource types and tags, as supported by the AWS Tagging API `GetResources
       <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
       operation. If you specify more than one tag key, only resources that match all tag keys,
       and at least one value of each specified tag key, are returned in your query. If you
       specify more than one value for a tag key, a resource matches the filter if it has a tag
       key value that matches *any* of the specified values.

      For example, consider the following sample query for resources that have two tags,
      ``Stage`` and ``Version`` , with two values each.
      (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` )
      The results of this query might include the following.

      * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` ,
      and ``{"Key":"Version","Value":"2"}``

      * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
      {"Key":"Version","Value":"1"}

      The query would not return the following results, however. The following EC2 instance does
      not have all tag keys specified in the filter, so it is rejected. The RDS database has all
      of the tag keys, but no values that match at least one of the specified tag key values in
      the filter.

      * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

      * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}`` ,
      and ``{"Key":"Version","Value":"4"}``

       * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation
       stack ARN.

    - **Query** *(string) --*

      The query that defines a group or a search.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {
        "Group": ClientCreateGroupResponseGroupTypeDef,
        "ResourceQuery": ClientCreateGroupResponseResourceQueryTypeDef,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    Type definition for `ClientCreateGroup` `Response`

    - **Group** *(dict) --*

      A full description of the resource group after it is created.

      - **GroupArn** *(string) --*

        The ARN of a resource group.

      - **Name** *(string) --*

        The name of a resource group.

      - **Description** *(string) --*

        The description of the resource group.

    - **ResourceQuery** *(dict) --*

      The resource query associated with the group.

      - **Type** *(string) --*

        The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
        ``CLOUDFORMATION_STACK_1_0`` .

         * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
         filters for resource types and tags, as supported by the AWS Tagging API `GetResources
         <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
         operation. If you specify more than one tag key, only resources that match all tag keys,
         and at least one value of each specified tag key, are returned in your query. If you
         specify more than one value for a tag key, a resource matches the filter if it has a tag
         key value that matches *any* of the specified values.

        For example, consider the following sample query for resources that have two tags,
        ``Stage`` and ``Version`` , with two values each.
        (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` )
        The results of this query might include the following.

        * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` ,
        and ``{"Key":"Version","Value":"2"}``

        * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
        {"Key":"Version","Value":"1"}

        The query would not return the following results, however. The following EC2 instance does
        not have all tag keys specified in the filter, so it is rejected. The RDS database has all
        of the tag keys, but no values that match at least one of the specified tag key values in
        the filter.

        * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

        * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}`` ,
        and ``{"Key":"Version","Value":"4"}``

         * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation
         stack ARN.

      - **Query** *(string) --*

        The query that defines a group or a search.

    - **Tags** *(dict) --*

      The tags associated with the group.

      - *(string) --*

        - *(string) --*
    """


_ClientDeleteGroupResponseGroupTypeDef = TypedDict(
    "_ClientDeleteGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientDeleteGroupResponseGroupTypeDef(_ClientDeleteGroupResponseGroupTypeDef):
    """
    Type definition for `ClientDeleteGroupResponse` `Group`

    A full description of the deleted resource group.

    - **GroupArn** *(string) --*

      The ARN of a resource group.

    - **Name** *(string) --*

      The name of a resource group.

    - **Description** *(string) --*

      The description of the resource group.
    """


_ClientDeleteGroupResponseTypeDef = TypedDict(
    "_ClientDeleteGroupResponseTypeDef",
    {"Group": ClientDeleteGroupResponseGroupTypeDef},
    total=False,
)


class ClientDeleteGroupResponseTypeDef(_ClientDeleteGroupResponseTypeDef):
    """
    Type definition for `ClientDeleteGroup` `Response`

    - **Group** *(dict) --*

      A full description of the deleted resource group.

      - **GroupArn** *(string) --*

        The ARN of a resource group.

      - **Name** *(string) --*

        The name of a resource group.

      - **Description** *(string) --*

        The description of the resource group.
    """


_ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef = TypedDict(
    "_ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef",
    {"Type": str, "Query": str},
    total=False,
)


class ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef(
    _ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef
):
    """
    Type definition for `ClientGetGroupQueryResponseGroupQuery` `ResourceQuery`

    The resource query which determines which AWS resources are members of the associated
    resource group.

    - **Type** *(string) --*

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

       * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
       filters for resource types and tags, as supported by the AWS Tagging API `GetResources
       <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
       operation. If you specify more than one tag key, only resources that match all tag keys,
       and at least one value of each specified tag key, are returned in your query. If you
       specify more than one value for a tag key, a resource matches the filter if it has a tag
       key value that matches *any* of the specified values.

      For example, consider the following sample query for resources that have two tags,
      ``Stage`` and ``Version`` , with two values each.
      (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` )
      The results of this query might include the following.

      * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` ,
      and ``{"Key":"Version","Value":"2"}``

      * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
      {"Key":"Version","Value":"1"}

      The query would not return the following results, however. The following EC2 instance
      does not have all tag keys specified in the filter, so it is rejected. The RDS database
      has all of the tag keys, but no values that match at least one of the specified tag key
      values in the filter.

      * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

      * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}``
      , and ``{"Key":"Version","Value":"4"}``

       * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation
       stack ARN.

    - **Query** *(string) --*

      The query that defines a group or a search.
    """


_ClientGetGroupQueryResponseGroupQueryTypeDef = TypedDict(
    "_ClientGetGroupQueryResponseGroupQueryTypeDef",
    {
        "GroupName": str,
        "ResourceQuery": ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef,
    },
    total=False,
)


class ClientGetGroupQueryResponseGroupQueryTypeDef(
    _ClientGetGroupQueryResponseGroupQueryTypeDef
):
    """
    Type definition for `ClientGetGroupQueryResponse` `GroupQuery`

    The resource query associated with the specified group.

    - **GroupName** *(string) --*

      The name of a resource group that is associated with a specific resource query.

    - **ResourceQuery** *(dict) --*

      The resource query which determines which AWS resources are members of the associated
      resource group.

      - **Type** *(string) --*

        The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
        ``CLOUDFORMATION_STACK_1_0`` .

         * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
         filters for resource types and tags, as supported by the AWS Tagging API `GetResources
         <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
         operation. If you specify more than one tag key, only resources that match all tag keys,
         and at least one value of each specified tag key, are returned in your query. If you
         specify more than one value for a tag key, a resource matches the filter if it has a tag
         key value that matches *any* of the specified values.

        For example, consider the following sample query for resources that have two tags,
        ``Stage`` and ``Version`` , with two values each.
        (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` )
        The results of this query might include the following.

        * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` ,
        and ``{"Key":"Version","Value":"2"}``

        * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
        {"Key":"Version","Value":"1"}

        The query would not return the following results, however. The following EC2 instance
        does not have all tag keys specified in the filter, so it is rejected. The RDS database
        has all of the tag keys, but no values that match at least one of the specified tag key
        values in the filter.

        * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

        * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}``
        , and ``{"Key":"Version","Value":"4"}``

         * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation
         stack ARN.

      - **Query** *(string) --*

        The query that defines a group or a search.
    """


_ClientGetGroupQueryResponseTypeDef = TypedDict(
    "_ClientGetGroupQueryResponseTypeDef",
    {"GroupQuery": ClientGetGroupQueryResponseGroupQueryTypeDef},
    total=False,
)


class ClientGetGroupQueryResponseTypeDef(_ClientGetGroupQueryResponseTypeDef):
    """
    Type definition for `ClientGetGroupQuery` `Response`

    - **GroupQuery** *(dict) --*

      The resource query associated with the specified group.

      - **GroupName** *(string) --*

        The name of a resource group that is associated with a specific resource query.

      - **ResourceQuery** *(dict) --*

        The resource query which determines which AWS resources are members of the associated
        resource group.

        - **Type** *(string) --*

          The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
          ``CLOUDFORMATION_STACK_1_0`` .

           * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
           filters for resource types and tags, as supported by the AWS Tagging API `GetResources
           <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
           operation. If you specify more than one tag key, only resources that match all tag keys,
           and at least one value of each specified tag key, are returned in your query. If you
           specify more than one value for a tag key, a resource matches the filter if it has a tag
           key value that matches *any* of the specified values.

          For example, consider the following sample query for resources that have two tags,
          ``Stage`` and ``Version`` , with two values each.
          (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` )
          The results of this query might include the following.

          * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` ,
          and ``{"Key":"Version","Value":"2"}``

          * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
          {"Key":"Version","Value":"1"}

          The query would not return the following results, however. The following EC2 instance
          does not have all tag keys specified in the filter, so it is rejected. The RDS database
          has all of the tag keys, but no values that match at least one of the specified tag key
          values in the filter.

          * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

          * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}``
          , and ``{"Key":"Version","Value":"4"}``

           * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation
           stack ARN.

        - **Query** *(string) --*

          The query that defines a group or a search.
    """


_ClientGetGroupResponseGroupTypeDef = TypedDict(
    "_ClientGetGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientGetGroupResponseGroupTypeDef(_ClientGetGroupResponseGroupTypeDef):
    """
    Type definition for `ClientGetGroupResponse` `Group`

    A full description of the resource group.

    - **GroupArn** *(string) --*

      The ARN of a resource group.

    - **Name** *(string) --*

      The name of a resource group.

    - **Description** *(string) --*

      The description of the resource group.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef",
    {"Group": ClientGetGroupResponseGroupTypeDef},
    total=False,
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    Type definition for `ClientGetGroup` `Response`

    - **Group** *(dict) --*

      A full description of the resource group.

      - **GroupArn** *(string) --*

        The ARN of a resource group.

      - **Name** *(string) --*

        The name of a resource group.

      - **Description** *(string) --*

        The description of the resource group.
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    Type definition for `ClientGetTags` `Response`

    - **Arn** *(string) --*

      The ARN of the tagged resource group.

    - **Tags** *(dict) --*

      The tags associated with the specified resource group.

      - *(string) --*

        - *(string) --*
    """


_ClientListGroupResourcesFiltersTypeDef = TypedDict(
    "_ClientListGroupResourcesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientListGroupResourcesFiltersTypeDef(_ClientListGroupResourcesFiltersTypeDef):
    """
    Type definition for `ClientListGroupResources` `Filters`

    A filter name and value pair that is used to obtain more specific results from a list of
    resources.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case-sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Allowed filter values vary by resource filter name, and are
      case-sensitive.

      - *(string) --*
    """


_ClientListGroupResourcesResponseQueryErrorsTypeDef = TypedDict(
    "_ClientListGroupResourcesResponseQueryErrorsTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientListGroupResourcesResponseQueryErrorsTypeDef(
    _ClientListGroupResourcesResponseQueryErrorsTypeDef
):
    """
    Type definition for `ClientListGroupResourcesResponse` `QueryErrors`

    A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources``
    operations on CloudFormation stack-based queries. The error occurs if the CloudFormation
    stack on which the query is based either does not exist, or has a status that renders the
    stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource
    Groups could not complete the operation, but the resulting group might have no member
    resources.

    - **ErrorCode** *(string) --*

      Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and
      ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

    - **Message** *(string) --*

      A message that explains the ``ErrorCode`` value. Messages might state that the specified
      CloudFormation stack does not exist (or no longer exists). For
      ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation
      stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
    """


_ClientListGroupResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "_ClientListGroupResourcesResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)


class ClientListGroupResourcesResponseResourceIdentifiersTypeDef(
    _ClientListGroupResourcesResponseResourceIdentifiersTypeDef
):
    """
    Type definition for `ClientListGroupResourcesResponse` `ResourceIdentifiers`

    The ARN of a resource, and its resource type.

    - **ResourceArn** *(string) --*

      The ARN of a resource.

    - **ResourceType** *(string) --*

      The resource type of a resource, such as ``AWS::EC2::Instance`` .
    """


_ClientListGroupResourcesResponseTypeDef = TypedDict(
    "_ClientListGroupResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ClientListGroupResourcesResponseResourceIdentifiersTypeDef
        ],
        "NextToken": str,
        "QueryErrors": List[ClientListGroupResourcesResponseQueryErrorsTypeDef],
    },
    total=False,
)


class ClientListGroupResourcesResponseTypeDef(_ClientListGroupResourcesResponseTypeDef):
    """
    Type definition for `ClientListGroupResources` `Response`

    - **ResourceIdentifiers** *(list) --*

      The ARNs and resource types of resources that are members of the group that you specified.

      - *(dict) --*

        The ARN of a resource, and its resource type.

        - **ResourceArn** *(string) --*

          The ARN of a resource.

        - **ResourceType** *(string) --*

          The resource type of a resource, such as ``AWS::EC2::Instance`` .

    - **NextToken** *(string) --*

      The NextToken value to include in a subsequent ``ListGroupResources`` request, to get more
      results.

    - **QueryErrors** *(list) --*

      A list of ``QueryError`` objects. Each error is an object that contains ``ErrorCode`` and
      ``Message`` structures. Possible values for ``ErrorCode`` are
      ``CLOUDFORMATION_STACK_INACTIVE`` and ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

      - *(dict) --*

        A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources``
        operations on CloudFormation stack-based queries. The error occurs if the CloudFormation
        stack on which the query is based either does not exist, or has a status that renders the
        stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource
        Groups could not complete the operation, but the resulting group might have no member
        resources.

        - **ErrorCode** *(string) --*

          Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and
          ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

        - **Message** *(string) --*

          A message that explains the ``ErrorCode`` value. Messages might state that the specified
          CloudFormation stack does not exist (or no longer exists). For
          ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation
          stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
    """


_ClientListGroupsFiltersTypeDef = TypedDict(
    "_ClientListGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientListGroupsFiltersTypeDef(_ClientListGroupsFiltersTypeDef):
    """
    Type definition for `ClientListGroups` `Filters`

    A filter name and value pair that is used to obtain more specific results from a list of groups.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case-sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Allowed filter values vary by group filter name, and are
      case-sensitive.

      - *(string) --*
    """


_ClientListGroupsResponseGroupIdentifiersTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupIdentifiersTypeDef",
    {"GroupName": str, "GroupArn": str},
    total=False,
)


class ClientListGroupsResponseGroupIdentifiersTypeDef(
    _ClientListGroupsResponseGroupIdentifiersTypeDef
):
    """
    Type definition for `ClientListGroupsResponse` `GroupIdentifiers`

    The ARN and group name of a group.

    - **GroupName** *(string) --*

      The name of a resource group.

    - **GroupArn** *(string) --*

      The ARN of a resource group.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    Type definition for `ClientListGroupsResponse` `Groups`

    A resource group.

    - **GroupArn** *(string) --*

      The ARN of a resource group.

    - **Name** *(string) --*

      The name of a resource group.

    - **Description** *(string) --*

      The description of the resource group.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {
        "GroupIdentifiers": List[ClientListGroupsResponseGroupIdentifiersTypeDef],
        "Groups": List[ClientListGroupsResponseGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    Type definition for `ClientListGroups` `Response`

    - **GroupIdentifiers** *(list) --*

      A list of GroupIdentifier objects. Each identifier is an object that contains both the
      GroupName and the GroupArn.

      - *(dict) --*

        The ARN and group name of a group.

        - **GroupName** *(string) --*

          The name of a resource group.

        - **GroupArn** *(string) --*

          The ARN of a resource group.

    - **Groups** *(list) --*

      A list of resource groups.

      - *(dict) --*

        A resource group.

        - **GroupArn** *(string) --*

          The ARN of a resource group.

        - **Name** *(string) --*

          The name of a resource group.

        - **Description** *(string) --*

          The description of the resource group.

    - **NextToken** *(string) --*

      The NextToken value to include in a subsequent ``ListGroups`` request, to get more results.
    """


_ClientSearchResourcesResourceQueryTypeDef = TypedDict(
    "_ClientSearchResourcesResourceQueryTypeDef", {"Type": str, "Query": str}
)


class ClientSearchResourcesResourceQueryTypeDef(
    _ClientSearchResourcesResourceQueryTypeDef
):
    """
    Type definition for `ClientSearchResources` `ResourceQuery`

    The search query, using the same formats that are supported for resource group definition.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

       * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
       filters for resource types and tags, as supported by the AWS Tagging API `GetResources
       <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
       operation. If you specify more than one tag key, only resources that match all tag keys, and
       at least one value of each specified tag key, are returned in your query. If you specify more
       than one value for a tag key, a resource matches the filter if it has a tag key value that
       matches *any* of the specified values.

      For example, consider the following sample query for resources that have two tags, ``Stage``
      and ``Version`` , with two values each.
      (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` ) The
      results of this query might include the following.

      * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` , and
      ``{"Key":"Version","Value":"2"}``

      * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
      {"Key":"Version","Value":"1"}

      The query would not return the following results, however. The following EC2 instance does not
      have all tag keys specified in the filter, so it is rejected. The RDS database has all of the
      tag keys, but no values that match at least one of the specified tag key values in the filter.

      * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

      * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}`` , and
      ``{"Key":"Version","Value":"4"}``

       * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation stack
       ARN.

    - **Query** *(string) --* **[REQUIRED]**

      The query that defines a group or a search.
    """


_ClientSearchResourcesResponseQueryErrorsTypeDef = TypedDict(
    "_ClientSearchResourcesResponseQueryErrorsTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientSearchResourcesResponseQueryErrorsTypeDef(
    _ClientSearchResourcesResponseQueryErrorsTypeDef
):
    """
    Type definition for `ClientSearchResourcesResponse` `QueryErrors`

    A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources``
    operations on CloudFormation stack-based queries. The error occurs if the CloudFormation
    stack on which the query is based either does not exist, or has a status that renders the
    stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource
    Groups could not complete the operation, but the resulting group might have no member
    resources.

    - **ErrorCode** *(string) --*

      Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and
      ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

    - **Message** *(string) --*

      A message that explains the ``ErrorCode`` value. Messages might state that the specified
      CloudFormation stack does not exist (or no longer exists). For
      ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation
      stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
    """


_ClientSearchResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "_ClientSearchResourcesResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)


class ClientSearchResourcesResponseResourceIdentifiersTypeDef(
    _ClientSearchResourcesResponseResourceIdentifiersTypeDef
):
    """
    Type definition for `ClientSearchResourcesResponse` `ResourceIdentifiers`

    The ARN of a resource, and its resource type.

    - **ResourceArn** *(string) --*

      The ARN of a resource.

    - **ResourceType** *(string) --*

      The resource type of a resource, such as ``AWS::EC2::Instance`` .
    """


_ClientSearchResourcesResponseTypeDef = TypedDict(
    "_ClientSearchResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ClientSearchResourcesResponseResourceIdentifiersTypeDef
        ],
        "NextToken": str,
        "QueryErrors": List[ClientSearchResourcesResponseQueryErrorsTypeDef],
    },
    total=False,
)


class ClientSearchResourcesResponseTypeDef(_ClientSearchResourcesResponseTypeDef):
    """
    Type definition for `ClientSearchResources` `Response`

    - **ResourceIdentifiers** *(list) --*

      The ARNs and resource types of resources that are members of the group that you specified.

      - *(dict) --*

        The ARN of a resource, and its resource type.

        - **ResourceArn** *(string) --*

          The ARN of a resource.

        - **ResourceType** *(string) --*

          The resource type of a resource, such as ``AWS::EC2::Instance`` .

    - **NextToken** *(string) --*

      The NextToken value to include in a subsequent ``SearchResources`` request, to get more
      results.

    - **QueryErrors** *(list) --*

      A list of ``QueryError`` objects. Each error is an object that contains ``ErrorCode`` and
      ``Message`` structures. Possible values for ``ErrorCode`` are
      ``CLOUDFORMATION_STACK_INACTIVE`` and ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

      - *(dict) --*

        A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources``
        operations on CloudFormation stack-based queries. The error occurs if the CloudFormation
        stack on which the query is based either does not exist, or has a status that renders the
        stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource
        Groups could not complete the operation, but the resulting group might have no member
        resources.

        - **ErrorCode** *(string) --*

          Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and
          ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

        - **Message** *(string) --*

          A message that explains the ``ErrorCode`` value. Messages might state that the specified
          CloudFormation stack does not exist (or no longer exists). For
          ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation
          stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
    """


_ClientTagResponseTypeDef = TypedDict(
    "_ClientTagResponseTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
)


class ClientTagResponseTypeDef(_ClientTagResponseTypeDef):
    """
    Type definition for `ClientTag` `Response`

    - **Arn** *(string) --*

      The ARN of the tagged resource.

    - **Tags** *(dict) --*

      The tags that have been added to the specified resource.

      - *(string) --*

        - *(string) --*
    """


_ClientUntagResponseTypeDef = TypedDict(
    "_ClientUntagResponseTypeDef", {"Arn": str, "Keys": List[str]}, total=False
)


class ClientUntagResponseTypeDef(_ClientUntagResponseTypeDef):
    """
    Type definition for `ClientUntag` `Response`

    - **Arn** *(string) --*

      The ARN of the resource from which tags have been removed.

    - **Keys** *(list) --*

      The keys of tags that have been removed.

      - *(string) --*
    """


_ClientUpdateGroupQueryResourceQueryTypeDef = TypedDict(
    "_ClientUpdateGroupQueryResourceQueryTypeDef", {"Type": str, "Query": str}
)


class ClientUpdateGroupQueryResourceQueryTypeDef(
    _ClientUpdateGroupQueryResourceQueryTypeDef
):
    """
    Type definition for `ClientUpdateGroupQuery` `ResourceQuery`

    The resource query that determines which AWS resources are members of the resource group.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

       * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
       filters for resource types and tags, as supported by the AWS Tagging API `GetResources
       <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
       operation. If you specify more than one tag key, only resources that match all tag keys, and
       at least one value of each specified tag key, are returned in your query. If you specify more
       than one value for a tag key, a resource matches the filter if it has a tag key value that
       matches *any* of the specified values.

      For example, consider the following sample query for resources that have two tags, ``Stage``
      and ``Version`` , with two values each.
      (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` ) The
      results of this query might include the following.

      * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` , and
      ``{"Key":"Version","Value":"2"}``

      * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
      {"Key":"Version","Value":"1"}

      The query would not return the following results, however. The following EC2 instance does not
      have all tag keys specified in the filter, so it is rejected. The RDS database has all of the
      tag keys, but no values that match at least one of the specified tag key values in the filter.

      * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

      * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}`` , and
      ``{"Key":"Version","Value":"4"}``

       * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation stack
       ARN.

    - **Query** *(string) --* **[REQUIRED]**

      The query that defines a group or a search.
    """


_ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef = TypedDict(
    "_ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef",
    {"Type": str, "Query": str},
    total=False,
)


class ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef(
    _ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef
):
    """
    Type definition for `ClientUpdateGroupQueryResponseGroupQuery` `ResourceQuery`

    The resource query which determines which AWS resources are members of the associated
    resource group.

    - **Type** *(string) --*

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

       * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
       filters for resource types and tags, as supported by the AWS Tagging API `GetResources
       <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
       operation. If you specify more than one tag key, only resources that match all tag keys,
       and at least one value of each specified tag key, are returned in your query. If you
       specify more than one value for a tag key, a resource matches the filter if it has a tag
       key value that matches *any* of the specified values.

      For example, consider the following sample query for resources that have two tags,
      ``Stage`` and ``Version`` , with two values each.
      (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` )
      The results of this query might include the following.

      * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` ,
      and ``{"Key":"Version","Value":"2"}``

      * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
      {"Key":"Version","Value":"1"}

      The query would not return the following results, however. The following EC2 instance
      does not have all tag keys specified in the filter, so it is rejected. The RDS database
      has all of the tag keys, but no values that match at least one of the specified tag key
      values in the filter.

      * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

      * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}``
      , and ``{"Key":"Version","Value":"4"}``

       * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation
       stack ARN.

    - **Query** *(string) --*

      The query that defines a group or a search.
    """


_ClientUpdateGroupQueryResponseGroupQueryTypeDef = TypedDict(
    "_ClientUpdateGroupQueryResponseGroupQueryTypeDef",
    {
        "GroupName": str,
        "ResourceQuery": ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef,
    },
    total=False,
)


class ClientUpdateGroupQueryResponseGroupQueryTypeDef(
    _ClientUpdateGroupQueryResponseGroupQueryTypeDef
):
    """
    Type definition for `ClientUpdateGroupQueryResponse` `GroupQuery`

    The resource query associated with the resource group after the update.

    - **GroupName** *(string) --*

      The name of a resource group that is associated with a specific resource query.

    - **ResourceQuery** *(dict) --*

      The resource query which determines which AWS resources are members of the associated
      resource group.

      - **Type** *(string) --*

        The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
        ``CLOUDFORMATION_STACK_1_0`` .

         * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
         filters for resource types and tags, as supported by the AWS Tagging API `GetResources
         <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
         operation. If you specify more than one tag key, only resources that match all tag keys,
         and at least one value of each specified tag key, are returned in your query. If you
         specify more than one value for a tag key, a resource matches the filter if it has a tag
         key value that matches *any* of the specified values.

        For example, consider the following sample query for resources that have two tags,
        ``Stage`` and ``Version`` , with two values each.
        (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` )
        The results of this query might include the following.

        * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` ,
        and ``{"Key":"Version","Value":"2"}``

        * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
        {"Key":"Version","Value":"1"}

        The query would not return the following results, however. The following EC2 instance
        does not have all tag keys specified in the filter, so it is rejected. The RDS database
        has all of the tag keys, but no values that match at least one of the specified tag key
        values in the filter.

        * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

        * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}``
        , and ``{"Key":"Version","Value":"4"}``

         * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation
         stack ARN.

      - **Query** *(string) --*

        The query that defines a group or a search.
    """


_ClientUpdateGroupQueryResponseTypeDef = TypedDict(
    "_ClientUpdateGroupQueryResponseTypeDef",
    {"GroupQuery": ClientUpdateGroupQueryResponseGroupQueryTypeDef},
    total=False,
)


class ClientUpdateGroupQueryResponseTypeDef(_ClientUpdateGroupQueryResponseTypeDef):
    """
    Type definition for `ClientUpdateGroupQuery` `Response`

    - **GroupQuery** *(dict) --*

      The resource query associated with the resource group after the update.

      - **GroupName** *(string) --*

        The name of a resource group that is associated with a specific resource query.

      - **ResourceQuery** *(dict) --*

        The resource query which determines which AWS resources are members of the associated
        resource group.

        - **Type** *(string) --*

          The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
          ``CLOUDFORMATION_STACK_1_0`` .

           * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
           filters for resource types and tags, as supported by the AWS Tagging API `GetResources
           <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
           operation. If you specify more than one tag key, only resources that match all tag keys,
           and at least one value of each specified tag key, are returned in your query. If you
           specify more than one value for a tag key, a resource matches the filter if it has a tag
           key value that matches *any* of the specified values.

          For example, consider the following sample query for resources that have two tags,
          ``Stage`` and ``Version`` , with two values each.
          (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` )
          The results of this query might include the following.

          * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` ,
          and ``{"Key":"Version","Value":"2"}``

          * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
          {"Key":"Version","Value":"1"}

          The query would not return the following results, however. The following EC2 instance
          does not have all tag keys specified in the filter, so it is rejected. The RDS database
          has all of the tag keys, but no values that match at least one of the specified tag key
          values in the filter.

          * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

          * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}``
          , and ``{"Key":"Version","Value":"4"}``

           * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation
           stack ARN.

        - **Query** *(string) --*

          The query that defines a group or a search.
    """


_ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "_ClientUpdateGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientUpdateGroupResponseGroupTypeDef(_ClientUpdateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientUpdateGroupResponse` `Group`

    The full description of the resource group after it has been updated.

    - **GroupArn** *(string) --*

      The ARN of a resource group.

    - **Name** *(string) --*

      The name of a resource group.

    - **Description** *(string) --*

      The description of the resource group.
    """


_ClientUpdateGroupResponseTypeDef = TypedDict(
    "_ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)


class ClientUpdateGroupResponseTypeDef(_ClientUpdateGroupResponseTypeDef):
    """
    Type definition for `ClientUpdateGroup` `Response`

    - **Group** *(dict) --*

      The full description of the resource group after it has been updated.

      - **GroupArn** *(string) --*

        The ARN of a resource group.

      - **Name** *(string) --*

        The name of a resource group.

      - **Description** *(string) --*

        The description of the resource group.
    """


_ListGroupResourcesPaginateFiltersTypeDef = TypedDict(
    "_ListGroupResourcesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ListGroupResourcesPaginateFiltersTypeDef(
    _ListGroupResourcesPaginateFiltersTypeDef
):
    """
    Type definition for `ListGroupResourcesPaginate` `Filters`

    A filter name and value pair that is used to obtain more specific results from a list of
    resources.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case-sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Allowed filter values vary by resource filter name, and are
      case-sensitive.

      - *(string) --*
    """


_ListGroupResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupResourcesPaginatePaginationConfigTypeDef(
    _ListGroupResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupResourcesPaginate` `PaginationConfig`

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


_ListGroupResourcesPaginateResponseQueryErrorsTypeDef = TypedDict(
    "_ListGroupResourcesPaginateResponseQueryErrorsTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ListGroupResourcesPaginateResponseQueryErrorsTypeDef(
    _ListGroupResourcesPaginateResponseQueryErrorsTypeDef
):
    """
    Type definition for `ListGroupResourcesPaginateResponse` `QueryErrors`

    A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources``
    operations on CloudFormation stack-based queries. The error occurs if the CloudFormation
    stack on which the query is based either does not exist, or has a status that renders the
    stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource
    Groups could not complete the operation, but the resulting group might have no member
    resources.

    - **ErrorCode** *(string) --*

      Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and
      ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

    - **Message** *(string) --*

      A message that explains the ``ErrorCode`` value. Messages might state that the specified
      CloudFormation stack does not exist (or no longer exists). For
      ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation
      stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
    """


_ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef = TypedDict(
    "_ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)


class ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef(
    _ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef
):
    """
    Type definition for `ListGroupResourcesPaginateResponse` `ResourceIdentifiers`

    The ARN of a resource, and its resource type.

    - **ResourceArn** *(string) --*

      The ARN of a resource.

    - **ResourceType** *(string) --*

      The resource type of a resource, such as ``AWS::EC2::Instance`` .
    """


_ListGroupResourcesPaginateResponseTypeDef = TypedDict(
    "_ListGroupResourcesPaginateResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef
        ],
        "QueryErrors": List[ListGroupResourcesPaginateResponseQueryErrorsTypeDef],
    },
    total=False,
)


class ListGroupResourcesPaginateResponseTypeDef(
    _ListGroupResourcesPaginateResponseTypeDef
):
    """
    Type definition for `ListGroupResourcesPaginate` `Response`

    - **ResourceIdentifiers** *(list) --*

      The ARNs and resource types of resources that are members of the group that you specified.

      - *(dict) --*

        The ARN of a resource, and its resource type.

        - **ResourceArn** *(string) --*

          The ARN of a resource.

        - **ResourceType** *(string) --*

          The resource type of a resource, such as ``AWS::EC2::Instance`` .

    - **QueryErrors** *(list) --*

      A list of ``QueryError`` objects. Each error is an object that contains ``ErrorCode`` and
      ``Message`` structures. Possible values for ``ErrorCode`` are
      ``CLOUDFORMATION_STACK_INACTIVE`` and ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

      - *(dict) --*

        A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources``
        operations on CloudFormation stack-based queries. The error occurs if the CloudFormation
        stack on which the query is based either does not exist, or has a status that renders the
        stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource
        Groups could not complete the operation, but the resulting group might have no member
        resources.

        - **ErrorCode** *(string) --*

          Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and
          ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

        - **Message** *(string) --*

          A message that explains the ``ErrorCode`` value. Messages might state that the specified
          CloudFormation stack does not exist (or no longer exists). For
          ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation
          stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
    """


_ListGroupsPaginateFiltersTypeDef = TypedDict(
    "_ListGroupsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ListGroupsPaginateFiltersTypeDef(_ListGroupsPaginateFiltersTypeDef):
    """
    Type definition for `ListGroupsPaginate` `Filters`

    A filter name and value pair that is used to obtain more specific results from a list of groups.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case-sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Allowed filter values vary by group filter name, and are
      case-sensitive.

      - *(string) --*
    """


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(
    _ListGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupsPaginate` `PaginationConfig`

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


_ListGroupsPaginateResponseGroupIdentifiersTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupIdentifiersTypeDef",
    {"GroupName": str, "GroupArn": str},
    total=False,
)


class ListGroupsPaginateResponseGroupIdentifiersTypeDef(
    _ListGroupsPaginateResponseGroupIdentifiersTypeDef
):
    """
    Type definition for `ListGroupsPaginateResponse` `GroupIdentifiers`

    The ARN and group name of a group.

    - **GroupName** *(string) --*

      The name of a resource group.

    - **GroupArn** *(string) --*

      The ARN of a resource group.
    """


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    Type definition for `ListGroupsPaginateResponse` `Groups`

    A resource group.

    - **GroupArn** *(string) --*

      The ARN of a resource group.

    - **Name** *(string) --*

      The name of a resource group.

    - **Description** *(string) --*

      The description of the resource group.
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {
        "GroupIdentifiers": List[ListGroupsPaginateResponseGroupIdentifiersTypeDef],
        "Groups": List[ListGroupsPaginateResponseGroupsTypeDef],
    },
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    Type definition for `ListGroupsPaginate` `Response`

    - **GroupIdentifiers** *(list) --*

      A list of GroupIdentifier objects. Each identifier is an object that contains both the
      GroupName and the GroupArn.

      - *(dict) --*

        The ARN and group name of a group.

        - **GroupName** *(string) --*

          The name of a resource group.

        - **GroupArn** *(string) --*

          The ARN of a resource group.

    - **Groups** *(list) --*

      A list of resource groups.

      - *(dict) --*

        A resource group.

        - **GroupArn** *(string) --*

          The ARN of a resource group.

        - **Name** *(string) --*

          The name of a resource group.

        - **Description** *(string) --*

          The description of the resource group.
    """


_SearchResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchResourcesPaginatePaginationConfigTypeDef(
    _SearchResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchResourcesPaginate` `PaginationConfig`

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


_SearchResourcesPaginateResourceQueryTypeDef = TypedDict(
    "_SearchResourcesPaginateResourceQueryTypeDef", {"Type": str, "Query": str}
)


class SearchResourcesPaginateResourceQueryTypeDef(
    _SearchResourcesPaginateResourceQueryTypeDef
):
    """
    Type definition for `SearchResourcesPaginate` `ResourceQuery`

    The search query, using the same formats that are supported for resource group definition.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

       * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
       filters for resource types and tags, as supported by the AWS Tagging API `GetResources
       <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
       operation. If you specify more than one tag key, only resources that match all tag keys, and
       at least one value of each specified tag key, are returned in your query. If you specify more
       than one value for a tag key, a resource matches the filter if it has a tag key value that
       matches *any* of the specified values.

      For example, consider the following sample query for resources that have two tags, ``Stage``
      and ``Version`` , with two values each.
      (``[{"Key":"Stage","Values":["Test","Deploy"]},{"Key":"Version","Values":["1","2"]}]`` ) The
      results of this query might include the following.

      * An EC2 instance that has the following two tags: ``{"Key":"Stage","Value":"Deploy"}`` , and
      ``{"Key":"Version","Value":"2"}``

      * An S3 bucket that has the following two tags: {"Key":"Stage","Value":"Test"}, and
      {"Key":"Version","Value":"1"}

      The query would not return the following results, however. The following EC2 instance does not
      have all tag keys specified in the filter, so it is rejected. The RDS database has all of the
      tag keys, but no values that match at least one of the specified tag key values in the filter.

      * An EC2 instance that has only the following tag: ``{"Key":"Stage","Value":"Deploy"}`` .

      * An RDS database that has the following two tags: ``{"Key":"Stage","Value":"Archived"}`` , and
      ``{"Key":"Version","Value":"4"}``

       * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation stack
       ARN.

    - **Query** *(string) --* **[REQUIRED]**

      The query that defines a group or a search.
    """


_SearchResourcesPaginateResponseQueryErrorsTypeDef = TypedDict(
    "_SearchResourcesPaginateResponseQueryErrorsTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class SearchResourcesPaginateResponseQueryErrorsTypeDef(
    _SearchResourcesPaginateResponseQueryErrorsTypeDef
):
    """
    Type definition for `SearchResourcesPaginateResponse` `QueryErrors`

    A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources``
    operations on CloudFormation stack-based queries. The error occurs if the CloudFormation
    stack on which the query is based either does not exist, or has a status that renders the
    stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource
    Groups could not complete the operation, but the resulting group might have no member
    resources.

    - **ErrorCode** *(string) --*

      Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and
      ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

    - **Message** *(string) --*

      A message that explains the ``ErrorCode`` value. Messages might state that the specified
      CloudFormation stack does not exist (or no longer exists). For
      ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation
      stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
    """


_SearchResourcesPaginateResponseResourceIdentifiersTypeDef = TypedDict(
    "_SearchResourcesPaginateResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)


class SearchResourcesPaginateResponseResourceIdentifiersTypeDef(
    _SearchResourcesPaginateResponseResourceIdentifiersTypeDef
):
    """
    Type definition for `SearchResourcesPaginateResponse` `ResourceIdentifiers`

    The ARN of a resource, and its resource type.

    - **ResourceArn** *(string) --*

      The ARN of a resource.

    - **ResourceType** *(string) --*

      The resource type of a resource, such as ``AWS::EC2::Instance`` .
    """


_SearchResourcesPaginateResponseTypeDef = TypedDict(
    "_SearchResourcesPaginateResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            SearchResourcesPaginateResponseResourceIdentifiersTypeDef
        ],
        "QueryErrors": List[SearchResourcesPaginateResponseQueryErrorsTypeDef],
    },
    total=False,
)


class SearchResourcesPaginateResponseTypeDef(_SearchResourcesPaginateResponseTypeDef):
    """
    Type definition for `SearchResourcesPaginate` `Response`

    - **ResourceIdentifiers** *(list) --*

      The ARNs and resource types of resources that are members of the group that you specified.

      - *(dict) --*

        The ARN of a resource, and its resource type.

        - **ResourceArn** *(string) --*

          The ARN of a resource.

        - **ResourceType** *(string) --*

          The resource type of a resource, such as ``AWS::EC2::Instance`` .

    - **QueryErrors** *(list) --*

      A list of ``QueryError`` objects. Each error is an object that contains ``ErrorCode`` and
      ``Message`` structures. Possible values for ``ErrorCode`` are
      ``CLOUDFORMATION_STACK_INACTIVE`` and ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

      - *(dict) --*

        A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources``
        operations on CloudFormation stack-based queries. The error occurs if the CloudFormation
        stack on which the query is based either does not exist, or has a status that renders the
        stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource
        Groups could not complete the operation, but the resulting group might have no member
        resources.

        - **ErrorCode** *(string) --*

          Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and
          ``CLOUDFORMATION_STACK_NOT_EXISTING`` .

        - **Message** *(string) --*

          A message that explains the ``ErrorCode`` value. Messages might state that the specified
          CloudFormation stack does not exist (or no longer exists). For
          ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation
          stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
    """
