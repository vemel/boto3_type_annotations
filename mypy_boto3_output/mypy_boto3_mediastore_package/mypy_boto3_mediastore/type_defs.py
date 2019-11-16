"Main interface for mediastore type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateContainerResponseContainerTypeDef",
    "ClientCreateContainerResponseTypeDef",
    "ClientCreateContainerTagsTypeDef",
    "ClientDescribeContainerResponseContainerTypeDef",
    "ClientDescribeContainerResponseTypeDef",
    "ClientGetContainerPolicyResponseTypeDef",
    "ClientGetCorsPolicyResponseCorsPolicyTypeDef",
    "ClientGetCorsPolicyResponseTypeDef",
    "ClientGetLifecyclePolicyResponseTypeDef",
    "ClientListContainersResponseContainersTypeDef",
    "ClientListContainersResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutCorsPolicyCorsPolicyTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ListContainersPaginatePaginationConfigTypeDef",
    "ListContainersPaginateResponseContainersTypeDef",
    "ListContainersPaginateResponseTypeDef",
)


_ClientCreateContainerResponseContainerTypeDef = TypedDict(
    "_ClientCreateContainerResponseContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": str,
        "AccessLoggingEnabled": bool,
    },
    total=False,
)


class ClientCreateContainerResponseContainerTypeDef(
    _ClientCreateContainerResponseContainerTypeDef
):
    """
    Type definition for `ClientCreateContainerResponse` `Container`

    ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN has the
    following format: arn:aws:<region>:<account that owns this container>:container/<name of
    container>. For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

    ContainerName: The container name as specified in the request.

    CreationTime: Unix time stamp.

    Status: The status of container creation or deletion. The status is one of the following:
    ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container,
    the status is ``CREATING`` . When an endpoint is available, the status changes to ``ACTIVE`` .

    The return value does not include the container's endpoint. To make downstream requests, you
    must obtain this value by using  DescribeContainer or  ListContainers .

    - **Endpoint** *(string) --*

      The DNS endpoint of the container. Use the endpoint to identify the specific container when
      sending requests to the data plane. The service assigns this value when the container is
      created. Once the value has been assigned, it does not change.

    - **CreationTime** *(datetime) --*

      Unix timestamp.

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the container. The ARN has the following format:

      arn:aws:<region>:<account that owns this container>:container/<name of container>

      For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

    - **Name** *(string) --*

      The name of the container.

    - **Status** *(string) --*

      The status of container creation or deletion. The status is one of the following:
      ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container,
      the status is ``CREATING`` . When the endpoint is available, the status changes to
      ``ACTIVE`` .

    - **AccessLoggingEnabled** *(boolean) --*

      The state of access logging on the container. This value is ``false`` by default,
      indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch
      Logs. When you enable access logging on the container, MediaStore changes this value to
      ``true`` , indicating that the service delivers access logs for objects stored in that
      container to CloudWatch Logs.
    """


_ClientCreateContainerResponseTypeDef = TypedDict(
    "_ClientCreateContainerResponseTypeDef",
    {"Container": ClientCreateContainerResponseContainerTypeDef},
    total=False,
)


class ClientCreateContainerResponseTypeDef(_ClientCreateContainerResponseTypeDef):
    """
    Type definition for `ClientCreateContainer` `Response`

    - **Container** *(dict) --*

      ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN has the
      following format: arn:aws:<region>:<account that owns this container>:container/<name of
      container>. For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

      ContainerName: The container name as specified in the request.

      CreationTime: Unix time stamp.

      Status: The status of container creation or deletion. The status is one of the following:
      ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container,
      the status is ``CREATING`` . When an endpoint is available, the status changes to ``ACTIVE`` .

      The return value does not include the container's endpoint. To make downstream requests, you
      must obtain this value by using  DescribeContainer or  ListContainers .

      - **Endpoint** *(string) --*

        The DNS endpoint of the container. Use the endpoint to identify the specific container when
        sending requests to the data plane. The service assigns this value when the container is
        created. Once the value has been assigned, it does not change.

      - **CreationTime** *(datetime) --*

        Unix timestamp.

      - **ARN** *(string) --*

        The Amazon Resource Name (ARN) of the container. The ARN has the following format:

        arn:aws:<region>:<account that owns this container>:container/<name of container>

        For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

      - **Name** *(string) --*

        The name of the container.

      - **Status** *(string) --*

        The status of container creation or deletion. The status is one of the following:
        ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container,
        the status is ``CREATING`` . When the endpoint is available, the status changes to
        ``ACTIVE`` .

      - **AccessLoggingEnabled** *(boolean) --*

        The state of access logging on the container. This value is ``false`` by default,
        indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch
        Logs. When you enable access logging on the container, MediaStore changes this value to
        ``true`` , indicating that the service delivers access logs for objects stored in that
        container to CloudWatch Logs.
    """


