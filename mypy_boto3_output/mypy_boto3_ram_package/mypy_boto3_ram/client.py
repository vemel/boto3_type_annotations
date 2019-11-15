"Main interface for ram Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from mypy_boto3_ram.type_defs import (
    ClientAcceptResourceShareInvitationResponseTypeDef,
    ClientAssociateResourceShareResponseTypeDef,
    ClientCreateResourceShareResponseTypeDef,
    ClientCreateResourceSharetagsTypeDef,
    ClientDeleteResourceShareResponseTypeDef,
    ClientDisassociateResourceShareResponseTypeDef,
    ClientEnableSharingWithAwsOrganizationResponseTypeDef,
    ClientGetResourcePoliciesResponseTypeDef,
    ClientGetResourceShareAssociationsResponseTypeDef,
    ClientGetResourceShareInvitationsResponseTypeDef,
    ClientGetResourceSharesResponseTypeDef,
    ClientGetResourceSharestagFiltersTypeDef,
    ClientListPendingInvitationResourcesResponseTypeDef,
    ClientListPrincipalsResponseTypeDef,
    ClientListResourcesResponseTypeDef,
    ClientRejectResourceShareInvitationResponseTypeDef,
    ClientTagResourcetagsTypeDef,
    ClientUpdateResourceShareResponseTypeDef,
)


