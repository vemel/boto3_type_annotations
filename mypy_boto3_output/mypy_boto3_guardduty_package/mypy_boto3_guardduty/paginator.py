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


__all__ = (
    "ListDetectorsPaginator",
    "ListFiltersPaginator",
    "ListFindingsPaginator",
    "ListIPSetsPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
    "ListThreatIntelSetsPaginator",
)


class ListDetectorsPaginator(Boto3Paginator):
    """
    Paginator for `list_detectors`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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


class ListFiltersPaginator(Boto3Paginator):
    """
    Paginator for `list_filters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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


class ListFindingsPaginator(Boto3Paginator):
    """
    Paginator for `list_findings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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


class ListIPSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_ip_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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


class ListInvitationsPaginator(Boto3Paginator):
    """
    Paginator for `list_invitations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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

        """


class ListMembersPaginator(Boto3Paginator):
    """
    Paginator for `list_members`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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


class ListThreatIntelSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_threat_intel_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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
