"Main interface for support Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_support.client as client_scope

# pylint: disable=import-self
import mypy_boto3_support.paginator as paginator_scope
from mypy_boto3_support.type_defs import (
    ClientAddAttachmentsToSetResponseTypeDef,
    ClientAddAttachmentsToSetattachmentsTypeDef,
    ClientAddCommunicationToCaseResponseTypeDef,
    ClientCreateCaseResponseTypeDef,
    ClientDescribeAttachmentResponseTypeDef,
    ClientDescribeCasesResponseTypeDef,
    ClientDescribeCommunicationsResponseTypeDef,
    ClientDescribeServicesResponseTypeDef,
    ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef,
    ClientDescribeTrustedAdvisorCheckResultResponseTypeDef,
    ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef,
    ClientDescribeTrustedAdvisorChecksResponseTypeDef,
    ClientRefreshTrustedAdvisorCheckResponseTypeDef,
    ClientResolveCaseResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_attachments_to_set(
        self,
        attachments: List[ClientAddAttachmentsToSetattachmentsTypeDef],
        attachmentSetId: str = None,
    ) -> ClientAddAttachmentsToSetResponseTypeDef:
        """
        Adds one or more attachments to an attachment set. If an ``attachmentSetId`` is not specified, a
        new attachment set is created, and the ID of the set is returned in the response. If an
        ``attachmentSetId`` is specified, the attachments are added to the specified set, if it exists.

        An attachment set is a temporary container for attachments that are to be added to a case or case
        communication. The set is available for one hour after it is created; the ``expiryTime`` returned
        in the response indicates when the set expires. The maximum number of attachments in a set is 3,
        and the maximum size of any attachment in the set is 5 MB.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/AddAttachmentsToSet>`_

        **Request Syntax**
        ::

          response = client.add_attachments_to_set(
              attachmentSetId='string',
              attachments=[
                  {
                      'fileName': 'string',
                      'data': b'bytes'
                  },
              ]
          )
        :type attachmentSetId: string
        :param attachmentSetId:

          The ID of the attachment set. If an ``attachmentSetId`` is not specified, a new attachment set is
          created, and the ID of the set is returned in the response. If an ``attachmentSetId`` is
          specified, the attachments are added to the specified set, if it exists.

        :type attachments: list
        :param attachments: **[REQUIRED]**

          One or more attachments to add to the set. The limit is 3 attachments per set, and the size limit
          is 5 MB per attachment.

          - *(dict) --*

            An attachment to a case communication. The attachment consists of the file name and the content
            of the file.

            - **fileName** *(string) --*

              The name of the attachment file.

            - **data** *(bytes) --*

              The content of the attachment file.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'attachmentSetId': 'string',
                'expiryTime': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The ID and expiry time of the attachment set returned by the  AddAttachmentsToSet operation.

            - **attachmentSetId** *(string) --*

              The ID of the attachment set. If an ``attachmentSetId`` was not specified, a new attachment
              set is created, and the ID of the set is returned in the response. If an ``attachmentSetId``
              was specified, the attachments are added to the specified set, if it exists.

            - **expiryTime** *(string) --*

              The time and date when the attachment set expires.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_communication_to_case(
        self,
        communicationBody: str,
        caseId: str = None,
        ccEmailAddresses: List[str] = None,
        attachmentSetId: str = None,
    ) -> ClientAddCommunicationToCaseResponseTypeDef:
        """
        Adds additional customer communication to an AWS Support case. You use the ``caseId`` value to
        identify the case to add communication to. You can list a set of email addresses to copy on the
        communication using the ``ccEmailAddresses`` value. The ``communicationBody`` value contains the
        text of the communication.

        The response indicates the success or failure of the request.

        This operation implements a subset of the features of the AWS Support Center.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/AddCommunicationToCase>`_

        **Request Syntax**
        ::

          response = client.add_communication_to_case(
              caseId='string',
              communicationBody='string',
              ccEmailAddresses=[
                  'string',
              ],
              attachmentSetId='string'
          )
        :type caseId: string
        :param caseId:

          The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string
          formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*

        :type communicationBody: string
        :param communicationBody: **[REQUIRED]**

          The body of an email communication to add to the support case.

        :type ccEmailAddresses: list
        :param ccEmailAddresses:

          The email addresses in the CC line of an email to be added to the support case.

          - *(string) --*

        :type attachmentSetId: string
        :param attachmentSetId:

          The ID of a set of one or more attachments for the communication to add to the case. Create the
          set by calling  AddAttachmentsToSet

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'result': True|False
            }
          **Response Structure**

          - *(dict) --*

            The result of the  AddCommunicationToCase operation.

            - **result** *(boolean) --*

              True if  AddCommunicationToCase succeeds. Otherwise, returns an error.

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
    def create_case(
        self,
        subject: str,
        communicationBody: str,
        serviceCode: str = None,
        severityCode: str = None,
        categoryCode: str = None,
        ccEmailAddresses: List[str] = None,
        language: str = None,
        issueType: str = None,
        attachmentSetId: str = None,
    ) -> ClientCreateCaseResponseTypeDef:
        """
        Creates a new case in the AWS Support Center. This operation is modeled on the behavior of the AWS
        Support Center `Create Case <https://console.aws.amazon.com/support/home#/case/create>`__ page. Its
        parameters require you to specify the following information:

        * **issueType.** The type of issue for the case. You can specify either "customer-service" or
        "technical." If you do not indicate a value, the default is "technical."

        .. note::

           Service limit increases are not supported by the Support API; you must submit service limit
           increase requests in `Support Center <https://console.aws.amazon.com/support>`__ . The
           ``caseId`` is not the ``displayId`` that appears in `Support Center
           <https://console.aws.amazon.com/support>`__ . You can use the  DescribeCases API to get the
           ``displayId`` .

        * **serviceCode.** The code for an AWS service. You can get the possible ``serviceCode`` values by
        calling  DescribeServices .

        * **categoryCode.** The category for the service defined for the ``serviceCode`` value. You also
        get the category code for a service by calling  DescribeServices . Each AWS service defines its own
        set of category codes.

        * **severityCode.** A value that indicates the urgency of the case, which in turn determines the
        response time according to your service level agreement with AWS Support. You can get the possible
        ``severityCode`` values by calling  DescribeSeverityLevels . For more information about the meaning
        of the codes, see  SeverityLevel and `Choosing a Severity
        <https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity>`__ .

        * **subject.** The **Subject** field on the AWS Support Center `Create Case
        <https://console.aws.amazon.com/support/home#/case/create>`__ page.

        * **communicationBody.** The **Description** field on the AWS Support Center `Create Case
        <https://console.aws.amazon.com/support/home#/case/create>`__ page.

        * **attachmentSetId.** The ID of a set of attachments that has been created by using
        AddAttachmentsToSet .

        * **language.** The human language in which AWS Support handles the case. English and Japanese are
        currently supported.

        * **ccEmailAddresses.** The AWS Support Center **CC** field on the `Create Case
        <https://console.aws.amazon.com/support/home#/case/create>`__ page. You can list email addresses to
        be copied on any correspondence about the case. The account that opens the case is already
        identified by passing the AWS Credentials in the HTTP POST method or in a method or function call
        from one of the programming languages supported by an `AWS SDK <http://aws.amazon.com/tools/>`__ .

        .. note::

          To add additional communication or attachments to an existing case, use  AddCommunicationToCase .

        A successful  CreateCase request returns an AWS Support case number. Case numbers are used by the
        DescribeCases operation to retrieve existing AWS Support cases.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/CreateCase>`_

        **Request Syntax**
        ::

          response = client.create_case(
              subject='string',
              serviceCode='string',
              severityCode='string',
              categoryCode='string',
              communicationBody='string',
              ccEmailAddresses=[
                  'string',
              ],
              language='string',
              issueType='string',
              attachmentSetId='string'
          )
        :type subject: string
        :param subject: **[REQUIRED]**

          The title of the AWS Support case.

        :type serviceCode: string
        :param serviceCode:

          The code for the AWS service returned by the call to  DescribeServices .

        :type severityCode: string
        :param severityCode:

          The code for the severity level returned by the call to  DescribeSeverityLevels .

          .. note::

            The availability of severity levels depends on the support plan for the account.

        :type categoryCode: string
        :param categoryCode:

          The category of problem for the AWS Support case.

        :type communicationBody: string
        :param communicationBody: **[REQUIRED]**

          The communication body text when you create an AWS Support case by calling  CreateCase .

        :type ccEmailAddresses: list
        :param ccEmailAddresses:

          A list of email addresses that AWS Support copies on case correspondence.

          - *(string) --*

        :type language: string
        :param language:

          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports
          English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations
          that take them.

        :type issueType: string
        :param issueType:

          The type of issue for the case. You can specify either "customer-service" or "technical." If you
          do not indicate a value, the default is "technical."

          .. note::

            Service limit increases are not supported by the Support API; you must submit service limit
            increase requests in `Support Center <https://console.aws.amazon.com/support>`__ .

        :type attachmentSetId: string
        :param attachmentSetId:

          The ID of a set of one or more attachments for the case. Create the set by using
          AddAttachmentsToSet .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'caseId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The AWS Support case ID returned by a successful completion of the  CreateCase operation.

            - **caseId** *(string) --*

              The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
              string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attachment(
        self, attachmentId: str
    ) -> ClientDescribeAttachmentResponseTypeDef:
        """
        Returns the attachment that has the specified ID. Attachment IDs are generated by the case
        management system when you add an attachment to a case or case communication. Attachment IDs are
        returned in the  AttachmentDetails objects that are returned by the  DescribeCommunications
        operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeAttachment>`_

        **Request Syntax**
        ::

          response = client.describe_attachment(
              attachmentId='string'
          )
        :type attachmentId: string
        :param attachmentId: **[REQUIRED]**

          The ID of the attachment to return. Attachment IDs are returned by the  DescribeCommunications
          operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'attachment': {
                    'fileName': 'string',
                    'data': b'bytes'
                }
            }
          **Response Structure**

          - *(dict) --*

            The content and file name of the attachment returned by the  DescribeAttachment operation.

            - **attachment** *(dict) --*

              The attachment content and file name.

              - **fileName** *(string) --*

                The name of the attachment file.

              - **data** *(bytes) --*

                The content of the attachment file.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cases(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        nextToken: str = None,
        maxResults: int = None,
        language: str = None,
        includeCommunications: bool = None,
    ) -> ClientDescribeCasesResponseTypeDef:
        """
        Returns a list of cases that you specify by passing one or more case IDs. In addition, you can
        filter the cases by date by setting values for the ``afterTime`` and ``beforeTime`` request
        parameters. You can set values for the ``includeResolvedCases`` and ``includeCommunications``
        request parameters to control how much information is returned.

        Case data is available for 12 months after creation. If a case was created more than 12 months ago,
        a request for data might cause an error.

        The response returns the following in JSON format:

        * One or more  CaseDetails data types.

        * One or more ``nextToken`` values, which specify where to paginate the returned records
        represented by the ``CaseDetails`` objects.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeCases>`_

        **Request Syntax**
        ::

          response = client.describe_cases(
              caseIdList=[
                  'string',
              ],
              displayId='string',
              afterTime='string',
              beforeTime='string',
              includeResolvedCases=True|False,
              nextToken='string',
              maxResults=123,
              language='string',
              includeCommunications=True|False
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

        :type nextToken: string
        :param nextToken:

          A resumption point for pagination.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return before paginating.

        :type language: string
        :param language:

          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports
          English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations
          that take them.

        :type includeCommunications: boolean
        :param includeCommunications:

          Specifies whether communications should be included in the  DescribeCases results. The default is
          *true* .

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              A resumption point for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_communications(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeCommunicationsResponseTypeDef:
        """
        Returns communications (and attachments) for one or more support cases. You can use the
        ``afterTime`` and ``beforeTime`` parameters to filter by date. You can use the ``caseId`` parameter
        to restrict the results to a particular case.

        Case data is available for 12 months after creation. If a case was created more than 12 months ago,
        a request for data might cause an error.

        You can use the ``maxResults`` and ``nextToken`` parameters to control the pagination of the result
        set. Set ``maxResults`` to the number of cases you want displayed on each page, and use
        ``nextToken`` to specify the resumption of pagination.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeCommunications>`_

        **Request Syntax**
        ::

          response = client.describe_communications(
              caseId='string',
              beforeTime='string',
              afterTime='string',
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          A resumption point for pagination.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return before paginating.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              A resumption point for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_services(
        self, serviceCodeList: List[str] = None, language: str = None
    ) -> ClientDescribeServicesResponseTypeDef:
        """
        Returns the current list of AWS services and a list of service categories that applies to each one.
        You then use service names and categories in your  CreateCase requests. Each AWS service has its
        own set of categories.

        The service codes and category codes correspond to the values that are displayed in the **Service**
        and **Category** drop-down lists on the AWS Support Center `Create Case
        <https://console.aws.amazon.com/support/home#/case/create>`__ page. The values in those fields,
        however, do not necessarily match the service codes and categories returned by the
        ``DescribeServices`` request. Always use the service codes and categories obtained
        programmatically. This practice ensures that you always have the most recent set of service and
        category codes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeServices>`_

        **Request Syntax**
        ::

          response = client.describe_services(
              serviceCodeList=[
                  'string',
              ],
              language='string'
          )
        :type serviceCodeList: list
        :param serviceCodeList:

          A JSON-formatted list of service codes available for AWS services.

          - *(string) --*

        :type language: string
        :param language:

          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports
          English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations
          that take them.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'services': [
                    {
                        'code': 'string',
                        'name': 'string',
                        'categories': [
                            {
                                'code': 'string',
                                'name': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            The list of AWS services returned by the  DescribeServices operation.

            - **services** *(list) --*

              A JSON-formatted list of AWS services.

              - *(dict) --*

                Information about an AWS service returned by the  DescribeServices operation.

                - **code** *(string) --*

                  The code for an AWS service returned by the  DescribeServices response. The ``name``
                  element contains the corresponding friendly name.

                - **name** *(string) --*

                  The friendly name for an AWS service. The ``code`` element contains the corresponding
                  code.

                - **categories** *(list) --*

                  A list of categories that describe the type of support issue a case describes. Categories
                  consist of a category name and a category code. Category names and codes are passed to
                  AWS Support when you call  CreateCase .

                  - *(dict) --*

                    A JSON-formatted name/value pair that represents the category name and category code of
                    the problem, selected from the  DescribeServices response for each AWS service.

                    - **code** *(string) --*

                      The category code for the support case.

                    - **name** *(string) --*

                      The category name for the support case.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_severity_levels(self, language: str = None) -> Dict[str, Any]:
        """
        Returns the list of severity levels that you can assign to an AWS Support case. The severity level
        for a case is also a field in the  CaseDetails data type included in any  CreateCase request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeSeverityLevels>`_

        **Request Syntax**
        ::

          response = client.describe_severity_levels(
              language='string'
          )
        :type language: string
        :param language:

          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports
          English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations
          that take them.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'severityLevels': [
                    {
                        'code': 'string',
                        'name': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            The list of severity levels returned by the  DescribeSeverityLevels operation.

            - **severityLevels** *(list) --*

              The available severity levels for the support case. Available severity levels are defined by
              your service level agreement with AWS.

              - *(dict) --*

                A code and name pair that represents the severity level of a support case. The available
                values depend on the support plan for the account. For more information, see `Choosing a
                Severity
                <https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity>`__
                .

                - **code** *(string) --*

                  The code for case severity level.

                  Valid values: ``low`` | ``normal`` | ``high`` | ``urgent`` | ``critical``

                - **name** *(string) --*

                  The name of the severity level that corresponds to the severity level code.

                  .. note::

                    The values returned by the API differ from the values that are displayed in the AWS
                    Support Center. For example, for the code "low", the API name is "Low", but the name in
                    the Support Center is "General guidance". These are the Support Center code/name
                    mappings:

                    * ``low`` : General guidance

                    * ``normal`` : System impaired

                    * ``high`` : Production system impaired

                    * ``urgent`` : Production system down

                    * ``critical`` : Business-critical system down

                  For more information, see `Choosing a Severity
                  <https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity>`__
        <https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity>`__

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusted_advisor_check_refresh_statuses(
        self, checkIds: List[str]
    ) -> ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef:
        """
        Returns the refresh status of the Trusted Advisor checks that have the specified check IDs. Check
        IDs can be obtained by calling  DescribeTrustedAdvisorChecks .

        .. note::

          Some checks are refreshed automatically, and their refresh statuses cannot be retrieved by using
          this operation. Use of the ``DescribeTrustedAdvisorCheckRefreshStatuses`` operation for these
          checks causes an ``InvalidParameterValue`` error.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses>`_
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses>`_

        **Request Syntax**
        ::

          response = client.describe_trusted_advisor_check_refresh_statuses(
              checkIds=[
                  'string',
              ]
          )
        :type checkIds: list
        :param checkIds: **[REQUIRED]**

          The IDs of the Trusted Advisor checks to get the status of. **Note:** Specifying the check ID of
          a check that is automatically refreshed causes an ``InvalidParameterValue`` error.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'statuses': [
                    {
                        'checkId': 'string',
                        'status': 'string',
                        'millisUntilNextRefreshable': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            The statuses of the Trusted Advisor checks returned by the
            DescribeTrustedAdvisorCheckRefreshStatuses operation.

            - **statuses** *(list) --*

              The refresh status of the specified Trusted Advisor checks.

              - *(dict) --*

                The refresh status of a Trusted Advisor check.

                - **checkId** *(string) --*

                  The unique identifier for the Trusted Advisor check.

                - **status** *(string) --*

                  The status of the Trusted Advisor check for which a refresh has been requested:

                  * ``none:`` The check is not refreshed or the non-success status exceeds the timeout

                  * ``enqueued:`` The check refresh requests has entered the refresh queue

                  * ``processing:`` The check refresh request is picked up by the rule processing engine

                  * ``success:`` The check is successfully refreshed

                  * ``abandoned:`` The check refresh has failed

                - **millisUntilNextRefreshable** *(integer) --*

                  The amount of time, in milliseconds, until the Trusted Advisor check is eligible for
                  refresh.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusted_advisor_check_result(
        self, checkId: str, language: str = None
    ) -> ClientDescribeTrustedAdvisorCheckResultResponseTypeDef:
        """
        Returns the results of the Trusted Advisor check that has the specified check ID. Check IDs can be
        obtained by calling  DescribeTrustedAdvisorChecks .

        The response contains a  TrustedAdvisorCheckResult object, which contains these three objects:

        *  TrustedAdvisorCategorySpecificSummary

        *  TrustedAdvisorResourceDetail

        *  TrustedAdvisorResourcesSummary

        In addition, the response contains these fields:

        * **status.** The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or
        "not_available".

        * **timestamp.** The time of the last refresh of the check.

        * **checkId.** The unique identifier for the check.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorCheckResult>`_

        **Request Syntax**
        ::

          response = client.describe_trusted_advisor_check_result(
              checkId='string',
              language='string'
          )
        :type checkId: string
        :param checkId: **[REQUIRED]**

          The unique identifier for the Trusted Advisor check.

        :type language: string
        :param language:

          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports
          English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations
          that take them.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'result': {
                    'checkId': 'string',
                    'timestamp': 'string',
                    'status': 'string',
                    'resourcesSummary': {
                        'resourcesProcessed': 123,
                        'resourcesFlagged': 123,
                        'resourcesIgnored': 123,
                        'resourcesSuppressed': 123
                    },
                    'categorySpecificSummary': {
                        'costOptimizing': {
                            'estimatedMonthlySavings': 123.0,
                            'estimatedPercentMonthlySavings': 123.0
                        }
                    },
                    'flaggedResources': [
                        {
                            'status': 'string',
                            'region': 'string',
                            'resourceId': 'string',
                            'isSuppressed': True|False,
                            'metadata': [
                                'string',
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            The result of the Trusted Advisor check returned by the  DescribeTrustedAdvisorCheckResult
            operation.

            - **result** *(dict) --*

              The detailed results of the Trusted Advisor check.

              - **checkId** *(string) --*

                The unique identifier for the Trusted Advisor check.

              - **timestamp** *(string) --*

                The time of the last refresh of the check.

              - **status** *(string) --*

                The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or
                "not_available".

              - **resourcesSummary** *(dict) --*

                Details about AWS resources that were analyzed in a call to Trusted Advisor
                DescribeTrustedAdvisorCheckSummaries .

                - **resourcesProcessed** *(integer) --*

                  The number of AWS resources that were analyzed by the Trusted Advisor check.

                - **resourcesFlagged** *(integer) --*

                  The number of AWS resources that were flagged (listed) by the Trusted Advisor check.

                - **resourcesIgnored** *(integer) --*

                  The number of AWS resources ignored by Trusted Advisor because information was
                  unavailable.

                - **resourcesSuppressed** *(integer) --*

                  The number of AWS resources ignored by Trusted Advisor because they were marked as
                  suppressed by the user.

              - **categorySpecificSummary** *(dict) --*

                Summary information that relates to the category of the check. Cost Optimizing is the only
                category that is currently supported.

                - **costOptimizing** *(dict) --*

                  The summary information about cost savings for a Trusted Advisor check that is in the
                  Cost Optimizing category.

                  - **estimatedMonthlySavings** *(float) --*

                    The estimated monthly savings that might be realized if the recommended actions are
                    taken.

                  - **estimatedPercentMonthlySavings** *(float) --*

                    The estimated percentage of savings that might be realized if the recommended actions
                    are taken.

              - **flaggedResources** *(list) --*

                The details about each resource listed in the check result.

                - *(dict) --*

                  Contains information about a resource identified by a Trusted Advisor check.

                  - **status** *(string) --*

                    The status code for the resource identified in the Trusted Advisor check.

                  - **region** *(string) --*

                    The AWS region in which the identified resource is located.

                  - **resourceId** *(string) --*

                    The unique identifier for the identified resource.

                  - **isSuppressed** *(boolean) --*

                    Specifies whether the AWS resource was ignored by Trusted Advisor because it was marked
                    as suppressed by the user.

                  - **metadata** *(list) --*

                    Additional information about the identified resource. The exact metadata and its order
                    can be obtained by inspecting the  TrustedAdvisorCheckDescription object returned by
                    the call to  DescribeTrustedAdvisorChecks . **Metadata** contains all the data that is
                    shown in the Excel download, even in those cases where the UI shows just summary data.

                    - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusted_advisor_check_summaries(
        self, checkIds: List[str]
    ) -> ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef:
        """
        Returns the summaries of the results of the Trusted Advisor checks that have the specified check
        IDs. Check IDs can be obtained by calling  DescribeTrustedAdvisorChecks .

        The response contains an array of  TrustedAdvisorCheckSummary objects.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries>`_

        **Request Syntax**
        ::

          response = client.describe_trusted_advisor_check_summaries(
              checkIds=[
                  'string',
              ]
          )
        :type checkIds: list
        :param checkIds: **[REQUIRED]**

          The IDs of the Trusted Advisor checks.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summaries': [
                    {
                        'checkId': 'string',
                        'timestamp': 'string',
                        'status': 'string',
                        'hasFlaggedResources': True|False,
                        'resourcesSummary': {
                            'resourcesProcessed': 123,
                            'resourcesFlagged': 123,
                            'resourcesIgnored': 123,
                            'resourcesSuppressed': 123
                        },
                        'categorySpecificSummary': {
                            'costOptimizing': {
                                'estimatedMonthlySavings': 123.0,
                                'estimatedPercentMonthlySavings': 123.0
                            }
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            The summaries of the Trusted Advisor checks returned by the
            DescribeTrustedAdvisorCheckSummaries operation.

            - **summaries** *(list) --*

              The summary information for the requested Trusted Advisor checks.

              - *(dict) --*

                A summary of a Trusted Advisor check result, including the alert status, last refresh, and
                number of resources examined.

                - **checkId** *(string) --*

                  The unique identifier for the Trusted Advisor check.

                - **timestamp** *(string) --*

                  The time of the last refresh of the check.

                - **status** *(string) --*

                  The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or
                  "not_available".

                - **hasFlaggedResources** *(boolean) --*

                  Specifies whether the Trusted Advisor check has flagged resources.

                - **resourcesSummary** *(dict) --*

                  Details about AWS resources that were analyzed in a call to Trusted Advisor
                  DescribeTrustedAdvisorCheckSummaries .

                  - **resourcesProcessed** *(integer) --*

                    The number of AWS resources that were analyzed by the Trusted Advisor check.

                  - **resourcesFlagged** *(integer) --*

                    The number of AWS resources that were flagged (listed) by the Trusted Advisor check.

                  - **resourcesIgnored** *(integer) --*

                    The number of AWS resources ignored by Trusted Advisor because information was
                    unavailable.

                  - **resourcesSuppressed** *(integer) --*

                    The number of AWS resources ignored by Trusted Advisor because they were marked as
                    suppressed by the user.

                - **categorySpecificSummary** *(dict) --*

                  Summary information that relates to the category of the check. Cost Optimizing is the
                  only category that is currently supported.

                  - **costOptimizing** *(dict) --*

                    The summary information about cost savings for a Trusted Advisor check that is in the
                    Cost Optimizing category.

                    - **estimatedMonthlySavings** *(float) --*

                      The estimated monthly savings that might be realized if the recommended actions are
                      taken.

                    - **estimatedPercentMonthlySavings** *(float) --*

                      The estimated percentage of savings that might be realized if the recommended actions
                      are taken.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusted_advisor_checks(
        self, language: str
    ) -> ClientDescribeTrustedAdvisorChecksResponseTypeDef:
        """
        Returns information about all available Trusted Advisor checks, including name, ID, category,
        description, and metadata. You must specify a language code; English ("en") and Japanese ("ja") are
        currently supported. The response contains a  TrustedAdvisorCheckDescription for each check. The
        region must be set to us-east-1.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorChecks>`_

        **Request Syntax**
        ::

          response = client.describe_trusted_advisor_checks(
              language='string'
          )
        :type language: string
        :param language: **[REQUIRED]**

          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports
          English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations
          that take them.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'checks': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'description': 'string',
                        'category': 'string',
                        'metadata': [
                            'string',
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Information about the Trusted Advisor checks returned by the  DescribeTrustedAdvisorChecks
            operation.

            - **checks** *(list) --*

              Information about all available Trusted Advisor checks.

              - *(dict) --*

                The description and metadata for a Trusted Advisor check.

                - **id** *(string) --*

                  The unique identifier for the Trusted Advisor check.

                - **name** *(string) --*

                  The display name for the Trusted Advisor check.

                - **description** *(string) --*

                  The description of the Trusted Advisor check, which includes the alert criteria and
                  recommended actions (contains HTML markup).

                - **category** *(string) --*

                  The category of the Trusted Advisor check.

                - **metadata** *(list) --*

                  The column headings for the data returned by the Trusted Advisor check. The order of the
                  headings corresponds to the order of the data in the **Metadata** element of the
                  TrustedAdvisorResourceDetail for the check. **Metadata** contains all the data that is
                  shown in the Excel download, even in those cases where the UI shows just summary data.

                  - *(string) --*

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
    def refresh_trusted_advisor_check(
        self, checkId: str
    ) -> ClientRefreshTrustedAdvisorCheckResponseTypeDef:
        """
        Requests a refresh of the Trusted Advisor check that has the specified check ID. Check IDs can be
        obtained by calling  DescribeTrustedAdvisorChecks .

        .. note::

          Some checks are refreshed automatically, and they cannot be refreshed by using this operation.
          Use of the ``RefreshTrustedAdvisorCheck`` operation for these checks causes an
          ``InvalidParameterValue`` error.

        The response contains a  TrustedAdvisorCheckRefreshStatus object, which contains these fields:

        * **status.** The refresh status of the check:

          * ``none:`` The check is not refreshed or the non-success status exceeds the timeout

          * ``enqueued:`` The check refresh requests has entered the refresh queue

          * ``processing:`` The check refresh request is picked up by the rule processing engine

          * ``success:`` The check is successfully refreshed

          * ``abandoned:`` The check refresh has failed

        * **millisUntilNextRefreshable.** The amount of time, in milliseconds, until the check is eligible
        for refresh.

        * **checkId.** The unique identifier for the check.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/RefreshTrustedAdvisorCheck>`_

        **Request Syntax**
        ::

          response = client.refresh_trusted_advisor_check(
              checkId='string'
          )
        :type checkId: string
        :param checkId: **[REQUIRED]**

          The unique identifier for the Trusted Advisor check to refresh. **Note:** Specifying the check ID
          of a check that is automatically refreshed causes an ``InvalidParameterValue`` error.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'status': {
                    'checkId': 'string',
                    'status': 'string',
                    'millisUntilNextRefreshable': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            The current refresh status of a Trusted Advisor check.

            - **status** *(dict) --*

              The current refresh status for a check, including the amount of time until the check is
              eligible for refresh.

              - **checkId** *(string) --*

                The unique identifier for the Trusted Advisor check.

              - **status** *(string) --*

                The status of the Trusted Advisor check for which a refresh has been requested:

                * ``none:`` The check is not refreshed or the non-success status exceeds the timeout

                * ``enqueued:`` The check refresh requests has entered the refresh queue

                * ``processing:`` The check refresh request is picked up by the rule processing engine

                * ``success:`` The check is successfully refreshed

                * ``abandoned:`` The check refresh has failed

              - **millisUntilNextRefreshable** *(integer) --*

                The amount of time, in milliseconds, until the Trusted Advisor check is eligible for
                refresh.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resolve_case(self, caseId: str = None) -> ClientResolveCaseResponseTypeDef:
        """
        Takes a ``caseId`` and returns the initial state of the case along with the state of the case after
        the call to  ResolveCase completed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/ResolveCase>`_

        **Request Syntax**
        ::

          response = client.resolve_case(
              caseId='string'
          )
        :type caseId: string
        :param caseId:

          The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string
          formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'initialCaseStatus': 'string',
                'finalCaseStatus': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The status of the case returned by the  ResolveCase operation.

            - **initialCaseStatus** *(string) --*

              The status of the case when the  ResolveCase request was sent.

            - **finalCaseStatus** *(string) --*

              The status of the case after the  ResolveCase request was processed.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cases"]
    ) -> paginator_scope.DescribeCasesPaginator:
        """
        Get Paginator for `describe_cases` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_communications"]
    ) -> paginator_scope.DescribeCommunicationsPaginator:
        """
        Get Paginator for `describe_communications` operation.
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
    AttachmentIdNotFound: Boto3ClientError
    AttachmentLimitExceeded: Boto3ClientError
    AttachmentSetExpired: Boto3ClientError
    AttachmentSetIdNotFound: Boto3ClientError
    AttachmentSetSizeLimitExceeded: Boto3ClientError
    CaseCreationLimitExceeded: Boto3ClientError
    CaseIdNotFound: Boto3ClientError
    ClientError: Boto3ClientError
    DescribeAttachmentLimitExceeded: Boto3ClientError
    InternalServerError: Boto3ClientError
