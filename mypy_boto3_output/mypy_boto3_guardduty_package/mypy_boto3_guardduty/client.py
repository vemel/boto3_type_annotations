"Main interface for guardduty Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_guardduty.client as client_scope

# pylint: disable=import-self
import mypy_boto3_guardduty.paginator as paginator_scope
from mypy_boto3_guardduty.type_defs import (
    ClientCreateDetectorResponseTypeDef,
    ClientCreateFilterFindingCriteriaTypeDef,
    ClientCreateFilterResponseTypeDef,
    ClientCreateIpSetResponseTypeDef,
    ClientCreateMembersAccountDetailsTypeDef,
    ClientCreateMembersResponseTypeDef,
    ClientCreatePublishingDestinationDestinationPropertiesTypeDef,
    ClientCreatePublishingDestinationResponseTypeDef,
    ClientCreateThreatIntelSetResponseTypeDef,
    ClientDeclineInvitationsResponseTypeDef,
    ClientDeleteInvitationsResponseTypeDef,
    ClientDeleteMembersResponseTypeDef,
    ClientDescribePublishingDestinationResponseTypeDef,
    ClientDisassociateMembersResponseTypeDef,
    ClientGetDetectorResponseTypeDef,
    ClientGetFilterResponseTypeDef,
    ClientGetFindingsResponseTypeDef,
    ClientGetFindingsSortCriteriaTypeDef,
    ClientGetFindingsStatisticsFindingCriteriaTypeDef,
    ClientGetFindingsStatisticsResponseTypeDef,
    ClientGetInvitationsCountResponseTypeDef,
    ClientGetIpSetResponseTypeDef,
    ClientGetMasterAccountResponseTypeDef,
    ClientGetMembersResponseTypeDef,
    ClientGetThreatIntelSetResponseTypeDef,
    ClientInviteMembersResponseTypeDef,
    ClientListDetectorsResponseTypeDef,
    ClientListFiltersResponseTypeDef,
    ClientListFindingsFindingCriteriaTypeDef,
    ClientListFindingsResponseTypeDef,
    ClientListFindingsSortCriteriaTypeDef,
    ClientListInvitationsResponseTypeDef,
    ClientListIpSetsResponseTypeDef,
    ClientListMembersResponseTypeDef,
    ClientListPublishingDestinationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListThreatIntelSetsResponseTypeDef,
    ClientStartMonitoringMembersResponseTypeDef,
    ClientStopMonitoringMembersResponseTypeDef,
    ClientUpdateFilterFindingCriteriaTypeDef,
    ClientUpdateFilterResponseTypeDef,
    ClientUpdatePublishingDestinationDestinationPropertiesTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_invitation(
        self, DetectorId: str, MasterId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        Accepts the invitation to be monitored by a master GuardDuty account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/AcceptInvitation>`_

        **Request Syntax**
        ::

          response = client.accept_invitation(
              DetectorId='string',
              MasterId='string',
              InvitationId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty member account.

        :type MasterId: string
        :param MasterId: **[REQUIRED]**

          The account ID of the master GuardDuty account whose invitation you're accepting.

        :type InvitationId: string
        :param InvitationId: **[REQUIRED]**

          This value is used to validate the master account to the member account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def archive_findings(
        self, DetectorId: str, FindingIds: List[str]
    ) -> Dict[str, Any]:
        """
        Archives GuardDuty findings specified by the list of finding IDs.

        .. note::

          Only the master account can archive findings. Member accounts do not have permission to archive
          findings from their accounts.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ArchiveFindings>`_

        **Request Syntax**
        ::

          response = client.archive_findings(
              DetectorId='string',
              FindingIds=[
                  'string',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector that specifies the GuardDuty service whose findings you want to archive.

        :type FindingIds: list
        :param FindingIds: **[REQUIRED]**

          IDs of the findings that you want to archive.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
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
    def create_detector(
        self,
        Enable: bool,
        ClientToken: str = None,
        FindingPublishingFrequency: str = None,
        Tags: List[str] = None,
    ) -> ClientCreateDetectorResponseTypeDef:
        """
        Creates a single Amazon GuardDuty detector. A detector is a resource that represents the GuardDuty
        service. To start using GuardDuty, you must create a detector in each region that you enable the
        service. You can have only one detector per account per region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateDetector>`_

        **Request Syntax**
        ::

          response = client.create_detector(
              Enable=True|False,
              ClientToken='string',
              FindingPublishingFrequency='FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
              Tags={
                  'string': 'string'
              }
          )
        :type Enable: boolean
        :param Enable: **[REQUIRED]**

          A boolean value that specifies whether the detector is to be enabled.

        :type ClientToken: string
        :param ClientToken:

          The idempotency token for the create request.

          This field is autopopulated if not provided.

        :type FindingPublishingFrequency: string
        :param FindingPublishingFrequency:

          A enum value that specifies how frequently customer got Finding updates published.

        :type Tags: dict
        :param Tags:

          The tags to be added to a new detector resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DetectorId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DetectorId** *(string) --*

              The unique ID of the created detector.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_filter(
        self,
        DetectorId: str,
        Name: str,
        FindingCriteria: ClientCreateFilterFindingCriteriaTypeDef,
        Description: str = None,
        Action: str = None,
        Rank: int = None,
        ClientToken: str = None,
        Tags: List[str] = None,
    ) -> ClientCreateFilterResponseTypeDef:
        """
        Creates a filter using the specified finding criteria.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateFilter>`_

        **Request Syntax**
        ::

          response = client.create_filter(
              DetectorId='string',
              Name='string',
              Description='string',
              Action='NOOP'|'ARCHIVE',
              Rank=123,
              FindingCriteria={
                  'Criterion': {
                      'string': {
                          'Eq': [
                              'string',
                          ],
                          'Neq': [
                              'string',
                          ],
                          'Gt': 123,
                          'Gte': 123,
                          'Lt': 123,
                          'Lte': 123,
                          'Equals': [
                              'string',
                          ],
                          'NotEquals': [
                              'string',
                          ],
                          'GreaterThan': 123,
                          'GreaterThanOrEqual': 123,
                          'LessThan': 123,
                          'LessThanOrEqual': 123
                      }
                  }
              },
              ClientToken='string',
              Tags={
                  'string': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account for which you want to create a filter.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the filter.

        :type Description: string
        :param Description:

          The description of the filter.

        :type Action: string
        :param Action:

          Specifies the action that is to be applied to the findings that match the filter.

        :type Rank: integer
        :param Rank:

          Specifies the position of the filter in the list of current filters. Also specifies the order in
          which this filter is applied to the findings.

        :type FindingCriteria: dict
        :param FindingCriteria: **[REQUIRED]**

          Represents the criteria to be used in the filter for querying findings.

          - **Criterion** *(dict) --*

            Represents a map of finding properties that match specified conditions and values when querying
            findings.

            - *(string) --*

              - *(dict) --*

                Contains information about the condition.

                - **Eq** *(list) --*

                  Represents the equal condition to be applied to a single field when querying for findings.

                  - *(string) --*

                - **Neq** *(list) --*

                  Represents the not equal condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **Gt** *(integer) --*

                  Represents a greater than condition to be applied to a single field when querying for
                  findings.

                - **Gte** *(integer) --*

                  Represents a greater than equal condition to be applied to a single field when querying
                  for findings.

                - **Lt** *(integer) --*

                  Represents a less than condition to be applied to a single field when querying for
                  findings.

                - **Lte** *(integer) --*

                  Represents a less than equal condition to be applied to a single field when querying for
                  findings.

                - **Equals** *(list) --*

                  Represents an **equal** condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **NotEquals** *(list) --*

                  Represents an **not equal** condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **GreaterThan** *(integer) --*

                  Represents a greater than condition to be applied to a single field when querying for
                  findings.

                - **GreaterThanOrEqual** *(integer) --*

                  Represents a greater than equal condition to be applied to a single field when querying
                  for findings.

                - **LessThan** *(integer) --*

                  Represents a less than condition to be applied to a single field when querying for
                  findings.

                - **LessThanOrEqual** *(integer) --*

                  Represents a less than equal condition to be applied to a single field when querying for
                  findings.

        :type ClientToken: string
        :param ClientToken:

          The idempotency token for the create request.

          This field is autopopulated if not provided.

        :type Tags: dict
        :param Tags:

          The tags to be added to a new filter resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the successfully created filter.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ip_set(
        self,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: List[str] = None,
    ) -> ClientCreateIpSetResponseTypeDef:
        """
        Creates a new IPSet, called Trusted IP list in the consoler user interface. An IPSet is a list IP
        addresses trusted for secure communication with AWS infrastructure and applications. GuardDuty does
        not generate findings for IP addresses included in IPSets. Only users from the master account can
        use this operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateIPSet>`_

        **Request Syntax**
        ::

          response = client.create_ip_set(
              DetectorId='string',
              Name='string',
              Format='TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
              Location='string',
              Activate=True|False,
              ClientToken='string',
              Tags={
                  'string': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account for which you want to create an IPSet.

        :type Name: string
        :param Name: **[REQUIRED]**

          The user friendly name to identify the IPSet. This name is displayed in all findings that are
          triggered by activity that involves IP addresses included in this IPSet.

        :type Format: string
        :param Format: **[REQUIRED]**

          The format of the file that contains the IPSet.

        :type Location: string
        :param Location: **[REQUIRED]**

          The URI of the file that contains the IPSet. For example
          (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)

        :type Activate: boolean
        :param Activate: **[REQUIRED]**

          A boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.

        :type ClientToken: string
        :param ClientToken:

          The idempotency token for the create request.

          This field is autopopulated if not provided.

        :type Tags: dict
        :param Tags:

          The tags to be added to a new IP set resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IpSetId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **IpSetId** *(string) --*

              The ID of the IPSet resource.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_members(
        self,
        DetectorId: str,
        AccountDetails: List[ClientCreateMembersAccountDetailsTypeDef],
    ) -> ClientCreateMembersResponseTypeDef:
        """
        Creates member accounts of the current AWS account by specifying a list of AWS account IDs. The
        current AWS account can then invite these members to manage GuardDuty in their accounts.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateMembers>`_

        **Request Syntax**
        ::

          response = client.create_members(
              DetectorId='string',
              AccountDetails=[
                  {
                      'AccountId': 'string',
                      'Email': 'string'
                  },
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account with which you want to associate member
          accounts.

        :type AccountDetails: list
        :param AccountDetails: **[REQUIRED]**

          A list of account ID and email address pairs of the accounts that you want to associate with the
          master GuardDuty account.

          - *(dict) --*

            Contains information about the account.

            - **AccountId** *(string) --* **[REQUIRED]**

              Member account ID.

            - **Email** *(string) --* **[REQUIRED]**

              Member account's email address.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of objects containing the unprocessed account and a result string explaining why it
              was unprocessed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_publishing_destination(
        self,
        DetectorId: str,
        DestinationType: str,
        DestinationProperties: ClientCreatePublishingDestinationDestinationPropertiesTypeDef,
        ClientToken: str = None,
    ) -> ClientCreatePublishingDestinationResponseTypeDef:
        """
        Creates a publishing destination to send findings to. The resource to send findings to must exist
        before you use this operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreatePublishingDestination>`_

        **Request Syntax**
        ::

          response = client.create_publishing_destination(
              DetectorId='string',
              DestinationType='S3',
              DestinationProperties={
                  'DestinationArn': 'string',
                  'KmsKeyArn': 'string'
              },
              ClientToken='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the GuardDuty detector associated with the publishing destination.

        :type DestinationType: string
        :param DestinationType: **[REQUIRED]**

          The type of resource for the publishing destination. Currently only S3 is supported.

        :type DestinationProperties: dict
        :param DestinationProperties: **[REQUIRED]**

          Properties of the publishing destination, including the ARNs for the destination and the KMS key
          used for encryption.

          - **DestinationArn** *(string) --*

            The ARN of the resource to publish to.

          - **KmsKeyArn** *(string) --*

            The ARN of the KMS key to use for encryption.

        :type ClientToken: string
        :param ClientToken:

          The idempotency token for the request.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DestinationId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DestinationId** *(string) --*

              The ID of the publishing destination created.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_sample_findings(
        self, DetectorId: str, FindingTypes: List[str] = None
    ) -> Dict[str, Any]:
        """
        Generates example findings of types specified by the list of finding types. If 'NULL' is specified
        for ``findingTypes`` , the API generates example findings of all supported finding types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateSampleFindings>`_

        **Request Syntax**
        ::

          response = client.create_sample_findings(
              DetectorId='string',
              FindingTypes=[
                  'string',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector to create sample findings for.

        :type FindingTypes: list
        :param FindingTypes:

          Types of sample findings to generate.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_threat_intel_set(
        self,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: List[str] = None,
    ) -> ClientCreateThreatIntelSetResponseTypeDef:
        """
        Create a new ThreatIntelSet. ThreatIntelSets consist of known malicious IP addresses. GuardDuty
        generates findings based on ThreatIntelSets. Only users of the master account can use this
        operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateThreatIntelSet>`_

        **Request Syntax**
        ::

          response = client.create_threat_intel_set(
              DetectorId='string',
              Name='string',
              Format='TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
              Location='string',
              Activate=True|False,
              ClientToken='string',
              Tags={
                  'string': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account for which you want to create a
          threatIntelSet.

        :type Name: string
        :param Name: **[REQUIRED]**

          A user-friendly ThreatIntelSet name that is displayed in all finding generated by activity that
          involves IP addresses included in this ThreatIntelSet.

        :type Format: string
        :param Format: **[REQUIRED]**

          The format of the file that contains the ThreatIntelSet.

        :type Location: string
        :param Location: **[REQUIRED]**

          The URI of the file that contains the ThreatIntelSet. For example
          (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).

        :type Activate: boolean
        :param Activate: **[REQUIRED]**

          A boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.

        :type ClientToken: string
        :param ClientToken:

          The idempotency token for the create request.

          This field is autopopulated if not provided.

        :type Tags: dict
        :param Tags:

          The tags to be added to a new Threat List resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ThreatIntelSetId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ThreatIntelSetId** *(string) --*

              The ID of the ThreatIntelSet resource.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decline_invitations(
        self, AccountIds: List[str]
    ) -> ClientDeclineInvitationsResponseTypeDef:
        """
        Declines invitations sent to the current member account by AWS account specified by their account
        IDs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeclineInvitations>`_

        **Request Syntax**
        ::

          response = client.decline_invitations(
              AccountIds=[
                  'string',
              ]
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs of the AWS accounts that sent invitations to the current member account
          that you want to decline invitations from.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of objects containing the unprocessed account and a result string explaining why it
              was unprocessed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_detector(self, DetectorId: str) -> Dict[str, Any]:
        """
        Deletes a Amazon GuardDuty detector specified by the detector ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteDetector>`_

        **Request Syntax**
        ::

          response = client.delete_detector(
              DetectorId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector that you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_filter(self, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        """
        Deletes the filter specified by the filter name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteFilter>`_

        **Request Syntax**
        ::

          response = client.delete_filter(
              DetectorId='string',
              FilterName='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the filter is associated with.

        :type FilterName: string
        :param FilterName: **[REQUIRED]**

          The name of the filter you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_invitations(
        self, AccountIds: List[str]
    ) -> ClientDeleteInvitationsResponseTypeDef:
        """
        Deletes invitations sent to the current member account by AWS accounts specified by their account
        IDs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteInvitations>`_

        **Request Syntax**
        ::

          response = client.delete_invitations(
              AccountIds=[
                  'string',
              ]
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs of the AWS accounts that sent invitations to the current member account
          that you want to delete invitations from.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of objects containing the unprocessed account and a result string explaining why it
              was unprocessed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ip_set(self, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        """
        Deletes the IPSet specified by the ``ipSetId`` . IPSets are called Trusted IP lists in the console
        user interface.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteIPSet>`_

        **Request Syntax**
        ::

          response = client.delete_ip_set(
              DetectorId='string',
              IpSetId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector associated with the IPSet.

        :type IpSetId: string
        :param IpSetId: **[REQUIRED]**

          The unique ID of the IPSet to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientDeleteMembersResponseTypeDef:
        """
        Deletes GuardDuty member accounts (to the current GuardDuty master account) specified by the
        account IDs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteMembers>`_

        **Request Syntax**
        ::

          response = client.delete_members(
              DetectorId='string',
              AccountIds=[
                  'string',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account whose members you want to delete.

        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs of the GuardDuty member accounts that you want to delete.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              The accounts that could not be processed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_publishing_destination(
        self, DetectorId: str, DestinationId: str
    ) -> Dict[str, Any]:
        """
        Deletes the publishing definition with the specified ``destinationId`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeletePublishingDestination>`_

        **Request Syntax**
        ::

          response = client.delete_publishing_destination(
              DetectorId='string',
              DestinationId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector associated with the publishing destination to delete.

        :type DestinationId: string
        :param DestinationId: **[REQUIRED]**

          The ID of the publishing destination to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_threat_intel_set(
        self, DetectorId: str, ThreatIntelSetId: str
    ) -> Dict[str, Any]:
        """
        Deletes ThreatIntelSet specified by the ThreatIntelSet ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteThreatIntelSet>`_

        **Request Syntax**
        ::

          response = client.delete_threat_intel_set(
              DetectorId='string',
              ThreatIntelSetId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the threatIntelSet is associated with.

        :type ThreatIntelSetId: string
        :param ThreatIntelSetId: **[REQUIRED]**

          The unique ID of the threatIntelSet you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_publishing_destination(
        self, DetectorId: str, DestinationId: str
    ) -> ClientDescribePublishingDestinationResponseTypeDef:
        """
        Returns information about the publishing destination specified by the provided ``destinationId`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DescribePublishingDestination>`_

        **Request Syntax**
        ::

          response = client.describe_publishing_destination(
              DetectorId='string',
              DestinationId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector associated with the publishing destination to retrieve.

        :type DestinationId: string
        :param DestinationId: **[REQUIRED]**

          The ID of the publishing destination to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DestinationId': 'string',
                'DestinationType': 'S3',
                'Status':
                'PENDING_VERIFICATION'|'PUBLISHING'|'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY'|'STOPPED',
                'PublishingFailureStartTimestamp': 123,
                'DestinationProperties': {
                    'DestinationArn': 'string',
                    'KmsKeyArn': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **DestinationId** *(string) --*

              The ID of the publishing destination.

            - **DestinationType** *(string) --*

              The type of the publishing destination. Currently, only S3 is supported.

            - **Status** *(string) --*

              The status of the publishing destination.

            - **PublishingFailureStartTimestamp** *(integer) --*

              The time, in epoch millisecond format, at which GuardDuty was first unable to publish
              findings to the destination.

            - **DestinationProperties** *(dict) --*

              A ``DestinationProperties`` object that includes the ``DestinationArn`` and ``KmsKeyArn`` of
              the publishing destination.

              - **DestinationArn** *(string) --*

                The ARN of the resource to publish to.

              - **KmsKeyArn** *(string) --*

                The ARN of the KMS key to use for encryption.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_from_master_account(self, DetectorId: str) -> Dict[str, Any]:
        """
        Disassociates the current GuardDuty member account from its master account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DisassociateFromMasterAccount>`_

        **Request Syntax**
        ::

          response = client.disassociate_from_master_account(
              DetectorId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty member account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientDisassociateMembersResponseTypeDef:
        """
        Disassociates GuardDuty member accounts (to the current GuardDuty master account) specified by the
        account IDs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DisassociateMembers>`_

        **Request Syntax**
        ::

          response = client.disassociate_members(
              DetectorId='string',
              AccountIds=[
                  'string',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account whose members you want to disassociate
          from master.

        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs of the GuardDuty member accounts that you want to disassociate from master.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of objects containing the unprocessed account and a result string explaining why it
              was unprocessed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

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
    def get_detector(self, DetectorId: str) -> ClientGetDetectorResponseTypeDef:
        """
        Retrieves an Amazon GuardDuty detector specified by the detectorId.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetDetector>`_

        **Request Syntax**
        ::

          response = client.get_detector(
              DetectorId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector that you want to get.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CreatedAt': 'string',
                'FindingPublishingFrequency': 'FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
                'ServiceRole': 'string',
                'Status': 'ENABLED'|'DISABLED',
                'UpdatedAt': 'string',
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **CreatedAt** *(string) --*

              Detector creation timestamp.

            - **FindingPublishingFrequency** *(string) --*

              Finding publishing frequency.

            - **ServiceRole** *(string) --*

              The GuardDuty service role.

            - **Status** *(string) --*

              The detector status.

            - **UpdatedAt** *(string) --*

              Detector last update timestamp.

            - **Tags** *(dict) --*

              The tags of the detector resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_filter(
        self, DetectorId: str, FilterName: str
    ) -> ClientGetFilterResponseTypeDef:
        """
        Returns the details of the filter specified by the filter name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFilter>`_

        **Request Syntax**
        ::

          response = client.get_filter(
              DetectorId='string',
              FilterName='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the filter is associated with.

        :type FilterName: string
        :param FilterName: **[REQUIRED]**

          The name of the filter you want to get.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'Description': 'string',
                'Action': 'NOOP'|'ARCHIVE',
                'Rank': 123,
                'FindingCriteria': {
                    'Criterion': {
                        'string': {
                            'Eq': [
                                'string',
                            ],
                            'Neq': [
                                'string',
                            ],
                            'Gt': 123,
                            'Gte': 123,
                            'Lt': 123,
                            'Lte': 123,
                            'Equals': [
                                'string',
                            ],
                            'NotEquals': [
                                'string',
                            ],
                            'GreaterThan': 123,
                            'GreaterThanOrEqual': 123,
                            'LessThan': 123,
                            'LessThanOrEqual': 123
                        }
                    }
                },
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the filter.

            - **Description** *(string) --*

              The description of the filter.

            - **Action** *(string) --*

              Specifies the action that is to be applied to the findings that match the filter.

            - **Rank** *(integer) --*

              Specifies the position of the filter in the list of current filters. Also specifies the order
              in which this filter is applied to the findings.

            - **FindingCriteria** *(dict) --*

              Represents the criteria to be used in the filter for querying findings.

              - **Criterion** *(dict) --*

                Represents a map of finding properties that match specified conditions and values when
                querying findings.

                - *(string) --*

                  - *(dict) --*

                    Contains information about the condition.

                    - **Eq** *(list) --*

                      Represents the equal condition to be applied to a single field when querying for
                      findings.

                      - *(string) --*

                    - **Neq** *(list) --*

                      Represents the not equal condition to be applied to a single field when querying for
                      findings.

                      - *(string) --*

                    - **Gt** *(integer) --*

                      Represents a greater than condition to be applied to a single field when querying for
                      findings.

                    - **Gte** *(integer) --*

                      Represents a greater than equal condition to be applied to a single field when
                      querying for findings.

                    - **Lt** *(integer) --*

                      Represents a less than condition to be applied to a single field when querying for
                      findings.

                    - **Lte** *(integer) --*

                      Represents a less than equal condition to be applied to a single field when querying
                      for findings.

                    - **Equals** *(list) --*

                      Represents an **equal** condition to be applied to a single field when querying for
                      findings.

                      - *(string) --*

                    - **NotEquals** *(list) --*

                      Represents an **not equal** condition to be applied to a single field when querying
                      for findings.

                      - *(string) --*

                    - **GreaterThan** *(integer) --*

                      Represents a greater than condition to be applied to a single field when querying for
                      findings.

                    - **GreaterThanOrEqual** *(integer) --*

                      Represents a greater than equal condition to be applied to a single field when
                      querying for findings.

                    - **LessThan** *(integer) --*

                      Represents a less than condition to be applied to a single field when querying for
                      findings.

                    - **LessThanOrEqual** *(integer) --*

                      Represents a less than equal condition to be applied to a single field when querying
                      for findings.

            - **Tags** *(dict) --*

              The tags of the filter resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_findings(
        self,
        DetectorId: str,
        FindingIds: List[str],
        SortCriteria: ClientGetFindingsSortCriteriaTypeDef = None,
    ) -> ClientGetFindingsResponseTypeDef:
        """
        Describes Amazon GuardDuty findings specified by finding IDs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFindings>`_

        **Request Syntax**
        ::

          response = client.get_findings(
              DetectorId='string',
              FindingIds=[
                  'string',
              ],
              SortCriteria={
                  'AttributeName': 'string',
                  'OrderBy': 'ASC'|'DESC'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.

        :type FindingIds: list
        :param FindingIds: **[REQUIRED]**

          IDs of the findings that you want to retrieve.

          - *(string) --*

        :type SortCriteria: dict
        :param SortCriteria:

          Represents the criteria used for sorting findings.

          - **AttributeName** *(string) --*

            Represents the finding attribute (for example, accountId) by which to sort findings.

          - **OrderBy** *(string) --*

            Order by which the sorted findings are to be displayed.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Findings': [
                    {
                        'AccountId': 'string',
                        'Arn': 'string',
                        'Confidence': 123.0,
                        'CreatedAt': 'string',
                        'Description': 'string',
                        'Id': 'string',
                        'Partition': 'string',
                        'Region': 'string',
                        'Resource': {
                            'AccessKeyDetails': {
                                'AccessKeyId': 'string',
                                'PrincipalId': 'string',
                                'UserName': 'string',
                                'UserType': 'string'
                            },
                            'InstanceDetails': {
                                'AvailabilityZone': 'string',
                                'IamInstanceProfile': {
                                    'Arn': 'string',
                                    'Id': 'string'
                                },
                                'ImageDescription': 'string',
                                'ImageId': 'string',
                                'InstanceId': 'string',
                                'InstanceState': 'string',
                                'InstanceType': 'string',
                                'LaunchTime': 'string',
                                'NetworkInterfaces': [
                                    {
                                        'Ipv6Addresses': [
                                            'string',
                                        ],
                                        'NetworkInterfaceId': 'string',
                                        'PrivateDnsName': 'string',
                                        'PrivateIpAddress': 'string',
                                        'PrivateIpAddresses': [
                                            {
                                                'PrivateDnsName': 'string',
                                                'PrivateIpAddress': 'string'
                                            },
                                        ],
                                        'PublicDnsName': 'string',
                                        'PublicIp': 'string',
                                        'SecurityGroups': [
                                            {
                                                'GroupId': 'string',
                                                'GroupName': 'string'
                                            },
                                        ],
                                        'SubnetId': 'string',
                                        'VpcId': 'string'
                                    },
                                ],
                                'Platform': 'string',
                                'ProductCodes': [
                                    {
                                        'Code': 'string',
                                        'ProductType': 'string'
                                    },
                                ],
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            },
                            'ResourceType': 'string'
                        },
                        'SchemaVersion': 'string',
                        'Service': {
                            'Action': {
                                'ActionType': 'string',
                                'AwsApiCallAction': {
                                    'Api': 'string',
                                    'CallerType': 'string',
                                    'DomainDetails': {
                                        'Domain': 'string'
                                    },
                                    'RemoteIpDetails': {
                                        'City': {
                                            'CityName': 'string'
                                        },
                                        'Country': {
                                            'CountryCode': 'string',
                                            'CountryName': 'string'
                                        },
                                        'GeoLocation': {
                                            'Lat': 123.0,
                                            'Lon': 123.0
                                        },
                                        'IpAddressV4': 'string',
                                        'Organization': {
                                            'Asn': 'string',
                                            'AsnOrg': 'string',
                                            'Isp': 'string',
                                            'Org': 'string'
                                        }
                                    },
                                    'ServiceName': 'string'
                                },
                                'DnsRequestAction': {
                                    'Domain': 'string'
                                },
                                'NetworkConnectionAction': {
                                    'Blocked': True|False,
                                    'ConnectionDirection': 'string',
                                    'LocalPortDetails': {
                                        'Port': 123,
                                        'PortName': 'string'
                                    },
                                    'Protocol': 'string',
                                    'RemoteIpDetails': {
                                        'City': {
                                            'CityName': 'string'
                                        },
                                        'Country': {
                                            'CountryCode': 'string',
                                            'CountryName': 'string'
                                        },
                                        'GeoLocation': {
                                            'Lat': 123.0,
                                            'Lon': 123.0
                                        },
                                        'IpAddressV4': 'string',
                                        'Organization': {
                                            'Asn': 'string',
                                            'AsnOrg': 'string',
                                            'Isp': 'string',
                                            'Org': 'string'
                                        }
                                    },
                                    'RemotePortDetails': {
                                        'Port': 123,
                                        'PortName': 'string'
                                    }
                                },
                                'PortProbeAction': {
                                    'Blocked': True|False,
                                    'PortProbeDetails': [
                                        {
                                            'LocalPortDetails': {
                                                'Port': 123,
                                                'PortName': 'string'
                                            },
                                            'RemoteIpDetails': {
                                                'City': {
                                                    'CityName': 'string'
                                                },
                                                'Country': {
                                                    'CountryCode': 'string',
                                                    'CountryName': 'string'
                                                },
                                                'GeoLocation': {
                                                    'Lat': 123.0,
                                                    'Lon': 123.0
                                                },
                                                'IpAddressV4': 'string',
                                                'Organization': {
                                                    'Asn': 'string',
                                                    'AsnOrg': 'string',
                                                    'Isp': 'string',
                                                    'Org': 'string'
                                                }
                                            }
                                        },
                                    ]
                                }
                            },
                            'Evidence': {
                                'ThreatIntelligenceDetails': [
                                    {
                                        'ThreatListName': 'string',
                                        'ThreatNames': [
                                            'string',
                                        ]
                                    },
                                ]
                            },
                            'Archived': True|False,
                            'Count': 123,
                            'DetectorId': 'string',
                            'EventFirstSeen': 'string',
                            'EventLastSeen': 'string',
                            'ResourceRole': 'string',
                            'ServiceName': 'string',
                            'UserFeedback': 'string'
                        },
                        'Severity': 123.0,
                        'Title': 'string',
                        'Type': 'string',
                        'UpdatedAt': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Findings** *(list) --*

              A list of findings.

              - *(dict) --*

                Contains information about the finding, which is generated when abnormal or suspicious
                activity is detected.

                - **AccountId** *(string) --*

                  The ID of the account in which the finding was generated.

                - **Arn** *(string) --*

                  The ARN for the finding.

                - **Confidence** *(float) --*

                  The confidence score for the finding.

                - **CreatedAt** *(string) --*

                  The time and date at which the finding was created.

                - **Description** *(string) --*

                  The description of the finding.

                - **Id** *(string) --*

                  The ID of the finding.

                - **Partition** *(string) --*

                  The partition associated with the finding.

                - **Region** *(string) --*

                  The Region in which the finding was generated.

                - **Resource** *(dict) --*

                  Contains information about the AWS resource associated with the activity that prompted
                  GuardDuty to generate a finding.

                  - **AccessKeyDetails** *(dict) --*

                    The IAM access key details (IAM user information) of a user that engaged in the
                    activity that prompted GuardDuty to generate a finding.

                    - **AccessKeyId** *(string) --*

                      Access key ID of the user.

                    - **PrincipalId** *(string) --*

                      The principal ID of the user.

                    - **UserName** *(string) --*

                      The name of the user.

                    - **UserType** *(string) --*

                      The type of the user.

                  - **InstanceDetails** *(dict) --*

                    The information about the EC2 instance associated with the activity that prompted
                    GuardDuty to generate a finding.

                    - **AvailabilityZone** *(string) --*

                      The availability zone of the EC2 instance.

                    - **IamInstanceProfile** *(dict) --*

                      The profile information of the EC2 instance.

                      - **Arn** *(string) --*

                        AWS EC2 instance profile ARN.

                      - **Id** *(string) --*

                        AWS EC2 instance profile ID.

                    - **ImageDescription** *(string) --*

                      The image description of the EC2 instance.

                    - **ImageId** *(string) --*

                      The image ID of the EC2 instance.

                    - **InstanceId** *(string) --*

                      The ID of the EC2 instance.

                    - **InstanceState** *(string) --*

                      The state of the EC2 instance.

                    - **InstanceType** *(string) --*

                      The type of the EC2 instance.

                    - **LaunchTime** *(string) --*

                      The launch time of the EC2 instance.

                    - **NetworkInterfaces** *(list) --*

                      The network interface information of the EC2 instance.

                      - *(dict) --*

                        Contains information about the network interface of the Ec2 instance.

                        - **Ipv6Addresses** *(list) --*

                          A list of EC2 instance IPv6 address information.

                          - *(string) --*

                        - **NetworkInterfaceId** *(string) --*

                          The ID of the network interface

                        - **PrivateDnsName** *(string) --*

                          Private DNS name of the EC2 instance.

                        - **PrivateIpAddress** *(string) --*

                          Private IP address of the EC2 instance.

                        - **PrivateIpAddresses** *(list) --*

                          Other private IP address information of the EC2 instance.

                          - *(dict) --*

                            Contains other private IP address information of the EC2 instance.

                            - **PrivateDnsName** *(string) --*

                              Private DNS name of the EC2 instance.

                            - **PrivateIpAddress** *(string) --*

                              Private IP address of the EC2 instance.

                        - **PublicDnsName** *(string) --*

                          Public DNS name of the EC2 instance.

                        - **PublicIp** *(string) --*

                          Public IP address of the EC2 instance.

                        - **SecurityGroups** *(list) --*

                          Security groups associated with the EC2 instance.

                          - *(dict) --*

                            Contains information about the security groups associated with the EC2 instance.

                            - **GroupId** *(string) --*

                              EC2 instance's security group ID.

                            - **GroupName** *(string) --*

                              EC2 instance's security group name.

                        - **SubnetId** *(string) --*

                          The subnet ID of the EC2 instance.

                        - **VpcId** *(string) --*

                          The VPC ID of the EC2 instance.

                    - **Platform** *(string) --*

                      The platform of the EC2 instance.

                    - **ProductCodes** *(list) --*

                      The product code of the EC2 instance.

                      - *(dict) --*

                        Contains information about the product code for the Ec2 instance.

                        - **Code** *(string) --*

                          Product code information.

                        - **ProductType** *(string) --*

                          Product code type.

                    - **Tags** *(list) --*

                      The tags of the EC2 instance.

                      - *(dict) --*

                        Contains information about a tag associated with the Ec2 instance.

                        - **Key** *(string) --*

                          EC2 instance tag key.

                        - **Value** *(string) --*

                          EC2 instance tag value.

                  - **ResourceType** *(string) --*

                    The type of the AWS resource.

                - **SchemaVersion** *(string) --*

                  The version of the schema used for the finding.

                - **Service** *(dict) --*

                  Contains additional information about the generated finding.

                  - **Action** *(dict) --*

                    Information about the activity described in a finding.

                    - **ActionType** *(string) --*

                      GuardDuty Finding activity type.

                    - **AwsApiCallAction** *(dict) --*

                      Information about the AWS_API_CALL action described in this finding.

                      - **Api** *(string) --*

                        AWS API name.

                      - **CallerType** *(string) --*

                        AWS API caller type.

                      - **DomainDetails** *(dict) --*

                        Domain information for the AWS API call.

                        - **Domain** *(string) --*

                          Domain information for the AWS API call.

                      - **RemoteIpDetails** *(dict) --*

                        Remote IP information of the connection.

                        - **City** *(dict) --*

                          City information of the remote IP address.

                          - **CityName** *(string) --*

                            City name of the remote IP address.

                        - **Country** *(dict) --*

                          Country code of the remote IP address.

                          - **CountryCode** *(string) --*

                            Country code of the remote IP address.

                          - **CountryName** *(string) --*

                            Country name of the remote IP address.

                        - **GeoLocation** *(dict) --*

                          Location information of the remote IP address.

                          - **Lat** *(float) --*

                            Latitude information of remote IP address.

                          - **Lon** *(float) --*

                            Longitude information of remote IP address.

                        - **IpAddressV4** *(string) --*

                          IPV4 remote address of the connection.

                        - **Organization** *(dict) --*

                          ISP Organization information of the remote IP address.

                          - **Asn** *(string) --*

                            Autonomous system number of the internet provider of the remote IP address.

                          - **AsnOrg** *(string) --*

                            Organization that registered this ASN.

                          - **Isp** *(string) --*

                            ISP information for the internet provider.

                          - **Org** *(string) --*

                            Name of the internet provider.

                      - **ServiceName** *(string) --*

                        AWS service name whose API was invoked.

                    - **DnsRequestAction** *(dict) --*

                      Information about the DNS_REQUEST action described in this finding.

                      - **Domain** *(string) --*

                        Domain information for the API request.

                    - **NetworkConnectionAction** *(dict) --*

                      Information about the NETWORK_CONNECTION action described in this finding.

                      - **Blocked** *(boolean) --*

                        Network connection blocked information.

                      - **ConnectionDirection** *(string) --*

                        Network connection direction.

                      - **LocalPortDetails** *(dict) --*

                        Local port information of the connection.

                        - **Port** *(integer) --*

                          Port number of the local connection.

                        - **PortName** *(string) --*

                          Port name of the local connection.

                      - **Protocol** *(string) --*

                        Network connection protocol.

                      - **RemoteIpDetails** *(dict) --*

                        Remote IP information of the connection.

                        - **City** *(dict) --*

                          City information of the remote IP address.

                          - **CityName** *(string) --*

                            City name of the remote IP address.

                        - **Country** *(dict) --*

                          Country code of the remote IP address.

                          - **CountryCode** *(string) --*

                            Country code of the remote IP address.

                          - **CountryName** *(string) --*

                            Country name of the remote IP address.

                        - **GeoLocation** *(dict) --*

                          Location information of the remote IP address.

                          - **Lat** *(float) --*

                            Latitude information of remote IP address.

                          - **Lon** *(float) --*

                            Longitude information of remote IP address.

                        - **IpAddressV4** *(string) --*

                          IPV4 remote address of the connection.

                        - **Organization** *(dict) --*

                          ISP Organization information of the remote IP address.

                          - **Asn** *(string) --*

                            Autonomous system number of the internet provider of the remote IP address.

                          - **AsnOrg** *(string) --*

                            Organization that registered this ASN.

                          - **Isp** *(string) --*

                            ISP information for the internet provider.

                          - **Org** *(string) --*

                            Name of the internet provider.

                      - **RemotePortDetails** *(dict) --*

                        Remote port information of the connection.

                        - **Port** *(integer) --*

                          Port number of the remote connection.

                        - **PortName** *(string) --*

                          Port name of the remote connection.

                    - **PortProbeAction** *(dict) --*

                      Information about the PORT_PROBE action described in this finding.

                      - **Blocked** *(boolean) --*

                        Port probe blocked information.

                      - **PortProbeDetails** *(list) --*

                        A list of port probe details objects.

                        - *(dict) --*

                          Contains information about the port probe details.

                          - **LocalPortDetails** *(dict) --*

                            Local port information of the connection.

                            - **Port** *(integer) --*

                              Port number of the local connection.

                            - **PortName** *(string) --*

                              Port name of the local connection.

                          - **RemoteIpDetails** *(dict) --*

                            Remote IP information of the connection.

                            - **City** *(dict) --*

                              City information of the remote IP address.

                              - **CityName** *(string) --*

                                City name of the remote IP address.

                            - **Country** *(dict) --*

                              Country code of the remote IP address.

                              - **CountryCode** *(string) --*

                                Country code of the remote IP address.

                              - **CountryName** *(string) --*

                                Country name of the remote IP address.

                            - **GeoLocation** *(dict) --*

                              Location information of the remote IP address.

                              - **Lat** *(float) --*

                                Latitude information of remote IP address.

                              - **Lon** *(float) --*

                                Longitude information of remote IP address.

                            - **IpAddressV4** *(string) --*

                              IPV4 remote address of the connection.

                            - **Organization** *(dict) --*

                              ISP Organization information of the remote IP address.

                              - **Asn** *(string) --*

                                Autonomous system number of the internet provider of the remote IP address.

                              - **AsnOrg** *(string) --*

                                Organization that registered this ASN.

                              - **Isp** *(string) --*

                                ISP information for the internet provider.

                              - **Org** *(string) --*

                                Name of the internet provider.

                  - **Evidence** *(dict) --*

                    An evidence object associated with the service.

                    - **ThreatIntelligenceDetails** *(list) --*

                      A list of threat intelligence details related to the evidence.

                      - *(dict) --*

                        An instance of a threat intelligence detail that constitutes evidence for the
                        finding.

                        - **ThreatListName** *(string) --*

                          The name of the threat intelligence list that triggered the finding.

                        - **ThreatNames** *(list) --*

                          A list of names of the threats in the threat intelligence list that triggered the
                          finding.

                          - *(string) --*

                  - **Archived** *(boolean) --*

                    Indicates whether this finding is archived.

                  - **Count** *(integer) --*

                    Total count of the occurrences of this finding type.

                  - **DetectorId** *(string) --*

                    Detector ID for the GuardDuty service.

                  - **EventFirstSeen** *(string) --*

                    First seen timestamp of the activity that prompted GuardDuty to generate this finding.

                  - **EventLastSeen** *(string) --*

                    Last seen timestamp of the activity that prompted GuardDuty to generate this finding.

                  - **ResourceRole** *(string) --*

                    Resource role information for this finding.

                  - **ServiceName** *(string) --*

                    The name of the AWS service (GuardDuty) that generated a finding.

                  - **UserFeedback** *(string) --*

                    Feedback left about the finding.

                - **Severity** *(float) --*

                  The severity of the finding.

                - **Title** *(string) --*

                  The title for the finding.

                - **Type** *(string) --*

                  The type of the finding.

                - **UpdatedAt** *(string) --*

                  The time and date at which the finding was laste updated.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_findings_statistics(
        self,
        DetectorId: str,
        FindingStatisticTypes: List[str],
        FindingCriteria: ClientGetFindingsStatisticsFindingCriteriaTypeDef = None,
    ) -> ClientGetFindingsStatisticsResponseTypeDef:
        """
        Lists Amazon GuardDuty findings' statistics for the specified detector ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFindingsStatistics>`_

        **Request Syntax**
        ::

          response = client.get_findings_statistics(
              DetectorId='string',
              FindingStatisticTypes=[
                  'COUNT_BY_SEVERITY',
              ],
              FindingCriteria={
                  'Criterion': {
                      'string': {
                          'Eq': [
                              'string',
                          ],
                          'Neq': [
                              'string',
                          ],
                          'Gt': 123,
                          'Gte': 123,
                          'Lt': 123,
                          'Lte': 123,
                          'Equals': [
                              'string',
                          ],
                          'NotEquals': [
                              'string',
                          ],
                          'GreaterThan': 123,
                          'GreaterThanOrEqual': 123,
                          'LessThan': 123,
                          'LessThanOrEqual': 123
                      }
                  }
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector that specifies the GuardDuty service whose findings' statistics you want
          to retrieve.

        :type FindingStatisticTypes: list
        :param FindingStatisticTypes: **[REQUIRED]**

          Types of finding statistics to retrieve.

          - *(string) --*

        :type FindingCriteria: dict
        :param FindingCriteria:

          Represents the criteria used for querying findings.

          - **Criterion** *(dict) --*

            Represents a map of finding properties that match specified conditions and values when querying
            findings.

            - *(string) --*

              - *(dict) --*

                Contains information about the condition.

                - **Eq** *(list) --*

                  Represents the equal condition to be applied to a single field when querying for findings.

                  - *(string) --*

                - **Neq** *(list) --*

                  Represents the not equal condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **Gt** *(integer) --*

                  Represents a greater than condition to be applied to a single field when querying for
                  findings.

                - **Gte** *(integer) --*

                  Represents a greater than equal condition to be applied to a single field when querying
                  for findings.

                - **Lt** *(integer) --*

                  Represents a less than condition to be applied to a single field when querying for
                  findings.

                - **Lte** *(integer) --*

                  Represents a less than equal condition to be applied to a single field when querying for
                  findings.

                - **Equals** *(list) --*

                  Represents an **equal** condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **NotEquals** *(list) --*

                  Represents an **not equal** condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **GreaterThan** *(integer) --*

                  Represents a greater than condition to be applied to a single field when querying for
                  findings.

                - **GreaterThanOrEqual** *(integer) --*

                  Represents a greater than equal condition to be applied to a single field when querying
                  for findings.

                - **LessThan** *(integer) --*

                  Represents a less than condition to be applied to a single field when querying for
                  findings.

                - **LessThanOrEqual** *(integer) --*

                  Represents a less than equal condition to be applied to a single field when querying for
                  findings.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FindingStatistics': {
                    'CountBySeverity': {
                        'string': 123
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **FindingStatistics** *(dict) --*

              Finding statistics object.

              - **CountBySeverity** *(dict) --*

                Represents a map of severity to count statistic for a set of findings

                - *(string) --*

                  - *(integer) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_invitations_count(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetInvitationsCountResponseTypeDef:
        """
        Returns the count of all GuardDuty membership invitations that were sent to the current member
        account except the currently accepted invitation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetInvitationsCount>`_

        **Request Syntax**
        ::

          response = client.get_invitations_count()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'InvitationsCount': 123
            }
          **Response Structure**

          - *(dict) --*

            - **InvitationsCount** *(integer) --*

              The number of received invitations.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ip_set(
        self, DetectorId: str, IpSetId: str
    ) -> ClientGetIpSetResponseTypeDef:
        """
        Retrieves the IPSet specified by the ``ipSetId`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetIPSet>`_

        **Request Syntax**
        ::

          response = client.get_ip_set(
              DetectorId='string',
              IpSetId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the ipSet is associated with.

        :type IpSetId: string
        :param IpSetId: **[REQUIRED]**

          The unique ID of the IPSet to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'Format': 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
                'Location': 'string',
                'Status':
                'INACTIVE'|'ACTIVATING'|'ACTIVE'|'DEACTIVATING'|'ERROR'|'DELETE_PENDING'|'DELETED',
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The user friendly name for the IPSet.

            - **Format** *(string) --*

              The format of the file that contains the IPSet.

            - **Location** *(string) --*

              The URI of the file that contains the IPSet. For example
              (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)

            - **Status** *(string) --*

              The status of ipSet file uploaded.

            - **Tags** *(dict) --*

              The tags of the IP set resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_master_account(
        self, DetectorId: str
    ) -> ClientGetMasterAccountResponseTypeDef:
        """
        Provides the details for the GuardDuty master account associated with the current GuardDuty member
        account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetMasterAccount>`_

        **Request Syntax**
        ::

          response = client.get_master_account(
              DetectorId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty member account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Master': {
                    'AccountId': 'string',
                    'InvitationId': 'string',
                    'RelationshipStatus': 'string',
                    'InvitedAt': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Master** *(dict) --*

              Master account details.

              - **AccountId** *(string) --*

                The ID of the account used as the Master account.

              - **InvitationId** *(string) --*

                This value is used to validate the master account to the member account.

              - **RelationshipStatus** *(string) --*

                The status of the relationship between the master and member accounts.

              - **InvitedAt** *(string) --*

                Timestamp at which the invitation was sent.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientGetMembersResponseTypeDef:
        """
        Retrieves GuardDuty member accounts (to the current GuardDuty master account) specified by the
        account IDs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetMembers>`_

        **Request Syntax**
        ::

          response = client.get_members(
              DetectorId='string',
              AccountIds=[
                  'string',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account whose members you want to retrieve.

        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs of the GuardDuty member accounts that you want to describe.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Members': [
                    {
                        'AccountId': 'string',
                        'DetectorId': 'string',
                        'MasterId': 'string',
                        'Email': 'string',
                        'RelationshipStatus': 'string',
                        'InvitedAt': 'string',
                        'UpdatedAt': 'string'
                    },
                ],
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Members** *(list) --*

              A list of members.

              - *(dict) --*

                Continas information about the member account

                - **AccountId** *(string) --*

                  Member account ID.

                - **DetectorId** *(string) --*

                  Member account's detector ID.

                - **MasterId** *(string) --*

                  Master account ID.

                - **Email** *(string) --*

                  Member account's email address.

                - **RelationshipStatus** *(string) --*

                  The status of the relationship between the member and the master.

                - **InvitedAt** *(string) --*

                  Timestamp at which the invitation was sent

                - **UpdatedAt** *(string) --*

                  Member last updated timestamp.

            - **UnprocessedAccounts** *(list) --*

              A list of objects containing the unprocessed account and a result string explaining why it
              was unprocessed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_threat_intel_set(
        self, DetectorId: str, ThreatIntelSetId: str
    ) -> ClientGetThreatIntelSetResponseTypeDef:
        """
        Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetThreatIntelSet>`_

        **Request Syntax**
        ::

          response = client.get_threat_intel_set(
              DetectorId='string',
              ThreatIntelSetId='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the threatIntelSet is associated with.

        :type ThreatIntelSetId: string
        :param ThreatIntelSetId: **[REQUIRED]**

          The unique ID of the threatIntelSet you want to get.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'Format': 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
                'Location': 'string',
                'Status':
                'INACTIVE'|'ACTIVATING'|'ACTIVE'|'DEACTIVATING'|'ERROR'|'DELETE_PENDING'|'DELETED',
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              A user-friendly ThreatIntelSet name that is displayed in all finding generated by activity
              that involves IP addresses included in this ThreatIntelSet.

            - **Format** *(string) --*

              The format of the threatIntelSet.

            - **Location** *(string) --*

              The URI of the file that contains the ThreatIntelSet. For example
              (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).

            - **Status** *(string) --*

              The status of threatIntelSet file uploaded.

            - **Tags** *(dict) --*

              The tags of the Threat List resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invite_members(
        self,
        DetectorId: str,
        AccountIds: List[str],
        DisableEmailNotification: bool = None,
        Message: str = None,
    ) -> ClientInviteMembersResponseTypeDef:
        """
        Invites other AWS accounts (created as members of the current AWS account by CreateMembers) to
        enable GuardDuty and allow the current AWS account to view and manage these accounts' GuardDuty
        findings on their behalf as the master account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/InviteMembers>`_

        **Request Syntax**
        ::

          response = client.invite_members(
              DetectorId='string',
              AccountIds=[
                  'string',
              ],
              DisableEmailNotification=True|False,
              Message='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account with which you want to invite members.

        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs of the accounts that you want to invite to GuardDuty as members.

          - *(string) --*

        :type DisableEmailNotification: boolean
        :param DisableEmailNotification:

          A boolean value that specifies whether you want to disable email notification to the accounts
          that you’re inviting to GuardDuty as members.

        :type Message: string
        :param Message:

          The invitation message that you want to send to the accounts that you’re inviting to GuardDuty as
          members.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of objects containing the unprocessed account and a result string explaining why it
              was unprocessed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_detectors(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListDetectorsResponseTypeDef:
        """
        Lists detectorIds of all the existing Amazon GuardDuty detector resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListDetectors>`_

        **Request Syntax**
        ::

          response = client.list_detectors(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          You can use this parameter to indicate the maximum number of items you want in the response. The
          default value is 50. The maximum value is 50.

        :type NextToken: string
        :param NextToken:

          You can use this parameter when paginating results. Set the value of this parameter to null on
          your first call to the list action. For subsequent calls to the action fill nextToken in the
          request with the value of NextToken from the previous response to continue listing data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DetectorIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DetectorIds** *(list) --*

              A list of detector Ids.

              - *(string) --*

            - **NextToken** *(string) --*

              Pagination parameter to be used on the next list operation to retrieve more items.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_filters(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListFiltersResponseTypeDef:
        """
        Returns a paginated list of the current filters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFilters>`_

        **Request Syntax**
        ::

          response = client.list_filters(
              DetectorId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the filter is associated with.

        :type MaxResults: integer
        :param MaxResults:

          You can use this parameter to indicate the maximum number of items you want in the response. The
          default value is 50. The maximum value is 50.

        :type NextToken: string
        :param NextToken:

          You can use this parameter when paginating results. Set the value of this parameter to null on
          your first call to the list action. For subsequent calls to the action fill nextToken in the
          request with the value of NextToken from the previous response to continue listing data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FilterNames': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **FilterNames** *(list) --*

              A list of filter names

              - *(string) --*

            - **NextToken** *(string) --*

              Pagination parameter to be used on the next list operation to retrieve more items.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_findings(
        self,
        DetectorId: str,
        FindingCriteria: ClientListFindingsFindingCriteriaTypeDef = None,
        SortCriteria: ClientListFindingsSortCriteriaTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListFindingsResponseTypeDef:
        """
        Lists Amazon GuardDuty findings for the specified detector ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFindings>`_

        **Request Syntax**
        ::

          response = client.list_findings(
              DetectorId='string',
              FindingCriteria={
                  'Criterion': {
                      'string': {
                          'Eq': [
                              'string',
                          ],
                          'Neq': [
                              'string',
                          ],
                          'Gt': 123,
                          'Gte': 123,
                          'Lt': 123,
                          'Lte': 123,
                          'Equals': [
                              'string',
                          ],
                          'NotEquals': [
                              'string',
                          ],
                          'GreaterThan': 123,
                          'GreaterThanOrEqual': 123,
                          'LessThan': 123,
                          'LessThanOrEqual': 123
                      }
                  }
              },
              SortCriteria={
                  'AttributeName': 'string',
                  'OrderBy': 'ASC'|'DESC'
              },
              MaxResults=123,
              NextToken='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector that specifies the GuardDuty service whose findings you want to list.

        :type FindingCriteria: dict
        :param FindingCriteria:

          Represents the criteria used for querying findings. Valid values include:

          * JSON field name

          * accountId

          * region

          * confidence

          * id

          * resource.accessKeyDetails.accessKeyId

          * resource.accessKeyDetails.principalId

          * resource.accessKeyDetails.userName

          * resource.accessKeyDetails.userType

          * resource.instanceDetails.iamInstanceProfile.id

          * resource.instanceDetails.imageId

          * resource.instanceDetails.instanceId

          * resource.instanceDetails.networkInterfaces.ipv6Addresses

          * resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress

          * resource.instanceDetails.networkInterfaces.publicDnsName

          * resource.instanceDetails.networkInterfaces.publicIp

          * resource.instanceDetails.networkInterfaces.securityGroups.groupId

          * resource.instanceDetails.networkInterfaces.securityGroups.groupName

          * resource.instanceDetails.networkInterfaces.subnetId

          * resource.instanceDetails.networkInterfaces.vpcId

          * resource.instanceDetails.tags.key

          * resource.instanceDetails.tags.value

          * resource.resourceType

          * service.action.actionType

          * service.action.awsApiCallAction.api

          * service.action.awsApiCallAction.callerType

          * service.action.awsApiCallAction.remoteIpDetails.city.cityName

          * service.action.awsApiCallAction.remoteIpDetails.country.countryName

          * service.action.awsApiCallAction.remoteIpDetails.ipAddressV4

          * service.action.awsApiCallAction.remoteIpDetails.organization.asn

          * service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg

          * service.action.awsApiCallAction.serviceName

          * service.action.dnsRequestAction.domain

          * service.action.networkConnectionAction.blocked

          * service.action.networkConnectionAction.connectionDirection

          * service.action.networkConnectionAction.localPortDetails.port

          * service.action.networkConnectionAction.protocol

          * service.action.networkConnectionAction.remoteIpDetails.city.cityName

          * service.action.networkConnectionAction.remoteIpDetails.country.countryName

          * service.action.networkConnectionAction.remoteIpDetails.ipAddressV4

          * service.action.networkConnectionAction.remoteIpDetails.organization.asn

          * service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg

          * service.action.networkConnectionAction.remotePortDetails.port

          * service.additionalInfo.threatListName

          * service.archived When this attribute is set to 'true', only archived findings are listed. When
          it's set to 'false', only unarchived findings are listed. When this attribute is not set, all
          existing findings are listed.

          * service.resourceRole

          * severity

          * type

          * updatedAt Type: Timestamp in Unix Epoch millisecond format: 1486685375000

          - **Criterion** *(dict) --*

            Represents a map of finding properties that match specified conditions and values when querying
            findings.

            - *(string) --*

              - *(dict) --*

                Contains information about the condition.

                - **Eq** *(list) --*

                  Represents the equal condition to be applied to a single field when querying for findings.

                  - *(string) --*

                - **Neq** *(list) --*

                  Represents the not equal condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **Gt** *(integer) --*

                  Represents a greater than condition to be applied to a single field when querying for
                  findings.

                - **Gte** *(integer) --*

                  Represents a greater than equal condition to be applied to a single field when querying
                  for findings.

                - **Lt** *(integer) --*

                  Represents a less than condition to be applied to a single field when querying for
                  findings.

                - **Lte** *(integer) --*

                  Represents a less than equal condition to be applied to a single field when querying for
                  findings.

                - **Equals** *(list) --*

                  Represents an **equal** condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **NotEquals** *(list) --*

                  Represents an **not equal** condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **GreaterThan** *(integer) --*

                  Represents a greater than condition to be applied to a single field when querying for
                  findings.

                - **GreaterThanOrEqual** *(integer) --*

                  Represents a greater than equal condition to be applied to a single field when querying
                  for findings.

                - **LessThan** *(integer) --*

                  Represents a less than condition to be applied to a single field when querying for
                  findings.

                - **LessThanOrEqual** *(integer) --*

                  Represents a less than equal condition to be applied to a single field when querying for
                  findings.

        :type SortCriteria: dict
        :param SortCriteria:

          Represents the criteria used for sorting findings.

          - **AttributeName** *(string) --*

            Represents the finding attribute (for example, accountId) by which to sort findings.

          - **OrderBy** *(string) --*

            Order by which the sorted findings are to be displayed.

        :type MaxResults: integer
        :param MaxResults:

          You can use this parameter to indicate the maximum number of items you want in the response. The
          default value is 50. The maximum value is 50.

        :type NextToken: string
        :param NextToken:

          You can use this parameter when paginating results. Set the value of this parameter to null on
          your first call to the list action. For subsequent calls to the action fill nextToken in the
          request with the value of NextToken from the previous response to continue listing data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FindingIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **FindingIds** *(list) --*

              The IDs of the findings you are listing.

              - *(string) --*

            - **NextToken** *(string) --*

              Pagination parameter to be used on the next list operation to retrieve more items.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListInvitationsResponseTypeDef:
        """
        Lists all GuardDuty membership invitations that were sent to the current AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListInvitations>`_

        **Request Syntax**
        ::

          response = client.list_invitations(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          You can use this parameter to indicate the maximum number of items you want in the response. The
          default value is 50. The maximum value is 50.

        :type NextToken: string
        :param NextToken:

          You can use this parameter when paginating results. Set the value of this parameter to null on
          your first call to the list action. For subsequent calls to the action fill nextToken in the
          request with the value of NextToken from the previous response to continue listing data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Invitations': [
                    {
                        'AccountId': 'string',
                        'InvitationId': 'string',
                        'RelationshipStatus': 'string',
                        'InvitedAt': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Invitations** *(list) --*

              A list of invitation descriptions.

              - *(dict) --*

                Contains information about the invitation to become a member account.

                - **AccountId** *(string) --*

                  The ID of the account from which the invitations was sent.

                - **InvitationId** *(string) --*

                  The ID of the invitation. This value is used to validate the inviter account to the
                  member account.

                - **RelationshipStatus** *(string) --*

                  The status of the relationship between the inviter and invitee accounts.

                - **InvitedAt** *(string) --*

                  Timestamp at which the invitation was sent.

            - **NextToken** *(string) --*

              Pagination parameter to be used on the next list operation to retrieve more items.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ip_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListIpSetsResponseTypeDef:
        """
        Lists the IPSets of the GuardDuty service specified by the detector ID. If you use this operation
        from a member account, the IPSets returned are the IPSets from the associated master account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListIPSets>`_

        **Request Syntax**
        ::

          response = client.list_ip_sets(
              DetectorId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the ipSet is associated with.

        :type MaxResults: integer
        :param MaxResults:

          You can use this parameter to indicate the maximum number of items you want in the response. The
          default value is 50. The maximum value is 50.

        :type NextToken: string
        :param NextToken:

          You can use this parameter when paginating results. Set the value of this parameter to null on
          your first call to the list action. For subsequent calls to the action fill nextToken in the
          request with the value of NextToken from the previous response to continue listing data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IpSetIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **IpSetIds** *(list) --*

              The IDs of the IPSet resources.

              - *(string) --*

            - **NextToken** *(string) --*

              Pagination parameter to be used on the next list operation to retrieve more items.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_members(
        self,
        DetectorId: str,
        MaxResults: int = None,
        NextToken: str = None,
        OnlyAssociated: str = None,
    ) -> ClientListMembersResponseTypeDef:
        """
        Lists details about all member accounts for the current GuardDuty master account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListMembers>`_

        **Request Syntax**
        ::

          response = client.list_members(
              DetectorId='string',
              MaxResults=123,
              NextToken='string',
              OnlyAssociated='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the member is associated with.

        :type MaxResults: integer
        :param MaxResults:

          You can use this parameter to indicate the maximum number of items you want in the response. The
          default value is 50. The maximum value is 50.

        :type NextToken: string
        :param NextToken:

          You can use this parameter when paginating results. Set the value of this parameter to null on
          your first call to the list action. For subsequent calls to the action fill nextToken in the
          request with the value of NextToken from the previous response to continue listing data.

        :type OnlyAssociated: string
        :param OnlyAssociated:

          Specifies whether to only return associated members or to return all members (including members
          which haven't been invited yet or have been disassociated).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Members': [
                    {
                        'AccountId': 'string',
                        'DetectorId': 'string',
                        'MasterId': 'string',
                        'Email': 'string',
                        'RelationshipStatus': 'string',
                        'InvitedAt': 'string',
                        'UpdatedAt': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Members** *(list) --*

              A list of members.

              - *(dict) --*

                Continas information about the member account

                - **AccountId** *(string) --*

                  Member account ID.

                - **DetectorId** *(string) --*

                  Member account's detector ID.

                - **MasterId** *(string) --*

                  Master account ID.

                - **Email** *(string) --*

                  Member account's email address.

                - **RelationshipStatus** *(string) --*

                  The status of the relationship between the member and the master.

                - **InvitedAt** *(string) --*

                  Timestamp at which the invitation was sent

                - **UpdatedAt** *(string) --*

                  Member last updated timestamp.

            - **NextToken** *(string) --*

              Pagination parameter to be used on the next list operation to retrieve more items.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_publishing_destinations(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListPublishingDestinationsResponseTypeDef:
        """
        Returns a list of publishing destinations associated with the specified ``dectectorId`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListPublishingDestinations>`_

        **Request Syntax**
        ::

          response = client.list_publishing_destinations(
              DetectorId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector to retrieve publishing destinations for.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in the response.

        :type NextToken: string
        :param NextToken:

          A token to use for paginating results returned in the repsonse. Set the value of this parameter
          to null for the first request to a list action. For subsequent calls, use the ``NextToken`` value
          returned from the previous request to continue listing results after the first page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Destinations': [
                    {
                        'DestinationId': 'string',
                        'DestinationType': 'S3',
                        'Status':
                        'PENDING_VERIFICATION'|'PUBLISHING'|'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY'
                        |'STOPPED'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Destinations** *(list) --*

              A ``Destinations`` obect that includes information about each publishing destination returned.

              - *(dict) --*

                Contains information about a publishing destination, including the ID, type, and status.

                - **DestinationId** *(string) --*

                  The unique ID of the publishing destination.

                - **DestinationType** *(string) --*

                  The type of resource used for the publishing destination. Currently, only S3 is supported.

                - **Status** *(string) --*

                  The status of the publishing destination.

            - **NextToken** *(string) --*

              A token to use for paginating results returned in the repsonse. Set the value of this
              parameter to null for the first request to a list action. For subsequent calls, use the
              ``NextToken`` value returned from the previous request to continue listing results after the
              first page.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource. Tagging is currently supported for detectors, finding filters, IP sets,
        and Threat Intel sets, with a limit of 50 tags per resource. When invoked, this operation returns
        all assigned tags for a given resource..

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the given GuardDuty resource

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(dict) --*

              The tags associated with the resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_threat_intel_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListThreatIntelSetsResponseTypeDef:
        """
        Lists the ThreatIntelSets of the GuardDuty service specified by the detector ID. If you use this
        operation from a member account, the ThreatIntelSets associated with the master account are
        returned.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListThreatIntelSets>`_

        **Request Syntax**
        ::

          response = client.list_threat_intel_sets(
              DetectorId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the threatIntelSet is associated with.

        :type MaxResults: integer
        :param MaxResults:

          You can use this parameter to indicate the maximum number of items you want in the response. The
          default value is 50. The maximum value is 50.

        :type NextToken: string
        :param NextToken:

          You can use this parameter to paginate results in the response. Set the value of this parameter
          to null on your first call to the list action. For subsequent calls to the action fill nextToken
          in the request with the value of NextToken from the previous response to continue listing data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ThreatIntelSetIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ThreatIntelSetIds** *(list) --*

              The IDs of the ThreatIntelSet resources.

              - *(string) --*

            - **NextToken** *(string) --*

              Pagination parameter to be used on the next list operation to retrieve more items.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientStartMonitoringMembersResponseTypeDef:
        """
        Turns on GuardDuty monitoring of the specified member accounts. Use this operation to restart
        monitoring of accounts that you stopped monitoring with the ``StopMonitoringMembers`` operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/StartMonitoringMembers>`_

        **Request Syntax**
        ::

          response = client.start_monitoring_members(
              DetectorId='string',
              AccountIds=[
                  'string',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty master account associated with the member accounts
          to monitor.

        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs of the GuardDuty member accounts to start monitoring.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of objects containing the unprocessed account and a result string explaining why it
              was unprocessed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientStopMonitoringMembersResponseTypeDef:
        """
        Stops GuardDuty monitoring for the specified member accounnts. Use the ``StartMonitoringMembers``
        to restart monitoring for those accounts.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/StopMonitoringMembers>`_

        **Request Syntax**
        ::

          response = client.stop_monitoring_members(
              DetectorId='string',
              AccountIds=[
                  'string',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector of the GuardDuty account that you want to stop from monitor
          members' findings.

        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs of the GuardDuty member accounts whose findings you want the master account
          to stop monitoring.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'Result': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of objects containing the unprocessed account and a result string explaining why it
              was unprocessed.

              - *(dict) --*

                Contains information about the accounts that were not processed.

                - **AccountId** *(string) --*

                  AWS Account ID.

                - **Result** *(string) --*

                  A reason why the account hasn't been processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[str]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the GuardDuty resource to apply a tag to.

        :type Tags: dict
        :param Tags: **[REQUIRED]**

          The tags to be added to a resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unarchive_findings(
        self, DetectorId: str, FindingIds: List[str]
    ) -> Dict[str, Any]:
        """
        Unarchives GuardDuty findings specified by the ``findingIds`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UnarchiveFindings>`_

        **Request Syntax**
        ::

          response = client.unarchive_findings(
              DetectorId='string',
              FindingIds=[
                  'string',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector associated with the findings to unarchive.

        :type FindingIds: list
        :param FindingIds: **[REQUIRED]**

          IDs of the findings to unarchive.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the resource to remove tags from.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The tag keys to remove from the resource.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_detector(
        self,
        DetectorId: str,
        Enable: bool = None,
        FindingPublishingFrequency: str = None,
    ) -> Dict[str, Any]:
        """
        Updates the Amazon GuardDuty detector specified by the detectorId.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateDetector>`_

        **Request Syntax**
        ::

          response = client.update_detector(
              DetectorId='string',
              Enable=True|False,
              FindingPublishingFrequency='FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector to update.

        :type Enable: boolean
        :param Enable:

          Specifies whether the detector is enabled or not enabled.

        :type FindingPublishingFrequency: string
        :param FindingPublishingFrequency:

          A enum value that specifies how frequently findings are exported, such as to CloudWatch Events.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_filter(
        self,
        DetectorId: str,
        FilterName: str,
        Description: str = None,
        Action: str = None,
        Rank: int = None,
        FindingCriteria: ClientUpdateFilterFindingCriteriaTypeDef = None,
    ) -> ClientUpdateFilterResponseTypeDef:
        """
        Updates the filter specified by the filter name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateFilter>`_

        **Request Syntax**
        ::

          response = client.update_filter(
              DetectorId='string',
              FilterName='string',
              Description='string',
              Action='NOOP'|'ARCHIVE',
              Rank=123,
              FindingCriteria={
                  'Criterion': {
                      'string': {
                          'Eq': [
                              'string',
                          ],
                          'Neq': [
                              'string',
                          ],
                          'Gt': 123,
                          'Gte': 123,
                          'Lt': 123,
                          'Lte': 123,
                          'Equals': [
                              'string',
                          ],
                          'NotEquals': [
                              'string',
                          ],
                          'GreaterThan': 123,
                          'GreaterThanOrEqual': 123,
                          'LessThan': 123,
                          'LessThanOrEqual': 123
                      }
                  }
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector that specifies the GuardDuty service where you want to update a
          filter.

        :type FilterName: string
        :param FilterName: **[REQUIRED]**

          The name of the filter.

        :type Description: string
        :param Description:

          The description of the filter.

        :type Action: string
        :param Action:

          Specifies the action that is to be applied to the findings that match the filter.

        :type Rank: integer
        :param Rank:

          Specifies the position of the filter in the list of current filters. Also specifies the order in
          which this filter is applied to the findings.

        :type FindingCriteria: dict
        :param FindingCriteria:

          Represents the criteria to be used in the filter for querying findings.

          - **Criterion** *(dict) --*

            Represents a map of finding properties that match specified conditions and values when querying
            findings.

            - *(string) --*

              - *(dict) --*

                Contains information about the condition.

                - **Eq** *(list) --*

                  Represents the equal condition to be applied to a single field when querying for findings.

                  - *(string) --*

                - **Neq** *(list) --*

                  Represents the not equal condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **Gt** *(integer) --*

                  Represents a greater than condition to be applied to a single field when querying for
                  findings.

                - **Gte** *(integer) --*

                  Represents a greater than equal condition to be applied to a single field when querying
                  for findings.

                - **Lt** *(integer) --*

                  Represents a less than condition to be applied to a single field when querying for
                  findings.

                - **Lte** *(integer) --*

                  Represents a less than equal condition to be applied to a single field when querying for
                  findings.

                - **Equals** *(list) --*

                  Represents an **equal** condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **NotEquals** *(list) --*

                  Represents an **not equal** condition to be applied to a single field when querying for
                  findings.

                  - *(string) --*

                - **GreaterThan** *(integer) --*

                  Represents a greater than condition to be applied to a single field when querying for
                  findings.

                - **GreaterThanOrEqual** *(integer) --*

                  Represents a greater than equal condition to be applied to a single field when querying
                  for findings.

                - **LessThan** *(integer) --*

                  Represents a less than condition to be applied to a single field when querying for
                  findings.

                - **LessThanOrEqual** *(integer) --*

                  Represents a less than equal condition to be applied to a single field when querying for
                  findings.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the filter.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_findings_feedback(
        self,
        DetectorId: str,
        FindingIds: List[str],
        Feedback: str,
        Comments: str = None,
    ) -> Dict[str, Any]:
        """
        Marks the specified GuardDuty findings as useful or not useful.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateFindingsFeedback>`_

        **Request Syntax**
        ::

          response = client.update_findings_feedback(
              DetectorId='string',
              FindingIds=[
                  'string',
              ],
              Feedback='USEFUL'|'NOT_USEFUL',
              Comments='string'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector associated with the findings to update feedback for.

        :type FindingIds: list
        :param FindingIds: **[REQUIRED]**

          IDs of the findings that you want to mark as useful or not useful.

          - *(string) --*

        :type Feedback: string
        :param Feedback: **[REQUIRED]**

          The feedback for the finding.

        :type Comments: string
        :param Comments:

          Additional feedback about the GuardDuty findings.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        Updates the IPSet specified by the IPSet ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateIPSet>`_

        **Request Syntax**
        ::

          response = client.update_ip_set(
              DetectorId='string',
              IpSetId='string',
              Name='string',
              Location='string',
              Activate=True|False
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The detectorID that specifies the GuardDuty service whose IPSet you want to update.

        :type IpSetId: string
        :param IpSetId: **[REQUIRED]**

          The unique ID that specifies the IPSet that you want to update.

        :type Name: string
        :param Name:

          The unique ID that specifies the IPSet that you want to update.

        :type Location: string
        :param Location:

          The updated URI of the file that contains the IPSet. For example
          (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).

        :type Activate: boolean
        :param Activate:

          The updated boolean value that specifies whether the IPSet is active or not.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_publishing_destination(
        self,
        DetectorId: str,
        DestinationId: str,
        DestinationProperties: ClientUpdatePublishingDestinationDestinationPropertiesTypeDef = None,
    ) -> Dict[str, Any]:
        """
        Updates information about the publishing destination specified by the ``destinationId`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdatePublishingDestination>`_

        **Request Syntax**
        ::

          response = client.update_publishing_destination(
              DetectorId='string',
              DestinationId='string',
              DestinationProperties={
                  'DestinationArn': 'string',
                  'KmsKeyArn': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the

        :type DestinationId: string
        :param DestinationId: **[REQUIRED]**

          The ID of the detector associated with the publishing destinations to update.

        :type DestinationProperties: dict
        :param DestinationProperties:

          A ``DestinationProperties`` object that includes the ``DestinationArn`` and ``KmsKeyArn`` of the
          publishing destination.

          - **DestinationArn** *(string) --*

            The ARN of the resource to publish to.

          - **KmsKeyArn** *(string) --*

            The ARN of the KMS key to use for encryption.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        Updates the ThreatIntelSet specified by ThreatIntelSet ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateThreatIntelSet>`_

        **Request Syntax**
        ::

          response = client.update_threat_intel_set(
              DetectorId='string',
              ThreatIntelSetId='string',
              Name='string',
              Location='string',
              Activate=True|False
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to update.

        :type ThreatIntelSetId: string
        :param ThreatIntelSetId: **[REQUIRED]**

          The unique ID that specifies the ThreatIntelSet that you want to update.

        :type Name: string
        :param Name:

          The unique ID that specifies the ThreatIntelSet that you want to update.

        :type Location: string
        :param Location:

          The updated URI of the file that contains the ThreateIntelSet. For example
          (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)

        :type Activate: boolean
        :param Activate:

          The updated boolean value that specifies whether the ThreateIntelSet is active or not.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_detectors"]
    ) -> paginator_scope.ListDetectorsPaginator:
        """
        Get Paginator for `list_detectors` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_filters"]
    ) -> paginator_scope.ListFiltersPaginator:
        """
        Get Paginator for `list_filters` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_findings"]
    ) -> paginator_scope.ListFindingsPaginator:
        """
        Get Paginator for `list_findings` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_ip_sets"]
    ) -> paginator_scope.ListIPSetsPaginator:
        """
        Get Paginator for `list_ip_sets` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> paginator_scope.ListInvitationsPaginator:
        """
        Get Paginator for `list_invitations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_members"]
    ) -> paginator_scope.ListMembersPaginator:
        """
        Get Paginator for `list_members` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_threat_intel_sets"]
    ) -> paginator_scope.ListThreatIntelSetsPaginator:
        """
        Get Paginator for `list_threat_intel_sets` operation.
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
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
