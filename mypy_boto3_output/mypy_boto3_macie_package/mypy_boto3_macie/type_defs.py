"Main interface for macie type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientAssociateS3ResourcesResponseTypeDef",
    "ClientAssociateS3Resourcess3ResourcesclassificationTypeTypeDef",
    "ClientAssociateS3Resourcess3ResourcesTypeDef",
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientDisassociateS3ResourcesResponseTypeDef",
    "ClientDisassociateS3ResourcesassociatedS3ResourcesTypeDef",
    "ClientListMemberAccountsResponsememberAccountsTypeDef",
    "ClientListMemberAccountsResponseTypeDef",
    "ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef",
    "ClientListS3ResourcesResponses3ResourcesTypeDef",
    "ClientListS3ResourcesResponseTypeDef",
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientUpdateS3ResourcesResponseTypeDef",
    "ClientUpdateS3Resourcess3ResourcesUpdateclassificationTypeUpdateTypeDef",
    "ClientUpdateS3Resourcess3ResourcesUpdateTypeDef",
    "ListMemberAccountsPaginatePaginationConfigTypeDef",
    "ListMemberAccountsPaginateResponsememberAccountsTypeDef",
    "ListMemberAccountsPaginateResponseTypeDef",
    "ListS3ResourcesPaginatePaginationConfigTypeDef",
    "ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef",
    "ListS3ResourcesPaginateResponses3ResourcesTypeDef",
    "ListS3ResourcesPaginateResponseTypeDef",
)


_ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "_ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)


class ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef(
    _ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef
):
    """
    Type definition for `ClientAssociateS3ResourcesResponsefailedS3Resources` `failedItem`

    The failed S3 resources.

    - **bucketName** *(string) --*

      The name of the S3 bucket.

    - **prefix** *(string) --*

      The prefix of the S3 bucket.
    """


_ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "_ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)


class ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef(
    _ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef
):
    """
    Type definition for `ClientAssociateS3ResourcesResponse` `failedS3Resources`

    Includes details about the failed S3 resources.

    - **failedItem** *(dict) --*

      The failed S3 resources.

      - **bucketName** *(string) --*

        The name of the S3 bucket.

      - **prefix** *(string) --*

        The prefix of the S3 bucket.

    - **errorCode** *(string) --*

      The status code of a failed item.

    - **errorMessage** *(string) --*

      The error message of a failed item.
    """


_ClientAssociateS3ResourcesResponseTypeDef = TypedDict(
    "_ClientAssociateS3ResourcesResponseTypeDef",
    {
        "failedS3Resources": List[
            ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef
        ]
    },
    total=False,
)


class ClientAssociateS3ResourcesResponseTypeDef(
    _ClientAssociateS3ResourcesResponseTypeDef
):
    """
    Type definition for `ClientAssociateS3Resources` `Response`

    - **failedS3Resources** *(list) --*

      S3 resources that couldn't be associated with Amazon Macie. An error code and an error
      message are provided for each failed item.

      - *(dict) --*

        Includes details about the failed S3 resources.

        - **failedItem** *(dict) --*

          The failed S3 resources.

          - **bucketName** *(string) --*

            The name of the S3 bucket.

          - **prefix** *(string) --*

            The prefix of the S3 bucket.

        - **errorCode** *(string) --*

          The status code of a failed item.

        - **errorMessage** *(string) --*

          The error message of a failed item.
    """


_ClientAssociateS3Resourcess3ResourcesclassificationTypeTypeDef = TypedDict(
    "_ClientAssociateS3Resourcess3ResourcesclassificationTypeTypeDef",
    {"oneTime": str, "continuous": str},
)


