"Main interface for kms Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kms.type_defs import (
    ListAliasesPaginatePaginationConfigTypeDef,
    ListAliasesPaginateResponseTypeDef,
    ListGrantsPaginatePaginationConfigTypeDef,
    ListGrantsPaginateResponseTypeDef,
    ListKeyPoliciesPaginatePaginationConfigTypeDef,
    ListKeyPoliciesPaginateResponseTypeDef,
    ListKeysPaginatePaginationConfigTypeDef,
    ListKeysPaginateResponseTypeDef,
)


__all__ = (
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeysPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    Paginator for `list_aliases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        KeyId: str = None,
        PaginationConfig: ListAliasesPaginatePaginationConfigTypeDef = None,
    ) -> ListAliasesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`KMS.Client.list_aliases`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListAliases>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              KeyId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type KeyId: string
        :param KeyId:

          Lists only aliases that refer to the specified CMK. The value of this parameter can be the ID or
          Amazon Resource Name (ARN) of a CMK in the caller's account and region. You cannot use an alias
          name or alias ARN in this value.

          This parameter is optional. If you omit it, ``ListAliases`` returns all aliases in the account
          and region.

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
                'Aliases': [
                    {
                        'AliasName': 'string',
                        'AliasArn': 'string',
                        'TargetKeyId': 'string'
                    },
                ],
                'Truncated': True|False,
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Aliases** *(list) --*

              A list of aliases.

              - *(dict) --*

                Contains information about an alias.

                - **AliasName** *(string) --*

                  String that contains the alias. This value begins with ``alias/`` .

                - **AliasArn** *(string) --*

                  String that contains the key ARN.

                - **TargetKeyId** *(string) --*

                  String that contains the key identifier referred to by the alias.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is true, the
              list in this response is truncated. To get more items, pass the value of the ``NextMarker``
              element in thisresponse to the ``Marker`` parameter in a subsequent request.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListGrantsPaginator(Boto3Paginator):
    """
    Paginator for `list_grants`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        KeyId: str,
        PaginationConfig: ListGrantsPaginatePaginationConfigTypeDef = None,
    ) -> ListGrantsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`KMS.Client.list_grants`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListGrants>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              KeyId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different
          AWS account, you must use the key ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

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
                'Grants': [
                    {
                        'KeyId': 'string',
                        'GrantId': 'string',
                        'Name': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'GranteePrincipal': 'string',
                        'RetiringPrincipal': 'string',
                        'IssuingAccount': 'string',
                        'Operations': [
                            'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'
                            |'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
                        ],
                        'Constraints': {
                            'EncryptionContextSubset': {
                                'string': 'string'
                            },
                            'EncryptionContextEquals': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'Truncated': True|False,
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Grants** *(list) --*

              A list of grants.

              - *(dict) --*

                Contains information about an entry in a list of grants.

                - **KeyId** *(string) --*

                  The unique identifier for the customer master key (CMK) to which the grant applies.

                - **GrantId** *(string) --*

                  The unique identifier for the grant.

                - **Name** *(string) --*

                  The friendly name that identifies the grant. If a name was provided in the  CreateGrant
                  request, that name is returned. Otherwise this value is null.

                - **CreationDate** *(datetime) --*

                  The date and time when the grant was created.

                - **GranteePrincipal** *(string) --*

                  The principal that receives the grant's permissions.

                - **RetiringPrincipal** *(string) --*

                  The principal that can retire the grant.

                - **IssuingAccount** *(string) --*

                  The AWS account under which the grant was issued.

                - **Operations** *(list) --*

                  The list of operations permitted by the grant.

                  - *(string) --*

                - **Constraints** *(dict) --*

                  A list of key-value pairs that must be present in the encryption context of certain
                  subsequent operations that the grant allows.

                  - **EncryptionContextSubset** *(dict) --*

                    A list of key-value pairs that must be included in the encryption context of the
                    cryptographic operation request. The grant allows the cryptographic operation only when
                    the encryption context in the request includes the key-value pairs specified in this
                    constraint, although it can include additional key-value pairs.

                    - *(string) --*

                      - *(string) --*

                  - **EncryptionContextEquals** *(dict) --*

                    A list of key-value pairs that must match the encryption context in the cryptographic
                    operation request. The grant allows the operation only when the encryption context in
                    the request is the same as the encryption context specified in this constraint.

                    - *(string) --*

                      - *(string) --*

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is true, the
              list in this response is truncated. To get more items, pass the value of the ``NextMarker``
              element in thisresponse to the ``Marker`` parameter in a subsequent request.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListKeyPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_key_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        KeyId: str,
        PaginationConfig: ListKeyPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListKeyPoliciesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`KMS.Client.list_key_policies`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeyPolicies>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              KeyId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

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
                'PolicyNames': [
                    'string',
                ],
                'Truncated': True|False,
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyNames** *(list) --*

              A list of key policy names. The only valid value is ``default`` .

              - *(string) --*

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is true, the
              list in this response is truncated. To get more items, pass the value of the ``NextMarker``
              element in thisresponse to the ``Marker`` parameter in a subsequent request.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListKeysPaginator(Boto3Paginator):
    """
    Paginator for `list_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListKeysPaginatePaginationConfigTypeDef = None
    ) -> ListKeysPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`KMS.Client.list_keys`.

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeys>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
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
                'Keys': [
                    {
                        'KeyId': 'string',
                        'KeyArn': 'string'
                    },
                ],
                'Truncated': True|False,
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Keys** *(list) --*

              A list of customer master keys (CMKs).

              - *(dict) --*

                Contains information about each entry in the key list.

                - **KeyId** *(string) --*

                  Unique identifier of the key.

                - **KeyArn** *(string) --*

                  ARN of the key.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is true, the
              list in this response is truncated. To get more items, pass the value of the ``NextMarker``
              element in thisresponse to the ``Marker`` parameter in a subsequent request.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
