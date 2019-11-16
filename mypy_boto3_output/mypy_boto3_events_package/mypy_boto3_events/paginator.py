"Main interface for events Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_events.type_defs import (
    ListRuleNamesByTargetPaginatePaginationConfigTypeDef,
    ListRuleNamesByTargetPaginateResponseTypeDef,
    ListRulesPaginatePaginationConfigTypeDef,
    ListRulesPaginateResponseTypeDef,
    ListTargetsByRulePaginatePaginationConfigTypeDef,
    ListTargetsByRulePaginateResponseTypeDef,
)


__all__ = (
    "ListRuleNamesByTargetPaginator",
    "ListRulesPaginator",
    "ListTargetsByRulePaginator",
)


class ListRuleNamesByTargetPaginator(Boto3Paginator):
    """
    Paginator for `list_rule_names_by_target`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TargetArn: str,
        EventBusName: str = None,
        PaginationConfig: ListRuleNamesByTargetPaginatePaginationConfigTypeDef = None,
    ) -> ListRuleNamesByTargetPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`EventBridge.Client.list_rule_names_by_target`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/ListRuleNamesByTarget>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              TargetArn='string',
              EventBusName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type TargetArn: string
        :param TargetArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the target resource.

        :type EventBusName: string
        :param EventBusName:

          Limits the results to show only the rules associated with the specified event bus.

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
                'RuleNames': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **RuleNames** *(list) --*

              The names of the rules that can invoke the given target.

              - *(string) --*

        """


class ListRulesPaginator(Boto3Paginator):
    """
    Paginator for `list_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        PaginationConfig: ListRulesPaginatePaginationConfigTypeDef = None,
    ) -> ListRulesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`EventBridge.Client.list_rules`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/ListRules>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              NamePrefix='string',
              EventBusName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type NamePrefix: string
        :param NamePrefix:

          The prefix matching the rule name.

        :type EventBusName: string
        :param EventBusName:

          Limits the results to show only the rules associated with the specified event bus.

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
                'Rules': [
                    {
                        'Name': 'string',
                        'Arn': 'string',
                        'EventPattern': 'string',
                        'State': 'ENABLED'|'DISABLED',
                        'Description': 'string',
                        'ScheduleExpression': 'string',
                        'RoleArn': 'string',
                        'ManagedBy': 'string',
                        'EventBusName': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Rules** *(list) --*

              The rules that match the specified criteria.

              - *(dict) --*

                Contains information about a rule in Amazon EventBridge.

                - **Name** *(string) --*

                  The name of the rule.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the rule.

                - **EventPattern** *(string) --*

                  The event pattern of the rule. For more information, see `Event Patterns
                  <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`__
                  in the *Amazon EventBridge User Guide* .

                - **State** *(string) --*

                  The state of the rule.

                - **Description** *(string) --*

                  The description of the rule.

                - **ScheduleExpression** *(string) --*

                  The scheduling expression: for example, ``"cron(0 20 * * ? *)"`` or ``"rate(5 minutes)"``
                  .

                - **RoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the role that is used for target invocation.

                - **ManagedBy** *(string) --*

                  If an AWS service created the rule on behalf of your account, this field displays the
                  principal name of the service that created the rule.

                - **EventBusName** *(string) --*

                  The event bus associated with the rule.

        """