class ClientAssociateS3Resourcess3ResourcesclassificationTypeTypeDef(
    _ClientAssociateS3Resourcess3ResourcesclassificationTypeTypeDef
):
    """
    Type definition for `ClientAssociateS3Resourcess3Resources` `classificationType`

    The classification type that you want to specify for the resource associated with Amazon
    Macie.

    - **oneTime** *(string) --* **[REQUIRED]**

      A one-time classification of all of the existing objects in a specified S3 bucket.

    - **continuous** *(string) --* **[REQUIRED]**

      A continuous classification of the objects that are added to a specified S3 bucket. Amazon
      Macie begins performing continuous classification after a bucket is successfully associated
      with Amazon Macie.
    """


_RequiredClientAssociateS3Resourcess3ResourcesTypeDef = TypedDict(
    "_RequiredClientAssociateS3Resourcess3ResourcesTypeDef",
    {
        "bucketName": str,
        "classificationType": ClientAssociateS3Resourcess3ResourcesclassificationTypeTypeDef,
    },
)
_OptionalClientAssociateS3Resourcess3ResourcesTypeDef = TypedDict(
    "_OptionalClientAssociateS3Resourcess3ResourcesTypeDef",
    {"prefix": str},
    total=False,
)


class ClientAssociateS3Resourcess3ResourcesTypeDef(
    _RequiredClientAssociateS3Resourcess3ResourcesTypeDef,
    _OptionalClientAssociateS3Resourcess3ResourcesTypeDef,
):
    """
    Type definition for `ClientAssociateS3Resources` `s3Resources`

    The S3 resources that you want to associate with Amazon Macie for monitoring and data
    classification. This data type is used as a request parameter in the AssociateS3Resources
    action and a response parameter in the ListS3Resources action.

    - **bucketName** *(string) --* **[REQUIRED]**

      The name of the S3 bucket that you want to associate with Amazon Macie.

    - **prefix** *(string) --*

      The prefix of the S3 bucket that you want to associate with Amazon Macie.

    - **classificationType** *(dict) --* **[REQUIRED]**

      The classification type that you want to specify for the resource associated with Amazon
      Macie.

      - **oneTime** *(string) --* **[REQUIRED]**

        A one-time classification of all of the existing objects in a specified S3 bucket.

      - **continuous** *(string) --* **[REQUIRED]**

        A continuous classification of the objects that are added to a specified S3 bucket. Amazon
        Macie begins performing continuous classification after a bucket is successfully associated
        with Amazon Macie.
    """


_ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "_ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)


class ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef(
    _ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef
):
    """
    Type definition for `ClientDisassociateS3ResourcesResponsefailedS3Resources` `failedItem`

    The failed S3 resources.

    - **bucketName** *(string) --*

      The name of the S3 bucket.

    - **prefix** *(string) --*

      The prefix of the S3 bucket.
    """


_ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "_ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)


class ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef(
    _ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef
):
    """
    Type definition for `ClientDisassociateS3ResourcesResponse` `failedS3Resources`

    Includes details about the failed S3 resources.

    - **failedItem** *(dict) --*

      The failed S3 resources.

      - **bucketName** *(string) --*

        The name of the S3 bucket.

      - **prefix** *(string) --*

        The prefix of the S3 bucket.

    - **errorCode** *(string) --*

      The status code of a failed item.

    - **errorMessage** *(string) --*

      The error message of a failed item.
    """


_ClientDisassociateS3ResourcesResponseTypeDef = TypedDict(
    "_ClientDisassociateS3ResourcesResponseTypeDef",
    {
        "failedS3Resources": List[
            ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef
        ]
    },
    total=False,
)


class ClientDisassociateS3ResourcesResponseTypeDef(
    _ClientDisassociateS3ResourcesResponseTypeDef
):
    """
    Type definition for `ClientDisassociateS3Resources` `Response`

    - **failedS3Resources** *(list) --*

      S3 resources that couldn't be removed from being monitored and classified by Amazon Macie. An
      error code and an error message are provided for each failed item.

      - *(dict) --*

        Includes details about the failed S3 resources.

        - **failedItem** *(dict) --*

          The failed S3 resources.

          - **bucketName** *(string) --*

            The name of the S3 bucket.

          - **prefix** *(string) --*

            The prefix of the S3 bucket.

        - **errorCode** *(string) --*

          The status code of a failed item.

        - **errorMessage** *(string) --*

          The error message of a failed item.
    """


