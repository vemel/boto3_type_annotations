"Main interface for iotevents Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_iotevents.client as client_scope
from mypy_boto3_iotevents.type_defs import (
    ClientCreateDetectorModelResponseTypeDef,
    ClientCreateDetectorModeldetectorModelDefinitionTypeDef,
    ClientCreateDetectorModeltagsTypeDef,
    ClientCreateInputResponseTypeDef,
    ClientCreateInputinputDefinitionTypeDef,
    ClientCreateInputtagsTypeDef,
    ClientDescribeDetectorModelResponseTypeDef,
    ClientDescribeInputResponseTypeDef,
    ClientDescribeLoggingOptionsResponseTypeDef,
    ClientListDetectorModelVersionsResponseTypeDef,
    ClientListDetectorModelsResponseTypeDef,
    ClientListInputsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutLoggingOptionsloggingOptionsTypeDef,
    ClientTagResourcetagsTypeDef,
    ClientUpdateDetectorModelResponseTypeDef,
    ClientUpdateDetectorModeldetectorModelDefinitionTypeDef,
    ClientUpdateInputResponseTypeDef,
    ClientUpdateInputinputDefinitionTypeDef,
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
    def create_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: ClientCreateDetectorModeldetectorModelDefinitionTypeDef,
        roleArn: str,
        detectorModelDescription: str = None,
        key: str = None,
        tags: List[ClientCreateDetectorModeltagsTypeDef] = None,
        evaluationMethod: str = None,
    ) -> ClientCreateDetectorModelResponseTypeDef:
        """
        Creates a detector model.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/CreateDetectorModel>`_

        **Request Syntax**
        ::

          response = client.create_detector_model(
              detectorModelName='string',
              detectorModelDefinition={
                  'states': [
                      {
                          'stateName': 'string',
                          'onInput': {
                              'events': [
                                  {
                                      'eventName': 'string',
                                      'condition': 'string',
                                      'actions': [
                                          {
                                              'setVariable': {
                                                  'variableName': 'string',
                                                  'value': 'string'
                                              },
                                              'sns': {
                                                  'targetArn': 'string'
                                              },
                                              'iotTopicPublish': {
                                                  'mqttTopic': 'string'
                                              },
                                              'setTimer': {
                                                  'timerName': 'string',
                                                  'seconds': 123
                                              },
                                              'clearTimer': {
                                                  'timerName': 'string'
                                              },
                                              'resetTimer': {
                                                  'timerName': 'string'
                                              },
                                              'lambda': {
                                                  'functionArn': 'string'
                                              },
                                              'iotEvents': {
                                                  'inputName': 'string'
                                              },
                                              'sqs': {
                                                  'queueUrl': 'string',
                                                  'useBase64': True|False
                                              },
                                              'firehose': {
                                                  'deliveryStreamName': 'string',
                                                  'separator': 'string'
                                              }
                                          },
                                      ]
                                  },
                              ],
                              'transitionEvents': [
                                  {
                                      'eventName': 'string',
                                      'condition': 'string',
                                      'actions': [
                                          {
                                              'setVariable': {
                                                  'variableName': 'string',
                                                  'value': 'string'
                                              },
                                              'sns': {
                                                  'targetArn': 'string'
                                              },
                                              'iotTopicPublish': {
                                                  'mqttTopic': 'string'
                                              },
                                              'setTimer': {
                                                  'timerName': 'string',
                                                  'seconds': 123
                                              },
                                              'clearTimer': {
                                                  'timerName': 'string'
                                              },
                                              'resetTimer': {
                                                  'timerName': 'string'
                                              },
                                              'lambda': {
                                                  'functionArn': 'string'
                                              },
                                              'iotEvents': {
                                                  'inputName': 'string'
                                              },
                                              'sqs': {
                                                  'queueUrl': 'string',
                                                  'useBase64': True|False
                                              },
                                              'firehose': {
                                                  'deliveryStreamName': 'string',
                                                  'separator': 'string'
                                              }
                                          },
                                      ],
                                      'nextState': 'string'
                                  },
                              ]
                          },
                          'onEnter': {
                              'events': [
                                  {
                                      'eventName': 'string',
                                      'condition': 'string',
                                      'actions': [
                                          {
                                              'setVariable': {
                                                  'variableName': 'string',
                                                  'value': 'string'
                                              },
                                              'sns': {
                                                  'targetArn': 'string'
                                              },
                                              'iotTopicPublish': {
                                                  'mqttTopic': 'string'
                                              },
                                              'setTimer': {
                                                  'timerName': 'string',
                                                  'seconds': 123
                                              },
                                              'clearTimer': {
                                                  'timerName': 'string'
                                              },
                                              'resetTimer': {
                                                  'timerName': 'string'
                                              },
                                              'lambda': {
                                                  'functionArn': 'string'
                                              },
                                              'iotEvents': {
                                                  'inputName': 'string'
                                              },
                                              'sqs': {
                                                  'queueUrl': 'string',
                                                  'useBase64': True|False
                                              },
                                              'firehose': {
                                                  'deliveryStreamName': 'string',
                                                  'separator': 'string'
                                              }
                                          },
                                      ]
                                  },
                              ]
                          },
                          'onExit': {
                              'events': [
                                  {
                                      'eventName': 'string',
                                      'condition': 'string',
                                      'actions': [
                                          {
                                              'setVariable': {
                                                  'variableName': 'string',
                                                  'value': 'string'
                                              },
                                              'sns': {
                                                  'targetArn': 'string'
                                              },
                                              'iotTopicPublish': {
                                                  'mqttTopic': 'string'
                                              },
                                              'setTimer': {
                                                  'timerName': 'string',
                                                  'seconds': 123
                                              },
                                              'clearTimer': {
                                                  'timerName': 'string'
                                              },
                                              'resetTimer': {
                                                  'timerName': 'string'
                                              },
                                              'lambda': {
                                                  'functionArn': 'string'
                                              },
                                              'iotEvents': {
                                                  'inputName': 'string'
                                              },
                                              'sqs': {
                                                  'queueUrl': 'string',
                                                  'useBase64': True|False
                                              },
                                              'firehose': {
                                                  'deliveryStreamName': 'string',
                                                  'separator': 'string'
                                              }
                                          },
                                      ]
                                  },
                              ]
                          }
                      },
                  ],
                  'initialStateName': 'string'
              },
              detectorModelDescription='string',
              key='string',
              roleArn='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              evaluationMethod='BATCH'|'SERIAL'
          )
        :type detectorModelName: string
        :param detectorModelName: **[REQUIRED]**

          The name of the detector model.

        :type detectorModelDefinition: dict
        :param detectorModelDefinition: **[REQUIRED]**

          Information that defines how the detectors operate.

          - **states** *(list) --* **[REQUIRED]**

            Information about the states of the detector.

            - *(dict) --*

              Information that defines a state of a detector.

              - **stateName** *(string) --* **[REQUIRED]**

                The name of the state.

              - **onInput** *(dict) --*

                When an input is received and the ``"condition"`` is TRUE, perform the specified
                ``"actions"`` .

                - **events** *(list) --*

                  Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

                  - *(dict) --*

                    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

                    - **eventName** *(string) --* **[REQUIRED]**

                      The name of the event.

                    - **condition** *(string) --*

                      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                      performed. If not present, the actions are performed (=TRUE); if the expression
                      result is not a Boolean value, the actions are NOT performed (=FALSE).

                    - **actions** *(list) --*

                      The actions to be performed.

                      - *(dict) --*

                        An action to be performed when the ``"condition"`` is TRUE.

                        - **setVariable** *(dict) --*

                          Sets a variable to a specified value.

                          - **variableName** *(string) --* **[REQUIRED]**

                            The name of the variable.

                          - **value** *(string) --* **[REQUIRED]**

                            The new value of the variable.

                        - **sns** *(dict) --*

                          Sends an Amazon SNS message.

                          - **targetArn** *(string) --* **[REQUIRED]**

                            The ARN of the Amazon SNS target where the message is sent.

                        - **iotTopicPublish** *(dict) --*

                          Publishes an MQTT message with the given topic to the AWS IoT message broker.

                          - **mqttTopic** *(string) --* **[REQUIRED]**

                            The MQTT topic of the message.

                        - **setTimer** *(dict) --*

                          Information needed to set the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer.

                          - **seconds** *(integer) --* **[REQUIRED]**

                            The number of seconds until the timer expires. The minimum value is 60 seconds
                            to ensure accuracy.

                        - **clearTimer** *(dict) --*

                          Information needed to clear the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to clear.

                        - **resetTimer** *(dict) --*

                          Information needed to reset the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to reset.

                        - **lambda** *(dict) --*

                          Calls an AWS Lambda function, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **functionArn** *(string) --* **[REQUIRED]**

                            The ARN of the AWS Lambda function which is executed.

                        - **iotEvents** *(dict) --*

                          Sends an IoT Events input, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **inputName** *(string) --* **[REQUIRED]**

                            The name of the AWS IoT Events input where the data is sent.

                        - **sqs** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to an Amazon SQS queue.

                          - **queueUrl** *(string) --* **[REQUIRED]**

                            The URL of the Amazon SQS queue where the data is written.

                          - **useBase64** *(boolean) --*

                            Set this to TRUE if you want the data to be Base-64 encoded before it is
                            written to the queue. Otherwise, set this to FALSE.

                        - **firehose** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to a Kinesis Data Firehose delivery stream.

                          - **deliveryStreamName** *(string) --* **[REQUIRED]**

                            The name of the Kinesis Data Firehose delivery stream where the data is written.

                          - **separator** *(string) --*

                            A character separator that is used to separate records written to the Kinesis
                            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                            '\\r\\n' (Windows newline), ',' (comma).

                - **transitionEvents** *(list) --*

                  Specifies the actions performed, and the next state entered, when a ``"condition"``
                  evaluates to TRUE.

                  - *(dict) --*

                    Specifies the actions performed and the next state entered when a ``"condition"``
                    evaluates to TRUE.

                    - **eventName** *(string) --* **[REQUIRED]**

                      The name of the transition event.

                    - **condition** *(string) --* **[REQUIRED]**

                      [Required] A Boolean expression that when TRUE causes the actions to be performed and
                      the ``"nextState"`` to be entered.

                    - **actions** *(list) --*

                      The actions to be performed.

                      - *(dict) --*

                        An action to be performed when the ``"condition"`` is TRUE.

                        - **setVariable** *(dict) --*

                          Sets a variable to a specified value.

                          - **variableName** *(string) --* **[REQUIRED]**

                            The name of the variable.

                          - **value** *(string) --* **[REQUIRED]**

                            The new value of the variable.

                        - **sns** *(dict) --*

                          Sends an Amazon SNS message.

                          - **targetArn** *(string) --* **[REQUIRED]**

                            The ARN of the Amazon SNS target where the message is sent.

                        - **iotTopicPublish** *(dict) --*

                          Publishes an MQTT message with the given topic to the AWS IoT message broker.

                          - **mqttTopic** *(string) --* **[REQUIRED]**

                            The MQTT topic of the message.

                        - **setTimer** *(dict) --*

                          Information needed to set the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer.

                          - **seconds** *(integer) --* **[REQUIRED]**

                            The number of seconds until the timer expires. The minimum value is 60 seconds
                            to ensure accuracy.

                        - **clearTimer** *(dict) --*

                          Information needed to clear the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to clear.

                        - **resetTimer** *(dict) --*

                          Information needed to reset the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to reset.

                        - **lambda** *(dict) --*

                          Calls an AWS Lambda function, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **functionArn** *(string) --* **[REQUIRED]**

                            The ARN of the AWS Lambda function which is executed.

                        - **iotEvents** *(dict) --*

                          Sends an IoT Events input, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **inputName** *(string) --* **[REQUIRED]**

                            The name of the AWS IoT Events input where the data is sent.

                        - **sqs** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to an Amazon SQS queue.

                          - **queueUrl** *(string) --* **[REQUIRED]**

                            The URL of the Amazon SQS queue where the data is written.

                          - **useBase64** *(boolean) --*

                            Set this to TRUE if you want the data to be Base-64 encoded before it is
                            written to the queue. Otherwise, set this to FALSE.

                        - **firehose** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to a Kinesis Data Firehose delivery stream.

                          - **deliveryStreamName** *(string) --* **[REQUIRED]**

                            The name of the Kinesis Data Firehose delivery stream where the data is written.

                          - **separator** *(string) --*

                            A character separator that is used to separate records written to the Kinesis
                            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                            '\\r\\n' (Windows newline), ',' (comma).

                    - **nextState** *(string) --* **[REQUIRED]**

                      The next state to enter.

              - **onEnter** *(dict) --*

                When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

                - **events** *(list) --*

                  Specifies the actions that are performed when the state is entered and the
                  ``"condition"`` is TRUE.

                  - *(dict) --*

                    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

                    - **eventName** *(string) --* **[REQUIRED]**

                      The name of the event.

                    - **condition** *(string) --*

                      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                      performed. If not present, the actions are performed (=TRUE); if the expression
                      result is not a Boolean value, the actions are NOT performed (=FALSE).

                    - **actions** *(list) --*

                      The actions to be performed.

                      - *(dict) --*

                        An action to be performed when the ``"condition"`` is TRUE.

                        - **setVariable** *(dict) --*

                          Sets a variable to a specified value.

                          - **variableName** *(string) --* **[REQUIRED]**

                            The name of the variable.

                          - **value** *(string) --* **[REQUIRED]**

                            The new value of the variable.

                        - **sns** *(dict) --*

                          Sends an Amazon SNS message.

                          - **targetArn** *(string) --* **[REQUIRED]**

                            The ARN of the Amazon SNS target where the message is sent.

                        - **iotTopicPublish** *(dict) --*

                          Publishes an MQTT message with the given topic to the AWS IoT message broker.

                          - **mqttTopic** *(string) --* **[REQUIRED]**

                            The MQTT topic of the message.

                        - **setTimer** *(dict) --*

                          Information needed to set the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer.

                          - **seconds** *(integer) --* **[REQUIRED]**

                            The number of seconds until the timer expires. The minimum value is 60 seconds
                            to ensure accuracy.

                        - **clearTimer** *(dict) --*

                          Information needed to clear the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to clear.

                        - **resetTimer** *(dict) --*

                          Information needed to reset the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to reset.

                        - **lambda** *(dict) --*

                          Calls an AWS Lambda function, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **functionArn** *(string) --* **[REQUIRED]**

                            The ARN of the AWS Lambda function which is executed.

                        - **iotEvents** *(dict) --*

                          Sends an IoT Events input, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **inputName** *(string) --* **[REQUIRED]**

                            The name of the AWS IoT Events input where the data is sent.

                        - **sqs** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to an Amazon SQS queue.

                          - **queueUrl** *(string) --* **[REQUIRED]**

                            The URL of the Amazon SQS queue where the data is written.

                          - **useBase64** *(boolean) --*

                            Set this to TRUE if you want the data to be Base-64 encoded before it is
                            written to the queue. Otherwise, set this to FALSE.

                        - **firehose** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to a Kinesis Data Firehose delivery stream.

                          - **deliveryStreamName** *(string) --* **[REQUIRED]**

                            The name of the Kinesis Data Firehose delivery stream where the data is written.

                          - **separator** *(string) --*

                            A character separator that is used to separate records written to the Kinesis
                            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                            '\\r\\n' (Windows newline), ',' (comma).

              - **onExit** *(dict) --*

                When exiting this state, perform these ``"actions"`` if the specified ``"condition"`` is
                TRUE.

                - **events** *(list) --*

                  Specifies the ``"actions"`` that are performed when the state is exited and the
                  ``"condition"`` is TRUE.

                  - *(dict) --*

                    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

                    - **eventName** *(string) --* **[REQUIRED]**

                      The name of the event.

                    - **condition** *(string) --*

                      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                      performed. If not present, the actions are performed (=TRUE); if the expression
                      result is not a Boolean value, the actions are NOT performed (=FALSE).

                    - **actions** *(list) --*

                      The actions to be performed.

                      - *(dict) --*

                        An action to be performed when the ``"condition"`` is TRUE.

                        - **setVariable** *(dict) --*

                          Sets a variable to a specified value.

                          - **variableName** *(string) --* **[REQUIRED]**

                            The name of the variable.

                          - **value** *(string) --* **[REQUIRED]**

                            The new value of the variable.

                        - **sns** *(dict) --*

                          Sends an Amazon SNS message.

                          - **targetArn** *(string) --* **[REQUIRED]**

                            The ARN of the Amazon SNS target where the message is sent.

                        - **iotTopicPublish** *(dict) --*

                          Publishes an MQTT message with the given topic to the AWS IoT message broker.

                          - **mqttTopic** *(string) --* **[REQUIRED]**

                            The MQTT topic of the message.

                        - **setTimer** *(dict) --*

                          Information needed to set the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer.

                          - **seconds** *(integer) --* **[REQUIRED]**

                            The number of seconds until the timer expires. The minimum value is 60 seconds
                            to ensure accuracy.

                        - **clearTimer** *(dict) --*

                          Information needed to clear the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to clear.

                        - **resetTimer** *(dict) --*

                          Information needed to reset the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to reset.

                        - **lambda** *(dict) --*

                          Calls an AWS Lambda function, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **functionArn** *(string) --* **[REQUIRED]**

                            The ARN of the AWS Lambda function which is executed.

                        - **iotEvents** *(dict) --*

                          Sends an IoT Events input, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **inputName** *(string) --* **[REQUIRED]**

                            The name of the AWS IoT Events input where the data is sent.

                        - **sqs** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to an Amazon SQS queue.

                          - **queueUrl** *(string) --* **[REQUIRED]**

                            The URL of the Amazon SQS queue where the data is written.

                          - **useBase64** *(boolean) --*

                            Set this to TRUE if you want the data to be Base-64 encoded before it is
                            written to the queue. Otherwise, set this to FALSE.

                        - **firehose** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to a Kinesis Data Firehose delivery stream.

                          - **deliveryStreamName** *(string) --* **[REQUIRED]**

                            The name of the Kinesis Data Firehose delivery stream where the data is written.

                          - **separator** *(string) --*

                            A character separator that is used to separate records written to the Kinesis
                            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                            '\\r\\n' (Windows newline), ',' (comma).

          - **initialStateName** *(string) --* **[REQUIRED]**

            The state that is entered at the creation of each detector (instance).

        :type detectorModelDescription: string
        :param detectorModelDescription:

          A brief description of the detector model.

        :type key: string
        :param key:

          The input attribute key used to identify a device or system to create a detector (an instance of
          the detector model) and then to route each input received to the appropriate detector (instance).
          This parameter uses a JSON-path expression to specify the attribute-value pair in the message
          payload of each input that is used to identify the device associated with the input.

        :type roleArn: string
        :param roleArn: **[REQUIRED]**

          The ARN of the role that grants permission to AWS IoT Events to perform its operations.

        :type tags: list
        :param tags:

          Metadata that can be used to manage the detector model.

          - *(dict) --*

            Metadata that can be used to manage the resource.

            - **key** *(string) --* **[REQUIRED]**

              The tag's key.

            - **value** *(string) --* **[REQUIRED]**

              The tag's value.

        :type evaluationMethod: string
        :param evaluationMethod:

          When set to ``SERIAL`` , variables are updated and event conditions evaluated in the order that
          the events are defined. When set to ``BATCH`` , variables are updated and events performed only
          after all event conditions are evaluated.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'detectorModelConfiguration': {
                    'detectorModelName': 'string',
                    'detectorModelVersion': 'string',
                    'detectorModelDescription': 'string',
                    'detectorModelArn': 'string',
                    'roleArn': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdateTime': datetime(2015, 1, 1),
                    'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
                    'key': 'string',
                    'evaluationMethod': 'BATCH'|'SERIAL'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **detectorModelConfiguration** *(dict) --*

              Information about how the detector model is configured.

              - **detectorModelName** *(string) --*

                The name of the detector model.

              - **detectorModelVersion** *(string) --*

                The version of the detector model.

              - **detectorModelDescription** *(string) --*

                A brief description of the detector model.

              - **detectorModelArn** *(string) --*

                The ARN of the detector model.

              - **roleArn** *(string) --*

                The ARN of the role that grants permission to AWS IoT Events to perform its operations.

              - **creationTime** *(datetime) --*

                The time the detector model was created.

              - **lastUpdateTime** *(datetime) --*

                The time the detector model was last updated.

              - **status** *(string) --*

                The status of the detector model.

              - **key** *(string) --*

                The input attribute key used to identify a device or system to create a detector (an
                instance of the detector model) and then to route each input received to the appropriate
                detector (instance). This parameter uses a JSON-path expression to specify the
                attribute-value pair in the message payload of each input that is used to identify the
                device associated with the input.

              - **evaluationMethod** *(string) --*

                When set to ``SERIAL`` , variables are updated and event conditions evaluated in the order
                that the events are defined. When set to ``BATCH`` , variables are updated and events
                performed only after all event conditions are evaluated.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_input(
        self,
        inputName: str,
        inputDefinition: ClientCreateInputinputDefinitionTypeDef,
        inputDescription: str = None,
        tags: List[ClientCreateInputtagsTypeDef] = None,
    ) -> ClientCreateInputResponseTypeDef:
        """
        Creates an input.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/CreateInput>`_

        **Request Syntax**
        ::

          response = client.create_input(
              inputName='string',
              inputDescription='string',
              inputDefinition={
                  'attributes': [
                      {
                          'jsonPath': 'string'
                      },
                  ]
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type inputName: string
        :param inputName: **[REQUIRED]**

          The name you want to give to the input.

        :type inputDescription: string
        :param inputDescription:

          A brief description of the input.

        :type inputDefinition: dict
        :param inputDefinition: **[REQUIRED]**

          The definition of the input.

          - **attributes** *(list) --* **[REQUIRED]**

            The attributes from the JSON payload that are made available by the input. Inputs are derived
            from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
            contains a JSON payload, and those attributes (and their paired values) specified here are
            available for use in the ``"condition"`` expressions used by detectors that monitor this input.

            - *(dict) --*

              The attributes from the JSON payload that are made available by the input. Inputs are derived
              from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
              contains a JSON payload, and those attributes (and their paired values) specified here are
              available for use in the ``condition`` expressions used by detectors.

              - **jsonPath** *(string) --* **[REQUIRED]**

                An expression that specifies an attribute-value pair in a JSON structure. Use this to
                specify an attribute from the JSON payload that is made available by the input. Inputs are
                derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
                message contains a JSON payload, and the attribute (and its paired value) specified here
                are available for use in the ``"condition"`` expressions used by detectors.

                Syntax: ``<field-name>.<field-name>...``

        :type tags: list
        :param tags:

          Metadata that can be used to manage the input.

          - *(dict) --*

            Metadata that can be used to manage the resource.

            - **key** *(string) --* **[REQUIRED]**

              The tag's key.

            - **value** *(string) --* **[REQUIRED]**

              The tag's value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'inputConfiguration': {
                    'inputName': 'string',
                    'inputDescription': 'string',
                    'inputArn': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdateTime': datetime(2015, 1, 1),
                    'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **inputConfiguration** *(dict) --*

              Information about the configuration of the input.

              - **inputName** *(string) --*

                The name of the input.

              - **inputDescription** *(string) --*

                A brief description of the input.

              - **inputArn** *(string) --*

                The ARN of the input.

              - **creationTime** *(datetime) --*

                The time the input was created.

              - **lastUpdateTime** *(datetime) --*

                The last time the input was updated.

              - **status** *(string) --*

                The status of the input.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_detector_model(self, detectorModelName: str) -> Dict[str, Any]:
        """
        Deletes a detector model. Any active instances of the detector model are also deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/DeleteDetectorModel>`_

        **Request Syntax**
        ::

          response = client.delete_detector_model(
              detectorModelName='string'
          )
        :type detectorModelName: string
        :param detectorModelName: **[REQUIRED]**

          The name of the detector model to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_input(self, inputName: str) -> Dict[str, Any]:
        """
        Deletes an input.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/DeleteInput>`_

        **Request Syntax**
        ::

          response = client.delete_input(
              inputName='string'
          )
        :type inputName: string
        :param inputName: **[REQUIRED]**

          The name of the input to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_detector_model(
        self, detectorModelName: str, detectorModelVersion: str = None
    ) -> ClientDescribeDetectorModelResponseTypeDef:
        """
        Describes a detector model. If the ``"version"`` parameter is not specified, information about the
        latest version is returned.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/DescribeDetectorModel>`_

        **Request Syntax**
        ::

          response = client.describe_detector_model(
              detectorModelName='string',
              detectorModelVersion='string'
          )
        :type detectorModelName: string
        :param detectorModelName: **[REQUIRED]**

          The name of the detector model.

        :type detectorModelVersion: string
        :param detectorModelVersion:

          The version of the detector model.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'detectorModel': {
                    'detectorModelDefinition': {
                        'states': [
                            {
                                'stateName': 'string',
                                'onInput': {
                                    'events': [
                                        {
                                            'eventName': 'string',
                                            'condition': 'string',
                                            'actions': [
                                                {
                                                    'setVariable': {
                                                        'variableName': 'string',
                                                        'value': 'string'
                                                    },
                                                    'sns': {
                                                        'targetArn': 'string'
                                                    },
                                                    'iotTopicPublish': {
                                                        'mqttTopic': 'string'
                                                    },
                                                    'setTimer': {
                                                        'timerName': 'string',
                                                        'seconds': 123
                                                    },
                                                    'clearTimer': {
                                                        'timerName': 'string'
                                                    },
                                                    'resetTimer': {
                                                        'timerName': 'string'
                                                    },
                                                    'lambda': {
                                                        'functionArn': 'string'
                                                    },
                                                    'iotEvents': {
                                                        'inputName': 'string'
                                                    },
                                                    'sqs': {
                                                        'queueUrl': 'string',
                                                        'useBase64': True|False
                                                    },
                                                    'firehose': {
                                                        'deliveryStreamName': 'string',
                                                        'separator': 'string'
                                                    }
                                                },
                                            ]
                                        },
                                    ],
                                    'transitionEvents': [
                                        {
                                            'eventName': 'string',
                                            'condition': 'string',
                                            'actions': [
                                                {
                                                    'setVariable': {
                                                        'variableName': 'string',
                                                        'value': 'string'
                                                    },
                                                    'sns': {
                                                        'targetArn': 'string'
                                                    },
                                                    'iotTopicPublish': {
                                                        'mqttTopic': 'string'
                                                    },
                                                    'setTimer': {
                                                        'timerName': 'string',
                                                        'seconds': 123
                                                    },
                                                    'clearTimer': {
                                                        'timerName': 'string'
                                                    },
                                                    'resetTimer': {
                                                        'timerName': 'string'
                                                    },
                                                    'lambda': {
                                                        'functionArn': 'string'
                                                    },
                                                    'iotEvents': {
                                                        'inputName': 'string'
                                                    },
                                                    'sqs': {
                                                        'queueUrl': 'string',
                                                        'useBase64': True|False
                                                    },
                                                    'firehose': {
                                                        'deliveryStreamName': 'string',
                                                        'separator': 'string'
                                                    }
                                                },
                                            ],
                                            'nextState': 'string'
                                        },
                                    ]
                                },
                                'onEnter': {
                                    'events': [
                                        {
                                            'eventName': 'string',
                                            'condition': 'string',
                                            'actions': [
                                                {
                                                    'setVariable': {
                                                        'variableName': 'string',
                                                        'value': 'string'
                                                    },
                                                    'sns': {
                                                        'targetArn': 'string'
                                                    },
                                                    'iotTopicPublish': {
                                                        'mqttTopic': 'string'
                                                    },
                                                    'setTimer': {
                                                        'timerName': 'string',
                                                        'seconds': 123
                                                    },
                                                    'clearTimer': {
                                                        'timerName': 'string'
                                                    },
                                                    'resetTimer': {
                                                        'timerName': 'string'
                                                    },
                                                    'lambda': {
                                                        'functionArn': 'string'
                                                    },
                                                    'iotEvents': {
                                                        'inputName': 'string'
                                                    },
                                                    'sqs': {
                                                        'queueUrl': 'string',
                                                        'useBase64': True|False
                                                    },
                                                    'firehose': {
                                                        'deliveryStreamName': 'string',
                                                        'separator': 'string'
                                                    }
                                                },
                                            ]
                                        },
                                    ]
                                },
                                'onExit': {
                                    'events': [
                                        {
                                            'eventName': 'string',
                                            'condition': 'string',
                                            'actions': [
                                                {
                                                    'setVariable': {
                                                        'variableName': 'string',
                                                        'value': 'string'
                                                    },
                                                    'sns': {
                                                        'targetArn': 'string'
                                                    },
                                                    'iotTopicPublish': {
                                                        'mqttTopic': 'string'
                                                    },
                                                    'setTimer': {
                                                        'timerName': 'string',
                                                        'seconds': 123
                                                    },
                                                    'clearTimer': {
                                                        'timerName': 'string'
                                                    },
                                                    'resetTimer': {
                                                        'timerName': 'string'
                                                    },
                                                    'lambda': {
                                                        'functionArn': 'string'
                                                    },
                                                    'iotEvents': {
                                                        'inputName': 'string'
                                                    },
                                                    'sqs': {
                                                        'queueUrl': 'string',
                                                        'useBase64': True|False
                                                    },
                                                    'firehose': {
                                                        'deliveryStreamName': 'string',
                                                        'separator': 'string'
                                                    }
                                                },
                                            ]
                                        },
                                    ]
                                }
                            },
                        ],
                        'initialStateName': 'string'
                    },
                    'detectorModelConfiguration': {
                        'detectorModelName': 'string',
                        'detectorModelVersion': 'string',
                        'detectorModelDescription': 'string',
                        'detectorModelArn': 'string',
                        'roleArn': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
                        'key': 'string',
                        'evaluationMethod': 'BATCH'|'SERIAL'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **detectorModel** *(dict) --*

              Information about the detector model.

              - **detectorModelDefinition** *(dict) --*

                Information that defines how a detector operates.

                - **states** *(list) --*

                  Information about the states of the detector.

                  - *(dict) --*

                    Information that defines a state of a detector.

                    - **stateName** *(string) --*

                      The name of the state.

                    - **onInput** *(dict) --*

                      When an input is received and the ``"condition"`` is TRUE, perform the specified
                      ``"actions"`` .

                      - **events** *(list) --*

                        Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

                        - *(dict) --*

                          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                          TRUE.

                          - **eventName** *(string) --*

                            The name of the event.

                          - **condition** *(string) --*

                            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                            performed. If not present, the actions are performed (=TRUE); if the expression
                            result is not a Boolean value, the actions are NOT performed (=FALSE).

                          - **actions** *(list) --*

                            The actions to be performed.

                            - *(dict) --*

                              An action to be performed when the ``"condition"`` is TRUE.

                              - **setVariable** *(dict) --*

                                Sets a variable to a specified value.

                                - **variableName** *(string) --*

                                  The name of the variable.

                                - **value** *(string) --*

                                  The new value of the variable.

                              - **sns** *(dict) --*

                                Sends an Amazon SNS message.

                                - **targetArn** *(string) --*

                                  The ARN of the Amazon SNS target where the message is sent.

                              - **iotTopicPublish** *(dict) --*

                                Publishes an MQTT message with the given topic to the AWS IoT message
                                broker.

                                - **mqttTopic** *(string) --*

                                  The MQTT topic of the message.

                              - **setTimer** *(dict) --*

                                Information needed to set the timer.

                                - **timerName** *(string) --*

                                  The name of the timer.

                                - **seconds** *(integer) --*

                                  The number of seconds until the timer expires. The minimum value is 60
                                  seconds to ensure accuracy.

                              - **clearTimer** *(dict) --*

                                Information needed to clear the timer.

                                - **timerName** *(string) --*

                                  The name of the timer to clear.

                              - **resetTimer** *(dict) --*

                                Information needed to reset the timer.

                                - **timerName** *(string) --*

                                  The name of the timer to reset.

                              - **lambda** *(dict) --*

                                Calls an AWS Lambda function, passing in information about the detector
                                model instance and the event which triggered the action.

                                - **functionArn** *(string) --*

                                  The ARN of the AWS Lambda function which is executed.

                              - **iotEvents** *(dict) --*

                                Sends an IoT Events input, passing in information about the detector model
                                instance and the event which triggered the action.

                                - **inputName** *(string) --*

                                  The name of the AWS IoT Events input where the data is sent.

                              - **sqs** *(dict) --*

                                Sends information about the detector model instance and the event which
                                triggered the action to an Amazon SQS queue.

                                - **queueUrl** *(string) --*

                                  The URL of the Amazon SQS queue where the data is written.

                                - **useBase64** *(boolean) --*

                                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                                  written to the queue. Otherwise, set this to FALSE.

                              - **firehose** *(dict) --*

                                Sends information about the detector model instance and the event which
                                triggered the action to a Kinesis Data Firehose delivery stream.

                                - **deliveryStreamName** *(string) --*

                                  The name of the Kinesis Data Firehose delivery stream where the data is
                                  written.

                                - **separator** *(string) --*

                                  A character separator that is used to separate records written to the
                                  Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                                  '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

                      - **transitionEvents** *(list) --*

                        Specifies the actions performed, and the next state entered, when a ``"condition"``
                        evaluates to TRUE.

                        - *(dict) --*

                          Specifies the actions performed and the next state entered when a ``"condition"``
                          evaluates to TRUE.

                          - **eventName** *(string) --*

                            The name of the transition event.

                          - **condition** *(string) --*

                            [Required] A Boolean expression that when TRUE causes the actions to be
                            performed and the ``"nextState"`` to be entered.

                          - **actions** *(list) --*

                            The actions to be performed.

                            - *(dict) --*

                              An action to be performed when the ``"condition"`` is TRUE.

                              - **setVariable** *(dict) --*

                                Sets a variable to a specified value.

                                - **variableName** *(string) --*

                                  The name of the variable.

                                - **value** *(string) --*

                                  The new value of the variable.

                              - **sns** *(dict) --*

                                Sends an Amazon SNS message.

                                - **targetArn** *(string) --*

                                  The ARN of the Amazon SNS target where the message is sent.

                              - **iotTopicPublish** *(dict) --*

                                Publishes an MQTT message with the given topic to the AWS IoT message
                                broker.

                                - **mqttTopic** *(string) --*

                                  The MQTT topic of the message.

                              - **setTimer** *(dict) --*

                                Information needed to set the timer.

                                - **timerName** *(string) --*

                                  The name of the timer.

                                - **seconds** *(integer) --*

                                  The number of seconds until the timer expires. The minimum value is 60
                                  seconds to ensure accuracy.

                              - **clearTimer** *(dict) --*

                                Information needed to clear the timer.

                                - **timerName** *(string) --*

                                  The name of the timer to clear.

                              - **resetTimer** *(dict) --*

                                Information needed to reset the timer.

                                - **timerName** *(string) --*

                                  The name of the timer to reset.

                              - **lambda** *(dict) --*

                                Calls an AWS Lambda function, passing in information about the detector
                                model instance and the event which triggered the action.

                                - **functionArn** *(string) --*

                                  The ARN of the AWS Lambda function which is executed.

                              - **iotEvents** *(dict) --*

                                Sends an IoT Events input, passing in information about the detector model
                                instance and the event which triggered the action.

                                - **inputName** *(string) --*

                                  The name of the AWS IoT Events input where the data is sent.

                              - **sqs** *(dict) --*

                                Sends information about the detector model instance and the event which
                                triggered the action to an Amazon SQS queue.

                                - **queueUrl** *(string) --*

                                  The URL of the Amazon SQS queue where the data is written.

                                - **useBase64** *(boolean) --*

                                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                                  written to the queue. Otherwise, set this to FALSE.

                              - **firehose** *(dict) --*

                                Sends information about the detector model instance and the event which
                                triggered the action to a Kinesis Data Firehose delivery stream.

                                - **deliveryStreamName** *(string) --*

                                  The name of the Kinesis Data Firehose delivery stream where the data is
                                  written.

                                - **separator** *(string) --*

                                  A character separator that is used to separate records written to the
                                  Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                                  '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

                          - **nextState** *(string) --*

                            The next state to enter.

                    - **onEnter** *(dict) --*

                      When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

                      - **events** *(list) --*

                        Specifies the actions that are performed when the state is entered and the
                        ``"condition"`` is TRUE.

                        - *(dict) --*

                          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                          TRUE.

                          - **eventName** *(string) --*

                            The name of the event.

                          - **condition** *(string) --*

                            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                            performed. If not present, the actions are performed (=TRUE); if the expression
                            result is not a Boolean value, the actions are NOT performed (=FALSE).

                          - **actions** *(list) --*

                            The actions to be performed.

                            - *(dict) --*

                              An action to be performed when the ``"condition"`` is TRUE.

                              - **setVariable** *(dict) --*

                                Sets a variable to a specified value.

                                - **variableName** *(string) --*

                                  The name of the variable.

                                - **value** *(string) --*

                                  The new value of the variable.

                              - **sns** *(dict) --*

                                Sends an Amazon SNS message.

                                - **targetArn** *(string) --*

                                  The ARN of the Amazon SNS target where the message is sent.

                              - **iotTopicPublish** *(dict) --*

                                Publishes an MQTT message with the given topic to the AWS IoT message
                                broker.

                                - **mqttTopic** *(string) --*

                                  The MQTT topic of the message.

                              - **setTimer** *(dict) --*

                                Information needed to set the timer.

                                - **timerName** *(string) --*

                                  The name of the timer.

                                - **seconds** *(integer) --*

                                  The number of seconds until the timer expires. The minimum value is 60
                                  seconds to ensure accuracy.

                              - **clearTimer** *(dict) --*

                                Information needed to clear the timer.

                                - **timerName** *(string) --*

                                  The name of the timer to clear.

                              - **resetTimer** *(dict) --*

                                Information needed to reset the timer.

                                - **timerName** *(string) --*

                                  The name of the timer to reset.

                              - **lambda** *(dict) --*

                                Calls an AWS Lambda function, passing in information about the detector
                                model instance and the event which triggered the action.

                                - **functionArn** *(string) --*

                                  The ARN of the AWS Lambda function which is executed.

                              - **iotEvents** *(dict) --*

                                Sends an IoT Events input, passing in information about the detector model
                                instance and the event which triggered the action.

                                - **inputName** *(string) --*

                                  The name of the AWS IoT Events input where the data is sent.

                              - **sqs** *(dict) --*

                                Sends information about the detector model instance and the event which
                                triggered the action to an Amazon SQS queue.

                                - **queueUrl** *(string) --*

                                  The URL of the Amazon SQS queue where the data is written.

                                - **useBase64** *(boolean) --*

                                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                                  written to the queue. Otherwise, set this to FALSE.

                              - **firehose** *(dict) --*

                                Sends information about the detector model instance and the event which
                                triggered the action to a Kinesis Data Firehose delivery stream.

                                - **deliveryStreamName** *(string) --*

                                  The name of the Kinesis Data Firehose delivery stream where the data is
                                  written.

                                - **separator** *(string) --*

                                  A character separator that is used to separate records written to the
                                  Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                                  '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

                    - **onExit** *(dict) --*

                      When exiting this state, perform these ``"actions"`` if the specified ``"condition"``
                      is TRUE.

                      - **events** *(list) --*

                        Specifies the ``"actions"`` that are performed when the state is exited and the
                        ``"condition"`` is TRUE.

                        - *(dict) --*

                          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                          TRUE.

                          - **eventName** *(string) --*

                            The name of the event.

                          - **condition** *(string) --*

                            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                            performed. If not present, the actions are performed (=TRUE); if the expression
                            result is not a Boolean value, the actions are NOT performed (=FALSE).

                          - **actions** *(list) --*

                            The actions to be performed.

                            - *(dict) --*

                              An action to be performed when the ``"condition"`` is TRUE.

                              - **setVariable** *(dict) --*

                                Sets a variable to a specified value.

                                - **variableName** *(string) --*

                                  The name of the variable.

                                - **value** *(string) --*

                                  The new value of the variable.

                              - **sns** *(dict) --*

                                Sends an Amazon SNS message.

                                - **targetArn** *(string) --*

                                  The ARN of the Amazon SNS target where the message is sent.

                              - **iotTopicPublish** *(dict) --*

                                Publishes an MQTT message with the given topic to the AWS IoT message
                                broker.

                                - **mqttTopic** *(string) --*

                                  The MQTT topic of the message.

                              - **setTimer** *(dict) --*

                                Information needed to set the timer.

                                - **timerName** *(string) --*

                                  The name of the timer.

                                - **seconds** *(integer) --*

                                  The number of seconds until the timer expires. The minimum value is 60
                                  seconds to ensure accuracy.

                              - **clearTimer** *(dict) --*

                                Information needed to clear the timer.

                                - **timerName** *(string) --*

                                  The name of the timer to clear.

                              - **resetTimer** *(dict) --*

                                Information needed to reset the timer.

                                - **timerName** *(string) --*

                                  The name of the timer to reset.

                              - **lambda** *(dict) --*

                                Calls an AWS Lambda function, passing in information about the detector
                                model instance and the event which triggered the action.

                                - **functionArn** *(string) --*

                                  The ARN of the AWS Lambda function which is executed.

                              - **iotEvents** *(dict) --*

                                Sends an IoT Events input, passing in information about the detector model
                                instance and the event which triggered the action.

                                - **inputName** *(string) --*

                                  The name of the AWS IoT Events input where the data is sent.

                              - **sqs** *(dict) --*

                                Sends information about the detector model instance and the event which
                                triggered the action to an Amazon SQS queue.

                                - **queueUrl** *(string) --*

                                  The URL of the Amazon SQS queue where the data is written.

                                - **useBase64** *(boolean) --*

                                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                                  written to the queue. Otherwise, set this to FALSE.

                              - **firehose** *(dict) --*

                                Sends information about the detector model instance and the event which
                                triggered the action to a Kinesis Data Firehose delivery stream.

                                - **deliveryStreamName** *(string) --*

                                  The name of the Kinesis Data Firehose delivery stream where the data is
                                  written.

                                - **separator** *(string) --*

                                  A character separator that is used to separate records written to the
                                  Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                                  '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

                - **initialStateName** *(string) --*

                  The state that is entered at the creation of each detector (instance).

              - **detectorModelConfiguration** *(dict) --*

                Information about how the detector is configured.

                - **detectorModelName** *(string) --*

                  The name of the detector model.

                - **detectorModelVersion** *(string) --*

                  The version of the detector model.

                - **detectorModelDescription** *(string) --*

                  A brief description of the detector model.

                - **detectorModelArn** *(string) --*

                  The ARN of the detector model.

                - **roleArn** *(string) --*

                  The ARN of the role that grants permission to AWS IoT Events to perform its operations.

                - **creationTime** *(datetime) --*

                  The time the detector model was created.

                - **lastUpdateTime** *(datetime) --*

                  The time the detector model was last updated.

                - **status** *(string) --*

                  The status of the detector model.

                - **key** *(string) --*

                  The input attribute key used to identify a device or system to create a detector (an
                  instance of the detector model) and then to route each input received to the appropriate
                  detector (instance). This parameter uses a JSON-path expression to specify the
                  attribute-value pair in the message payload of each input that is used to identify the
                  device associated with the input.

                - **evaluationMethod** *(string) --*

                  When set to ``SERIAL`` , variables are updated and event conditions evaluated in the
                  order that the events are defined. When set to ``BATCH`` , variables are updated and
                  events performed only after all event conditions are evaluated.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_input(self, inputName: str) -> ClientDescribeInputResponseTypeDef:
        """
        Describes an input.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/DescribeInput>`_

        **Request Syntax**
        ::

          response = client.describe_input(
              inputName='string'
          )
        :type inputName: string
        :param inputName: **[REQUIRED]**

          The name of the input.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'input': {
                    'inputConfiguration': {
                        'inputName': 'string',
                        'inputDescription': 'string',
                        'inputArn': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
                    },
                    'inputDefinition': {
                        'attributes': [
                            {
                                'jsonPath': 'string'
                            },
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **input** *(dict) --*

              Information about the input.

              - **inputConfiguration** *(dict) --*

                Information about the configuration of an input.

                - **inputName** *(string) --*

                  The name of the input.

                - **inputDescription** *(string) --*

                  A brief description of the input.

                - **inputArn** *(string) --*

                  The ARN of the input.

                - **creationTime** *(datetime) --*

                  The time the input was created.

                - **lastUpdateTime** *(datetime) --*

                  The last time the input was updated.

                - **status** *(string) --*

                  The status of the input.

              - **inputDefinition** *(dict) --*

                The definition of the input.

                - **attributes** *(list) --*

                  The attributes from the JSON payload that are made available by the input. Inputs are
                  derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each
                  such message contains a JSON payload, and those attributes (and their paired values)
                  specified here are available for use in the ``"condition"`` expressions used by detectors
                  that monitor this input.

                  - *(dict) --*

                    The attributes from the JSON payload that are made available by the input. Inputs are
                    derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` .
                    Each such message contains a JSON payload, and those attributes (and their paired
                    values) specified here are available for use in the ``condition`` expressions used by
                    detectors.

                    - **jsonPath** *(string) --*

                      An expression that specifies an attribute-value pair in a JSON structure. Use this to
                      specify an attribute from the JSON payload that is made available by the input.
                      Inputs are derived from messages sent to the AWS IoT Events system
                      (``BatchPutMessage`` ). Each such message contains a JSON payload, and the attribute
                      (and its paired value) specified here are available for use in the ``"condition"``
                      expressions used by detectors.

                      Syntax: ``<field-name>.<field-name>...``

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_logging_options(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeLoggingOptionsResponseTypeDef:
        """
        Retrieves the current settings of the AWS IoT Events logging options.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/DescribeLoggingOptions>`_

        **Request Syntax**
        ::

          response = client.describe_logging_options()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'loggingOptions': {
                    'roleArn': 'string',
                    'level': 'ERROR'|'INFO'|'DEBUG',
                    'enabled': True|False,
                    'detectorDebugOptions': [
                        {
                            'detectorModelName': 'string',
                            'keyValue': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **loggingOptions** *(dict) --*

              The current settings of the AWS IoT Events logging options.

              - **roleArn** *(string) --*

                The ARN of the role that grants permission to AWS IoT Events to perform logging.

              - **level** *(string) --*

                The logging level.

              - **enabled** *(boolean) --*

                If TRUE, logging is enabled for AWS IoT Events.

              - **detectorDebugOptions** *(list) --*

                Information that identifies those detector models and their detectors (instances) for which
                the logging level is given.

                - *(dict) --*

                  The detector model and the specific detectors (instances) for which the logging level is
                  given.

                  - **detectorModelName** *(string) --*

                    The name of the detector model.

                  - **keyValue** *(string) --*

                    The value of the input attribute key used to create the detector (the instance of the
                    detector model).

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
    def list_detector_model_versions(
        self, detectorModelName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListDetectorModelVersionsResponseTypeDef:
        """
        Lists all the versions of a detector model. Only the metadata associated with each detector model
        version is returned.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/ListDetectorModelVersions>`_

        **Request Syntax**
        ::

          response = client.list_detector_model_versions(
              detectorModelName='string',
              nextToken='string',
              maxResults=123
          )
        :type detectorModelName: string
        :param detectorModelName: **[REQUIRED]**

          The name of the detector model whose versions are returned.

        :type nextToken: string
        :param nextToken:

          The token for the next set of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return at one time.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'detectorModelVersionSummaries': [
                    {
                        'detectorModelName': 'string',
                        'detectorModelVersion': 'string',
                        'detectorModelArn': 'string',
                        'roleArn': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
                        'evaluationMethod': 'BATCH'|'SERIAL'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **detectorModelVersionSummaries** *(list) --*

              Summary information about the detector model versions.

              - *(dict) --*

                Information about the detector model version.

                - **detectorModelName** *(string) --*

                  The name of the detector model.

                - **detectorModelVersion** *(string) --*

                  The ID of the detector model version.

                - **detectorModelArn** *(string) --*

                  The ARN of the detector model version.

                - **roleArn** *(string) --*

                  The ARN of the role that grants the detector model permission to perform its tasks.

                - **creationTime** *(datetime) --*

                  The time the detector model version was created.

                - **lastUpdateTime** *(datetime) --*

                  The last time the detector model version was updated.

                - **status** *(string) --*

                  The status of the detector model version.

                - **evaluationMethod** *(string) --*

                  When set to ``SERIAL`` , variables are updated and event conditions evaluated in the
                  order that the events are defined. When set to ``BATCH`` , variables are updated and
                  events performed only after all event conditions are evaluated.

            - **nextToken** *(string) --*

              A token to retrieve the next set of results, or ``null`` if there are no additional results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_detector_models(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListDetectorModelsResponseTypeDef:
        """
        Lists the detector models you have created. Only the metadata associated with each detector model
        is returned.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/ListDetectorModels>`_

        **Request Syntax**
        ::

          response = client.list_detector_models(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken:

          The token for the next set of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return at one time.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'detectorModelSummaries': [
                    {
                        'detectorModelName': 'string',
                        'detectorModelDescription': 'string',
                        'creationTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **detectorModelSummaries** *(list) --*

              Summary information about the detector models.

              - *(dict) --*

                Information about the detector model.

                - **detectorModelName** *(string) --*

                  The name of the detector model.

                - **detectorModelDescription** *(string) --*

                  A brief description of the detector model.

                - **creationTime** *(datetime) --*

                  The time the detector model was created.

            - **nextToken** *(string) --*

              A token to retrieve the next set of results, or ``null`` if there are no additional results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_inputs(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListInputsResponseTypeDef:
        """
        Lists the inputs you have created.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/ListInputs>`_

        **Request Syntax**
        ::

          response = client.list_inputs(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken:

          The token for the next set of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return at one time.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'inputSummaries': [
                    {
                        'inputName': 'string',
                        'inputDescription': 'string',
                        'inputArn': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **inputSummaries** *(list) --*

              Summary information about the inputs.

              - *(dict) --*

                Information about the input.

                - **inputName** *(string) --*

                  The name of the input.

                - **inputDescription** *(string) --*

                  A brief description of the input.

                - **inputArn** *(string) --*

                  The ARN of the input.

                - **creationTime** *(datetime) --*

                  The time the input was created.

                - **lastUpdateTime** *(datetime) --*

                  The last time the input was updated.

                - **status** *(string) --*

                  The status of the input.

            - **nextToken** *(string) --*

              A token to retrieve the next set of results, or ``null`` if there are no additional results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) you have assigned to the resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The ARN of the resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **tags** *(list) --*

              The list of tags assigned to the resource.

              - *(dict) --*

                Metadata that can be used to manage the resource.

                - **key** *(string) --*

                  The tag's key.

                - **value** *(string) --*

                  The tag's value.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_logging_options(
        self, loggingOptions: ClientPutLoggingOptionsloggingOptionsTypeDef
    ) -> None:
        """
        Sets or updates the AWS IoT Events logging options.

        If you update the value of any ``"loggingOptions"`` field, it takes up to one minute for the change
        to take effect. Also, if you change the policy attached to the role you specified in the
        ``"roleArn"`` field (for example, to correct an invalid policy) it takes up to five minutes for
        that change to take effect.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/PutLoggingOptions>`_

        **Request Syntax**
        ::

          response = client.put_logging_options(
              loggingOptions={
                  'roleArn': 'string',
                  'level': 'ERROR'|'INFO'|'DEBUG',
                  'enabled': True|False,
                  'detectorDebugOptions': [
                      {
                          'detectorModelName': 'string',
                          'keyValue': 'string'
                      },
                  ]
              }
          )
        :type loggingOptions: dict
        :param loggingOptions: **[REQUIRED]**

          The new values of the AWS IoT Events logging options.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the role that grants permission to AWS IoT Events to perform logging.

          - **level** *(string) --* **[REQUIRED]**

            The logging level.

          - **enabled** *(boolean) --* **[REQUIRED]**

            If TRUE, logging is enabled for AWS IoT Events.

          - **detectorDebugOptions** *(list) --*

            Information that identifies those detector models and their detectors (instances) for which the
            logging level is given.

            - *(dict) --*

              The detector model and the specific detectors (instances) for which the logging level is
              given.

              - **detectorModelName** *(string) --* **[REQUIRED]**

                The name of the detector model.

              - **keyValue** *(string) --*

                The value of the input attribute key used to create the detector (the instance of the
                detector model).

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourcetagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a
        resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceArn='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The ARN of the resource.

        :type tags: list
        :param tags: **[REQUIRED]**

          The new or modified tags for the resource.

          - *(dict) --*

            Metadata that can be used to manage the resource.

            - **key** *(string) --* **[REQUIRED]**

              The tag's key.

            - **value** *(string) --* **[REQUIRED]**

              The tag's value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the given tags (metadata) from the resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The ARN of the resource.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          A list of the keys of the tags to be removed from the resource.

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
    def update_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: ClientUpdateDetectorModeldetectorModelDefinitionTypeDef,
        roleArn: str,
        detectorModelDescription: str = None,
        evaluationMethod: str = None,
    ) -> ClientUpdateDetectorModelResponseTypeDef:
        """
        Updates a detector model. Detectors (instances) spawned by the previous version are deleted and
        then re-created as new inputs arrive.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/UpdateDetectorModel>`_

        **Request Syntax**
        ::

          response = client.update_detector_model(
              detectorModelName='string',
              detectorModelDefinition={
                  'states': [
                      {
                          'stateName': 'string',
                          'onInput': {
                              'events': [
                                  {
                                      'eventName': 'string',
                                      'condition': 'string',
                                      'actions': [
                                          {
                                              'setVariable': {
                                                  'variableName': 'string',
                                                  'value': 'string'
                                              },
                                              'sns': {
                                                  'targetArn': 'string'
                                              },
                                              'iotTopicPublish': {
                                                  'mqttTopic': 'string'
                                              },
                                              'setTimer': {
                                                  'timerName': 'string',
                                                  'seconds': 123
                                              },
                                              'clearTimer': {
                                                  'timerName': 'string'
                                              },
                                              'resetTimer': {
                                                  'timerName': 'string'
                                              },
                                              'lambda': {
                                                  'functionArn': 'string'
                                              },
                                              'iotEvents': {
                                                  'inputName': 'string'
                                              },
                                              'sqs': {
                                                  'queueUrl': 'string',
                                                  'useBase64': True|False
                                              },
                                              'firehose': {
                                                  'deliveryStreamName': 'string',
                                                  'separator': 'string'
                                              }
                                          },
                                      ]
                                  },
                              ],
                              'transitionEvents': [
                                  {
                                      'eventName': 'string',
                                      'condition': 'string',
                                      'actions': [
                                          {
                                              'setVariable': {
                                                  'variableName': 'string',
                                                  'value': 'string'
                                              },
                                              'sns': {
                                                  'targetArn': 'string'
                                              },
                                              'iotTopicPublish': {
                                                  'mqttTopic': 'string'
                                              },
                                              'setTimer': {
                                                  'timerName': 'string',
                                                  'seconds': 123
                                              },
                                              'clearTimer': {
                                                  'timerName': 'string'
                                              },
                                              'resetTimer': {
                                                  'timerName': 'string'
                                              },
                                              'lambda': {
                                                  'functionArn': 'string'
                                              },
                                              'iotEvents': {
                                                  'inputName': 'string'
                                              },
                                              'sqs': {
                                                  'queueUrl': 'string',
                                                  'useBase64': True|False
                                              },
                                              'firehose': {
                                                  'deliveryStreamName': 'string',
                                                  'separator': 'string'
                                              }
                                          },
                                      ],
                                      'nextState': 'string'
                                  },
                              ]
                          },
                          'onEnter': {
                              'events': [
                                  {
                                      'eventName': 'string',
                                      'condition': 'string',
                                      'actions': [
                                          {
                                              'setVariable': {
                                                  'variableName': 'string',
                                                  'value': 'string'
                                              },
                                              'sns': {
                                                  'targetArn': 'string'
                                              },
                                              'iotTopicPublish': {
                                                  'mqttTopic': 'string'
                                              },
                                              'setTimer': {
                                                  'timerName': 'string',
                                                  'seconds': 123
                                              },
                                              'clearTimer': {
                                                  'timerName': 'string'
                                              },
                                              'resetTimer': {
                                                  'timerName': 'string'
                                              },
                                              'lambda': {
                                                  'functionArn': 'string'
                                              },
                                              'iotEvents': {
                                                  'inputName': 'string'
                                              },
                                              'sqs': {
                                                  'queueUrl': 'string',
                                                  'useBase64': True|False
                                              },
                                              'firehose': {
                                                  'deliveryStreamName': 'string',
                                                  'separator': 'string'
                                              }
                                          },
                                      ]
                                  },
                              ]
                          },
                          'onExit': {
                              'events': [
                                  {
                                      'eventName': 'string',
                                      'condition': 'string',
                                      'actions': [
                                          {
                                              'setVariable': {
                                                  'variableName': 'string',
                                                  'value': 'string'
                                              },
                                              'sns': {
                                                  'targetArn': 'string'
                                              },
                                              'iotTopicPublish': {
                                                  'mqttTopic': 'string'
                                              },
                                              'setTimer': {
                                                  'timerName': 'string',
                                                  'seconds': 123
                                              },
                                              'clearTimer': {
                                                  'timerName': 'string'
                                              },
                                              'resetTimer': {
                                                  'timerName': 'string'
                                              },
                                              'lambda': {
                                                  'functionArn': 'string'
                                              },
                                              'iotEvents': {
                                                  'inputName': 'string'
                                              },
                                              'sqs': {
                                                  'queueUrl': 'string',
                                                  'useBase64': True|False
                                              },
                                              'firehose': {
                                                  'deliveryStreamName': 'string',
                                                  'separator': 'string'
                                              }
                                          },
                                      ]
                                  },
                              ]
                          }
                      },
                  ],
                  'initialStateName': 'string'
              },
              detectorModelDescription='string',
              roleArn='string',
              evaluationMethod='BATCH'|'SERIAL'
          )
        :type detectorModelName: string
        :param detectorModelName: **[REQUIRED]**

          The name of the detector model that is updated.

        :type detectorModelDefinition: dict
        :param detectorModelDefinition: **[REQUIRED]**

          Information that defines how a detector operates.

          - **states** *(list) --* **[REQUIRED]**

            Information about the states of the detector.

            - *(dict) --*

              Information that defines a state of a detector.

              - **stateName** *(string) --* **[REQUIRED]**

                The name of the state.

              - **onInput** *(dict) --*

                When an input is received and the ``"condition"`` is TRUE, perform the specified
                ``"actions"`` .

                - **events** *(list) --*

                  Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

                  - *(dict) --*

                    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

                    - **eventName** *(string) --* **[REQUIRED]**

                      The name of the event.

                    - **condition** *(string) --*

                      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                      performed. If not present, the actions are performed (=TRUE); if the expression
                      result is not a Boolean value, the actions are NOT performed (=FALSE).

                    - **actions** *(list) --*

                      The actions to be performed.

                      - *(dict) --*

                        An action to be performed when the ``"condition"`` is TRUE.

                        - **setVariable** *(dict) --*

                          Sets a variable to a specified value.

                          - **variableName** *(string) --* **[REQUIRED]**

                            The name of the variable.

                          - **value** *(string) --* **[REQUIRED]**

                            The new value of the variable.

                        - **sns** *(dict) --*

                          Sends an Amazon SNS message.

                          - **targetArn** *(string) --* **[REQUIRED]**

                            The ARN of the Amazon SNS target where the message is sent.

                        - **iotTopicPublish** *(dict) --*

                          Publishes an MQTT message with the given topic to the AWS IoT message broker.

                          - **mqttTopic** *(string) --* **[REQUIRED]**

                            The MQTT topic of the message.

                        - **setTimer** *(dict) --*

                          Information needed to set the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer.

                          - **seconds** *(integer) --* **[REQUIRED]**

                            The number of seconds until the timer expires. The minimum value is 60 seconds
                            to ensure accuracy.

                        - **clearTimer** *(dict) --*

                          Information needed to clear the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to clear.

                        - **resetTimer** *(dict) --*

                          Information needed to reset the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to reset.

                        - **lambda** *(dict) --*

                          Calls an AWS Lambda function, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **functionArn** *(string) --* **[REQUIRED]**

                            The ARN of the AWS Lambda function which is executed.

                        - **iotEvents** *(dict) --*

                          Sends an IoT Events input, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **inputName** *(string) --* **[REQUIRED]**

                            The name of the AWS IoT Events input where the data is sent.

                        - **sqs** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to an Amazon SQS queue.

                          - **queueUrl** *(string) --* **[REQUIRED]**

                            The URL of the Amazon SQS queue where the data is written.

                          - **useBase64** *(boolean) --*

                            Set this to TRUE if you want the data to be Base-64 encoded before it is
                            written to the queue. Otherwise, set this to FALSE.

                        - **firehose** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to a Kinesis Data Firehose delivery stream.

                          - **deliveryStreamName** *(string) --* **[REQUIRED]**

                            The name of the Kinesis Data Firehose delivery stream where the data is written.

                          - **separator** *(string) --*

                            A character separator that is used to separate records written to the Kinesis
                            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                            '\\r\\n' (Windows newline), ',' (comma).

                - **transitionEvents** *(list) --*

                  Specifies the actions performed, and the next state entered, when a ``"condition"``
                  evaluates to TRUE.

                  - *(dict) --*

                    Specifies the actions performed and the next state entered when a ``"condition"``
                    evaluates to TRUE.

                    - **eventName** *(string) --* **[REQUIRED]**

                      The name of the transition event.

                    - **condition** *(string) --* **[REQUIRED]**

                      [Required] A Boolean expression that when TRUE causes the actions to be performed and
                      the ``"nextState"`` to be entered.

                    - **actions** *(list) --*

                      The actions to be performed.

                      - *(dict) --*

                        An action to be performed when the ``"condition"`` is TRUE.

                        - **setVariable** *(dict) --*

                          Sets a variable to a specified value.

                          - **variableName** *(string) --* **[REQUIRED]**

                            The name of the variable.

                          - **value** *(string) --* **[REQUIRED]**

                            The new value of the variable.

                        - **sns** *(dict) --*

                          Sends an Amazon SNS message.

                          - **targetArn** *(string) --* **[REQUIRED]**

                            The ARN of the Amazon SNS target where the message is sent.

                        - **iotTopicPublish** *(dict) --*

                          Publishes an MQTT message with the given topic to the AWS IoT message broker.

                          - **mqttTopic** *(string) --* **[REQUIRED]**

                            The MQTT topic of the message.

                        - **setTimer** *(dict) --*

                          Information needed to set the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer.

                          - **seconds** *(integer) --* **[REQUIRED]**

                            The number of seconds until the timer expires. The minimum value is 60 seconds
                            to ensure accuracy.

                        - **clearTimer** *(dict) --*

                          Information needed to clear the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to clear.

                        - **resetTimer** *(dict) --*

                          Information needed to reset the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to reset.

                        - **lambda** *(dict) --*

                          Calls an AWS Lambda function, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **functionArn** *(string) --* **[REQUIRED]**

                            The ARN of the AWS Lambda function which is executed.

                        - **iotEvents** *(dict) --*

                          Sends an IoT Events input, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **inputName** *(string) --* **[REQUIRED]**

                            The name of the AWS IoT Events input where the data is sent.

                        - **sqs** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to an Amazon SQS queue.

                          - **queueUrl** *(string) --* **[REQUIRED]**

                            The URL of the Amazon SQS queue where the data is written.

                          - **useBase64** *(boolean) --*

                            Set this to TRUE if you want the data to be Base-64 encoded before it is
                            written to the queue. Otherwise, set this to FALSE.

                        - **firehose** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to a Kinesis Data Firehose delivery stream.

                          - **deliveryStreamName** *(string) --* **[REQUIRED]**

                            The name of the Kinesis Data Firehose delivery stream where the data is written.

                          - **separator** *(string) --*

                            A character separator that is used to separate records written to the Kinesis
                            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                            '\\r\\n' (Windows newline), ',' (comma).

                    - **nextState** *(string) --* **[REQUIRED]**

                      The next state to enter.

              - **onEnter** *(dict) --*

                When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

                - **events** *(list) --*

                  Specifies the actions that are performed when the state is entered and the
                  ``"condition"`` is TRUE.

                  - *(dict) --*

                    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

                    - **eventName** *(string) --* **[REQUIRED]**

                      The name of the event.

                    - **condition** *(string) --*

                      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                      performed. If not present, the actions are performed (=TRUE); if the expression
                      result is not a Boolean value, the actions are NOT performed (=FALSE).

                    - **actions** *(list) --*

                      The actions to be performed.

                      - *(dict) --*

                        An action to be performed when the ``"condition"`` is TRUE.

                        - **setVariable** *(dict) --*

                          Sets a variable to a specified value.

                          - **variableName** *(string) --* **[REQUIRED]**

                            The name of the variable.

                          - **value** *(string) --* **[REQUIRED]**

                            The new value of the variable.

                        - **sns** *(dict) --*

                          Sends an Amazon SNS message.

                          - **targetArn** *(string) --* **[REQUIRED]**

                            The ARN of the Amazon SNS target where the message is sent.

                        - **iotTopicPublish** *(dict) --*

                          Publishes an MQTT message with the given topic to the AWS IoT message broker.

                          - **mqttTopic** *(string) --* **[REQUIRED]**

                            The MQTT topic of the message.

                        - **setTimer** *(dict) --*

                          Information needed to set the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer.

                          - **seconds** *(integer) --* **[REQUIRED]**

                            The number of seconds until the timer expires. The minimum value is 60 seconds
                            to ensure accuracy.

                        - **clearTimer** *(dict) --*

                          Information needed to clear the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to clear.

                        - **resetTimer** *(dict) --*

                          Information needed to reset the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to reset.

                        - **lambda** *(dict) --*

                          Calls an AWS Lambda function, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **functionArn** *(string) --* **[REQUIRED]**

                            The ARN of the AWS Lambda function which is executed.

                        - **iotEvents** *(dict) --*

                          Sends an IoT Events input, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **inputName** *(string) --* **[REQUIRED]**

                            The name of the AWS IoT Events input where the data is sent.

                        - **sqs** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to an Amazon SQS queue.

                          - **queueUrl** *(string) --* **[REQUIRED]**

                            The URL of the Amazon SQS queue where the data is written.

                          - **useBase64** *(boolean) --*

                            Set this to TRUE if you want the data to be Base-64 encoded before it is
                            written to the queue. Otherwise, set this to FALSE.

                        - **firehose** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to a Kinesis Data Firehose delivery stream.

                          - **deliveryStreamName** *(string) --* **[REQUIRED]**

                            The name of the Kinesis Data Firehose delivery stream where the data is written.

                          - **separator** *(string) --*

                            A character separator that is used to separate records written to the Kinesis
                            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                            '\\r\\n' (Windows newline), ',' (comma).

              - **onExit** *(dict) --*

                When exiting this state, perform these ``"actions"`` if the specified ``"condition"`` is
                TRUE.

                - **events** *(list) --*

                  Specifies the ``"actions"`` that are performed when the state is exited and the
                  ``"condition"`` is TRUE.

                  - *(dict) --*

                    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

                    - **eventName** *(string) --* **[REQUIRED]**

                      The name of the event.

                    - **condition** *(string) --*

                      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                      performed. If not present, the actions are performed (=TRUE); if the expression
                      result is not a Boolean value, the actions are NOT performed (=FALSE).

                    - **actions** *(list) --*

                      The actions to be performed.

                      - *(dict) --*

                        An action to be performed when the ``"condition"`` is TRUE.

                        - **setVariable** *(dict) --*

                          Sets a variable to a specified value.

                          - **variableName** *(string) --* **[REQUIRED]**

                            The name of the variable.

                          - **value** *(string) --* **[REQUIRED]**

                            The new value of the variable.

                        - **sns** *(dict) --*

                          Sends an Amazon SNS message.

                          - **targetArn** *(string) --* **[REQUIRED]**

                            The ARN of the Amazon SNS target where the message is sent.

                        - **iotTopicPublish** *(dict) --*

                          Publishes an MQTT message with the given topic to the AWS IoT message broker.

                          - **mqttTopic** *(string) --* **[REQUIRED]**

                            The MQTT topic of the message.

                        - **setTimer** *(dict) --*

                          Information needed to set the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer.

                          - **seconds** *(integer) --* **[REQUIRED]**

                            The number of seconds until the timer expires. The minimum value is 60 seconds
                            to ensure accuracy.

                        - **clearTimer** *(dict) --*

                          Information needed to clear the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to clear.

                        - **resetTimer** *(dict) --*

                          Information needed to reset the timer.

                          - **timerName** *(string) --* **[REQUIRED]**

                            The name of the timer to reset.

                        - **lambda** *(dict) --*

                          Calls an AWS Lambda function, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **functionArn** *(string) --* **[REQUIRED]**

                            The ARN of the AWS Lambda function which is executed.

                        - **iotEvents** *(dict) --*

                          Sends an IoT Events input, passing in information about the detector model
                          instance and the event which triggered the action.

                          - **inputName** *(string) --* **[REQUIRED]**

                            The name of the AWS IoT Events input where the data is sent.

                        - **sqs** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to an Amazon SQS queue.

                          - **queueUrl** *(string) --* **[REQUIRED]**

                            The URL of the Amazon SQS queue where the data is written.

                          - **useBase64** *(boolean) --*

                            Set this to TRUE if you want the data to be Base-64 encoded before it is
                            written to the queue. Otherwise, set this to FALSE.

                        - **firehose** *(dict) --*

                          Sends information about the detector model instance and the event which triggered
                          the action to a Kinesis Data Firehose delivery stream.

                          - **deliveryStreamName** *(string) --* **[REQUIRED]**

                            The name of the Kinesis Data Firehose delivery stream where the data is written.

                          - **separator** *(string) --*

                            A character separator that is used to separate records written to the Kinesis
                            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                            '\\r\\n' (Windows newline), ',' (comma).

          - **initialStateName** *(string) --* **[REQUIRED]**

            The state that is entered at the creation of each detector (instance).

        :type detectorModelDescription: string
        :param detectorModelDescription:

          A brief description of the detector model.

        :type roleArn: string
        :param roleArn: **[REQUIRED]**

          The ARN of the role that grants permission to AWS IoT Events to perform its operations.

        :type evaluationMethod: string
        :param evaluationMethod:

          When set to ``SERIAL`` , variables are updated and event conditions evaluated in the order that
          the events are defined. When set to ``BATCH`` , variables are updated and events performed only
          after all event conditions are evaluated.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'detectorModelConfiguration': {
                    'detectorModelName': 'string',
                    'detectorModelVersion': 'string',
                    'detectorModelDescription': 'string',
                    'detectorModelArn': 'string',
                    'roleArn': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdateTime': datetime(2015, 1, 1),
                    'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
                    'key': 'string',
                    'evaluationMethod': 'BATCH'|'SERIAL'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **detectorModelConfiguration** *(dict) --*

              Information about how the detector model is configured.

              - **detectorModelName** *(string) --*

                The name of the detector model.

              - **detectorModelVersion** *(string) --*

                The version of the detector model.

              - **detectorModelDescription** *(string) --*

                A brief description of the detector model.

              - **detectorModelArn** *(string) --*

                The ARN of the detector model.

              - **roleArn** *(string) --*

                The ARN of the role that grants permission to AWS IoT Events to perform its operations.

              - **creationTime** *(datetime) --*

                The time the detector model was created.

              - **lastUpdateTime** *(datetime) --*

                The time the detector model was last updated.

              - **status** *(string) --*

                The status of the detector model.

              - **key** *(string) --*

                The input attribute key used to identify a device or system to create a detector (an
                instance of the detector model) and then to route each input received to the appropriate
                detector (instance). This parameter uses a JSON-path expression to specify the
                attribute-value pair in the message payload of each input that is used to identify the
                device associated with the input.

              - **evaluationMethod** *(string) --*

                When set to ``SERIAL`` , variables are updated and event conditions evaluated in the order
                that the events are defined. When set to ``BATCH`` , variables are updated and events
                performed only after all event conditions are evaluated.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_input(
        self,
        inputName: str,
        inputDefinition: ClientUpdateInputinputDefinitionTypeDef,
        inputDescription: str = None,
    ) -> ClientUpdateInputResponseTypeDef:
        """
        Updates an input.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/UpdateInput>`_

        **Request Syntax**
        ::

          response = client.update_input(
              inputName='string',
              inputDescription='string',
              inputDefinition={
                  'attributes': [
                      {
                          'jsonPath': 'string'
                      },
                  ]
              }
          )
        :type inputName: string
        :param inputName: **[REQUIRED]**

          The name of the input you want to update.

        :type inputDescription: string
        :param inputDescription:

          A brief description of the input.

        :type inputDefinition: dict
        :param inputDefinition: **[REQUIRED]**

          The definition of the input.

          - **attributes** *(list) --* **[REQUIRED]**

            The attributes from the JSON payload that are made available by the input. Inputs are derived
            from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
            contains a JSON payload, and those attributes (and their paired values) specified here are
            available for use in the ``"condition"`` expressions used by detectors that monitor this input.

            - *(dict) --*

              The attributes from the JSON payload that are made available by the input. Inputs are derived
              from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
              contains a JSON payload, and those attributes (and their paired values) specified here are
              available for use in the ``condition`` expressions used by detectors.

              - **jsonPath** *(string) --* **[REQUIRED]**

                An expression that specifies an attribute-value pair in a JSON structure. Use this to
                specify an attribute from the JSON payload that is made available by the input. Inputs are
                derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
                message contains a JSON payload, and the attribute (and its paired value) specified here
                are available for use in the ``"condition"`` expressions used by detectors.

                Syntax: ``<field-name>.<field-name>...``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'inputConfiguration': {
                    'inputName': 'string',
                    'inputDescription': 'string',
                    'inputArn': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdateTime': datetime(2015, 1, 1),
                    'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **inputConfiguration** *(dict) --*

              Information about the configuration of the input.

              - **inputName** *(string) --*

                The name of the input.

              - **inputDescription** *(string) --*

                A brief description of the input.

              - **inputArn** *(string) --*

                The ARN of the input.

              - **creationTime** *(datetime) --*

                The time the input was created.

              - **lastUpdateTime** *(datetime) --*

                The last time the input was updated.

              - **status** *(string) --*

                The status of the input.

        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError
