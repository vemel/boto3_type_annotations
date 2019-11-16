"Main interface for fms Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_fms.type_defs import (
    ListComplianceStatusPaginatePaginationConfigTypeDef,
    ListComplianceStatusPaginateResponseTypeDef,
    ListMemberAccountsPaginatePaginationConfigTypeDef,
    ListMemberAccountsPaginateResponseTypeDef,
    ListPoliciesPaginatePaginationConfigTypeDef,
    ListPoliciesPaginateResponseTypeDef,
)


__all__ = (
    "ListComplianceStatusPaginator",
    "ListMemberAccountsPaginator",
    "ListPoliciesPaginator",
)


class ListComplianceStatusPaginator(Boto3Paginator):
    """
    Paginator for `list_compliance_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicyId: str,
        PaginationConfig: ListComplianceStatusPaginatePaginationConfigTypeDef = None,
    ) -> ListComplianceStatusPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`FMS.Client.list_compliance_status`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListComplianceStatus>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PolicyId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]**

          The ID of the AWS Firewall Manager policy that you want the details for.

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

        """


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    Paginator for `list_member_accounts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListMemberAccountsPaginatePaginationConfigTypeDef = None
    ) -> ListMemberAccountsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`FMS.Client.list_member_accounts`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListMemberAccounts>`_

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
                'MemberAccounts': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **MemberAccounts** *(list) --*

              An array of account IDs.

              - *(string) --*

        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPoliciesPaginatePaginationConfigTypeDef = None
    ) -> ListPoliciesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`FMS.Client.list_policies`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListPolicies>`_

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

        """
