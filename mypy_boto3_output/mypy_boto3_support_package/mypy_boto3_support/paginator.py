"Main interface for support Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_support.type_defs import (
    DescribeCasesPaginatePaginationConfigTypeDef,
    DescribeCasesPaginateResponseTypeDef,
    DescribeCommunicationsPaginatePaginationConfigTypeDef,
    DescribeCommunicationsPaginateResponseTypeDef,
)


__all__ = ("DescribeCasesPaginator", "DescribeCommunicationsPaginator")


class DescribeCasesPaginator(Boto3Paginator):
    """
    Paginator for `describe_cases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        language: str = None,
        includeCommunications: bool = None,
        PaginationConfig: DescribeCasesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCasesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Support.Client.describe_cases`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeCases>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              caseIdList=[
                  'string',
              ],
              displayId='string',
              afterTime='string',
              beforeTime='string',
              includeResolvedCases=True|False,
              language='string',
              includeCommunications=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type caseIdList: list
        :param caseIdList:

          A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.

          - *(string) --*

        :type displayId: string
        :param displayId:

          The ID displayed for a case in the AWS Support Center user interface.

        :type afterTime: string
        :param afterTime:

          The start date for a filtered date search on support case communications. Case communications are
          available for 12 months after creation.

        :type beforeTime: string
        :param beforeTime:

          The end date for a filtered date search on support case communications. Case communications are
          available for 12 months after creation.

        :type includeResolvedCases: boolean
        :param includeResolvedCases:

          Specifies whether resolved support cases should be included in the  DescribeCases results. The
          default is *false* .

        :type language: string
        :param language:

          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports
          English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations
          that take them.

        :type includeCommunications: boolean
        :param includeCommunications:

          Specifies whether communications should be included in the  DescribeCases results. The default is
          *true* .

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
                'cases': [
                    {
                        'caseId': 'string',
                        'displayId': 'string',
                        'subject': 'string',
                        'status': 'string',
                        'serviceCode': 'string',
                        'categoryCode': 'string',
                        'severityCode': 'string',
                        'submittedBy': 'string',
                        'timeCreated': 'string',
                        'recentCommunications': {
                            'communications': [
                                {
                                    'caseId': 'string',
                                    'body': 'string',
                                    'submittedBy': 'string',
                                    'timeCreated': 'string',
                                    'attachmentSet': [
                                        {
                                            'attachmentId': 'string',
                                            'fileName': 'string'
                                        },
                                    ]
                                },
                            ],
                            'nextToken': 'string'
                        },
                        'ccEmailAddresses': [
                            'string',
                        ],
                        'language': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Returns an array of  CaseDetails objects and a ``nextToken`` that defines a point for
            pagination in the result set.

            - **cases** *(list) --*

              The details for the cases that match the request.

              - *(dict) --*

                A JSON-formatted object that contains the metadata for a support case. It is contained the
                response from a  DescribeCases request. **CaseDetails** contains the following fields:

                * **caseId.** The AWS Support case ID requested or returned in the call. The case ID is an
                alphanumeric string formatted as shown in this example:
                case-*12345678910-2013-c4c1d2bf33c5cf47* .

                * **categoryCode.** The category of problem for the AWS Support case. Corresponds to the
                CategoryCode values returned by a call to  DescribeServices .

                * **displayId.** The identifier for the case on pages in the AWS Support Center.

                * **language.** The ISO 639-1 code for the language in which AWS provides support. AWS
                Support currently supports English ("en") and Japanese ("ja"). Language parameters must be
                passed explicitly for operations that take them.

                * **recentCommunications.** One or more  Communication objects. Fields of these objects are
                ``attachments`` , ``body`` , ``caseId`` , ``submittedBy`` , and ``timeCreated`` .

                * **nextToken.** A resumption point for pagination.

                * **serviceCode.** The identifier for the AWS service that corresponds to the service code
                defined in the call to  DescribeServices .

                * **severityCode.** The severity code assigned to the case. Contains one of the values
                returned by the call to  DescribeSeverityLevels . The possible values are: ``low`` ,
                ``normal`` , ``high`` , ``urgent`` , and ``critical`` .

                * **status.** The status of the case in the AWS Support Center. The possible values are:
                ``resolved`` , ``pending-customer-action`` , ``opened`` , ``unassigned`` , and
                ``work-in-progress`` .

                * **subject.** The subject line of the case.

                * **submittedBy.** The email address of the account that submitted the case.

                * **timeCreated.** The time the case was created, in ISO-8601 format.

                - **caseId** *(string) --*

                  The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
                  string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*

                - **displayId** *(string) --*

                  The ID displayed for the case in the AWS Support Center. This is a numeric string.

                - **subject** *(string) --*

                  The subject line for the case in the AWS Support Center.

                - **status** *(string) --*

                  The status of the case. Valid values: ``resolved`` | ``pending-customer-action`` |
                  ``opened`` | ``unassigned`` | ``work-in-progress`` .

                - **serviceCode** *(string) --*

                  The code for the AWS service. You can get a list of codes and the corresponding service
                  names by calling  DescribeServices .

                - **categoryCode** *(string) --*

                  The category of problem for the AWS Support case.

                - **severityCode** *(string) --*

                  The code for the severity level returned by the call to  DescribeSeverityLevels .

                - **submittedBy** *(string) --*

                  The email address of the account that submitted the case.

                - **timeCreated** *(string) --*

                  The time that the case was case created in the AWS Support Center.

                - **recentCommunications** *(dict) --*

                  The five most recent communications between you and AWS Support Center, including the IDs
                  of any attachments to the communications. Also includes a ``nextToken`` that you can use
                  to retrieve earlier communications.

                  - **communications** *(list) --*

                    The five most recent communications associated with the case.

                    - *(dict) --*

                      A communication associated with an AWS Support case. The communication consists of
                      the case ID, the message body, attachment information, the submitter of the
                      communication, and the date and time of the communication.

                      - **caseId** *(string) --*

                        The AWS Support case ID requested or returned in the call. The case ID is an
                        alphanumeric string formatted as shown in this example:
                        case-*12345678910-2013-c4c1d2bf33c5cf47*

                      - **body** *(string) --*

                        The text of the communication between the customer and AWS Support.

                      - **submittedBy** *(string) --*

                        The identity of the account that submitted, or responded to, the support case.
                        Customer entries include the role or IAM user as well as the email address. For
                        example, "AdminRole (Role) <someone@example.com>. Entries from the AWS Support team
                        display "Amazon Web Services," and do not show an email address.

                      - **timeCreated** *(string) --*

                        The time the communication was created.

                      - **attachmentSet** *(list) --*

                        Information about the attachments to the case communication.

                        - *(dict) --*

                          The file name and ID of an attachment to a case communication. You can use the ID
                          to retrieve the attachment with the  DescribeAttachment operation.

                          - **attachmentId** *(string) --*

                            The ID of the attachment.

                          - **fileName** *(string) --*

                            The file name of the attachment.

                  - **nextToken** *(string) --*

                    A resumption point for pagination.

                - **ccEmailAddresses** *(list) --*

                  The email addresses that receive copies of communication about the case.

                  - *(string) --*

                - **language** *(string) --*

                  The ISO 639-1 code for the language in which AWS provides support. AWS Support currently
                  supports English ("en") and Japanese ("ja"). Language parameters must be passed
                  explicitly for operations that take them.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class DescribeCommunicationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_communications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        PaginationConfig: DescribeCommunicationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCommunicationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Support.Client.describe_communications`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeCommunications>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              caseId='string',
              beforeTime='string',
              afterTime='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type caseId: string
        :param caseId: **[REQUIRED]**

          The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string
          formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*

        :type beforeTime: string
        :param beforeTime:

          The end date for a filtered date search on support case communications. Case communications are
          available for 12 months after creation.

        :type afterTime: string
        :param afterTime:

          The start date for a filtered date search on support case communications. Case communications are
          available for 12 months after creation.

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
                'communications': [
                    {
                        'caseId': 'string',
                        'body': 'string',
                        'submittedBy': 'string',
                        'timeCreated': 'string',
                        'attachmentSet': [
                            {
                                'attachmentId': 'string',
                                'fileName': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The communications returned by the  DescribeCommunications operation.

            - **communications** *(list) --*

              The communications for the case.

              - *(dict) --*

                A communication associated with an AWS Support case. The communication consists of the case
                ID, the message body, attachment information, the submitter of the communication, and the
                date and time of the communication.

                - **caseId** *(string) --*

                  The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
                  string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*

                - **body** *(string) --*

                  The text of the communication between the customer and AWS Support.

                - **submittedBy** *(string) --*

                  The identity of the account that submitted, or responded to, the support case. Customer
                  entries include the role or IAM user as well as the email address. For example,
                  "AdminRole (Role) <someone@example.com>. Entries from the AWS Support team display
                  "Amazon Web Services," and do not show an email address.

                - **timeCreated** *(string) --*

                  The time the communication was created.

                - **attachmentSet** *(list) --*

                  Information about the attachments to the case communication.

                  - *(dict) --*

                    The file name and ID of an attachment to a case communication. You can use the ID to
                    retrieve the attachment with the  DescribeAttachment operation.

                    - **attachmentId** *(string) --*

                      The ID of the attachment.

                    - **fileName** *(string) --*

                      The file name of the attachment.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
