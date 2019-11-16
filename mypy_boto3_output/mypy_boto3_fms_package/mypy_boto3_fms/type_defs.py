"Main interface for fms type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientGetAdminAccountResponseTypeDef",
    "ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef",
    "ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef",
    "ClientGetComplianceDetailResponseTypeDef",
    "ClientGetNotificationChannelResponseTypeDef",
    "ClientGetProtectionStatusResponseTypeDef",
    "ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    "ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef",
    "ClientListComplianceStatusResponseTypeDef",
    "ClientListMemberAccountsResponseTypeDef",
    "ClientListPoliciesResponsePolicyListTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientPutPolicyPolicySecurityServicePolicyDataTypeDef",
    "ClientPutPolicyPolicyTypeDef",
    "ListComplianceStatusPaginatePaginationConfigTypeDef",
    "ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    "ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef",
    "ListComplianceStatusPaginateResponseTypeDef",
    "ListMemberAccountsPaginatePaginationConfigTypeDef",
    "ListMemberAccountsPaginateResponseTypeDef",
    "ListPoliciesPaginatePaginationConfigTypeDef",
    "ListPoliciesPaginateResponsePolicyListTypeDef",
    "ListPoliciesPaginateResponseTypeDef",
)


_ClientGetAdminAccountResponseTypeDef = TypedDict(
    "_ClientGetAdminAccountResponseTypeDef",
    {"AdminAccount": str, "RoleStatus": str},
    total=False,
)


class ClientGetAdminAccountResponseTypeDef(_ClientGetAdminAccountResponseTypeDef):
    """
    Type definition for `ClientGetAdminAccount` `Response`

    - **AdminAccount** *(string) --*

      The AWS account that is set as the AWS Firewall Manager administrator.

    - **RoleStatus** *(string) --*

      The status of the AWS account that you set as the AWS Firewall Manager administrator.
    """


_ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef = TypedDict(
    "_ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef",
    {"ResourceId": str, "ViolationReason": str, "ResourceType": str},
    total=False,
)


class ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef(
    _ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailResponsePolicyComplianceDetail` `Violators`

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
    """


_ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef = TypedDict(
    "_ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "MemberAccount": str,
        "Violators": List[
            ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef
        ],
        "EvaluationLimitExceeded": bool,
        "ExpiredAt": datetime,
        "IssueInfoMap": Dict[str, str],
    },
    total=False,
)


class ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef(
    _ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailResponse` `PolicyComplianceDetail`

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


_ClientGetComplianceDetailResponseTypeDef = TypedDict(
    "_ClientGetComplianceDetailResponseTypeDef",
    {
        "PolicyComplianceDetail": ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef
    },
    total=False,
)


class ClientGetComplianceDetailResponseTypeDef(
    _ClientGetComplianceDetailResponseTypeDef
):
    """
    Type definition for `ClientGetComplianceDetail` `Response`

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


_ClientGetNotificationChannelResponseTypeDef = TypedDict(
    "_ClientGetNotificationChannelResponseTypeDef",
    {"SnsTopicArn": str, "SnsRoleName": str},
    total=False,
)


class ClientGetNotificationChannelResponseTypeDef(
    _ClientGetNotificationChannelResponseTypeDef
):
    """
    Type definition for `ClientGetNotificationChannel` `Response`

    - **SnsTopicArn** *(string) --*

      The SNS topic that records AWS Firewall Manager activity.

    - **SnsRoleName** *(string) --*

      The IAM role that is used by AWS Firewall Manager to record activity to SNS.
    """


_ClientGetProtectionStatusResponseTypeDef = TypedDict(
    "_ClientGetProtectionStatusResponseTypeDef",
    {"AdminAccountId": str, "ServiceType": str, "Data": str, "NextToken": str},
    total=False,
)


class ClientGetProtectionStatusResponseTypeDef(
    _ClientGetProtectionStatusResponseTypeDef
):
    """
    Type definition for `ClientGetProtectionStatus` `Response`

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


_ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef = TypedDict(
    "_ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    {"ComplianceStatus": str, "ViolatorCount": int, "EvaluationLimitExceeded": bool},
    total=False,
)


class ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef(
    _ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef
):
    """
    Type definition for `ClientListComplianceStatusResponsePolicyComplianceStatusList` `EvaluationResults`

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
    """


_ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef = TypedDict(
    "_ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List[
            ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef
        ],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[str, str],
    },
    total=False,
)


class ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef(
    _ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef
):
    """
    Type definition for `ClientListComplianceStatusResponse` `PolicyComplianceStatusList`

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
    """


