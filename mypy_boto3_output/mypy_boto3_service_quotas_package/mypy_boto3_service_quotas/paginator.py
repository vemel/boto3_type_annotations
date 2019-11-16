"Main interface for service-quotas Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_service_quotas.type_defs import (
    ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef,
    ListAWSDefaultServiceQuotasPaginateResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef,
    ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef,
    ListServiceQuotasPaginatePaginationConfigTypeDef,
    ListServiceQuotasPaginateResponseTypeDef,
    ListServicesPaginatePaginationConfigTypeDef,
    ListServicesPaginateResponseTypeDef,
)


__all__ = (
    "ListAWSDefaultServiceQuotasPaginator",
    "ListRequestedServiceQuotaChangeHistoryPaginator",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginator",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginator",
    "ListServiceQuotasPaginator",
    "ListServicesPaginator",
)


class ListAWSDefaultServiceQuotasPaginator(Boto3Paginator):
    """
    Paginator for `list_aws_default_service_quotas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str,
        PaginationConfig: ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef = None,
    ) -> ListAWSDefaultServiceQuotasPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ServiceQuotas.Client.list_aws_default_service_quotas`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListAWSDefaultServiceQuotas>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ServiceCode='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          Specifies the service that you want to use.

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


class ListRequestedServiceQuotaChangeHistoryPaginator(Boto3Paginator):
    """
    Paginator for `list_requested_service_quota_change_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        Status: str = None,
        PaginationConfig: ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef = None,
    ) -> ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ServiceQuotas.Client.list_requested_service_quota_change_history`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ServiceCode='string',
              Status='PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ServiceCode: string
        :param ServiceCode:

          Specifies the service that you want to use.

        :type Status: string
        :param Status:

          Specifies the status value of the quota increase request.

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


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginator(Boto3Paginator):
    """
    Paginator for `list_requested_service_quota_change_history_by_quota`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: str = None,
        PaginationConfig: ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef = None,
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ServiceQuotas.Client.list_requested_service_quota_change_history_by_quota`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistoryByQuota>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistoryByQuota>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ServiceCode='string',
              QuotaCode='string',
              Status='PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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


class ListServiceQuotaIncreaseRequestsInTemplatePaginator(Boto3Paginator):
    """
    Paginator for `list_service_quota_increase_requests_in_template`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        PaginationConfig: ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef = None,
    ) -> ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ServiceQuotas.Client.list_service_quota_increase_requests_in_template`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListServiceQuotaIncreaseRequestsInTemplate>`_
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListServiceQuotaIncreaseRequestsInTemplate>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ServiceCode='string',
              AwsRegion='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ServiceCode: string
        :param ServiceCode:

          The identifier for a service. When performing an operation, use the ``ServiceCode`` to specify a
          particular service.

        :type AwsRegion: string
        :param AwsRegion:

          Specifies the AWS Region for the quota that you want to use.

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

        """


class ListServiceQuotasPaginator(Boto3Paginator):
    """
    Paginator for `list_service_quotas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str,
        PaginationConfig: ListServiceQuotasPaginatePaginationConfigTypeDef = None,
    ) -> ListServiceQuotasPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ServiceQuotas.Client.list_service_quotas`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListServiceQuotas>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ServiceCode='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**

          The identifier for a service. When performing an operation, use the ``ServiceCode`` to specify a
          particular service.

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


class ListServicesPaginator(Boto3Paginator):
    """
    Paginator for `list_services`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListServicesPaginatePaginationConfigTypeDef = None
    ) -> ListServicesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ServiceQuotas.Client.list_services`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListServices>`_

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
                'Services': [
                    {
                        'ServiceCode': 'string',
                        'ServiceName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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
