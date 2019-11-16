"Main interface for support type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddAttachmentsToSetResponseTypeDef",
    "ClientAddAttachmentsToSetattachmentsTypeDef",
    "ClientAddCommunicationToCaseResponseTypeDef",
    "ClientCreateCaseResponseTypeDef",
    "ClientDescribeAttachmentResponseattachmentTypeDef",
    "ClientDescribeAttachmentResponseTypeDef",
    "ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    "ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef",
    "ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef",
    "ClientDescribeCasesResponsecasesTypeDef",
    "ClientDescribeCasesResponseTypeDef",
    "ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef",
    "ClientDescribeCommunicationsResponsecommunicationsTypeDef",
    "ClientDescribeCommunicationsResponseTypeDef",
    "ClientDescribeServicesResponseservicescategoriesTypeDef",
    "ClientDescribeServicesResponseservicesTypeDef",
    "ClientDescribeServicesResponseTypeDef",
    "ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef",
    "ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    "ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef",
    "ClientDescribeTrustedAdvisorChecksResponseTypeDef",
    "ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef",
    "ClientRefreshTrustedAdvisorCheckResponseTypeDef",
    "ClientResolveCaseResponseTypeDef",
    "DescribeCasesPaginatePaginationConfigTypeDef",
    "DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    "DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef",
    "DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef",
    "DescribeCasesPaginateResponsecasesTypeDef",
    "DescribeCasesPaginateResponseTypeDef",
    "DescribeCommunicationsPaginatePaginationConfigTypeDef",
    "DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef",
    "DescribeCommunicationsPaginateResponsecommunicationsTypeDef",
    "DescribeCommunicationsPaginateResponseTypeDef",
)


_ClientAddAttachmentsToSetResponseTypeDef = TypedDict(
    "_ClientAddAttachmentsToSetResponseTypeDef",
    {"attachmentSetId": str, "expiryTime": str},
    total=False,
)


class ClientAddAttachmentsToSetResponseTypeDef(
    _ClientAddAttachmentsToSetResponseTypeDef
):
    """
    Type definition for `ClientAddAttachmentsToSet` `Response`

    The ID and expiry time of the attachment set returned by the  AddAttachmentsToSet operation.

    - **attachmentSetId** *(string) --*

      The ID of the attachment set. If an ``attachmentSetId`` was not specified, a new attachment
      set is created, and the ID of the set is returned in the response. If an ``attachmentSetId``
      was specified, the attachments are added to the specified set, if it exists.

    - **expiryTime** *(string) --*

      The time and date when the attachment set expires.
    """


_ClientAddAttachmentsToSetattachmentsTypeDef = TypedDict(
    "_ClientAddAttachmentsToSetattachmentsTypeDef",
    {"fileName": str, "data": bytes},
    total=False,
)


class ClientAddAttachmentsToSetattachmentsTypeDef(
    _ClientAddAttachmentsToSetattachmentsTypeDef
):
    """
    Type definition for `ClientAddAttachmentsToSet` `attachments`

    An attachment to a case communication. The attachment consists of the file name and the content
    of the file.

    - **fileName** *(string) --*

      The name of the attachment file.

    - **data** *(bytes) --*

      The content of the attachment file.
    """


_ClientAddCommunicationToCaseResponseTypeDef = TypedDict(
    "_ClientAddCommunicationToCaseResponseTypeDef", {"result": bool}, total=False
)


class ClientAddCommunicationToCaseResponseTypeDef(
    _ClientAddCommunicationToCaseResponseTypeDef
):
    """
    Type definition for `ClientAddCommunicationToCase` `Response`

    The result of the  AddCommunicationToCase operation.

    - **result** *(boolean) --*

      True if  AddCommunicationToCase succeeds. Otherwise, returns an error.
    """


_ClientCreateCaseResponseTypeDef = TypedDict(
    "_ClientCreateCaseResponseTypeDef", {"caseId": str}, total=False
)