_RequiredClientDisassociateS3ResourcesassociatedS3ResourcesTypeDef = TypedDict(
    "_RequiredClientDisassociateS3ResourcesassociatedS3ResourcesTypeDef",
    {"bucketName": str},
)
_OptionalClientDisassociateS3ResourcesassociatedS3ResourcesTypeDef = TypedDict(
    "_OptionalClientDisassociateS3ResourcesassociatedS3ResourcesTypeDef",
    {"prefix": str},
    total=False,
)


class ClientDisassociateS3ResourcesassociatedS3ResourcesTypeDef(
    _RequiredClientDisassociateS3ResourcesassociatedS3ResourcesTypeDef,
    _OptionalClientDisassociateS3ResourcesassociatedS3ResourcesTypeDef,
):
    """
    Type definition for `ClientDisassociateS3Resources` `associatedS3Resources`

    Contains information about the S3 resource. This data type is used as a request parameter in
    the DisassociateS3Resources action and can be used as a response parameter in the
    AssociateS3Resources and UpdateS3Resources actions.

    - **bucketName** *(string) --* **[REQUIRED]**

      The name of the S3 bucket.

    - **prefix** *(string) --*

      The prefix of the S3 bucket.
    """


_ClientListMemberAccountsResponsememberAccountsTypeDef = TypedDict(
    "_ClientListMemberAccountsResponsememberAccountsTypeDef",
    {"accountId": str},
    total=False,
)


class ClientListMemberAccountsResponsememberAccountsTypeDef(
    _ClientListMemberAccountsResponsememberAccountsTypeDef
):
    """
    Type definition for `ClientListMemberAccountsResponse` `memberAccounts`

    Contains information about the Amazon Macie member account.

    - **accountId** *(string) --*

      The AWS account ID of the Amazon Macie member account.
    """