_ClientListComplianceStatusResponseTypeDef = TypedDict(
    "_ClientListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[
            ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListComplianceStatusResponseTypeDef(
    _ClientListComplianceStatusResponseTypeDef
):
    """
    Type definition for `ClientListComplianceStatus` `Response`

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


_ClientListMemberAccountsResponseTypeDef = TypedDict(
    "_ClientListMemberAccountsResponseTypeDef",
    {"MemberAccounts": List[str], "NextToken": str},
    total=False,
)


class ClientListMemberAccountsResponseTypeDef(_ClientListMemberAccountsResponseTypeDef):
    """
    Type definition for `ClientListMemberAccounts` `Response`

    - **MemberAccounts** *(list) --*

      An array of account IDs.

      - *(string) --*

    - **NextToken** *(string) --*

      If you have more member account IDs than the number that you specified for ``MaxResults`` in
      the request, the response includes a ``NextToken`` value. To list more IDs, submit another
      ``ListMemberAccounts`` request, and specify the ``NextToken`` value from the response in the
      ``NextToken`` value in the next request.
    """


_ClientListPoliciesResponsePolicyListTypeDef = TypedDict(
    "_ClientListPoliciesResponsePolicyListTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": str,
        "RemediationEnabled": bool,
    },
    total=False,
)


class ClientListPoliciesResponsePolicyListTypeDef(
    _ClientListPoliciesResponsePolicyListTypeDef
):
    """
    Type definition for `ClientListPoliciesResponse` `PolicyList`

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
    """


_ClientListPoliciesResponseTypeDef = TypedDict(
    "_ClientListPoliciesResponseTypeDef",
    {"PolicyList": List[ClientListPoliciesResponsePolicyListTypeDef], "NextToken": str},
    total=False,
)


class ClientListPoliciesResponseTypeDef(_ClientListPoliciesResponseTypeDef):
    """
    Type definition for `ClientListPolicies` `Response`

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


_RequiredClientPutPolicyPolicySecurityServicePolicyDataTypeDef = TypedDict(
    "_RequiredClientPutPolicyPolicySecurityServicePolicyDataTypeDef", {"Type": str}
)
_OptionalClientPutPolicyPolicySecurityServicePolicyDataTypeDef = TypedDict(
    "_OptionalClientPutPolicyPolicySecurityServicePolicyDataTypeDef",
    {"ManagedServiceData": str},
    total=False,
)


class ClientPutPolicyPolicySecurityServicePolicyDataTypeDef(
    _RequiredClientPutPolicyPolicySecurityServicePolicyDataTypeDef,
    _OptionalClientPutPolicyPolicySecurityServicePolicyDataTypeDef,
):
    """
    Type definition for `ClientPutPolicyPolicy` `SecurityServicePolicyData`

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
    """


_RequiredClientPutPolicyPolicyTypeDef = TypedDict(
    "_RequiredClientPutPolicyPolicyTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": ClientPutPolicyPolicySecurityServicePolicyDataTypeDef,
    },
)
_OptionalClientPutPolicyPolicyTypeDef = TypedDict(
    "_OptionalClientPutPolicyPolicyTypeDef",
    {"PolicyId": str, "PolicyUpdateToken": str},
    total=False,
)


class ClientPutPolicyPolicyTypeDef(
    _RequiredClientPutPolicyPolicyTypeDef, _OptionalClientPutPolicyPolicyTypeDef
):
    """
    Type definition for `ClientPutPolicy` `Policy`

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
    """


_ListComplianceStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_ListComplianceStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListComplianceStatusPaginatePaginationConfigTypeDef(
    _ListComplianceStatusPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListComplianceStatusPaginate` `PaginationConfig`

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


_ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef = TypedDict(
    "_ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    {"ComplianceStatus": str, "ViolatorCount": int, "EvaluationLimitExceeded": bool},
    total=False,
)


class ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef(
    _ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef
):
    """
    Type definition for `ListComplianceStatusPaginateResponsePolicyComplianceStatusList` `EvaluationResults`

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
    """


_ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef = TypedDict(
    "_ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List[
            ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef
        ],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[str, str],
    },
    total=False,
)


class ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef(
    _ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef
):
    """
    Type definition for `ListComplianceStatusPaginateResponse` `PolicyComplianceStatusList`

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
    """


_ListComplianceStatusPaginateResponseTypeDef = TypedDict(
    "_ListComplianceStatusPaginateResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[
            ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef
        ]
    },
    total=False,
)


class ListComplianceStatusPaginateResponseTypeDef(
    _ListComplianceStatusPaginateResponseTypeDef
):
    """
    Type definition for `ListComplianceStatusPaginate` `Response`

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
    """


_ListMemberAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMemberAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMemberAccountsPaginatePaginationConfigTypeDef(
    _ListMemberAccountsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMemberAccountsPaginate` `PaginationConfig`

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


_ListMemberAccountsPaginateResponseTypeDef = TypedDict(
    "_ListMemberAccountsPaginateResponseTypeDef",
    {"MemberAccounts": List[str]},
    total=False,
)


class ListMemberAccountsPaginateResponseTypeDef(
    _ListMemberAccountsPaginateResponseTypeDef
):
    """
    Type definition for `ListMemberAccountsPaginate` `Response`

    - **MemberAccounts** *(list) --*

      An array of account IDs.

      - *(string) --*
    """


_ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPoliciesPaginatePaginationConfigTypeDef(
    _ListPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPoliciesPaginate` `PaginationConfig`

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


_ListPoliciesPaginateResponsePolicyListTypeDef = TypedDict(
    "_ListPoliciesPaginateResponsePolicyListTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": str,
        "RemediationEnabled": bool,
    },
    total=False,
)


class ListPoliciesPaginateResponsePolicyListTypeDef(
    _ListPoliciesPaginateResponsePolicyListTypeDef
):
    """
    Type definition for `ListPoliciesPaginateResponse` `PolicyList`

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
    """


_ListPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesPaginateResponseTypeDef",
    {"PolicyList": List[ListPoliciesPaginateResponsePolicyListTypeDef]},
    total=False,
)


class ListPoliciesPaginateResponseTypeDef(_ListPoliciesPaginateResponseTypeDef):
    """
    Type definition for `ListPoliciesPaginate` `Response`

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
    """