class ListTargetsByRulePaginator(Boto3Paginator):
    """
    Paginator for `list_targets_by_rule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Rule: str,
        EventBusName: str = None,
        PaginationConfig: ListTargetsByRulePaginatePaginationConfigTypeDef = None,
    ) -> ListTargetsByRulePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`EventBridge.Client.list_targets_by_rule`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/ListTargetsByRule>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Rule='string',
              EventBusName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Rule: string
        :param Rule: **[REQUIRED]**

          The name of the rule.

        :type EventBusName: string
        :param EventBusName:

          The event bus associated with the rule. If you omit this, the default event bus is used.

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
                'Targets': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'RoleArn': 'string',
                        'Input': 'string',
                        'InputPath': 'string',
                        'InputTransformer': {
                            'InputPathsMap': {
                                'string': 'string'
                            },
                            'InputTemplate': 'string'
                        },
                        'KinesisParameters': {
                            'PartitionKeyPath': 'string'
                        },
                        'RunCommandParameters': {
                            'RunCommandTargets': [
                                {
                                    'Key': 'string',
                                    'Values': [
                                        'string',
                                    ]
                                },
                            ]
                        },
                        'EcsParameters': {
                            'TaskDefinitionArn': 'string',
                            'TaskCount': 123,
                            'LaunchType': 'EC2'|'FARGATE',
                            'NetworkConfiguration': {
                                'awsvpcConfiguration': {
                                    'Subnets': [
                                        'string',
                                    ],
                                    'SecurityGroups': [
                                        'string',
                                    ],
                                    'AssignPublicIp': 'ENABLED'|'DISABLED'
                                }
                            },
                            'PlatformVersion': 'string',
                            'Group': 'string'
                        },
                        'BatchParameters': {
                            'JobDefinition': 'string',
                            'JobName': 'string',
                            'ArrayProperties': {
                                'Size': 123
                            },
                            'RetryStrategy': {
                                'Attempts': 123
                            }
                        },
                        'SqsParameters': {
                            'MessageGroupId': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Targets** *(list) --*

              The targets assigned to the rule.

              - *(dict) --*

                Targets are the resources to be invoked when a rule is triggered. For a complete list of
                services and resources that can be set as a target, see  PutTargets .

                If you're setting the event bus of another account as the target and that account granted
                permission to your account through an organization instead of directly by the account ID,
                you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For
                more information, see `Sending and Receiving Events Between AWS Accounts
                <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
                in the *Amazon EventBridge User Guide* .

                - **Id** *(string) --*

                  A name for the target. Use a string that will help you identify the target. Each target
                  associated with a rule must have an ``Id`` unique for that rule.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the target.

                - **RoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule
                  is triggered. If one rule triggers multiple targets, you can use a different IAM role for
                  each target.

                - **Input** *(string) --*

                  Valid JSON text passed to the target. In this case, nothing from the event itself is
                  passed to the target. For more information, see `The JavaScript Object Notation (JSON)
                  Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .

                - **InputPath** *(string) --*

                  The value of the JSONPath that is used for extracting part of the matched event when
                  passing it to the target. You must use JSON dot notation, not bracket notation. For more
                  information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .

                - **InputTransformer** *(dict) --*

                  Settings to enable you to provide custom input to a target based on certain event data.
                  You can extract one or more key-value pairs from the event and then use that data to send
                  customized input to the target.

                  - **InputPathsMap** *(dict) --*

                    Map of JSON paths to be extracted from the event. You can then insert these in the
                    template in ``InputTemplate`` to produce the output to be sent to the target.

                     ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path.
                     You can have as many as 10 key-value pairs. You must use JSON dot notation, not
                     bracket notation.

                    The keys can't start with ``"AWS"`` .

                    - *(string) --*

                      - *(string) --*

                  - **InputTemplate** *(string) --*

                    Input template where you specify placeholders that will be filled with the values of
                    the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
                    ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

                    If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
                    restrictions apply:

                    * The placeholder can't be used as an object key

                    * Object values can't include quote marks

                    The following example shows the syntax for using ``InputPathsMap`` and
                    ``InputTemplate`` .

                     ``"InputTransformer":``

                     ``{``

                     ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

                     ``"InputTemplate": "<instance> is in state <status>"``

                     ``}``

                    To have the ``InputTemplate`` include quote marks within a JSON string, escape each
                    quote marks with a slash, as in the following example:

                     ``"InputTransformer":``

                     ``{``

                     ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

                     ``"InputTemplate": "<instance> is in state \\"<status>\\""``

                     ``}``

                - **KinesisParameters** *(dict) --*

                  The custom parameter that you can use to control the shard assignment when the target is
                  a Kinesis data stream. If you don't include this parameter, the default is to use the
                  ``eventId`` as the partition key.

                  - **PartitionKeyPath** *(string) --*

                    The JSON path to be extracted from the event and used as the partition key. For more
                    information, see `Amazon Kinesis Streams Key Concepts
                    <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in
                    the *Amazon Kinesis Streams Developer Guide* .

                - **RunCommandParameters** *(dict) --*

                  Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

                  - **RunCommandTargets** *(list) --*

                    Currently, we support including only one ``RunCommandTarget`` block, which specifies
                    either an array of ``InstanceIds`` or a tag.

                    - *(dict) --*

                      Information about the EC2 instances that are to be sent the command, specified as
                      key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
                      key can specify multiple values.

                      - **Key** *(string) --*

                        Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

                      - **Values** *(list) --*

                        If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
                        is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

                        - *(string) --*

                - **EcsParameters** *(dict) --*

                  Contains the Amazon ECS task definition and task count to be used if the event target is
                  an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
                  <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in
                  the *Amazon EC2 Container Service Developer Guide* .

                  - **TaskDefinitionArn** *(string) --*

                    The ARN of the task definition to use if the event target is an Amazon ECS task.

                  - **TaskCount** *(integer) --*

                    The number of tasks to create based on ``TaskDefinition`` . The default is 1.

                  - **LaunchType** *(string) --*

                    Specifies the launch type on which your task is running. The launch type that you
                    specify here must match one of the launch type (compatibilities) of the target task.
                    The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon
                    ECS is supported. For more information, see `AWS Fargate on Amazon ECS
                    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in
                    the *Amazon Elastic Container Service Developer Guide* .

                  - **NetworkConfiguration** *(dict) --*

                    Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
                    specifies the VPC subnets and security groups associated with the task and whether a
                    public IP address is to be used. This structure is required if ``LaunchType`` is
                    ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

                    If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
                    ``awsvpc`` network mode, the task fails.

                    - **awsvpcConfiguration** *(dict) --*

                      Use this structure to specify the VPC subnets and security groups for the task and
                      whether a public IP address is to be used. This structure is relevant only for ECS
                      tasks that use the ``awsvpc`` network mode.

                      - **Subnets** *(list) --*

                        Specifies the subnets associated with the task. These subnets must all be in the
                        same VPC. You can specify as many as 16 subnets.

                        - *(string) --*

                      - **SecurityGroups** *(list) --*

                        Specifies the security groups associated with the task. These security groups must
                        all be in the same VPC. You can specify as many as five security groups. If you
                        don't specify a security group, the default security group for the VPC is used.

                        - *(string) --*

                      - **AssignPublicIp** *(string) --*

                        Specifies whether the task's elastic network interface receives a public IP
                        address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
                        is set to ``FARGATE`` .

                  - **PlatformVersion** *(string) --*

                    Specifies the platform version for the task. Specify only the numeric portion of the
                    platform version, such as ``1.1.0`` .

                    This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information
                    about valid platform versions, see `AWS Fargate Platform Versions
                    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__
                    in the *Amazon Elastic Container Service Developer Guide* .

                  - **Group** *(string) --*

                    Specifies an ECS task group for the task. The maximum length is 255 characters.

                - **BatchParameters** *(dict) --*

                  If the event target is an AWS Batch job, this contains the job definition, job name, and
                  other parameters. For more information, see `Jobs
                  <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
                  Guide* .

                  - **JobDefinition** *(string) --*

                    The ARN or name of the job definition to use if the event target is an AWS Batch job.
                    This job definition must already exist.

                  - **JobName** *(string) --*

                    The name to use for this execution of the job, if the target is an AWS Batch job.

                  - **ArrayProperties** *(dict) --*

                    The array properties for the submitted job, such as the size of the array. The array
                    size can be between 2 and 10,000. If you specify array properties for a job, it becomes
                    an array job. This parameter is used only if the target is an AWS Batch job.

                    - **Size** *(integer) --*

                      The size of the array, if this is an array batch job. Valid values are integers
                      between 2 and 10,000.

                  - **RetryStrategy** *(dict) --*

                    The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
                    strategy is the number of times to retry the failed job execution. Valid values are
                    1–10. When you specify a retry strategy here, it overrides the retry strategy defined
                    in the job definition.

                    - **Attempts** *(integer) --*

                      The number of times to attempt to retry, if the job fails. Valid values are 1–10.

                - **SqsParameters** *(dict) --*

                  Contains the message group ID to use when the target is a FIFO queue.

                  If you specify an SQS FIFO queue as a target, the queue must have content-based
                  deduplication enabled.

                  - **MessageGroupId** *(string) --*

                    The FIFO message group ID to use as the target.

        """