_ClientListMemberAccountsResponseTypeDef = TypedDict(
    "_ClientListMemberAccountsResponseTypeDef",
    {
        "memberAccounts": List[ClientListMemberAccountsResponsememberAccountsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListMemberAccountsResponseTypeDef(_ClientListMemberAccountsResponseTypeDef):
    """
    Type definition for `ClientListMemberAccounts` `Response`

    - **memberAccounts** *(list) --*

      A list of the Amazon Macie member accounts returned by the action. The current master account
      is also included in this list.

      - *(dict) --*

        Contains information about the Amazon Macie member account.

        - **accountId** *(string) --*

          The AWS account ID of the Amazon Macie member account.

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the nextToken parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef = TypedDict(
    "_ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef",
    {"oneTime": str, "continuous": str},
    total=False,
)


class ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef(
    _ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef
):
    """
    Type definition for `ClientListS3ResourcesResponses3Resources` `classificationType`

    The classification type that you want to specify for the resource associated with Amazon
    Macie.

    - **oneTime** *(string) --*

      A one-time classification of all of the existing objects in a specified S3 bucket.

    - **continuous** *(string) --*

      A continuous classification of the objects that are added to a specified S3 bucket.
      Amazon Macie begins performing continuous classification after a bucket is successfully
      associated with Amazon Macie.
    """


_ClientListS3ResourcesResponses3ResourcesTypeDef = TypedDict(
    "_ClientListS3ResourcesResponses3ResourcesTypeDef",
    {
        "bucketName": str,
        "prefix": str,
        "classificationType": ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)


class ClientListS3ResourcesResponses3ResourcesTypeDef(
    _ClientListS3ResourcesResponses3ResourcesTypeDef
):
    """
    Type definition for `ClientListS3ResourcesResponse` `s3Resources`

    The S3 resources that you want to associate with Amazon Macie for monitoring and data
    classification. This data type is used as a request parameter in the AssociateS3Resources
    action and a response parameter in the ListS3Resources action.

    - **bucketName** *(string) --*

      The name of the S3 bucket that you want to associate with Amazon Macie.

    - **prefix** *(string) --*

      The prefix of the S3 bucket that you want to associate with Amazon Macie.

    - **classificationType** *(dict) --*

      The classification type that you want to specify for the resource associated with Amazon
      Macie.

      - **oneTime** *(string) --*

        A one-time classification of all of the existing objects in a specified S3 bucket.

      - **continuous** *(string) --*

        A continuous classification of the objects that are added to a specified S3 bucket.
        Amazon Macie begins performing continuous classification after a bucket is successfully
        associated with Amazon Macie.
    """


_ClientListS3ResourcesResponseTypeDef = TypedDict(
    "_ClientListS3ResourcesResponseTypeDef",
    {
        "s3Resources": List[ClientListS3ResourcesResponses3ResourcesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListS3ResourcesResponseTypeDef(_ClientListS3ResourcesResponseTypeDef):
    """
    Type definition for `ClientListS3Resources` `Response`

    - **s3Resources** *(list) --*

      A list of the associated S3 resources returned by the action.

      - *(dict) --*

        The S3 resources that you want to associate with Amazon Macie for monitoring and data
        classification. This data type is used as a request parameter in the AssociateS3Resources
        action and a response parameter in the ListS3Resources action.

        - **bucketName** *(string) --*

          The name of the S3 bucket that you want to associate with Amazon Macie.

        - **prefix** *(string) --*

          The prefix of the S3 bucket that you want to associate with Amazon Macie.

        - **classificationType** *(dict) --*

          The classification type that you want to specify for the resource associated with Amazon
          Macie.

          - **oneTime** *(string) --*

            A one-time classification of all of the existing objects in a specified S3 bucket.

          - **continuous** *(string) --*

            A continuous classification of the objects that are added to a specified S3 bucket.
            Amazon Macie begins performing continuous classification after a bucket is successfully
            associated with Amazon Macie.

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the nextToken parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "_ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)


class ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef(
    _ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef
):
    """
    Type definition for `ClientUpdateS3ResourcesResponsefailedS3Resources` `failedItem`

    The failed S3 resources.

    - **bucketName** *(string) --*

      The name of the S3 bucket.

    - **prefix** *(string) --*

      The prefix of the S3 bucket.
    """


_ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "_ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)


class ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef(
    _ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef
):
    """
    Type definition for `ClientUpdateS3ResourcesResponse` `failedS3Resources`

    Includes details about the failed S3 resources.

    - **failedItem** *(dict) --*

      The failed S3 resources.

      - **bucketName** *(string) --*

        The name of the S3 bucket.

      - **prefix** *(string) --*

        The prefix of the S3 bucket.

    - **errorCode** *(string) --*

      The status code of a failed item.

    - **errorMessage** *(string) --*

      The error message of a failed item.
    """


_ClientUpdateS3ResourcesResponseTypeDef = TypedDict(
    "_ClientUpdateS3ResourcesResponseTypeDef",
    {
        "failedS3Resources": List[
            ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef
        ]
    },
    total=False,
)


class ClientUpdateS3ResourcesResponseTypeDef(_ClientUpdateS3ResourcesResponseTypeDef):
    """
    Type definition for `ClientUpdateS3Resources` `Response`

    - **failedS3Resources** *(list) --*

      The S3 resources whose classification types can't be updated. An error code and an error
      message are provided for each failed item.

      - *(dict) --*

        Includes details about the failed S3 resources.

        - **failedItem** *(dict) --*

          The failed S3 resources.

          - **bucketName** *(string) --*

            The name of the S3 bucket.

          - **prefix** *(string) --*

            The prefix of the S3 bucket.

        - **errorCode** *(string) --*

          The status code of a failed item.

        - **errorMessage** *(string) --*

          The error message of a failed item.
    """


_ClientUpdateS3Resourcess3ResourcesUpdateclassificationTypeUpdateTypeDef = TypedDict(
    "_ClientUpdateS3Resourcess3ResourcesUpdateclassificationTypeUpdateTypeDef",
    {"oneTime": str, "continuous": str},
    total=False,
)


class ClientUpdateS3Resourcess3ResourcesUpdateclassificationTypeUpdateTypeDef(
    _ClientUpdateS3Resourcess3ResourcesUpdateclassificationTypeUpdateTypeDef
):
    """
    Type definition for `ClientUpdateS3Resourcess3ResourcesUpdate` `classificationTypeUpdate`

    The classification type that you want to update for the resource associated with Amazon Macie.

    - **oneTime** *(string) --*

      A one-time classification of all of the existing objects in a specified S3 bucket.

    - **continuous** *(string) --*

      A continuous classification of the objects that are added to a specified S3 bucket. Amazon
      Macie begins performing continuous classification after a bucket is successfully associated
      with Amazon Macie.
    """


_RequiredClientUpdateS3Resourcess3ResourcesUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateS3Resourcess3ResourcesUpdateTypeDef",
    {
        "bucketName": str,
        "classificationTypeUpdate": ClientUpdateS3Resourcess3ResourcesUpdateclassificationTypeUpdateTypeDef,
    },
)
_OptionalClientUpdateS3Resourcess3ResourcesUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateS3Resourcess3ResourcesUpdateTypeDef",
    {"prefix": str},
    total=False,
)


class ClientUpdateS3Resourcess3ResourcesUpdateTypeDef(
    _RequiredClientUpdateS3Resourcess3ResourcesUpdateTypeDef,
    _OptionalClientUpdateS3Resourcess3ResourcesUpdateTypeDef,
):
    """
    Type definition for `ClientUpdateS3Resources` `s3ResourcesUpdate`

    The S3 resources whose classification types you want to update. This data type is used as a
    request parameter in the UpdateS3Resources action.

    - **bucketName** *(string) --* **[REQUIRED]**

      The name of the S3 bucket whose classification types you want to update.

    - **prefix** *(string) --*

      The prefix of the S3 bucket whose classification types you want to update.

    - **classificationTypeUpdate** *(dict) --* **[REQUIRED]**

      The classification type that you want to update for the resource associated with Amazon Macie.

      - **oneTime** *(string) --*

        A one-time classification of all of the existing objects in a specified S3 bucket.

      - **continuous** *(string) --*

        A continuous classification of the objects that are added to a specified S3 bucket. Amazon
        Macie begins performing continuous classification after a bucket is successfully associated
        with Amazon Macie.
    """


_ListMemberAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMemberAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMemberAccountsPaginatePaginationConfigTypeDef(
    _ListMemberAccountsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMemberAccountsPaginate` `PaginationConfig`

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


_ListMemberAccountsPaginateResponsememberAccountsTypeDef = TypedDict(
    "_ListMemberAccountsPaginateResponsememberAccountsTypeDef",
    {"accountId": str},
    total=False,
)


class ListMemberAccountsPaginateResponsememberAccountsTypeDef(
    _ListMemberAccountsPaginateResponsememberAccountsTypeDef
):
    """
    Type definition for `ListMemberAccountsPaginateResponse` `memberAccounts`

    Contains information about the Amazon Macie member account.

    - **accountId** *(string) --*

      The AWS account ID of the Amazon Macie member account.
    """


_ListMemberAccountsPaginateResponseTypeDef = TypedDict(
    "_ListMemberAccountsPaginateResponseTypeDef",
    {
        "memberAccounts": List[ListMemberAccountsPaginateResponsememberAccountsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListMemberAccountsPaginateResponseTypeDef(
    _ListMemberAccountsPaginateResponseTypeDef
):
    """
    Type definition for `ListMemberAccountsPaginate` `Response`

    - **memberAccounts** *(list) --*

      A list of the Amazon Macie member accounts returned by the action. The current master account
      is also included in this list.

      - *(dict) --*

        Contains information about the Amazon Macie member account.

        - **accountId** *(string) --*

          The AWS account ID of the Amazon Macie member account.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListS3ResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListS3ResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListS3ResourcesPaginatePaginationConfigTypeDef(
    _ListS3ResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListS3ResourcesPaginate` `PaginationConfig`

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


_ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef = TypedDict(
    "_ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef",
    {"oneTime": str, "continuous": str},
    total=False,
)


class ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef(
    _ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef
):
    """
    Type definition for `ListS3ResourcesPaginateResponses3Resources` `classificationType`

    The classification type that you want to specify for the resource associated with Amazon
    Macie.

    - **oneTime** *(string) --*

      A one-time classification of all of the existing objects in a specified S3 bucket.

    - **continuous** *(string) --*

      A continuous classification of the objects that are added to a specified S3 bucket.
      Amazon Macie begins performing continuous classification after a bucket is successfully
      associated with Amazon Macie.
    """


_ListS3ResourcesPaginateResponses3ResourcesTypeDef = TypedDict(
    "_ListS3ResourcesPaginateResponses3ResourcesTypeDef",
    {
        "bucketName": str,
        "prefix": str,
        "classificationType": ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)


class ListS3ResourcesPaginateResponses3ResourcesTypeDef(
    _ListS3ResourcesPaginateResponses3ResourcesTypeDef
):
    """
    Type definition for `ListS3ResourcesPaginateResponse` `s3Resources`

    The S3 resources that you want to associate with Amazon Macie for monitoring and data
    classification. This data type is used as a request parameter in the AssociateS3Resources
    action and a response parameter in the ListS3Resources action.

    - **bucketName** *(string) --*

      The name of the S3 bucket that you want to associate with Amazon Macie.

    - **prefix** *(string) --*

      The prefix of the S3 bucket that you want to associate with Amazon Macie.

    - **classificationType** *(dict) --*

      The classification type that you want to specify for the resource associated with Amazon
      Macie.

      - **oneTime** *(string) --*

        A one-time classification of all of the existing objects in a specified S3 bucket.

      - **continuous** *(string) --*

        A continuous classification of the objects that are added to a specified S3 bucket.
        Amazon Macie begins performing continuous classification after a bucket is successfully
        associated with Amazon Macie.
    """


_ListS3ResourcesPaginateResponseTypeDef = TypedDict(
    "_ListS3ResourcesPaginateResponseTypeDef",
    {
        "s3Resources": List[ListS3ResourcesPaginateResponses3ResourcesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListS3ResourcesPaginateResponseTypeDef(_ListS3ResourcesPaginateResponseTypeDef):
    """
    Type definition for `ListS3ResourcesPaginate` `Response`

    - **s3Resources** *(list) --*

      A list of the associated S3 resources returned by the action.

      - *(dict) --*

        The S3 resources that you want to associate with Amazon Macie for monitoring and data
        classification. This data type is used as a request parameter in the AssociateS3Resources
        action and a response parameter in the ListS3Resources action.

        - **bucketName** *(string) --*

          The name of the S3 bucket that you want to associate with Amazon Macie.

        - **prefix** *(string) --*

          The prefix of the S3 bucket that you want to associate with Amazon Macie.

        - **classificationType** *(dict) --*

          The classification type that you want to specify for the resource associated with Amazon
          Macie.

          - **oneTime** *(string) --*

            A one-time classification of all of the existing objects in a specified S3 bucket.

          - **continuous** *(string) --*

            A continuous classification of the objects that are added to a specified S3 bucket.
            Amazon Macie begins performing continuous classification after a bucket is successfully
            associated with Amazon Macie.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
