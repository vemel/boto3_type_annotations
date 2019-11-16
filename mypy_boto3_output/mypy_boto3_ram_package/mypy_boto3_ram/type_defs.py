"Main interface for ram type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    "ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef",
    "ClientAcceptResourceShareInvitationResponseTypeDef",
    "ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef",
    "ClientAssociateResourceShareResponseTypeDef",
    "ClientCreateResourceShareResponseresourceSharetagsTypeDef",
    "ClientCreateResourceShareResponseresourceShareTypeDef",
    "ClientCreateResourceShareResponseTypeDef",
    "ClientCreateResourceSharetagsTypeDef",
    "ClientDeleteResourceShareResponseTypeDef",
    "ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef",
    "ClientDisassociateResourceShareResponseTypeDef",
    "ClientEnableSharingWithAwsOrganizationResponseTypeDef",
    "ClientGetResourcePoliciesResponseTypeDef",
    "ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef",
    "ClientGetResourceShareAssociationsResponseTypeDef",
    "ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    "ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef",
    "ClientGetResourceShareInvitationsResponseTypeDef",
    "ClientGetResourceSharesResponseresourceSharestagsTypeDef",
    "ClientGetResourceSharesResponseresourceSharesTypeDef",
    "ClientGetResourceSharesResponseTypeDef",
    "ClientGetResourceSharestagFiltersTypeDef",
    "ClientListPendingInvitationResourcesResponseresourcesTypeDef",
    "ClientListPendingInvitationResourcesResponseTypeDef",
    "ClientListPrincipalsResponseprincipalsTypeDef",
    "ClientListPrincipalsResponseTypeDef",
    "ClientListResourcesResponseresourcesTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    "ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef",
    "ClientRejectResourceShareInvitationResponseTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUpdateResourceShareResponseresourceSharetagsTypeDef",
    "ClientUpdateResourceShareResponseresourceShareTypeDef",
    "ClientUpdateResourceShareResponseTypeDef",
    "GetResourcePoliciesPaginatePaginationConfigTypeDef",
    "GetResourcePoliciesPaginateResponseTypeDef",
    "GetResourceShareAssociationsPaginatePaginationConfigTypeDef",
    "GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef",
    "GetResourceShareAssociationsPaginateResponseTypeDef",
    "GetResourceShareInvitationsPaginatePaginationConfigTypeDef",
    "GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    "GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef",
    "GetResourceShareInvitationsPaginateResponseTypeDef",
    "GetResourceSharesPaginatePaginationConfigTypeDef",
    "GetResourceSharesPaginateResponseresourceSharestagsTypeDef",
    "GetResourceSharesPaginateResponseresourceSharesTypeDef",
    "GetResourceSharesPaginateResponseTypeDef",
    "GetResourceSharesPaginatetagFiltersTypeDef",
    "ListPrincipalsPaginatePaginationConfigTypeDef",
    "ListPrincipalsPaginateResponseprincipalsTypeDef",
    "ListPrincipalsPaginateResponseTypeDef",
    "ListResourcesPaginatePaginationConfigTypeDef",
    "ListResourcesPaginateResponseresourcesTypeDef",
    "ListResourcesPaginateResponseTypeDef",
)


_ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef = TypedDict(
    "_ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef(
    _ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
):
    """
    Type definition for `ClientAcceptResourceShareInvitationResponseresourceShareInvitation` `resourceShareAssociations`

    Describes an association with a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **associatedEntity** *(string) --*

      The associated entity. For resource associations, this is the ARN of the resource. For
      principal associations, this is the ID of an AWS account or the ARN of an OU or
      organization from AWS Organizations.

    - **associationType** *(string) --*

      The association type.

    - **status** *(string) --*

      The status of the association.

    - **statusMessage** *(string) --*

      A message about the status of the association.

    - **creationTime** *(datetime) --*

      The time when the association was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS account
      that owns the resource share.
    """


_ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef = TypedDict(
    "_ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": str,
        "resourceShareAssociations": List[
            ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)


class ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef(
    _ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef
):
    """
    Type definition for `ClientAcceptResourceShareInvitationResponse` `resourceShareInvitation`

    Information about the invitation.

    - **resourceShareInvitationArn** *(string) --*

      The Amazon Resource Name (ARN) of the invitation.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **senderAccountId** *(string) --*

      The ID of the AWS account that sent the invitation.

    - **receiverAccountId** *(string) --*

      The ID of the AWS account that received the invitation.

    - **invitationTimestamp** *(datetime) --*

      The date and time when the invitation was sent.

    - **status** *(string) --*

      The status of the invitation.

    - **resourceShareAssociations** *(list) --*

      To view the resources associated with a pending resource share invitation, use
      `ListPendingInvitationResources
      <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
      .

      - *(dict) --*

        Describes an association with a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **associatedEntity** *(string) --*

          The associated entity. For resource associations, this is the ARN of the resource. For
          principal associations, this is the ID of an AWS account or the ARN of an OU or
          organization from AWS Organizations.

        - **associationType** *(string) --*

          The association type.

        - **status** *(string) --*

          The status of the association.

        - **statusMessage** *(string) --*

          A message about the status of the association.

        - **creationTime** *(datetime) --*

          The time when the association was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS account
          that owns the resource share.
    """


_ClientAcceptResourceShareInvitationResponseTypeDef = TypedDict(
    "_ClientAcceptResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef,
        "clientToken": str,
    },
    total=False,
)


