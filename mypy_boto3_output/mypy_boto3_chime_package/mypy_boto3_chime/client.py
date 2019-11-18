"Main interface for chime Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_chime.client as client_scope

# pylint: disable=import-self
import mypy_boto3_chime.paginator as paginator_scope
from mypy_boto3_chime.type_defs import (
    ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef,
    ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef,
    ClientBatchCreateRoomMembershipMembershipItemListTypeDef,
    ClientBatchCreateRoomMembershipResponseTypeDef,
    ClientBatchDeletePhoneNumberResponseTypeDef,
    ClientBatchSuspendUserResponseTypeDef,
    ClientBatchUnsuspendUserResponseTypeDef,
    ClientBatchUpdatePhoneNumberResponseTypeDef,
    ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef,
    ClientBatchUpdateUserResponseTypeDef,
    ClientBatchUpdateUserUpdateUserRequestItemsTypeDef,
    ClientCreateAccountResponseTypeDef,
    ClientCreateBotResponseTypeDef,
    ClientCreatePhoneNumberOrderResponseTypeDef,
    ClientCreateRoomMembershipResponseTypeDef,
    ClientCreateRoomResponseTypeDef,
    ClientCreateVoiceConnectorGroupResponseTypeDef,
    ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
    ClientCreateVoiceConnectorResponseTypeDef,
    ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef,
    ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef,
    ClientGetAccountResponseTypeDef,
    ClientGetAccountSettingsResponseTypeDef,
    ClientGetBotResponseTypeDef,
    ClientGetEventsConfigurationResponseTypeDef,
    ClientGetGlobalSettingsResponseTypeDef,
    ClientGetPhoneNumberOrderResponseTypeDef,
    ClientGetPhoneNumberResponseTypeDef,
    ClientGetPhoneNumberSettingsResponseTypeDef,
    ClientGetRoomResponseTypeDef,
    ClientGetUserResponseTypeDef,
    ClientGetUserSettingsResponseTypeDef,
    ClientGetVoiceConnectorGroupResponseTypeDef,
    ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef,
    ClientGetVoiceConnectorOriginationResponseTypeDef,
    ClientGetVoiceConnectorResponseTypeDef,
    ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef,
    ClientGetVoiceConnectorTerminationHealthResponseTypeDef,
    ClientGetVoiceConnectorTerminationResponseTypeDef,
    ClientInviteUsersResponseTypeDef,
    ClientListAccountsResponseTypeDef,
    ClientListBotsResponseTypeDef,
    ClientListPhoneNumberOrdersResponseTypeDef,
    ClientListPhoneNumbersResponseTypeDef,
    ClientListRoomMembershipsResponseTypeDef,
    ClientListRoomsResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientListVoiceConnectorGroupsResponseTypeDef,
    ClientListVoiceConnectorTerminationCredentialsResponseTypeDef,
    ClientListVoiceConnectorsResponseTypeDef,
    ClientPutEventsConfigurationResponseTypeDef,
    ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef,
    ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef,
    ClientPutVoiceConnectorOriginationOriginationTypeDef,
    ClientPutVoiceConnectorOriginationResponseTypeDef,
    ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef,
    ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
    ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef,
    ClientPutVoiceConnectorTerminationResponseTypeDef,
    ClientPutVoiceConnectorTerminationTerminationTypeDef,
    ClientRegenerateSecurityTokenResponseTypeDef,
    ClientResetPersonalPinResponseTypeDef,
    ClientRestorePhoneNumberResponseTypeDef,
    ClientSearchAvailablePhoneNumbersResponseTypeDef,
    ClientUpdateAccountResponseTypeDef,
    ClientUpdateAccountSettingsAccountSettingsTypeDef,
    ClientUpdateBotResponseTypeDef,
    ClientUpdateGlobalSettingsBusinessCallingTypeDef,
    ClientUpdateGlobalSettingsVoiceConnectorTypeDef,
    ClientUpdatePhoneNumberResponseTypeDef,
    ClientUpdateRoomMembershipResponseTypeDef,
    ClientUpdateRoomResponseTypeDef,
    ClientUpdateUserResponseTypeDef,
    ClientUpdateUserSettingsUserSettingsTypeDef,
    ClientUpdateVoiceConnectorGroupResponseTypeDef,
    ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
    ClientUpdateVoiceConnectorResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_phone_number_with_user(
        self, AccountId: str, UserId: str, E164PhoneNumber: str
    ) -> Dict[str, Any]:
        """
        Associates a phone number with the specified Amazon Chime user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/AssociatePhoneNumberWithUser>`_

        **Request Syntax**
        ::

          response = client.associate_phone_number_with_user(
              AccountId='string',
              UserId='string',
              E164PhoneNumber='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The user ID.

        :type E164PhoneNumber: string
        :param E164PhoneNumber: **[REQUIRED]**

          The phone number, in E.164 format.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_phone_numbers_with_voice_connector(
        self,
        VoiceConnectorId: str,
        E164PhoneNumbers: List[str] = None,
        ForceAssociate: bool = None,
    ) -> ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef:
        """
        Associates phone numbers with the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/AssociatePhoneNumbersWithVoiceConnector>`_

        **Request Syntax**
        ::

          response = client.associate_phone_numbers_with_voice_connector(
              VoiceConnectorId='string',
              E164PhoneNumbers=[
                  'string',
              ],
              ForceAssociate=True|False
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type E164PhoneNumbers: list
        :param E164PhoneNumbers:

          List of phone numbers, in E.164 format.

          - *(string) --*

        :type ForceAssociate: boolean
        :param ForceAssociate:

          If true, associates the provided phone numbers with the provided Amazon Chime Voice Connector and
          removes any previously existing associations. If false, does not associate any phone numbers that
          have previously existing associations.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberErrors** *(list) --*

              If the action fails for one or more of the phone numbers in the request, a list of the phone
              numbers is returned, along with error codes and error messages.

              - *(dict) --*

                If the phone number action fails for one or more of the phone numbers in the request, a
                list of the phone numbers is returned, along with error codes and error messages.

                - **PhoneNumberId** *(string) --*

                  The phone number ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_phone_numbers_with_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: List[str] = None,
        ForceAssociate: bool = None,
    ) -> ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef:
        """
        Associates phone numbers with the specified Amazon Chime Voice Connector group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/AssociatePhoneNumbersWithVoiceConnectorGroup>`_
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/AssociatePhoneNumbersWithVoiceConnectorGroup>`_

        **Request Syntax**
        ::

          response = client.associate_phone_numbers_with_voice_connector_group(
              VoiceConnectorGroupId='string',
              E164PhoneNumbers=[
                  'string',
              ],
              ForceAssociate=True|False
          )
        :type VoiceConnectorGroupId: string
        :param VoiceConnectorGroupId: **[REQUIRED]**

          The Amazon Chime Voice Connector group ID.

        :type E164PhoneNumbers: list
        :param E164PhoneNumbers:

          List of phone numbers, in E.164 format.

          - *(string) --*

        :type ForceAssociate: boolean
        :param ForceAssociate:

          If true, associates the provided phone numbers with the provided Amazon Chime Voice Connector
          Group and removes any previously existing associations. If false, does not associate any phone
          numbers that have previously existing associations.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberErrors** *(list) --*

              If the action fails for one or more of the phone numbers in the request, a list of the phone
              numbers is returned, along with error codes and error messages.

              - *(dict) --*

                If the phone number action fails for one or more of the phone numbers in the request, a
                list of the phone numbers is returned, along with error codes and error messages.

                - **PhoneNumberId** *(string) --*

                  The phone number ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_create_room_membership(
        self,
        AccountId: str,
        RoomId: str,
        MembershipItemList: List[
            ClientBatchCreateRoomMembershipMembershipItemListTypeDef
        ],
    ) -> ClientBatchCreateRoomMembershipResponseTypeDef:
        """
        Adds up to 50 members to a chat room. Members can be either users or bots. The member role
        designates whether the member is a chat room administrator or a general chat room member.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchCreateRoomMembership>`_

        **Request Syntax**
        ::

          response = client.batch_create_room_membership(
              AccountId='string',
              RoomId='string',
              MembershipItemList=[
                  {
                      'MemberId': 'string',
                      'Role': 'Administrator'|'Member'
                  },
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type RoomId: string
        :param RoomId: **[REQUIRED]**

          The room ID.

        :type MembershipItemList: list
        :param MembershipItemList: **[REQUIRED]**

          The list of membership items.

          - *(dict) --*

            Membership details, such as member ID and member role.

            - **MemberId** *(string) --*

              The member ID.

            - **Role** *(string) --*

              The member role.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Errors': [
                    {
                        'MemberId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Errors** *(list) --*

              If the action fails for one or more of the member IDs in the request, a list of the member
              IDs is returned, along with error codes and error messages.

              - *(dict) --*

                The list of errors returned when a member action results in an error.

                - **MemberId** *(string) --*

                  The member ID.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_phone_number(
        self, PhoneNumberIds: List[str]
    ) -> ClientBatchDeletePhoneNumberResponseTypeDef:
        """
        Moves phone numbers into the **Deletion queue** . Phone numbers must be disassociated from any
        users or Amazon Chime Voice Connectors before they can be deleted.

        Phone numbers remain in the **Deletion queue** for 7 days before they are deleted permanently.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchDeletePhoneNumber>`_

        **Request Syntax**
        ::

          response = client.batch_delete_phone_number(
              PhoneNumberIds=[
                  'string',
              ]
          )
        :type PhoneNumberIds: list
        :param PhoneNumberIds: **[REQUIRED]**

          List of phone number IDs.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberErrors** *(list) --*

              If the action fails for one or more of the phone numbers in the request, a list of the phone
              numbers is returned, along with error codes and error messages.

              - *(dict) --*

                If the phone number action fails for one or more of the phone numbers in the request, a
                list of the phone numbers is returned, along with error codes and error messages.

                - **PhoneNumberId** *(string) --*

                  The phone number ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_suspend_user(
        self, AccountId: str, UserIdList: List[str]
    ) -> ClientBatchSuspendUserResponseTypeDef:
        """
        Suspends up to 50 users from a ``Team`` or ``EnterpriseLWA`` Amazon Chime account. For more
        information about different account types, see `Managing Your Amazon Chime Accounts
        <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime
        Administration Guide* .

        Users suspended from a ``Team`` account are dissasociated from the account, but they can continue
        to use Amazon Chime as free users. To remove the suspension from suspended ``Team`` account users,
        invite them to the ``Team`` account again. You can use the  InviteUsers action to do so.

        Users suspended from an ``EnterpriseLWA`` account are immediately signed out of Amazon Chime and
        can no longer sign in. To remove the suspension from suspended ``EnterpriseLWA`` account users, use
        the  BatchUnsuspendUser action.

        To sign out users without suspending them, use the  LogoutUser action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchSuspendUser>`_

        **Request Syntax**
        ::

          response = client.batch_suspend_user(
              AccountId='string',
              UserIdList=[
                  'string',
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserIdList: list
        :param UserIdList: **[REQUIRED]**

          The request containing the user IDs to suspend.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserErrors': [
                    {
                        'UserId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UserErrors** *(list) --*

              If the  BatchSuspendUser action fails for one or more of the user IDs in the request, a list
              of the user IDs is returned, along with error codes and error messages.

              - *(dict) --*

                The list of errors returned when errors are encountered during the  BatchSuspendUser ,
                BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
                error messages.

                - **UserId** *(string) --*

                  The user ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_unsuspend_user(
        self, AccountId: str, UserIdList: List[str]
    ) -> ClientBatchUnsuspendUserResponseTypeDef:
        """
        Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime
        ``EnterpriseLWA`` account. Only users on ``EnterpriseLWA`` accounts can be unsuspended using this
        action. For more information about different account types, see `Managing Your Amazon Chime
        Accounts <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
        Chime Administration Guide* .

        Previously suspended users who are unsuspended using this action are returned to ``Registered``
        status. Users who are not previously suspended are ignored.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchUnsuspendUser>`_

        **Request Syntax**
        ::

          response = client.batch_unsuspend_user(
              AccountId='string',
              UserIdList=[
                  'string',
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserIdList: list
        :param UserIdList: **[REQUIRED]**

          The request containing the user IDs to unsuspend.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserErrors': [
                    {
                        'UserId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UserErrors** *(list) --*

              If the  BatchUnsuspendUser action fails for one or more of the user IDs in the request, a
              list of the user IDs is returned, along with error codes and error messages.

              - *(dict) --*

                The list of errors returned when errors are encountered during the  BatchSuspendUser ,
                BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
                error messages.

                - **UserId** *(string) --*

                  The user ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_update_phone_number(
        self,
        UpdatePhoneNumberRequestItems: List[
            ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef
        ],
    ) -> ClientBatchUpdatePhoneNumberResponseTypeDef:
        """
        Updates phone number product types or calling names. You can update one attribute at a time for
        each ``UpdatePhoneNumberRequestItem`` . For example, you can update either the product type or the
        calling name.

        For product types, choose from Amazon Chime Business Calling and Amazon Chime Voice Connector. For
        toll-free numbers, you must use the Amazon Chime Voice Connector product type.

        Updates to outbound calling names can take up to 72 hours to complete. Pending updates to outbound
        calling names must be complete before you can request another update.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchUpdatePhoneNumber>`_

        **Request Syntax**
        ::

          response = client.batch_update_phone_number(
              UpdatePhoneNumberRequestItems=[
                  {
                      'PhoneNumberId': 'string',
                      'ProductType': 'BusinessCalling'|'VoiceConnector',
                      'CallingName': 'string'
                  },
              ]
          )
        :type UpdatePhoneNumberRequestItems: list
        :param UpdatePhoneNumberRequestItems: **[REQUIRED]**

          The request containing the phone number IDs and product types or calling names to update.

          - *(dict) --*

            The phone number ID, product type, or calling name fields to update, used with the
            BatchUpdatePhoneNumber and  UpdatePhoneNumber actions.

            - **PhoneNumberId** *(string) --* **[REQUIRED]**

              The phone number ID to update.

            - **ProductType** *(string) --*

              The product type to update.

            - **CallingName** *(string) --*

              The outbound calling name to update.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberErrors** *(list) --*

              If the action fails for one or more of the phone numbers in the request, a list of the phone
              numbers is returned, along with error codes and error messages.

              - *(dict) --*

                If the phone number action fails for one or more of the phone numbers in the request, a
                list of the phone numbers is returned, along with error codes and error messages.

                - **PhoneNumberId** *(string) --*

                  The phone number ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_update_user(
        self,
        AccountId: str,
        UpdateUserRequestItems: List[
            ClientBatchUpdateUserUpdateUserRequestItemsTypeDef
        ],
    ) -> ClientBatchUpdateUserResponseTypeDef:
        """
        Updates user details within the  UpdateUserRequestItem object for up to 20 users for the specified
        Amazon Chime account. Currently, only ``LicenseType`` updates are supported for this action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchUpdateUser>`_

        **Request Syntax**
        ::

          response = client.batch_update_user(
              AccountId='string',
              UpdateUserRequestItems=[
                  {
                      'UserId': 'string',
                      'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial'
                  },
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UpdateUserRequestItems: list
        :param UpdateUserRequestItems: **[REQUIRED]**

          The request containing the user IDs and details to update.

          - *(dict) --*

            The user ID and user fields to update, used with the  BatchUpdateUser action.

            - **UserId** *(string) --* **[REQUIRED]**

              The user ID.

            - **LicenseType** *(string) --*

              The user license type.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserErrors': [
                    {
                        'UserId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UserErrors** *(list) --*

              If the  BatchUpdateUser action fails for one or more of the user IDs in the request, a list
              of the user IDs is returned, along with error codes and error messages.

              - *(dict) --*

                The list of errors returned when errors are encountered during the  BatchSuspendUser ,
                BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
                error messages.

                - **UserId** *(string) --*

                  The user ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

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
    def create_account(self, Name: str) -> ClientCreateAccountResponseTypeDef:
        """
        Creates an Amazon Chime account under the administrator's AWS account. Only ``Team`` account types
        are currently supported for this action. For more information about different account types, see
        `Managing Your Amazon Chime Accounts
        <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime
        Administration Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateAccount>`_

        **Request Syntax**
        ::

          response = client.create_account(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the Amazon Chime account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Account': {
                    'AwsAccountId': 'string',
                    'AccountId': 'string',
                    'Name': 'string',
                    'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'SupportedLicenses': [
                        'Basic'|'Plus'|'Pro'|'ProTrial',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Account** *(dict) --*

              The Amazon Chime account details.

              - **AwsAccountId** *(string) --*

                The AWS account ID.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **Name** *(string) --*

                The Amazon Chime account name.

              - **AccountType** *(string) --*

                The Amazon Chime account type. For more information about different account types, see
                `Managing Your Amazon Chime Accounts
                <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
                Chime Administration Guide* .

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime account creation timestamp, in ISO 8601 format.

              - **DefaultLicense** *(string) --*

                The default license for the Amazon Chime account.

              - **SupportedLicenses** *(list) --*

                Supported licenses for the Amazon Chime account.

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_bot(
        self, AccountId: str, DisplayName: str, Domain: str = None
    ) -> ClientCreateBotResponseTypeDef:
        """
        Creates a bot for an Amazon Chime Enterprise account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateBot>`_

        **Request Syntax**
        ::

          response = client.create_bot(
              AccountId='string',
              DisplayName='string',
              Domain='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type DisplayName: string
        :param DisplayName: **[REQUIRED]**

          The bot display name.

        :type Domain: string
        :param Domain:

          The domain of the Amazon Chime Enterprise account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Bot': {
                    'BotId': 'string',
                    'UserId': 'string',
                    'DisplayName': 'string',
                    'BotType': 'ChatBot',
                    'Disabled': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'BotEmail': 'string',
                    'SecurityToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Bot** *(dict) --*

              The bot details.

              - **BotId** *(string) --*

                The bot ID.

              - **UserId** *(string) --*

                The unique ID for the bot user.

              - **DisplayName** *(string) --*

                The bot display name.

              - **BotType** *(string) --*

                The bot type.

              - **Disabled** *(boolean) --*

                When true, the bot is stopped from running in your account.

              - **CreatedTimestamp** *(datetime) --*

                The bot creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated bot timestamp, in ISO 8601 format.

              - **BotEmail** *(string) --*

                The bot email address.

              - **SecurityToken** *(string) --*

                The security token used to authenticate Amazon Chime with the outgoing event endpoint.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_phone_number_order(
        self, ProductType: str, E164PhoneNumbers: List[str]
    ) -> ClientCreatePhoneNumberOrderResponseTypeDef:
        """
        Creates an order for phone numbers to be provisioned. Choose from Amazon Chime Business Calling and
        Amazon Chime Voice Connector product types. For toll-free numbers, you must use the Amazon Chime
        Voice Connector product type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreatePhoneNumberOrder>`_

        **Request Syntax**
        ::

          response = client.create_phone_number_order(
              ProductType='BusinessCalling'|'VoiceConnector',
              E164PhoneNumbers=[
                  'string',
              ]
          )
        :type ProductType: string
        :param ProductType: **[REQUIRED]**

          The phone number product type.

        :type E164PhoneNumbers: list
        :param E164PhoneNumbers: **[REQUIRED]**

          List of phone numbers, in E.164 format.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberOrder': {
                    'PhoneNumberOrderId': 'string',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status': 'Processing'|'Successful'|'Failed'|'Partial',
                    'OrderedPhoneNumbers': [
                        {
                            'E164PhoneNumber': 'string',
                            'Status': 'Processing'|'Acquired'|'Failed'
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberOrder** *(dict) --*

              The phone number order details.

              - **PhoneNumberOrderId** *(string) --*

                The phone number order ID.

              - **ProductType** *(string) --*

                The phone number order product type.

              - **Status** *(string) --*

                The status of the phone number order.

              - **OrderedPhoneNumbers** *(list) --*

                The ordered phone number details, such as the phone number in E.164 format and the phone
                number status.

                - *(dict) --*

                  A phone number for which an order has been placed.

                  - **E164PhoneNumber** *(string) --*

                    The phone number, in E.164 format.

                  - **Status** *(string) --*

                    The phone number status.

              - **CreatedTimestamp** *(datetime) --*

                The phone number order creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated phone number order timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_room(
        self, AccountId: str, Name: str, ClientRequestToken: str = None
    ) -> ClientCreateRoomResponseTypeDef:
        """
        Creates a chat room for the specified Amazon Chime account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateRoom>`_

        **Request Syntax**
        ::

          response = client.create_room(
              AccountId='string',
              Name='string',
              ClientRequestToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type Name: string
        :param Name: **[REQUIRED]**

          The room name.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          The idempotency token for the request.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Room': {
                    'RoomId': 'string',
                    'Name': 'string',
                    'AccountId': 'string',
                    'CreatedBy': 'string',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Room** *(dict) --*

              The room details.

              - **RoomId** *(string) --*

                The room ID.

              - **Name** *(string) --*

                The room name.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **CreatedBy** *(string) --*

                The identifier of the room creator.

              - **CreatedTimestamp** *(datetime) --*

                The room creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The room update timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_room_membership(
        self, AccountId: str, RoomId: str, MemberId: str, Role: str = None
    ) -> ClientCreateRoomMembershipResponseTypeDef:
        """
        Adds a member to a chat room. A member can be either a user or a bot. The member role designates
        whether the member is a chat room administrator or a general chat room member.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateRoomMembership>`_

        **Request Syntax**
        ::

          response = client.create_room_membership(
              AccountId='string',
              RoomId='string',
              MemberId='string',
              Role='Administrator'|'Member'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type RoomId: string
        :param RoomId: **[REQUIRED]**

          The room ID.

        :type MemberId: string
        :param MemberId: **[REQUIRED]**

          The Amazon Chime member ID (user ID or bot ID).

        :type Role: string
        :param Role:

          The role of the member.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RoomMembership': {
                    'RoomId': 'string',
                    'Member': {
                        'MemberId': 'string',
                        'MemberType': 'User'|'Bot'|'Webhook',
                        'Email': 'string',
                        'FullName': 'string',
                        'AccountId': 'string'
                    },
                    'Role': 'Administrator'|'Member',
                    'InvitedBy': 'string',
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **RoomMembership** *(dict) --*

              The room membership details.

              - **RoomId** *(string) --*

                The room ID.

              - **Member** *(dict) --*

                The member details, such as email address, name, member ID, and member type.

                - **MemberId** *(string) --*

                  The member ID (user ID or bot ID).

                - **MemberType** *(string) --*

                  The member type.

                - **Email** *(string) --*

                  The member email address.

                - **FullName** *(string) --*

                  The member name.

                - **AccountId** *(string) --*

                  The Amazon Chime account ID.

              - **Role** *(string) --*

                The membership role.

              - **InvitedBy** *(string) --*

                The identifier of the user that invited the room member.

              - **UpdatedTimestamp** *(datetime) --*

                The room membership update timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_voice_connector(
        self, Name: str, RequireEncryption: bool, AwsRegion: str = None
    ) -> ClientCreateVoiceConnectorResponseTypeDef:
        """
        Creates an Amazon Chime Voice Connector under the administrator's AWS account. You can choose to
        create an Amazon Chime Voice Connector in a specific AWS Region.

        Enabling  CreateVoiceConnectorRequest$RequireEncryption configures your Amazon Chime Voice
        Connector to use TLS transport for SIP signaling and Secure RTP (SRTP) for media. Inbound calls use
        TLS transport, and unencrypted outbound calls are blocked.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateVoiceConnector>`_

        **Request Syntax**
        ::

          response = client.create_voice_connector(
              Name='string',
              AwsRegion='us-east-1'|'us-west-2',
              RequireEncryption=True|False
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the Amazon Chime Voice Connector.

        :type AwsRegion: string
        :param AwsRegion:

          The AWS Region in which the Amazon Chime Voice Connector is created. Default value: ``us-east-1``
          .

        :type RequireEncryption: boolean
        :param RequireEncryption: **[REQUIRED]**

          When enabled, requires encryption for the Amazon Chime Voice Connector.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VoiceConnector': {
                    'VoiceConnectorId': 'string',
                    'AwsRegion': 'us-east-1'|'us-west-2',
                    'Name': 'string',
                    'OutboundHostName': 'string',
                    'RequireEncryption': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **VoiceConnector** *(dict) --*

              The Amazon Chime Voice Connector details.

              - **VoiceConnectorId** *(string) --*

                The Amazon Chime Voice Connector ID.

              - **AwsRegion** *(string) --*

                The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
                .

              - **Name** *(string) --*

                The name of the Amazon Chime Voice Connector.

              - **OutboundHostName** *(string) --*

                The outbound host name for the Amazon Chime Voice Connector.

              - **RequireEncryption** *(boolean) --*

                Designates whether encryption is required for the Amazon Chime Voice Connector.

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_voice_connector_group(
        self,
        Name: str,
        VoiceConnectorItems: List[
            ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ] = None,
    ) -> ClientCreateVoiceConnectorGroupResponseTypeDef:
        """
        Creates an Amazon Chime Voice Connector group under the administrator's AWS account. You can
        associate up to three existing Amazon Chime Voice Connectors with the Amazon Chime Voice Connector
        group by including ``VoiceConnectorItems`` in the request.

        You can include Amazon Chime Voice Connectors from different AWS Regions in your group. This
        creates a fault tolerant mechanism for fallback in case of availability events.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateVoiceConnectorGroup>`_

        **Request Syntax**
        ::

          response = client.create_voice_connector_group(
              Name='string',
              VoiceConnectorItems=[
                  {
                      'VoiceConnectorId': 'string',
                      'Priority': 123
                  },
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the Amazon Chime Voice Connector group.

        :type VoiceConnectorItems: list
        :param VoiceConnectorItems:

          The Amazon Chime Voice Connectors to route inbound calls to.

          - *(dict) --*

            For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route
            inbound calls. Includes priority configuration settings. Limit: 3 ``VoiceConnectorItems`` per
            Amazon Chime Voice Connector group.

            - **VoiceConnectorId** *(string) --* **[REQUIRED]**

              The Amazon Chime Voice Connector ID.

            - **Priority** *(integer) --* **[REQUIRED]**

              The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
              priority. Higher priority Amazon Chime Voice Connectors are attempted first.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VoiceConnectorGroup': {
                    'VoiceConnectorGroupId': 'string',
                    'Name': 'string',
                    'VoiceConnectorItems': [
                        {
                            'VoiceConnectorId': 'string',
                            'Priority': 123
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **VoiceConnectorGroup** *(dict) --*

              The Amazon Chime Voice Connector group details.

              - **VoiceConnectorGroupId** *(string) --*

                The Amazon Chime Voice Connector group ID.

              - **Name** *(string) --*

                The name of the Amazon Chime Voice Connector group.

              - **VoiceConnectorItems** *(list) --*

                The Amazon Chime Voice Connectors to which to route inbound calls.

                - *(dict) --*

                  For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
                  route inbound calls. Includes priority configuration settings. Limit: 3
                  ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

                  - **VoiceConnectorId** *(string) --*

                    The Amazon Chime Voice Connector ID.

                  - **Priority** *(integer) --*

                    The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
                    priority. Higher priority Amazon Chime Voice Connectors are attempted first.

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_account(self, AccountId: str) -> Dict[str, Any]:
        """
        Deletes the specified Amazon Chime account. You must suspend all users before deleting a ``Team``
        account. You can use the  BatchSuspendUser action to do so.

        For ``EnterpriseLWA`` and ``EnterpriseAD`` accounts, you must release the claimed domains for your
        Amazon Chime account before deletion. As soon as you release the domain, all users under that
        account are suspended.

        Deleted accounts appear in your ``Disabled`` accounts list for 90 days. To restore a deleted
        account from your ``Disabled`` accounts list, you must contact AWS Support.

        After 90 days, deleted accounts are permanently removed from your ``Disabled`` accounts list.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteAccount>`_

        **Request Syntax**
        ::

          response = client.delete_account(
              AccountId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_events_configuration(self, AccountId: str, BotId: str) -> None:
        """
        Deletes the events configuration that allows a bot to receive outgoing events.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteEventsConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_events_configuration(
              AccountId='string',
              BotId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type BotId: string
        :param BotId: **[REQUIRED]**

          The bot ID.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_phone_number(self, PhoneNumberId: str) -> None:
        """
        Moves the specified phone number into the **Deletion queue** . A phone number must be disassociated
        from any users or Amazon Chime Voice Connectors before it can be deleted.

        Deleted phone numbers remain in the **Deletion queue** for 7 days before they are deleted
        permanently.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeletePhoneNumber>`_

        **Request Syntax**
        ::

          response = client.delete_phone_number(
              PhoneNumberId='string'
          )
        :type PhoneNumberId: string
        :param PhoneNumberId: **[REQUIRED]**

          The phone number ID.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_room(self, AccountId: str, RoomId: str) -> None:
        """
        Deletes a chat room.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteRoom>`_

        **Request Syntax**
        ::

          response = client.delete_room(
              AccountId='string',
              RoomId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type RoomId: string
        :param RoomId: **[REQUIRED]**

          The chat room ID.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_room_membership(
        self, AccountId: str, RoomId: str, MemberId: str
    ) -> None:
        """
        Removes a member from a chat room.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteRoomMembership>`_

        **Request Syntax**
        ::

          response = client.delete_room_membership(
              AccountId='string',
              RoomId='string',
              MemberId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type RoomId: string
        :param RoomId: **[REQUIRED]**

          The room ID.

        :type MemberId: string
        :param MemberId: **[REQUIRED]**

          The member ID (user ID or bot ID).

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector(self, VoiceConnectorId: str) -> None:
        """
        Deletes the specified Amazon Chime Voice Connector. Any phone numbers associated with the Amazon
        Chime Voice Connector must be disassociated from it before it can be deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnector>`_

        **Request Syntax**
        ::

          response = client.delete_voice_connector(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_group(self, VoiceConnectorGroupId: str) -> None:
        """
        Deletes the specified Amazon Chime Voice Connector group. Any ``VoiceConnectorItems`` and phone
        numbers associated with the group must be removed before it can be deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorGroup>`_

        **Request Syntax**
        ::

          response = client.delete_voice_connector_group(
              VoiceConnectorGroupId='string'
          )
        :type VoiceConnectorGroupId: string
        :param VoiceConnectorGroupId: **[REQUIRED]**

          The Amazon Chime Voice Connector group ID.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_origination(self, VoiceConnectorId: str) -> None:
        """
        Deletes the origination settings for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorOrigination>`_

        **Request Syntax**
        ::

          response = client.delete_voice_connector_origination(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str
    ) -> None:
        """
        Deletes the streaming configuration for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorStreamingConfiguration>`_
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorStreamingConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_voice_connector_streaming_configuration(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_termination(self, VoiceConnectorId: str) -> None:
        """
        Deletes the termination settings for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorTermination>`_

        **Request Syntax**
        ::

          response = client.delete_voice_connector_termination(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_connector_termination_credentials(
        self, VoiceConnectorId: str, Usernames: List[str] = None
    ) -> None:
        """
        Deletes the specified SIP credentials used by your equipment to authenticate during call
        termination.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorTerminationCredentials>`_
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorTerminationCredentials>`_

        **Request Syntax**
        ::

          response = client.delete_voice_connector_termination_credentials(
              VoiceConnectorId='string',
              Usernames=[
                  'string',
              ]
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type Usernames: list
        :param Usernames:

          The RFC2617 compliant username associated with the SIP credentials, in US-ASCII format.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_phone_number_from_user(
        self, AccountId: str, UserId: str
    ) -> Dict[str, Any]:
        """
        Disassociates the primary provisioned phone number from the specified Amazon Chime user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DisassociatePhoneNumberFromUser>`_

        **Request Syntax**
        ::

          response = client.disassociate_phone_number_from_user(
              AccountId='string',
              UserId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The user ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_phone_numbers_from_voice_connector(
        self, VoiceConnectorId: str, E164PhoneNumbers: List[str] = None
    ) -> ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
        """
        Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DisassociatePhoneNumbersFromVoiceConnector>`_
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DisassociatePhoneNumbersFromVoiceConnector>`_

        **Request Syntax**
        ::

          response = client.disassociate_phone_numbers_from_voice_connector(
              VoiceConnectorId='string',
              E164PhoneNumbers=[
                  'string',
              ]
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type E164PhoneNumbers: list
        :param E164PhoneNumbers:

          List of phone numbers, in E.164 format.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberErrors** *(list) --*

              If the action fails for one or more of the phone numbers in the request, a list of the phone
              numbers is returned, along with error codes and error messages.

              - *(dict) --*

                If the phone number action fails for one or more of the phone numbers in the request, a
                list of the phone numbers is returned, along with error codes and error messages.

                - **PhoneNumberId** *(string) --*

                  The phone number ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_phone_numbers_from_voice_connector_group(
        self, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str] = None
    ) -> ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
        """
        Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DisassociatePhoneNumbersFromVoiceConnectorGroup>`_
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DisassociatePhoneNumbersFromVoiceConnectorGroup>`_

        **Request Syntax**
        ::

          response = client.disassociate_phone_numbers_from_voice_connector_group(
              VoiceConnectorGroupId='string',
              E164PhoneNumbers=[
                  'string',
              ]
          )
        :type VoiceConnectorGroupId: string
        :param VoiceConnectorGroupId: **[REQUIRED]**

          The Amazon Chime Voice Connector group ID.

        :type E164PhoneNumbers: list
        :param E164PhoneNumbers:

          List of phone numbers, in E.164 format.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode':
                        'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'
                        |'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'
                        |'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'
                        |'PhoneNumberAssociationsExist',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberErrors** *(list) --*

              If the action fails for one or more of the phone numbers in the request, a list of the phone
              numbers is returned, along with error codes and error messages.

              - *(dict) --*

                If the phone number action fails for one or more of the phone numbers in the request, a
                list of the phone numbers is returned, along with error codes and error messages.

                - **PhoneNumberId** *(string) --*

                  The phone number ID for which the action failed.

                - **ErrorCode** *(string) --*

                  The error code.

                - **ErrorMessage** *(string) --*

                  The error message.

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
    def get_account(self, AccountId: str) -> ClientGetAccountResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime account, such as account type and supported
        licenses.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetAccount>`_

        **Request Syntax**
        ::

          response = client.get_account(
              AccountId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Account': {
                    'AwsAccountId': 'string',
                    'AccountId': 'string',
                    'Name': 'string',
                    'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'SupportedLicenses': [
                        'Basic'|'Plus'|'Pro'|'ProTrial',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Account** *(dict) --*

              The Amazon Chime account details.

              - **AwsAccountId** *(string) --*

                The AWS account ID.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **Name** *(string) --*

                The Amazon Chime account name.

              - **AccountType** *(string) --*

                The Amazon Chime account type. For more information about different account types, see
                `Managing Your Amazon Chime Accounts
                <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
                Chime Administration Guide* .

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime account creation timestamp, in ISO 8601 format.

              - **DefaultLicense** *(string) --*

                The default license for the Amazon Chime account.

              - **SupportedLicenses** *(list) --*

                Supported licenses for the Amazon Chime account.

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_account_settings(
        self, AccountId: str
    ) -> ClientGetAccountSettingsResponseTypeDef:
        """
        Retrieves account settings for the specified Amazon Chime account ID, such as remote control and
        dial out settings. For more information about these settings, see `Use the Policies Page
        <https://docs.aws.amazon.com/chime/latest/ag/policies.html>`__ in the *Amazon Chime Administration
        Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetAccountSettings>`_

        **Request Syntax**
        ::

          response = client.get_account_settings(
              AccountId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AccountSettings': {
                    'DisableRemoteControl': True|False,
                    'EnableDialOut': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **AccountSettings** *(dict) --*

              The Amazon Chime account settings.

              - **DisableRemoteControl** *(boolean) --*

                Setting that stops or starts remote control of shared screens during meetings.

              - **EnableDialOut** *(boolean) --*

                Setting that allows meeting participants to choose the **Call me at a phone number**
                option. For more information, see `Join a Meeting without the Amazon Chime App
                <https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bot(self, AccountId: str, BotId: str) -> ClientGetBotResponseTypeDef:
        """
        Retrieves details for the specified bot, such as bot email address, bot type, status, and display
        name.

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetBot>`_

        **Request Syntax**
        ::

          response = client.get_bot(
              AccountId='string',
              BotId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type BotId: string
        :param BotId: **[REQUIRED]**

          The bot ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Bot': {
                    'BotId': 'string',
                    'UserId': 'string',
                    'DisplayName': 'string',
                    'BotType': 'ChatBot',
                    'Disabled': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'BotEmail': 'string',
                    'SecurityToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Bot** *(dict) --*

              The chat bot details.

              - **BotId** *(string) --*

                The bot ID.

              - **UserId** *(string) --*

                The unique ID for the bot user.

              - **DisplayName** *(string) --*

                The bot display name.

              - **BotType** *(string) --*

                The bot type.

              - **Disabled** *(boolean) --*

                When true, the bot is stopped from running in your account.

              - **CreatedTimestamp** *(datetime) --*

                The bot creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated bot timestamp, in ISO 8601 format.

              - **BotEmail** *(string) --*

                The bot email address.

              - **SecurityToken** *(string) --*

                The security token used to authenticate Amazon Chime with the outgoing event endpoint.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_events_configuration(
        self, AccountId: str, BotId: str
    ) -> ClientGetEventsConfigurationResponseTypeDef:
        """
        Gets details for an events configuration that allows a bot to receive outgoing events, such as an
        HTTPS endpoint or Lambda function ARN.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetEventsConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_events_configuration(
              AccountId='string',
              BotId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type BotId: string
        :param BotId: **[REQUIRED]**

          The bot ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventsConfiguration': {
                    'BotId': 'string',
                    'OutboundEventsHTTPSEndpoint': 'string',
                    'LambdaFunctionArn': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EventsConfiguration** *(dict) --*

              The events configuration details.

              - **BotId** *(string) --*

                The bot ID.

              - **OutboundEventsHTTPSEndpoint** *(string) --*

                HTTPS endpoint that allows a bot to receive outgoing events.

              - **LambdaFunctionArn** *(string) --*

                Lambda function ARN that allows a bot to receive outgoing events.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_global_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetGlobalSettingsResponseTypeDef:
        """
        Retrieves global settings for the administrator's AWS account, such as Amazon Chime Business
        Calling and Amazon Chime Voice Connector settings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetGlobalSettings>`_

        **Request Syntax**

        ::

          response = client.get_global_settings()
        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'BusinessCalling': {
                    'CdrBucket': 'string'
                },
                'VoiceConnector': {
                    'CdrBucket': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **BusinessCalling** *(dict) --*

              The Amazon Chime Business Calling settings.

              - **CdrBucket** *(string) --*

                The Amazon S3 bucket designated for call detail record storage.

            - **VoiceConnector** *(dict) --*

              The Amazon Chime Voice Connector settings.

              - **CdrBucket** *(string) --*

                The Amazon S3 bucket designated for call detail record storage.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_phone_number(
        self, PhoneNumberId: str
    ) -> ClientGetPhoneNumberResponseTypeDef:
        """
        Retrieves details for the specified phone number ID, such as associations, capabilities, and
        product type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetPhoneNumber>`_

        **Request Syntax**
        ::

          response = client.get_phone_number(
              PhoneNumberId='string'
          )
        :type PhoneNumberId: string
        :param PhoneNumberId: **[REQUIRED]**

          The phone number ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumber': {
                    'PhoneNumberId': 'string',
                    'E164PhoneNumber': 'string',
                    'Type': 'Local'|'TollFree',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status':
                    'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'
                    |'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                    'Capabilities': {
                        'InboundCall': True|False,
                        'OutboundCall': True|False,
                        'InboundSMS': True|False,
                        'OutboundSMS': True|False,
                        'InboundMMS': True|False,
                        'OutboundMMS': True|False
                    },
                    'Associations': [
                        {
                            'Value': 'string',
                            'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                            'AssociatedTimestamp': datetime(2015, 1, 1)
                        },
                    ],
                    'CallingName': 'string',
                    'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'DeletionTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumber** *(dict) --*

              The phone number details.

              - **PhoneNumberId** *(string) --*

                The phone number ID.

              - **E164PhoneNumber** *(string) --*

                The phone number, in E.164 format.

              - **Type** *(string) --*

                The phone number type.

              - **ProductType** *(string) --*

                The phone number product type.

              - **Status** *(string) --*

                The phone number status.

              - **Capabilities** *(dict) --*

                The phone number capabilities.

                - **InboundCall** *(boolean) --*

                  Allows or denies inbound calling for the specified phone number.

                - **OutboundCall** *(boolean) --*

                  Allows or denies outbound calling for the specified phone number.

                - **InboundSMS** *(boolean) --*

                  Allows or denies inbound SMS messaging for the specified phone number.

                - **OutboundSMS** *(boolean) --*

                  Allows or denies outbound SMS messaging for the specified phone number.

                - **InboundMMS** *(boolean) --*

                  Allows or denies inbound MMS messaging for the specified phone number.

                - **OutboundMMS** *(boolean) --*

                  Allows or denies outbound MMS messaging for the specified phone number.

              - **Associations** *(list) --*

                The phone number associations.

                - *(dict) --*

                  The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
                  Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

                  - **Value** *(string) --*

                    Contains the ID for the entity specified in Name.

                  - **Name** *(string) --*

                    Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
                    Connector ID, or Amazon Chime Voice Connector group ID.

                  - **AssociatedTimestamp** *(datetime) --*

                    The timestamp of the phone number association, in ISO 8601 format.

              - **CallingName** *(string) --*

                The outbound calling name associated with the phone number.

              - **CallingNameStatus** *(string) --*

                The outbound calling name status.

              - **CreatedTimestamp** *(datetime) --*

                The phone number creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated phone number timestamp, in ISO 8601 format.

              - **DeletionTimestamp** *(datetime) --*

                The deleted phone number timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_phone_number_order(
        self, PhoneNumberOrderId: str
    ) -> ClientGetPhoneNumberOrderResponseTypeDef:
        """
        Retrieves details for the specified phone number order, such as order creation timestamp, phone
        numbers in E.164 format, product type, and order status.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetPhoneNumberOrder>`_

        **Request Syntax**
        ::

          response = client.get_phone_number_order(
              PhoneNumberOrderId='string'
          )
        :type PhoneNumberOrderId: string
        :param PhoneNumberOrderId: **[REQUIRED]**

          The ID for the phone number order.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberOrder': {
                    'PhoneNumberOrderId': 'string',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status': 'Processing'|'Successful'|'Failed'|'Partial',
                    'OrderedPhoneNumbers': [
                        {
                            'E164PhoneNumber': 'string',
                            'Status': 'Processing'|'Acquired'|'Failed'
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberOrder** *(dict) --*

              The phone number order details.

              - **PhoneNumberOrderId** *(string) --*

                The phone number order ID.

              - **ProductType** *(string) --*

                The phone number order product type.

              - **Status** *(string) --*

                The status of the phone number order.

              - **OrderedPhoneNumbers** *(list) --*

                The ordered phone number details, such as the phone number in E.164 format and the phone
                number status.

                - *(dict) --*

                  A phone number for which an order has been placed.

                  - **E164PhoneNumber** *(string) --*

                    The phone number, in E.164 format.

                  - **Status** *(string) --*

                    The phone number status.

              - **CreatedTimestamp** *(datetime) --*

                The phone number order creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated phone number order timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_phone_number_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetPhoneNumberSettingsResponseTypeDef:
        """
        Retrieves the phone number settings for the administrator's AWS account, such as the default
        outbound calling name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetPhoneNumberSettings>`_

        **Request Syntax**

        ::

          response = client.get_phone_number_settings()
        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CallingName': 'string',
                'CallingNameUpdatedTimestamp': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **CallingName** *(string) --*

              The default outbound calling name for the account.

            - **CallingNameUpdatedTimestamp** *(datetime) --*

              The updated outbound calling name timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_room(self, AccountId: str, RoomId: str) -> ClientGetRoomResponseTypeDef:
        """
        Retrieves room details, such as name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetRoom>`_

        **Request Syntax**
        ::

          response = client.get_room(
              AccountId='string',
              RoomId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type RoomId: string
        :param RoomId: **[REQUIRED]**

          The room ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Room': {
                    'RoomId': 'string',
                    'Name': 'string',
                    'AccountId': 'string',
                    'CreatedBy': 'string',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Room** *(dict) --*

              The room details.

              - **RoomId** *(string) --*

                The room ID.

              - **Name** *(string) --*

                The room name.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **CreatedBy** *(string) --*

                The identifier of the room creator.

              - **CreatedTimestamp** *(datetime) --*

                The room creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The room update timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user(self, AccountId: str, UserId: str) -> ClientGetUserResponseTypeDef:
        """
        Retrieves details for the specified user ID, such as primary email address, license type, and
        personal meeting PIN.

        To retrieve user details with an email address instead of a user ID, use the  ListUsers action, and
        then filter by email address.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetUser>`_

        **Request Syntax**
        ::

          response = client.get_user(
              AccountId='string',
              UserId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The user ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'User': {
                    'UserId': 'string',
                    'AccountId': 'string',
                    'PrimaryEmail': 'string',
                    'PrimaryProvisionedNumber': 'string',
                    'DisplayName': 'string',
                    'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                    'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                    'RegisteredOn': datetime(2015, 1, 1),
                    'InvitedOn': datetime(2015, 1, 1),
                    'PersonalPIN': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **User** *(dict) --*

              The user details.

              - **UserId** *(string) --*

                The user ID.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **PrimaryEmail** *(string) --*

                The primary email address of the user.

              - **PrimaryProvisionedNumber** *(string) --*

                The primary phone number associated with the user.

              - **DisplayName** *(string) --*

                The display name of the user.

              - **LicenseType** *(string) --*

                The license type for the user.

              - **UserRegistrationStatus** *(string) --*

                The user registration status.

              - **UserInvitationStatus** *(string) --*

                The user invite status.

              - **RegisteredOn** *(datetime) --*

                Date and time when the user is registered, in ISO 8601 format.

              - **InvitedOn** *(datetime) --*

                Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

              - **PersonalPIN** *(string) --*

                The user's personal meeting PIN.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_settings(
        self, AccountId: str, UserId: str
    ) -> ClientGetUserSettingsResponseTypeDef:
        """
        Retrieves settings for the specified user ID, such as any associated phone number settings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetUserSettings>`_

        **Request Syntax**
        ::

          response = client.get_user_settings(
              AccountId='string',
              UserId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The user ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserSettings': {
                    'Telephony': {
                        'InboundCalling': True|False,
                        'OutboundCalling': True|False,
                        'SMS': True|False
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **UserSettings** *(dict) --*

              The user settings.

              - **Telephony** *(dict) --*

                The telephony settings associated with the user.

                - **InboundCalling** *(boolean) --*

                  Allows or denies inbound calling.

                - **OutboundCalling** *(boolean) --*

                  Allows or denies outbound calling.

                - **SMS** *(boolean) --*

                  Allows or denies SMS messaging.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime Voice Connector, such as timestamps, name,
        outbound host, and encryption requirements.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnector>`_

        **Request Syntax**
        ::

          response = client.get_voice_connector(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VoiceConnector': {
                    'VoiceConnectorId': 'string',
                    'AwsRegion': 'us-east-1'|'us-west-2',
                    'Name': 'string',
                    'OutboundHostName': 'string',
                    'RequireEncryption': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **VoiceConnector** *(dict) --*

              The Amazon Chime Voice Connector details.

              - **VoiceConnectorId** *(string) --*

                The Amazon Chime Voice Connector ID.

              - **AwsRegion** *(string) --*

                The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
                .

              - **Name** *(string) --*

                The name of the Amazon Chime Voice Connector.

              - **OutboundHostName** *(string) --*

                The outbound host name for the Amazon Chime Voice Connector.

              - **RequireEncryption** *(boolean) --*

                Designates whether encryption is required for the Amazon Chime Voice Connector.

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_group(
        self, VoiceConnectorGroupId: str
    ) -> ClientGetVoiceConnectorGroupResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime Voice Connector group, such as timestamps, name,
        and associated ``VoiceConnectorItems`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorGroup>`_

        **Request Syntax**
        ::

          response = client.get_voice_connector_group(
              VoiceConnectorGroupId='string'
          )
        :type VoiceConnectorGroupId: string
        :param VoiceConnectorGroupId: **[REQUIRED]**

          The Amazon Chime Voice Connector group ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VoiceConnectorGroup': {
                    'VoiceConnectorGroupId': 'string',
                    'Name': 'string',
                    'VoiceConnectorItems': [
                        {
                            'VoiceConnectorId': 'string',
                            'Priority': 123
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **VoiceConnectorGroup** *(dict) --*

              The Amazon Chime Voice Connector group details.

              - **VoiceConnectorGroupId** *(string) --*

                The Amazon Chime Voice Connector group ID.

              - **Name** *(string) --*

                The name of the Amazon Chime Voice Connector group.

              - **VoiceConnectorItems** *(list) --*

                The Amazon Chime Voice Connectors to which to route inbound calls.

                - *(dict) --*

                  For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
                  route inbound calls. Includes priority configuration settings. Limit: 3
                  ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

                  - **VoiceConnectorId** *(string) --*

                    The Amazon Chime Voice Connector ID.

                  - **Priority** *(integer) --*

                    The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
                    priority. Higher priority Amazon Chime Voice Connectors are attempted first.

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_logging_configuration(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        Retrieves the logging configuration details for the specified Amazon Chime Voice Connector. Shows
        whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorLoggingConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_voice_connector_logging_configuration(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LoggingConfiguration': {
                    'EnableSIPLogs': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **LoggingConfiguration** *(dict) --*

              The logging configuration details.

              - **EnableSIPLogs** *(boolean) --*

                When true, enables SIP message logs for sending to Amazon CloudWatch Logs.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_origination(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorOriginationResponseTypeDef:
        """
        Retrieves origination setting details for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorOrigination>`_

        **Request Syntax**
        ::

          response = client.get_voice_connector_origination(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Origination': {
                    'Routes': [
                        {
                            'Host': 'string',
                            'Port': 123,
                            'Protocol': 'TCP'|'UDP',
                            'Priority': 123,
                            'Weight': 123
                        },
                    ],
                    'Disabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Origination** *(dict) --*

              The origination setting details.

              - **Routes** *(list) --*

                The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
                1. Maximum value of 20.

                - *(dict) --*

                  Origination routes define call distribution properties for your SIP hosts to receive
                  inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
                  each Amazon Chime Voice Connector.

                  - **Host** *(string) --*

                    The FQDN or IP address to contact for origination traffic.

                  - **Port** *(integer) --*

                    The designated origination route port. Defaults to 5060.

                  - **Protocol** *(string) --*

                    The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
                    Connectors use TCP protocol by default.

                  - **Priority** *(integer) --*

                    The priority associated with the host, with 1 being the highest priority. Higher
                    priority hosts are attempted first.

                  - **Weight** *(integer) --*

                    The weight associated with the host. If hosts are equal in priority, calls are
                    distributed among them based on their relative weight.

              - **Disabled** *(boolean) --*

                When origination settings are disabled, inbound calls are not enabled for your Amazon Chime
                Voice Connector.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        Retrieves the streaming configuration details for the specified Amazon Chime Voice Connector. Shows
        whether media streaming is enabled for sending to Amazon Kinesis. It also shows the retention
        period, in hours, for the Amazon Kinesis data.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorStreamingConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_voice_connector_streaming_configuration(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StreamingConfiguration': {
                    'DataRetentionInHours': 123,
                    'Disabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **StreamingConfiguration** *(dict) --*

              The streaming configuration details.

              - **DataRetentionInHours** *(integer) --*

                The retention period, in hours, for the Amazon Kinesis data.

              - **Disabled** *(boolean) --*

                When true, media streaming to Amazon Kinesis is turned off.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_termination(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorTerminationResponseTypeDef:
        """
        Retrieves termination setting details for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorTermination>`_

        **Request Syntax**
        ::

          response = client.get_voice_connector_termination(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Termination': {
                    'CpsLimit': 123,
                    'DefaultPhoneNumber': 'string',
                    'CallingRegions': [
                        'string',
                    ],
                    'CidrAllowedList': [
                        'string',
                    ],
                    'Disabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Termination** *(dict) --*

              The termination setting details.

              - **CpsLimit** *(integer) --*

                The limit on calls per second. Max value based on account service limit. Default value of 1.

              - **DefaultPhoneNumber** *(string) --*

                The default caller ID phone number.

              - **CallingRegions** *(list) --*

                The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

                - *(string) --*

              - **CidrAllowedList** *(list) --*

                The IP addresses allowed to make calls, in CIDR format. Required.

                - *(string) --*

              - **Disabled** *(boolean) --*

                When termination settings are disabled, outbound calls can not be made.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_connector_termination_health(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorTerminationHealthResponseTypeDef:
        """
        Retrieves information about the last time a SIP ``OPTIONS`` ping was received from your SIP
        infrastructure for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorTerminationHealth>`_

        **Request Syntax**
        ::

          response = client.get_voice_connector_termination_health(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TerminationHealth': {
                    'Timestamp': datetime(2015, 1, 1),
                    'Source': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **TerminationHealth** *(dict) --*

              The termination health details.

              - **Timestamp** *(datetime) --*

                The timestamp, in ISO 8601 format.

              - **Source** *(string) --*

                The source IP address.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invite_users(
        self, AccountId: str, UserEmailList: List[str]
    ) -> ClientInviteUsersResponseTypeDef:
        """
        Sends email to a maximum of 50 users, inviting them to the specified Amazon Chime ``Team`` account.
        Only ``Team`` account types are currently supported for this action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/InviteUsers>`_

        **Request Syntax**
        ::

          response = client.invite_users(
              AccountId='string',
              UserEmailList=[
                  'string',
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserEmailList: list
        :param UserEmailList: **[REQUIRED]**

          The user email addresses to which to send the email invitation.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Invites': [
                    {
                        'InviteId': 'string',
                        'Status': 'Pending'|'Accepted'|'Failed',
                        'EmailAddress': 'string',
                        'EmailStatus': 'NotSent'|'Sent'|'Failed'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Invites** *(list) --*

              The email invitation details.

              - *(dict) --*

                Invitation object returned after emailing users to invite them to join the Amazon Chime
                ``Team`` account.

                - **InviteId** *(string) --*

                  The invite ID.

                - **Status** *(string) --*

                  The status of the invite.

                - **EmailAddress** *(string) --*

                  The email address to which the invite is sent.

                - **EmailStatus** *(string) --*

                  The status of the invite email.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_accounts(
        self,
        Name: str = None,
        UserEmail: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListAccountsResponseTypeDef:
        """
        Lists the Amazon Chime accounts under the administrator's AWS account. You can filter accounts by
        account name prefix. To find out which Amazon Chime account a user belongs to, you can filter by
        the user's email address, which returns one account result.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListAccounts>`_

        **Request Syntax**
        ::

          response = client.list_accounts(
              Name='string',
              UserEmail='string',
              NextToken='string',
              MaxResults=123
          )
        :type Name: string
        :param Name:

          Amazon Chime account name prefix with which to filter results.

        :type UserEmail: string
        :param UserEmail:

          User email address with which to filter results.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call. Defaults to 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Accounts': [
                    {
                        'AwsAccountId': 'string',
                        'AccountId': 'string',
                        'Name': 'string',
                        'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                        'SupportedLicenses': [
                            'Basic'|'Plus'|'Pro'|'ProTrial',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Accounts** *(list) --*

              List of Amazon Chime accounts and account details.

              - *(dict) --*

                The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.

                - **AwsAccountId** *(string) --*

                  The AWS account ID.

                - **AccountId** *(string) --*

                  The Amazon Chime account ID.

                - **Name** *(string) --*

                  The Amazon Chime account name.

                - **AccountType** *(string) --*

                  The Amazon Chime account type. For more information about different account types, see
                  `Managing Your Amazon Chime Accounts
                  <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
                  Chime Administration Guide* .

                - **CreatedTimestamp** *(datetime) --*

                  The Amazon Chime account creation timestamp, in ISO 8601 format.

                - **DefaultLicense** *(string) --*

                  The default license for the Amazon Chime account.

                - **SupportedLicenses** *(list) --*

                  Supported licenses for the Amazon Chime account.

                  - *(string) --*

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bots(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListBotsResponseTypeDef:
        """
        Lists the bots associated with the administrator's Amazon Chime Enterprise account ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListBots>`_

        **Request Syntax**
        ::

          response = client.list_bots(
              AccountId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call. The default is 10.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Bots': [
                    {
                        'BotId': 'string',
                        'UserId': 'string',
                        'DisplayName': 'string',
                        'BotType': 'ChatBot',
                        'Disabled': True|False,
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1),
                        'BotEmail': 'string',
                        'SecurityToken': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Bots** *(list) --*

              List of bots and bot details.

              - *(dict) --*

                A resource that allows Enterprise account administrators to configure an interface to
                receive events from Amazon Chime.

                - **BotId** *(string) --*

                  The bot ID.

                - **UserId** *(string) --*

                  The unique ID for the bot user.

                - **DisplayName** *(string) --*

                  The bot display name.

                - **BotType** *(string) --*

                  The bot type.

                - **Disabled** *(boolean) --*

                  When true, the bot is stopped from running in your account.

                - **CreatedTimestamp** *(datetime) --*

                  The bot creation timestamp, in ISO 8601 format.

                - **UpdatedTimestamp** *(datetime) --*

                  The updated bot timestamp, in ISO 8601 format.

                - **BotEmail** *(string) --*

                  The bot email address.

                - **SecurityToken** *(string) --*

                  The security token used to authenticate Amazon Chime with the outgoing event endpoint.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_phone_number_orders(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListPhoneNumberOrdersResponseTypeDef:
        """
        Lists the phone number orders for the administrator's Amazon Chime account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListPhoneNumberOrders>`_

        **Request Syntax**
        ::

          response = client.list_phone_number_orders(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberOrders': [
                    {
                        'PhoneNumberOrderId': 'string',
                        'ProductType': 'BusinessCalling'|'VoiceConnector',
                        'Status': 'Processing'|'Successful'|'Failed'|'Partial',
                        'OrderedPhoneNumbers': [
                            {
                                'E164PhoneNumber': 'string',
                                'Status': 'Processing'|'Acquired'|'Failed'
                            },
                        ],
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberOrders** *(list) --*

              The phone number order details.

              - *(dict) --*

                The details of a phone number order created for Amazon Chime.

                - **PhoneNumberOrderId** *(string) --*

                  The phone number order ID.

                - **ProductType** *(string) --*

                  The phone number order product type.

                - **Status** *(string) --*

                  The status of the phone number order.

                - **OrderedPhoneNumbers** *(list) --*

                  The ordered phone number details, such as the phone number in E.164 format and the phone
                  number status.

                  - *(dict) --*

                    A phone number for which an order has been placed.

                    - **E164PhoneNumber** *(string) --*

                      The phone number, in E.164 format.

                    - **Status** *(string) --*

                      The phone number status.

                - **CreatedTimestamp** *(datetime) --*

                  The phone number order creation timestamp, in ISO 8601 format.

                - **UpdatedTimestamp** *(datetime) --*

                  The updated phone number order timestamp, in ISO 8601 format.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_phone_numbers(
        self,
        Status: str = None,
        ProductType: str = None,
        FilterName: str = None,
        FilterValue: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListPhoneNumbersResponseTypeDef:
        """
        Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, Amazon Chime
        Voice Connector, or Amazon Chime Voice Connector group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListPhoneNumbers>`_

        **Request Syntax**
        ::

          response = client.list_phone_numbers(
              Status=
                  'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'
                  |'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
              ProductType='BusinessCalling'|'VoiceConnector',
              FilterName='AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
              FilterValue='string',
              MaxResults=123,
              NextToken='string'
          )
        :type Status: string
        :param Status:

          The phone number status.

        :type ProductType: string
        :param ProductType:

          The phone number product type.

        :type FilterName: string
        :param FilterName:

          The filter to use to limit the number of results.

        :type FilterValue: string
        :param FilterValue:

          The value to use for the filter.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumbers': [
                    {
                        'PhoneNumberId': 'string',
                        'E164PhoneNumber': 'string',
                        'Type': 'Local'|'TollFree',
                        'ProductType': 'BusinessCalling'|'VoiceConnector',
                        'Status':
                        'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'
                        |'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                        'Capabilities': {
                            'InboundCall': True|False,
                            'OutboundCall': True|False,
                            'InboundSMS': True|False,
                            'OutboundSMS': True|False,
                            'InboundMMS': True|False,
                            'OutboundMMS': True|False
                        },
                        'Associations': [
                            {
                                'Value': 'string',
                                'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                                'AssociatedTimestamp': datetime(2015, 1, 1)
                            },
                        ],
                        'CallingName': 'string',
                        'CallingNameStatus':
                        'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1),
                        'DeletionTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumbers** *(list) --*

              The phone number details.

              - *(dict) --*

                A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.

                - **PhoneNumberId** *(string) --*

                  The phone number ID.

                - **E164PhoneNumber** *(string) --*

                  The phone number, in E.164 format.

                - **Type** *(string) --*

                  The phone number type.

                - **ProductType** *(string) --*

                  The phone number product type.

                - **Status** *(string) --*

                  The phone number status.

                - **Capabilities** *(dict) --*

                  The phone number capabilities.

                  - **InboundCall** *(boolean) --*

                    Allows or denies inbound calling for the specified phone number.

                  - **OutboundCall** *(boolean) --*

                    Allows or denies outbound calling for the specified phone number.

                  - **InboundSMS** *(boolean) --*

                    Allows or denies inbound SMS messaging for the specified phone number.

                  - **OutboundSMS** *(boolean) --*

                    Allows or denies outbound SMS messaging for the specified phone number.

                  - **InboundMMS** *(boolean) --*

                    Allows or denies inbound MMS messaging for the specified phone number.

                  - **OutboundMMS** *(boolean) --*

                    Allows or denies outbound MMS messaging for the specified phone number.

                - **Associations** *(list) --*

                  The phone number associations.

                  - *(dict) --*

                    The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
                    Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

                    - **Value** *(string) --*

                      Contains the ID for the entity specified in Name.

                    - **Name** *(string) --*

                      Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
                      Connector ID, or Amazon Chime Voice Connector group ID.

                    - **AssociatedTimestamp** *(datetime) --*

                      The timestamp of the phone number association, in ISO 8601 format.

                - **CallingName** *(string) --*

                  The outbound calling name associated with the phone number.

                - **CallingNameStatus** *(string) --*

                  The outbound calling name status.

                - **CreatedTimestamp** *(datetime) --*

                  The phone number creation timestamp, in ISO 8601 format.

                - **UpdatedTimestamp** *(datetime) --*

                  The updated phone number timestamp, in ISO 8601 format.

                - **DeletionTimestamp** *(datetime) --*

                  The deleted phone number timestamp, in ISO 8601 format.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_room_memberships(
        self, AccountId: str, RoomId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListRoomMembershipsResponseTypeDef:
        """
        Lists the membership details for the specified room, such as member IDs, member email addresses,
        and member names.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListRoomMemberships>`_

        **Request Syntax**
        ::

          response = client.list_room_memberships(
              AccountId='string',
              RoomId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type RoomId: string
        :param RoomId: **[REQUIRED]**

          The room ID.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RoomMemberships': [
                    {
                        'RoomId': 'string',
                        'Member': {
                            'MemberId': 'string',
                            'MemberType': 'User'|'Bot'|'Webhook',
                            'Email': 'string',
                            'FullName': 'string',
                            'AccountId': 'string'
                        },
                        'Role': 'Administrator'|'Member',
                        'InvitedBy': 'string',
                        'UpdatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **RoomMemberships** *(list) --*

              The room membership details.

              - *(dict) --*

                The room membership details.

                - **RoomId** *(string) --*

                  The room ID.

                - **Member** *(dict) --*

                  The member details, such as email address, name, member ID, and member type.

                  - **MemberId** *(string) --*

                    The member ID (user ID or bot ID).

                  - **MemberType** *(string) --*

                    The member type.

                  - **Email** *(string) --*

                    The member email address.

                  - **FullName** *(string) --*

                    The member name.

                  - **AccountId** *(string) --*

                    The Amazon Chime account ID.

                - **Role** *(string) --*

                  The membership role.

                - **InvitedBy** *(string) --*

                  The identifier of the user that invited the room member.

                - **UpdatedTimestamp** *(datetime) --*

                  The room membership update timestamp, in ISO 8601 format.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_rooms(
        self,
        AccountId: str,
        MemberId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListRoomsResponseTypeDef:
        """
        Lists the room details for the specified Amazon Chime account. Optionally, filter the results by a
        member ID (user ID or bot ID) to see a list of rooms that the member belongs to.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListRooms>`_

        **Request Syntax**
        ::

          response = client.list_rooms(
              AccountId='string',
              MemberId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type MemberId: string
        :param MemberId:

          The member ID (user ID or bot ID).

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Rooms': [
                    {
                        'RoomId': 'string',
                        'Name': 'string',
                        'AccountId': 'string',
                        'CreatedBy': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Rooms** *(list) --*

              The room details.

              - *(dict) --*

                The Amazon Chime chat room details.

                - **RoomId** *(string) --*

                  The room ID.

                - **Name** *(string) --*

                  The room name.

                - **AccountId** *(string) --*

                  The Amazon Chime account ID.

                - **CreatedBy** *(string) --*

                  The identifier of the room creator.

                - **CreatedTimestamp** *(datetime) --*

                  The room creation timestamp, in ISO 8601 format.

                - **UpdatedTimestamp** *(datetime) --*

                  The room update timestamp, in ISO 8601 format.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self,
        AccountId: str,
        UserEmail: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListUsersResponseTypeDef:
        """
        Lists the users that belong to the specified Amazon Chime account. You can specify an email address
        to list only the user that the email address belongs to.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListUsers>`_

        **Request Syntax**
        ::

          response = client.list_users(
              AccountId='string',
              UserEmail='string',
              MaxResults=123,
              NextToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserEmail: string
        :param UserEmail:

          Optional. The user email address used to filter results. Maximum 1.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call. Defaults to 100.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Users': [
                    {
                        'UserId': 'string',
                        'AccountId': 'string',
                        'PrimaryEmail': 'string',
                        'PrimaryProvisionedNumber': 'string',
                        'DisplayName': 'string',
                        'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                        'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                        'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                        'RegisteredOn': datetime(2015, 1, 1),
                        'InvitedOn': datetime(2015, 1, 1),
                        'PersonalPIN': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Users** *(list) --*

              List of users and user details.

              - *(dict) --*

                The user on the Amazon Chime account.

                - **UserId** *(string) --*

                  The user ID.

                - **AccountId** *(string) --*

                  The Amazon Chime account ID.

                - **PrimaryEmail** *(string) --*

                  The primary email address of the user.

                - **PrimaryProvisionedNumber** *(string) --*

                  The primary phone number associated with the user.

                - **DisplayName** *(string) --*

                  The display name of the user.

                - **LicenseType** *(string) --*

                  The license type for the user.

                - **UserRegistrationStatus** *(string) --*

                  The user registration status.

                - **UserInvitationStatus** *(string) --*

                  The user invite status.

                - **RegisteredOn** *(datetime) --*

                  Date and time when the user is registered, in ISO 8601 format.

                - **InvitedOn** *(datetime) --*

                  Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

                - **PersonalPIN** *(string) --*

                  The user's personal meeting PIN.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_voice_connector_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListVoiceConnectorGroupsResponseTypeDef:
        """
        Lists the Amazon Chime Voice Connector groups for the administrator's AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListVoiceConnectorGroups>`_

        **Request Syntax**
        ::

          response = client.list_voice_connector_groups(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VoiceConnectorGroups': [
                    {
                        'VoiceConnectorGroupId': 'string',
                        'Name': 'string',
                        'VoiceConnectorItems': [
                            {
                                'VoiceConnectorId': 'string',
                                'Priority': 123
                            },
                        ],
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **VoiceConnectorGroups** *(list) --*

              The details of the Amazon Chime Voice Connector groups.

              - *(dict) --*

                The Amazon Chime Voice Connector group configuration, including associated Amazon Chime
                Voice Connectors. You can include Amazon Chime Voice Connectors from different AWS Regions
                in your group. This creates a fault tolerant mechanism for fallback in case of availability
                events.

                - **VoiceConnectorGroupId** *(string) --*

                  The Amazon Chime Voice Connector group ID.

                - **Name** *(string) --*

                  The name of the Amazon Chime Voice Connector group.

                - **VoiceConnectorItems** *(list) --*

                  The Amazon Chime Voice Connectors to which to route inbound calls.

                  - *(dict) --*

                    For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
                    route inbound calls. Includes priority configuration settings. Limit: 3
                    ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

                    - **VoiceConnectorId** *(string) --*

                      The Amazon Chime Voice Connector ID.

                    - **Priority** *(integer) --*

                      The priority associated with the Amazon Chime Voice Connector, with 1 being the
                      highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.

                - **CreatedTimestamp** *(datetime) --*

                  The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

                - **UpdatedTimestamp** *(datetime) --*

                  The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_voice_connector_termination_credentials(
        self, VoiceConnectorId: str
    ) -> ClientListVoiceConnectorTerminationCredentialsResponseTypeDef:
        """
        Lists the SIP credentials for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListVoiceConnectorTerminationCredentials>`_
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListVoiceConnectorTerminationCredentials>`_

        **Request Syntax**
        ::

          response = client.list_voice_connector_termination_credentials(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Usernames': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Usernames** *(list) --*

              A list of user names.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_voice_connectors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListVoiceConnectorsResponseTypeDef:
        """
        Lists the Amazon Chime Voice Connectors for the administrator's AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListVoiceConnectors>`_

        **Request Syntax**
        ::

          response = client.list_voice_connectors(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VoiceConnectors': [
                    {
                        'VoiceConnectorId': 'string',
                        'AwsRegion': 'us-east-1'|'us-west-2',
                        'Name': 'string',
                        'OutboundHostName': 'string',
                        'RequireEncryption': True|False,
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **VoiceConnectors** *(list) --*

              The details of the Amazon Chime Voice Connectors.

              - *(dict) --*

                The Amazon Chime Voice Connector configuration, including outbound host name and encryption
                settings.

                - **VoiceConnectorId** *(string) --*

                  The Amazon Chime Voice Connector ID.

                - **AwsRegion** *(string) --*

                  The AWS Region in which the Amazon Chime Voice Connector is created. Default:
                  ``us-east-1`` .

                - **Name** *(string) --*

                  The name of the Amazon Chime Voice Connector.

                - **OutboundHostName** *(string) --*

                  The outbound host name for the Amazon Chime Voice Connector.

                - **RequireEncryption** *(boolean) --*

                  Designates whether encryption is required for the Amazon Chime Voice Connector.

                - **CreatedTimestamp** *(datetime) --*

                  The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

                - **UpdatedTimestamp** *(datetime) --*

                  The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def logout_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        Logs out the specified user from all of the devices they are currently logged into.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/LogoutUser>`_

        **Request Syntax**
        ::

          response = client.logout_user(
              AccountId='string',
              UserId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The user ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_events_configuration(
        self,
        AccountId: str,
        BotId: str,
        OutboundEventsHTTPSEndpoint: str = None,
        LambdaFunctionArn: str = None,
    ) -> ClientPutEventsConfigurationResponseTypeDef:
        """
        Creates an events configuration that allows a bot to receive outgoing events sent by Amazon Chime.
        Choose either an HTTPS endpoint or a Lambda function ARN. For more information, see  Bot .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutEventsConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_events_configuration(
              AccountId='string',
              BotId='string',
              OutboundEventsHTTPSEndpoint='string',
              LambdaFunctionArn='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type BotId: string
        :param BotId: **[REQUIRED]**

          The bot ID.

        :type OutboundEventsHTTPSEndpoint: string
        :param OutboundEventsHTTPSEndpoint:

          HTTPS endpoint that allows the bot to receive outgoing events.

        :type LambdaFunctionArn: string
        :param LambdaFunctionArn:

          Lambda function ARN that allows the bot to receive outgoing events.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventsConfiguration': {
                    'BotId': 'string',
                    'OutboundEventsHTTPSEndpoint': 'string',
                    'LambdaFunctionArn': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EventsConfiguration** *(dict) --*

              The configuration that allows a bot to receive outgoing events. Can be either an HTTPS
              endpoint or a Lambda function ARN.

              - **BotId** *(string) --*

                The bot ID.

              - **OutboundEventsHTTPSEndpoint** *(string) --*

                HTTPS endpoint that allows a bot to receive outgoing events.

              - **LambdaFunctionArn** *(string) --*

                Lambda function ARN that allows a bot to receive outgoing events.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_logging_configuration(
        self,
        VoiceConnectorId: str,
        LoggingConfiguration: ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef,
    ) -> ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        Adds a logging configuration for the specified Amazon Chime Voice Connector. The logging
        configuration specifies whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutVoiceConnectorLoggingConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_voice_connector_logging_configuration(
              VoiceConnectorId='string',
              LoggingConfiguration={
                  'EnableSIPLogs': True|False
              }
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type LoggingConfiguration: dict
        :param LoggingConfiguration: **[REQUIRED]**

          The logging configuration details to add.

          - **EnableSIPLogs** *(boolean) --*

            When true, enables SIP message logs for sending to Amazon CloudWatch Logs.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LoggingConfiguration': {
                    'EnableSIPLogs': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **LoggingConfiguration** *(dict) --*

              The updated logging configuration details.

              - **EnableSIPLogs** *(boolean) --*

                When true, enables SIP message logs for sending to Amazon CloudWatch Logs.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_origination(
        self,
        VoiceConnectorId: str,
        Origination: ClientPutVoiceConnectorOriginationOriginationTypeDef,
    ) -> ClientPutVoiceConnectorOriginationResponseTypeDef:
        """
        Adds origination settings for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutVoiceConnectorOrigination>`_

        **Request Syntax**
        ::

          response = client.put_voice_connector_origination(
              VoiceConnectorId='string',
              Origination={
                  'Routes': [
                      {
                          'Host': 'string',
                          'Port': 123,
                          'Protocol': 'TCP'|'UDP',
                          'Priority': 123,
                          'Weight': 123
                      },
                  ],
                  'Disabled': True|False
              }
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type Origination: dict
        :param Origination: **[REQUIRED]**

          The origination setting details to add.

          - **Routes** *(list) --*

            The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1.
            Maximum value of 20.

            - *(dict) --*

              Origination routes define call distribution properties for your SIP hosts to receive inbound
              calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon
              Chime Voice Connector.

              - **Host** *(string) --*

                The FQDN or IP address to contact for origination traffic.

              - **Port** *(integer) --*

                The designated origination route port. Defaults to 5060.

              - **Protocol** *(string) --*

                The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
                Connectors use TCP protocol by default.

              - **Priority** *(integer) --*

                The priority associated with the host, with 1 being the highest priority. Higher priority
                hosts are attempted first.

              - **Weight** *(integer) --*

                The weight associated with the host. If hosts are equal in priority, calls are distributed
                among them based on their relative weight.

          - **Disabled** *(boolean) --*

            When origination settings are disabled, inbound calls are not enabled for your Amazon Chime
            Voice Connector.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Origination': {
                    'Routes': [
                        {
                            'Host': 'string',
                            'Port': 123,
                            'Protocol': 'TCP'|'UDP',
                            'Priority': 123,
                            'Weight': 123
                        },
                    ],
                    'Disabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Origination** *(dict) --*

              The updated origination setting details.

              - **Routes** *(list) --*

                The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
                1. Maximum value of 20.

                - *(dict) --*

                  Origination routes define call distribution properties for your SIP hosts to receive
                  inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
                  each Amazon Chime Voice Connector.

                  - **Host** *(string) --*

                    The FQDN or IP address to contact for origination traffic.

                  - **Port** *(integer) --*

                    The designated origination route port. Defaults to 5060.

                  - **Protocol** *(string) --*

                    The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
                    Connectors use TCP protocol by default.

                  - **Priority** *(integer) --*

                    The priority associated with the host, with 1 being the highest priority. Higher
                    priority hosts are attempted first.

                  - **Weight** *(integer) --*

                    The weight associated with the host. If hosts are equal in priority, calls are
                    distributed among them based on their relative weight.

              - **Disabled** *(boolean) --*

                When origination settings are disabled, inbound calls are not enabled for your Amazon Chime
                Voice Connector.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_streaming_configuration(
        self,
        VoiceConnectorId: str,
        StreamingConfiguration: ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
    ) -> ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        Adds a streaming configuration for the specified Amazon Chime Voice Connector. The streaming
        configuration specifies whether media streaming is enabled for sending to Amazon Kinesis. It also
        sets the retention period, in hours, for the Amazon Kinesis data.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutVoiceConnectorStreamingConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_voice_connector_streaming_configuration(
              VoiceConnectorId='string',
              StreamingConfiguration={
                  'DataRetentionInHours': 123,
                  'Disabled': True|False
              }
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type StreamingConfiguration: dict
        :param StreamingConfiguration: **[REQUIRED]**

          The streaming configuration details to add.

          - **DataRetentionInHours** *(integer) --* **[REQUIRED]**

            The retention period, in hours, for the Amazon Kinesis data.

          - **Disabled** *(boolean) --*

            When true, media streaming to Amazon Kinesis is turned off.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StreamingConfiguration': {
                    'DataRetentionInHours': 123,
                    'Disabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **StreamingConfiguration** *(dict) --*

              The updated streaming configuration details.

              - **DataRetentionInHours** *(integer) --*

                The retention period, in hours, for the Amazon Kinesis data.

              - **Disabled** *(boolean) --*

                When true, media streaming to Amazon Kinesis is turned off.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_termination(
        self,
        VoiceConnectorId: str,
        Termination: ClientPutVoiceConnectorTerminationTerminationTypeDef,
    ) -> ClientPutVoiceConnectorTerminationResponseTypeDef:
        """
        Adds termination settings for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutVoiceConnectorTermination>`_

        **Request Syntax**
        ::

          response = client.put_voice_connector_termination(
              VoiceConnectorId='string',
              Termination={
                  'CpsLimit': 123,
                  'DefaultPhoneNumber': 'string',
                  'CallingRegions': [
                      'string',
                  ],
                  'CidrAllowedList': [
                      'string',
                  ],
                  'Disabled': True|False
              }
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type Termination: dict
        :param Termination: **[REQUIRED]**

          The termination setting details to add.

          - **CpsLimit** *(integer) --*

            The limit on calls per second. Max value based on account service limit. Default value of 1.

          - **DefaultPhoneNumber** *(string) --*

            The default caller ID phone number.

          - **CallingRegions** *(list) --*

            The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

            - *(string) --*

          - **CidrAllowedList** *(list) --*

            The IP addresses allowed to make calls, in CIDR format. Required.

            - *(string) --*

          - **Disabled** *(boolean) --*

            When termination settings are disabled, outbound calls can not be made.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Termination': {
                    'CpsLimit': 123,
                    'DefaultPhoneNumber': 'string',
                    'CallingRegions': [
                        'string',
                    ],
                    'CidrAllowedList': [
                        'string',
                    ],
                    'Disabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Termination** *(dict) --*

              The updated termination setting details.

              - **CpsLimit** *(integer) --*

                The limit on calls per second. Max value based on account service limit. Default value of 1.

              - **DefaultPhoneNumber** *(string) --*

                The default caller ID phone number.

              - **CallingRegions** *(list) --*

                The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

                - *(string) --*

              - **CidrAllowedList** *(list) --*

                The IP addresses allowed to make calls, in CIDR format. Required.

                - *(string) --*

              - **Disabled** *(boolean) --*

                When termination settings are disabled, outbound calls can not be made.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_voice_connector_termination_credentials(
        self,
        VoiceConnectorId: str,
        Credentials: List[
            ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef
        ] = None,
    ) -> None:
        """
        Adds termination SIP credentials for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutVoiceConnectorTerminationCredentials>`_

        **Request Syntax**
        ::

          response = client.put_voice_connector_termination_credentials(
              VoiceConnectorId='string',
              Credentials=[
                  {
                      'Username': 'string',
                      'Password': 'string'
                  },
              ]
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type Credentials: list
        :param Credentials:

          The termination SIP credentials.

          - *(dict) --*

            The SIP credentials used to authenticate requests to your Amazon Chime Voice Connector.

            - **Username** *(string) --*

              The RFC2617 compliant user name associated with the SIP credentials, in US-ASCII format.

            - **Password** *(string) --*

              The RFC2617 compliant password associated with the SIP credentials, in US-ASCII format.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def regenerate_security_token(
        self, AccountId: str, BotId: str
    ) -> ClientRegenerateSecurityTokenResponseTypeDef:
        """
        Regenerates the security token for a bot.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/RegenerateSecurityToken>`_

        **Request Syntax**
        ::

          response = client.regenerate_security_token(
              AccountId='string',
              BotId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type BotId: string
        :param BotId: **[REQUIRED]**

          The bot ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Bot': {
                    'BotId': 'string',
                    'UserId': 'string',
                    'DisplayName': 'string',
                    'BotType': 'ChatBot',
                    'Disabled': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'BotEmail': 'string',
                    'SecurityToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Bot** *(dict) --*

              A resource that allows Enterprise account administrators to configure an interface to receive
              events from Amazon Chime.

              - **BotId** *(string) --*

                The bot ID.

              - **UserId** *(string) --*

                The unique ID for the bot user.

              - **DisplayName** *(string) --*

                The bot display name.

              - **BotType** *(string) --*

                The bot type.

              - **Disabled** *(boolean) --*

                When true, the bot is stopped from running in your account.

              - **CreatedTimestamp** *(datetime) --*

                The bot creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated bot timestamp, in ISO 8601 format.

              - **BotEmail** *(string) --*

                The bot email address.

              - **SecurityToken** *(string) --*

                The security token used to authenticate Amazon Chime with the outgoing event endpoint.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_personal_pin(
        self, AccountId: str, UserId: str
    ) -> ClientResetPersonalPinResponseTypeDef:
        """
        Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the
        User object with the updated personal meeting PIN.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ResetPersonalPIN>`_

        **Request Syntax**
        ::

          response = client.reset_personal_pin(
              AccountId='string',
              UserId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The user ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'User': {
                    'UserId': 'string',
                    'AccountId': 'string',
                    'PrimaryEmail': 'string',
                    'PrimaryProvisionedNumber': 'string',
                    'DisplayName': 'string',
                    'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                    'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                    'RegisteredOn': datetime(2015, 1, 1),
                    'InvitedOn': datetime(2015, 1, 1),
                    'PersonalPIN': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **User** *(dict) --*

              The user details and new personal meeting PIN.

              - **UserId** *(string) --*

                The user ID.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **PrimaryEmail** *(string) --*

                The primary email address of the user.

              - **PrimaryProvisionedNumber** *(string) --*

                The primary phone number associated with the user.

              - **DisplayName** *(string) --*

                The display name of the user.

              - **LicenseType** *(string) --*

                The license type for the user.

              - **UserRegistrationStatus** *(string) --*

                The user registration status.

              - **UserInvitationStatus** *(string) --*

                The user invite status.

              - **RegisteredOn** *(datetime) --*

                Date and time when the user is registered, in ISO 8601 format.

              - **InvitedOn** *(datetime) --*

                Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

              - **PersonalPIN** *(string) --*

                The user's personal meeting PIN.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_phone_number(
        self, PhoneNumberId: str
    ) -> ClientRestorePhoneNumberResponseTypeDef:
        """
        Moves a phone number from the **Deletion queue** back into the phone number **Inventory** .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/RestorePhoneNumber>`_

        **Request Syntax**
        ::

          response = client.restore_phone_number(
              PhoneNumberId='string'
          )
        :type PhoneNumberId: string
        :param PhoneNumberId: **[REQUIRED]**

          The phone number.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumber': {
                    'PhoneNumberId': 'string',
                    'E164PhoneNumber': 'string',
                    'Type': 'Local'|'TollFree',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status':
                    'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'
                    |'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                    'Capabilities': {
                        'InboundCall': True|False,
                        'OutboundCall': True|False,
                        'InboundSMS': True|False,
                        'OutboundSMS': True|False,
                        'InboundMMS': True|False,
                        'OutboundMMS': True|False
                    },
                    'Associations': [
                        {
                            'Value': 'string',
                            'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                            'AssociatedTimestamp': datetime(2015, 1, 1)
                        },
                    ],
                    'CallingName': 'string',
                    'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'DeletionTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumber** *(dict) --*

              The phone number details.

              - **PhoneNumberId** *(string) --*

                The phone number ID.

              - **E164PhoneNumber** *(string) --*

                The phone number, in E.164 format.

              - **Type** *(string) --*

                The phone number type.

              - **ProductType** *(string) --*

                The phone number product type.

              - **Status** *(string) --*

                The phone number status.

              - **Capabilities** *(dict) --*

                The phone number capabilities.

                - **InboundCall** *(boolean) --*

                  Allows or denies inbound calling for the specified phone number.

                - **OutboundCall** *(boolean) --*

                  Allows or denies outbound calling for the specified phone number.

                - **InboundSMS** *(boolean) --*

                  Allows or denies inbound SMS messaging for the specified phone number.

                - **OutboundSMS** *(boolean) --*

                  Allows or denies outbound SMS messaging for the specified phone number.

                - **InboundMMS** *(boolean) --*

                  Allows or denies inbound MMS messaging for the specified phone number.

                - **OutboundMMS** *(boolean) --*

                  Allows or denies outbound MMS messaging for the specified phone number.

              - **Associations** *(list) --*

                The phone number associations.

                - *(dict) --*

                  The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
                  Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

                  - **Value** *(string) --*

                    Contains the ID for the entity specified in Name.

                  - **Name** *(string) --*

                    Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
                    Connector ID, or Amazon Chime Voice Connector group ID.

                  - **AssociatedTimestamp** *(datetime) --*

                    The timestamp of the phone number association, in ISO 8601 format.

              - **CallingName** *(string) --*

                The outbound calling name associated with the phone number.

              - **CallingNameStatus** *(string) --*

                The outbound calling name status.

              - **CreatedTimestamp** *(datetime) --*

                The phone number creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated phone number timestamp, in ISO 8601 format.

              - **DeletionTimestamp** *(datetime) --*

                The deleted phone number timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_available_phone_numbers(
        self,
        AreaCode: str = None,
        City: str = None,
        Country: str = None,
        State: str = None,
        TollFreePrefix: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientSearchAvailablePhoneNumbersResponseTypeDef:
        """
        Searches phone numbers that can be ordered.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/SearchAvailablePhoneNumbers>`_

        **Request Syntax**
        ::

          response = client.search_available_phone_numbers(
              AreaCode='string',
              City='string',
              Country='string',
              State='string',
              TollFreePrefix='string',
              MaxResults=123,
              NextToken='string'
          )
        :type AreaCode: string
        :param AreaCode:

          The area code used to filter results.

        :type City: string
        :param City:

          The city used to filter results.

        :type Country: string
        :param Country:

          The country used to filter results.

        :type State: string
        :param State:

          The state used to filter results.

        :type TollFreePrefix: string
        :param TollFreePrefix:

          The toll-free prefix that you use to filter results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'E164PhoneNumbers': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **E164PhoneNumbers** *(list) --*

              List of phone numbers, in E.164 format.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_account(
        self, AccountId: str, Name: str = None
    ) -> ClientUpdateAccountResponseTypeDef:
        """
        Updates account details for the specified Amazon Chime account. Currently, only account name
        updates are supported for this action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateAccount>`_

        **Request Syntax**
        ::

          response = client.update_account(
              AccountId='string',
              Name='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type Name: string
        :param Name:

          The new name for the specified Amazon Chime account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Account': {
                    'AwsAccountId': 'string',
                    'AccountId': 'string',
                    'Name': 'string',
                    'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'SupportedLicenses': [
                        'Basic'|'Plus'|'Pro'|'ProTrial',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Account** *(dict) --*

              The updated Amazon Chime account details.

              - **AwsAccountId** *(string) --*

                The AWS account ID.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **Name** *(string) --*

                The Amazon Chime account name.

              - **AccountType** *(string) --*

                The Amazon Chime account type. For more information about different account types, see
                `Managing Your Amazon Chime Accounts
                <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
                Chime Administration Guide* .

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime account creation timestamp, in ISO 8601 format.

              - **DefaultLicense** *(string) --*

                The default license for the Amazon Chime account.

              - **SupportedLicenses** *(list) --*

                Supported licenses for the Amazon Chime account.

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_account_settings(
        self,
        AccountId: str,
        AccountSettings: ClientUpdateAccountSettingsAccountSettingsTypeDef,
    ) -> Dict[str, Any]:
        """
        Updates the settings for the specified Amazon Chime account. You can update settings for remote
        control of shared screens, or for the dial-out option. For more information about these settings,
        see `Use the Policies Page <https://docs.aws.amazon.com/chime/latest/ag/policies.html>`__ in the
        *Amazon Chime Administration Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateAccountSettings>`_

        **Request Syntax**
        ::

          response = client.update_account_settings(
              AccountId='string',
              AccountSettings={
                  'DisableRemoteControl': True|False,
                  'EnableDialOut': True|False
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type AccountSettings: dict
        :param AccountSettings: **[REQUIRED]**

          The Amazon Chime account settings to update.

          - **DisableRemoteControl** *(boolean) --*

            Setting that stops or starts remote control of shared screens during meetings.

          - **EnableDialOut** *(boolean) --*

            Setting that allows meeting participants to choose the **Call me at a phone number** option.
            For more information, see `Join a Meeting without the Amazon Chime App
            <https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_bot(
        self, AccountId: str, BotId: str, Disabled: bool = None
    ) -> ClientUpdateBotResponseTypeDef:
        """
        Updates the status of the specified bot, such as starting or stopping the bot from running in your
        Amazon Chime Enterprise account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateBot>`_

        **Request Syntax**
        ::

          response = client.update_bot(
              AccountId='string',
              BotId='string',
              Disabled=True|False
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type BotId: string
        :param BotId: **[REQUIRED]**

          The bot ID.

        :type Disabled: boolean
        :param Disabled:

          When true, stops the specified bot from running in your account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Bot': {
                    'BotId': 'string',
                    'UserId': 'string',
                    'DisplayName': 'string',
                    'BotType': 'ChatBot',
                    'Disabled': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'BotEmail': 'string',
                    'SecurityToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Bot** *(dict) --*

              The updated bot details.

              - **BotId** *(string) --*

                The bot ID.

              - **UserId** *(string) --*

                The unique ID for the bot user.

              - **DisplayName** *(string) --*

                The bot display name.

              - **BotType** *(string) --*

                The bot type.

              - **Disabled** *(boolean) --*

                When true, the bot is stopped from running in your account.

              - **CreatedTimestamp** *(datetime) --*

                The bot creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated bot timestamp, in ISO 8601 format.

              - **BotEmail** *(string) --*

                The bot email address.

              - **SecurityToken** *(string) --*

                The security token used to authenticate Amazon Chime with the outgoing event endpoint.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_global_settings(
        self,
        BusinessCalling: ClientUpdateGlobalSettingsBusinessCallingTypeDef,
        VoiceConnector: ClientUpdateGlobalSettingsVoiceConnectorTypeDef,
    ) -> None:
        """
        Updates global settings for the administrator's AWS account, such as Amazon Chime Business Calling
        and Amazon Chime Voice Connector settings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateGlobalSettings>`_

        **Request Syntax**
        ::

          response = client.update_global_settings(
              BusinessCalling={
                  'CdrBucket': 'string'
              },
              VoiceConnector={
                  'CdrBucket': 'string'
              }
          )
        :type BusinessCalling: dict
        :param BusinessCalling: **[REQUIRED]**

          The Amazon Chime Business Calling settings.

          - **CdrBucket** *(string) --*

            The Amazon S3 bucket designated for call detail record storage.

        :type VoiceConnector: dict
        :param VoiceConnector: **[REQUIRED]**

          The Amazon Chime Voice Connector settings.

          - **CdrBucket** *(string) --*

            The Amazon S3 bucket designated for call detail record storage.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_phone_number(
        self, PhoneNumberId: str, ProductType: str = None, CallingName: str = None
    ) -> ClientUpdatePhoneNumberResponseTypeDef:
        """
        Updates phone number details, such as product type or calling name, for the specified phone number
        ID. You can update one phone number detail at a time. For example, you can update either the
        product type or the calling name in one action.

        For toll-free numbers, you must use the Amazon Chime Voice Connector product type.

        Updates to outbound calling names can take up to 72 hours to complete. Pending updates to outbound
        calling names must be complete before you can request another update.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdatePhoneNumber>`_

        **Request Syntax**
        ::

          response = client.update_phone_number(
              PhoneNumberId='string',
              ProductType='BusinessCalling'|'VoiceConnector',
              CallingName='string'
          )
        :type PhoneNumberId: string
        :param PhoneNumberId: **[REQUIRED]**

          The phone number ID.

        :type ProductType: string
        :param ProductType:

          The product type.

        :type CallingName: string
        :param CallingName:

          The outbound calling name associated with the phone number.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumber': {
                    'PhoneNumberId': 'string',
                    'E164PhoneNumber': 'string',
                    'Type': 'Local'|'TollFree',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status':
                    'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'
                    |'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                    'Capabilities': {
                        'InboundCall': True|False,
                        'OutboundCall': True|False,
                        'InboundSMS': True|False,
                        'OutboundSMS': True|False,
                        'InboundMMS': True|False,
                        'OutboundMMS': True|False
                    },
                    'Associations': [
                        {
                            'Value': 'string',
                            'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                            'AssociatedTimestamp': datetime(2015, 1, 1)
                        },
                    ],
                    'CallingName': 'string',
                    'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'DeletionTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumber** *(dict) --*

              The updated phone number details.

              - **PhoneNumberId** *(string) --*

                The phone number ID.

              - **E164PhoneNumber** *(string) --*

                The phone number, in E.164 format.

              - **Type** *(string) --*

                The phone number type.

              - **ProductType** *(string) --*

                The phone number product type.

              - **Status** *(string) --*

                The phone number status.

              - **Capabilities** *(dict) --*

                The phone number capabilities.

                - **InboundCall** *(boolean) --*

                  Allows or denies inbound calling for the specified phone number.

                - **OutboundCall** *(boolean) --*

                  Allows or denies outbound calling for the specified phone number.

                - **InboundSMS** *(boolean) --*

                  Allows or denies inbound SMS messaging for the specified phone number.

                - **OutboundSMS** *(boolean) --*

                  Allows or denies outbound SMS messaging for the specified phone number.

                - **InboundMMS** *(boolean) --*

                  Allows or denies inbound MMS messaging for the specified phone number.

                - **OutboundMMS** *(boolean) --*

                  Allows or denies outbound MMS messaging for the specified phone number.

              - **Associations** *(list) --*

                The phone number associations.

                - *(dict) --*

                  The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
                  Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

                  - **Value** *(string) --*

                    Contains the ID for the entity specified in Name.

                  - **Name** *(string) --*

                    Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
                    Connector ID, or Amazon Chime Voice Connector group ID.

                  - **AssociatedTimestamp** *(datetime) --*

                    The timestamp of the phone number association, in ISO 8601 format.

              - **CallingName** *(string) --*

                The outbound calling name associated with the phone number.

              - **CallingNameStatus** *(string) --*

                The outbound calling name status.

              - **CreatedTimestamp** *(datetime) --*

                The phone number creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated phone number timestamp, in ISO 8601 format.

              - **DeletionTimestamp** *(datetime) --*

                The deleted phone number timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_phone_number_settings(self, CallingName: str) -> None:
        """
        Updates the phone number settings for the administrator's AWS account, such as the default outbound
        calling name. You can update the default outbound calling name once every seven days. Outbound
        calling names can take up to 72 hours to update.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdatePhoneNumberSettings>`_

        **Request Syntax**
        ::

          response = client.update_phone_number_settings(
              CallingName='string'
          )
        :type CallingName: string
        :param CallingName: **[REQUIRED]**

          The default outbound calling name for the account.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_room(
        self, AccountId: str, RoomId: str, Name: str = None
    ) -> ClientUpdateRoomResponseTypeDef:
        """
        Updates room details, such as the room name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateRoom>`_

        **Request Syntax**
        ::

          response = client.update_room(
              AccountId='string',
              RoomId='string',
              Name='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type RoomId: string
        :param RoomId: **[REQUIRED]**

          The room ID.

        :type Name: string
        :param Name:

          The room name.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Room': {
                    'RoomId': 'string',
                    'Name': 'string',
                    'AccountId': 'string',
                    'CreatedBy': 'string',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Room** *(dict) --*

              The room details.

              - **RoomId** *(string) --*

                The room ID.

              - **Name** *(string) --*

                The room name.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **CreatedBy** *(string) --*

                The identifier of the room creator.

              - **CreatedTimestamp** *(datetime) --*

                The room creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The room update timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_room_membership(
        self, AccountId: str, RoomId: str, MemberId: str, Role: str = None
    ) -> ClientUpdateRoomMembershipResponseTypeDef:
        """
        Updates room membership details, such as member role. The member role designates whether the member
        is a chat room administrator or a general chat room member. Member role can only be updated for
        user IDs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateRoomMembership>`_

        **Request Syntax**
        ::

          response = client.update_room_membership(
              AccountId='string',
              RoomId='string',
              MemberId='string',
              Role='Administrator'|'Member'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type RoomId: string
        :param RoomId: **[REQUIRED]**

          The room ID.

        :type MemberId: string
        :param MemberId: **[REQUIRED]**

          The member ID.

        :type Role: string
        :param Role:

          The role of the member.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RoomMembership': {
                    'RoomId': 'string',
                    'Member': {
                        'MemberId': 'string',
                        'MemberType': 'User'|'Bot'|'Webhook',
                        'Email': 'string',
                        'FullName': 'string',
                        'AccountId': 'string'
                    },
                    'Role': 'Administrator'|'Member',
                    'InvitedBy': 'string',
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **RoomMembership** *(dict) --*

              The room membership details.

              - **RoomId** *(string) --*

                The room ID.

              - **Member** *(dict) --*

                The member details, such as email address, name, member ID, and member type.

                - **MemberId** *(string) --*

                  The member ID (user ID or bot ID).

                - **MemberType** *(string) --*

                  The member type.

                - **Email** *(string) --*

                  The member email address.

                - **FullName** *(string) --*

                  The member name.

                - **AccountId** *(string) --*

                  The Amazon Chime account ID.

              - **Role** *(string) --*

                The membership role.

              - **InvitedBy** *(string) --*

                The identifier of the user that invited the room member.

              - **UpdatedTimestamp** *(datetime) --*

                The room membership update timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user(
        self, AccountId: str, UserId: str, LicenseType: str = None
    ) -> ClientUpdateUserResponseTypeDef:
        """
        Updates user details for a specified user ID. Currently, only ``LicenseType`` updates are supported
        for this action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateUser>`_

        **Request Syntax**
        ::

          response = client.update_user(
              AccountId='string',
              UserId='string',
              LicenseType='Basic'|'Plus'|'Pro'|'ProTrial'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The user ID.

        :type LicenseType: string
        :param LicenseType:

          The user license type to update. This must be a supported license type for the Amazon Chime
          account that the user belongs to.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'User': {
                    'UserId': 'string',
                    'AccountId': 'string',
                    'PrimaryEmail': 'string',
                    'PrimaryProvisionedNumber': 'string',
                    'DisplayName': 'string',
                    'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                    'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                    'RegisteredOn': datetime(2015, 1, 1),
                    'InvitedOn': datetime(2015, 1, 1),
                    'PersonalPIN': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **User** *(dict) --*

              The updated user details.

              - **UserId** *(string) --*

                The user ID.

              - **AccountId** *(string) --*

                The Amazon Chime account ID.

              - **PrimaryEmail** *(string) --*

                The primary email address of the user.

              - **PrimaryProvisionedNumber** *(string) --*

                The primary phone number associated with the user.

              - **DisplayName** *(string) --*

                The display name of the user.

              - **LicenseType** *(string) --*

                The license type for the user.

              - **UserRegistrationStatus** *(string) --*

                The user registration status.

              - **UserInvitationStatus** *(string) --*

                The user invite status.

              - **RegisteredOn** *(datetime) --*

                Date and time when the user is registered, in ISO 8601 format.

              - **InvitedOn** *(datetime) --*

                Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

              - **PersonalPIN** *(string) --*

                The user's personal meeting PIN.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_settings(
        self,
        AccountId: str,
        UserId: str,
        UserSettings: ClientUpdateUserSettingsUserSettingsTypeDef,
    ) -> None:
        """
        Updates the settings for the specified user, such as phone number settings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateUserSettings>`_

        **Request Syntax**
        ::

          response = client.update_user_settings(
              AccountId='string',
              UserId='string',
              UserSettings={
                  'Telephony': {
                      'InboundCalling': True|False,
                      'OutboundCalling': True|False,
                      'SMS': True|False
                  }
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The Amazon Chime account ID.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The user ID.

        :type UserSettings: dict
        :param UserSettings: **[REQUIRED]**

          The user settings to update.

          - **Telephony** *(dict) --* **[REQUIRED]**

            The telephony settings associated with the user.

            - **InboundCalling** *(boolean) --* **[REQUIRED]**

              Allows or denies inbound calling.

            - **OutboundCalling** *(boolean) --* **[REQUIRED]**

              Allows or denies outbound calling.

            - **SMS** *(boolean) --* **[REQUIRED]**

              Allows or denies SMS messaging.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_voice_connector(
        self, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> ClientUpdateVoiceConnectorResponseTypeDef:
        """
        Updates details for the specified Amazon Chime Voice Connector.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateVoiceConnector>`_

        **Request Syntax**
        ::

          response = client.update_voice_connector(
              VoiceConnectorId='string',
              Name='string',
              RequireEncryption=True|False
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**

          The Amazon Chime Voice Connector ID.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the Amazon Chime Voice Connector.

        :type RequireEncryption: boolean
        :param RequireEncryption: **[REQUIRED]**

          When enabled, requires encryption for the Amazon Chime Voice Connector.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VoiceConnector': {
                    'VoiceConnectorId': 'string',
                    'AwsRegion': 'us-east-1'|'us-west-2',
                    'Name': 'string',
                    'OutboundHostName': 'string',
                    'RequireEncryption': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **VoiceConnector** *(dict) --*

              The updated Amazon Chime Voice Connector details.

              - **VoiceConnectorId** *(string) --*

                The Amazon Chime Voice Connector ID.

              - **AwsRegion** *(string) --*

                The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
                .

              - **Name** *(string) --*

                The name of the Amazon Chime Voice Connector.

              - **OutboundHostName** *(string) --*

                The outbound host name for the Amazon Chime Voice Connector.

              - **RequireEncryption** *(boolean) --*

                Designates whether encryption is required for the Amazon Chime Voice Connector.

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        Name: str,
        VoiceConnectorItems: List[
            ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
    ) -> ClientUpdateVoiceConnectorGroupResponseTypeDef:
        """
        Updates details for the specified Amazon Chime Voice Connector group, such as the name and Amazon
        Chime Voice Connector priority ranking.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateVoiceConnectorGroup>`_

        **Request Syntax**
        ::

          response = client.update_voice_connector_group(
              VoiceConnectorGroupId='string',
              Name='string',
              VoiceConnectorItems=[
                  {
                      'VoiceConnectorId': 'string',
                      'Priority': 123
                  },
              ]
          )
        :type VoiceConnectorGroupId: string
        :param VoiceConnectorGroupId: **[REQUIRED]**

          The Amazon Chime Voice Connector group ID.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the Amazon Chime Voice Connector group.

        :type VoiceConnectorItems: list
        :param VoiceConnectorItems: **[REQUIRED]**

          The ``VoiceConnectorItems`` to associate with the group.

          - *(dict) --*

            For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route
            inbound calls. Includes priority configuration settings. Limit: 3 ``VoiceConnectorItems`` per
            Amazon Chime Voice Connector group.

            - **VoiceConnectorId** *(string) --* **[REQUIRED]**

              The Amazon Chime Voice Connector ID.

            - **Priority** *(integer) --* **[REQUIRED]**

              The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
              priority. Higher priority Amazon Chime Voice Connectors are attempted first.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VoiceConnectorGroup': {
                    'VoiceConnectorGroupId': 'string',
                    'Name': 'string',
                    'VoiceConnectorItems': [
                        {
                            'VoiceConnectorId': 'string',
                            'Priority': 123
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **VoiceConnectorGroup** *(dict) --*

              The updated Amazon Chime Voice Connector group details.

              - **VoiceConnectorGroupId** *(string) --*

                The Amazon Chime Voice Connector group ID.

              - **Name** *(string) --*

                The name of the Amazon Chime Voice Connector group.

              - **VoiceConnectorItems** *(list) --*

                The Amazon Chime Voice Connectors to which to route inbound calls.

                - *(dict) --*

                  For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
                  route inbound calls. Includes priority configuration settings. Limit: 3
                  ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

                  - **VoiceConnectorId** *(string) --*

                    The Amazon Chime Voice Connector ID.

                  - **Priority** *(integer) --*

                    The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
                    priority. Higher priority Amazon Chime Voice Connectors are attempted first.

              - **CreatedTimestamp** *(datetime) --*

                The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

              - **UpdatedTimestamp** *(datetime) --*

                The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_accounts"]
    ) -> paginator_scope.ListAccountsPaginator:
        """
        Get Paginator for `list_accounts` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> paginator_scope.ListUsersPaginator:
        """
        Get Paginator for `list_users` operation.
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
    AccessDeniedException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ServiceFailureException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottledClientException: Boto3ClientError
    UnauthorizedClientException: Boto3ClientError
    UnprocessableEntityException: Boto3ClientError
