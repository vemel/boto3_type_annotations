"Main interface for service-quotas Client"
from __future__ import annotations

from typing import Any, Dict
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_service_quotas.client as client_scope

# pylint: disable=import-self
import mypy_boto3_service_quotas.paginator as paginator_scope
from mypy_boto3_service_quotas.type_defs import (
    ClientGetAssociationForServiceQuotaTemplateResponseTypeDef,
    ClientGetAwsDefaultServiceQuotaResponseTypeDef,
    ClientGetRequestedServiceQuotaChangeResponseTypeDef,
    ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef,
    ClientGetServiceQuotaResponseTypeDef,
    ClientListAwsDefaultServiceQuotasResponseTypeDef,
    ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ClientListServiceQuotasResponseTypeDef,
    ClientListServicesResponseTypeDef,
    ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef,
    ClientRequestServiceQuotaIncreaseResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_service_quota_template(
        self, *args: Any, **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Associates the Service Quotas template with your organization so that when new accounts are created
        in your organization, the template submits increase requests for the specified service quotas. Use
        the Service Quotas template to request an increase for any adjustable quota value. After you define
        the Service Quotas template, use this operation to associate, or enable, the template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/AssociateServiceQuotaTemplate>`_

        **Request Syntax**
        ::

          response = client.associate_service_quota_template()

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
    def delete_service_quota_increase_request_from_template(
        self, ServiceCode: str, QuotaCode: str, AwsRegion: str
    ) -> Dict[str, Any]:
        """
        Removes a service quota increase request from the Service Quotas template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/DeleteServiceQuotaIncreaseRequestFromTemplate>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/DeleteServiceQuotaIncreaseRequestFromTemplate>`_

        **Request Syntax**
        ::

          response = client.delete_service_quota_increase_request_from_template(
              ServiceCode='string',
              QuotaCode='string',
              AwsRegion='string'
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the code for the service that you want to delete.

        :type QuotaCode: string
        :param QuotaCode: **[REQUIRED]**

          Specifies the code for the quota that you want to delete.

        :type AwsRegion: string
        :param AwsRegion: **[REQUIRED]**

          Specifies the AWS Region for the quota that you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_service_quota_template(
        self, *args: Any, **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Disables the Service Quotas template. Once the template is disabled, it does not request quota
        increases for new accounts in your organization. Disabling the quota template does not apply the
        quota increase requests from the template.

         **Related operations**

        * To enable the quota template, call  AssociateServiceQuotaTemplate .

        * To delete a specific service quota from the template, use
        DeleteServiceQuotaIncreaseRequestFromTemplate .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate>`_

        **Request Syntax**
        ::

          response = client.disassociate_service_quota_template()

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
    def get_association_for_service_quota_template(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAssociationForServiceQuotaTemplateResponseTypeDef:
        """
        Retrieves the ``ServiceQuotaTemplateAssociationStatus`` value from the service. Use this action to
        determine if the Service Quota template is associated, or enabled.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/GetAssociationForServiceQuotaTemplate>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/GetAssociationForServiceQuotaTemplate>`_

        **Request Syntax**
        ::

          response = client.get_association_for_service_quota_template()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ServiceQuotaTemplateAssociationStatus': 'ASSOCIATED'|'DISASSOCIATED'
            }
          **Response Structure**

          - *(dict) --*

            - **ServiceQuotaTemplateAssociationStatus** *(string) --*

              Specifies whether the template is ``ASSOCIATED`` or ``DISASSOCIATED`` . If the template is
              ``ASSOCIATED`` , then it requests service quota increases for all new accounts created in
              your organization.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_aws_default_service_quota(
        self, ServiceCode: str, QuotaCode: str
    ) -> ClientGetAwsDefaultServiceQuotaResponseTypeDef:
        """
        Retrieves the default service quotas values. The Value returned for each quota is the AWS default
        value, even if the quotas have been increased..

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/GetAWSDefaultServiceQuota>`_

        **Request Syntax**
        ::

          response = client.get_aws_default_service_quota(
              ServiceCode='string',
              QuotaCode='string'
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the service that you want to use.

        :type QuotaCode: string
        :param QuotaCode: **[REQUIRED]**

          Identifies the service quota you want to select.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Quota': {
                    'ServiceCode': 'string',
                    'ServiceName': 'string',
                    'QuotaArn': 'string',
                    'QuotaCode': 'string',
                    'QuotaName': 'string',
                    'Value': 123.0,
                    'Unit': 'string',
                    'Adjustable': True|False,
                    'GlobalQuota': True|False,
                    'UsageMetric': {
                        'MetricNamespace': 'string',
                        'MetricName': 'string',
                        'MetricDimensions': {
                            'string': 'string'
                        },
                        'MetricStatisticRecommendation': 'string'
                    },
                    'Period': {
                        'PeriodValue': 123,
                        'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
                    },
                    'ErrorReason': {
                        'ErrorCode':
                        'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'
                        |'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                        'ErrorMessage': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Quota** *(dict) --*

              Returns the  ServiceQuota object which contains all values for a quota.

              - **ServiceCode** *(string) --*

                Specifies the service that you want to use.

              - **ServiceName** *(string) --*

                The name of the AWS service specified in the increase request.

              - **QuotaArn** *(string) --*

                The Amazon Resource Name (ARN) of the service quota.

              - **QuotaCode** *(string) --*

                The code identifier for the service quota specified.

              - **QuotaName** *(string) --*

                The name identifier of the service quota.

              - **Value** *(float) --*

                The value of service quota.

              - **Unit** *(string) --*

                The unit of measurement for the value of the service quota.

              - **Adjustable** *(boolean) --*

                Specifies if the quota value can be increased.

              - **GlobalQuota** *(boolean) --*

                Specifies if the quota is global.

              - **UsageMetric** *(dict) --*

                Specifies the details about the measurement.

                - **MetricNamespace** *(string) --*

                  The namespace of the metric. The namespace is a container for CloudWatch metrics. You can
                  specify a name for the namespace when you create a metric.

                - **MetricName** *(string) --*

                  The name of the CloudWatch metric that measures usage of a service quota. This is a
                  required field.

                - **MetricDimensions** *(dict) --*

                  A dimension is a name/value pair that is part of the identity of a metric. Every metric
                  has specific characteristics that describe it, and you can think of dimensions as
                  categories for those characteristics. These dimensions are part of the CloudWatch Metric
                  Identity that measures usage against a particular service quota.

                  - *(string) --*

                    - *(string) --*

                - **MetricStatisticRecommendation** *(string) --*

                  Statistics are metric data aggregations over specified periods of time. This is the
                  recommended statistic to use when comparing usage in the CloudWatch Metric against your
                  Service Quota.

              - **Period** *(dict) --*

                Identifies the unit and value of how time is measured.

                - **PeriodValue** *(integer) --*

                  The value of a period.

                - **PeriodUnit** *(string) --*

                  The time unit of a period.

              - **ErrorReason** *(dict) --*

                Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

                - **ErrorCode** *(string) --*

                  Service Quotas returns the following error values.

                   ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have permission
                   to call the service or service quota. To resolve the error, you need permission to
                   access the service or service quota.

                   ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is throttling
                   Service Quotas.

                   ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has availability
                   issues.

                   ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
                   Quotas.

                - **ErrorMessage** *(string) --*

                  The error message that provides more detail.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_requested_service_quota_change(
        self, RequestId: str
    ) -> ClientGetRequestedServiceQuotaChangeResponseTypeDef:
        """
        Retrieves the details for a particular increase request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/GetRequestedServiceQuotaChange>`_

        **Request Syntax**
        ::

          response = client.get_requested_service_quota_change(
              RequestId='string'
          )
        :type RequestId: string
        :param RequestId: **[REQUIRED]**

          Identifies the quota increase request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestedQuota': {
                    'Id': 'string',
                    'CaseId': 'string',
                    'ServiceCode': 'string',
                    'ServiceName': 'string',
                    'QuotaCode': 'string',
                    'QuotaName': 'string',
                    'DesiredValue': 123.0,
                    'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
                    'Created': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'Requester': 'string',
                    'QuotaArn': 'string',
                    'GlobalQuota': True|False,
                    'Unit': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **RequestedQuota** *(dict) --*

              Returns the ``RequestedServiceQuotaChange`` object for the specific increase request.

              - **Id** *(string) --*

                The unique identifier of a requested service quota change.

              - **CaseId** *(string) --*

                The case Id for the service quota increase request.

              - **ServiceCode** *(string) --*

                Specifies the service that you want to use.

              - **ServiceName** *(string) --*

                The name of the AWS service specified in the increase request.

              - **QuotaCode** *(string) --*

                Specifies the service quota that you want to use.

              - **QuotaName** *(string) --*

                Name of the service quota.

              - **DesiredValue** *(float) --*

                New increased value for the service quota.

              - **Status** *(string) --*

                State of the service quota increase request.

              - **Created** *(datetime) --*

                The date and time when the service quota increase request was received and the case Id was
                created.

              - **LastUpdated** *(datetime) --*

                The date and time of the most recent change in the service quota increase request.

              - **Requester** *(string) --*

                The IAM identity who submitted the service quota increase request.

              - **QuotaArn** *(string) --*

                The Amazon Resource Name (ARN) of the service quota.

              - **GlobalQuota** *(boolean) --*

                Identifies if the quota is global.

              - **Unit** *(string) --*

                Specifies the unit used for the quota.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_quota(
        self, ServiceCode: str, QuotaCode: str
    ) -> ClientGetServiceQuotaResponseTypeDef:
        """
        Returns the details for the specified service quota. This operation provides a different Value than
        the ``GetAWSDefaultServiceQuota`` operation. This operation returns the applied value for each
        quota. ``GetAWSDefaultServiceQuota`` returns the default AWS value for each quota.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/GetServiceQuota>`_

        **Request Syntax**
        ::

          response = client.get_service_quota(
              ServiceCode='string',
              QuotaCode='string'
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the service that you want to use.

        :type QuotaCode: string
        :param QuotaCode: **[REQUIRED]**

          Identifies the service quota you want to select.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Quota': {
                    'ServiceCode': 'string',
                    'ServiceName': 'string',
                    'QuotaArn': 'string',
                    'QuotaCode': 'string',
                    'QuotaName': 'string',
                    'Value': 123.0,
                    'Unit': 'string',
                    'Adjustable': True|False,
                    'GlobalQuota': True|False,
                    'UsageMetric': {
                        'MetricNamespace': 'string',
                        'MetricName': 'string',
                        'MetricDimensions': {
                            'string': 'string'
                        },
                        'MetricStatisticRecommendation': 'string'
                    },
                    'Period': {
                        'PeriodValue': 123,
                        'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
                    },
                    'ErrorReason': {
                        'ErrorCode':
                        'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'
                        |'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                        'ErrorMessage': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Quota** *(dict) --*

              Returns the  ServiceQuota object which contains all values for a quota.

              - **ServiceCode** *(string) --*

                Specifies the service that you want to use.

              - **ServiceName** *(string) --*

                The name of the AWS service specified in the increase request.

              - **QuotaArn** *(string) --*

                The Amazon Resource Name (ARN) of the service quota.

              - **QuotaCode** *(string) --*

                The code identifier for the service quota specified.

              - **QuotaName** *(string) --*

                The name identifier of the service quota.

              - **Value** *(float) --*

                The value of service quota.

              - **Unit** *(string) --*

                The unit of measurement for the value of the service quota.

              - **Adjustable** *(boolean) --*

                Specifies if the quota value can be increased.

              - **GlobalQuota** *(boolean) --*

                Specifies if the quota is global.

              - **UsageMetric** *(dict) --*

                Specifies the details about the measurement.

                - **MetricNamespace** *(string) --*

                  The namespace of the metric. The namespace is a container for CloudWatch metrics. You can
                  specify a name for the namespace when you create a metric.

                - **MetricName** *(string) --*

                  The name of the CloudWatch metric that measures usage of a service quota. This is a
                  required field.

                - **MetricDimensions** *(dict) --*

                  A dimension is a name/value pair that is part of the identity of a metric. Every metric
                  has specific characteristics that describe it, and you can think of dimensions as
                  categories for those characteristics. These dimensions are part of the CloudWatch Metric
                  Identity that measures usage against a particular service quota.

                  - *(string) --*

                    - *(string) --*

                - **MetricStatisticRecommendation** *(string) --*

                  Statistics are metric data aggregations over specified periods of time. This is the
                  recommended statistic to use when comparing usage in the CloudWatch Metric against your
                  Service Quota.

              - **Period** *(dict) --*

                Identifies the unit and value of how time is measured.

                - **PeriodValue** *(integer) --*

                  The value of a period.

                - **PeriodUnit** *(string) --*

                  The time unit of a period.

              - **ErrorReason** *(dict) --*

                Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

                - **ErrorCode** *(string) --*

                  Service Quotas returns the following error values.

                   ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have permission
                   to call the service or service quota. To resolve the error, you need permission to
                   access the service or service quota.

                   ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is throttling
                   Service Quotas.

                   ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has availability
                   issues.

                   ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
                   Quotas.

                - **ErrorMessage** *(string) --*

                  The error message that provides more detail.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_quota_increase_request_from_template(
        self, ServiceCode: str, QuotaCode: str, AwsRegion: str
    ) -> ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef:
        """
        Returns the details of the service quota increase request in your template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate>`_

        **Request Syntax**
        ::

          response = client.get_service_quota_increase_request_from_template(
              ServiceCode='string',
              QuotaCode='string',
              AwsRegion='string'
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the service that you want to use.

        :type QuotaCode: string
        :param QuotaCode: **[REQUIRED]**

          Specifies the quota you want.

        :type AwsRegion: string
        :param AwsRegion: **[REQUIRED]**

          Specifies the AWS Region for the quota that you want to use.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ServiceQuotaIncreaseRequestInTemplate': {
                    'ServiceCode': 'string',
                    'ServiceName': 'string',
                    'QuotaCode': 'string',
                    'QuotaName': 'string',
                    'DesiredValue': 123.0,
                    'AwsRegion': 'string',
                    'Unit': 'string',
                    'GlobalQuota': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ServiceQuotaIncreaseRequestInTemplate** *(dict) --*

              This object contains the details about the quota increase request.

              - **ServiceCode** *(string) --*

                The code identifier for the AWS service specified in the increase request.

              - **ServiceName** *(string) --*

                The name of the AWS service specified in the increase request.

              - **QuotaCode** *(string) --*

                The code identifier for the service quota specified in the increase request.

              - **QuotaName** *(string) --*

                The name of the service quota in the increase request.

              - **DesiredValue** *(float) --*

                Identifies the new, increased value of the service quota in the increase request.

              - **AwsRegion** *(string) --*

                The AWS Region where the increase request occurs.

              - **Unit** *(string) --*

                The unit of measure for the increase request.

              - **GlobalQuota** *(boolean) --*

                Specifies if the quota is a global quota.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aws_default_service_quotas(
        self, ServiceCode: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAwsDefaultServiceQuotasResponseTypeDef:
        """
        Lists all default service quotas for the specified AWS service or all AWS services.
        ListAWSDefaultServiceQuotas is similar to  ListServiceQuotas except for the Value object. The Value
        object returned by ``ListAWSDefaultServiceQuotas`` is the default value assigned by AWS. This
        request returns a list of all service quotas for the specified service. The listing of each you'll
        see the default values are the values that AWS provides for the quotas.

        .. note::

          Always check the ``NextToken`` response parameter when calling any of the ``List*`` operations.
          These operations can return an unexpected list of results, even when there are more results
          available. When this happens, the ``NextToken`` response parameter contains a value to pass the
          next call to the same API to request the next part of the list.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListAWSDefaultServiceQuotas>`_

        **Request Syntax**
        ::

          response = client.list_aws_default_service_quotas(
              ServiceCode='string',
              NextToken='string',
              MaxResults=123
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the service that you want to use.

        :type NextToken: string
        :param NextToken:

          (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a previous
          request that indicates that there's more output available. In a subsequent call, set it to the
          value of the previous call's ``NextToken`` response to indicate where the output should continue
          from. If additional items exist beyond the specified maximum, the ``NextToken`` element is
          present and has a value (isn't null). Include that value as the ``NextToken`` request parameter
          in the call to the operation to get the next part of the results. You should check ``NextToken``
          after every operation to ensure that you receive all of the results.

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Limits the number of results that you want to include in the response. If you don't
          include this parameter, the response defaults to a value that's specific to the operation. If
          additional items exist beyond the specified maximum, the ``NextToken`` element is present and has
          a value (isn't null). Include that value as the ``NextToken`` request parameter in the call to
          the operation to get the next part of the results. You should check ``NextToken`` after every
          operation to ensure that you receive all of the results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Quotas': [
                    {
                        'ServiceCode': 'string',
                        'ServiceName': 'string',
                        'QuotaArn': 'string',
                        'QuotaCode': 'string',
                        'QuotaName': 'string',
                        'Value': 123.0,
                        'Unit': 'string',
                        'Adjustable': True|False,
                        'GlobalQuota': True|False,
                        'UsageMetric': {
                            'MetricNamespace': 'string',
                            'MetricName': 'string',
                            'MetricDimensions': {
                                'string': 'string'
                            },
                            'MetricStatisticRecommendation': 'string'
                        },
                        'Period': {
                            'PeriodValue': 123,
                            'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
                        },
                        'ErrorReason': {
                            'ErrorCode':
                            'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'
                            |'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a
              previous request that indicates that there's more output available. In a subsequent call, set
              it to the value of the previous call's ``NextToken`` response to indicate where the output
              should continue from.

            - **Quotas** *(list) --*

              A list of the quotas in the account with the AWS default values.

              - *(dict) --*

                A structure that contains the full set of details that define the service quota.

                - **ServiceCode** *(string) --*

                  Specifies the service that you want to use.

                - **ServiceName** *(string) --*

                  The name of the AWS service specified in the increase request.

                - **QuotaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the service quota.

                - **QuotaCode** *(string) --*

                  The code identifier for the service quota specified.

                - **QuotaName** *(string) --*

                  The name identifier of the service quota.

                - **Value** *(float) --*

                  The value of service quota.

                - **Unit** *(string) --*

                  The unit of measurement for the value of the service quota.

                - **Adjustable** *(boolean) --*

                  Specifies if the quota value can be increased.

                - **GlobalQuota** *(boolean) --*

                  Specifies if the quota is global.

                - **UsageMetric** *(dict) --*

                  Specifies the details about the measurement.

                  - **MetricNamespace** *(string) --*

                    The namespace of the metric. The namespace is a container for CloudWatch metrics. You
                    can specify a name for the namespace when you create a metric.

                  - **MetricName** *(string) --*

                    The name of the CloudWatch metric that measures usage of a service quota. This is a
                    required field.

                  - **MetricDimensions** *(dict) --*

                    A dimension is a name/value pair that is part of the identity of a metric. Every metric
                    has specific characteristics that describe it, and you can think of dimensions as
                    categories for those characteristics. These dimensions are part of the CloudWatch
                    Metric Identity that measures usage against a particular service quota.

                    - *(string) --*

                      - *(string) --*

                  - **MetricStatisticRecommendation** *(string) --*

                    Statistics are metric data aggregations over specified periods of time. This is the
                    recommended statistic to use when comparing usage in the CloudWatch Metric against your
                    Service Quota.

                - **Period** *(dict) --*

                  Identifies the unit and value of how time is measured.

                  - **PeriodValue** *(integer) --*

                    The value of a period.

                  - **PeriodUnit** *(string) --*

                    The time unit of a period.

                - **ErrorReason** *(dict) --*

                  Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

                  - **ErrorCode** *(string) --*

                    Service Quotas returns the following error values.

                     ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
                     permission to call the service or service quota. To resolve the error, you need
                     permission to access the service or service quota.

                     ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
                     throttling Service Quotas.

                     ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
                     availability issues.

                     ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
                     Quotas.

                  - **ErrorMessage** *(string) --*

                    The error message that provides more detail.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_requested_service_quota_change_history(
        self,
        ServiceCode: str = None,
        Status: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef:
        """
        Requests a list of the changes to quotas for a service.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory>`_

        **Request Syntax**
        ::

          response = client.list_requested_service_quota_change_history(
              ServiceCode='string',
              Status='PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
              NextToken='string',
              MaxResults=123
          )
        :type ServiceCode: string
        :param ServiceCode:

          Specifies the service that you want to use.

        :type Status: string
        :param Status:

          Specifies the status value of the quota increase request.

        :type NextToken: string
        :param NextToken:

          (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a previous
          request that indicates that there's more output available. In a subsequent call, set it to the
          value of the previous call's ``NextToken`` response to indicate where the output should continue
          from.

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Limits the number of results that you want to include in the response. If you don't
          include this parameter, the response defaults to a value that's specific to the operation. If
          additional items exist beyond the specified maximum, the ``NextToken`` element is present and has
          a value (isn't null). Include that value as the ``NextToken`` request parameter in the call to
          the operation to get the next part of the results. You should check ``NextToken`` after every
          operation to ensure that you receive all of the results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'RequestedQuotas': [
                    {
                        'Id': 'string',
                        'CaseId': 'string',
                        'ServiceCode': 'string',
                        'ServiceName': 'string',
                        'QuotaCode': 'string',
                        'QuotaName': 'string',
                        'DesiredValue': 123.0,
                        'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
                        'Created': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'Requester': 'string',
                        'QuotaArn': 'string',
                        'GlobalQuota': True|False,
                        'Unit': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              If present in the response, this value indicates there's more output available that what's
              included in the current response. This can occur even when the response includes no values at
              all, such as when you ask for a filtered view of a very long list. Use this value in the
              ``NextToken`` request parameter in a subsequent call to the operation to continue processing
              and get the next part of the output. You should repeat this until the ``NextToken`` response
              element comes back empty (as ``null`` ).

            - **RequestedQuotas** *(list) --*

              Returns a list of service quota requests.

              - *(dict) --*

                A structure that contains information about a requested change for a quota.

                - **Id** *(string) --*

                  The unique identifier of a requested service quota change.

                - **CaseId** *(string) --*

                  The case Id for the service quota increase request.

                - **ServiceCode** *(string) --*

                  Specifies the service that you want to use.

                - **ServiceName** *(string) --*

                  The name of the AWS service specified in the increase request.

                - **QuotaCode** *(string) --*

                  Specifies the service quota that you want to use.

                - **QuotaName** *(string) --*

                  Name of the service quota.

                - **DesiredValue** *(float) --*

                  New increased value for the service quota.

                - **Status** *(string) --*

                  State of the service quota increase request.

                - **Created** *(datetime) --*

                  The date and time when the service quota increase request was received and the case Id
                  was created.

                - **LastUpdated** *(datetime) --*

                  The date and time of the most recent change in the service quota increase request.

                - **Requester** *(string) --*

                  The IAM identity who submitted the service quota increase request.

                - **QuotaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the service quota.

                - **GlobalQuota** *(boolean) --*

                  Identifies if the quota is global.

                - **Unit** *(string) --*

                  Specifies the unit used for the quota.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_requested_service_quota_change_history_by_quota(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef:
        """
        Requests a list of the changes to specific service quotas. This command provides additional
        granularity over the ``ListRequestedServiceQuotaChangeHistory`` command. Once a quota change
        request has reached ``CASE_CLOSED, APPROVED,`` or ``DENIED`` , the history has been kept for 90
        days.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistoryByQuota>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistoryByQuota>`_

        **Request Syntax**
        ::

          response = client.list_requested_service_quota_change_history_by_quota(
              ServiceCode='string',
              QuotaCode='string',
              Status='PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
              NextToken='string',
              MaxResults=123
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the service that you want to use.

        :type QuotaCode: string
        :param QuotaCode: **[REQUIRED]**

          Specifies the service quota that you want to use

        :type Status: string
        :param Status:

          Specifies the status value of the quota increase request.

        :type NextToken: string
        :param NextToken:

          (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a previous
          request that indicates that there's more output available. In a subsequent call, set it to the
          value of the previous call's ``NextToken`` response to indicate where the output should continue
          from.

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Limits the number of results that you want to include in the response. If you don't
          include this parameter, the response defaults to a value that's specific to the operation. If
          additional items exist beyond the specified maximum, the ``NextToken`` element is present and has
          a value (isn't null). Include that value as the ``NextToken`` request parameter in the call to
          the operation to get the next part of the results. You should check ``NextToken`` after every
          operation to ensure that you receive all of the results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'RequestedQuotas': [
                    {
                        'Id': 'string',
                        'CaseId': 'string',
                        'ServiceCode': 'string',
                        'ServiceName': 'string',
                        'QuotaCode': 'string',
                        'QuotaName': 'string',
                        'DesiredValue': 123.0,
                        'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
                        'Created': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'Requester': 'string',
                        'QuotaArn': 'string',
                        'GlobalQuota': True|False,
                        'Unit': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              If present in the response, this value indicates there's more output available that what's
              included in the current response. This can occur even when the response includes no values at
              all, such as when you ask for a filtered view of a very long list. Use this value in the
              ``NextToken`` request parameter in a subsequent call to the operation to continue processing
              and get the next part of the output. You should repeat this until the ``NextToken`` response
              element comes back empty (as ``null`` ).

            - **RequestedQuotas** *(list) --*

              Returns a list of service quota requests.

              - *(dict) --*

                A structure that contains information about a requested change for a quota.

                - **Id** *(string) --*

                  The unique identifier of a requested service quota change.

                - **CaseId** *(string) --*

                  The case Id for the service quota increase request.

                - **ServiceCode** *(string) --*

                  Specifies the service that you want to use.

                - **ServiceName** *(string) --*

                  The name of the AWS service specified in the increase request.

                - **QuotaCode** *(string) --*

                  Specifies the service quota that you want to use.

                - **QuotaName** *(string) --*

                  Name of the service quota.

                - **DesiredValue** *(float) --*

                  New increased value for the service quota.

                - **Status** *(string) --*

                  State of the service quota increase request.

                - **Created** *(datetime) --*

                  The date and time when the service quota increase request was received and the case Id
                  was created.

                - **LastUpdated** *(datetime) --*

                  The date and time of the most recent change in the service quota increase request.

                - **Requester** *(string) --*

                  The IAM identity who submitted the service quota increase request.

                - **QuotaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the service quota.

                - **GlobalQuota** *(boolean) --*

                  Identifies if the quota is global.

                - **Unit** *(string) --*

                  Specifies the unit used for the quota.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_service_quota_increase_requests_in_template(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef:
        """
        Returns a list of the quota increase requests in the template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListServiceQuotaIncreaseRequestsInTemplate>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListServiceQuotaIncreaseRequestsInTemplate>`_

        **Request Syntax**
        ::

          response = client.list_service_quota_increase_requests_in_template(
              ServiceCode='string',
              AwsRegion='string',
              NextToken='string',
              MaxResults=123
          )
        :type ServiceCode: string
        :param ServiceCode:

          The identifier for a service. When performing an operation, use the ``ServiceCode`` to specify a
          particular service.

        :type AwsRegion: string
        :param AwsRegion:

          Specifies the AWS Region for the quota that you want to use.

        :type NextToken: string
        :param NextToken:

          (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a previous
          request that indicates that there's more output available. In a subsequent call, set it to the
          value of the previous call's ``NextToken`` response to indicate where the output should continue
          from.

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Limits the number of results that you want to include in the response. If you don't
          include this parameter, the response defaults to a value that's specific to the operation. If
          additional items exist beyond the specified maximum, the ``NextToken`` element is present and has
          a value (isn't null). Include that value as the ``NextToken`` request parameter in the call to
          the operation to get the next part of the results. You should check ``NextToken`` after every
          operation to ensure that you receive all of the results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ServiceQuotaIncreaseRequestInTemplateList': [
                    {
                        'ServiceCode': 'string',
                        'ServiceName': 'string',
                        'QuotaCode': 'string',
                        'QuotaName': 'string',
                        'DesiredValue': 123.0,
                        'AwsRegion': 'string',
                        'Unit': 'string',
                        'GlobalQuota': True|False
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ServiceQuotaIncreaseRequestInTemplateList** *(list) --*

              Returns the list of values of the quota increase request in the template.

              - *(dict) --*

                A structure that contains information about one service quota increase request.

                - **ServiceCode** *(string) --*

                  The code identifier for the AWS service specified in the increase request.

                - **ServiceName** *(string) --*

                  The name of the AWS service specified in the increase request.

                - **QuotaCode** *(string) --*

                  The code identifier for the service quota specified in the increase request.

                - **QuotaName** *(string) --*

                  The name of the service quota in the increase request.

                - **DesiredValue** *(float) --*

                  Identifies the new, increased value of the service quota in the increase request.

                - **AwsRegion** *(string) --*

                  The AWS Region where the increase request occurs.

                - **Unit** *(string) --*

                  The unit of measure for the increase request.

                - **GlobalQuota** *(boolean) --*

                  Specifies if the quota is a global quota.

            - **NextToken** *(string) --*

              If present in the response, this value indicates there's more output available that what's
              included in the current response. This can occur even when the response includes no values at
              all, such as when you ask for a filtered view of a very long list. Use this value in the
              ``NextToken`` request parameter in a subsequent call to the operation to continue processing
              and get the next part of the output. You should repeat this until the ``NextToken`` response
              element comes back empty (as ``null`` ).

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_service_quotas(
        self, ServiceCode: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListServiceQuotasResponseTypeDef:
        """
        Lists all service quotas for the specified AWS service. This request returns a list of the service
        quotas for the specified service. you'll see the default values are the values that AWS provides
        for the quotas.

        .. note::

          Always check the ``NextToken`` response parameter when calling any of the ``List*`` operations.
          These operations can return an unexpected list of results, even when there are more results
          available. When this happens, the ``NextToken`` response parameter contains a value to pass the
          next call to the same API to request the next part of the list.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListServiceQuotas>`_

        **Request Syntax**
        ::

          response = client.list_service_quotas(
              ServiceCode='string',
              NextToken='string',
              MaxResults=123
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          The identifier for a service. When performing an operation, use the ``ServiceCode`` to specify a
          particular service.

        :type NextToken: string
        :param NextToken:

          (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a previous
          request that indicates that there's more output available. In a subsequent call, set it to the
          value of the previous call's ``NextToken`` response to indicate where the output should continue
          from.

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Limits the number of results that you want to include in the response. If you don't
          include this parameter, the response defaults to a value that's specific to the operation. If
          additional items exist beyond the specified maximum, the ``NextToken`` element is present and has
          a value (isn't null). Include that value as the ``NextToken`` request parameter in the call to
          the operation to get the next part of the results. You should check ``NextToken`` after every
          operation to ensure that you receive all of the results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Quotas': [
                    {
                        'ServiceCode': 'string',
                        'ServiceName': 'string',
                        'QuotaArn': 'string',
                        'QuotaCode': 'string',
                        'QuotaName': 'string',
                        'Value': 123.0,
                        'Unit': 'string',
                        'Adjustable': True|False,
                        'GlobalQuota': True|False,
                        'UsageMetric': {
                            'MetricNamespace': 'string',
                            'MetricName': 'string',
                            'MetricDimensions': {
                                'string': 'string'
                            },
                            'MetricStatisticRecommendation': 'string'
                        },
                        'Period': {
                            'PeriodValue': 123,
                            'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
                        },
                        'ErrorReason': {
                            'ErrorCode':
                            'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'
                            |'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              If present in the response, this value indicates there's more output available that what's
              included in the current response. This can occur even when the response includes no values at
              all, such as when you ask for a filtered view of a very long list. Use this value in the
              ``NextToken`` request parameter in a subsequent call to the operation to continue processing
              and get the next part of the output. You should repeat this until the ``NextToken`` response
              element comes back empty (as ``null`` ).

            - **Quotas** *(list) --*

              The response information for a quota lists all attribute information for the quota.

              - *(dict) --*

                A structure that contains the full set of details that define the service quota.

                - **ServiceCode** *(string) --*

                  Specifies the service that you want to use.

                - **ServiceName** *(string) --*

                  The name of the AWS service specified in the increase request.

                - **QuotaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the service quota.

                - **QuotaCode** *(string) --*

                  The code identifier for the service quota specified.

                - **QuotaName** *(string) --*

                  The name identifier of the service quota.

                - **Value** *(float) --*

                  The value of service quota.

                - **Unit** *(string) --*

                  The unit of measurement for the value of the service quota.

                - **Adjustable** *(boolean) --*

                  Specifies if the quota value can be increased.

                - **GlobalQuota** *(boolean) --*

                  Specifies if the quota is global.

                - **UsageMetric** *(dict) --*

                  Specifies the details about the measurement.

                  - **MetricNamespace** *(string) --*

                    The namespace of the metric. The namespace is a container for CloudWatch metrics. You
                    can specify a name for the namespace when you create a metric.

                  - **MetricName** *(string) --*

                    The name of the CloudWatch metric that measures usage of a service quota. This is a
                    required field.

                  - **MetricDimensions** *(dict) --*

                    A dimension is a name/value pair that is part of the identity of a metric. Every metric
                    has specific characteristics that describe it, and you can think of dimensions as
                    categories for those characteristics. These dimensions are part of the CloudWatch
                    Metric Identity that measures usage against a particular service quota.

                    - *(string) --*

                      - *(string) --*

                  - **MetricStatisticRecommendation** *(string) --*

                    Statistics are metric data aggregations over specified periods of time. This is the
                    recommended statistic to use when comparing usage in the CloudWatch Metric against your
                    Service Quota.

                - **Period** *(dict) --*

                  Identifies the unit and value of how time is measured.

                  - **PeriodValue** *(integer) --*

                    The value of a period.

                  - **PeriodUnit** *(string) --*

                    The time unit of a period.

                - **ErrorReason** *(dict) --*

                  Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

                  - **ErrorCode** *(string) --*

                    Service Quotas returns the following error values.

                     ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
                     permission to call the service or service quota. To resolve the error, you need
                     permission to access the service or service quota.

                     ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
                     throttling Service Quotas.

                     ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
                     availability issues.

                     ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
                     Quotas.

                  - **ErrorMessage** *(string) --*

                    The error message that provides more detail.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_services(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListServicesResponseTypeDef:
        """
        Lists the AWS services available in Service Quotas. Not all AWS services are available in Service
        Quotas. To list the see the list of the service quotas for a specific service, use
        ListServiceQuotas .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListServices>`_

        **Request Syntax**
        ::

          response = client.list_services(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a previous
          request that indicates that there's more output available. In a subsequent call, set it to the
          value of the previous call's ``NextToken`` response to indicate where the output should continue
          from.

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Limits the number of results that you want to include in the response. If you don't
          include this parameter, the response defaults to a value that's specific to the operation. If
          additional items exist beyond the specified maximum, the ``NextToken`` element is present and has
          a value (isn't null). Include that value as the ``NextToken`` request parameter in the call to
          the operation to get the next part of the results. You should check ``NextToken`` after every
          operation to ensure that you receive all of the results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Services': [
                    {
                        'ServiceCode': 'string',
                        'ServiceName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              If present in the response, this value indicates there's more output available that what's
              included in the current response. This can occur even when the response includes no values at
              all, such as when you ask for a filtered view of a very long list. Use this value in the
              ``NextToken`` request parameter in a subsequent call to the operation to continue processing
              and get the next part of the output. You should repeat this until the ``NextToken`` response
              element comes back empty (as ``null`` ).

            - **Services** *(list) --*

              Returns a list of services.

              - *(dict) --*

                A structure that contains the ``ServiceName`` and ``ServiceCode`` . It does not include all
                details of the service quota. To get those values, use the  ListServiceQuotas operation.

                - **ServiceCode** *(string) --*

                  Specifies the service that you want to use.

                - **ServiceName** *(string) --*

                  The name of the AWS service specified in the increase request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_service_quota_increase_request_into_template(
        self, QuotaCode: str, ServiceCode: str, AwsRegion: str, DesiredValue: float
    ) -> ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef:
        """
        Defines and adds a quota to the service quota template. To add a quota to the template, you must
        provide the ``ServiceCode`` , ``QuotaCode`` , ``AwsRegion`` , and ``DesiredValue`` . Once you add a
        quota to the template, use  ListServiceQuotaIncreaseRequestsInTemplate to see the list of quotas in
        the template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/PutServiceQuotaIncreaseRequestIntoTemplate>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/PutServiceQuotaIncreaseRequestIntoTemplate>`_

        **Request Syntax**
        ::

          response = client.put_service_quota_increase_request_into_template(
              QuotaCode='string',
              ServiceCode='string',
              AwsRegion='string',
              DesiredValue=123.0
          )
        :type QuotaCode: string
        :param QuotaCode: **[REQUIRED]**

          Specifies the service quota that you want to use.

        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the service that you want to use.

        :type AwsRegion: string
        :param AwsRegion: **[REQUIRED]**

          Specifies the AWS Region for the quota.

        :type DesiredValue: float
        :param DesiredValue: **[REQUIRED]**

          Specifies the new, increased value for the quota.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ServiceQuotaIncreaseRequestInTemplate': {
                    'ServiceCode': 'string',
                    'ServiceName': 'string',
                    'QuotaCode': 'string',
                    'QuotaName': 'string',
                    'DesiredValue': 123.0,
                    'AwsRegion': 'string',
                    'Unit': 'string',
                    'GlobalQuota': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ServiceQuotaIncreaseRequestInTemplate** *(dict) --*

              A structure that contains information about one service quota increase request.

              - **ServiceCode** *(string) --*

                The code identifier for the AWS service specified in the increase request.

              - **ServiceName** *(string) --*

                The name of the AWS service specified in the increase request.

              - **QuotaCode** *(string) --*

                The code identifier for the service quota specified in the increase request.

              - **QuotaName** *(string) --*

                The name of the service quota in the increase request.

              - **DesiredValue** *(float) --*

                Identifies the new, increased value of the service quota in the increase request.

              - **AwsRegion** *(string) --*

                The AWS Region where the increase request occurs.

              - **Unit** *(string) --*

                The unit of measure for the increase request.

              - **GlobalQuota** *(boolean) --*

                Specifies if the quota is a global quota.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_service_quota_increase(
        self, ServiceCode: str, QuotaCode: str, DesiredValue: float
    ) -> ClientRequestServiceQuotaIncreaseResponseTypeDef:
        """
        Retrieves the details of a service quota increase request. The response to this command provides
        the details in the  RequestedServiceQuotaChange object.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/RequestServiceQuotaIncrease>`_

        **Request Syntax**
        ::

          response = client.request_service_quota_increase(
              ServiceCode='string',
              QuotaCode='string',
              DesiredValue=123.0
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the service that you want to use.

        :type QuotaCode: string
        :param QuotaCode: **[REQUIRED]**

          Specifies the service quota that you want to use.

        :type DesiredValue: float
        :param DesiredValue: **[REQUIRED]**

          Specifies the value submitted in the service quota increase request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestedQuota': {
                    'Id': 'string',
                    'CaseId': 'string',
                    'ServiceCode': 'string',
                    'ServiceName': 'string',
                    'QuotaCode': 'string',
                    'QuotaName': 'string',
                    'DesiredValue': 123.0,
                    'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
                    'Created': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'Requester': 'string',
                    'QuotaArn': 'string',
                    'GlobalQuota': True|False,
                    'Unit': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **RequestedQuota** *(dict) --*

              Returns a list of service quota requests.

              - **Id** *(string) --*

                The unique identifier of a requested service quota change.

              - **CaseId** *(string) --*

                The case Id for the service quota increase request.

              - **ServiceCode** *(string) --*

                Specifies the service that you want to use.

              - **ServiceName** *(string) --*

                The name of the AWS service specified in the increase request.

              - **QuotaCode** *(string) --*

                Specifies the service quota that you want to use.

              - **QuotaName** *(string) --*

                Name of the service quota.

              - **DesiredValue** *(float) --*

                New increased value for the service quota.

              - **Status** *(string) --*

                State of the service quota increase request.

              - **Created** *(datetime) --*

                The date and time when the service quota increase request was received and the case Id was
                created.

              - **LastUpdated** *(datetime) --*

                The date and time of the most recent change in the service quota increase request.

              - **Requester** *(string) --*

                The IAM identity who submitted the service quota increase request.

              - **QuotaArn** *(string) --*

                The Amazon Resource Name (ARN) of the service quota.

              - **GlobalQuota** *(boolean) --*

                Identifies if the quota is global.

              - **Unit** *(string) --*

                Specifies the unit used for the quota.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aws_default_service_quotas"]
    ) -> paginator_scope.ListAWSDefaultServiceQuotasPaginator:
        """
        Get Paginator for `list_aws_default_service_quotas` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_requested_service_quota_change_history"]
    ) -> paginator_scope.ListRequestedServiceQuotaChangeHistoryPaginator:
        """
        Get Paginator for `list_requested_service_quota_change_history` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self,
        operation_name: Literal["list_requested_service_quota_change_history_by_quota"],
    ) -> paginator_scope.ListRequestedServiceQuotaChangeHistoryByQuotaPaginator:
        """
        Get Paginator for `list_requested_service_quota_change_history_by_quota` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self,
        operation_name: Literal["list_service_quota_increase_requests_in_template"],
    ) -> paginator_scope.ListServiceQuotaIncreaseRequestsInTemplatePaginator:
        """
        Get Paginator for `list_service_quota_increase_requests_in_template` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_service_quotas"]
    ) -> paginator_scope.ListServiceQuotasPaginator:
        """
        Get Paginator for `list_service_quotas` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_services"]
    ) -> paginator_scope.ListServicesPaginator:
        """
        Get Paginator for `list_services` operation.
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
    AWSServiceAccessNotEnabledException: Boto3ClientError
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    DependencyAccessDeniedException: Boto3ClientError
    IllegalArgumentException: Boto3ClientError
    InvalidPaginationTokenException: Boto3ClientError
    InvalidResourceStateException: Boto3ClientError
    NoAvailableOrganizationException: Boto3ClientError
    NoSuchResourceException: Boto3ClientError
    OrganizationNotInAllFeaturesModeException: Boto3ClientError
    QuotaExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ServiceException: Boto3ClientError
    ServiceQuotaTemplateNotInUseException: Boto3ClientError
    TemplatesNotAvailableInRegionException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
