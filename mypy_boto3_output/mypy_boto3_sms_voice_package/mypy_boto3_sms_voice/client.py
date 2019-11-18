"Main interface for sms-voice Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sms_voice.client as client_scope
from mypy_boto3_sms_voice.type_defs import (
    ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
    ClientGetConfigurationSetEventDestinationsResponseTypeDef,
    ClientListConfigurationSetsResponseTypeDef,
    ClientSendVoiceMessageResponseTypeDef,
    ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
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
    def create_configuration_set(
        self, ConfigurationSetName: str = None
    ) -> Dict[str, Any]:
        """
        Create a new configuration set. After you create the configuration set, you can add one or more
        event destinations to it.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet>`_

        **Request Syntax**
        ::

          response = client.create_configuration_set(
              ConfigurationSetName='string'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: The name that you want to give the configuration set.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* CreateConfigurationSetResponse
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = None,
        EventDestinationName: str = None,
    ) -> Dict[str, Any]:
        """
        Create a new event destination in a configuration set.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination>`_
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination>`_

        **Request Syntax**
        ::

          response = client.create_configuration_set_event_destination(
              ConfigurationSetName='string',
              EventDestination={
                  'CloudWatchLogsDestination': {
                      'IamRoleArn': 'string',
                      'LogGroupArn': 'string'
                  },
                  'Enabled': True|False,
                  'KinesisFirehoseDestination': {
                      'DeliveryStreamArn': 'string',
                      'IamRoleArn': 'string'
                  },
                  'MatchingEventTypes': [
                      'INITIATED_CALL'|'RINGING'|'ANSWERED'|'COMPLETED_CALL'|'BUSY'|'FAILED'|'NO_ANSWER',
                  ],
                  'SnsDestination': {
                      'TopicArn': 'string'
                  }
              },
              EventDestinationName='string'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** ConfigurationSetName

        :type EventDestination: dict
        :param EventDestination: An object that defines a single event destination.

          - **CloudWatchLogsDestination** *(dict) --* An object that contains information about an event
          destination that sends data to Amazon CloudWatch Logs.

            - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of an Amazon Identity and Access
            Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.

            - **LogGroupArn** *(string) --* The name of the Amazon CloudWatch Log Group that you want to
            record events in.

          - **Enabled** *(boolean) --* Indicates whether or not the event destination is enabled. If the
          event destination is enabled, then Amazon Pinpoint sends response data to the specified event
          destination.

          - **KinesisFirehoseDestination** *(dict) --* An object that contains information about an event
          destination that sends data to Amazon Kinesis Data Firehose.

            - **DeliveryStreamArn** *(string) --* The Amazon Resource Name (ARN) of an IAM role that can
            write data to an Amazon Kinesis Data Firehose stream.

            - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon Kinesis Data
            Firehose destination that you want to use in the event destination.

          - **MatchingEventTypes** *(list) --* An array of EventDestination objects. Each EventDestination
          object includes ARNs and other information that define an event destination.

            - *(string) --* The types of events that are sent to the event destination.

          - **SnsDestination** *(dict) --* An object that contains information about an event destination
          that sends data to Amazon SNS.

            - **TopicArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon SNS topic that you
            want to publish events to.

        :type EventDestinationName: string
        :param EventDestinationName: A name that identifies the event destination.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* CreateConfigurationSetEventDestinationResponse
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        Deletes an existing configuration set.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet>`_

        **Request Syntax**
        ::

          response = client.delete_configuration_set(
              ConfigurationSetName='string'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** ConfigurationSetName

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* DeleteConfigurationSetResponse
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        Deletes an event destination in a configuration set.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination>`_
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination>`_

        **Request Syntax**
        ::

          response = client.delete_configuration_set_event_destination(
              ConfigurationSetName='string',
              EventDestinationName='string'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** ConfigurationSetName

        :type EventDestinationName: string
        :param EventDestinationName: **[REQUIRED]** EventDestinationName

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* DeleteConfigurationSetEventDestinationResponse
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
    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> ClientGetConfigurationSetEventDestinationsResponseTypeDef:
        """
        Obtain information about an event destination, including the types of events it reports, the Amazon
        Resource Name (ARN) of the destination, and the name of the event destination.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations>`_
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations>`_

        **Request Syntax**
        ::

          response = client.get_configuration_set_event_destinations(
              ConfigurationSetName='string'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** ConfigurationSetName

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventDestinations': [
                    {
                        'CloudWatchLogsDestination': {
                            'IamRoleArn': 'string',
                            'LogGroupArn': 'string'
                        },
                        'Enabled': True|False,
                        'KinesisFirehoseDestination': {
                            'DeliveryStreamArn': 'string',
                            'IamRoleArn': 'string'
                        },
                        'MatchingEventTypes': [
                            'INITIATED_CALL'|'RINGING'|'ANSWERED'|'COMPLETED_CALL'|'BUSY'|'FAILED'
                            |'NO_ANSWER',
                        ],
                        'Name': 'string',
                        'SnsDestination': {
                            'TopicArn': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* GetConfigurationSetEventDestinationsResponse

            - **EventDestinations** *(list) --* An array of EventDestination objects. Each EventDestination
            object includes ARNs and other information that define an event destination.

              - *(dict) --* An object that defines an event destination.

                - **CloudWatchLogsDestination** *(dict) --* An object that contains information about an
                event destination that sends data to Amazon CloudWatch Logs.

                  - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of an Amazon Identity and
                  Access Management (IAM) role that is able to write event data to an Amazon CloudWatch
                  destination.

                  - **LogGroupArn** *(string) --* The name of the Amazon CloudWatch Log Group that you want
                  to record events in.

                - **Enabled** *(boolean) --* Indicates whether or not the event destination is enabled. If
                the event destination is enabled, then Amazon Pinpoint sends response data to the specified
                event destination.

                - **KinesisFirehoseDestination** *(dict) --* An object that contains information about an
                event destination that sends data to Amazon Kinesis Data Firehose.

                  - **DeliveryStreamArn** *(string) --* The Amazon Resource Name (ARN) of an IAM role that
                  can write data to an Amazon Kinesis Data Firehose stream.

                  - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon Kinesis Data
                  Firehose destination that you want to use in the event destination.

                - **MatchingEventTypes** *(list) --* An array of EventDestination objects. Each
                EventDestination object includes ARNs and other information that define an event
                destination.

                  - *(string) --* The types of events that are sent to the event destination.

                - **Name** *(string) --* A name that identifies the event destination configuration.

                - **SnsDestination** *(dict) --* An object that contains information about an event
                destination that sends data to Amazon SNS.

                  - **TopicArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon SNS topic that
                  you want to publish events to.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configuration_sets(
        self, NextToken: str = None, PageSize: str = None
    ) -> ClientListConfigurationSetsResponseTypeDef:
        """
        List all of the configuration sets associated with your Amazon Pinpoint account in the current
        region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/ListConfigurationSets>`_

        **Request Syntax**
        ::

          response = client.list_configuration_sets(
              NextToken='string',
              PageSize='string'
          )
        :type NextToken: string
        :param NextToken: A token returned from a previous call to the API that indicates the position in
        the list of results.

        :type PageSize: string
        :param PageSize: Used to specify the number of items that should be returned in the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ConfigurationSets': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --* ListConfigurationSetsResponse

            - **ConfigurationSets** *(list) --* An object that contains a list of configuration sets for
            your account in the current region.

              - *(string) --*

            - **NextToken** *(string) --* A token returned from a previous call to ListConfigurationSets to
            indicate the position in the list of configuration sets.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_voice_message(
        self,
        CallerId: str = None,
        ConfigurationSetName: str = None,
        Content: Dict[str, Any] = None,
        DestinationPhoneNumber: str = None,
        OriginationPhoneNumber: str = None,
    ) -> ClientSendVoiceMessageResponseTypeDef:
        """
        Create a new voice message and send it to a recipient's phone number.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/SendVoiceMessage>`_

        **Request Syntax**
        ::

          response = client.send_voice_message(
              CallerId='string',
              ConfigurationSetName='string',
              Content={
                  'CallInstructionsMessage': {
                      'Text': 'string'
                  },
                  'PlainTextMessage': {
                      'LanguageCode': 'string',
                      'Text': 'string',
                      'VoiceId': 'string'
                  },
                  'SSMLMessage': {
                      'LanguageCode': 'string',
                      'Text': 'string',
                      'VoiceId': 'string'
                  }
              },
              DestinationPhoneNumber='string',
              OriginationPhoneNumber='string'
          )
        :type CallerId: string
        :param CallerId: The phone number that appears on recipients' devices when they receive the message.

        :type ConfigurationSetName: string
        :param ConfigurationSetName: The name of the configuration set that you want to use to send the
        message.

        :type Content: dict
        :param Content: An object that contains a voice message and information about the recipient that
        you want to send it to.

          - **CallInstructionsMessage** *(dict) --* An object that defines a message that contains text
          formatted using Amazon Pinpoint Voice Instructions markup.

            - **Text** *(string) --* The language to use when delivering the message. For a complete list
            of supported languages, see the Amazon Polly Developer Guide.

          - **PlainTextMessage** *(dict) --* An object that defines a message that contains unformatted
          text.

            - **LanguageCode** *(string) --* The language to use when delivering the message. For a
            complete list of supported languages, see the Amazon Polly Developer Guide.

            - **Text** *(string) --* The plain (not SSML-formatted) text to deliver to the recipient.

            - **VoiceId** *(string) --* The name of the voice that you want to use to deliver the message.
            For a complete list of supported voices, see the Amazon Polly Developer Guide.

          - **SSMLMessage** *(dict) --* An object that defines a message that contains SSML-formatted text.

            - **LanguageCode** *(string) --* The language to use when delivering the message. For a
            complete list of supported languages, see the Amazon Polly Developer Guide.

            - **Text** *(string) --* The SSML-formatted text to deliver to the recipient.

            - **VoiceId** *(string) --* The name of the voice that you want to use to deliver the message.
            For a complete list of supported voices, see the Amazon Polly Developer Guide.

        :type DestinationPhoneNumber: string
        :param DestinationPhoneNumber: The phone number that you want to send the voice message to.

        :type OriginationPhoneNumber: string
        :param OriginationPhoneNumber: The phone number that Amazon Pinpoint should use to send the voice
        message. This isn't necessarily the phone number that appears on recipients' devices when they
        receive the message, because you can specify a CallerId parameter in the request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MessageId': 'string'
            }
          **Response Structure**

          - *(dict) --* SendVoiceMessageResponse

            - **MessageId** *(string) --* A unique identifier for the voice message.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        Update an event destination in a configuration set. An event destination is a location that you
        publish information about your voice calls to. For example, you can log an event to an Amazon
        CloudWatch destination when a call fails.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination>`_
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination>`_

        **Request Syntax**
        ::

          response = client.update_configuration_set_event_destination(
              ConfigurationSetName='string',
              EventDestination={
                  'CloudWatchLogsDestination': {
                      'IamRoleArn': 'string',
                      'LogGroupArn': 'string'
                  },
                  'Enabled': True|False,
                  'KinesisFirehoseDestination': {
                      'DeliveryStreamArn': 'string',
                      'IamRoleArn': 'string'
                  },
                  'MatchingEventTypes': [
                      'INITIATED_CALL'|'RINGING'|'ANSWERED'|'COMPLETED_CALL'|'BUSY'|'FAILED'|'NO_ANSWER',
                  ],
                  'SnsDestination': {
                      'TopicArn': 'string'
                  }
              },
              EventDestinationName='string'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** ConfigurationSetName

        :type EventDestination: dict
        :param EventDestination: An object that defines a single event destination.

          - **CloudWatchLogsDestination** *(dict) --* An object that contains information about an event
          destination that sends data to Amazon CloudWatch Logs.

            - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of an Amazon Identity and Access
            Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.

            - **LogGroupArn** *(string) --* The name of the Amazon CloudWatch Log Group that you want to
            record events in.

          - **Enabled** *(boolean) --* Indicates whether or not the event destination is enabled. If the
          event destination is enabled, then Amazon Pinpoint sends response data to the specified event
          destination.

          - **KinesisFirehoseDestination** *(dict) --* An object that contains information about an event
          destination that sends data to Amazon Kinesis Data Firehose.

            - **DeliveryStreamArn** *(string) --* The Amazon Resource Name (ARN) of an IAM role that can
            write data to an Amazon Kinesis Data Firehose stream.

            - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon Kinesis Data
            Firehose destination that you want to use in the event destination.

          - **MatchingEventTypes** *(list) --* An array of EventDestination objects. Each EventDestination
          object includes ARNs and other information that define an event destination.

            - *(string) --* The types of events that are sent to the event destination.

          - **SnsDestination** *(dict) --* An object that contains information about an event destination
          that sends data to Amazon SNS.

            - **TopicArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon SNS topic that you
            want to publish events to.

        :type EventDestinationName: string
        :param EventDestinationName: **[REQUIRED]** EventDestinationName

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* UpdateConfigurationSetEventDestinationResponse
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
