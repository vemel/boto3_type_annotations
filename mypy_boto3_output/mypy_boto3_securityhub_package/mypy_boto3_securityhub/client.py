"Main interface for securityhub Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_securityhub.client as client_scope

# pylint: disable=import-self
import mypy_boto3_securityhub.paginator as paginator_scope
from mypy_boto3_securityhub.type_defs import (
    ClientBatchDisableStandardsResponseTypeDef,
    ClientBatchEnableStandardsResponseTypeDef,
    ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef,
    ClientBatchImportFindingsFindingsTypeDef,
    ClientBatchImportFindingsResponseTypeDef,
    ClientCreateActionTargetResponseTypeDef,
    ClientCreateInsightFiltersTypeDef,
    ClientCreateInsightResponseTypeDef,
    ClientCreateMembersAccountDetailsTypeDef,
    ClientCreateMembersResponseTypeDef,
    ClientDeclineInvitationsResponseTypeDef,
    ClientDeleteActionTargetResponseTypeDef,
    ClientDeleteInsightResponseTypeDef,
    ClientDeleteInvitationsResponseTypeDef,
    ClientDeleteMembersResponseTypeDef,
    ClientDescribeActionTargetsResponseTypeDef,
    ClientDescribeHubResponseTypeDef,
    ClientDescribeProductsResponseTypeDef,
    ClientEnableImportFindingsForProductResponseTypeDef,
    ClientGetEnabledStandardsResponseTypeDef,
    ClientGetFindingsFiltersTypeDef,
    ClientGetFindingsResponseTypeDef,
    ClientGetFindingsSortCriteriaTypeDef,
    ClientGetInsightResultsResponseTypeDef,
    ClientGetInsightsResponseTypeDef,
    ClientGetInvitationsCountResponseTypeDef,
    ClientGetMasterAccountResponseTypeDef,
    ClientGetMembersResponseTypeDef,
    ClientInviteMembersResponseTypeDef,
    ClientListEnabledProductsForImportResponseTypeDef,
    ClientListInvitationsResponseTypeDef,
    ClientListMembersResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateFindingsFiltersTypeDef,
    ClientUpdateFindingsNoteTypeDef,
    ClientUpdateInsightFiltersTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_invitation(self, MasterId: str, InvitationId: str) -> Dict[str, Any]:
        """
        Accepts the invitation to be a member account and be monitored by the Security Hub master account
        that the invitation was sent from. When the member account accepts the invitation, permission is
        granted to the master account to view findings generated in the member account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/AcceptInvitation>`_

        **Request Syntax**
        ::

          response = client.accept_invitation(
              MasterId='string',
              InvitationId='string'
          )
        :type MasterId: string
        :param MasterId: **[REQUIRED]**

          The account ID of the Security Hub master account that sent the invitation.

        :type InvitationId: string
        :param InvitationId: **[REQUIRED]**

          The ID of the invitation sent from the Security Hub master account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_disable_standards(
        self, StandardsSubscriptionArns: List[str]
    ) -> ClientBatchDisableStandardsResponseTypeDef:
        """
        Disables the standards specified by the provided ``StandardsSubscriptionArns`` . For more
        information, see `Standards Supported in AWS Security Hub
        <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchDisableStandards>`_

        **Request Syntax**
        ::

          response = client.batch_disable_standards(
              StandardsSubscriptionArns=[
                  'string',
              ]
          )
        :type StandardsSubscriptionArns: list
        :param StandardsSubscriptionArns: **[REQUIRED]**

          The ARNs of the standards subscriptions to disable.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StandardsSubscriptions': [
                    {
                        'StandardsSubscriptionArn': 'string',
                        'StandardsArn': 'string',
                        'StandardsInput': {
                            'string': 'string'
                        },
                        'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **StandardsSubscriptions** *(list) --*

              The details of the standards subscriptions that were disabled.

              - *(dict) --*

                A resource that represents your subscription to a supported standard.

                - **StandardsSubscriptionArn** *(string) --*

                  The ARN of a resource that represents your subscription to a supported standard.

                - **StandardsArn** *(string) --*

                  The ARN of a standard.

                  In this release, Security Hub supports only the CIS AWS Foundations standard, which uses
                  the following ARN:
                  ``arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0.``

                - **StandardsInput** *(dict) --*

                  A key-value pair of input for the standard.

                  - *(string) --*

                    - *(string) --*

                - **StandardsStatus** *(string) --*

                  The status of the standards subscription.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_enable_standards(
        self,
        StandardsSubscriptionRequests: List[
            ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef
        ],
    ) -> ClientBatchEnableStandardsResponseTypeDef:
        """
        Enables the standards specified by the provided ``standardsArn`` . In this release, only CIS AWS
        Foundations standards are supported. For more information, see `Standards Supported in AWS Security
        Hub <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchEnableStandards>`_

        **Request Syntax**
        ::

          response = client.batch_enable_standards(
              StandardsSubscriptionRequests=[
                  {
                      'StandardsArn': 'string',
                      'StandardsInput': {
                          'string': 'string'
                      }
                  },
              ]
          )
        :type StandardsSubscriptionRequests: list
        :param StandardsSubscriptionRequests: **[REQUIRED]**

          The list of standards compliance checks to enable.

          .. warning::

            In this release, Security Hub supports only the CIS AWS Foundations standard.

            The ARN for the standard is
            ``arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0`` .

          - *(dict) --*

            The standard that you want to enable.

            - **StandardsArn** *(string) --* **[REQUIRED]**

              The ARN of the standard that you want to enable.

              .. warning::

                In this release, Security Hub only supports the CIS AWS Foundations standard.

                Its ARN is ``arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0`` .

            - **StandardsInput** *(dict) --*

              A key-value pair of input for the standard.

              - *(string) --*

                - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StandardsSubscriptions': [
                    {
                        'StandardsSubscriptionArn': 'string',
                        'StandardsArn': 'string',
                        'StandardsInput': {
                            'string': 'string'
                        },
                        'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **StandardsSubscriptions** *(list) --*

              The details of the standards subscriptions that were enabled.

              - *(dict) --*

                A resource that represents your subscription to a supported standard.

                - **StandardsSubscriptionArn** *(string) --*

                  The ARN of a resource that represents your subscription to a supported standard.

                - **StandardsArn** *(string) --*

                  The ARN of a standard.

                  In this release, Security Hub supports only the CIS AWS Foundations standard, which uses
                  the following ARN:
                  ``arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0.``

                - **StandardsInput** *(dict) --*

                  A key-value pair of input for the standard.

                  - *(string) --*

                    - *(string) --*

                - **StandardsStatus** *(string) --*

                  The status of the standards subscription.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_import_findings(
        self, Findings: List[ClientBatchImportFindingsFindingsTypeDef]
    ) -> ClientBatchImportFindingsResponseTypeDef:
        """
        Imports security findings generated from an integrated third-party product into Security Hub. This
        action is requested by the integrated product to import its findings into Security Hub. The maximum
        allowed size for a finding is 240 Kb. An error is returned for any finding larger than 240 Kb.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchImportFindings>`_

        **Request Syntax**
        ::

          response = client.batch_import_findings(
              Findings=[
                  {
                      'SchemaVersion': 'string',
                      'Id': 'string',
                      'ProductArn': 'string',
                      'GeneratorId': 'string',
                      'AwsAccountId': 'string',
                      'Types': [
                          'string',
                      ],
                      'FirstObservedAt': 'string',
                      'LastObservedAt': 'string',
                      'CreatedAt': 'string',
                      'UpdatedAt': 'string',
                      'Severity': {
                          'Product': 123.0,
                          'Normalized': 123
                      },
                      'Confidence': 123,
                      'Criticality': 123,
                      'Title': 'string',
                      'Description': 'string',
                      'Remediation': {
                          'Recommendation': {
                              'Text': 'string',
                              'Url': 'string'
                          }
                      },
                      'SourceUrl': 'string',
                      'ProductFields': {
                          'string': 'string'
                      },
                      'UserDefinedFields': {
                          'string': 'string'
                      },
                      'Malware': [
                          {
                              'Name': 'string',
                              'Type':
                              'ADWARE'|'BLENDED_THREAT'|'BOTNET_AGENT'|'COIN_MINER'|'EXPLOIT_KIT'
                              |'KEYLOGGER'|'MACRO'|'POTENTIALLY_UNWANTED'|'SPYWARE'|'RANSOMWARE'
                              |'REMOTE_ACCESS'|'ROOTKIT'|'TROJAN'|'VIRUS'|'WORM',
                              'Path': 'string',
                              'State': 'OBSERVED'|'REMOVAL_FAILED'|'REMOVED'
                          },
                      ],
                      'Network': {
                          'Direction': 'IN'|'OUT',
                          'Protocol': 'string',
                          'SourceIpV4': 'string',
                          'SourceIpV6': 'string',
                          'SourcePort': 123,
                          'SourceDomain': 'string',
                          'SourceMac': 'string',
                          'DestinationIpV4': 'string',
                          'DestinationIpV6': 'string',
                          'DestinationPort': 123,
                          'DestinationDomain': 'string'
                      },
                      'Process': {
                          'Name': 'string',
                          'Path': 'string',
                          'Pid': 123,
                          'ParentPid': 123,
                          'LaunchedAt': 'string',
                          'TerminatedAt': 'string'
                      },
                      'ThreatIntelIndicators': [
                          {
                              'Type':
                              'DOMAIN'|'EMAIL_ADDRESS'|'HASH_MD5'|'HASH_SHA1'|'HASH_SHA256'|'HASH_SHA512'
                              |'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MUTEX'|'PROCESS'|'URL',
                              'Value': 'string',
                              'Category':
                              'BACKDOOR'|'CARD_STEALER'|'COMMAND_AND_CONTROL'|'DROP_SITE'|'EXPLOIT_SITE'
                              |'KEYLOGGER',
                              'LastObservedAt': 'string',
                              'Source': 'string',
                              'SourceUrl': 'string'
                          },
                      ],
                      'Resources': [
                          {
                              'Type': 'string',
                              'Id': 'string',
                              'Partition': 'aws'|'aws-cn'|'aws-us-gov',
                              'Region': 'string',
                              'Tags': {
                                  'string': 'string'
                              },
                              'Details': {
                                  'AwsEc2Instance': {
                                      'Type': 'string',
                                      'ImageId': 'string',
                                      'IpV4Addresses': [
                                          'string',
                                      ],
                                      'IpV6Addresses': [
                                          'string',
                                      ],
                                      'KeyName': 'string',
                                      'IamInstanceProfileArn': 'string',
                                      'VpcId': 'string',
                                      'SubnetId': 'string',
                                      'LaunchedAt': 'string'
                                  },
                                  'AwsS3Bucket': {
                                      'OwnerId': 'string',
                                      'OwnerName': 'string'
                                  },
                                  'AwsIamAccessKey': {
                                      'UserName': 'string',
                                      'Status': 'Active'|'Inactive',
                                      'CreatedAt': 'string'
                                  },
                                  'Container': {
                                      'Name': 'string',
                                      'ImageId': 'string',
                                      'ImageName': 'string',
                                      'LaunchedAt': 'string'
                                  },
                                  'Other': {
                                      'string': 'string'
                                  }
                              }
                          },
                      ],
                      'Compliance': {
                          'Status': 'PASSED'|'WARNING'|'FAILED'|'NOT_AVAILABLE'
                      },
                      'VerificationState': 'UNKNOWN'|'TRUE_POSITIVE'|'FALSE_POSITIVE'|'BENIGN_POSITIVE',
                      'WorkflowState': 'NEW'|'ASSIGNED'|'IN_PROGRESS'|'DEFERRED'|'RESOLVED',
                      'RecordState': 'ACTIVE'|'ARCHIVED',
                      'RelatedFindings': [
                          {
                              'ProductArn': 'string',
                              'Id': 'string'
                          },
                      ],
                      'Note': {
                          'Text': 'string',
                          'UpdatedBy': 'string',
                          'UpdatedAt': 'string'
                      }
                  },
              ]
          )
        :type Findings: list
        :param Findings: **[REQUIRED]**

          A list of findings to import. To successfully import a finding, it must follow the `AWS Security
          Finding Format
          <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`__ .

          - *(dict) --*

            Provides consistent format for the contents of the Security Hub-aggregated findings.
            ``AwsSecurityFinding`` format enables you to share findings between AWS security services and
            third-party solutions, and compliance checks.

            .. note::

              A finding is a potential security issue generated either by AWS services (Amazon GuardDuty,
              Amazon Inspector, and Amazon Macie) or by the integrated third-party solutions and compliance
              checks.

            - **SchemaVersion** *(string) --* **[REQUIRED]**

              The schema version that a finding is formatted for.

            - **Id** *(string) --* **[REQUIRED]**

              The security findings provider-specific identifier for a finding.

            - **ProductArn** *(string) --* **[REQUIRED]**

              The ARN generated by Security Hub that uniquely identifies a third-party company
              (security-findings provider) after this provider's product (solution that generates findings)
              is registered with Security Hub.

            - **GeneratorId** *(string) --* **[REQUIRED]**

              The identifier for the solution-specific component (a discrete unit of logic) that generated
              a finding. In various security-findings providers' solutions, this generator can be called a
              rule, a check, a detector, a plug-in, etc.

            - **AwsAccountId** *(string) --* **[REQUIRED]**

              The AWS account ID that a finding is generated in.

            - **Types** *(list) --* **[REQUIRED]**

              One or more finding types in the format of ``namespace/category/classifier`` that classify a
              finding.

              Valid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual
              Behaviors | Sensitive Data Identifications

              - *(string) --*

            - **FirstObservedAt** *(string) --*

              An ISO8601-formatted timestamp that indicates when the security-findings provider first
              observed the potential security issue that a finding captured.

            - **LastObservedAt** *(string) --*

              An ISO8601-formatted timestamp that indicates when the security-findings provider most
              recently observed the potential security issue that a finding captured.

            - **CreatedAt** *(string) --* **[REQUIRED]**

              An ISO8601-formatted timestamp that indicates when the security-findings provider created the
              potential security issue that a finding captured.

            - **UpdatedAt** *(string) --* **[REQUIRED]**

              An ISO8601-formatted timestamp that indicates when the security-findings provider last
              updated the finding record.

            - **Severity** *(dict) --* **[REQUIRED]**

              A finding's severity.

              - **Product** *(float) --*

                The native severity as defined by the AWS service or integrated partner product that
                generated the finding.

              - **Normalized** *(integer) --* **[REQUIRED]**

                The normalized severity of a finding.

            - **Confidence** *(integer) --*

              A finding's confidence. Confidence is defined as the likelihood that a finding accurately
              identifies the behavior or issue that it was intended to identify. Confidence is scored on a
              0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100
              percent confidence.

            - **Criticality** *(integer) --*

              The level of importance assigned to the resources associated with the finding. A score of 0
              means that the underlying resources have no criticality, and a score of 100 is reserved for
              the most critical resources.

            - **Title** *(string) --* **[REQUIRED]**

              A finding's title.

              .. note::

                In this release, ``Title`` is a required property.

            - **Description** *(string) --* **[REQUIRED]**

              A finding's description.

              .. note::

                In this release, ``Description`` is a required property.

            - **Remediation** *(dict) --*

              A data type that describes the remediation options for a finding.

              - **Recommendation** *(dict) --*

                A recommendation on the steps to take to remediate the issue identified by a finding.

                - **Text** *(string) --*

                  Describes the recommended steps to take to remediate an issue identified in a finding.

                - **Url** *(string) --*

                  A URL to a page or site that contains information about how to remediate a finding.

            - **SourceUrl** *(string) --*

              A URL that links to a page about the current finding in the security-findings provider's
              solution.

            - **ProductFields** *(dict) --*

              A data type where security-findings providers can include additional solution-specific
              details that aren't part of the defined ``AwsSecurityFinding`` format.

              - *(string) --*

                - *(string) --*

            - **UserDefinedFields** *(dict) --*

              A list of name/value string pairs associated with the finding. These are custom, user-defined
              fields added to a finding.

              - *(string) --*

                - *(string) --*

            - **Malware** *(list) --*

              A list of malware related to a finding.

              - *(dict) --*

                A list of malware related to a finding.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the malware that was observed.

                - **Type** *(string) --*

                  The type of the malware that was observed.

                - **Path** *(string) --*

                  The file system path of the malware that was observed.

                - **State** *(string) --*

                  The state of the malware that was observed.

            - **Network** *(dict) --*

              The details of network-related information about a finding.

              - **Direction** *(string) --*

                The direction of network traffic associated with a finding.

              - **Protocol** *(string) --*

                The protocol of network-related information about a finding.

              - **SourceIpV4** *(string) --*

                The source IPv4 address of network-related information about a finding.

              - **SourceIpV6** *(string) --*

                The source IPv6 address of network-related information about a finding.

              - **SourcePort** *(integer) --*

                The source port of network-related information about a finding.

              - **SourceDomain** *(string) --*

                The source domain of network-related information about a finding.

              - **SourceMac** *(string) --*

                The source media access control (MAC) address of network-related information about a
                finding.

              - **DestinationIpV4** *(string) --*

                The destination IPv4 address of network-related information about a finding.

              - **DestinationIpV6** *(string) --*

                The destination IPv6 address of network-related information about a finding.

              - **DestinationPort** *(integer) --*

                The destination port of network-related information about a finding.

              - **DestinationDomain** *(string) --*

                The destination domain of network-related information about a finding.

            - **Process** *(dict) --*

              The details of process-related information about a finding.

              - **Name** *(string) --*

                The name of the process.

              - **Path** *(string) --*

                The path to the process executable.

              - **Pid** *(integer) --*

                The process ID.

              - **ParentPid** *(integer) --*

                The parent process ID.

              - **LaunchedAt** *(string) --*

                The date/time that the process was launched.

              - **TerminatedAt** *(string) --*

                The date and time when the process was terminated.

            - **ThreatIntelIndicators** *(list) --*

              Threat intel details related to a finding.

              - *(dict) --*

                Details about the threat intel related to a finding.

                - **Type** *(string) --*

                  The type of a threat intel indicator.

                - **Value** *(string) --*

                  The value of a threat intel indicator.

                - **Category** *(string) --*

                  The category of a threat intel indicator.

                - **LastObservedAt** *(string) --*

                  The date and time when the most recent instance of a threat intel indicator was observed.

                - **Source** *(string) --*

                  The source of the threat intel indicator.

                - **SourceUrl** *(string) --*

                  The URL to the page or site where you can get more information about the threat intel
                  indicator.

            - **Resources** *(list) --* **[REQUIRED]**

              A set of resource data types that describe the resources that the finding refers to.

              - *(dict) --*

                A resource related to a finding.

                - **Type** *(string) --* **[REQUIRED]**

                  The type of the resource that details are provided for.

                - **Id** *(string) --* **[REQUIRED]**

                  The canonical identifier for the given resource type.

                - **Partition** *(string) --*

                  The canonical AWS partition name that the Region is assigned to.

                - **Region** *(string) --*

                  The canonical AWS external Region name where this resource is located.

                - **Tags** *(dict) --*

                  A list of AWS tags associated with a resource at the time the finding was processed.

                  - *(string) --*

                    - *(string) --*

                - **Details** *(dict) --*

                  Additional details about the resource related to a finding.

                  - **AwsEc2Instance** *(dict) --*

                    Details about an Amazon EC2 instance related to a finding.

                    - **Type** *(string) --*

                      The instance type of the instance.

                    - **ImageId** *(string) --*

                      The Amazon Machine Image (AMI) ID of the instance.

                    - **IpV4Addresses** *(list) --*

                      The IPv4 addresses associated with the instance.

                      - *(string) --*

                    - **IpV6Addresses** *(list) --*

                      The IPv6 addresses associated with the instance.

                      - *(string) --*

                    - **KeyName** *(string) --*

                      The key name associated with the instance.

                    - **IamInstanceProfileArn** *(string) --*

                      The IAM profile ARN of the instance.

                    - **VpcId** *(string) --*

                      The identifier of the VPC that the instance was launched in.

                    - **SubnetId** *(string) --*

                      The identifier of the subnet that the instance was launched in.

                    - **LaunchedAt** *(string) --*

                      The date/time the instance was launched.

                  - **AwsS3Bucket** *(dict) --*

                    Details about an Amazon S3 Bucket related to a finding.

                    - **OwnerId** *(string) --*

                      The canonical user ID of the owner of the S3 bucket.

                    - **OwnerName** *(string) --*

                      The display name of the owner of the S3 bucket.

                  - **AwsIamAccessKey** *(dict) --*

                    Details about an IAM access key related to a finding.

                    - **UserName** *(string) --*

                      The user associated with the IAM access key related to a finding.

                    - **Status** *(string) --*

                      The status of the IAM access key related to a finding.

                    - **CreatedAt** *(string) --*

                      The creation date/time of the IAM access key related to a finding.

                  - **Container** *(dict) --*

                    Details about a container resource related to a finding.

                    - **Name** *(string) --*

                      The name of the container related to a finding.

                    - **ImageId** *(string) --*

                      The identifier of the image related to a finding.

                    - **ImageName** *(string) --*

                      The name of the image related to a finding.

                    - **LaunchedAt** *(string) --*

                      The date and time when the container started.

                  - **Other** *(dict) --*

                    Details about a resource that doesn't have a specific type defined.

                    - *(string) --*

                      - *(string) --*

            - **Compliance** *(dict) --*

              This data type is exclusive to findings that are generated as the result of a check run
              against a specific rule in a supported standard (for example, CIS AWS Foundations). Contains
              compliance-related finding details.

              - **Status** *(string) --*

                The result of a compliance check.

            - **VerificationState** *(string) --*

              Indicates the veracity of a finding.

            - **WorkflowState** *(string) --*

              The workflow state of a finding.

            - **RecordState** *(string) --*

              The record state of a finding.

            - **RelatedFindings** *(list) --*

              A list of related findings.

              - *(dict) --*

                Details about a related finding.

                - **ProductArn** *(string) --* **[REQUIRED]**

                  The ARN of the product that generated a related finding.

                - **Id** *(string) --* **[REQUIRED]**

                  The product-generated identifier for a related finding.

            - **Note** *(dict) --*

              A user-defined note added to a finding.

              - **Text** *(string) --* **[REQUIRED]**

                The text of a note.

              - **UpdatedBy** *(string) --* **[REQUIRED]**

                The principal that created a note.

              - **UpdatedAt** *(string) --* **[REQUIRED]**

                The timestamp of when the note was updated.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FailedCount': 123,
                'SuccessCount': 123,
                'FailedFindings': [
                    {
                        'Id': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **FailedCount** *(integer) --*

              The number of findings that failed to import.

            - **SuccessCount** *(integer) --*

              The number of findings that were successfully imported.

            - **FailedFindings** *(list) --*

              The list of the findings that failed to import.

              - *(dict) --*

                Includes details of the list of the findings that can't be imported.

                - **Id** *(string) --*

                  The ID of the error made during the ``BatchImportFindings`` operation.

                - **ErrorCode** *(string) --*

                  The code of the error made during the ``BatchImportFindings`` operation.

                - **ErrorMessage** *(string) --*

                  The message of the error made during the ``BatchImportFindings`` operation.

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
    def create_action_target(
        self, Name: str, Description: str, Id: str
    ) -> ClientCreateActionTargetResponseTypeDef:
        """
        Creates a custom action target in Security Hub. You can use custom actions on findings and insights
        in Security Hub to trigger target actions in Amazon CloudWatch Events.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/CreateActionTarget>`_

        **Request Syntax**
        ::

          response = client.create_action_target(
              Name='string',
              Description='string',
              Id='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the custom action target.

        :type Description: string
        :param Description: **[REQUIRED]**

          The description for the custom action target.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID for the custom action target.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ActionTargetArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ActionTargetArn** *(string) --*

              The ARN for the custom action target.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_insight(
        self,
        Name: str,
        Filters: ClientCreateInsightFiltersTypeDef,
        GroupByAttribute: str,
    ) -> ClientCreateInsightResponseTypeDef:
        """
        Creates a custom insight in Security Hub. An insight is a consolidation of findings that relate to
        a security issue that requires attention or remediation. Use the ``GroupByAttribute`` to group the
        related findings in the insight.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/CreateInsight>`_

        **Request Syntax**
        ::

          response = client.create_insight(
              Name='string',
              Filters={
                  'ProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'AwsAccountId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Id': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'GeneratorId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Type': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'FirstObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'LastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'CreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'UpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'SeverityProduct': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityNormalized': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityLabel': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Confidence': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Criticality': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Title': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Description': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RecommendationText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'SourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProductFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ProductName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'CompanyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'UserDefinedFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'MalwareName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwareType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwarePath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwareState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkDirection': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkProtocol': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourceIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourcePort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkSourceDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceMac': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkDestinationIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationPort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkDestinationDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessPath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessParentPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ProcessTerminatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorValue': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorCategory': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorLastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorSource': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorSourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourcePartition': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceRegion': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ResourceAwsEc2InstanceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV4Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV6Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceKeyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceVpcId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceSubnetId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceAwsS3BucketOwnerId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsS3BucketOwnerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyUserName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyCreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceContainerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceDetailsOther': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ComplianceStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'VerificationState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'WorkflowState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RecordState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NoteText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NoteUpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'NoteUpdatedBy': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Keyword': [
                      {
                          'Value': 'string'
                      },
                  ]
              },
              GroupByAttribute='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the custom insight to create.

        :type Filters: dict
        :param Filters: **[REQUIRED]**

          One or more attributes used to filter the findings included in the insight. Only findings that
          match the criteria defined in the filters are included in the insight.

          - **ProductArn** *(list) --*

            The ARN generated by Security Hub that uniquely identifies a third-party company (security
            findings provider) after this provider's product (solution that generates findings) is
            registered with Security Hub.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **AwsAccountId** *(list) --*

            The AWS account ID that a finding is generated in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Id** *(list) --*

            The security findings provider-specific identifier for a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **GeneratorId** *(list) --*

            The identifier for the solution-specific component (a discrete unit of logic) that generated a
            finding. In various security-findings providers' solutions, this generator can be called a
            rule, a check, a detector, a plug-in, etc.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Type** *(list) --*

            A finding type in the format of ``namespace/category/classifier`` that classifies a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **FirstObservedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider first
            observed the potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **LastObservedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider most recently
            observed the potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **CreatedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider captured the
            potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **UpdatedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider last updated
            the finding record.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **SeverityProduct** *(list) --*

            The native severity as defined by the security-findings provider's solution that generated the
            finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **SeverityNormalized** *(list) --*

            The normalized severity of a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **SeverityLabel** *(list) --*

            The label of a finding's severity.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Confidence** *(list) --*

            A finding's confidence. Confidence is defined as the likelihood that a finding accurately
            identifies the behavior or issue that it was intended to identify. Confidence is scored on a
            0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100
            percent confidence.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **Criticality** *(list) --*

            The level of importance assigned to the resources associated with the finding. A score of 0
            means that the underlying resources have no criticality, and a score of 100 is reserved for the
            most critical resources.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **Title** *(list) --*

            A finding's title.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Description** *(list) --*

            A finding's description.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RecommendationText** *(list) --*

            The recommendation of what to do about the issue described in a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **SourceUrl** *(list) --*

            A URL that links to a page about the current finding in the security-findings provider's
            solution.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProductFields** *(list) --*

            A data type where security-findings providers can include additional solution-specific details
            that aren't part of the defined ``AwsSecurityFinding`` format.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ProductName** *(list) --*

            The name of the solution (product) that generates findings.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **CompanyName** *(list) --*

            The name of the findings provider (company) that owns the solution (product) that generates
            findings.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **UserDefinedFields** *(list) --*

            A list of name/value string pairs associated with the finding. These are custom, user-defined
            fields added to a finding.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **MalwareName** *(list) --*

            The name of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwareType** *(list) --*

            The type of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwarePath** *(list) --*

            The filesystem path of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwareState** *(list) --*

            The state of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkDirection** *(list) --*

            Indicates the direction of network traffic associated with a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkProtocol** *(list) --*

            The protocol of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkSourceIpV4** *(list) --*

            The source IPv4 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkSourceIpV6** *(list) --*

            The source IPv6 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkSourcePort** *(list) --*

            The source port of network-related information about a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **NetworkSourceDomain** *(list) --*

            The source domain of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkSourceMac** *(list) --*

            The source media access control (MAC) address of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkDestinationIpV4** *(list) --*

            The destination IPv4 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkDestinationIpV6** *(list) --*

            The destination IPv6 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkDestinationPort** *(list) --*

            The destination port of network-related information about a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **NetworkDestinationDomain** *(list) --*

            The destination domain of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessName** *(list) --*

            The name of the process.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessPath** *(list) --*

            The path to the process executable.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessPid** *(list) --*

            The process ID.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **ProcessParentPid** *(list) --*

            The parent process ID.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **ProcessLaunchedAt** *(list) --*

            The date/time that the process was launched.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ProcessTerminatedAt** *(list) --*

            The date/time that the process was terminated.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ThreatIntelIndicatorType** *(list) --*

            The type of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorValue** *(list) --*

            The value of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorCategory** *(list) --*

            The category of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorLastObservedAt** *(list) --*

            The date/time of the last observation of a threat intel indicator.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ThreatIntelIndicatorSource** *(list) --*

            The source of the threat intel.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorSourceUrl** *(list) --*

            The URL for more details from the source of the threat intel.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceType** *(list) --*

            Specifies the type of the resource that details are provided for.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceId** *(list) --*

            The canonical identifier for the given resource type.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourcePartition** *(list) --*

            The canonical AWS partition name that the Region is assigned to.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceRegion** *(list) --*

            The canonical AWS external Region name where this resource is located.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceTags** *(list) --*

            A list of AWS tags associated with a resource at the time the finding was processed.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ResourceAwsEc2InstanceType** *(list) --*

            The instance type of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceImageId** *(list) --*

            The Amazon Machine Image (AMI) ID of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*

            The IPv4 addresses associated with the instance.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*

            The IPv6 addresses associated with the instance.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **ResourceAwsEc2InstanceKeyName** *(list) --*

            The key name associated with the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*

            The IAM profile ARN of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceVpcId** *(list) --*

            The identifier of the VPC that the instance was launched in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceSubnetId** *(list) --*

            The identifier of the subnet that the instance was launched in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*

            The date/time the instance was launched.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceAwsS3BucketOwnerId** *(list) --*

            The canonical user ID of the owner of the S3 bucket.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsS3BucketOwnerName** *(list) --*

            The display name of the owner of the S3 bucket.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyUserName** *(list) --*

            The user associated with the IAM access key related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyStatus** *(list) --*

            The status of the IAM access key related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*

            The creation date/time of the IAM access key related to a finding.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceContainerName** *(list) --*

            The name of the container related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerImageId** *(list) --*

            The identifier of the image related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerImageName** *(list) --*

            The name of the image related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerLaunchedAt** *(list) --*

            The date/time that the container was started.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceDetailsOther** *(list) --*

            The details of a resource that doesn't have a specific subfield for the resource type defined.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ComplianceStatus** *(list) --*

            Exclusive to findings that are generated as the result of a check run against a specific rule
            in a supported standard (for example, CIS AWS Foundations). Contains compliance-related finding
            details.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **VerificationState** *(list) --*

            The veracity of a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **WorkflowState** *(list) --*

            The workflow state of a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RecordState** *(list) --*

            The updated record state for the finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RelatedFindingsProductArn** *(list) --*

            The ARN of the solution that generated a related finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RelatedFindingsId** *(list) --*

            The solution-generated identifier for a related finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NoteText** *(list) --*

            The text of a note.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NoteUpdatedAt** *(list) --*

            The timestamp of when the note was updated.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **NoteUpdatedBy** *(list) --*

            The principal that created a note.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Keyword** *(list) --*

            A keyword for a finding.

            - *(dict) --*

              A keyword filter for querying findings.

              - **Value** *(string) --*

                A value for the keyword.

        :type GroupByAttribute: string
        :param GroupByAttribute: **[REQUIRED]**

          The attribute used as the aggregator to group related findings for the insight.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'InsightArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **InsightArn** *(string) --*

              The ARN of the insight created.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_members(
        self, AccountDetails: List[ClientCreateMembersAccountDetailsTypeDef] = None
    ) -> ClientCreateMembersResponseTypeDef:
        """
        Creates a member association in Security Hub between the specified accounts and the account used to
        make the request, which is the master account. To successfully create a member, you must use this
        action from an account that already has Security Hub enabled. You can use the  EnableSecurityHub to
        enable Security Hub.

        After you use ``CreateMembers`` to create member account associations in Security Hub, you need to
        use the  InviteMembers action, which invites the accounts to enable Security Hub and become member
        accounts in Security Hub. If the invitation is accepted by the account owner, the account becomes a
        member account in Security Hub, and a permission policy is added that permits the master account to
        view the findings generated in the member account. When Security Hub is enabled in the invited
        account, findings start being sent to both the member and master accounts.

        You can remove the association between the master and member accounts by using the
        DisassociateFromMasterAccount or  DisassociateMembers operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/CreateMembers>`_

        **Request Syntax**
        ::

          response = client.create_members(
              AccountDetails=[
                  {
                      'AccountId': 'string',
                      'Email': 'string'
                  },
              ]
          )
        :type AccountDetails: list
        :param AccountDetails:

          A list of account ID and email address pairs of the accounts to associate with the Security Hub
          master account.

          - *(dict) --*

            The details of an AWS account.

            - **AccountId** *(string) --*

              The ID of an AWS account.

            - **Email** *(string) --*

              The email of an AWS account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of account ID and email address pairs of the AWS accounts that weren't processed.

              - *(dict) --*

                Details about the account that wasn't processed.

                - **AccountId** *(string) --*

                  An AWS account ID of the account that wasn't be processed.

                - **ProcessingResult** *(string) --*

                  The reason that the account wasn't be processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decline_invitations(
        self, AccountIds: List[str]
    ) -> ClientDeclineInvitationsResponseTypeDef:
        """
        Declines invitations to become a member account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeclineInvitations>`_

        **Request Syntax**
        ::

          response = client.decline_invitations(
              AccountIds=[
                  'string',
              ]
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs that specify the accounts that invitations to Security Hub are declined
          from.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of account ID and email address pairs of the AWS accounts that weren't processed.

              - *(dict) --*

                Details about the account that wasn't processed.

                - **AccountId** *(string) --*

                  An AWS account ID of the account that wasn't be processed.

                - **ProcessingResult** *(string) --*

                  The reason that the account wasn't be processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_action_target(
        self, ActionTargetArn: str
    ) -> ClientDeleteActionTargetResponseTypeDef:
        """
        Deletes a custom action target from Security Hub. Deleting a custom action target doesn't affect
        any findings or insights that were already sent to Amazon CloudWatch Events using the custom action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeleteActionTarget>`_

        **Request Syntax**
        ::

          response = client.delete_action_target(
              ActionTargetArn='string'
          )
        :type ActionTargetArn: string
        :param ActionTargetArn: **[REQUIRED]**

          The ARN of the custom action target to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ActionTargetArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ActionTargetArn** *(string) --*

              The ARN of the custom action target that was deleted.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_insight(self, InsightArn: str) -> ClientDeleteInsightResponseTypeDef:
        """
        Deletes the insight specified by the ``InsightArn`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeleteInsight>`_

        **Request Syntax**
        ::

          response = client.delete_insight(
              InsightArn='string'
          )
        :type InsightArn: string
        :param InsightArn: **[REQUIRED]**

          The ARN of the insight to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'InsightArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **InsightArn** *(string) --*

              The ARN of the insight that was deleted.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_invitations(
        self, AccountIds: List[str]
    ) -> ClientDeleteInvitationsResponseTypeDef:
        """
        Deletes invitations received by the AWS account to become a member account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeleteInvitations>`_

        **Request Syntax**
        ::

          response = client.delete_invitations(
              AccountIds=[
                  'string',
              ]
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of the account IDs that sent the invitations to delete.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of account ID and email address pairs of the AWS accounts that invitations weren't
              deleted for.

              - *(dict) --*

                Details about the account that wasn't processed.

                - **AccountId** *(string) --*

                  An AWS account ID of the account that wasn't be processed.

                - **ProcessingResult** *(string) --*

                  The reason that the account wasn't be processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_members(
        self, AccountIds: List[str] = None
    ) -> ClientDeleteMembersResponseTypeDef:
        """
        Deletes the specified member accounts from Security Hub.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeleteMembers>`_

        **Request Syntax**
        ::

          response = client.delete_members(
              AccountIds=[
                  'string',
              ]
          )
        :type AccountIds: list
        :param AccountIds:

          A list of account IDs of the member accounts to delete.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of account ID and email address pairs of the AWS accounts that weren't deleted.

              - *(dict) --*

                Details about the account that wasn't processed.

                - **AccountId** *(string) --*

                  An AWS account ID of the account that wasn't be processed.

                - **ProcessingResult** *(string) --*

                  The reason that the account wasn't be processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_action_targets(
        self,
        ActionTargetArns: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeActionTargetsResponseTypeDef:
        """
        Returns a list of the custom action targets in Security Hub in your account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DescribeActionTargets>`_

        **Request Syntax**
        ::

          response = client.describe_action_targets(
              ActionTargetArns=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type ActionTargetArns: list
        :param ActionTargetArns:

          A list of custom action target ARNs for the custom action targets to retrieve.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          The token that is required for pagination.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ActionTargets': [
                    {
                        'ActionTargetArn': 'string',
                        'Name': 'string',
                        'Description': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ActionTargets** *(list) --*

              A list of ``ActionTarget`` objects. Each object includes the ``ActionTargetArn`` ,
              ``Description`` , and ``Name`` of a custom action target available in Security Hub.

              - *(dict) --*

                An ``ActionTarget`` object.

                - **ActionTargetArn** *(string) --*

                  The ARN for the target action.

                - **Name** *(string) --*

                  The name of the action target.

                - **Description** *(string) --*

                  The description of the target action.

            - **NextToken** *(string) --*

              The token that is required for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_hub(self, HubArn: str = None) -> ClientDescribeHubResponseTypeDef:
        """
        Returns details about the Hub resource in your account, including the ``HubArn`` and the time when
        you enabled Security Hub.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DescribeHub>`_

        **Request Syntax**
        ::

          response = client.describe_hub(
              HubArn='string'
          )
        :type HubArn: string
        :param HubArn:

          The ARN of the Hub resource to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HubArn': 'string',
                'SubscribedAt': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **HubArn** *(string) --*

              The ARN of the Hub resource retrieved.

            - **SubscribedAt** *(string) --*

              The date and time when Security Hub was enabled in the account.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_products(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeProductsResponseTypeDef:
        """
        Returns information about the products available that you can subscribe to and integrate with
        Security Hub to consolidate findings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DescribeProducts>`_

        **Request Syntax**
        ::

          response = client.describe_products(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          The token that is required for pagination.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Products': [
                    {
                        'ProductArn': 'string',
                        'ProductName': 'string',
                        'CompanyName': 'string',
                        'Description': 'string',
                        'Categories': [
                            'string',
                        ],
                        'MarketplaceUrl': 'string',
                        'ActivationUrl': 'string',
                        'ProductSubscriptionResourcePolicy': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Products** *(list) --*

              A list of products, including details for each product.

              - *(dict) --*

                Contains details about a product.

                - **ProductArn** *(string) --*

                  The ARN assigned to the product.

                - **ProductName** *(string) --*

                  The name of the product.

                - **CompanyName** *(string) --*

                  The name of the company that provides the product.

                - **Description** *(string) --*

                  A description of the product.

                - **Categories** *(list) --*

                  The categories assigned to the product.

                  - *(string) --*

                - **MarketplaceUrl** *(string) --*

                  The URL for the page that contains more information about the product.

                - **ActivationUrl** *(string) --*

                  The URL used to activate the product.

                - **ProductSubscriptionResourcePolicy** *(string) --*

                  The resource policy associated with the product.

            - **NextToken** *(string) --*

              The token that is required for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_import_findings_for_product(
        self, ProductSubscriptionArn: str
    ) -> Dict[str, Any]:
        """
        Disables the integration of the specified product with Security Hub. Findings from that product are
        no longer sent to Security Hub after the integration is disabled.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DisableImportFindingsForProduct>`_

        **Request Syntax**
        ::

          response = client.disable_import_findings_for_product(
              ProductSubscriptionArn='string'
          )
        :type ProductSubscriptionArn: string
        :param ProductSubscriptionArn: **[REQUIRED]**

          The ARN of the integrated product to disable the integration for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_security_hub(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        Disables Security Hub in your account only in the current Region. To disable Security Hub in all
        Regions, you must submit one request per Region where you have enabled Security Hub. When you
        disable Security Hub for a master account, it doesn't disable Security Hub for any associated
        member accounts.

        When you disable Security Hub, your existing findings and insights and any Security Hub
        configuration settings are deleted after 90 days and can't be recovered. Any standards that were
        enabled are disabled, and your master and member account associations are removed. If you want to
        save your existing findings, you must export them before you disable Security Hub.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DisableSecurityHub>`_

        **Request Syntax**
        ::

          response = client.disable_security_hub()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_from_master_account(
        self, *args: Any, **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Disassociates the current Security Hub member account from the associated master account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DisassociateFromMasterAccount>`_

        **Request Syntax**
        ::

          response = client.disassociate_from_master_account()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_members(self, AccountIds: List[str] = None) -> Dict[str, Any]:
        """
        Disassociates the specified member accounts from the associated master account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DisassociateMembers>`_

        **Request Syntax**
        ::

          response = client.disassociate_members(
              AccountIds=[
                  'string',
              ]
          )
        :type AccountIds: list
        :param AccountIds:

          The account IDs of the member accounts to disassociate from the master account.

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
    def enable_import_findings_for_product(
        self, ProductArn: str
    ) -> ClientEnableImportFindingsForProductResponseTypeDef:
        """
        Enables the integration of a partner product with Security Hub. Integrated products send findings
        to Security Hub. When you enable a product integration, a permission policy that grants permission
        for the product to send findings to Security Hub is applied.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/EnableImportFindingsForProduct>`_

        **Request Syntax**
        ::

          response = client.enable_import_findings_for_product(
              ProductArn='string'
          )
        :type ProductArn: string
        :param ProductArn: **[REQUIRED]**

          The ARN of the product to enable the integration for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProductSubscriptionArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ProductSubscriptionArn** *(string) --*

              The ARN of your subscription to the product to enable integrations for.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_security_hub(self, Tags: List[str] = None) -> Dict[str, Any]:
        """
        Enables Security Hub for your account in the current Region or the Region you specify in the
        request. When you enable Security Hub, you grant to Security Hub the permissions necessary to
        gather findings from AWS Config, Amazon GuardDuty, Amazon Inspector, and Amazon Macie. To learn
        more, see `Setting Up AWS Security Hub
        <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/EnableSecurityHub>`_

        **Request Syntax**
        ::

          response = client.enable_security_hub(
              Tags={
                  'string': 'string'
              }
          )
        :type Tags: dict
        :param Tags:

          The tags to add to the Hub resource when you enable Security Hub.

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
    def get_enabled_standards(
        self,
        StandardsSubscriptionArns: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetEnabledStandardsResponseTypeDef:
        """
        Returns a list of the standards that are currently enabled.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetEnabledStandards>`_

        **Request Syntax**
        ::

          response = client.get_enabled_standards(
              StandardsSubscriptionArns=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type StandardsSubscriptionArns: list
        :param StandardsSubscriptionArns:

          A list of the standards subscription ARNs for the standards to retrieve.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          Paginates results. On your first call to the ``GetEnabledStandards`` operation, set the value of
          this parameter to ``NULL`` . For subsequent calls to the operation, fill ``nextToken`` in the
          request with the value of ``nextToken`` from the previous response to continue listing data.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StandardsSubscriptions': [
                    {
                        'StandardsSubscriptionArn': 'string',
                        'StandardsArn': 'string',
                        'StandardsInput': {
                            'string': 'string'
                        },
                        'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **StandardsSubscriptions** *(list) --*

              A list of ``StandardsSubscriptions`` objects that include information about the enabled
              standards.

              - *(dict) --*

                A resource that represents your subscription to a supported standard.

                - **StandardsSubscriptionArn** *(string) --*

                  The ARN of a resource that represents your subscription to a supported standard.

                - **StandardsArn** *(string) --*

                  The ARN of a standard.

                  In this release, Security Hub supports only the CIS AWS Foundations standard, which uses
                  the following ARN:
                  ``arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0.``

                - **StandardsInput** *(dict) --*

                  A key-value pair of input for the standard.

                  - *(string) --*

                    - *(string) --*

                - **StandardsStatus** *(string) --*

                  The status of the standards subscription.

            - **NextToken** *(string) --*

              The token that is required for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_findings(
        self,
        Filters: ClientGetFindingsFiltersTypeDef = None,
        SortCriteria: List[ClientGetFindingsSortCriteriaTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetFindingsResponseTypeDef:
        """
        Returns a list of findings that match the specified criteria.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetFindings>`_

        **Request Syntax**
        ::

          response = client.get_findings(
              Filters={
                  'ProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'AwsAccountId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Id': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'GeneratorId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Type': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'FirstObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'LastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'CreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'UpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'SeverityProduct': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityNormalized': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityLabel': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Confidence': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Criticality': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Title': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Description': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RecommendationText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'SourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProductFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ProductName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'CompanyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'UserDefinedFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'MalwareName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwareType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwarePath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwareState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkDirection': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkProtocol': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourceIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourcePort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkSourceDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceMac': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkDestinationIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationPort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkDestinationDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessPath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessParentPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ProcessTerminatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorValue': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorCategory': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorLastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorSource': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorSourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourcePartition': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceRegion': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ResourceAwsEc2InstanceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV4Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV6Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceKeyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceVpcId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceSubnetId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceAwsS3BucketOwnerId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsS3BucketOwnerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyUserName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyCreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceContainerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceDetailsOther': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ComplianceStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'VerificationState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'WorkflowState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RecordState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NoteText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NoteUpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'NoteUpdatedBy': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Keyword': [
                      {
                          'Value': 'string'
                      },
                  ]
              },
              SortCriteria=[
                  {
                      'Field': 'string',
                      'SortOrder': 'asc'|'desc'
                  },
              ],
              NextToken='string',
              MaxResults=123
          )
        :type Filters: dict
        :param Filters:

          The findings attributes used to define a condition to filter the findings returned.

          - **ProductArn** *(list) --*

            The ARN generated by Security Hub that uniquely identifies a third-party company (security
            findings provider) after this provider's product (solution that generates findings) is
            registered with Security Hub.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **AwsAccountId** *(list) --*

            The AWS account ID that a finding is generated in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Id** *(list) --*

            The security findings provider-specific identifier for a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **GeneratorId** *(list) --*

            The identifier for the solution-specific component (a discrete unit of logic) that generated a
            finding. In various security-findings providers' solutions, this generator can be called a
            rule, a check, a detector, a plug-in, etc.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Type** *(list) --*

            A finding type in the format of ``namespace/category/classifier`` that classifies a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **FirstObservedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider first
            observed the potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **LastObservedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider most recently
            observed the potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **CreatedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider captured the
            potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **UpdatedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider last updated
            the finding record.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **SeverityProduct** *(list) --*

            The native severity as defined by the security-findings provider's solution that generated the
            finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **SeverityNormalized** *(list) --*

            The normalized severity of a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **SeverityLabel** *(list) --*

            The label of a finding's severity.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Confidence** *(list) --*

            A finding's confidence. Confidence is defined as the likelihood that a finding accurately
            identifies the behavior or issue that it was intended to identify. Confidence is scored on a
            0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100
            percent confidence.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **Criticality** *(list) --*

            The level of importance assigned to the resources associated with the finding. A score of 0
            means that the underlying resources have no criticality, and a score of 100 is reserved for the
            most critical resources.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **Title** *(list) --*

            A finding's title.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Description** *(list) --*

            A finding's description.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RecommendationText** *(list) --*

            The recommendation of what to do about the issue described in a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **SourceUrl** *(list) --*

            A URL that links to a page about the current finding in the security-findings provider's
            solution.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProductFields** *(list) --*

            A data type where security-findings providers can include additional solution-specific details
            that aren't part of the defined ``AwsSecurityFinding`` format.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ProductName** *(list) --*

            The name of the solution (product) that generates findings.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **CompanyName** *(list) --*

            The name of the findings provider (company) that owns the solution (product) that generates
            findings.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **UserDefinedFields** *(list) --*

            A list of name/value string pairs associated with the finding. These are custom, user-defined
            fields added to a finding.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **MalwareName** *(list) --*

            The name of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwareType** *(list) --*

            The type of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwarePath** *(list) --*

            The filesystem path of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwareState** *(list) --*

            The state of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkDirection** *(list) --*

            Indicates the direction of network traffic associated with a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkProtocol** *(list) --*

            The protocol of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkSourceIpV4** *(list) --*

            The source IPv4 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkSourceIpV6** *(list) --*

            The source IPv6 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkSourcePort** *(list) --*

            The source port of network-related information about a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **NetworkSourceDomain** *(list) --*

            The source domain of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkSourceMac** *(list) --*

            The source media access control (MAC) address of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkDestinationIpV4** *(list) --*

            The destination IPv4 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkDestinationIpV6** *(list) --*

            The destination IPv6 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkDestinationPort** *(list) --*

            The destination port of network-related information about a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **NetworkDestinationDomain** *(list) --*

            The destination domain of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessName** *(list) --*

            The name of the process.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessPath** *(list) --*

            The path to the process executable.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessPid** *(list) --*

            The process ID.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **ProcessParentPid** *(list) --*

            The parent process ID.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **ProcessLaunchedAt** *(list) --*

            The date/time that the process was launched.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ProcessTerminatedAt** *(list) --*

            The date/time that the process was terminated.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ThreatIntelIndicatorType** *(list) --*

            The type of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorValue** *(list) --*

            The value of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorCategory** *(list) --*

            The category of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorLastObservedAt** *(list) --*

            The date/time of the last observation of a threat intel indicator.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ThreatIntelIndicatorSource** *(list) --*

            The source of the threat intel.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorSourceUrl** *(list) --*

            The URL for more details from the source of the threat intel.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceType** *(list) --*

            Specifies the type of the resource that details are provided for.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceId** *(list) --*

            The canonical identifier for the given resource type.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourcePartition** *(list) --*

            The canonical AWS partition name that the Region is assigned to.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceRegion** *(list) --*

            The canonical AWS external Region name where this resource is located.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceTags** *(list) --*

            A list of AWS tags associated with a resource at the time the finding was processed.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ResourceAwsEc2InstanceType** *(list) --*

            The instance type of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceImageId** *(list) --*

            The Amazon Machine Image (AMI) ID of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*

            The IPv4 addresses associated with the instance.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*

            The IPv6 addresses associated with the instance.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **ResourceAwsEc2InstanceKeyName** *(list) --*

            The key name associated with the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*

            The IAM profile ARN of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceVpcId** *(list) --*

            The identifier of the VPC that the instance was launched in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceSubnetId** *(list) --*

            The identifier of the subnet that the instance was launched in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*

            The date/time the instance was launched.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceAwsS3BucketOwnerId** *(list) --*

            The canonical user ID of the owner of the S3 bucket.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsS3BucketOwnerName** *(list) --*

            The display name of the owner of the S3 bucket.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyUserName** *(list) --*

            The user associated with the IAM access key related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyStatus** *(list) --*

            The status of the IAM access key related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*

            The creation date/time of the IAM access key related to a finding.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceContainerName** *(list) --*

            The name of the container related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerImageId** *(list) --*

            The identifier of the image related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerImageName** *(list) --*

            The name of the image related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerLaunchedAt** *(list) --*

            The date/time that the container was started.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceDetailsOther** *(list) --*

            The details of a resource that doesn't have a specific subfield for the resource type defined.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ComplianceStatus** *(list) --*

            Exclusive to findings that are generated as the result of a check run against a specific rule
            in a supported standard (for example, CIS AWS Foundations). Contains compliance-related finding
            details.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **VerificationState** *(list) --*

            The veracity of a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **WorkflowState** *(list) --*

            The workflow state of a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RecordState** *(list) --*

            The updated record state for the finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RelatedFindingsProductArn** *(list) --*

            The ARN of the solution that generated a related finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RelatedFindingsId** *(list) --*

            The solution-generated identifier for a related finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NoteText** *(list) --*

            The text of a note.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NoteUpdatedAt** *(list) --*

            The timestamp of when the note was updated.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **NoteUpdatedBy** *(list) --*

            The principal that created a note.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Keyword** *(list) --*

            A keyword for a finding.

            - *(dict) --*

              A keyword filter for querying findings.

              - **Value** *(string) --*

                A value for the keyword.

        :type SortCriteria: list
        :param SortCriteria:

          Findings attributes used to sort the list of findings returned.

          - *(dict) --*

            A collection of finding attributes used to sort findings.

            - **Field** *(string) --*

              The finding attribute used to sort findings.

            - **SortOrder** *(string) --*

              The order used to sort findings.

        :type NextToken: string
        :param NextToken:

          Paginates results. On your first call to the ``GetFindings`` operation, set the value of this
          parameter to ``NULL`` . For subsequent calls to the operation, fill ``nextToken`` in the request
          with the value of ``nextToken`` from the previous response to continue listing data.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of findings to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Findings': [
                    {
                        'SchemaVersion': 'string',
                        'Id': 'string',
                        'ProductArn': 'string',
                        'GeneratorId': 'string',
                        'AwsAccountId': 'string',
                        'Types': [
                            'string',
                        ],
                        'FirstObservedAt': 'string',
                        'LastObservedAt': 'string',
                        'CreatedAt': 'string',
                        'UpdatedAt': 'string',
                        'Severity': {
                            'Product': 123.0,
                            'Normalized': 123
                        },
                        'Confidence': 123,
                        'Criticality': 123,
                        'Title': 'string',
                        'Description': 'string',
                        'Remediation': {
                            'Recommendation': {
                                'Text': 'string',
                                'Url': 'string'
                            }
                        },
                        'SourceUrl': 'string',
                        'ProductFields': {
                            'string': 'string'
                        },
                        'UserDefinedFields': {
                            'string': 'string'
                        },
                        'Malware': [
                            {
                                'Name': 'string',
                                'Type':
                                'ADWARE'|'BLENDED_THREAT'|'BOTNET_AGENT'|'COIN_MINER'|'EXPLOIT_KIT'
                                |'KEYLOGGER'|'MACRO'|'POTENTIALLY_UNWANTED'|'SPYWARE'|'RANSOMWARE'
                                |'REMOTE_ACCESS'|'ROOTKIT'|'TROJAN'|'VIRUS'|'WORM',
                                'Path': 'string',
                                'State': 'OBSERVED'|'REMOVAL_FAILED'|'REMOVED'
                            },
                        ],
                        'Network': {
                            'Direction': 'IN'|'OUT',
                            'Protocol': 'string',
                            'SourceIpV4': 'string',
                            'SourceIpV6': 'string',
                            'SourcePort': 123,
                            'SourceDomain': 'string',
                            'SourceMac': 'string',
                            'DestinationIpV4': 'string',
                            'DestinationIpV6': 'string',
                            'DestinationPort': 123,
                            'DestinationDomain': 'string'
                        },
                        'Process': {
                            'Name': 'string',
                            'Path': 'string',
                            'Pid': 123,
                            'ParentPid': 123,
                            'LaunchedAt': 'string',
                            'TerminatedAt': 'string'
                        },
                        'ThreatIntelIndicators': [
                            {
                                'Type':
                                'DOMAIN'|'EMAIL_ADDRESS'|'HASH_MD5'|'HASH_SHA1'|'HASH_SHA256'|'HASH_SHA512'
                                |'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MUTEX'|'PROCESS'|'URL',
                                'Value': 'string',
                                'Category':
                                'BACKDOOR'|'CARD_STEALER'|'COMMAND_AND_CONTROL'|'DROP_SITE'|'EXPLOIT_SITE'
                                |'KEYLOGGER',
                                'LastObservedAt': 'string',
                                'Source': 'string',
                                'SourceUrl': 'string'
                            },
                        ],
                        'Resources': [
                            {
                                'Type': 'string',
                                'Id': 'string',
                                'Partition': 'aws'|'aws-cn'|'aws-us-gov',
                                'Region': 'string',
                                'Tags': {
                                    'string': 'string'
                                },
                                'Details': {
                                    'AwsEc2Instance': {
                                        'Type': 'string',
                                        'ImageId': 'string',
                                        'IpV4Addresses': [
                                            'string',
                                        ],
                                        'IpV6Addresses': [
                                            'string',
                                        ],
                                        'KeyName': 'string',
                                        'IamInstanceProfileArn': 'string',
                                        'VpcId': 'string',
                                        'SubnetId': 'string',
                                        'LaunchedAt': 'string'
                                    },
                                    'AwsS3Bucket': {
                                        'OwnerId': 'string',
                                        'OwnerName': 'string'
                                    },
                                    'AwsIamAccessKey': {
                                        'UserName': 'string',
                                        'Status': 'Active'|'Inactive',
                                        'CreatedAt': 'string'
                                    },
                                    'Container': {
                                        'Name': 'string',
                                        'ImageId': 'string',
                                        'ImageName': 'string',
                                        'LaunchedAt': 'string'
                                    },
                                    'Other': {
                                        'string': 'string'
                                    }
                                }
                            },
                        ],
                        'Compliance': {
                            'Status': 'PASSED'|'WARNING'|'FAILED'|'NOT_AVAILABLE'
                        },
                        'VerificationState': 'UNKNOWN'|'TRUE_POSITIVE'|'FALSE_POSITIVE'|'BENIGN_POSITIVE',
                        'WorkflowState': 'NEW'|'ASSIGNED'|'IN_PROGRESS'|'DEFERRED'|'RESOLVED',
                        'RecordState': 'ACTIVE'|'ARCHIVED',
                        'RelatedFindings': [
                            {
                                'ProductArn': 'string',
                                'Id': 'string'
                            },
                        ],
                        'Note': {
                            'Text': 'string',
                            'UpdatedBy': 'string',
                            'UpdatedAt': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Findings** *(list) --*

              The findings that matched the filters specified in the request.

              - *(dict) --*

                Provides consistent format for the contents of the Security Hub-aggregated findings.
                ``AwsSecurityFinding`` format enables you to share findings between AWS security services
                and third-party solutions, and compliance checks.

                .. note::

                  A finding is a potential security issue generated either by AWS services (Amazon
                  GuardDuty, Amazon Inspector, and Amazon Macie) or by the integrated third-party solutions
                  and compliance checks.

                - **SchemaVersion** *(string) --*

                  The schema version that a finding is formatted for.

                - **Id** *(string) --*

                  The security findings provider-specific identifier for a finding.

                - **ProductArn** *(string) --*

                  The ARN generated by Security Hub that uniquely identifies a third-party company
                  (security-findings provider) after this provider's product (solution that generates
                  findings) is registered with Security Hub.

                - **GeneratorId** *(string) --*

                  The identifier for the solution-specific component (a discrete unit of logic) that
                  generated a finding. In various security-findings providers' solutions, this generator
                  can be called a rule, a check, a detector, a plug-in, etc.

                - **AwsAccountId** *(string) --*

                  The AWS account ID that a finding is generated in.

                - **Types** *(list) --*

                  One or more finding types in the format of ``namespace/category/classifier`` that
                  classify a finding.

                  Valid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual
                  Behaviors | Sensitive Data Identifications

                  - *(string) --*

                - **FirstObservedAt** *(string) --*

                  An ISO8601-formatted timestamp that indicates when the security-findings provider first
                  observed the potential security issue that a finding captured.

                - **LastObservedAt** *(string) --*

                  An ISO8601-formatted timestamp that indicates when the security-findings provider most
                  recently observed the potential security issue that a finding captured.

                - **CreatedAt** *(string) --*

                  An ISO8601-formatted timestamp that indicates when the security-findings provider created
                  the potential security issue that a finding captured.

                - **UpdatedAt** *(string) --*

                  An ISO8601-formatted timestamp that indicates when the security-findings provider last
                  updated the finding record.

                - **Severity** *(dict) --*

                  A finding's severity.

                  - **Product** *(float) --*

                    The native severity as defined by the AWS service or integrated partner product that
                    generated the finding.

                  - **Normalized** *(integer) --*

                    The normalized severity of a finding.

                - **Confidence** *(integer) --*

                  A finding's confidence. Confidence is defined as the likelihood that a finding accurately
                  identifies the behavior or issue that it was intended to identify. Confidence is scored
                  on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means
                  100 percent confidence.

                - **Criticality** *(integer) --*

                  The level of importance assigned to the resources associated with the finding. A score of
                  0 means that the underlying resources have no criticality, and a score of 100 is reserved
                  for the most critical resources.

                - **Title** *(string) --*

                  A finding's title.

                  .. note::

                    In this release, ``Title`` is a required property.

                - **Description** *(string) --*

                  A finding's description.

                  .. note::

                    In this release, ``Description`` is a required property.

                - **Remediation** *(dict) --*

                  A data type that describes the remediation options for a finding.

                  - **Recommendation** *(dict) --*

                    A recommendation on the steps to take to remediate the issue identified by a finding.

                    - **Text** *(string) --*

                      Describes the recommended steps to take to remediate an issue identified in a finding.

                    - **Url** *(string) --*

                      A URL to a page or site that contains information about how to remediate a finding.

                - **SourceUrl** *(string) --*

                  A URL that links to a page about the current finding in the security-findings provider's
                  solution.

                - **ProductFields** *(dict) --*

                  A data type where security-findings providers can include additional solution-specific
                  details that aren't part of the defined ``AwsSecurityFinding`` format.

                  - *(string) --*

                    - *(string) --*

                - **UserDefinedFields** *(dict) --*

                  A list of name/value string pairs associated with the finding. These are custom,
                  user-defined fields added to a finding.

                  - *(string) --*

                    - *(string) --*

                - **Malware** *(list) --*

                  A list of malware related to a finding.

                  - *(dict) --*

                    A list of malware related to a finding.

                    - **Name** *(string) --*

                      The name of the malware that was observed.

                    - **Type** *(string) --*

                      The type of the malware that was observed.

                    - **Path** *(string) --*

                      The file system path of the malware that was observed.

                    - **State** *(string) --*

                      The state of the malware that was observed.

                - **Network** *(dict) --*

                  The details of network-related information about a finding.

                  - **Direction** *(string) --*

                    The direction of network traffic associated with a finding.

                  - **Protocol** *(string) --*

                    The protocol of network-related information about a finding.

                  - **SourceIpV4** *(string) --*

                    The source IPv4 address of network-related information about a finding.

                  - **SourceIpV6** *(string) --*

                    The source IPv6 address of network-related information about a finding.

                  - **SourcePort** *(integer) --*

                    The source port of network-related information about a finding.

                  - **SourceDomain** *(string) --*

                    The source domain of network-related information about a finding.

                  - **SourceMac** *(string) --*

                    The source media access control (MAC) address of network-related information about a
                    finding.

                  - **DestinationIpV4** *(string) --*

                    The destination IPv4 address of network-related information about a finding.

                  - **DestinationIpV6** *(string) --*

                    The destination IPv6 address of network-related information about a finding.

                  - **DestinationPort** *(integer) --*

                    The destination port of network-related information about a finding.

                  - **DestinationDomain** *(string) --*

                    The destination domain of network-related information about a finding.

                - **Process** *(dict) --*

                  The details of process-related information about a finding.

                  - **Name** *(string) --*

                    The name of the process.

                  - **Path** *(string) --*

                    The path to the process executable.

                  - **Pid** *(integer) --*

                    The process ID.

                  - **ParentPid** *(integer) --*

                    The parent process ID.

                  - **LaunchedAt** *(string) --*

                    The date/time that the process was launched.

                  - **TerminatedAt** *(string) --*

                    The date and time when the process was terminated.

                - **ThreatIntelIndicators** *(list) --*

                  Threat intel details related to a finding.

                  - *(dict) --*

                    Details about the threat intel related to a finding.

                    - **Type** *(string) --*

                      The type of a threat intel indicator.

                    - **Value** *(string) --*

                      The value of a threat intel indicator.

                    - **Category** *(string) --*

                      The category of a threat intel indicator.

                    - **LastObservedAt** *(string) --*

                      The date and time when the most recent instance of a threat intel indicator was
                      observed.

                    - **Source** *(string) --*

                      The source of the threat intel indicator.

                    - **SourceUrl** *(string) --*

                      The URL to the page or site where you can get more information about the threat intel
                      indicator.

                - **Resources** *(list) --*

                  A set of resource data types that describe the resources that the finding refers to.

                  - *(dict) --*

                    A resource related to a finding.

                    - **Type** *(string) --*

                      The type of the resource that details are provided for.

                    - **Id** *(string) --*

                      The canonical identifier for the given resource type.

                    - **Partition** *(string) --*

                      The canonical AWS partition name that the Region is assigned to.

                    - **Region** *(string) --*

                      The canonical AWS external Region name where this resource is located.

                    - **Tags** *(dict) --*

                      A list of AWS tags associated with a resource at the time the finding was processed.

                      - *(string) --*

                        - *(string) --*

                    - **Details** *(dict) --*

                      Additional details about the resource related to a finding.

                      - **AwsEc2Instance** *(dict) --*

                        Details about an Amazon EC2 instance related to a finding.

                        - **Type** *(string) --*

                          The instance type of the instance.

                        - **ImageId** *(string) --*

                          The Amazon Machine Image (AMI) ID of the instance.

                        - **IpV4Addresses** *(list) --*

                          The IPv4 addresses associated with the instance.

                          - *(string) --*

                        - **IpV6Addresses** *(list) --*

                          The IPv6 addresses associated with the instance.

                          - *(string) --*

                        - **KeyName** *(string) --*

                          The key name associated with the instance.

                        - **IamInstanceProfileArn** *(string) --*

                          The IAM profile ARN of the instance.

                        - **VpcId** *(string) --*

                          The identifier of the VPC that the instance was launched in.

                        - **SubnetId** *(string) --*

                          The identifier of the subnet that the instance was launched in.

                        - **LaunchedAt** *(string) --*

                          The date/time the instance was launched.

                      - **AwsS3Bucket** *(dict) --*

                        Details about an Amazon S3 Bucket related to a finding.

                        - **OwnerId** *(string) --*

                          The canonical user ID of the owner of the S3 bucket.

                        - **OwnerName** *(string) --*

                          The display name of the owner of the S3 bucket.

                      - **AwsIamAccessKey** *(dict) --*

                        Details about an IAM access key related to a finding.

                        - **UserName** *(string) --*

                          The user associated with the IAM access key related to a finding.

                        - **Status** *(string) --*

                          The status of the IAM access key related to a finding.

                        - **CreatedAt** *(string) --*

                          The creation date/time of the IAM access key related to a finding.

                      - **Container** *(dict) --*

                        Details about a container resource related to a finding.

                        - **Name** *(string) --*

                          The name of the container related to a finding.

                        - **ImageId** *(string) --*

                          The identifier of the image related to a finding.

                        - **ImageName** *(string) --*

                          The name of the image related to a finding.

                        - **LaunchedAt** *(string) --*

                          The date and time when the container started.

                      - **Other** *(dict) --*

                        Details about a resource that doesn't have a specific type defined.

                        - *(string) --*

                          - *(string) --*

                - **Compliance** *(dict) --*

                  This data type is exclusive to findings that are generated as the result of a check run
                  against a specific rule in a supported standard (for example, CIS AWS Foundations).
                  Contains compliance-related finding details.

                  - **Status** *(string) --*

                    The result of a compliance check.

                - **VerificationState** *(string) --*

                  Indicates the veracity of a finding.

                - **WorkflowState** *(string) --*

                  The workflow state of a finding.

                - **RecordState** *(string) --*

                  The record state of a finding.

                - **RelatedFindings** *(list) --*

                  A list of related findings.

                  - *(dict) --*

                    Details about a related finding.

                    - **ProductArn** *(string) --*

                      The ARN of the product that generated a related finding.

                    - **Id** *(string) --*

                      The product-generated identifier for a related finding.

                - **Note** *(dict) --*

                  A user-defined note added to a finding.

                  - **Text** *(string) --*

                    The text of a note.

                  - **UpdatedBy** *(string) --*

                    The principal that created a note.

                  - **UpdatedAt** *(string) --*

                    The timestamp of when the note was updated.

            - **NextToken** *(string) --*

              The token that is required for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_insight_results(
        self, InsightArn: str
    ) -> ClientGetInsightResultsResponseTypeDef:
        """
        Lists the results of the Security Hub insight that the insight ARN specifies.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetInsightResults>`_

        **Request Syntax**
        ::

          response = client.get_insight_results(
              InsightArn='string'
          )
        :type InsightArn: string
        :param InsightArn: **[REQUIRED]**

          The ARN of the insight whose results you want to see.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'InsightResults': {
                    'InsightArn': 'string',
                    'GroupByAttribute': 'string',
                    'ResultValues': [
                        {
                            'GroupByAttributeValue': 'string',
                            'Count': 123
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **InsightResults** *(dict) --*

              The insight results returned by the operation.

              - **InsightArn** *(string) --*

                The ARN of the insight whose results are returned by the ``GetInsightResults`` operation.

              - **GroupByAttribute** *(string) --*

                The attribute that the findings are grouped by for the insight whose results are returned
                by the ``GetInsightResults`` operation.

              - **ResultValues** *(list) --*

                The list of insight result values returned by the ``GetInsightResults`` operation.

                - *(dict) --*

                  The insight result values returned by the ``GetInsightResults`` operation.

                  - **GroupByAttributeValue** *(string) --*

                    The value of the attribute that the findings are grouped by for the insight whose
                    results are returned by the ``GetInsightResults`` operation.

                  - **Count** *(integer) --*

                    The number of findings returned for each ``GroupByAttributeValue`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_insights(
        self,
        InsightArns: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetInsightsResponseTypeDef:
        """
        Lists and describes insights that insight ARNs specify.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetInsights>`_

        **Request Syntax**
        ::

          response = client.get_insights(
              InsightArns=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type InsightArns: list
        :param InsightArns:

          The ARNs of the insights that you want to describe.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          Paginates results. On your first call to the ``GetInsights`` operation, set the value of this
          parameter to ``NULL`` . For subsequent calls to the operation, fill ``nextToken`` in the request
          with the value of ``nextToken`` from the previous response to continue listing data.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of items that you want in the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Insights': [
                    {
                        'InsightArn': 'string',
                        'Name': 'string',
                        'Filters': {
                            'ProductArn': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'AwsAccountId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'Id': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'GeneratorId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'Type': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'FirstObservedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'LastObservedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'CreatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'UpdatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'SeverityProduct': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'SeverityNormalized': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'SeverityLabel': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'Confidence': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'Criticality': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'Title': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'Description': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'RecommendationText': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'SourceUrl': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ProductFields': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'
                                },
                            ],
                            'ProductName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'CompanyName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'UserDefinedFields': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'
                                },
                            ],
                            'MalwareName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'MalwareType': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'MalwarePath': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'MalwareState': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'NetworkDirection': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'NetworkProtocol': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'NetworkSourceIpV4': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'NetworkSourceIpV6': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'NetworkSourcePort': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'NetworkSourceDomain': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'NetworkSourceMac': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'NetworkDestinationIpV4': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'NetworkDestinationIpV6': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'NetworkDestinationPort': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'NetworkDestinationDomain': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ProcessName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ProcessPath': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ProcessPid': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'ProcessParentPid': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'ProcessLaunchedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ProcessTerminatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ThreatIntelIndicatorType': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ThreatIntelIndicatorValue': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ThreatIntelIndicatorCategory': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ThreatIntelIndicatorLastObservedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ThreatIntelIndicatorSource': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ThreatIntelIndicatorSourceUrl': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceType': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourcePartition': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceRegion': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceTags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'
                                },
                            ],
                            'ResourceAwsEc2InstanceType': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceImageId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceIpV4Addresses': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'ResourceAwsEc2InstanceIpV6Addresses': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'ResourceAwsEc2InstanceKeyName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceVpcId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceSubnetId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceLaunchedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ResourceAwsS3BucketOwnerId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsS3BucketOwnerName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsIamAccessKeyUserName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsIamAccessKeyStatus': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsIamAccessKeyCreatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ResourceContainerName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceContainerImageId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceContainerImageName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'ResourceContainerLaunchedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ResourceDetailsOther': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'
                                },
                            ],
                            'ComplianceStatus': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'VerificationState': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'WorkflowState': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'RecordState': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'RelatedFindingsProductArn': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'RelatedFindingsId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'NoteText': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'NoteUpdatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'NoteUpdatedBy': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'PREFIX'
                                },
                            ],
                            'Keyword': [
                                {
                                    'Value': 'string'
                                },
                            ]
                        },
                        'GroupByAttribute': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Insights** *(list) --*

              The insights returned by the operation.

              - *(dict) --*

                Contains information about a Security Hub insight.

                - **InsightArn** *(string) --*

                  The ARN of a Security Hub insight.

                - **Name** *(string) --*

                  The name of a Security Hub insight.

                - **Filters** *(dict) --*

                  One or more attributes used to filter the findings included in the insight. Only findings
                  that match the criteria defined in the filters are included in the insight.

                  - **ProductArn** *(list) --*

                    The ARN generated by Security Hub that uniquely identifies a third-party company
                    (security findings provider) after this provider's product (solution that generates
                    findings) is registered with Security Hub.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **AwsAccountId** *(list) --*

                    The AWS account ID that a finding is generated in.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **Id** *(list) --*

                    The security findings provider-specific identifier for a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **GeneratorId** *(list) --*

                    The identifier for the solution-specific component (a discrete unit of logic) that
                    generated a finding. In various security-findings providers' solutions, this generator
                    can be called a rule, a check, a detector, a plug-in, etc.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **Type** *(list) --*

                    A finding type in the format of ``namespace/category/classifier`` that classifies a
                    finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **FirstObservedAt** *(list) --*

                    An ISO8601-formatted timestamp that indicates when the security-findings provider first
                    observed the potential security issue that a finding captured.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **LastObservedAt** *(list) --*

                    An ISO8601-formatted timestamp that indicates when the security-findings provider most
                    recently observed the potential security issue that a finding captured.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **CreatedAt** *(list) --*

                    An ISO8601-formatted timestamp that indicates when the security-findings provider
                    captured the potential security issue that a finding captured.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **UpdatedAt** *(list) --*

                    An ISO8601-formatted timestamp that indicates when the security-findings provider last
                    updated the finding record.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **SeverityProduct** *(list) --*

                    The native severity as defined by the security-findings provider's solution that
                    generated the finding.

                    - *(dict) --*

                      A number filter for querying findings.

                      - **Gte** *(float) --*

                        The greater-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Lte** *(float) --*

                        The less-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Eq** *(float) --*

                        The equal-to condition to be applied to a single field when querying for findings.

                  - **SeverityNormalized** *(list) --*

                    The normalized severity of a finding.

                    - *(dict) --*

                      A number filter for querying findings.

                      - **Gte** *(float) --*

                        The greater-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Lte** *(float) --*

                        The less-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Eq** *(float) --*

                        The equal-to condition to be applied to a single field when querying for findings.

                  - **SeverityLabel** *(list) --*

                    The label of a finding's severity.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **Confidence** *(list) --*

                    A finding's confidence. Confidence is defined as the likelihood that a finding
                    accurately identifies the behavior or issue that it was intended to identify.
                    Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent
                    confidence and 100 means 100 percent confidence.

                    - *(dict) --*

                      A number filter for querying findings.

                      - **Gte** *(float) --*

                        The greater-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Lte** *(float) --*

                        The less-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Eq** *(float) --*

                        The equal-to condition to be applied to a single field when querying for findings.

                  - **Criticality** *(list) --*

                    The level of importance assigned to the resources associated with the finding. A score
                    of 0 means that the underlying resources have no criticality, and a score of 100 is
                    reserved for the most critical resources.

                    - *(dict) --*

                      A number filter for querying findings.

                      - **Gte** *(float) --*

                        The greater-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Lte** *(float) --*

                        The less-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Eq** *(float) --*

                        The equal-to condition to be applied to a single field when querying for findings.

                  - **Title** *(list) --*

                    A finding's title.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **Description** *(list) --*

                    A finding's description.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **RecommendationText** *(list) --*

                    The recommendation of what to do about the issue described in a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **SourceUrl** *(list) --*

                    A URL that links to a page about the current finding in the security-findings
                    provider's solution.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ProductFields** *(list) --*

                    A data type where security-findings providers can include additional solution-specific
                    details that aren't part of the defined ``AwsSecurityFinding`` format.

                    - *(dict) --*

                      The map filter for querying findings.

                      - **Key** *(string) --*

                        The key of the map filter.

                      - **Value** *(string) --*

                        The value for the key in the map filter.

                      - **Comparison** *(string) --*

                        The condition to apply to a key value when querying for findings with a map filter.

                  - **ProductName** *(list) --*

                    The name of the solution (product) that generates findings.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **CompanyName** *(list) --*

                    The name of the findings provider (company) that owns the solution (product) that
                    generates findings.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **UserDefinedFields** *(list) --*

                    A list of name/value string pairs associated with the finding. These are custom,
                    user-defined fields added to a finding.

                    - *(dict) --*

                      The map filter for querying findings.

                      - **Key** *(string) --*

                        The key of the map filter.

                      - **Value** *(string) --*

                        The value for the key in the map filter.

                      - **Comparison** *(string) --*

                        The condition to apply to a key value when querying for findings with a map filter.

                  - **MalwareName** *(list) --*

                    The name of the malware that was observed.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **MalwareType** *(list) --*

                    The type of the malware that was observed.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **MalwarePath** *(list) --*

                    The filesystem path of the malware that was observed.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **MalwareState** *(list) --*

                    The state of the malware that was observed.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **NetworkDirection** *(list) --*

                    Indicates the direction of network traffic associated with a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **NetworkProtocol** *(list) --*

                    The protocol of network-related information about a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **NetworkSourceIpV4** *(list) --*

                    The source IPv4 address of network-related information about a finding.

                    - *(dict) --*

                      The IP filter for querying findings.

                      - **Cidr** *(string) --*

                        A finding's CIDR value.

                  - **NetworkSourceIpV6** *(list) --*

                    The source IPv6 address of network-related information about a finding.

                    - *(dict) --*

                      The IP filter for querying findings.

                      - **Cidr** *(string) --*

                        A finding's CIDR value.

                  - **NetworkSourcePort** *(list) --*

                    The source port of network-related information about a finding.

                    - *(dict) --*

                      A number filter for querying findings.

                      - **Gte** *(float) --*

                        The greater-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Lte** *(float) --*

                        The less-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Eq** *(float) --*

                        The equal-to condition to be applied to a single field when querying for findings.

                  - **NetworkSourceDomain** *(list) --*

                    The source domain of network-related information about a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **NetworkSourceMac** *(list) --*

                    The source media access control (MAC) address of network-related information about a
                    finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **NetworkDestinationIpV4** *(list) --*

                    The destination IPv4 address of network-related information about a finding.

                    - *(dict) --*

                      The IP filter for querying findings.

                      - **Cidr** *(string) --*

                        A finding's CIDR value.

                  - **NetworkDestinationIpV6** *(list) --*

                    The destination IPv6 address of network-related information about a finding.

                    - *(dict) --*

                      The IP filter for querying findings.

                      - **Cidr** *(string) --*

                        A finding's CIDR value.

                  - **NetworkDestinationPort** *(list) --*

                    The destination port of network-related information about a finding.

                    - *(dict) --*

                      A number filter for querying findings.

                      - **Gte** *(float) --*

                        The greater-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Lte** *(float) --*

                        The less-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Eq** *(float) --*

                        The equal-to condition to be applied to a single field when querying for findings.

                  - **NetworkDestinationDomain** *(list) --*

                    The destination domain of network-related information about a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ProcessName** *(list) --*

                    The name of the process.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ProcessPath** *(list) --*

                    The path to the process executable.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ProcessPid** *(list) --*

                    The process ID.

                    - *(dict) --*

                      A number filter for querying findings.

                      - **Gte** *(float) --*

                        The greater-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Lte** *(float) --*

                        The less-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Eq** *(float) --*

                        The equal-to condition to be applied to a single field when querying for findings.

                  - **ProcessParentPid** *(list) --*

                    The parent process ID.

                    - *(dict) --*

                      A number filter for querying findings.

                      - **Gte** *(float) --*

                        The greater-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Lte** *(float) --*

                        The less-than-equal condition to be applied to a single field when querying for
                        findings.

                      - **Eq** *(float) --*

                        The equal-to condition to be applied to a single field when querying for findings.

                  - **ProcessLaunchedAt** *(list) --*

                    The date/time that the process was launched.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **ProcessTerminatedAt** *(list) --*

                    The date/time that the process was terminated.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **ThreatIntelIndicatorType** *(list) --*

                    The type of a threat intel indicator.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ThreatIntelIndicatorValue** *(list) --*

                    The value of a threat intel indicator.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ThreatIntelIndicatorCategory** *(list) --*

                    The category of a threat intel indicator.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ThreatIntelIndicatorLastObservedAt** *(list) --*

                    The date/time of the last observation of a threat intel indicator.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **ThreatIntelIndicatorSource** *(list) --*

                    The source of the threat intel.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ThreatIntelIndicatorSourceUrl** *(list) --*

                    The URL for more details from the source of the threat intel.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceType** *(list) --*

                    Specifies the type of the resource that details are provided for.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceId** *(list) --*

                    The canonical identifier for the given resource type.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourcePartition** *(list) --*

                    The canonical AWS partition name that the Region is assigned to.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceRegion** *(list) --*

                    The canonical AWS external Region name where this resource is located.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceTags** *(list) --*

                    A list of AWS tags associated with a resource at the time the finding was processed.

                    - *(dict) --*

                      The map filter for querying findings.

                      - **Key** *(string) --*

                        The key of the map filter.

                      - **Value** *(string) --*

                        The value for the key in the map filter.

                      - **Comparison** *(string) --*

                        The condition to apply to a key value when querying for findings with a map filter.

                  - **ResourceAwsEc2InstanceType** *(list) --*

                    The instance type of the instance.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsEc2InstanceImageId** *(list) --*

                    The Amazon Machine Image (AMI) ID of the instance.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*

                    The IPv4 addresses associated with the instance.

                    - *(dict) --*

                      The IP filter for querying findings.

                      - **Cidr** *(string) --*

                        A finding's CIDR value.

                  - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*

                    The IPv6 addresses associated with the instance.

                    - *(dict) --*

                      The IP filter for querying findings.

                      - **Cidr** *(string) --*

                        A finding's CIDR value.

                  - **ResourceAwsEc2InstanceKeyName** *(list) --*

                    The key name associated with the instance.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*

                    The IAM profile ARN of the instance.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsEc2InstanceVpcId** *(list) --*

                    The identifier of the VPC that the instance was launched in.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsEc2InstanceSubnetId** *(list) --*

                    The identifier of the subnet that the instance was launched in.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*

                    The date/time the instance was launched.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **ResourceAwsS3BucketOwnerId** *(list) --*

                    The canonical user ID of the owner of the S3 bucket.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsS3BucketOwnerName** *(list) --*

                    The display name of the owner of the S3 bucket.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsIamAccessKeyUserName** *(list) --*

                    The user associated with the IAM access key related to a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsIamAccessKeyStatus** *(list) --*

                    The status of the IAM access key related to a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*

                    The creation date/time of the IAM access key related to a finding.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **ResourceContainerName** *(list) --*

                    The name of the container related to a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceContainerImageId** *(list) --*

                    The identifier of the image related to a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceContainerImageName** *(list) --*

                    The name of the image related to a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **ResourceContainerLaunchedAt** *(list) --*

                    The date/time that the container was started.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **ResourceDetailsOther** *(list) --*

                    The details of a resource that doesn't have a specific subfield for the resource type
                    defined.

                    - *(dict) --*

                      The map filter for querying findings.

                      - **Key** *(string) --*

                        The key of the map filter.

                      - **Value** *(string) --*

                        The value for the key in the map filter.

                      - **Comparison** *(string) --*

                        The condition to apply to a key value when querying for findings with a map filter.

                  - **ComplianceStatus** *(list) --*

                    Exclusive to findings that are generated as the result of a check run against a
                    specific rule in a supported standard (for example, CIS AWS Foundations). Contains
                    compliance-related finding details.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **VerificationState** *(list) --*

                    The veracity of a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **WorkflowState** *(list) --*

                    The workflow state of a finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **RecordState** *(list) --*

                    The updated record state for the finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **RelatedFindingsProductArn** *(list) --*

                    The ARN of the solution that generated a related finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **RelatedFindingsId** *(list) --*

                    The solution-generated identifier for a related finding.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **NoteText** *(list) --*

                    The text of a note.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **NoteUpdatedAt** *(list) --*

                    The timestamp of when the note was updated.

                    - *(dict) --*

                      A date filter for querying findings.

                      - **Start** *(string) --*

                        A start date for the date filter.

                      - **End** *(string) --*

                        An end date for the date filter.

                      - **DateRange** *(dict) --*

                        A date range for the date filter.

                        - **Value** *(integer) --*

                          A date range value for the date filter.

                        - **Unit** *(string) --*

                          A date range unit for the date filter.

                  - **NoteUpdatedBy** *(list) --*

                    The principal that created a note.

                    - *(dict) --*

                      A string filter for querying findings.

                      - **Value** *(string) --*

                        The string filter value.

                      - **Comparison** *(string) --*

                        The condition to be applied to a string value when querying for findings.

                  - **Keyword** *(list) --*

                    A keyword for a finding.

                    - *(dict) --*

                      A keyword filter for querying findings.

                      - **Value** *(string) --*

                        A value for the keyword.

                - **GroupByAttribute** *(string) --*

                  The attribute that the insight's findings are grouped by. This attribute is used as a
                  findings aggregator for the purposes of viewing and managing multiple related findings
                  under a single operand.

            - **NextToken** *(string) --*

              The token that is required for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_invitations_count(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetInvitationsCountResponseTypeDef:
        """
        Returns the count of all Security Hub membership invitations that were sent to the current member
        account, not including the currently accepted invitation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetInvitationsCount>`_

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

              The number of all membership invitations sent to this Security Hub member account, not
              including the currently accepted invitation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_master_account(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetMasterAccountResponseTypeDef:
        """
        Provides the details for the Security Hub master account to the current member account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetMasterAccount>`_

        **Request Syntax**
        ::

          response = client.get_master_account()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Master': {
                    'AccountId': 'string',
                    'InvitationId': 'string',
                    'InvitedAt': datetime(2015, 1, 1),
                    'MemberStatus': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Master** *(dict) --*

              A list of details about the Security Hub master account for the current member account.

              - **AccountId** *(string) --*

                The account ID of the Security Hub master account that the invitation was sent from.

              - **InvitationId** *(string) --*

                The ID of the invitation sent to the member account.

              - **InvitedAt** *(datetime) --*

                The timestamp of when the invitation was sent.

              - **MemberStatus** *(string) --*

                The current status of the association between member and master accounts.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_members(self, AccountIds: List[str]) -> ClientGetMembersResponseTypeDef:
        """
        Returns the details on the Security Hub member accounts that the account IDs specify.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetMembers>`_

        **Request Syntax**
        ::

          response = client.get_members(
              AccountIds=[
                  'string',
              ]
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**

          A list of account IDs for the Security Hub member accounts that you want to return the details
          for.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Members': [
                    {
                        'AccountId': 'string',
                        'Email': 'string',
                        'MasterId': 'string',
                        'MemberStatus': 'string',
                        'InvitedAt': datetime(2015, 1, 1),
                        'UpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Members** *(list) --*

              A list of details about the Security Hub member accounts.

              - *(dict) --*

                The details about a member account.

                - **AccountId** *(string) --*

                  The AWS account ID of the member account.

                - **Email** *(string) --*

                  The email address of the member account.

                - **MasterId** *(string) --*

                  The AWS account ID of the Security Hub master account associated with this member account.

                - **MemberStatus** *(string) --*

                  The status of the relationship between the member account and its master account.

                - **InvitedAt** *(datetime) --*

                  A timestamp for the date and time when the invitation was sent to the member account.

                - **UpdatedAt** *(datetime) --*

                  The timestamp for the date and time when the member account was updated.

            - **UnprocessedAccounts** *(list) --*

              A list of account ID and email address pairs of the AWS accounts that couldn't be processed.

              - *(dict) --*

                Details about the account that wasn't processed.

                - **AccountId** *(string) --*

                  An AWS account ID of the account that wasn't be processed.

                - **ProcessingResult** *(string) --*

                  The reason that the account wasn't be processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invite_members(
        self, AccountIds: List[str] = None
    ) -> ClientInviteMembersResponseTypeDef:
        """
        Invites other AWS accounts to become member accounts for the Security Hub master account that the
        invitation is sent from. Before you can use this action to invite a member, you must first create
        the member account in Security Hub by using the  CreateMembers action. When the account owner
        accepts the invitation to become a member account and enables Security Hub, the master account can
        view the findings generated from member account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/InviteMembers>`_

        **Request Syntax**
        ::

          response = client.invite_members(
              AccountIds=[
                  'string',
              ]
          )
        :type AccountIds: list
        :param AccountIds:

          A list of IDs of the AWS accounts that you want to invite to Security Hub as members.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **UnprocessedAccounts** *(list) --*

              A list of account ID and email address pairs of the AWS accounts that couldn't be processed.

              - *(dict) --*

                Details about the account that wasn't processed.

                - **AccountId** *(string) --*

                  An AWS account ID of the account that wasn't be processed.

                - **ProcessingResult** *(string) --*

                  The reason that the account wasn't be processed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_enabled_products_for_import(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListEnabledProductsForImportResponseTypeDef:
        """
        Lists all findings-generating solutions (products) whose findings you have subscribed to receive in
        Security Hub.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListEnabledProductsForImport>`_

        **Request Syntax**
        ::

          response = client.list_enabled_products_for_import(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          Paginates results. On your first call to the ``ListEnabledProductsForImport`` operation, set the
          value of this parameter to ``NULL`` . For subsequent calls to the operation, fill ``nextToken``
          in the request with the value of ``NextToken`` from the previous response to continue listing
          data.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of items that you want in the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProductSubscriptions': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ProductSubscriptions** *(list) --*

              A list of ARNs for the resources that represent your subscriptions to products.

              - *(string) --*

            - **NextToken** *(string) --*

              The token that is required for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListInvitationsResponseTypeDef:
        """
        Lists all Security Hub membership invitations that were sent to the current AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListInvitations>`_

        **Request Syntax**
        ::

          response = client.list_invitations(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The maximum number of items that you want in the response.

        :type NextToken: string
        :param NextToken:

          Paginates results. On your first call to the ``ListInvitations`` operation, set the value of this
          parameter to ``NULL`` . For subsequent calls to the operation, fill ``nextToken`` in the request
          with the value of ``NextToken`` from the previous response to continue listing data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Invitations': [
                    {
                        'AccountId': 'string',
                        'InvitationId': 'string',
                        'InvitedAt': datetime(2015, 1, 1),
                        'MemberStatus': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Invitations** *(list) --*

              The details of the invitations returned by the operation.

              - *(dict) --*

                Details about an invitation.

                - **AccountId** *(string) --*

                  The account ID of the Security Hub master account that the invitation was sent from.

                - **InvitationId** *(string) --*

                  The ID of the invitation sent to the member account.

                - **InvitedAt** *(datetime) --*

                  The timestamp of when the invitation was sent.

                - **MemberStatus** *(string) --*

                  The current status of the association between member and master accounts.

            - **NextToken** *(string) --*

              The token that is required for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_members(
        self, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientListMembersResponseTypeDef:
        """
        Lists details about all member accounts for the current Security Hub master account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListMembers>`_

        **Request Syntax**
        ::

          response = client.list_members(
              OnlyAssociated=True|False,
              MaxResults=123,
              NextToken='string'
          )
        :type OnlyAssociated: boolean
        :param OnlyAssociated:

          Specifies which member accounts the response includes based on their relationship status with the
          master account. The default value is ``TRUE`` . If ``onlyAssociated`` is set to ``TRUE`` , the
          response includes member accounts whose relationship status with the master is set to ``ENABLED``
          or ``DISABLED`` . If ``onlyAssociated`` is set to ``FALSE`` , the response includes all existing
          member accounts.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of items that you want in the response.

        :type NextToken: string
        :param NextToken:

          Paginates results. Set the value of this parameter to ``NULL`` on your first call to the
          ``ListMembers`` operation. For subsequent calls to the operation, fill ``nextToken`` in the
          request with the value of ``nextToken`` from the previous response to continue listing data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Members': [
                    {
                        'AccountId': 'string',
                        'Email': 'string',
                        'MasterId': 'string',
                        'MemberStatus': 'string',
                        'InvitedAt': datetime(2015, 1, 1),
                        'UpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Members** *(list) --*

              Member details returned by the operation.

              - *(dict) --*

                The details about a member account.

                - **AccountId** *(string) --*

                  The AWS account ID of the member account.

                - **Email** *(string) --*

                  The email address of the member account.

                - **MasterId** *(string) --*

                  The AWS account ID of the Security Hub master account associated with this member account.

                - **MemberStatus** *(string) --*

                  The status of the relationship between the member account and its master account.

                - **InvitedAt** *(datetime) --*

                  A timestamp for the date and time when the invitation was sent to the member account.

                - **UpdatedAt** *(datetime) --*

                  The timestamp for the date and time when the member account was updated.

            - **NextToken** *(string) --*

              The token that is required for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags associated with a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The ARN of the resource to retrieve tags for.

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

              The tags associated with a resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[str]) -> Dict[str, Any]:
        """
        Adds one or more tags to a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/TagResource>`_

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

          The ARN of the resource to apply the tags to.

        :type Tags: dict
        :param Tags: **[REQUIRED]**

          The tags to add to the resource.

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
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/UntagResource>`_

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

          The ARN of the resource to remove the tags from.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The tag keys associated with the tags to remove from the resource.

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
    def update_action_target(
        self, ActionTargetArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates the name and description of a custom action target in Security Hub.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/UpdateActionTarget>`_

        **Request Syntax**
        ::

          response = client.update_action_target(
              ActionTargetArn='string',
              Name='string',
              Description='string'
          )
        :type ActionTargetArn: string
        :param ActionTargetArn: **[REQUIRED]**

          The ARN of the custom action target to update.

        :type Name: string
        :param Name:

          The updated name of the custom action target.

        :type Description: string
        :param Description:

          The updated description for the custom action target.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_findings(
        self,
        Filters: ClientUpdateFindingsFiltersTypeDef,
        Note: ClientUpdateFindingsNoteTypeDef = None,
        RecordState: str = None,
    ) -> Dict[str, Any]:
        """
        Updates the ``Note`` and ``RecordState`` of the Security Hub-aggregated findings that the filter
        attributes specify. Any member account that can view the finding also sees the update to the
        finding.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/UpdateFindings>`_

        **Request Syntax**
        ::

          response = client.update_findings(
              Filters={
                  'ProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'AwsAccountId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Id': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'GeneratorId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Type': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'FirstObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'LastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'CreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'UpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'SeverityProduct': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityNormalized': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityLabel': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Confidence': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Criticality': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Title': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Description': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RecommendationText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'SourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProductFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ProductName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'CompanyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'UserDefinedFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'MalwareName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwareType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwarePath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwareState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkDirection': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkProtocol': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourceIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourcePort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkSourceDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceMac': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkDestinationIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationPort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkDestinationDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessPath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessParentPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ProcessTerminatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorValue': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorCategory': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorLastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorSource': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorSourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourcePartition': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceRegion': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ResourceAwsEc2InstanceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV4Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV6Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceKeyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceVpcId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceSubnetId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceAwsS3BucketOwnerId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsS3BucketOwnerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyUserName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyCreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceContainerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceDetailsOther': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ComplianceStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'VerificationState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'WorkflowState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RecordState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NoteText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NoteUpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'NoteUpdatedBy': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Keyword': [
                      {
                          'Value': 'string'
                      },
                  ]
              },
              Note={
                  'Text': 'string',
                  'UpdatedBy': 'string'
              },
              RecordState='ACTIVE'|'ARCHIVED'
          )
        :type Filters: dict
        :param Filters: **[REQUIRED]**

          A collection of attributes that specify which findings you want to update.

          - **ProductArn** *(list) --*

            The ARN generated by Security Hub that uniquely identifies a third-party company (security
            findings provider) after this provider's product (solution that generates findings) is
            registered with Security Hub.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **AwsAccountId** *(list) --*

            The AWS account ID that a finding is generated in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Id** *(list) --*

            The security findings provider-specific identifier for a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **GeneratorId** *(list) --*

            The identifier for the solution-specific component (a discrete unit of logic) that generated a
            finding. In various security-findings providers' solutions, this generator can be called a
            rule, a check, a detector, a plug-in, etc.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Type** *(list) --*

            A finding type in the format of ``namespace/category/classifier`` that classifies a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **FirstObservedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider first
            observed the potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **LastObservedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider most recently
            observed the potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **CreatedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider captured the
            potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **UpdatedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider last updated
            the finding record.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **SeverityProduct** *(list) --*

            The native severity as defined by the security-findings provider's solution that generated the
            finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **SeverityNormalized** *(list) --*

            The normalized severity of a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **SeverityLabel** *(list) --*

            The label of a finding's severity.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Confidence** *(list) --*

            A finding's confidence. Confidence is defined as the likelihood that a finding accurately
            identifies the behavior or issue that it was intended to identify. Confidence is scored on a
            0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100
            percent confidence.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **Criticality** *(list) --*

            The level of importance assigned to the resources associated with the finding. A score of 0
            means that the underlying resources have no criticality, and a score of 100 is reserved for the
            most critical resources.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **Title** *(list) --*

            A finding's title.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Description** *(list) --*

            A finding's description.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RecommendationText** *(list) --*

            The recommendation of what to do about the issue described in a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **SourceUrl** *(list) --*

            A URL that links to a page about the current finding in the security-findings provider's
            solution.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProductFields** *(list) --*

            A data type where security-findings providers can include additional solution-specific details
            that aren't part of the defined ``AwsSecurityFinding`` format.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ProductName** *(list) --*

            The name of the solution (product) that generates findings.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **CompanyName** *(list) --*

            The name of the findings provider (company) that owns the solution (product) that generates
            findings.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **UserDefinedFields** *(list) --*

            A list of name/value string pairs associated with the finding. These are custom, user-defined
            fields added to a finding.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **MalwareName** *(list) --*

            The name of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwareType** *(list) --*

            The type of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwarePath** *(list) --*

            The filesystem path of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwareState** *(list) --*

            The state of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkDirection** *(list) --*

            Indicates the direction of network traffic associated with a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkProtocol** *(list) --*

            The protocol of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkSourceIpV4** *(list) --*

            The source IPv4 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkSourceIpV6** *(list) --*

            The source IPv6 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkSourcePort** *(list) --*

            The source port of network-related information about a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **NetworkSourceDomain** *(list) --*

            The source domain of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkSourceMac** *(list) --*

            The source media access control (MAC) address of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkDestinationIpV4** *(list) --*

            The destination IPv4 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkDestinationIpV6** *(list) --*

            The destination IPv6 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkDestinationPort** *(list) --*

            The destination port of network-related information about a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **NetworkDestinationDomain** *(list) --*

            The destination domain of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessName** *(list) --*

            The name of the process.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessPath** *(list) --*

            The path to the process executable.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessPid** *(list) --*

            The process ID.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **ProcessParentPid** *(list) --*

            The parent process ID.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **ProcessLaunchedAt** *(list) --*

            The date/time that the process was launched.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ProcessTerminatedAt** *(list) --*

            The date/time that the process was terminated.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ThreatIntelIndicatorType** *(list) --*

            The type of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorValue** *(list) --*

            The value of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorCategory** *(list) --*

            The category of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorLastObservedAt** *(list) --*

            The date/time of the last observation of a threat intel indicator.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ThreatIntelIndicatorSource** *(list) --*

            The source of the threat intel.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorSourceUrl** *(list) --*

            The URL for more details from the source of the threat intel.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceType** *(list) --*

            Specifies the type of the resource that details are provided for.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceId** *(list) --*

            The canonical identifier for the given resource type.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourcePartition** *(list) --*

            The canonical AWS partition name that the Region is assigned to.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceRegion** *(list) --*

            The canonical AWS external Region name where this resource is located.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceTags** *(list) --*

            A list of AWS tags associated with a resource at the time the finding was processed.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ResourceAwsEc2InstanceType** *(list) --*

            The instance type of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceImageId** *(list) --*

            The Amazon Machine Image (AMI) ID of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*

            The IPv4 addresses associated with the instance.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*

            The IPv6 addresses associated with the instance.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **ResourceAwsEc2InstanceKeyName** *(list) --*

            The key name associated with the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*

            The IAM profile ARN of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceVpcId** *(list) --*

            The identifier of the VPC that the instance was launched in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceSubnetId** *(list) --*

            The identifier of the subnet that the instance was launched in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*

            The date/time the instance was launched.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceAwsS3BucketOwnerId** *(list) --*

            The canonical user ID of the owner of the S3 bucket.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsS3BucketOwnerName** *(list) --*

            The display name of the owner of the S3 bucket.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyUserName** *(list) --*

            The user associated with the IAM access key related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyStatus** *(list) --*

            The status of the IAM access key related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*

            The creation date/time of the IAM access key related to a finding.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceContainerName** *(list) --*

            The name of the container related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerImageId** *(list) --*

            The identifier of the image related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerImageName** *(list) --*

            The name of the image related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerLaunchedAt** *(list) --*

            The date/time that the container was started.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceDetailsOther** *(list) --*

            The details of a resource that doesn't have a specific subfield for the resource type defined.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ComplianceStatus** *(list) --*

            Exclusive to findings that are generated as the result of a check run against a specific rule
            in a supported standard (for example, CIS AWS Foundations). Contains compliance-related finding
            details.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **VerificationState** *(list) --*

            The veracity of a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **WorkflowState** *(list) --*

            The workflow state of a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RecordState** *(list) --*

            The updated record state for the finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RelatedFindingsProductArn** *(list) --*

            The ARN of the solution that generated a related finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RelatedFindingsId** *(list) --*

            The solution-generated identifier for a related finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NoteText** *(list) --*

            The text of a note.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NoteUpdatedAt** *(list) --*

            The timestamp of when the note was updated.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **NoteUpdatedBy** *(list) --*

            The principal that created a note.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Keyword** *(list) --*

            A keyword for a finding.

            - *(dict) --*

              A keyword filter for querying findings.

              - **Value** *(string) --*

                A value for the keyword.

        :type Note: dict
        :param Note:

          The updated note for the finding.

          - **Text** *(string) --* **[REQUIRED]**

            The updated note text.

          - **UpdatedBy** *(string) --* **[REQUIRED]**

            The principal that updated the note.

        :type RecordState: string
        :param RecordState:

          The updated record state for the finding.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_insight(
        self,
        InsightArn: str,
        Name: str = None,
        Filters: ClientUpdateInsightFiltersTypeDef = None,
        GroupByAttribute: str = None,
    ) -> Dict[str, Any]:
        """
        Updates the Security Hub insight that the insight ARN specifies.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/UpdateInsight>`_

        **Request Syntax**
        ::

          response = client.update_insight(
              InsightArn='string',
              Name='string',
              Filters={
                  'ProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'AwsAccountId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Id': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'GeneratorId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Type': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'FirstObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'LastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'CreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'UpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'SeverityProduct': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityNormalized': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityLabel': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Confidence': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Criticality': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Title': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Description': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RecommendationText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'SourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProductFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ProductName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'CompanyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'UserDefinedFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'MalwareName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwareType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwarePath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'MalwareState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkDirection': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkProtocol': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourceIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourcePort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkSourceDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceMac': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NetworkDestinationIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationPort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkDestinationDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessPath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ProcessPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessParentPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ProcessTerminatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorValue': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorCategory': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorLastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorSource': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorSourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourcePartition': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceRegion': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ResourceAwsEc2InstanceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV4Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV6Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceKeyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceVpcId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceSubnetId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceAwsS3BucketOwnerId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsS3BucketOwnerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyUserName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyCreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceContainerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceDetailsOther': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'EQUALS'
                      },
                  ],
                  'ComplianceStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'VerificationState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'WorkflowState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RecordState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NoteText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'NoteUpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'NoteUpdatedBy': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'PREFIX'
                      },
                  ],
                  'Keyword': [
                      {
                          'Value': 'string'
                      },
                  ]
              },
              GroupByAttribute='string'
          )
        :type InsightArn: string
        :param InsightArn: **[REQUIRED]**

          The ARN of the insight that you want to update.

        :type Name: string
        :param Name:

          The updated name for the insight.

        :type Filters: dict
        :param Filters:

          The updated filters that define this insight.

          - **ProductArn** *(list) --*

            The ARN generated by Security Hub that uniquely identifies a third-party company (security
            findings provider) after this provider's product (solution that generates findings) is
            registered with Security Hub.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **AwsAccountId** *(list) --*

            The AWS account ID that a finding is generated in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Id** *(list) --*

            The security findings provider-specific identifier for a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **GeneratorId** *(list) --*

            The identifier for the solution-specific component (a discrete unit of logic) that generated a
            finding. In various security-findings providers' solutions, this generator can be called a
            rule, a check, a detector, a plug-in, etc.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Type** *(list) --*

            A finding type in the format of ``namespace/category/classifier`` that classifies a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **FirstObservedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider first
            observed the potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **LastObservedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider most recently
            observed the potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **CreatedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider captured the
            potential security issue that a finding captured.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **UpdatedAt** *(list) --*

            An ISO8601-formatted timestamp that indicates when the security-findings provider last updated
            the finding record.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **SeverityProduct** *(list) --*

            The native severity as defined by the security-findings provider's solution that generated the
            finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **SeverityNormalized** *(list) --*

            The normalized severity of a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **SeverityLabel** *(list) --*

            The label of a finding's severity.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Confidence** *(list) --*

            A finding's confidence. Confidence is defined as the likelihood that a finding accurately
            identifies the behavior or issue that it was intended to identify. Confidence is scored on a
            0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100
            percent confidence.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **Criticality** *(list) --*

            The level of importance assigned to the resources associated with the finding. A score of 0
            means that the underlying resources have no criticality, and a score of 100 is reserved for the
            most critical resources.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **Title** *(list) --*

            A finding's title.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Description** *(list) --*

            A finding's description.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RecommendationText** *(list) --*

            The recommendation of what to do about the issue described in a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **SourceUrl** *(list) --*

            A URL that links to a page about the current finding in the security-findings provider's
            solution.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProductFields** *(list) --*

            A data type where security-findings providers can include additional solution-specific details
            that aren't part of the defined ``AwsSecurityFinding`` format.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ProductName** *(list) --*

            The name of the solution (product) that generates findings.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **CompanyName** *(list) --*

            The name of the findings provider (company) that owns the solution (product) that generates
            findings.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **UserDefinedFields** *(list) --*

            A list of name/value string pairs associated with the finding. These are custom, user-defined
            fields added to a finding.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **MalwareName** *(list) --*

            The name of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwareType** *(list) --*

            The type of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwarePath** *(list) --*

            The filesystem path of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **MalwareState** *(list) --*

            The state of the malware that was observed.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkDirection** *(list) --*

            Indicates the direction of network traffic associated with a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkProtocol** *(list) --*

            The protocol of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkSourceIpV4** *(list) --*

            The source IPv4 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkSourceIpV6** *(list) --*

            The source IPv6 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkSourcePort** *(list) --*

            The source port of network-related information about a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **NetworkSourceDomain** *(list) --*

            The source domain of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkSourceMac** *(list) --*

            The source media access control (MAC) address of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NetworkDestinationIpV4** *(list) --*

            The destination IPv4 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkDestinationIpV6** *(list) --*

            The destination IPv6 address of network-related information about a finding.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **NetworkDestinationPort** *(list) --*

            The destination port of network-related information about a finding.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **NetworkDestinationDomain** *(list) --*

            The destination domain of network-related information about a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessName** *(list) --*

            The name of the process.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessPath** *(list) --*

            The path to the process executable.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ProcessPid** *(list) --*

            The process ID.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **ProcessParentPid** *(list) --*

            The parent process ID.

            - *(dict) --*

              A number filter for querying findings.

              - **Gte** *(float) --*

                The greater-than-equal condition to be applied to a single field when querying for findings.

              - **Lte** *(float) --*

                The less-than-equal condition to be applied to a single field when querying for findings.

              - **Eq** *(float) --*

                The equal-to condition to be applied to a single field when querying for findings.

          - **ProcessLaunchedAt** *(list) --*

            The date/time that the process was launched.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ProcessTerminatedAt** *(list) --*

            The date/time that the process was terminated.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ThreatIntelIndicatorType** *(list) --*

            The type of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorValue** *(list) --*

            The value of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorCategory** *(list) --*

            The category of a threat intel indicator.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorLastObservedAt** *(list) --*

            The date/time of the last observation of a threat intel indicator.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ThreatIntelIndicatorSource** *(list) --*

            The source of the threat intel.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ThreatIntelIndicatorSourceUrl** *(list) --*

            The URL for more details from the source of the threat intel.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceType** *(list) --*

            Specifies the type of the resource that details are provided for.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceId** *(list) --*

            The canonical identifier for the given resource type.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourcePartition** *(list) --*

            The canonical AWS partition name that the Region is assigned to.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceRegion** *(list) --*

            The canonical AWS external Region name where this resource is located.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceTags** *(list) --*

            A list of AWS tags associated with a resource at the time the finding was processed.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ResourceAwsEc2InstanceType** *(list) --*

            The instance type of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceImageId** *(list) --*

            The Amazon Machine Image (AMI) ID of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*

            The IPv4 addresses associated with the instance.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*

            The IPv6 addresses associated with the instance.

            - *(dict) --*

              The IP filter for querying findings.

              - **Cidr** *(string) --*

                A finding's CIDR value.

          - **ResourceAwsEc2InstanceKeyName** *(list) --*

            The key name associated with the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*

            The IAM profile ARN of the instance.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceVpcId** *(list) --*

            The identifier of the VPC that the instance was launched in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceSubnetId** *(list) --*

            The identifier of the subnet that the instance was launched in.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*

            The date/time the instance was launched.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceAwsS3BucketOwnerId** *(list) --*

            The canonical user ID of the owner of the S3 bucket.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsS3BucketOwnerName** *(list) --*

            The display name of the owner of the S3 bucket.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyUserName** *(list) --*

            The user associated with the IAM access key related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyStatus** *(list) --*

            The status of the IAM access key related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*

            The creation date/time of the IAM access key related to a finding.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceContainerName** *(list) --*

            The name of the container related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerImageId** *(list) --*

            The identifier of the image related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerImageName** *(list) --*

            The name of the image related to a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **ResourceContainerLaunchedAt** *(list) --*

            The date/time that the container was started.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **ResourceDetailsOther** *(list) --*

            The details of a resource that doesn't have a specific subfield for the resource type defined.

            - *(dict) --*

              The map filter for querying findings.

              - **Key** *(string) --*

                The key of the map filter.

              - **Value** *(string) --*

                The value for the key in the map filter.

              - **Comparison** *(string) --*

                The condition to apply to a key value when querying for findings with a map filter.

          - **ComplianceStatus** *(list) --*

            Exclusive to findings that are generated as the result of a check run against a specific rule
            in a supported standard (for example, CIS AWS Foundations). Contains compliance-related finding
            details.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **VerificationState** *(list) --*

            The veracity of a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **WorkflowState** *(list) --*

            The workflow state of a finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RecordState** *(list) --*

            The updated record state for the finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RelatedFindingsProductArn** *(list) --*

            The ARN of the solution that generated a related finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **RelatedFindingsId** *(list) --*

            The solution-generated identifier for a related finding.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NoteText** *(list) --*

            The text of a note.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **NoteUpdatedAt** *(list) --*

            The timestamp of when the note was updated.

            - *(dict) --*

              A date filter for querying findings.

              - **Start** *(string) --*

                A start date for the date filter.

              - **End** *(string) --*

                An end date for the date filter.

              - **DateRange** *(dict) --*

                A date range for the date filter.

                - **Value** *(integer) --*

                  A date range value for the date filter.

                - **Unit** *(string) --*

                  A date range unit for the date filter.

          - **NoteUpdatedBy** *(list) --*

            The principal that created a note.

            - *(dict) --*

              A string filter for querying findings.

              - **Value** *(string) --*

                The string filter value.

              - **Comparison** *(string) --*

                The condition to be applied to a string value when querying for findings.

          - **Keyword** *(list) --*

            A keyword for a finding.

            - *(dict) --*

              A keyword filter for querying findings.

              - **Value** *(string) --*

                A value for the keyword.

        :type GroupByAttribute: string
        :param GroupByAttribute:

          The updated ``GroupBy`` attribute that defines this insight.

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
        self, operation_name: Literal["get_enabled_standards"]
    ) -> paginator_scope.GetEnabledStandardsPaginator:
        """
        Get Paginator for `get_enabled_standards` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_findings"]
    ) -> paginator_scope.GetFindingsPaginator:
        """
        Get Paginator for `get_findings` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_insights"]
    ) -> paginator_scope.GetInsightsPaginator:
        """
        Get Paginator for `get_insights` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_enabled_products_for_import"]
    ) -> paginator_scope.ListEnabledProductsForImportPaginator:
        """
        Get Paginator for `list_enabled_products_for_import` operation.
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
    ClientError: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidAccessException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