class ClientCreateCaseResponseTypeDef(_ClientCreateCaseResponseTypeDef):
    """
    Type definition for `ClientCreateCase` `Response`

    The AWS Support case ID returned by a successful completion of the  CreateCase operation.

    - **caseId** *(string) --*

      The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
      string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_ClientDescribeAttachmentResponseattachmentTypeDef = TypedDict(
    "_ClientDescribeAttachmentResponseattachmentTypeDef",
    {"fileName": str, "data": bytes},
    total=False,
)


class ClientDescribeAttachmentResponseattachmentTypeDef(
    _ClientDescribeAttachmentResponseattachmentTypeDef
):
    """
    Type definition for `ClientDescribeAttachmentResponse` `attachment`

    The attachment content and file name.

    - **fileName** *(string) --*

      The name of the attachment file.

    - **data** *(bytes) --*

      The content of the attachment file.
    """


_ClientDescribeAttachmentResponseTypeDef = TypedDict(
    "_ClientDescribeAttachmentResponseTypeDef",
    {"attachment": ClientDescribeAttachmentResponseattachmentTypeDef},
    total=False,
)


class ClientDescribeAttachmentResponseTypeDef(_ClientDescribeAttachmentResponseTypeDef):
    """
    Type definition for `ClientDescribeAttachment` `Response`

    The content and file name of the attachment returned by the  DescribeAttachment operation.

    - **attachment** *(dict) --*

      The attachment content and file name.

      - **fileName** *(string) --*

        The name of the attachment file.

      - **data** *(bytes) --*

        The content of the attachment file.
    """


_ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef = TypedDict(
    "_ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)


class ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef(
    _ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
):
    """
    Type definition for `ClientDescribeCasesResponsecasesrecentCommunicationscommunications` `attachmentSet`

    The file name and ID of an attachment to a case communication. You can use the ID
    to retrieve the attachment with the  DescribeAttachment operation.

    - **attachmentId** *(string) --*

      The ID of the attachment.

    - **fileName** *(string) --*

      The file name of the attachment.
    """


_ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef = TypedDict(
    "_ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef(
    _ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef
):
    """
    Type definition for `ClientDescribeCasesResponsecasesrecentCommunications` `communications`

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
    """


_ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef = TypedDict(
    "_ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef",
    {
        "communications": List[
            ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef(
    _ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef
):
    """
    Type definition for `ClientDescribeCasesResponsecases` `recentCommunications`

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
    """


_ClientDescribeCasesResponsecasesTypeDef = TypedDict(
    "_ClientDescribeCasesResponsecasesTypeDef",
    {
        "caseId": str,
        "displayId": str,
        "subject": str,
        "status": str,
        "serviceCode": str,
        "categoryCode": str,
        "severityCode": str,
        "submittedBy": str,
        "timeCreated": str,
        "recentCommunications": ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef,
        "ccEmailAddresses": List[str],
        "language": str,
    },
    total=False,
)


class ClientDescribeCasesResponsecasesTypeDef(_ClientDescribeCasesResponsecasesTypeDef):
    """
    Type definition for `ClientDescribeCasesResponse` `cases`

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
    """


_ClientDescribeCasesResponseTypeDef = TypedDict(
    "_ClientDescribeCasesResponseTypeDef",
    {"cases": List[ClientDescribeCasesResponsecasesTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeCasesResponseTypeDef(_ClientDescribeCasesResponseTypeDef):
    """
    Type definition for `ClientDescribeCases` `Response`

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


_ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef = TypedDict(
    "_ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)


class ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef(
    _ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef
):
    """
    Type definition for `ClientDescribeCommunicationsResponsecommunications` `attachmentSet`

    The file name and ID of an attachment to a case communication. You can use the ID to
    retrieve the attachment with the  DescribeAttachment operation.

    - **attachmentId** *(string) --*

      The ID of the attachment.

    - **fileName** *(string) --*

      The file name of the attachment.
    """


_ClientDescribeCommunicationsResponsecommunicationsTypeDef = TypedDict(
    "_ClientDescribeCommunicationsResponsecommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCommunicationsResponsecommunicationsTypeDef(
    _ClientDescribeCommunicationsResponsecommunicationsTypeDef
):
    """
    Type definition for `ClientDescribeCommunicationsResponse` `communications`

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
    """


_ClientDescribeCommunicationsResponseTypeDef = TypedDict(
    "_ClientDescribeCommunicationsResponseTypeDef",
    {
        "communications": List[
            ClientDescribeCommunicationsResponsecommunicationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeCommunicationsResponseTypeDef(
    _ClientDescribeCommunicationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeCommunications` `Response`

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


_ClientDescribeServicesResponseservicescategoriesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicescategoriesTypeDef",
    {"code": str, "name": str},
    total=False,
)


class ClientDescribeServicesResponseservicescategoriesTypeDef(
    _ClientDescribeServicesResponseservicescategoriesTypeDef
):
    """
    Type definition for `ClientDescribeServicesResponseservices` `categories`

    A JSON-formatted name/value pair that represents the category name and category code of
    the problem, selected from the  DescribeServices response for each AWS service.

    - **code** *(string) --*

      The category code for the support case.

    - **name** *(string) --*

      The category name for the support case.
    """


_ClientDescribeServicesResponseservicesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesTypeDef",
    {
        "code": str,
        "name": str,
        "categories": List[ClientDescribeServicesResponseservicescategoriesTypeDef],
    },
    total=False,
)


class ClientDescribeServicesResponseservicesTypeDef(
    _ClientDescribeServicesResponseservicesTypeDef
):
    """
    Type definition for `ClientDescribeServicesResponse` `services`

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


_ClientDescribeServicesResponseTypeDef = TypedDict(
    "_ClientDescribeServicesResponseTypeDef",
    {"services": List[ClientDescribeServicesResponseservicesTypeDef]},
    total=False,
)


class ClientDescribeServicesResponseTypeDef(_ClientDescribeServicesResponseTypeDef):
    """
    Type definition for `ClientDescribeServices` `Response`

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


_ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef",
    {"checkId": str, "status": str, "millisUntilNextRefreshable": int},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef(
    _ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckRefreshStatusesResponse` `statuses`

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


_ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    {
        "statuses": List[
            ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef(
    _ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckRefreshStatuses` `Response`

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


_ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef",
    {"estimatedMonthlySavings": float, "estimatedPercentMonthlySavings": float},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummary` `costOptimizing`

    The summary information about cost savings for a Trusted Advisor check that is in the
    Cost Optimizing category.

    - **estimatedMonthlySavings** *(float) --*

      The estimated monthly savings that might be realized if the recommended actions are
      taken.

    - **estimatedPercentMonthlySavings** *(float) --*

      The estimated percentage of savings that might be realized if the recommended actions
      are taken.
    """


_ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef",
    {
        "costOptimizing": ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckResultResponseresult` `categorySpecificSummary`

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
    """


_ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef",
    {
        "status": str,
        "region": str,
        "resourceId": str,
        "isSuppressed": bool,
        "metadata": List[str],
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckResultResponseresult` `flaggedResources`

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


_ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckResultResponseresult` `resourcesSummary`

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
    """


_ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef,
        "categorySpecificSummary": ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef,
        "flaggedResources": List[
            ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckResultResponse` `result`

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


_ClientDescribeTrustedAdvisorCheckResultResponseTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseTypeDef",
    {"result": ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckResult` `Response`

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


_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef",
    {"estimatedMonthlySavings": float, "estimatedPercentMonthlySavings": float},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummary` `costOptimizing`

    The summary information about cost savings for a Trusted Advisor check that is in the
    Cost Optimizing category.

    - **estimatedMonthlySavings** *(float) --*

      The estimated monthly savings that might be realized if the recommended actions are
      taken.

    - **estimatedPercentMonthlySavings** *(float) --*

      The estimated percentage of savings that might be realized if the recommended actions
      are taken.
    """


_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef",
    {
        "costOptimizing": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckSummariesResponsesummaries` `categorySpecificSummary`

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


_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckSummariesResponsesummaries` `resourcesSummary`

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
    """


_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "hasFlaggedResources": bool,
        "resourcesSummary": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef,
        "categorySpecificSummary": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef,
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckSummariesResponse` `summaries`

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


_ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    {
        "summaries": List[
            ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorCheckSummaries` `Response`

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


_ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "category": str,
        "metadata": List[str],
    },
    total=False,
)


class ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef(
    _ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorChecksResponse` `checks`

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


_ClientDescribeTrustedAdvisorChecksResponseTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorChecksResponseTypeDef",
    {"checks": List[ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef]},
    total=False,
)


class ClientDescribeTrustedAdvisorChecksResponseTypeDef(
    _ClientDescribeTrustedAdvisorChecksResponseTypeDef
):
    """
    Type definition for `ClientDescribeTrustedAdvisorChecks` `Response`

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


_ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef = TypedDict(
    "_ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef",
    {"checkId": str, "status": str, "millisUntilNextRefreshable": int},
    total=False,
)


class ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef(
    _ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef
):
    """
    Type definition for `ClientRefreshTrustedAdvisorCheckResponse` `status`

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


_ClientRefreshTrustedAdvisorCheckResponseTypeDef = TypedDict(
    "_ClientRefreshTrustedAdvisorCheckResponseTypeDef",
    {"status": ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef},
    total=False,
)


class ClientRefreshTrustedAdvisorCheckResponseTypeDef(
    _ClientRefreshTrustedAdvisorCheckResponseTypeDef
):
    """
    Type definition for `ClientRefreshTrustedAdvisorCheck` `Response`

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


_ClientResolveCaseResponseTypeDef = TypedDict(
    "_ClientResolveCaseResponseTypeDef",
    {"initialCaseStatus": str, "finalCaseStatus": str},
    total=False,
)


class ClientResolveCaseResponseTypeDef(_ClientResolveCaseResponseTypeDef):
    """
    Type definition for `ClientResolveCase` `Response`

    The status of the case returned by the  ResolveCase operation.

    - **initialCaseStatus** *(string) --*

      The status of the case when the  ResolveCase request was sent.

    - **finalCaseStatus** *(string) --*

      The status of the case after the  ResolveCase request was processed.
    """


_DescribeCasesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCasesPaginatePaginationConfigTypeDef(
    _DescribeCasesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCasesPaginate` `PaginationConfig`

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


_DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef = TypedDict(
    "_DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)


class DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef(
    _DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
):
    """
    Type definition for `DescribeCasesPaginateResponsecasesrecentCommunicationscommunications` `attachmentSet`

    The file name and ID of an attachment to a case communication. You can use the ID
    to retrieve the attachment with the  DescribeAttachment operation.

    - **attachmentId** *(string) --*

      The ID of the attachment.

    - **fileName** *(string) --*

      The file name of the attachment.
    """


_DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef = TypedDict(
    "_DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)


class DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef(
    _DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef
):
    """
    Type definition for `DescribeCasesPaginateResponsecasesrecentCommunications` `communications`

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
    """


_DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef = TypedDict(
    "_DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef",
    {
        "communications": List[
            DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef(
    _DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef
):
    """
    Type definition for `DescribeCasesPaginateResponsecases` `recentCommunications`

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
    """


_DescribeCasesPaginateResponsecasesTypeDef = TypedDict(
    "_DescribeCasesPaginateResponsecasesTypeDef",
    {
        "caseId": str,
        "displayId": str,
        "subject": str,
        "status": str,
        "serviceCode": str,
        "categoryCode": str,
        "severityCode": str,
        "submittedBy": str,
        "timeCreated": str,
        "recentCommunications": DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef,
        "ccEmailAddresses": List[str],
        "language": str,
    },
    total=False,
)


class DescribeCasesPaginateResponsecasesTypeDef(
    _DescribeCasesPaginateResponsecasesTypeDef
):
    """
    Type definition for `DescribeCasesPaginateResponse` `cases`

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
    """


_DescribeCasesPaginateResponseTypeDef = TypedDict(
    "_DescribeCasesPaginateResponseTypeDef",
    {"cases": List[DescribeCasesPaginateResponsecasesTypeDef], "NextToken": str},
    total=False,
)


class DescribeCasesPaginateResponseTypeDef(_DescribeCasesPaginateResponseTypeDef):
    """
    Type definition for `DescribeCasesPaginate` `Response`

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


_DescribeCommunicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCommunicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCommunicationsPaginatePaginationConfigTypeDef(
    _DescribeCommunicationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCommunicationsPaginate` `PaginationConfig`

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


_DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef = TypedDict(
    "_DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)


class DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef(
    _DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef
):
    """
    Type definition for `DescribeCommunicationsPaginateResponsecommunications` `attachmentSet`

    The file name and ID of an attachment to a case communication. You can use the ID to
    retrieve the attachment with the  DescribeAttachment operation.

    - **attachmentId** *(string) --*

      The ID of the attachment.

    - **fileName** *(string) --*

      The file name of the attachment.
    """


_DescribeCommunicationsPaginateResponsecommunicationsTypeDef = TypedDict(
    "_DescribeCommunicationsPaginateResponsecommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)


class DescribeCommunicationsPaginateResponsecommunicationsTypeDef(
    _DescribeCommunicationsPaginateResponsecommunicationsTypeDef
):
    """
    Type definition for `DescribeCommunicationsPaginateResponse` `communications`

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
    """


_DescribeCommunicationsPaginateResponseTypeDef = TypedDict(
    "_DescribeCommunicationsPaginateResponseTypeDef",
    {
        "communications": List[
            DescribeCommunicationsPaginateResponsecommunicationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCommunicationsPaginateResponseTypeDef(
    _DescribeCommunicationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeCommunicationsPaginate` `Response`

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