class ClientAcceptResourceShareInvitationResponseTypeDef(
    _ClientAcceptResourceShareInvitationResponseTypeDef
):
    """
    Type definition for `ClientAcceptResourceShareInvitation` `Response`

    - **resourceShareInvitation** *(dict) --*

      Information about the invitation.

      - **resourceShareInvitationArn** *(string) --*

        The Amazon Resource Name (ARN) of the invitation.

      - **resourceShareName** *(string) --*

        The name of the resource share.

      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.

      - **senderAccountId** *(string) --*

        The ID of the AWS account that sent the invitation.

      - **receiverAccountId** *(string) --*

        The ID of the AWS account that received the invitation.

      - **invitationTimestamp** *(datetime) --*

        The date and time when the invitation was sent.

      - **status** *(string) --*

        The status of the invitation.

      - **resourceShareAssociations** *(list) --*

        To view the resources associated with a pending resource share invitation, use
        `ListPendingInvitationResources
        <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
        .

        - *(dict) --*

          Describes an association with a resource share.

          - **resourceShareArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource share.

          - **resourceShareName** *(string) --*

            The name of the resource share.

          - **associatedEntity** *(string) --*

            The associated entity. For resource associations, this is the ARN of the resource. For
            principal associations, this is the ID of an AWS account or the ARN of an OU or
            organization from AWS Organizations.

          - **associationType** *(string) --*

            The association type.

          - **status** *(string) --*

            The status of the association.

          - **statusMessage** *(string) --*

            A message about the status of the association.

          - **creationTime** *(datetime) --*

            The time when the association was created.

          - **lastUpdatedTime** *(datetime) --*

            The time when the association was last updated.

          - **external** *(boolean) --*

            Indicates whether the principal belongs to the same AWS organization as the AWS account
            that owns the resource share.

    - **clientToken** *(string) --*

      A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    """


_ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef = TypedDict(
    "_ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef(
    _ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef
):
    """
    Type definition for `ClientAssociateResourceShareResponse` `resourceShareAssociations`

    Describes an association with a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **associatedEntity** *(string) --*

      The associated entity. For resource associations, this is the ARN of the resource. For
      principal associations, this is the ID of an AWS account or the ARN of an OU or
      organization from AWS Organizations.

    - **associationType** *(string) --*

      The association type.

    - **status** *(string) --*

      The status of the association.

    - **statusMessage** *(string) --*

      A message about the status of the association.

    - **creationTime** *(datetime) --*

      The time when the association was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS account
      that owns the resource share.
    """


_ClientAssociateResourceShareResponseTypeDef = TypedDict(
    "_ClientAssociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef
        ],
        "clientToken": str,
    },
    total=False,
)


class ClientAssociateResourceShareResponseTypeDef(
    _ClientAssociateResourceShareResponseTypeDef
):
    """
    Type definition for `ClientAssociateResourceShare` `Response`

    - **resourceShareAssociations** *(list) --*

      Information about the associations.

      - *(dict) --*

        Describes an association with a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **associatedEntity** *(string) --*

          The associated entity. For resource associations, this is the ARN of the resource. For
          principal associations, this is the ID of an AWS account or the ARN of an OU or
          organization from AWS Organizations.

        - **associationType** *(string) --*

          The association type.

        - **status** *(string) --*

          The status of the association.

        - **statusMessage** *(string) --*

          A message about the status of the association.

        - **creationTime** *(datetime) --*

          The time when the association was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS account
          that owns the resource share.

    - **clientToken** *(string) --*

      A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    """


_ClientCreateResourceShareResponseresourceSharetagsTypeDef = TypedDict(
    "_ClientCreateResourceShareResponseresourceSharetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateResourceShareResponseresourceSharetagsTypeDef(
    _ClientCreateResourceShareResponseresourceSharetagsTypeDef
):
    """
    Type definition for `ClientCreateResourceShareResponseresourceShare` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key of the tag.

    - **value** *(string) --*

      The value of the tag.
    """