_ClientCreateContainerTagsTypeDef = TypedDict(
    "_ClientCreateContainerTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateContainerTagsTypeDef(_ClientCreateContainerTagsTypeDef):
    """
    Type definition for `ClientCreateContainer` `Tags`

    A collection of tags associated with a container. Each tag consists of a key:value pair, which
    can be anything you define. Typically, the tag key represents a category (such as
    "environment") and the tag value represents a specific value within that category (such as
    "test," "development," or "production"). You can add up to 50 tags to each container. For more
    information about tagging, including naming and usage conventions, see `Tagging Resources in
    MediaStore <https://aws.amazon.com/documentation/mediastore/tagging>`__ .

    - **Key** *(string) --*

      Part of the key:value pair that defines a tag. You can use a tag key to describe a category
      of information, such as "customer." Tag keys are case-sensitive.

    - **Value** *(string) --*

      Part of the key:value pair that defines a tag. You can use a tag value to describe a specific
      value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.
    """


_ClientDescribeContainerResponseContainerTypeDef = TypedDict(
    "_ClientDescribeContainerResponseContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": str,
        "AccessLoggingEnabled": bool,
    },
    total=False,
)


class ClientDescribeContainerResponseContainerTypeDef(
    _ClientDescribeContainerResponseContainerTypeDef
):
    """
    Type definition for `ClientDescribeContainerResponse` `Container`

    The name of the queried container.

    - **Endpoint** *(string) --*

      The DNS endpoint of the container. Use the endpoint to identify the specific container when
      sending requests to the data plane. The service assigns this value when the container is
      created. Once the value has been assigned, it does not change.

    - **CreationTime** *(datetime) --*

      Unix timestamp.

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the container. The ARN has the following format:

      arn:aws:<region>:<account that owns this container>:container/<name of container>

      For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

    - **Name** *(string) --*

      The name of the container.

    - **Status** *(string) --*

      The status of container creation or deletion. The status is one of the following:
      ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container,
      the status is ``CREATING`` . When the endpoint is available, the status changes to
      ``ACTIVE`` .

    - **AccessLoggingEnabled** *(boolean) --*

      The state of access logging on the container. This value is ``false`` by default,
      indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch
      Logs. When you enable access logging on the container, MediaStore changes this value to
      ``true`` , indicating that the service delivers access logs for objects stored in that
      container to CloudWatch Logs.
    """


_ClientDescribeContainerResponseTypeDef = TypedDict(
    "_ClientDescribeContainerResponseTypeDef",
    {"Container": ClientDescribeContainerResponseContainerTypeDef},
    total=False,
)


class ClientDescribeContainerResponseTypeDef(_ClientDescribeContainerResponseTypeDef):
    """
    Type definition for `ClientDescribeContainer` `Response`

    - **Container** *(dict) --*

      The name of the queried container.

      - **Endpoint** *(string) --*

        The DNS endpoint of the container. Use the endpoint to identify the specific container when
        sending requests to the data plane. The service assigns this value when the container is
        created. Once the value has been assigned, it does not change.

      - **CreationTime** *(datetime) --*

        Unix timestamp.

      - **ARN** *(string) --*

        The Amazon Resource Name (ARN) of the container. The ARN has the following format:

        arn:aws:<region>:<account that owns this container>:container/<name of container>

        For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

      - **Name** *(string) --*

        The name of the container.

      - **Status** *(string) --*

        The status of container creation or deletion. The status is one of the following:
        ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container,
        the status is ``CREATING`` . When the endpoint is available, the status changes to
        ``ACTIVE`` .

      - **AccessLoggingEnabled** *(boolean) --*

        The state of access logging on the container. This value is ``false`` by default,
        indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch
        Logs. When you enable access logging on the container, MediaStore changes this value to
        ``true`` , indicating that the service delivers access logs for objects stored in that
        container to CloudWatch Logs.
    """


