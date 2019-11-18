"Main interface for fms Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_fms.client as client_scope

# pylint: disable=import-self
import mypy_boto3_fms.paginator as paginator_scope
from mypy_boto3_fms.type_defs import (
    ClientGetAdminAccountResponseTypeDef,
    ClientGetComplianceDetailResponseTypeDef,
    ClientGetNotificationChannelResponseTypeDef,
    ClientGetProtectionStatusResponseTypeDef,
    ClientListComplianceStatusResponseTypeDef,
    ClientListMemberAccountsResponseTypeDef,
    ClientListPoliciesResponseTypeDef,
    ClientPutPolicyPolicyTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_admin_account(self, AdminAccount: str) -> None:
        """
        Sets the AWS Firewall Manager administrator account. AWS Firewall Manager must be associated with
        the master account of your AWS organization or associated with a member account that has the
        appropriate permissions. If the account ID that you submit is not an AWS Organizations master
        account, AWS Firewall Manager will set the appropriate permissions for the given member account.

        The account that you associate with AWS Firewall Manager is called the AWS Firewall Manager
        administrator account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/AssociateAdminAccount>`_

        **Request Syntax**
        ::

          response = client.associate_admin_account(
              AdminAccount='string'
          )
        :type AdminAccount: string
        :param AdminAccount: **[REQUIRED]**

          The AWS account ID to associate with AWS Firewall Manager as the AWS Firewall Manager
          administrator account. This can be an AWS Organizations master account or a member account. For
          more information about AWS Organizations and master accounts, see `Managing the AWS Accounts in
          Your Organization
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html>`__ .

        :returns: None
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
    def delete_notification_channel(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes an AWS Firewall Manager association with the IAM role and the Amazon Simple Notification
        Service (SNS) topic that is used to record AWS Firewall Manager SNS logs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DeleteNotificationChannel>`_

        **Request Syntax**
        ::

          response = client.delete_notification_channel()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_policy(
        self, PolicyId: str, DeleteAllPolicyResources: bool = None
    ) -> None:
        """
        Permanently deletes an AWS Firewall Manager policy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DeletePolicy>`_

        **Request Syntax**
        ::

          response = client.delete_policy(
              PolicyId='string',
              DeleteAllPolicyResources=True|False
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]**

          The ID of the policy that you want to delete. ``PolicyId`` is returned by ``PutPolicy`` and by
          ``ListPolicies`` .

        :type DeleteAllPolicyResources: boolean
        :param DeleteAllPolicyResources:

          If ``True`` , the request performs cleanup according to the policy type.

          For AWS WAF and Shield Advanced policies, the cleanup does the following:

          * Deletes rule groups created by AWS Firewall Manager

          * Removes web ACLs from in-scope resources

          * Deletes web ACLs that contain no rules or rule groups

          For security group policies, the cleanup does the following for each security group in the policy:

          * Disassociates the security group from in-scope resources

          * Deletes the security group if it was created through Firewall Manager and if it's no longer
          associated with any resources through another policy

          After the cleanup, in-scope resources are no longer protected by web ACLs in this policy.
          Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you
          create and accounts that you associate with the policy. When creating the policy, if you specify
          that only resources in specific accounts or with specific tags are in scope of the policy, those
          accounts and resources are handled by the policy. All others are out of scope. If you don't
          specify tags or accounts, all resources are in scope.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_admin_account(self, *args: Any, **kwargs: Any) -> None:
        """
        Disassociates the account that has been set as the AWS Firewall Manager administrator account. To
        set a different account as the administrator account, you must submit an ``AssociateAdminAccount``
        request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DisassociateAdminAccount>`_

        **Request Syntax**
        ::

          response = client.disassociate_admin_account()

        :returns: None
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
    def get_admin_account(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAdminAccountResponseTypeDef:
        """
        Returns the AWS Organizations master account that is associated with AWS Firewall Manager as the
        AWS Firewall Manager administrator.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetAdminAccount>`_

        **Request Syntax**
        ::

          response = client.get_admin_account()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AdminAccount': 'string',
                'RoleStatus': 'READY'|'CREATING'|'PENDING_DELETION'|'DELETING'|'DELETED'
            }
          **Response Structure**

          - *(dict) --*

            - **AdminAccount** *(string) --*

              The AWS account that is set as the AWS Firewall Manager administrator.

            - **RoleStatus** *(string) --*

              The status of the AWS account that you set as the AWS Firewall Manager administrator.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_compliance_detail(
        self, PolicyId: str, MemberAccount: str
    ) -> ClientGetComplianceDetailResponseTypeDef:
        """
        Returns detailed compliance information about the specified member account. Details include
        resources that are in and out of compliance with the specified policy. Resources are considered
        noncompliant for AWS WAF and Shield Advanced policies if the specified policy has not been applied
        to them. Resources are considered noncompliant for security group policies if they are in scope of
        the policy, they violate one or more of the policy rules, and remediation is disabled or not
        possible.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetComplianceDetail>`_

        **Request Syntax**
        ::

          response = client.get_compliance_detail(
              PolicyId='string',
              MemberAccount='string'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]**

          The ID of the policy that you want to get the details for. ``PolicyId`` is returned by
          ``PutPolicy`` and by ``ListPolicies`` .

        :type MemberAccount: string
        :param MemberAccount: **[REQUIRED]**

          The AWS account that owns the resources that you want to get the details for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyComplianceDetail': {
                    'PolicyOwner': 'string',
                    'PolicyId': 'string',
                    'MemberAccount': 'string',
                    'Violators': [
                        {
                            'ResourceId': 'string',
                            'ViolationReason':
                            'WEB_ACL_MISSING_RULE_GROUP'|'RESOURCE_MISSING_WEB_ACL'
                            |'RESOURCE_INCORRECT_WEB_ACL'|'RESOURCE_MISSING_SHIELD_PROTECTION'
                            |'RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION'
                            |'RESOURCE_MISSING_SECURITY_GROUP'|'RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP'
                            |'SECURITY_GROUP_UNUSED'|'SECURITY_GROUP_REDUNDANT',
                            'ResourceType': 'string'
                        },
                    ],
                    'EvaluationLimitExceeded': True|False,
                    'ExpiredAt': datetime(2015, 1, 1),
                    'IssueInfoMap': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyComplianceDetail** *(dict) --*

              Information about the resources and the policy that you specified in the
              ``GetComplianceDetail`` request.

              - **PolicyOwner** *(string) --*

                The AWS account that created the AWS Firewall Manager policy.

              - **PolicyId** *(string) --*

                The ID of the AWS Firewall Manager policy.

              - **MemberAccount** *(string) --*

                The AWS account ID.

              - **Violators** *(list) --*

                An array of resources that aren't protected by the AWS WAF or Shield Advanced policy or
                that aren't in compliance with the security group policy.

                - *(dict) --*

                  Details of the resource that is not protected by the policy.

                  - **ResourceId** *(string) --*

                    The resource ID.

                  - **ViolationReason** *(string) --*

                    The reason that the resource is not protected by the policy.

                  - **ResourceType** *(string) --*

                    The resource type. This is in the format shown in the `AWS Resource Types Reference
                    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
                    . For example: ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or
                    ``AWS::CloudFront::Distribution`` .

              - **EvaluationLimitExceeded** *(boolean) --*

                Indicates if over 100 resources are noncompliant with the AWS Firewall Manager policy.

              - **ExpiredAt** *(datetime) --*

                A timestamp that indicates when the returned information should be considered out of date.

              - **IssueInfoMap** *(dict) --*

                Details about problems with dependent services, such as AWS WAF or AWS Config, that are
                causing a resource to be noncompliant. The details include the name of the dependent
                service and the error message received that indicates the problem with the service.

                - *(string) --*

                  - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_notification_channel(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetNotificationChannelResponseTypeDef:
        """
        Information about the Amazon Simple Notification Service (SNS) topic that is used to record AWS
        Firewall Manager SNS logs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetNotificationChannel>`_

        **Request Syntax**
        ::

          response = client.get_notification_channel()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SnsTopicArn': 'string',
                'SnsRoleName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **SnsTopicArn** *(string) --*

              The SNS topic that records AWS Firewall Manager activity.

            - **SnsRoleName** *(string) --*

              The IAM role that is used by AWS Firewall Manager to record activity to SNS.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_policy(self, PolicyId: str) -> Dict[str, Any]:
        """
        Returns information about the specified AWS Firewall Manager policy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetPolicy>`_

        **Request Syntax**
        ::

          response = client.get_policy(
              PolicyId='string'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]**

          The ID of the AWS Firewall Manager policy that you want the details for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Policy': {
                    'PolicyId': 'string',
                    'PolicyName': 'string',
                    'PolicyUpdateToken': 'string',
                    'SecurityServicePolicyData': {
                        'Type':
                        'WAF'|'SHIELD_ADVANCED'|'SECURITY_GROUPS_COMMON'|'SECURITY_GROUPS_CONTENT_AUDIT'
                        |'SECURITY_GROUPS_USAGE_AUDIT',
                        'ManagedServiceData': 'string'
                    },
                    'ResourceType': 'string',
                    'ResourceTypeList': [
                        'string',
                    ],
                    'ResourceTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'ExcludeResourceTags': True|False,
                    'RemediationEnabled': True|False,
                    'IncludeMap': {
                        'string': [
                            'string',
                        ]
                    },
                    'ExcludeMap': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'PolicyArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Policy** *(dict) --*

              Information about the specified AWS Firewall Manager policy.

              - **PolicyId** *(string) --*

                The ID of the AWS Firewall Manager policy.

              - **PolicyName** *(string) --*

                The friendly name of the AWS Firewall Manager policy.

              - **PolicyUpdateToken** *(string) --*

                A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request,
                the ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the
                current policy version. To get the ``PolicyUpdateToken`` of the current policy version, use
                a ``GetPolicy`` request.

              - **SecurityServicePolicyData** *(dict) --*

                Details about the security service that is being used to protect the resources.

                - **Type** *(string) --*

                  The service that the policy is using to protect the resources. This specifies the type of
                  policy that is created, either an AWS WAF policy, a Shield Advanced policy, or a security
                  group policy. For security group policies, Firewall Manager supports one security group
                  for each common policy and for each content audit policy. This is an adjustable limit
                  that you can increase by contacting AWS Support.

                - **ManagedServiceData** *(string) --*

                  Details about the service that are specific to the service type, in JSON format. For
                  service type ``SHIELD_ADVANCED`` , this is an empty string.

                  * Example: ``WAF``    ``ManagedServiceData": "{\\"type\\": \\"WAF\\", \\"ruleGroups\\":
                  [{\\"id\\": \\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" :
                  {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}``

                  * Example: ``SECURITY_GROUPS_COMMON``
                  ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_COMMON","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false,\\"securityGroups\\":[{\\"id\\":\\"
                  sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``
        sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``

                  * Example: ``SECURITY_GROUPS_CONTENT_AUDIT``
                  ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_CONTENT_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\"
                  sg-000e55995d61a06bd
                  \\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``
                    The security group action for content audit can be ``ALLOW`` or ``DENY`` . For
                    ``ALLOW`` , all in-scope security group rules must be within the allowed range of the
                    policy's security group rules. For ``DENY`` , all in-scope security group rules must
                    not contain a value or a range that matches a rule value or range in the policy
                    security group.

                  * Example: ``SECURITY_GROUPS_USAGE_AUDIT``
                  ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_USAGE_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"},"RemediationEnabled":false,"Resou
                  rceType":"AWS::EC2::SecurityGroup"}``

              - **ResourceType** *(string) --*

                The type of resource protected by or in scope of the policy. This is in the format shown in
                the `AWS Resource Types Reference
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
                . For AWS WAF and Shield Advanced, examples include
                ``AWS::ElasticLoadBalancingV2::LoadBalancer`` and ``AWS::CloudFront::Distribution`` . For a
                security group common policy, valid values are ``AWS::EC2::NetworkInterface`` and
                ``AWS::EC2::Instance`` . For a security group content audit policy, valid values are
                ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` .
                For a security group usage audit policy, the value is ``AWS::EC2::SecurityGroup`` .

              - **ResourceTypeList** *(list) --*

                An array of ``ResourceType`` .

                - *(string) --*

              - **ResourceTags** *(list) --*

                An array of ``ResourceTag`` objects.

                - *(dict) --*

                  The resource tags that AWS Firewall Manager uses to determine if a particular resource
                  should be included or excluded from the AWS Firewall Manager policy. Tags enable you to
                  categorize your AWS resources in different ways, for example, by purpose, owner, or
                  environment. Each tag consists of a key and an optional value. Firewall Manager combines
                  the tags with "AND" so that, if you add more than one tag to a policy scope, a resource
                  must have all the specified tags to be included or excluded. For more information, see
                  `Working with Tag Editor
                  <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .

                  - **Key** *(string) --*

                    The resource tag key.

                  - **Value** *(string) --*

                    The resource tag value.

              - **ExcludeResourceTags** *(boolean) --*

                If set to ``True`` , resources with the tags that are specified in the ``ResourceTag``
                array are not in scope of the policy. If set to ``False`` , and the ``ResourceTag`` array
                is not null, only resources with the specified tags are in scope of the policy.

              - **RemediationEnabled** *(boolean) --*

                Indicates if the policy should be automatically applied to new resources.

              - **IncludeMap** *(dict) --*

                Specifies the AWS account IDs to include in the policy. If ``IncludeMap`` is null, all
                accounts in the organization in AWS Organizations are included in the policy. If
                ``IncludeMap`` is not null, only values listed in ``IncludeMap`` are included in the policy.

                The key to the map is ``ACCOUNT`` . For example, a valid ``IncludeMap`` would be
                ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .

                - *(string) --*

                  - *(list) --*

                    - *(string) --*

              - **ExcludeMap** *(dict) --*

                Specifies the AWS account IDs to exclude from the policy. The ``IncludeMap`` values are
                evaluated first, with all the appropriate account IDs added to the policy. Then the
                accounts listed in ``ExcludeMap`` are removed, resulting in the final list of accounts to
                add to the policy.

                The key to the map is ``ACCOUNT`` . For example, a valid ``ExcludeMap`` would be
                ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .

                - *(string) --*

                  - *(list) --*

                    - *(string) --*

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN) of the specified policy.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_protection_status(
        self,
        PolicyId: str,
        MemberAccountId: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetProtectionStatusResponseTypeDef:
        """
        If you created a Shield Advanced policy, returns policy-level attack summary information in the
        event of a potential DDoS attack. Other policy types are currently unsupported.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetProtectionStatus>`_

        **Request Syntax**
        ::

          response = client.get_protection_status(
              PolicyId='string',
              MemberAccountId='string',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              NextToken='string',
              MaxResults=123
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]**

          The ID of the policy for which you want to get the attack information.

        :type MemberAccountId: string
        :param MemberAccountId:

          The AWS account that is in scope of the policy that you want to get the details for.

        :type StartTime: datetime
        :param StartTime:

          The start of the time period to query for the attacks. This is a ``timestamp`` type. The request
          syntax listing indicates a ``number`` type because the default used by AWS Firewall Manager is
          Unix time in seconds. However, any valid ``timestamp`` format is allowed.

        :type EndTime: datetime
        :param EndTime:

          The end of the time period to query for the attacks. This is a ``timestamp`` type. The request
          syntax listing indicates a ``number`` type because the default used by AWS Firewall Manager is
          Unix time in seconds. However, any valid ``timestamp`` format is allowed.

        :type NextToken: string
        :param NextToken:

          If you specify a value for ``MaxResults`` and you have more objects than the number that you
          specify for ``MaxResults`` , AWS Firewall Manager returns a ``NextToken`` value in the response,
          which you can use to retrieve another group of objects. For the second and subsequent
          ``GetProtectionStatus`` requests, specify the value of ``NextToken`` from the previous response
          to get information about another batch of objects.

        :type MaxResults: integer
        :param MaxResults:

          Specifies the number of objects that you want AWS Firewall Manager to return for this request. If
          you have more objects than the number that you specify for ``MaxResults`` , the response includes
          a ``NextToken`` value that you can use to get another batch of objects.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AdminAccountId': 'string',
                'ServiceType':
                'WAF'|'SHIELD_ADVANCED'|'SECURITY_GROUPS_COMMON'|'SECURITY_GROUPS_CONTENT_AUDIT'
                |'SECURITY_GROUPS_USAGE_AUDIT',
                'Data': 'string',
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AdminAccountId** *(string) --*

              The ID of the AWS Firewall administrator account for this policy.

            - **ServiceType** *(string) --*

              The service type that is protected by the policy. Currently, this is always
              ``SHIELD_ADVANCED`` .

            - **Data** *(string) --*

              Details about the attack, including the following:

              * Attack type

              * Account ID

              * ARN of the resource attacked

              * Start time of the attack

              * End time of the attack (ongoing attacks will not have an end time)

              The details are in JSON format.

            - **NextToken** *(string) --*

              If you have more objects than the number that you specified for ``MaxResults`` in the
              request, the response includes a ``NextToken`` value. To list more objects, submit another
              ``GetProtectionStatus`` request, and specify the ``NextToken`` value from the response in the
              ``NextToken`` value in the next request.

              AWS SDKs provide auto-pagination that identify ``NextToken`` in a response and make
              subsequent request calls automatically on your behalf. However, this feature is not supported
              by ``GetProtectionStatus`` . You must submit subsequent requests with ``NextToken`` using
              your own processes.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_compliance_status(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListComplianceStatusResponseTypeDef:
        """
        Returns an array of ``PolicyComplianceStatus`` objects in the response. Use
        ``PolicyComplianceStatus`` to get a summary of which member accounts are protected by the specified
        policy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListComplianceStatus>`_

        **Request Syntax**
        ::

          response = client.list_compliance_status(
              PolicyId='string',
              NextToken='string',
              MaxResults=123
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]**

          The ID of the AWS Firewall Manager policy that you want the details for.

        :type NextToken: string
        :param NextToken:

          If you specify a value for ``MaxResults`` and you have more ``PolicyComplianceStatus`` objects
          than the number that you specify for ``MaxResults`` , AWS Firewall Manager returns a
          ``NextToken`` value in the response that allows you to list another group of
          ``PolicyComplianceStatus`` objects. For the second and subsequent ``ListComplianceStatus``
          requests, specify the value of ``NextToken`` from the previous response to get information about
          another batch of ``PolicyComplianceStatus`` objects.

        :type MaxResults: integer
        :param MaxResults:

          Specifies the number of ``PolicyComplianceStatus`` objects that you want AWS Firewall Manager to
          return for this request. If you have more ``PolicyComplianceStatus`` objects than the number that
          you specify for ``MaxResults`` , the response includes a ``NextToken`` value that you can use to
          get another batch of ``PolicyComplianceStatus`` objects.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyComplianceStatusList': [
                    {
                        'PolicyOwner': 'string',
                        'PolicyId': 'string',
                        'PolicyName': 'string',
                        'MemberAccount': 'string',
                        'EvaluationResults': [
                            {
                                'ComplianceStatus': 'COMPLIANT'|'NON_COMPLIANT',
                                'ViolatorCount': 123,
                                'EvaluationLimitExceeded': True|False
                            },
                        ],
                        'LastUpdated': datetime(2015, 1, 1),
                        'IssueInfoMap': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyComplianceStatusList** *(list) --*

              An array of ``PolicyComplianceStatus`` objects.

              - *(dict) --*

                Indicates whether the account is compliant with the specified policy. An account is
                considered noncompliant if it includes resources that are not protected by the policy, for
                AWS WAF and Shield Advanced policies, or that are noncompliant with the policy, for
                security group policies.

                - **PolicyOwner** *(string) --*

                  The AWS account that created the AWS Firewall Manager policy.

                - **PolicyId** *(string) --*

                  The ID of the AWS Firewall Manager policy.

                - **PolicyName** *(string) --*

                  The friendly name of the AWS Firewall Manager policy.

                - **MemberAccount** *(string) --*

                  The member account ID.

                - **EvaluationResults** *(list) --*

                  An array of ``EvaluationResult`` objects.

                  - *(dict) --*

                    Describes the compliance status for the account. An account is considered noncompliant
                    if it includes resources that are not protected by the specified policy or that don't
                    comply with the policy.

                    - **ComplianceStatus** *(string) --*

                      Describes an AWS account's compliance with the AWS Firewall Manager policy.

                    - **ViolatorCount** *(integer) --*

                      The number of resources that are noncompliant with the specified policy. For AWS WAF
                      and Shield Advanced policies, a resource is considered noncompliant if it is not
                      associated with the policy. For security group policies, a resource is considered
                      noncompliant if it doesn't comply with the rules of the policy and remediation is
                      disabled or not possible.

                    - **EvaluationLimitExceeded** *(boolean) --*

                      Indicates that over 100 resources are noncompliant with the AWS Firewall Manager
                      policy.

                - **LastUpdated** *(datetime) --*

                  Timestamp of the last update to the ``EvaluationResult`` objects.

                - **IssueInfoMap** *(dict) --*

                  Details about problems with dependent services, such as AWS WAF or AWS Config, that are
                  causing a resource to be noncompliant. The details include the name of the dependent
                  service and the error message received that indicates the problem with the service.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              If you have more ``PolicyComplianceStatus`` objects than the number that you specified for
              ``MaxResults`` in the request, the response includes a ``NextToken`` value. To list more
              ``PolicyComplianceStatus`` objects, submit another ``ListComplianceStatus`` request, and
              specify the ``NextToken`` value from the response in the ``NextToken`` value in the next
              request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_member_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListMemberAccountsResponseTypeDef:
        """
        Returns a ``MemberAccounts`` object that lists the member accounts in the administrator's AWS
        organization.

        The ``ListMemberAccounts`` must be submitted by the account that is set as the AWS Firewall Manager
        administrator.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListMemberAccounts>`_

        **Request Syntax**
        ::

          response = client.list_member_accounts(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          If you specify a value for ``MaxResults`` and you have more account IDs than the number that you
          specify for ``MaxResults`` , AWS Firewall Manager returns a ``NextToken`` value in the response
          that allows you to list another group of IDs. For the second and subsequent
          ``ListMemberAccountsRequest`` requests, specify the value of ``NextToken`` from the previous
          response to get information about another batch of member account IDs.

        :type MaxResults: integer
        :param MaxResults:

          Specifies the number of member account IDs that you want AWS Firewall Manager to return for this
          request. If you have more IDs than the number that you specify for ``MaxResults`` , the response
          includes a ``NextToken`` value that you can use to get another batch of member account IDs.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MemberAccounts': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **MemberAccounts** *(list) --*

              An array of account IDs.

              - *(string) --*

            - **NextToken** *(string) --*

              If you have more member account IDs than the number that you specified for ``MaxResults`` in
              the request, the response includes a ``NextToken`` value. To list more IDs, submit another
              ``ListMemberAccounts`` request, and specify the ``NextToken`` value from the response in the
              ``NextToken`` value in the next request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_policies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListPoliciesResponseTypeDef:
        """
        Returns an array of ``PolicySummary`` objects in the response.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListPolicies>`_

        **Request Syntax**
        ::

          response = client.list_policies(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          If you specify a value for ``MaxResults`` and you have more ``PolicySummary`` objects than the
          number that you specify for ``MaxResults`` , AWS Firewall Manager returns a ``NextToken`` value
          in the response that allows you to list another group of ``PolicySummary`` objects. For the
          second and subsequent ``ListPolicies`` requests, specify the value of ``NextToken`` from the
          previous response to get information about another batch of ``PolicySummary`` objects.

        :type MaxResults: integer
        :param MaxResults:

          Specifies the number of ``PolicySummary`` objects that you want AWS Firewall Manager to return
          for this request. If you have more ``PolicySummary`` objects than the number that you specify for
          ``MaxResults`` , the response includes a ``NextToken`` value that you can use to get another
          batch of ``PolicySummary`` objects.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyList': [
                    {
                        'PolicyArn': 'string',
                        'PolicyId': 'string',
                        'PolicyName': 'string',
                        'ResourceType': 'string',
                        'SecurityServiceType':
                        'WAF'|'SHIELD_ADVANCED'|'SECURITY_GROUPS_COMMON'|'SECURITY_GROUPS_CONTENT_AUDIT'
                        |'SECURITY_GROUPS_USAGE_AUDIT',
                        'RemediationEnabled': True|False
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyList** *(list) --*

              An array of ``PolicySummary`` objects.

              - *(dict) --*

                Details of the AWS Firewall Manager policy.

                - **PolicyArn** *(string) --*

                  The Amazon Resource Name (ARN) of the specified policy.

                - **PolicyId** *(string) --*

                  The ID of the specified policy.

                - **PolicyName** *(string) --*

                  The friendly name of the specified policy.

                - **ResourceType** *(string) --*

                  The type of resource protected by or in scope of the policy. This is in the format shown
                  in the `AWS Resource Types Reference
                  <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
                  . For AWS WAF and Shield Advanced, examples include
                  ``AWS::ElasticLoadBalancingV2::LoadBalancer`` and ``AWS::CloudFront::Distribution`` . For
                  a security group common policy, valid values are ``AWS::EC2::NetworkInterface`` and
                  ``AWS::EC2::Instance`` . For a security group content audit policy, valid values are
                  ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance``
                  . For a security group usage audit policy, the value is ``AWS::EC2::SecurityGroup`` .

                - **SecurityServiceType** *(string) --*

                  The service that the policy is using to protect the resources. This specifies the type of
                  policy that is created, either an AWS WAF policy, a Shield Advanced policy, or a security
                  group policy.

                - **RemediationEnabled** *(boolean) --*

                  Indicates if the policy should be automatically applied to new resources.

            - **NextToken** *(string) --*

              If you have more ``PolicySummary`` objects than the number that you specified for
              ``MaxResults`` in the request, the response includes a ``NextToken`` value. To list more
              ``PolicySummary`` objects, submit another ``ListPolicies`` request, and specify the
              ``NextToken`` value from the response in the ``NextToken`` value in the next request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_notification_channel(self, SnsTopicArn: str, SnsRoleName: str) -> None:
        """
        Designates the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall
        Manager uses to record SNS logs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/PutNotificationChannel>`_

        **Request Syntax**
        ::

          response = client.put_notification_channel(
              SnsTopicArn='string',
              SnsRoleName='string'
          )
        :type SnsTopicArn: string
        :param SnsTopicArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall
          Manager.

        :type SnsRoleName: string
        :param SnsRoleName: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall
          Manager activity.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_policy(self, Policy: ClientPutPolicyPolicyTypeDef) -> Dict[str, Any]:
        """
        Creates an AWS Firewall Manager policy.

        Firewall Manager provides the following types of policies:

        * A Shield Advanced policy, which applies Shield Advanced protection to specified accounts and
        resources

        * An AWS WAF policy, which contains a rule group and defines which resources are to be protected by
        that rule group

        * A security group policy, which manages VPC security groups across your AWS organization.

        Each policy is specific to one of the three types. If you want to enforce more than one policy type
        across accounts, you can create multiple policies. You can create multiple policies for each type.

        You must be subscribed to Shield Advanced to create a Shield Advanced policy. For more information
        about subscribing to Shield Advanced, see `CreateSubscription
        <https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateSubscription.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/PutPolicy>`_

        **Request Syntax**
        ::

          response = client.put_policy(
              Policy={
                  'PolicyId': 'string',
                  'PolicyName': 'string',
                  'PolicyUpdateToken': 'string',
                  'SecurityServicePolicyData': {
                      'Type':
                      'WAF'|'SHIELD_ADVANCED'|'SECURITY_GROUPS_COMMON'|'SECURITY_GROUPS_CONTENT_AUDIT'
                      |'SECURITY_GROUPS_USAGE_AUDIT',
                      'ManagedServiceData': 'string'
                  },
                  'ResourceType': 'string',
                  'ResourceTypeList': [
                      'string',
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string'
                      },
                  ],
                  'ExcludeResourceTags': True|False,
                  'RemediationEnabled': True|False,
                  'IncludeMap': {
                      'string': [
                          'string',
                      ]
                  },
                  'ExcludeMap': {
                      'string': [
                          'string',
                      ]
                  }
              }
          )
        :type Policy: dict
        :param Policy: **[REQUIRED]**

          The details of the AWS Firewall Manager policy to be created.

          - **PolicyId** *(string) --*

            The ID of the AWS Firewall Manager policy.

          - **PolicyName** *(string) --* **[REQUIRED]**

            The friendly name of the AWS Firewall Manager policy.

          - **PolicyUpdateToken** *(string) --*

            A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request, the
            ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the current policy
            version. To get the ``PolicyUpdateToken`` of the current policy version, use a ``GetPolicy``
            request.

          - **SecurityServicePolicyData** *(dict) --* **[REQUIRED]**

            Details about the security service that is being used to protect the resources.

            - **Type** *(string) --* **[REQUIRED]**

              The service that the policy is using to protect the resources. This specifies the type of
              policy that is created, either an AWS WAF policy, a Shield Advanced policy, or a security
              group policy. For security group policies, Firewall Manager supports one security group for
              each common policy and for each content audit policy. This is an adjustable limit that you
              can increase by contacting AWS Support.

            - **ManagedServiceData** *(string) --*

              Details about the service that are specific to the service type, in JSON format. For service
              type ``SHIELD_ADVANCED`` , this is an empty string.

              * Example: ``WAF``    ``ManagedServiceData": "{\\"type\\": \\"WAF\\", \\"ruleGroups\\":
              [{\\"id\\": \\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\":
              \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}``

              * Example: ``SECURITY_GROUPS_COMMON``
              ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_COMMON","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false,\\"securityGroups\\":[{\\"id\\":\\"
              sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``
        sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``

              * Example: ``SECURITY_GROUPS_CONTENT_AUDIT``
              ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_CONTENT_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\"
              sg-000e55995d61a06bd
              \\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``
                The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` ,
                all in-scope security group rules must be within the allowed range of the policy's security
                group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a
                range that matches a rule value or range in the policy security group.

              * Example: ``SECURITY_GROUPS_USAGE_AUDIT``
              ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_USAGE_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"},"RemediationEnabled":false,"Resou
              rceType":"AWS::EC2::SecurityGroup"}``

          - **ResourceType** *(string) --* **[REQUIRED]**

            The type of resource protected by or in scope of the policy. This is in the format shown in the
            `AWS Resource Types Reference
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
            . For AWS WAF and Shield Advanced, examples include
            ``AWS::ElasticLoadBalancingV2::LoadBalancer`` and ``AWS::CloudFront::Distribution`` . For a
            security group common policy, valid values are ``AWS::EC2::NetworkInterface`` and
            ``AWS::EC2::Instance`` . For a security group content audit policy, valid values are
            ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` . For
            a security group usage audit policy, the value is ``AWS::EC2::SecurityGroup`` .

          - **ResourceTypeList** *(list) --*

            An array of ``ResourceType`` .

            - *(string) --*

          - **ResourceTags** *(list) --*

            An array of ``ResourceTag`` objects.

            - *(dict) --*

              The resource tags that AWS Firewall Manager uses to determine if a particular resource should
              be included or excluded from the AWS Firewall Manager policy. Tags enable you to categorize
              your AWS resources in different ways, for example, by purpose, owner, or environment. Each
              tag consists of a key and an optional value. Firewall Manager combines the tags with "AND" so
              that, if you add more than one tag to a policy scope, a resource must have all the specified
              tags to be included or excluded. For more information, see `Working with Tag Editor
              <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .

              - **Key** *(string) --* **[REQUIRED]**

                The resource tag key.

              - **Value** *(string) --*

                The resource tag value.

          - **ExcludeResourceTags** *(boolean) --* **[REQUIRED]**

            If set to ``True`` , resources with the tags that are specified in the ``ResourceTag`` array
            are not in scope of the policy. If set to ``False`` , and the ``ResourceTag`` array is not
            null, only resources with the specified tags are in scope of the policy.

          - **RemediationEnabled** *(boolean) --* **[REQUIRED]**

            Indicates if the policy should be automatically applied to new resources.

          - **IncludeMap** *(dict) --*

            Specifies the AWS account IDs to include in the policy. If ``IncludeMap`` is null, all accounts
            in the organization in AWS Organizations are included in the policy. If ``IncludeMap`` is not
            null, only values listed in ``IncludeMap`` are included in the policy.

            The key to the map is ``ACCOUNT`` . For example, a valid ``IncludeMap`` would be ``{“ACCOUNT” :
            [“accountID1”, “accountID2”]}`` .

            - *(string) --*

              - *(list) --*

                - *(string) --*

          - **ExcludeMap** *(dict) --*

            Specifies the AWS account IDs to exclude from the policy. The ``IncludeMap`` values are
            evaluated first, with all the appropriate account IDs added to the policy. Then the accounts
            listed in ``ExcludeMap`` are removed, resulting in the final list of accounts to add to the
            policy.

            The key to the map is ``ACCOUNT`` . For example, a valid ``ExcludeMap`` would be ``{“ACCOUNT” :
            [“accountID1”, “accountID2”]}`` .

            - *(string) --*

              - *(list) --*

                - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Policy': {
                    'PolicyId': 'string',
                    'PolicyName': 'string',
                    'PolicyUpdateToken': 'string',
                    'SecurityServicePolicyData': {
                        'Type':
                        'WAF'|'SHIELD_ADVANCED'|'SECURITY_GROUPS_COMMON'|'SECURITY_GROUPS_CONTENT_AUDIT'
                        |'SECURITY_GROUPS_USAGE_AUDIT',
                        'ManagedServiceData': 'string'
                    },
                    'ResourceType': 'string',
                    'ResourceTypeList': [
                        'string',
                    ],
                    'ResourceTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'ExcludeResourceTags': True|False,
                    'RemediationEnabled': True|False,
                    'IncludeMap': {
                        'string': [
                            'string',
                        ]
                    },
                    'ExcludeMap': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'PolicyArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Policy** *(dict) --*

              The details of the AWS Firewall Manager policy that was created.

              - **PolicyId** *(string) --*

                The ID of the AWS Firewall Manager policy.

              - **PolicyName** *(string) --*

                The friendly name of the AWS Firewall Manager policy.

              - **PolicyUpdateToken** *(string) --*

                A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request,
                the ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the
                current policy version. To get the ``PolicyUpdateToken`` of the current policy version, use
                a ``GetPolicy`` request.

              - **SecurityServicePolicyData** *(dict) --*

                Details about the security service that is being used to protect the resources.

                - **Type** *(string) --*

                  The service that the policy is using to protect the resources. This specifies the type of
                  policy that is created, either an AWS WAF policy, a Shield Advanced policy, or a security
                  group policy. For security group policies, Firewall Manager supports one security group
                  for each common policy and for each content audit policy. This is an adjustable limit
                  that you can increase by contacting AWS Support.

                - **ManagedServiceData** *(string) --*

                  Details about the service that are specific to the service type, in JSON format. For
                  service type ``SHIELD_ADVANCED`` , this is an empty string.

                  * Example: ``WAF``    ``ManagedServiceData": "{\\"type\\": \\"WAF\\", \\"ruleGroups\\":
                  [{\\"id\\": \\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" :
                  {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}``

                  * Example: ``SECURITY_GROUPS_COMMON``
                  ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_COMMON","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false,\\"securityGroups\\":[{\\"id\\":\\"
                  sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``
        sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``

                  * Example: ``SECURITY_GROUPS_CONTENT_AUDIT``
                  ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_CONTENT_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\"
                  sg-000e55995d61a06bd
                  \\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``
                    The security group action for content audit can be ``ALLOW`` or ``DENY`` . For
                    ``ALLOW`` , all in-scope security group rules must be within the allowed range of the
                    policy's security group rules. For ``DENY`` , all in-scope security group rules must
                    not contain a value or a range that matches a rule value or range in the policy
                    security group.

                  * Example: ``SECURITY_GROUPS_USAGE_AUDIT``
                  ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_USAGE_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"},"RemediationEnabled":false,"Resou
                  rceType":"AWS::EC2::SecurityGroup"}``

              - **ResourceType** *(string) --*

                The type of resource protected by or in scope of the policy. This is in the format shown in
                the `AWS Resource Types Reference
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
                . For AWS WAF and Shield Advanced, examples include
                ``AWS::ElasticLoadBalancingV2::LoadBalancer`` and ``AWS::CloudFront::Distribution`` . For a
                security group common policy, valid values are ``AWS::EC2::NetworkInterface`` and
                ``AWS::EC2::Instance`` . For a security group content audit policy, valid values are
                ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` .
                For a security group usage audit policy, the value is ``AWS::EC2::SecurityGroup`` .

              - **ResourceTypeList** *(list) --*

                An array of ``ResourceType`` .

                - *(string) --*

              - **ResourceTags** *(list) --*

                An array of ``ResourceTag`` objects.

                - *(dict) --*

                  The resource tags that AWS Firewall Manager uses to determine if a particular resource
                  should be included or excluded from the AWS Firewall Manager policy. Tags enable you to
                  categorize your AWS resources in different ways, for example, by purpose, owner, or
                  environment. Each tag consists of a key and an optional value. Firewall Manager combines
                  the tags with "AND" so that, if you add more than one tag to a policy scope, a resource
                  must have all the specified tags to be included or excluded. For more information, see
                  `Working with Tag Editor
                  <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .

                  - **Key** *(string) --*

                    The resource tag key.

                  - **Value** *(string) --*

                    The resource tag value.

              - **ExcludeResourceTags** *(boolean) --*

                If set to ``True`` , resources with the tags that are specified in the ``ResourceTag``
                array are not in scope of the policy. If set to ``False`` , and the ``ResourceTag`` array
                is not null, only resources with the specified tags are in scope of the policy.

              - **RemediationEnabled** *(boolean) --*

                Indicates if the policy should be automatically applied to new resources.

              - **IncludeMap** *(dict) --*

                Specifies the AWS account IDs to include in the policy. If ``IncludeMap`` is null, all
                accounts in the organization in AWS Organizations are included in the policy. If
                ``IncludeMap`` is not null, only values listed in ``IncludeMap`` are included in the policy.

                The key to the map is ``ACCOUNT`` . For example, a valid ``IncludeMap`` would be
                ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .

                - *(string) --*

                  - *(list) --*

                    - *(string) --*

              - **ExcludeMap** *(dict) --*

                Specifies the AWS account IDs to exclude from the policy. The ``IncludeMap`` values are
                evaluated first, with all the appropriate account IDs added to the policy. Then the
                accounts listed in ``ExcludeMap`` are removed, resulting in the final list of accounts to
                add to the policy.

                The key to the map is ``ACCOUNT`` . For example, a valid ``ExcludeMap`` would be
                ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .

                - *(string) --*

                  - *(list) --*

                    - *(string) --*

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN) of the policy that was created.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_compliance_status"]
    ) -> paginator_scope.ListComplianceStatusPaginator:
        """
        Get Paginator for `list_compliance_status` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> paginator_scope.ListMemberAccountsPaginator:
        """
        Get Paginator for `list_member_accounts` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_policies"]
    ) -> paginator_scope.ListPoliciesPaginator:
        """
        Get Paginator for `list_policies` operation.
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
    ClientError: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidTypeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
