"Main interface for guardduty Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_guardduty.type_defs import (
    ListDetectorsPaginatePaginationConfigTypeDef,
    ListDetectorsPaginateResponseTypeDef,
    ListFiltersPaginatePaginationConfigTypeDef,
    ListFiltersPaginateResponseTypeDef,
    ListFindingsPaginateFindingCriteriaTypeDef,
    ListFindingsPaginatePaginationConfigTypeDef,
    ListFindingsPaginateResponseTypeDef,
    ListFindingsPaginateSortCriteriaTypeDef,
    ListIPSetsPaginatePaginationConfigTypeDef,
    ListIPSetsPaginateResponseTypeDef,
    ListInvitationsPaginatePaginationConfigTypeDef,
    ListInvitationsPaginateResponseTypeDef,
    ListMembersPaginatePaginationConfigTypeDef,
    ListMembersPaginateResponseTypeDef,
    ListThreatIntelSetsPaginatePaginationConfigTypeDef,
    ListThreatIntelSetsPaginateResponseTypeDef,
)


class ListDetectors(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self, PaginationConfig: ListDetectorsPaginatePaginationConfigTypeDef = None
    ) -> ListDetectorsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GuardDuty.Client.list_detectors`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListDetectors>`_

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
                'DetectorIds': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **DetectorIds** *(list) --*

              A list of detector Ids.

              - *(string) --*

        """


class ListFilters(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: ListFiltersPaginatePaginationConfigTypeDef = None,
    ) -> ListFiltersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GuardDuty.Client.list_filters`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFilters>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              DetectorId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the filter is associated with.

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
                'FilterNames': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **FilterNames** *(list) --*

              A list of filter names

              - *(string) --*

        """


class ListFindings(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        DetectorId: str,
        FindingCriteria: ListFindingsPaginateFindingCriteriaTypeDef = None,
        SortCriteria: ListFindingsPaginateSortCriteriaTypeDef = None,
        PaginationConfig: ListFindingsPaginatePaginationConfigTypeDef = None,
    ) -> ListFindingsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GuardDuty.Client.list_findings`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFindings>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
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
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The ID of the detector that specifies the GuardDuty service whose findings you want to list.

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

                  Deprecated. Represents the equal condition to be applied to a single field when querying
                  for findings.

                  - *(string) --*

                - **Neq** *(list) --*

                  Deprecated. Represents the not equal condition to be applied to a single field when
                  querying for findings.

                  - *(string) --*

                - **Gt** *(integer) --*

                  Deprecated. Represents a greater than condition to be applied to a single field when
                  querying for findings.

                - **Gte** *(integer) --*

                  Deprecated. Represents a greater than equal condition to be applied to a single field
                  when querying for findings.

                - **Lt** *(integer) --*

                  Deprecated. Represents a less than condition to be applied to a single field when
                  querying for findings.

                - **Lte** *(integer) --*

                  Deprecated. Represents a less than equal condition to be applied to a single field when
                  querying for findings.

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
                'FindingIds': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **FindingIds** *(list) --*

              The IDs of the findings you are listing.

              - *(string) --*

        """


class ListIPSets(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: ListIPSetsPaginatePaginationConfigTypeDef = None,
    ) -> ListIPSetsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GuardDuty.Client.list_ip_sets`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListIPSets>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              DetectorId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the ipSet is associated with.

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
                'IpSetIds': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **IpSetIds** *(list) --*

              The IDs of the IPSet resources.

              - *(string) --*

        """


class ListInvitations(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self, PaginationConfig: ListInvitationsPaginatePaginationConfigTypeDef = None
    ) -> ListInvitationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GuardDuty.Client.list_invitations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListInvitations>`_

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
                'Invitations': [
                    {
                        'AccountId': 'string',
                        'InvitationId': 'string',
                        'RelationshipStatus': 'string',
                        'InvitedAt': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Invitations** *(list) --*

              A list of invitation descriptions.

              - *(dict) --*

                Contains information about the invitation.

                - **AccountId** *(string) --*

                  Inviter account ID

                - **InvitationId** *(string) --*

                  This value is used to validate the inviter account to the member account.

                - **RelationshipStatus** *(string) --*

                  The status of the relationship between the inviter and invitee accounts.

                - **InvitedAt** *(string) --*

                  Timestamp at which the invitation was sent

        """


class ListMembers(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        DetectorId: str,
        OnlyAssociated: str = None,
        PaginationConfig: ListMembersPaginatePaginationConfigTypeDef = None,
    ) -> ListMembersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GuardDuty.Client.list_members`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListMembers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              DetectorId='string',
              OnlyAssociated='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the member is associated with.

        :type OnlyAssociated: string
        :param OnlyAssociated:

          Specifies whether to only return associated members or to return all members (including members
          which haven't been invited yet or have been disassociated).

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

        """


class ListThreatIntelSets(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: ListThreatIntelSetsPaginatePaginationConfigTypeDef = None,
    ) -> ListThreatIntelSetsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GuardDuty.Client.list_threat_intel_sets`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListThreatIntelSets>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              DetectorId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]**

          The unique ID of the detector the threatIntelSet is associated with.

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
                'ThreatIntelSetIds': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ThreatIntelSetIds** *(list) --*

              The IDs of the ThreatIntelSet resources.

              - *(string) --*

        """