_ClientGetContainerPolicyResponseTypeDef = TypedDict(
    "_ClientGetContainerPolicyResponseTypeDef", {"Policy": str}, total=False
)


class ClientGetContainerPolicyResponseTypeDef(_ClientGetContainerPolicyResponseTypeDef):
    """
    Type definition for `ClientGetContainerPolicy` `Response`

    - **Policy** *(string) --*

      The contents of the access policy.
    """


_ClientGetCorsPolicyResponseCorsPolicyTypeDef = TypedDict(
    "_ClientGetCorsPolicyResponseCorsPolicyTypeDef",
    {
        "AllowedOrigins": List[str],
        "AllowedMethods": List[str],
        "AllowedHeaders": List[str],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)


class ClientGetCorsPolicyResponseCorsPolicyTypeDef(
    _ClientGetCorsPolicyResponseCorsPolicyTypeDef
):
    """
    Type definition for `ClientGetCorsPolicyResponse` `CorsPolicy`

    A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one
    rule applies, the service uses the first applicable rule listed.

    - **AllowedOrigins** *(list) --*

      One or more response headers that you want users to be able to access from their
      applications (for example, from a JavaScript ``XMLHttpRequest`` object).

      Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can
      include only one wildcard character (*), for example, http://*.example.com. Additionally,
      you can specify only one wildcard character to allow cross-origin access for all origins.

      - *(string) --*

    - **AllowedMethods** *(list) --*

      Identifies an HTTP method that the origin that is specified in the rule is allowed to
      execute.

      Each CORS rule must contain at least one ``AllowedMethods`` and one ``AllowedOrigins``
      element.

      - *(string) --*

    - **AllowedHeaders** *(list) --*

      Specifies which headers are allowed in a preflight ``OPTIONS`` request through the
      ``Access-Control-Request-Headers`` header. Each header name that is specified in
      ``Access-Control-Request-Headers`` must have a corresponding entry in the rule. Only the
      headers that were requested are sent back.

      This element can contain only one wildcard character (*).

      - *(string) --*

    - **MaxAgeSeconds** *(integer) --*

      The time in seconds that your browser caches the preflight response for the specified
      resource.

      A CORS rule can have only one ``MaxAgeSeconds`` element.

    - **ExposeHeaders** *(list) --*

      One or more headers in the response that you want users to be able to access from their
      applications (for example, from a JavaScript ``XMLHttpRequest`` object).

      This element is optional for each rule.

      - *(string) --*
    """


_ClientGetCorsPolicyResponseTypeDef = TypedDict(
    "_ClientGetCorsPolicyResponseTypeDef",
    {"CorsPolicy": List[ClientGetCorsPolicyResponseCorsPolicyTypeDef]},
    total=False,
)


class ClientGetCorsPolicyResponseTypeDef(_ClientGetCorsPolicyResponseTypeDef):
    """
    Type definition for `ClientGetCorsPolicy` `Response`

    - **CorsPolicy** *(list) --*

      The CORS policy assigned to the container.

      - *(dict) --*

        A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one
        rule applies, the service uses the first applicable rule listed.

        - **AllowedOrigins** *(list) --*

          One or more response headers that you want users to be able to access from their
          applications (for example, from a JavaScript ``XMLHttpRequest`` object).

          Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can
          include only one wildcard character (*), for example, http://*.example.com. Additionally,
          you can specify only one wildcard character to allow cross-origin access for all origins.

          - *(string) --*

        - **AllowedMethods** *(list) --*

          Identifies an HTTP method that the origin that is specified in the rule is allowed to
          execute.

          Each CORS rule must contain at least one ``AllowedMethods`` and one ``AllowedOrigins``
          element.

          - *(string) --*

        - **AllowedHeaders** *(list) --*

          Specifies which headers are allowed in a preflight ``OPTIONS`` request through the
          ``Access-Control-Request-Headers`` header. Each header name that is specified in
          ``Access-Control-Request-Headers`` must have a corresponding entry in the rule. Only the
          headers that were requested are sent back.

          This element can contain only one wildcard character (*).

          - *(string) --*

        - **MaxAgeSeconds** *(integer) --*

          The time in seconds that your browser caches the preflight response for the specified
          resource.

          A CORS rule can have only one ``MaxAgeSeconds`` element.

        - **ExposeHeaders** *(list) --*

          One or more headers in the response that you want users to be able to access from their
          applications (for example, from a JavaScript ``XMLHttpRequest`` object).

          This element is optional for each rule.

          - *(string) --*
    """


_ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponseTypeDef", {"LifecyclePolicy": str}, total=False
)