class Client(BaseClient):
    # pylint: disable=arguments-differ
    def accept_resource_share_invitation(
        self, resourceShareInvitationArn: str, clientToken: str = None
    ) -> ClientAcceptResourceShareInvitationResponseTypeDef:
        """
        Accepts an invitation to a resource share from another AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/AcceptResourceShareInvitation>`_

        **Request Syntax**
        ::

          response = client.accept_resource_share_invitation(
              resourceShareInvitationArn='string',
              clientToken='string'
          )
        :type resourceShareInvitationArn: string
        :param resourceShareInvitationArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the invitation.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareInvitation': {
                    'resourceShareInvitationArn': 'string',
                    'resourceShareName': 'string',
                    'resourceShareArn': 'string',
                    'senderAccountId': 'string',
                    'receiverAccountId': 'string',
                    'invitationTimestamp': datetime(2015, 1, 1),
                    'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
                    'resourceShareAssociations': [
                        {
                            'resourceShareArn': 'string',
                            'resourceShareName': 'string',
                            'associatedEntity': 'string',
                            'associationType': 'PRINCIPAL'|'RESOURCE',
                            'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                            'statusMessage': 'string',
                            'creationTime': datetime(2015, 1, 1),
                            'lastUpdatedTime': datetime(2015, 1, 1),
                            'external': True|False
                        },
                    ]
                },
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def associate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        clientToken: str = None,
    ) -> ClientAssociateResourceShareResponseTypeDef:
        """
        Associates the specified resource share with the specified principals and resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/AssociateResourceShare>`_

        **Request Syntax**
        ::

          response = client.associate_resource_share(
              resourceShareArn='string',
              resourceArns=[
                  'string',
              ],
              principals=[
                  'string',
              ],
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type resourceArns: list
        :param resourceArns:

          The Amazon Resource Names (ARN) of the resources.

          - *(string) --*

        :type principals: list
        :param principals:

          The principals.

          - *(string) --*

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareAssociations': [
                    {
                        'resourceShareArn': 'string',
                        'resourceShareName': 'string',
                        'associatedEntity': 'string',
                        'associationType': 'PRINCIPAL'|'RESOURCE',
                        'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ],
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
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

    # pylint: disable=arguments-differ
    def create_resource_share(
        self,
        name: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        tags: List[ClientCreateResourceSharetagsTypeDef] = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
    ) -> ClientCreateResourceShareResponseTypeDef:
        """
        Creates a resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/CreateResourceShare>`_

        **Request Syntax**
        ::

          response = client.create_resource_share(
              name='string',
              resourceArns=[
                  'string',
              ],
              principals=[
                  'string',
              ],
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              allowExternalPrincipals=True|False,
              clientToken='string'
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the resource share.

        :type resourceArns: list
        :param resourceArns:

          The Amazon Resource Names (ARN) of the resources to associate with the resource share.

          - *(string) --*

        :type principals: list
        :param principals:

          The principals to associate with the resource share. The possible values are IDs of AWS accounts,
          the ARN of an OU or organization from AWS Organizations.

          - *(string) --*

        :type tags: list
        :param tags:

          One or more tags.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key of the tag.

            - **value** *(string) --*

              The value of the tag.

        :type allowExternalPrincipals: boolean
        :param allowExternalPrincipals:

          Indicates whether principals outside your AWS organization can be associated with a resource
          share.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShare': {
                    'resourceShareArn': 'string',
                    'name': 'string',
                    'owningAccountId': 'string',
                    'allowExternalPrincipals': True|False,
                    'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                    'statusMessage': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1)
                },
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def delete_resource_share(
        self, resourceShareArn: str, clientToken: str = None
    ) -> ClientDeleteResourceShareResponseTypeDef:
        """
        Deletes the specified resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/DeleteResourceShare>`_

        **Request Syntax**
        ::

          response = client.delete_resource_share(
              resourceShareArn='string',
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'returnValue': True|False,
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **returnValue** *(boolean) --*

              Indicates whether the request succeeded.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        """

    # pylint: disable=arguments-differ
    def disassociate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        clientToken: str = None,
    ) -> ClientDisassociateResourceShareResponseTypeDef:
        """
        Disassociates the specified principals or resources from the specified resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/DisassociateResourceShare>`_

        **Request Syntax**
        ::

          response = client.disassociate_resource_share(
              resourceShareArn='string',
              resourceArns=[
                  'string',
              ],
              principals=[
                  'string',
              ],
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type resourceArns: list
        :param resourceArns:

          The Amazon Resource Names (ARN) of the resources.

          - *(string) --*

        :type principals: list
        :param principals:

          The principals.

          - *(string) --*

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareAssociations': [
                    {
                        'resourceShareArn': 'string',
                        'resourceShareName': 'string',
                        'associatedEntity': 'string',
                        'associationType': 'PRINCIPAL'|'RESOURCE',
                        'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ],
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def enable_sharing_with_aws_organization(
        self, *args: Any, **kwargs: Any
    ) -> ClientEnableSharingWithAwsOrganizationResponseTypeDef:
        """
        Enables resource sharing within your AWS Organization.

        The caller must be the master account for the AWS Organization.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/EnableSharingWithAwsOrganization>`_

        **Request Syntax**
        ::

          response = client.enable_sharing_with_aws_organization()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'returnValue': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **returnValue** *(boolean) --*

              Indicates whether the request succeeded.

        """

    # pylint: disable=arguments-differ
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

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str) -> Paginator:
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

    # pylint: disable=arguments-differ
    def get_resource_policies(
        self,
        resourceArns: List[str],
        principal: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourcePoliciesResponseTypeDef:
        """
        Gets the policies for the specified resources that you own and have shared.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetResourcePolicies>`_

        **Request Syntax**
        ::

          response = client.get_resource_policies(
              resourceArns=[
                  'string',
              ],
              principal='string',
              nextToken='string',
              maxResults=123
          )
        :type resourceArns: list
        :param resourceArns: **[REQUIRED]**

          The Amazon Resource Names (ARN) of the resources.

          - *(string) --*

        :type principal: string
        :param principal:

          The principal.

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining results,
          make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'policies': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **policies** *(list) --*

              A key policy document, in JSON format.

              - *(string) --*

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when there are
              no more results to return.

        """

    # pylint: disable=arguments-differ
    def get_resource_share_associations(
        self,
        associationType: str,
        resourceShareArns: List[str] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceShareAssociationsResponseTypeDef:
        """
        Gets the resources or principals for the resource shares that you own.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetResourceShareAssociations>`_

        **Request Syntax**
        ::

          response = client.get_resource_share_associations(
              associationType='PRINCIPAL'|'RESOURCE',
              resourceShareArns=[
                  'string',
              ],
              resourceArn='string',
              principal='string',
              associationStatus='ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
              nextToken='string',
              maxResults=123
          )
        :type associationType: string
        :param associationType: **[REQUIRED]**

          The association type.

        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type resourceArn: string
        :param resourceArn:

          The Amazon Resource Name (ARN) of the resource. You cannot specify this parameter if the
          association type is ``PRINCIPAL`` .

        :type principal: string
        :param principal:

          The principal. You cannot specify this parameter if the association type is ``RESOURCE`` .

        :type associationStatus: string
        :param associationStatus:

          The association status.

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining results,
          make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareAssociations': [
                    {
                        'resourceShareArn': 'string',
                        'resourceShareName': 'string',
                        'associatedEntity': 'string',
                        'associationType': 'PRINCIPAL'|'RESOURCE',
                        'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def get_resource_share_invitations(
        self,
        resourceShareInvitationArns: List[str] = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceShareInvitationsResponseTypeDef:
        """
        Gets the invitations for resource sharing that you've received.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetResourceShareInvitations>`_

        **Request Syntax**
        ::

          response = client.get_resource_share_invitations(
              resourceShareInvitationArns=[
                  'string',
              ],
              resourceShareArns=[
                  'string',
              ],
              nextToken='string',
              maxResults=123
          )
        :type resourceShareInvitationArns: list
        :param resourceShareInvitationArns:

          The Amazon Resource Names (ARN) of the invitations.

          - *(string) --*

        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining results,
          make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareInvitations': [
                    {
                        'resourceShareInvitationArn': 'string',
                        'resourceShareName': 'string',
                        'resourceShareArn': 'string',
                        'senderAccountId': 'string',
                        'receiverAccountId': 'string',
                        'invitationTimestamp': datetime(2015, 1, 1),
                        'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
                        'resourceShareAssociations': [
                            {
                                'resourceShareArn': 'string',
                                'resourceShareName': 'string',
                                'associatedEntity': 'string',
                                'associationType': 'PRINCIPAL'|'RESOURCE',
                                'status':
                                'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                                'statusMessage': 'string',
                                'creationTime': datetime(2015, 1, 1),
                                'lastUpdatedTime': datetime(2015, 1, 1),
                                'external': True|False
                            },
                        ]
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def get_resource_shares(
        self,
        resourceOwner: str,
        resourceShareArns: List[str] = None,
        resourceShareStatus: str = None,
        name: str = None,
        tagFilters: List[ClientGetResourceSharestagFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceSharesResponseTypeDef:
        """
        Gets the resource shares that you own or the resource shares that are shared with you.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetResourceShares>`_

        **Request Syntax**
        ::

          response = client.get_resource_shares(
              resourceShareArns=[
                  'string',
              ],
              resourceShareStatus='PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
              resourceOwner='SELF'|'OTHER-ACCOUNTS',
              name='string',
              tagFilters=[
                  {
                      'tagKey': 'string',
                      'tagValues': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
          )
        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type resourceShareStatus: string
        :param resourceShareStatus:

          The status of the resource share.

        :type resourceOwner: string
        :param resourceOwner: **[REQUIRED]**

          The type of owner.

        :type name: string
        :param name:

          The name of the resource share.

        :type tagFilters: list
        :param tagFilters:

          One or more tag filters.

          - *(dict) --*

            Used to filter information based on tags.

            - **tagKey** *(string) --*

              The tag key.

            - **tagValues** *(list) --*

              The tag values.

              - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining results,
          make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShares': [
                    {
                        'resourceShareArn': 'string',
                        'name': 'string',
                        'owningAccountId': 'string',
                        'allowExternalPrincipals': True|False,
                        'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                        'statusMessage': 'string',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str) -> Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """

    # pylint: disable=arguments-differ
    def list_pending_invitation_resources(
        self,
        resourceShareInvitationArn: str,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListPendingInvitationResourcesResponseTypeDef:
        """
        Lists the resources in a resource share that is shared with you but that the invitation is still
        pending for.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListPendingInvitationResources>`_

        **Request Syntax**
        ::

          response = client.list_pending_invitation_resources(
              resourceShareInvitationArn='string',
              nextToken='string',
              maxResults=123
          )
        :type resourceShareInvitationArn: string
        :param resourceShareInvitationArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the invitation.

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining results,
          make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resources': [
                    {
                        'arn': 'string',
                        'type': 'string',
                        'resourceShareArn': 'string',
                        'status':
                        'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'|'UNAVAILABLE'|'PENDING',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def list_principals(
        self,
        resourceOwner: str,
        resourceArn: str = None,
        principals: List[str] = None,
        resourceType: str = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListPrincipalsResponseTypeDef:
        """
        Lists the principals that you have shared resources with or the principals that have shared
        resources with you.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListPrincipals>`_

        **Request Syntax**
        ::

          response = client.list_principals(
              resourceOwner='SELF'|'OTHER-ACCOUNTS',
              resourceArn='string',
              principals=[
                  'string',
              ],
              resourceType='string',
              resourceShareArns=[
                  'string',
              ],
              nextToken='string',
              maxResults=123
          )
        :type resourceOwner: string
        :param resourceOwner: **[REQUIRED]**

          The type of owner.

        :type resourceArn: string
        :param resourceArn:

          The Amazon Resource Name (ARN) of the resource.

        :type principals: list
        :param principals:

          The principals.

          - *(string) --*

        :type resourceType: string
        :param resourceType:

          The resource type.

          Valid values: ``route53resolver:ResolverRule`` | ``ec2:TransitGateway`` | ``ec2:Subnet`` |
          ``license-manager:LicenseConfiguration``

        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining results,
          make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'principals': [
                    {
                        'id': 'string',
                        'resourceShareArn': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def list_resources(
        self,
        resourceOwner: str,
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[str] = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListResourcesResponseTypeDef:
        """
        Lists the resources that you added to a resource shares or the resources that are shared with you.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListResources>`_

        **Request Syntax**
        ::

          response = client.list_resources(
              resourceOwner='SELF'|'OTHER-ACCOUNTS',
              principal='string',
              resourceType='string',
              resourceArns=[
                  'string',
              ],
              resourceShareArns=[
                  'string',
              ],
              nextToken='string',
              maxResults=123
          )
        :type resourceOwner: string
        :param resourceOwner: **[REQUIRED]**

          The type of owner.

        :type principal: string
        :param principal:

          The principal.

        :type resourceType: string
        :param resourceType:

          The resource type.

          Valid values: ``route53resolver:ResolverRule`` | ``ec2:TransitGateway`` | ``ec2:Subnet`` |
          ``license-manager:LicenseConfiguration``

        :type resourceArns: list
        :param resourceArns:

          The Amazon Resource Names (ARN) of the resources.

          - *(string) --*

        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining results,
          make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resources': [
                    {
                        'arn': 'string',
                        'type': 'string',
                        'resourceShareArn': 'string',
                        'status':
                        'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'|'UNAVAILABLE'|'PENDING',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def reject_resource_share_invitation(
        self, resourceShareInvitationArn: str, clientToken: str = None
    ) -> ClientRejectResourceShareInvitationResponseTypeDef:
        """
        Rejects an invitation to a resource share from another AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/RejectResourceShareInvitation>`_

        **Request Syntax**
        ::

          response = client.reject_resource_share_invitation(
              resourceShareInvitationArn='string',
              clientToken='string'
          )
        :type resourceShareInvitationArn: string
        :param resourceShareInvitationArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the invitation.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareInvitation': {
                    'resourceShareInvitationArn': 'string',
                    'resourceShareName': 'string',
                    'resourceShareArn': 'string',
                    'senderAccountId': 'string',
                    'receiverAccountId': 'string',
                    'invitationTimestamp': datetime(2015, 1, 1),
                    'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
                    'resourceShareAssociations': [
                        {
                            'resourceShareArn': 'string',
                            'resourceShareName': 'string',
                            'associatedEntity': 'string',
                            'associationType': 'PRINCIPAL'|'RESOURCE',
                            'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                            'statusMessage': 'string',
                            'creationTime': datetime(2015, 1, 1),
                            'lastUpdatedTime': datetime(2015, 1, 1),
                            'external': True|False
                        },
                    ]
                },
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ
    def tag_resource(
        self, resourceShareArn: str, tags: List[ClientTagResourcetagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource share that you own.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceShareArn='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type tags: list
        :param tags: **[REQUIRED]**

          One or more tags.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key of the tag.

            - **value** *(string) --*

              The value of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ
    def untag_resource(
        self, resourceShareArn: str, tagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource share that you own.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceShareArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          The tag keys of the tags to remove.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ
    def update_resource_share(
        self,
        resourceShareArn: str,
        name: str = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
    ) -> ClientUpdateResourceShareResponseTypeDef:
        """
        Updates the specified resource share that you own.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/UpdateResourceShare>`_

        **Request Syntax**
        ::

          response = client.update_resource_share(
              resourceShareArn='string',
              name='string',
              allowExternalPrincipals=True|False,
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type name: string
        :param name:

          The name of the resource share.

        :type allowExternalPrincipals: boolean
        :param allowExternalPrincipals:

          Indicates whether principals outside your AWS organization can be associated with a resource
          share.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShare': {
                    'resourceShareArn': 'string',
                    'name': 'string',
                    'owningAccountId': 'string',
                    'allowExternalPrincipals': True|False,
                    'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                    'statusMessage': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1)
                },
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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