_ClientCreateResourceShareResponseresourceShareTypeDef = TypedDict(
    "_ClientCreateResourceShareResponseresourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": str,
        "statusMessage": str,
        "tags": List[ClientCreateResourceShareResponseresourceSharetagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientCreateResourceShareResponseresourceShareTypeDef(
    _ClientCreateResourceShareResponseresourceShareTypeDef
):
    """
    Type definition for `ClientCreateResourceShareResponse` `resourceShare`

    Information about the resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **name** *(string) --*

      The name of the resource share.

    - **owningAccountId** *(string) --*

      The ID of the AWS account that owns the resource share.

    - **allowExternalPrincipals** *(boolean) --*

      Indicates whether principals outside your AWS organization can be associated with a
      resource share.

    - **status** *(string) --*

      The status of the resource share.

    - **statusMessage** *(string) --*

      A message about the status of the resource share.

    - **tags** *(list) --*

      The tags for the resource share.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key of the tag.

        - **value** *(string) --*

          The value of the tag.

    - **creationTime** *(datetime) --*

      The time when the resource share was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the resource share was last updated.
    """


_ClientCreateResourceShareResponseTypeDef = TypedDict(
    "_ClientCreateResourceShareResponseTypeDef",
    {
        "resourceShare": ClientCreateResourceShareResponseresourceShareTypeDef,
        "clientToken": str,
    },
    total=False,
)


class ClientCreateResourceShareResponseTypeDef(
    _ClientCreateResourceShareResponseTypeDef
):
    """
    Type definition for `ClientCreateResourceShare` `Response`

    - **resourceShare** *(dict) --*

      Information about the resource share.

      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.

      - **name** *(string) --*

        The name of the resource share.

      - **owningAccountId** *(string) --*

        The ID of the AWS account that owns the resource share.

      - **allowExternalPrincipals** *(boolean) --*

        Indicates whether principals outside your AWS organization can be associated with a
        resource share.

      - **status** *(string) --*

        The status of the resource share.

      - **statusMessage** *(string) --*

        A message about the status of the resource share.

      - **tags** *(list) --*

        The tags for the resource share.

        - *(dict) --*

          Information about a tag.

          - **key** *(string) --*

            The key of the tag.

          - **value** *(string) --*

            The value of the tag.

      - **creationTime** *(datetime) --*

        The time when the resource share was created.

      - **lastUpdatedTime** *(datetime) --*

        The time when the resource share was last updated.

    - **clientToken** *(string) --*

      A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    """


_ClientCreateResourceSharetagsTypeDef = TypedDict(
    "_ClientCreateResourceSharetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateResourceSharetagsTypeDef(_ClientCreateResourceSharetagsTypeDef):
    """
    Type definition for `ClientCreateResourceShare` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key of the tag.

    - **value** *(string) --*

      The value of the tag.
    """


_ClientDeleteResourceShareResponseTypeDef = TypedDict(
    "_ClientDeleteResourceShareResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)


class ClientDeleteResourceShareResponseTypeDef(
    _ClientDeleteResourceShareResponseTypeDef
):
    """
    Type definition for `ClientDeleteResourceShare` `Response`

    - **returnValue** *(boolean) --*

      Indicates whether the request succeeded.

    - **clientToken** *(string) --*

      A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    """


_ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef = TypedDict(
    "_ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef(
    _ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef
):
    """
    Type definition for `ClientDisassociateResourceShareResponse` `resourceShareAssociations`

    Describes an association with a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **associatedEntity** *(string) --*

      The associated entity. For resource associations, this is the ARN of the resource. For
      principal associations, this is the ID of an AWS account or the ARN of an OU or
      organization from AWS Organizations.

    - **associationType** *(string) --*

      The association type.

    - **status** *(string) --*

      The status of the association.

    - **statusMessage** *(string) --*

      A message about the status of the association.

    - **creationTime** *(datetime) --*

      The time when the association was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS account
      that owns the resource share.
    """


_ClientDisassociateResourceShareResponseTypeDef = TypedDict(
    "_ClientDisassociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef
        ],
        "clientToken": str,
    },
    total=False,
)


class ClientDisassociateResourceShareResponseTypeDef(
    _ClientDisassociateResourceShareResponseTypeDef
):
    """
    Type definition for `ClientDisassociateResourceShare` `Response`

    - **resourceShareAssociations** *(list) --*

      Information about the associations.

      - *(dict) --*

        Describes an association with a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **associatedEntity** *(string) --*

          The associated entity. For resource associations, this is the ARN of the resource. For
          principal associations, this is the ID of an AWS account or the ARN of an OU or
          organization from AWS Organizations.

        - **associationType** *(string) --*

          The association type.

        - **status** *(string) --*

          The status of the association.

        - **statusMessage** *(string) --*

          A message about the status of the association.

        - **creationTime** *(datetime) --*

          The time when the association was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS account
          that owns the resource share.

    - **clientToken** *(string) --*

      A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    """


_ClientEnableSharingWithAwsOrganizationResponseTypeDef = TypedDict(
    "_ClientEnableSharingWithAwsOrganizationResponseTypeDef",
    {"returnValue": bool},
    total=False,
)


class ClientEnableSharingWithAwsOrganizationResponseTypeDef(
    _ClientEnableSharingWithAwsOrganizationResponseTypeDef
):
    """
    Type definition for `ClientEnableSharingWithAwsOrganization` `Response`

    - **returnValue** *(boolean) --*

      Indicates whether the request succeeded.
    """


_ClientGetResourcePoliciesResponseTypeDef = TypedDict(
    "_ClientGetResourcePoliciesResponseTypeDef",
    {"policies": List[str], "nextToken": str},
    total=False,
)


class ClientGetResourcePoliciesResponseTypeDef(
    _ClientGetResourcePoliciesResponseTypeDef
):
    """
    Type definition for `ClientGetResourcePolicies` `Response`

    - **policies** *(list) --*

      A key policy document, in JSON format.

      - *(string) --*

    - **nextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is ``null`` when there are
      no more results to return.
    """


_ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef = TypedDict(
    "_ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef(
    _ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef
):
    """
    Type definition for `ClientGetResourceShareAssociationsResponse` `resourceShareAssociations`

    Describes an association with a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **associatedEntity** *(string) --*

      The associated entity. For resource associations, this is the ARN of the resource. For
      principal associations, this is the ID of an AWS account or the ARN of an OU or
      organization from AWS Organizations.

    - **associationType** *(string) --*

      The association type.

    - **status** *(string) --*

      The status of the association.

    - **statusMessage** *(string) --*

      A message about the status of the association.

    - **creationTime** *(datetime) --*

      The time when the association was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS account
      that owns the resource share.
    """


_ClientGetResourceShareAssociationsResponseTypeDef = TypedDict(
    "_ClientGetResourceShareAssociationsResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetResourceShareAssociationsResponseTypeDef(
    _ClientGetResourceShareAssociationsResponseTypeDef
):
    """
    Type definition for `ClientGetResourceShareAssociations` `Response`

    - **resourceShareAssociations** *(list) --*

      Information about the associations.

      - *(dict) --*

        Describes an association with a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **associatedEntity** *(string) --*

          The associated entity. For resource associations, this is the ARN of the resource. For
          principal associations, this is the ID of an AWS account or the ARN of an OU or
          organization from AWS Organizations.

        - **associationType** *(string) --*

          The association type.

        - **status** *(string) --*

          The status of the association.

        - **statusMessage** *(string) --*

          A message about the status of the association.

        - **creationTime** *(datetime) --*

          The time when the association was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS account
          that owns the resource share.

    - **nextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is ``null`` when there are
      no more results to return.
    """


_ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef = TypedDict(
    "_ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef(
    _ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef
):
    """
    Type definition for `ClientGetResourceShareInvitationsResponseresourceShareInvitations` `resourceShareAssociations`

    Describes an association with a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **associatedEntity** *(string) --*

      The associated entity. For resource associations, this is the ARN of the resource.
      For principal associations, this is the ID of an AWS account or the ARN of an OU or
      organization from AWS Organizations.

    - **associationType** *(string) --*

      The association type.

    - **status** *(string) --*

      The status of the association.

    - **statusMessage** *(string) --*

      A message about the status of the association.

    - **creationTime** *(datetime) --*

      The time when the association was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS
      account that owns the resource share.
    """


_ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef = TypedDict(
    "_ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": str,
        "resourceShareAssociations": List[
            ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)


class ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef(
    _ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef
):
    """
    Type definition for `ClientGetResourceShareInvitationsResponse` `resourceShareInvitations`

    Describes an invitation to join a resource share.

    - **resourceShareInvitationArn** *(string) --*

      The Amazon Resource Name (ARN) of the invitation.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **senderAccountId** *(string) --*

      The ID of the AWS account that sent the invitation.

    - **receiverAccountId** *(string) --*

      The ID of the AWS account that received the invitation.

    - **invitationTimestamp** *(datetime) --*

      The date and time when the invitation was sent.

    - **status** *(string) --*

      The status of the invitation.

    - **resourceShareAssociations** *(list) --*

      To view the resources associated with a pending resource share invitation, use
      `ListPendingInvitationResources
      <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
      .

      - *(dict) --*

        Describes an association with a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **associatedEntity** *(string) --*

          The associated entity. For resource associations, this is the ARN of the resource.
          For principal associations, this is the ID of an AWS account or the ARN of an OU or
          organization from AWS Organizations.

        - **associationType** *(string) --*

          The association type.

        - **status** *(string) --*

          The status of the association.

        - **statusMessage** *(string) --*

          A message about the status of the association.

        - **creationTime** *(datetime) --*

          The time when the association was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS
          account that owns the resource share.
    """


_ClientGetResourceShareInvitationsResponseTypeDef = TypedDict(
    "_ClientGetResourceShareInvitationsResponseTypeDef",
    {
        "resourceShareInvitations": List[
            ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetResourceShareInvitationsResponseTypeDef(
    _ClientGetResourceShareInvitationsResponseTypeDef
):
    """
    Type definition for `ClientGetResourceShareInvitations` `Response`

    - **resourceShareInvitations** *(list) --*

      Information about the invitations.

      - *(dict) --*

        Describes an invitation to join a resource share.

        - **resourceShareInvitationArn** *(string) --*

          The Amazon Resource Name (ARN) of the invitation.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **senderAccountId** *(string) --*

          The ID of the AWS account that sent the invitation.

        - **receiverAccountId** *(string) --*

          The ID of the AWS account that received the invitation.

        - **invitationTimestamp** *(datetime) --*

          The date and time when the invitation was sent.

        - **status** *(string) --*

          The status of the invitation.

        - **resourceShareAssociations** *(list) --*

          To view the resources associated with a pending resource share invitation, use
          `ListPendingInvitationResources
          <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
          .

          - *(dict) --*

            Describes an association with a resource share.

            - **resourceShareArn** *(string) --*

              The Amazon Resource Name (ARN) of the resource share.

            - **resourceShareName** *(string) --*

              The name of the resource share.

            - **associatedEntity** *(string) --*

              The associated entity. For resource associations, this is the ARN of the resource.
              For principal associations, this is the ID of an AWS account or the ARN of an OU or
              organization from AWS Organizations.

            - **associationType** *(string) --*

              The association type.

            - **status** *(string) --*

              The status of the association.

            - **statusMessage** *(string) --*

              A message about the status of the association.

            - **creationTime** *(datetime) --*

              The time when the association was created.

            - **lastUpdatedTime** *(datetime) --*

              The time when the association was last updated.

            - **external** *(boolean) --*

              Indicates whether the principal belongs to the same AWS organization as the AWS
              account that owns the resource share.

    - **nextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is ``null`` when there are
      no more results to return.
    """


_ClientGetResourceSharesResponseresourceSharestagsTypeDef = TypedDict(
    "_ClientGetResourceSharesResponseresourceSharestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetResourceSharesResponseresourceSharestagsTypeDef(
    _ClientGetResourceSharesResponseresourceSharestagsTypeDef
):
    """
    Type definition for `ClientGetResourceSharesResponseresourceShares` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key of the tag.

    - **value** *(string) --*

      The value of the tag.
    """


_ClientGetResourceSharesResponseresourceSharesTypeDef = TypedDict(
    "_ClientGetResourceSharesResponseresourceSharesTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": str,
        "statusMessage": str,
        "tags": List[ClientGetResourceSharesResponseresourceSharestagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientGetResourceSharesResponseresourceSharesTypeDef(
    _ClientGetResourceSharesResponseresourceSharesTypeDef
):
    """
    Type definition for `ClientGetResourceSharesResponse` `resourceShares`

    Describes a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **name** *(string) --*

      The name of the resource share.

    - **owningAccountId** *(string) --*

      The ID of the AWS account that owns the resource share.

    - **allowExternalPrincipals** *(boolean) --*

      Indicates whether principals outside your AWS organization can be associated with a
      resource share.

    - **status** *(string) --*

      The status of the resource share.

    - **statusMessage** *(string) --*

      A message about the status of the resource share.

    - **tags** *(list) --*

      The tags for the resource share.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key of the tag.

        - **value** *(string) --*

          The value of the tag.

    - **creationTime** *(datetime) --*

      The time when the resource share was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the resource share was last updated.
    """


_ClientGetResourceSharesResponseTypeDef = TypedDict(
    "_ClientGetResourceSharesResponseTypeDef",
    {
        "resourceShares": List[ClientGetResourceSharesResponseresourceSharesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetResourceSharesResponseTypeDef(_ClientGetResourceSharesResponseTypeDef):
    """
    Type definition for `ClientGetResourceShares` `Response`

    - **resourceShares** *(list) --*

      Information about the resource shares.

      - *(dict) --*

        Describes a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **name** *(string) --*

          The name of the resource share.

        - **owningAccountId** *(string) --*

          The ID of the AWS account that owns the resource share.

        - **allowExternalPrincipals** *(boolean) --*

          Indicates whether principals outside your AWS organization can be associated with a
          resource share.

        - **status** *(string) --*

          The status of the resource share.

        - **statusMessage** *(string) --*

          A message about the status of the resource share.

        - **tags** *(list) --*

          The tags for the resource share.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key of the tag.

            - **value** *(string) --*

              The value of the tag.

        - **creationTime** *(datetime) --*

          The time when the resource share was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the resource share was last updated.

    - **nextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is ``null`` when there are
      no more results to return.
    """


_ClientGetResourceSharestagFiltersTypeDef = TypedDict(
    "_ClientGetResourceSharestagFiltersTypeDef",
    {"tagKey": str, "tagValues": List[str]},
    total=False,
)


class ClientGetResourceSharestagFiltersTypeDef(
    _ClientGetResourceSharestagFiltersTypeDef
):
    """
    Type definition for `ClientGetResourceShares` `tagFilters`

    Used to filter information based on tags.

    - **tagKey** *(string) --*

      The tag key.

    - **tagValues** *(list) --*

      The tag values.

      - *(string) --*
    """


_ClientListPendingInvitationResourcesResponseresourcesTypeDef = TypedDict(
    "_ClientListPendingInvitationResourcesResponseresourcesTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientListPendingInvitationResourcesResponseresourcesTypeDef(
    _ClientListPendingInvitationResourcesResponseresourcesTypeDef
):
    """
    Type definition for `ClientListPendingInvitationResourcesResponse` `resources`

    Describes a resource associated with a resource share.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **type** *(string) --*

      The resource type.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **status** *(string) --*

      The status of the resource.

    - **statusMessage** *(string) --*

      A message about the status of the resource.

    - **creationTime** *(datetime) --*

      The time when the resource was associated with the resource share.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.
    """


_ClientListPendingInvitationResourcesResponseTypeDef = TypedDict(
    "_ClientListPendingInvitationResourcesResponseTypeDef",
    {
        "resources": List[ClientListPendingInvitationResourcesResponseresourcesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListPendingInvitationResourcesResponseTypeDef(
    _ClientListPendingInvitationResourcesResponseTypeDef
):
    """
    Type definition for `ClientListPendingInvitationResources` `Response`

    - **resources** *(list) --*

      Information about the resources included the resource share.

      - *(dict) --*

        Describes a resource associated with a resource share.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

        - **type** *(string) --*

          The resource type.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **status** *(string) --*

          The status of the resource.

        - **statusMessage** *(string) --*

          A message about the status of the resource.

        - **creationTime** *(datetime) --*

          The time when the resource was associated with the resource share.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

    - **nextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is ``null`` when there are
      no more results to return.
    """


_ClientListPrincipalsResponseprincipalsTypeDef = TypedDict(
    "_ClientListPrincipalsResponseprincipalsTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientListPrincipalsResponseprincipalsTypeDef(
    _ClientListPrincipalsResponseprincipalsTypeDef
):
    """
    Type definition for `ClientListPrincipalsResponse` `principals`

    Describes a principal for use with AWS Resource Access Manager.

    - **id** *(string) --*

      The ID of the principal.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **creationTime** *(datetime) --*

      The time when the principal was associated with the resource share.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS account
      that owns the resource share.
    """


_ClientListPrincipalsResponseTypeDef = TypedDict(
    "_ClientListPrincipalsResponseTypeDef",
    {
        "principals": List[ClientListPrincipalsResponseprincipalsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListPrincipalsResponseTypeDef(_ClientListPrincipalsResponseTypeDef):
    """
    Type definition for `ClientListPrincipals` `Response`

    - **principals** *(list) --*

      The principals.

      - *(dict) --*

        Describes a principal for use with AWS Resource Access Manager.

        - **id** *(string) --*

          The ID of the principal.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **creationTime** *(datetime) --*

          The time when the principal was associated with the resource share.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS account
          that owns the resource share.

    - **nextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is ``null`` when there are
      no more results to return.
    """


_ClientListResourcesResponseresourcesTypeDef = TypedDict(
    "_ClientListResourcesResponseresourcesTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientListResourcesResponseresourcesTypeDef(
    _ClientListResourcesResponseresourcesTypeDef
):
    """
    Type definition for `ClientListResourcesResponse` `resources`

    Describes a resource associated with a resource share.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **type** *(string) --*

      The resource type.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **status** *(string) --*

      The status of the resource.

    - **statusMessage** *(string) --*

      A message about the status of the resource.

    - **creationTime** *(datetime) --*

      The time when the resource was associated with the resource share.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.
    """


_ClientListResourcesResponseTypeDef = TypedDict(
    "_ClientListResourcesResponseTypeDef",
    {"resources": List[ClientListResourcesResponseresourcesTypeDef], "nextToken": str},
    total=False,
)


class ClientListResourcesResponseTypeDef(_ClientListResourcesResponseTypeDef):
    """
    Type definition for `ClientListResources` `Response`

    - **resources** *(list) --*

      Information about the resources.

      - *(dict) --*

        Describes a resource associated with a resource share.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

        - **type** *(string) --*

          The resource type.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **status** *(string) --*

          The status of the resource.

        - **statusMessage** *(string) --*

          A message about the status of the resource.

        - **creationTime** *(datetime) --*

          The time when the resource was associated with the resource share.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

    - **nextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is ``null`` when there are
      no more results to return.
    """


_ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef = TypedDict(
    "_ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef(
    _ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
):
    """
    Type definition for `ClientRejectResourceShareInvitationResponseresourceShareInvitation` `resourceShareAssociations`

    Describes an association with a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **associatedEntity** *(string) --*

      The associated entity. For resource associations, this is the ARN of the resource. For
      principal associations, this is the ID of an AWS account or the ARN of an OU or
      organization from AWS Organizations.

    - **associationType** *(string) --*

      The association type.

    - **status** *(string) --*

      The status of the association.

    - **statusMessage** *(string) --*

      A message about the status of the association.

    - **creationTime** *(datetime) --*

      The time when the association was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS account
      that owns the resource share.
    """


_ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef = TypedDict(
    "_ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": str,
        "resourceShareAssociations": List[
            ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)


class ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef(
    _ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef
):
    """
    Type definition for `ClientRejectResourceShareInvitationResponse` `resourceShareInvitation`

    Information about the invitation.

    - **resourceShareInvitationArn** *(string) --*

      The Amazon Resource Name (ARN) of the invitation.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **senderAccountId** *(string) --*

      The ID of the AWS account that sent the invitation.

    - **receiverAccountId** *(string) --*

      The ID of the AWS account that received the invitation.

    - **invitationTimestamp** *(datetime) --*

      The date and time when the invitation was sent.

    - **status** *(string) --*

      The status of the invitation.

    - **resourceShareAssociations** *(list) --*

      To view the resources associated with a pending resource share invitation, use
      `ListPendingInvitationResources
      <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
      .

      - *(dict) --*

        Describes an association with a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **associatedEntity** *(string) --*

          The associated entity. For resource associations, this is the ARN of the resource. For
          principal associations, this is the ID of an AWS account or the ARN of an OU or
          organization from AWS Organizations.

        - **associationType** *(string) --*

          The association type.

        - **status** *(string) --*

          The status of the association.

        - **statusMessage** *(string) --*

          A message about the status of the association.

        - **creationTime** *(datetime) --*

          The time when the association was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS account
          that owns the resource share.
    """


_ClientRejectResourceShareInvitationResponseTypeDef = TypedDict(
    "_ClientRejectResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef,
        "clientToken": str,
    },
    total=False,
)


class ClientRejectResourceShareInvitationResponseTypeDef(
    _ClientRejectResourceShareInvitationResponseTypeDef
):
    """
    Type definition for `ClientRejectResourceShareInvitation` `Response`

    - **resourceShareInvitation** *(dict) --*

      Information about the invitation.

      - **resourceShareInvitationArn** *(string) --*

        The Amazon Resource Name (ARN) of the invitation.

      - **resourceShareName** *(string) --*

        The name of the resource share.

      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.

      - **senderAccountId** *(string) --*

        The ID of the AWS account that sent the invitation.

      - **receiverAccountId** *(string) --*

        The ID of the AWS account that received the invitation.

      - **invitationTimestamp** *(datetime) --*

        The date and time when the invitation was sent.

      - **status** *(string) --*

        The status of the invitation.

      - **resourceShareAssociations** *(list) --*

        To view the resources associated with a pending resource share invitation, use
        `ListPendingInvitationResources
        <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
        .

        - *(dict) --*

          Describes an association with a resource share.

          - **resourceShareArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource share.

          - **resourceShareName** *(string) --*

            The name of the resource share.

          - **associatedEntity** *(string) --*

            The associated entity. For resource associations, this is the ARN of the resource. For
            principal associations, this is the ID of an AWS account or the ARN of an OU or
            organization from AWS Organizations.

          - **associationType** *(string) --*

            The association type.

          - **status** *(string) --*

            The status of the association.

          - **statusMessage** *(string) --*

            A message about the status of the association.

          - **creationTime** *(datetime) --*

            The time when the association was created.

          - **lastUpdatedTime** *(datetime) --*

            The time when the association was last updated.

          - **external** *(boolean) --*

            Indicates whether the principal belongs to the same AWS organization as the AWS account
            that owns the resource share.

    - **clientToken** *(string) --*

      A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    """


_ClientTagResourcetagsTypeDef = TypedDict(
    "_ClientTagResourcetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientTagResourcetagsTypeDef(_ClientTagResourcetagsTypeDef):
    """
    Type definition for `ClientTagResource` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key of the tag.

    - **value** *(string) --*

      The value of the tag.
    """


_ClientUpdateResourceShareResponseresourceSharetagsTypeDef = TypedDict(
    "_ClientUpdateResourceShareResponseresourceSharetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateResourceShareResponseresourceSharetagsTypeDef(
    _ClientUpdateResourceShareResponseresourceSharetagsTypeDef
):
    """
    Type definition for `ClientUpdateResourceShareResponseresourceShare` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key of the tag.

    - **value** *(string) --*

      The value of the tag.
    """


_ClientUpdateResourceShareResponseresourceShareTypeDef = TypedDict(
    "_ClientUpdateResourceShareResponseresourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": str,
        "statusMessage": str,
        "tags": List[ClientUpdateResourceShareResponseresourceSharetagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientUpdateResourceShareResponseresourceShareTypeDef(
    _ClientUpdateResourceShareResponseresourceShareTypeDef
):
    """
    Type definition for `ClientUpdateResourceShareResponse` `resourceShare`

    Information about the resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **name** *(string) --*

      The name of the resource share.

    - **owningAccountId** *(string) --*

      The ID of the AWS account that owns the resource share.

    - **allowExternalPrincipals** *(boolean) --*

      Indicates whether principals outside your AWS organization can be associated with a
      resource share.

    - **status** *(string) --*

      The status of the resource share.

    - **statusMessage** *(string) --*

      A message about the status of the resource share.

    - **tags** *(list) --*

      The tags for the resource share.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key of the tag.

        - **value** *(string) --*

          The value of the tag.

    - **creationTime** *(datetime) --*

      The time when the resource share was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the resource share was last updated.
    """


_ClientUpdateResourceShareResponseTypeDef = TypedDict(
    "_ClientUpdateResourceShareResponseTypeDef",
    {
        "resourceShare": ClientUpdateResourceShareResponseresourceShareTypeDef,
        "clientToken": str,
    },
    total=False,
)


class ClientUpdateResourceShareResponseTypeDef(
    _ClientUpdateResourceShareResponseTypeDef
):
    """
    Type definition for `ClientUpdateResourceShare` `Response`

    - **resourceShare** *(dict) --*

      Information about the resource share.

      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.

      - **name** *(string) --*

        The name of the resource share.

      - **owningAccountId** *(string) --*

        The ID of the AWS account that owns the resource share.

      - **allowExternalPrincipals** *(boolean) --*

        Indicates whether principals outside your AWS organization can be associated with a
        resource share.

      - **status** *(string) --*

        The status of the resource share.

      - **statusMessage** *(string) --*

        A message about the status of the resource share.

      - **tags** *(list) --*

        The tags for the resource share.

        - *(dict) --*

          Information about a tag.

          - **key** *(string) --*

            The key of the tag.

          - **value** *(string) --*

            The value of the tag.

      - **creationTime** *(datetime) --*

        The time when the resource share was created.

      - **lastUpdatedTime** *(datetime) --*

        The time when the resource share was last updated.

    - **clientToken** *(string) --*

      A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    """


_GetResourcePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourcePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourcePoliciesPaginatePaginationConfigTypeDef(
    _GetResourcePoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetResourcePoliciesPaginate` `PaginationConfig`

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


_GetResourcePoliciesPaginateResponseTypeDef = TypedDict(
    "_GetResourcePoliciesPaginateResponseTypeDef",
    {"policies": List[str], "NextToken": str},
    total=False,
)


class GetResourcePoliciesPaginateResponseTypeDef(
    _GetResourcePoliciesPaginateResponseTypeDef
):
    """
    Type definition for `GetResourcePoliciesPaginate` `Response`

    - **policies** *(list) --*

      A key policy document, in JSON format.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetResourceShareAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourceShareAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourceShareAssociationsPaginatePaginationConfigTypeDef(
    _GetResourceShareAssociationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetResourceShareAssociationsPaginate` `PaginationConfig`

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


_GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef = TypedDict(
    "_GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef(
    _GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef
):
    """
    Type definition for `GetResourceShareAssociationsPaginateResponse` `resourceShareAssociations`

    Describes an association with a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **associatedEntity** *(string) --*

      The associated entity. For resource associations, this is the ARN of the resource. For
      principal associations, this is the ID of an AWS account or the ARN of an OU or
      organization from AWS Organizations.

    - **associationType** *(string) --*

      The association type.

    - **status** *(string) --*

      The status of the association.

    - **statusMessage** *(string) --*

      A message about the status of the association.

    - **creationTime** *(datetime) --*

      The time when the association was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS account
      that owns the resource share.
    """


_GetResourceShareAssociationsPaginateResponseTypeDef = TypedDict(
    "_GetResourceShareAssociationsPaginateResponseTypeDef",
    {
        "resourceShareAssociations": List[
            GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetResourceShareAssociationsPaginateResponseTypeDef(
    _GetResourceShareAssociationsPaginateResponseTypeDef
):
    """
    Type definition for `GetResourceShareAssociationsPaginate` `Response`

    - **resourceShareAssociations** *(list) --*

      Information about the associations.

      - *(dict) --*

        Describes an association with a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **associatedEntity** *(string) --*

          The associated entity. For resource associations, this is the ARN of the resource. For
          principal associations, this is the ID of an AWS account or the ARN of an OU or
          organization from AWS Organizations.

        - **associationType** *(string) --*

          The association type.

        - **status** *(string) --*

          The status of the association.

        - **statusMessage** *(string) --*

          A message about the status of the association.

        - **creationTime** *(datetime) --*

          The time when the association was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS account
          that owns the resource share.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetResourceShareInvitationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourceShareInvitationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourceShareInvitationsPaginatePaginationConfigTypeDef(
    _GetResourceShareInvitationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetResourceShareInvitationsPaginate` `PaginationConfig`

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


_GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef = TypedDict(
    "_GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef(
    _GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef
):
    """
    Type definition for `GetResourceShareInvitationsPaginateResponseresourceShareInvitations` `resourceShareAssociations`

    Describes an association with a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **associatedEntity** *(string) --*

      The associated entity. For resource associations, this is the ARN of the resource.
      For principal associations, this is the ID of an AWS account or the ARN of an OU or
      organization from AWS Organizations.

    - **associationType** *(string) --*

      The association type.

    - **status** *(string) --*

      The status of the association.

    - **statusMessage** *(string) --*

      A message about the status of the association.

    - **creationTime** *(datetime) --*

      The time when the association was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS
      account that owns the resource share.
    """


_GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef = TypedDict(
    "_GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": str,
        "resourceShareAssociations": List[
            GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)


class GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef(
    _GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef
):
    """
    Type definition for `GetResourceShareInvitationsPaginateResponse` `resourceShareInvitations`

    Describes an invitation to join a resource share.

    - **resourceShareInvitationArn** *(string) --*

      The Amazon Resource Name (ARN) of the invitation.

    - **resourceShareName** *(string) --*

      The name of the resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **senderAccountId** *(string) --*

      The ID of the AWS account that sent the invitation.

    - **receiverAccountId** *(string) --*

      The ID of the AWS account that received the invitation.

    - **invitationTimestamp** *(datetime) --*

      The date and time when the invitation was sent.

    - **status** *(string) --*

      The status of the invitation.

    - **resourceShareAssociations** *(list) --*

      To view the resources associated with a pending resource share invitation, use
      `ListPendingInvitationResources
      <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
      .

      - *(dict) --*

        Describes an association with a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **associatedEntity** *(string) --*

          The associated entity. For resource associations, this is the ARN of the resource.
          For principal associations, this is the ID of an AWS account or the ARN of an OU or
          organization from AWS Organizations.

        - **associationType** *(string) --*

          The association type.

        - **status** *(string) --*

          The status of the association.

        - **statusMessage** *(string) --*

          A message about the status of the association.

        - **creationTime** *(datetime) --*

          The time when the association was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS
          account that owns the resource share.
    """


_GetResourceShareInvitationsPaginateResponseTypeDef = TypedDict(
    "_GetResourceShareInvitationsPaginateResponseTypeDef",
    {
        "resourceShareInvitations": List[
            GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetResourceShareInvitationsPaginateResponseTypeDef(
    _GetResourceShareInvitationsPaginateResponseTypeDef
):
    """
    Type definition for `GetResourceShareInvitationsPaginate` `Response`

    - **resourceShareInvitations** *(list) --*

      Information about the invitations.

      - *(dict) --*

        Describes an invitation to join a resource share.

        - **resourceShareInvitationArn** *(string) --*

          The Amazon Resource Name (ARN) of the invitation.

        - **resourceShareName** *(string) --*

          The name of the resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **senderAccountId** *(string) --*

          The ID of the AWS account that sent the invitation.

        - **receiverAccountId** *(string) --*

          The ID of the AWS account that received the invitation.

        - **invitationTimestamp** *(datetime) --*

          The date and time when the invitation was sent.

        - **status** *(string) --*

          The status of the invitation.

        - **resourceShareAssociations** *(list) --*

          To view the resources associated with a pending resource share invitation, use
          `ListPendingInvitationResources
          <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
          .

          - *(dict) --*

            Describes an association with a resource share.

            - **resourceShareArn** *(string) --*

              The Amazon Resource Name (ARN) of the resource share.

            - **resourceShareName** *(string) --*

              The name of the resource share.

            - **associatedEntity** *(string) --*

              The associated entity. For resource associations, this is the ARN of the resource.
              For principal associations, this is the ID of an AWS account or the ARN of an OU or
              organization from AWS Organizations.

            - **associationType** *(string) --*

              The association type.

            - **status** *(string) --*

              The status of the association.

            - **statusMessage** *(string) --*

              A message about the status of the association.

            - **creationTime** *(datetime) --*

              The time when the association was created.

            - **lastUpdatedTime** *(datetime) --*

              The time when the association was last updated.

            - **external** *(boolean) --*

              Indicates whether the principal belongs to the same AWS organization as the AWS
              account that owns the resource share.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetResourceSharesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourceSharesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourceSharesPaginatePaginationConfigTypeDef(
    _GetResourceSharesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetResourceSharesPaginate` `PaginationConfig`

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


_GetResourceSharesPaginateResponseresourceSharestagsTypeDef = TypedDict(
    "_GetResourceSharesPaginateResponseresourceSharestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetResourceSharesPaginateResponseresourceSharestagsTypeDef(
    _GetResourceSharesPaginateResponseresourceSharestagsTypeDef
):
    """
    Type definition for `GetResourceSharesPaginateResponseresourceShares` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key of the tag.

    - **value** *(string) --*

      The value of the tag.
    """


_GetResourceSharesPaginateResponseresourceSharesTypeDef = TypedDict(
    "_GetResourceSharesPaginateResponseresourceSharesTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": str,
        "statusMessage": str,
        "tags": List[GetResourceSharesPaginateResponseresourceSharestagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class GetResourceSharesPaginateResponseresourceSharesTypeDef(
    _GetResourceSharesPaginateResponseresourceSharesTypeDef
):
    """
    Type definition for `GetResourceSharesPaginateResponse` `resourceShares`

    Describes a resource share.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **name** *(string) --*

      The name of the resource share.

    - **owningAccountId** *(string) --*

      The ID of the AWS account that owns the resource share.

    - **allowExternalPrincipals** *(boolean) --*

      Indicates whether principals outside your AWS organization can be associated with a
      resource share.

    - **status** *(string) --*

      The status of the resource share.

    - **statusMessage** *(string) --*

      A message about the status of the resource share.

    - **tags** *(list) --*

      The tags for the resource share.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key of the tag.

        - **value** *(string) --*

          The value of the tag.

    - **creationTime** *(datetime) --*

      The time when the resource share was created.

    - **lastUpdatedTime** *(datetime) --*

      The time when the resource share was last updated.
    """


_GetResourceSharesPaginateResponseTypeDef = TypedDict(
    "_GetResourceSharesPaginateResponseTypeDef",
    {
        "resourceShares": List[GetResourceSharesPaginateResponseresourceSharesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetResourceSharesPaginateResponseTypeDef(
    _GetResourceSharesPaginateResponseTypeDef
):
    """
    Type definition for `GetResourceSharesPaginate` `Response`

    - **resourceShares** *(list) --*

      Information about the resource shares.

      - *(dict) --*

        Describes a resource share.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **name** *(string) --*

          The name of the resource share.

        - **owningAccountId** *(string) --*

          The ID of the AWS account that owns the resource share.

        - **allowExternalPrincipals** *(boolean) --*

          Indicates whether principals outside your AWS organization can be associated with a
          resource share.

        - **status** *(string) --*

          The status of the resource share.

        - **statusMessage** *(string) --*

          A message about the status of the resource share.

        - **tags** *(list) --*

          The tags for the resource share.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key of the tag.

            - **value** *(string) --*

              The value of the tag.

        - **creationTime** *(datetime) --*

          The time when the resource share was created.

        - **lastUpdatedTime** *(datetime) --*

          The time when the resource share was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetResourceSharesPaginatetagFiltersTypeDef = TypedDict(
    "_GetResourceSharesPaginatetagFiltersTypeDef",
    {"tagKey": str, "tagValues": List[str]},
    total=False,
)


class GetResourceSharesPaginatetagFiltersTypeDef(
    _GetResourceSharesPaginatetagFiltersTypeDef
):
    """
    Type definition for `GetResourceSharesPaginate` `tagFilters`

    Used to filter information based on tags.

    - **tagKey** *(string) --*

      The tag key.

    - **tagValues** *(list) --*

      The tag values.

      - *(string) --*
    """


_ListPrincipalsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPrincipalsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPrincipalsPaginatePaginationConfigTypeDef(
    _ListPrincipalsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPrincipalsPaginate` `PaginationConfig`

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


_ListPrincipalsPaginateResponseprincipalsTypeDef = TypedDict(
    "_ListPrincipalsPaginateResponseprincipalsTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ListPrincipalsPaginateResponseprincipalsTypeDef(
    _ListPrincipalsPaginateResponseprincipalsTypeDef
):
    """
    Type definition for `ListPrincipalsPaginateResponse` `principals`

    Describes a principal for use with AWS Resource Access Manager.

    - **id** *(string) --*

      The ID of the principal.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **creationTime** *(datetime) --*

      The time when the principal was associated with the resource share.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.

    - **external** *(boolean) --*

      Indicates whether the principal belongs to the same AWS organization as the AWS account
      that owns the resource share.
    """


_ListPrincipalsPaginateResponseTypeDef = TypedDict(
    "_ListPrincipalsPaginateResponseTypeDef",
    {
        "principals": List[ListPrincipalsPaginateResponseprincipalsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPrincipalsPaginateResponseTypeDef(_ListPrincipalsPaginateResponseTypeDef):
    """
    Type definition for `ListPrincipalsPaginate` `Response`

    - **principals** *(list) --*

      The principals.

      - *(dict) --*

        Describes a principal for use with AWS Resource Access Manager.

        - **id** *(string) --*

          The ID of the principal.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **creationTime** *(datetime) --*

          The time when the principal was associated with the resource share.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

        - **external** *(boolean) --*

          Indicates whether the principal belongs to the same AWS organization as the AWS account
          that owns the resource share.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourcesPaginatePaginationConfigTypeDef(
    _ListResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourcesPaginate` `PaginationConfig`

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


_ListResourcesPaginateResponseresourcesTypeDef = TypedDict(
    "_ListResourcesPaginateResponseresourcesTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "status": str,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ListResourcesPaginateResponseresourcesTypeDef(
    _ListResourcesPaginateResponseresourcesTypeDef
):
    """
    Type definition for `ListResourcesPaginateResponse` `resources`

    Describes a resource associated with a resource share.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **type** *(string) --*

      The resource type.

    - **resourceShareArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource share.

    - **status** *(string) --*

      The status of the resource.

    - **statusMessage** *(string) --*

      A message about the status of the resource.

    - **creationTime** *(datetime) --*

      The time when the resource was associated with the resource share.

    - **lastUpdatedTime** *(datetime) --*

      The time when the association was last updated.
    """


_ListResourcesPaginateResponseTypeDef = TypedDict(
    "_ListResourcesPaginateResponseTypeDef",
    {
        "resources": List[ListResourcesPaginateResponseresourcesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListResourcesPaginateResponseTypeDef(_ListResourcesPaginateResponseTypeDef):
    """
    Type definition for `ListResourcesPaginate` `Response`

    - **resources** *(list) --*

      Information about the resources.

      - *(dict) --*

        Describes a resource associated with a resource share.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

        - **type** *(string) --*

          The resource type.

        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.

        - **status** *(string) --*

          The status of the resource.

        - **statusMessage** *(string) --*

          A message about the status of the resource.

        - **creationTime** *(datetime) --*

          The time when the resource was associated with the resource share.

        - **lastUpdatedTime** *(datetime) --*

          The time when the association was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