class ClientGetLifecyclePolicyResponseTypeDef(_ClientGetLifecyclePolicyResponseTypeDef):
    """
    Type definition for `ClientGetLifecyclePolicy` `Response`

    - **LifecyclePolicy** *(string) --*

      The object lifecycle policy that is assigned to the container.
    """


_ClientListContainersResponseContainersTypeDef = TypedDict(
    "_ClientListContainersResponseContainersTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": str,
        "AccessLoggingEnabled": bool,
    },
    total=False,
)


class ClientListContainersResponseContainersTypeDef(
    _ClientListContainersResponseContainersTypeDef
):
    """
    Type definition for `ClientListContainersResponse` `Containers`

    This section describes operations that you can perform on an AWS Elemental MediaStore
    container.

    - **Endpoint** *(string) --*

      The DNS endpoint of the container. Use the endpoint to identify the specific container
      when sending requests to the data plane. The service assigns this value when the
      container is created. Once the value has been assigned, it does not change.

    - **CreationTime** *(datetime) --*

      Unix timestamp.

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the container. The ARN has the following format:

      arn:aws:<region>:<account that owns this container>:container/<name of container>

      For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

    - **Name** *(string) --*

      The name of the container.

    - **Status** *(string) --*

      The status of container creation or deletion. The status is one of the following:
      ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the
      container, the status is ``CREATING`` . When the endpoint is available, the status
      changes to ``ACTIVE`` .

    - **AccessLoggingEnabled** *(boolean) --*

      The state of access logging on the container. This value is ``false`` by default,
      indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch
      Logs. When you enable access logging on the container, MediaStore changes this value to
      ``true`` , indicating that the service delivers access logs for objects stored in that
      container to CloudWatch Logs.
    """


