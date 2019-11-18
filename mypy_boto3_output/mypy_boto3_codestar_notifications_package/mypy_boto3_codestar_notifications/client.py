"Main interface for codestar-notifications Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_codestar_notifications.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codestar_notifications.paginator as paginator_scope
from mypy_boto3_codestar_notifications.type_defs import (
    ClientCreateNotificationRuleResponseTypeDef,
    ClientCreateNotificationRuleTargetsTypeDef,
    ClientDeleteNotificationRuleResponseTypeDef,
    ClientDescribeNotificationRuleResponseTypeDef,
    ClientListEventTypesFiltersTypeDef,
    ClientListEventTypesResponseTypeDef,
    ClientListNotificationRulesFiltersTypeDef,
    ClientListNotificationRulesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTargetsFiltersTypeDef,
    ClientListTargetsResponseTypeDef,
    ClientSubscribeResponseTypeDef,
    ClientSubscribeTargetTypeDef,
    ClientTagResourceResponseTypeDef,
    ClientUnsubscribeResponseTypeDef,
    ClientUpdateNotificationRuleTargetsTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

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
    def create_notification_rule(
        self,
        Name: str,
        EventTypeIds: List[str],
        Resource: str,
        Targets: List[ClientCreateNotificationRuleTargetsTypeDef],
        DetailType: str,
        ClientRequestToken: str = None,
        Tags: List[str] = None,
        Status: str = None,
    ) -> ClientCreateNotificationRuleResponseTypeDef:
        """
        Creates a notification rule for a resource. The rule specifies the events you want notifications
        about and the targets (such as SNS topics) where you want to receive them.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/CreateNotificationRule>`_

        **Request Syntax**
        ::

          response = client.create_notification_rule(
              Name='string',
              EventTypeIds=[
                  'string',
              ],
              Resource='string',
              Targets=[
                  {
                      'TargetType': 'string',
                      'TargetAddress': 'string'
                  },
              ],
              DetailType='BASIC'|'FULL',
              ClientRequestToken='string',
              Tags={
                  'string': 'string'
              },
              Status='ENABLED'|'DISABLED'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name for the notification rule. Notifictaion rule names must be unique in your AWS account.

        :type EventTypeIds: list
        :param EventTypeIds: **[REQUIRED]**

          A list of event types associated with this notification rule. For a list of allowed events, see
          EventTypeSummary .

          - *(string) --*

        :type Resource: string
        :param Resource: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported
          resources include pipelines in AWS CodePipeline, repositories in AWS CodeCommit, and build
          projects in AWS CodeBuild.

        :type Targets: list
        :param Targets: **[REQUIRED]**

          A list of Amazon Resource Names (ARNs) of SNS topics to associate with the notification rule.

          - *(dict) --*

            Information about the SNS topics associated with a notification rule.

            - **TargetType** *(string) --*

              The target type. Can be an Amazon SNS topic.

            - **TargetAddress** *(string) --*

              The Amazon Resource Name (ARN) of the SNS topic.

        :type DetailType: string
        :param DetailType: **[REQUIRED]**

          The level of detail to include in the notifications for this resource. BASIC will include only
          the contents of the event as it would appear in AWS CloudWatch. FULL will include any
          supplemental information provided by AWS CodeStar Notifications and/or the service for the
          resource for which the notification is created.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique, client-generated idempotency token that, when provided in a request, ensures the
          request cannot be repeated with a changed parameter. If a request with the same parameters is
          received and a token is included, the request returns information about the initial request that
          used that token.

          .. note::

            The AWS SDKs prepopulate client request tokens. If you are using an AWS SDK, an idempotency
            token is created for you.

          This field is autopopulated if not provided.

        :type Tags: dict
        :param Tags:

          A list of tags to apply to this notification rule. Key names cannot start with "aws".

          - *(string) --*

            - *(string) --*

        :type Status: string
        :param Status:

          The status of the notification rule. The default value is ENABLED. If the status is set to
          DISABLED, notifications aren't sent for the notification rule.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the notification rule.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_notification_rule(
        self, Arn: str
    ) -> ClientDeleteNotificationRuleResponseTypeDef:
        """
        Deletes a notification rule for a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/DeleteNotificationRule>`_

        **Request Syntax**
        ::

          response = client.delete_notification_rule(
              Arn='string'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the notification rule you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the deleted notification rule.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_target(
        self, TargetAddress: str, ForceUnsubscribeAll: bool = None
    ) -> Dict[str, Any]:
        """
        Deletes a specified target for notifications.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/DeleteTarget>`_

        **Request Syntax**
        ::

          response = client.delete_target(
              TargetAddress='string',
              ForceUnsubscribeAll=True|False
          )
        :type TargetAddress: string
        :param TargetAddress: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the SNS topic to delete.

        :type ForceUnsubscribeAll: boolean
        :param ForceUnsubscribeAll:

          A Boolean value that can be used to delete all associations with this SNS topic. The default
          value is FALSE. If set to TRUE, all associations between that target and every notification rule
          in your AWS account are deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_notification_rule(
        self, Arn: str
    ) -> ClientDescribeNotificationRuleResponseTypeDef:
        """
        Returns information about a specified notification rule.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/DescribeNotificationRule>`_
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/DescribeNotificationRule>`_

        **Request Syntax**
        ::

          response = client.describe_notification_rule(
              Arn='string'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the notification rule.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'Name': 'string',
                'EventTypes': [
                    {
                        'EventTypeId': 'string',
                        'ServiceName': 'string',
                        'EventTypeName': 'string',
                        'ResourceType': 'string'
                    },
                ],
                'Resource': 'string',
                'Targets': [
                    {
                        'TargetAddress': 'string',
                        'TargetType': 'string',
                        'TargetStatus': 'PENDING'|'ACTIVE'|'UNREACHABLE'|'INACTIVE'|'DEACTIVATED'
                    },
                ],
                'DetailType': 'BASIC'|'FULL',
                'CreatedBy': 'string',
                'Status': 'ENABLED'|'DISABLED',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'LastModifiedTimestamp': datetime(2015, 1, 1),
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the notification rule.

            - **Name** *(string) --*

              The name of the notification rule.

            - **EventTypes** *(list) --*

              A list of the event types associated with the notification rule.

              - *(dict) --*

                Returns information about an event that has triggered a notification rule.

                - **EventTypeId** *(string) --*

                  The system-generated ID of the event.

                - **ServiceName** *(string) --*

                  The name of the service for which the event applies.

                - **EventTypeName** *(string) --*

                  The name of the event.

                - **ResourceType** *(string) --*

                  The resource type of the event.

            - **Resource** *(string) --*

              The Amazon Resource Name (ARN) of the resource associated with the notification rule.

            - **Targets** *(list) --*

              A list of the SNS topics associated with the notification rule.

              - *(dict) --*

                Information about the targets specified for a notification rule.

                - **TargetAddress** *(string) --*

                  The Amazon Resource Name (ARN) of the SNS topic.

                - **TargetType** *(string) --*

                  The type of the target (for example, SNS).

                - **TargetStatus** *(string) --*

                  The status of the target.

            - **DetailType** *(string) --*

              The level of detail included in the notifications for this resource. BASIC will include only
              the contents of the event as it would appear in AWS CloudWatch. FULL will include any
              supplemental information provided by AWS CodeStar Notifications and/or the service for the
              resource for which the notification is created.

            - **CreatedBy** *(string) --*

              The name or email alias of the person who created the notification rule.

            - **Status** *(string) --*

              The status of the notification rule. Valid statuses are on (sending notifications) or off
              (not sending notifications).

            - **CreatedTimestamp** *(datetime) --*

              The date and time the notification rule was created, in timestamp format.

            - **LastModifiedTimestamp** *(datetime) --*

              The date and time the notification rule was most recently updated, in timestamp format.

            - **Tags** *(dict) --*

              The tags associated with the notification rule.

              - *(string) --*

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
    def list_event_types(
        self,
        Filters: List[ClientListEventTypesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEventTypesResponseTypeDef:
        """
        Returns information about the event types available for configuring notifications.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/ListEventTypes>`_

        **Request Syntax**
        ::

          response = client.list_event_types(
              Filters=[
                  {
                      'Name': 'RESOURCE_TYPE'|'SERVICE_NAME',
                      'Value': 'string'
                  },
              ],
              NextToken='string',
              MaxResults=123
          )
        :type Filters: list
        :param Filters:

          The filters to use to return information by service or resource type.

          - *(dict) --*

            Information about a filter to apply to the list of returned event types. You can filter by
            resource type or service name.

            - **Name** *(string) --* **[REQUIRED]**

              The system-generated name of the filter type you want to filter by.

            - **Value** *(string) --* **[REQUIRED]**

              The name of the resource type (for example, pipeline) or service name (for example,
              CodePipeline) that you want to filter by.

        :type NextToken: string
        :param NextToken:

          An enumeration token that, when provided in a request, returns the next batch of the results.

        :type MaxResults: integer
        :param MaxResults:

          A non-negative integer used to limit the number of returned results. The default number is 50.
          The maximum number of results that can be returned is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventTypes': [
                    {
                        'EventTypeId': 'string',
                        'ServiceName': 'string',
                        'EventTypeName': 'string',
                        'ResourceType': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **EventTypes** *(list) --*

              Information about each event, including service name, resource type, event ID, and event name.

              - *(dict) --*

                Returns information about an event that has triggered a notification rule.

                - **EventTypeId** *(string) --*

                  The system-generated ID of the event.

                - **ServiceName** *(string) --*

                  The name of the service for which the event applies.

                - **EventTypeName** *(string) --*

                  The name of the event.

                - **ResourceType** *(string) --*

                  The resource type of the event.

            - **NextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_notification_rules(
        self,
        Filters: List[ClientListNotificationRulesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListNotificationRulesResponseTypeDef:
        """
        Returns a list of the notification rules for an AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/ListNotificationRules>`_

        **Request Syntax**
        ::

          response = client.list_notification_rules(
              Filters=[
                  {
                      'Name': 'EVENT_TYPE_ID'|'CREATED_BY'|'RESOURCE'|'TARGET_ADDRESS',
                      'Value': 'string'
                  },
              ],
              NextToken='string',
              MaxResults=123
          )
        :type Filters: list
        :param Filters:

          The filters to use to return information by service or resource type. For valid values, see
          ListNotificationRulesFilter .

          .. note::

            A filter with the same name can appear more than once when used with OR statements. Filters
            with different names should be applied with AND statements.

          - *(dict) --*

            Information about a filter to apply to the list of returned notification rules. You can filter
            by event type, owner, resource, or target.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the attribute you want to use to filter the returned notification rules.

            - **Value** *(string) --* **[REQUIRED]**

              The value of the attribute you want to use to filter the returned notification rules. For
              example, if you specify filtering by *RESOURCE* in Name, you might specify the ARN of a
              pipeline in AWS CodePipeline for the value.

        :type NextToken: string
        :param NextToken:

          An enumeration token that, when provided in a request, returns the next batch of the results.

        :type MaxResults: integer
        :param MaxResults:

          A non-negative integer used to limit the number of returned results. The maximum number of
          results that can be returned is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'NotificationRules': [
                    {
                        'Id': 'string',
                        'Arn': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the results.

            - **NotificationRules** *(list) --*

              The list of notification rules for the AWS account, by Amazon Resource Name (ARN) and ID.

              - *(dict) --*

                Information about a specified notification rule.

                - **Id** *(string) --*

                  The unique ID of the notification rule.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the notification rule.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, Arn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags associated with a notification rule.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              Arn='string'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the notification rule.

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

              The tags associated with the notification rule.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_targets(
        self,
        Filters: List[ClientListTargetsFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListTargetsResponseTypeDef:
        """
        Returns a list of the notification rule targets for an AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/ListTargets>`_

        **Request Syntax**
        ::

          response = client.list_targets(
              Filters=[
                  {
                      'Name': 'TARGET_TYPE'|'TARGET_ADDRESS'|'TARGET_STATUS',
                      'Value': 'string'
                  },
              ],
              NextToken='string',
              MaxResults=123
          )
        :type Filters: list
        :param Filters:

          The filters to use to return information by service or resource type. Valid filters include
          target type, target address, and target status.

          .. note::

            A filter with the same name can appear more than once when used with OR statements. Filters
            with different names should be applied with AND statements.

          - *(dict) --*

            Information about a filter to apply to the list of returned targets. You can filter by target
            type, address, or status. For example, to filter results to notification rules that have active
            Amazon SNS topics as targets, you could specify a ListTargetsFilter Name as TargetType and a
            Value of SNS, and a Name of TARGET_STATUS and a Value of ACTIVE.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the attribute you want to use to filter the returned targets.

            - **Value** *(string) --* **[REQUIRED]**

              The value of the attribute you want to use to filter the returned targets. For example, if
              you specify *SNS* for the Target type, you could specify an Amazon Resource Name (ARN) for a
              topic as the value.

        :type NextToken: string
        :param NextToken:

          An enumeration token that, when provided in a request, returns the next batch of the results.

        :type MaxResults: integer
        :param MaxResults:

          A non-negative integer used to limit the number of returned results. The maximum number of
          results that can be returned is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Targets': [
                    {
                        'TargetAddress': 'string',
                        'TargetType': 'string',
                        'TargetStatus': 'PENDING'|'ACTIVE'|'UNREACHABLE'|'INACTIVE'|'DEACTIVATED'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Targets** *(list) --*

              The list of notification rule targets.

              - *(dict) --*

                Information about the targets specified for a notification rule.

                - **TargetAddress** *(string) --*

                  The Amazon Resource Name (ARN) of the SNS topic.

                - **TargetType** *(string) --*

                  The type of the target (for example, SNS).

                - **TargetStatus** *(string) --*

                  The status of the target.

            - **NextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def subscribe(
        self,
        Arn: str,
        Target: ClientSubscribeTargetTypeDef,
        ClientRequestToken: str = None,
    ) -> ClientSubscribeResponseTypeDef:
        """
        Creates an association between a notification rule and an SNS topic so that the associated target
        can receive notifications when the events described in the rule are triggered.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/Subscribe>`_

        **Request Syntax**
        ::

          response = client.subscribe(
              Arn='string',
              Target={
                  'TargetType': 'string',
                  'TargetAddress': 'string'
              },
              ClientRequestToken='string'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the notification rule for which you want to create the
          association.

        :type Target: dict
        :param Target: **[REQUIRED]**

          Information about the SNS topics associated with a notification rule.

          - **TargetType** *(string) --*

            The target type. Can be an Amazon SNS topic.

          - **TargetAddress** *(string) --*

            The Amazon Resource Name (ARN) of the SNS topic.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          An enumeration token that, when provided in a request, returns the next batch of the results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the notification rule for which you have created
              assocations.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, Arn: str, Tags: List[str]
    ) -> ClientTagResourceResponseTypeDef:
        """
        Associates a set of provided tags with a notification rule.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              Arn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the notification rule to tag.

        :type Tags: dict
        :param Tags: **[REQUIRED]**

          The list of tags to associate with the resource. Tag key names cannot start with "aws".

          - *(string) --*

            - *(string) --*

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

              The list of tags associated with the resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unsubscribe(
        self, Arn: str, TargetAddress: str
    ) -> ClientUnsubscribeResponseTypeDef:
        """
        Removes an association between a notification rule and an Amazon SNS topic so that subscribers to
        that topic stop receiving notifications when the events described in the rule are triggered.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/Unsubscribe>`_

        **Request Syntax**
        ::

          response = client.unsubscribe(
              Arn='string',
              TargetAddress='string'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the notification rule.

        :type TargetAddress: string
        :param TargetAddress: **[REQUIRED]**

          The ARN of the SNS topic to unsubscribe from the notification rule.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the the notification rule from which you have removed a
              subscription.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, Arn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the association between one or more provided tags and a notification rule.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              Arn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the notification rule from which to remove the tags.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The key names of the tags to remove.

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
    def update_notification_rule(
        self,
        Arn: str,
        Name: str = None,
        Status: str = None,
        EventTypeIds: List[str] = None,
        Targets: List[ClientUpdateNotificationRuleTargetsTypeDef] = None,
        DetailType: str = None,
    ) -> Dict[str, Any]:
        """
        Updates a notification rule for a resource. You can change the events that trigger the notification
        rule, the status of the rule, and the targets that receive the notifications.

        .. note::

          To add or remove tags for a notification rule, you must use  TagResource and  UntagResource .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/UpdateNotificationRule>`_

        **Request Syntax**
        ::

          response = client.update_notification_rule(
              Arn='string',
              Name='string',
              Status='ENABLED'|'DISABLED',
              EventTypeIds=[
                  'string',
              ],
              Targets=[
                  {
                      'TargetType': 'string',
                      'TargetAddress': 'string'
                  },
              ],
              DetailType='BASIC'|'FULL'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the notification rule.

        :type Name: string
        :param Name:

          The name of the notification rule.

        :type Status: string
        :param Status:

          The status of the notification rule. Valid statuses include enabled (sending notifications) or
          disabled (not sending notifications).

        :type EventTypeIds: list
        :param EventTypeIds:

          A list of event types associated with this notification rule.

          - *(string) --*

        :type Targets: list
        :param Targets:

          The address and type of the targets to receive notifications from this notification rule.

          - *(dict) --*

            Information about the SNS topics associated with a notification rule.

            - **TargetType** *(string) --*

              The target type. Can be an Amazon SNS topic.

            - **TargetAddress** *(string) --*

              The Amazon Resource Name (ARN) of the SNS topic.

        :type DetailType: string
        :param DetailType:

          The level of detail to include in the notifications for this resource. BASIC will include only
          the contents of the event as it would appear in AWS CloudWatch. FULL will include any
          supplemental information provided by AWS CodeStar Notifications and/or the service for the
          resource for which the notification is created.

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
        self, operation_name: Literal["list_event_types"]
    ) -> paginator_scope.ListEventTypesPaginator:
        """
        Get Paginator for `list_event_types` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_notification_rules"]
    ) -> paginator_scope.ListNotificationRulesPaginator:
        """
        Get Paginator for `list_notification_rules` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_targets"]
    ) -> paginator_scope.ListTargetsPaginator:
        """
        Get Paginator for `list_targets` operation.
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
    ConcurrentModificationException: Boto3ClientError
    ConfigurationException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