_ClientListContainersResponseTypeDef = TypedDict(
    "_ClientListContainersResponseTypeDef",
    {
        "Containers": List[ClientListContainersResponseContainersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListContainersResponseTypeDef(_ClientListContainersResponseTypeDef):
    """
    Type definition for `ClientListContainers` `Response`

    - **Containers** *(list) --*

      The names of the containers.

      - *(dict) --*

        This section describes operations that you can perform on an AWS Elemental MediaStore
        container.

        - **Endpoint** *(string) --*

          The DNS endpoint of the container. Use the endpoint to identify the specific container
          when sending requests to the data plane. The service assigns this value when the
          container is created. Once the value has been assigned, it does not change.

        - **CreationTime** *(datetime) --*

          Unix timestamp.

        - **ARN** *(string) --*

          The Amazon Resource Name (ARN) of the container. The ARN has the following format:

          arn:aws:<region>:<account that owns this container>:container/<name of container>

          For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

        - **Name** *(string) --*

          The name of the container.

        - **Status** *(string) --*

          The status of container creation or deletion. The status is one of the following:
          ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the
          container, the status is ``CREATING`` . When the endpoint is available, the status
          changes to ``ACTIVE`` .

        - **AccessLoggingEnabled** *(boolean) --*

          The state of access logging on the container. This value is ``false`` by default,
          indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch
          Logs. When you enable access logging on the container, MediaStore changes this value to
          ``true`` , indicating that the service delivers access logs for objects stored in that
          container to CloudWatch Logs.

    - **NextToken** *(string) --*

       ``NextToken`` is the token to use in the next call to ``ListContainers`` . This token is
       returned only if you included the ``MaxResults`` tag in the original command, and only if
       there are still containers to return.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    A collection of tags associated with a container. Each tag consists of a key:value pair,
    which can be anything you define. Typically, the tag key represents a category (such as
    "environment") and the tag value represents a specific value within that category (such as
    "test," "development," or "production"). You can add up to 50 tags to each container. For
    more information about tagging, including naming and usage conventions, see `Tagging
    Resources in MediaStore <https://aws.amazon.com/documentation/mediastore/tagging>`__ .

    - **Key** *(string) --*

      Part of the key:value pair that defines a tag. You can use a tag key to describe a
      category of information, such as "customer." Tag keys are case-sensitive.

    - **Value** *(string) --*

      Part of the key:value pair that defines a tag. You can use a tag value to describe a
      specific value within a category, such as "companyA" or "companyB." Tag values are
      case-sensitive.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      An array of key:value pairs that are assigned to the container.

      - *(dict) --*

        A collection of tags associated with a container. Each tag consists of a key:value pair,
        which can be anything you define. Typically, the tag key represents a category (such as
        "environment") and the tag value represents a specific value within that category (such as
        "test," "development," or "production"). You can add up to 50 tags to each container. For
        more information about tagging, including naming and usage conventions, see `Tagging
        Resources in MediaStore <https://aws.amazon.com/documentation/mediastore/tagging>`__ .

        - **Key** *(string) --*

          Part of the key:value pair that defines a tag. You can use a tag key to describe a
          category of information, such as "customer." Tag keys are case-sensitive.

        - **Value** *(string) --*

          Part of the key:value pair that defines a tag. You can use a tag value to describe a
          specific value within a category, such as "companyA" or "companyB." Tag values are
          case-sensitive.
    """


_RequiredClientPutCorsPolicyCorsPolicyTypeDef = TypedDict(
    "_RequiredClientPutCorsPolicyCorsPolicyTypeDef",
    {"AllowedOrigins": List[str], "AllowedHeaders": List[str]},
)
_OptionalClientPutCorsPolicyCorsPolicyTypeDef = TypedDict(
    "_OptionalClientPutCorsPolicyCorsPolicyTypeDef",
    {"AllowedMethods": List[str], "MaxAgeSeconds": int, "ExposeHeaders": List[str]},
    total=False,
)


class ClientPutCorsPolicyCorsPolicyTypeDef(
    _RequiredClientPutCorsPolicyCorsPolicyTypeDef,
    _OptionalClientPutCorsPolicyCorsPolicyTypeDef,
):
    """
    Type definition for `ClientPutCorsPolicy` `CorsPolicy`

    A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule
    applies, the service uses the first applicable rule listed.

    - **AllowedOrigins** *(list) --* **[REQUIRED]**

      One or more response headers that you want users to be able to access from their applications
      (for example, from a JavaScript ``XMLHttpRequest`` object).

      Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can
      include only one wildcard character (*), for example, http://*.example.com. Additionally, you
      can specify only one wildcard character to allow cross-origin access for all origins.

      - *(string) --*

    - **AllowedMethods** *(list) --*

      Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.

      Each CORS rule must contain at least one ``AllowedMethods`` and one ``AllowedOrigins``
      element.

      - *(string) --*

    - **AllowedHeaders** *(list) --* **[REQUIRED]**

      Specifies which headers are allowed in a preflight ``OPTIONS`` request through the
      ``Access-Control-Request-Headers`` header. Each header name that is specified in
      ``Access-Control-Request-Headers`` must have a corresponding entry in the rule. Only the
      headers that were requested are sent back.

      This element can contain only one wildcard character (*).

      - *(string) --*

    - **MaxAgeSeconds** *(integer) --*

      The time in seconds that your browser caches the preflight response for the specified
      resource.

      A CORS rule can have only one ``MaxAgeSeconds`` element.

    - **ExposeHeaders** *(list) --*

      One or more headers in the response that you want users to be able to access from their
      applications (for example, from a JavaScript ``XMLHttpRequest`` object).

      This element is optional for each rule.

      - *(string) --*
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A collection of tags associated with a container. Each tag consists of a key:value pair, which
    can be anything you define. Typically, the tag key represents a category (such as
    "environment") and the tag value represents a specific value within that category (such as
    "test," "development," or "production"). You can add up to 50 tags to each container. For more
    information about tagging, including naming and usage conventions, see `Tagging Resources in
    MediaStore <https://aws.amazon.com/documentation/mediastore/tagging>`__ .

    - **Key** *(string) --*

      Part of the key:value pair that defines a tag. You can use a tag key to describe a category
      of information, such as "customer." Tag keys are case-sensitive.

    - **Value** *(string) --*

      Part of the key:value pair that defines a tag. You can use a tag value to describe a specific
      value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.
    """


_ListContainersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListContainersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListContainersPaginatePaginationConfigTypeDef(
    _ListContainersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListContainersPaginate` `PaginationConfig`

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


_ListContainersPaginateResponseContainersTypeDef = TypedDict(
    "_ListContainersPaginateResponseContainersTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": str,
        "AccessLoggingEnabled": bool,
    },
    total=False,
)


class ListContainersPaginateResponseContainersTypeDef(
    _ListContainersPaginateResponseContainersTypeDef
):
    """
    Type definition for `ListContainersPaginateResponse` `Containers`

    This section describes operations that you can perform on an AWS Elemental MediaStore
    container.

    - **Endpoint** *(string) --*

      The DNS endpoint of the container. Use the endpoint to identify the specific container
      when sending requests to the data plane. The service assigns this value when the
      container is created. Once the value has been assigned, it does not change.

    - **CreationTime** *(datetime) --*

      Unix timestamp.

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the container. The ARN has the following format:

      arn:aws:<region>:<account that owns this container>:container/<name of container>

      For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

    - **Name** *(string) --*

      The name of the container.

    - **Status** *(string) --*

      The status of container creation or deletion. The status is one of the following:
      ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the
      container, the status is ``CREATING`` . When the endpoint is available, the status
      changes to ``ACTIVE`` .

    - **AccessLoggingEnabled** *(boolean) --*

      The state of access logging on the container. This value is ``false`` by default,
      indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch
      Logs. When you enable access logging on the container, MediaStore changes this value to
      ``true`` , indicating that the service delivers access logs for objects stored in that
      container to CloudWatch Logs.
    """


_ListContainersPaginateResponseTypeDef = TypedDict(
    "_ListContainersPaginateResponseTypeDef",
    {"Containers": List[ListContainersPaginateResponseContainersTypeDef]},
    total=False,
)


class ListContainersPaginateResponseTypeDef(_ListContainersPaginateResponseTypeDef):
    """
    Type definition for `ListContainersPaginate` `Response`

    - **Containers** *(list) --*

      The names of the containers.

      - *(dict) --*

        This section describes operations that you can perform on an AWS Elemental MediaStore
        container.

        - **Endpoint** *(string) --*

          The DNS endpoint of the container. Use the endpoint to identify the specific container
          when sending requests to the data plane. The service assigns this value when the
          container is created. Once the value has been assigned, it does not change.

        - **CreationTime** *(datetime) --*

          Unix timestamp.

        - **ARN** *(string) --*

          The Amazon Resource Name (ARN) of the container. The ARN has the following format:

          arn:aws:<region>:<account that owns this container>:container/<name of container>

          For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

        - **Name** *(string) --*

          The name of the container.

        - **Status** *(string) --*

          The status of container creation or deletion. The status is one of the following:
          ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the
          container, the status is ``CREATING`` . When the endpoint is available, the status
          changes to ``ACTIVE`` .

        - **AccessLoggingEnabled** *(boolean) --*

          The state of access logging on the container. This value is ``false`` by default,
          indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch
          Logs. When you enable access logging on the container, MediaStore changes this value to
          ``true`` , indicating that the service delivers access logs for objects stored in that
          container to CloudWatch Logs.
    """
