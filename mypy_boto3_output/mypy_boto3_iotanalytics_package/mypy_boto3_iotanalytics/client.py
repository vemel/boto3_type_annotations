"Main interface for iotanalytics Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_iotanalytics.client as client_scope

# pylint: disable=import-self
import mypy_boto3_iotanalytics.paginator as paginator_scope
from mypy_boto3_iotanalytics.type_defs import (
    ClientBatchPutMessageResponseTypeDef,
    ClientBatchPutMessagemessagesTypeDef,
    ClientCreateChannelResponseTypeDef,
    ClientCreateChannelchannelStorageTypeDef,
    ClientCreateChannelretentionPeriodTypeDef,
    ClientCreateChanneltagsTypeDef,
    ClientCreateDatasetContentResponseTypeDef,
    ClientCreateDatasetResponseTypeDef,
    ClientCreateDatasetactionsTypeDef,
    ClientCreateDatasetcontentDeliveryRulesTypeDef,
    ClientCreateDatasettagsTypeDef,
    ClientCreateDatasettriggersTypeDef,
    ClientCreateDatastoreResponseTypeDef,
    ClientCreateDatastoredatastoreStorageTypeDef,
    ClientCreateDatastoreretentionPeriodTypeDef,
    ClientCreateDatastoretagsTypeDef,
    ClientCreatePipelineResponseTypeDef,
    ClientCreatePipelinepipelineActivitiesTypeDef,
    ClientCreatePipelinetagsTypeDef,
    ClientDescribeChannelResponseTypeDef,
    ClientDescribeDatastoreResponseTypeDef,
    ClientDescribeLoggingOptionsResponseTypeDef,
    ClientDescribePipelineResponseTypeDef,
    ClientGetDatasetContentResponseTypeDef,
    ClientListChannelsResponseTypeDef,
    ClientListDatasetContentsResponseTypeDef,
    ClientListDatasetsResponseTypeDef,
    ClientListDatastoresResponseTypeDef,
    ClientListPipelinesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutLoggingOptionsloggingOptionsTypeDef,
    ClientRunPipelineActivityResponseTypeDef,
    ClientRunPipelineActivitypipelineActivityTypeDef,
    ClientSampleChannelDataResponseTypeDef,
    ClientStartPipelineReprocessingResponseTypeDef,
    ClientTagResourcetagsTypeDef,
    ClientUpdateChannelchannelStorageTypeDef,
    ClientUpdateChannelretentionPeriodTypeDef,
    ClientUpdateDatasetactionsTypeDef,
    ClientUpdateDatasetcontentDeliveryRulesTypeDef,
    ClientUpdateDatasetretentionPeriodTypeDef,
    ClientUpdateDatasettriggersTypeDef,
    ClientUpdateDatastoredatastoreStorageTypeDef,
    ClientUpdateDatastoreretentionPeriodTypeDef,
    ClientUpdatePipelinepipelineActivitiesTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_put_message(
        self, channelName: str, messages: List[ClientBatchPutMessagemessagesTypeDef]
    ) -> ClientBatchPutMessageResponseTypeDef:
        """
        Sends messages to a channel.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/BatchPutMessage>`_

        **Request Syntax**
        ::

          response = client.batch_put_message(
              channelName='string',
              messages=[
                  {
                      'messageId': 'string',
                      'payload': b'bytes'
                  },
              ]
          )
        :type channelName: string
        :param channelName: **[REQUIRED]**

          The name of the channel where the messages are sent.

        :type messages: list
        :param messages: **[REQUIRED]**

          The list of messages to be sent. Each message has format: '{ "messageId": "string", "payload":
          "string"}'.

          Note that the field names of message payloads (data) that you send to AWS IoT Analytics:

          * Must contain only alphanumeric characters and undescores (_); no other special characters are
          allowed.

          * Must begin with an alphabetic character or single underscore (_).

          * Cannot contain hyphens (-).

          * In regular expression terms: "^[A-Za-z_]([A-Za-z0-9]*|[A-Za-z0-9][A-Za-z0-9_]*)$".

          * Cannot be greater than 255 characters.

          * Are case-insensitive. (Fields named "foo" and "FOO" in the same payload are considered
          duplicates.)

          For example, {"temp_01": 29} or {"_temp_01": 29} are valid, but {"temp-01": 29}, {"01_temp": 29}
          or {"__temp_01": 29} are invalid in message payloads.

          - *(dict) --*

            Information about a message.

            - **messageId** *(string) --* **[REQUIRED]**

              The ID you wish to assign to the message. Each "messageId" must be unique within each batch
              sent.

            - **payload** *(bytes) --* **[REQUIRED]**

              The payload of the message. This may be a JSON string or a Base64-encoded string representing
              binary data (in which case you must decode it by means of a pipeline activity).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'batchPutMessageErrorEntries': [
                    {
                        'messageId': 'string',
                        'errorCode': 'string',
                        'errorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **batchPutMessageErrorEntries** *(list) --*

              A list of any errors encountered when sending the messages to the channel.

              - *(dict) --*

                Contains informations about errors.

                - **messageId** *(string) --*

                  The ID of the message that caused the error. (See the value corresponding to the
                  "messageId" key in the message object.)

                - **errorCode** *(string) --*

                  The code associated with the error.

                - **errorMessage** *(string) --*

                  The message associated with the error.

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
    def cancel_pipeline_reprocessing(
        self, pipelineName: str, reprocessingId: str
    ) -> Dict[str, Any]:
        """
        Cancels the reprocessing of data through the pipeline.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CancelPipelineReprocessing>`_

        **Request Syntax**
        ::

          response = client.cancel_pipeline_reprocessing(
              pipelineName='string',
              reprocessingId='string'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**

          The name of pipeline for which data reprocessing is canceled.

        :type reprocessingId: string
        :param reprocessingId: **[REQUIRED]**

          The ID of the reprocessing task (returned by "StartPipelineReprocessing").

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_channel(
        self,
        channelName: str,
        channelStorage: ClientCreateChannelchannelStorageTypeDef = None,
        retentionPeriod: ClientCreateChannelretentionPeriodTypeDef = None,
        tags: List[ClientCreateChanneltagsTypeDef] = None,
    ) -> ClientCreateChannelResponseTypeDef:
        """
        Creates a channel. A channel collects data from an MQTT topic and archives the raw, unprocessed
        messages before publishing the data to a pipeline.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateChannel>`_

        **Request Syntax**
        ::

          response = client.create_channel(
              channelName='string',
              channelStorage={
                  'serviceManagedS3': {}
                  ,
                  'customerManagedS3': {
                      'bucket': 'string',
                      'keyPrefix': 'string',
                      'roleArn': 'string'
                  }
              },
              retentionPeriod={
                  'unlimited': True|False,
                  'numberOfDays': 123
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type channelName: string
        :param channelName: **[REQUIRED]**

          The name of the channel.

        :type channelStorage: dict
        :param channelStorage:

          Where channel data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
          storage. If not specified, the default is "serviceManagedS3". This cannot be changed after
          creation of the channel.

          - **serviceManagedS3** *(dict) --*

            Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service. The
            choice of service-managed or customer-managed S3 storage cannot be changed after creation of
            the channel.

          - **customerManagedS3** *(dict) --*

            Use this to store channel data in an S3 bucket that you manage. If customer managed storage is
            selected, the "retentionPeriod" parameter is ignored. The choice of service-managed or
            customer-managed S3 storage cannot be changed after creation of the channel.

            - **bucket** *(string) --* **[REQUIRED]**

              The name of the Amazon S3 bucket in which channel data is stored.

            - **keyPrefix** *(string) --*

              [Optional] The prefix used to create the keys of the channel data objects. Each object in an
              Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in a
              bucket has exactly one key). The prefix must end with a '/'.

            - **roleArn** *(string) --* **[REQUIRED]**

              The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
              resources.

        :type retentionPeriod: dict
        :param retentionPeriod:

          How long, in days, message data is kept for the channel. When "customerManagedS3" storage is
          selected, this parameter is ignored.

          - **unlimited** *(boolean) --*

            If true, message data is kept indefinitely.

          - **numberOfDays** *(integer) --*

            The number of days that message data is kept. The "unlimited" parameter must be false.

        :type tags: list
        :param tags:

          Metadata which can be used to manage the channel.

          - *(dict) --*

            A set of key/value pairs which are used to manage the resource.

            - **key** *(string) --* **[REQUIRED]**

              The tag's key.

            - **value** *(string) --* **[REQUIRED]**

              The tag's value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'channelName': 'string',
                'channelArn': 'string',
                'retentionPeriod': {
                    'unlimited': True|False,
                    'numberOfDays': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            - **channelName** *(string) --*

              The name of the channel.

            - **channelArn** *(string) --*

              The ARN of the channel.

            - **retentionPeriod** *(dict) --*

              How long, in days, message data is kept for the channel.

              - **unlimited** *(boolean) --*

                If true, message data is kept indefinitely.

              - **numberOfDays** *(integer) --*

                The number of days that message data is kept. The "unlimited" parameter must be false.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataset(
        self,
        datasetName: str,
        actions: List[ClientCreateDatasetactionsTypeDef],
        triggers: List[ClientCreateDatasettriggersTypeDef] = None,
        contentDeliveryRules: List[
            ClientCreateDatasetcontentDeliveryRulesTypeDef
        ] = None,
        retentionPeriod: Dict = None,
        versioningConfiguration: Dict = None,
        tags: List[ClientCreateDatasettagsTypeDef] = None,
    ) -> ClientCreateDatasetResponseTypeDef:
        """
        Creates a data set. A data set stores data retrieved from a data store by applying a "queryAction"
        (a SQL query) or a "containerAction" (executing a containerized application). This operation
        creates the skeleton of a data set. The data set can be populated manually by calling
        "CreateDatasetContent" or automatically according to a "trigger" you specify.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateDataset>`_

        **Request Syntax**
        ::

          response = client.create_dataset(
              datasetName='string',
              actions=[
                  {
                      'actionName': 'string',
                      'queryAction': {
                          'sqlQuery': 'string',
                          'filters': [
                              {
                                  'deltaTime': {
                                      'offsetSeconds': 123,
                                      'timeExpression': 'string'
                                  }
                              },
                          ]
                      },
                      'containerAction': {
                          'image': 'string',
                          'executionRoleArn': 'string',
                          'resourceConfiguration': {
                              'computeType': 'ACU_1'|'ACU_2',
                              'volumeSizeInGB': 123
                          },
                          'variables': [
                              {
                                  'name': 'string',
                                  'stringValue': 'string',
                                  'doubleValue': 123.0,
                                  'datasetContentVersionValue': {
                                      'datasetName': 'string'
                                  },
                                  'outputFileUriValue': {
                                      'fileName': 'string'
                                  }
                              },
                          ]
                      }
                  },
              ],
              triggers=[
                  {
                      'schedule': {
                          'expression': 'string'
                      },
                      'dataset': {
                          'name': 'string'
                      }
                  },
              ],
              contentDeliveryRules=[
                  {
                      'entryName': 'string',
                      'destination': {
                          'iotEventsDestinationConfiguration': {
                              'inputName': 'string',
                              'roleArn': 'string'
                          },
                          's3DestinationConfiguration': {
                              'bucket': 'string',
                              'key': 'string',
                              'glueConfiguration': {
                                  'tableName': 'string',
                                  'databaseName': 'string'
                              },
                              'roleArn': 'string'
                          }
                      }
                  },
              ],
              retentionPeriod={
                  'unlimited': True|False,
                  'numberOfDays': 123
              },
              versioningConfiguration={
                  'unlimited': True|False,
                  'maxVersions': 123
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]**

          The name of the data set.

        :type actions: list
        :param actions: **[REQUIRED]**

          A list of actions that create the data set contents.

          - *(dict) --*

            A "DatasetAction" object that specifies how data set contents are automatically created.

            - **actionName** *(string) --*

              The name of the data set action by which data set contents are automatically created.

            - **queryAction** *(dict) --*

              An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set
              contents.

              - **sqlQuery** *(string) --* **[REQUIRED]**

                A SQL query string.

              - **filters** *(list) --*

                Pre-filters applied to message data.

                - *(dict) --*

                  Information which is used to filter message data, to segregate it according to the time
                  frame in which it arrives.

                  - **deltaTime** *(dict) --*

                    Used to limit data to that which has arrived since the last execution of the action.

                    - **offsetSeconds** *(integer) --* **[REQUIRED]**

                      The number of seconds of estimated "in flight" lag time of message data. When you
                      create data set contents using message data from a specified time frame, some message
                      data may still be "in flight" when processing begins, and so will not arrive in time
                      to be processed. Use this field to make allowances for the "in flight" time of your
                      message data, so that data not processed from a previous time frame will be included
                      with the next time frame. Without this, missed message data would be excluded from
                      processing during the next time frame as well, because its timestamp places it within
                      the previous time frame.

                    - **timeExpression** *(string) --* **[REQUIRED]**

                      An expression by which the time of the message data may be determined. This may be
                      the name of a timestamp field, or a SQL expression which is used to derive the time
                      the message data was generated.

            - **containerAction** *(dict) --*

              Information which allows the system to run a containerized application in order to create the
              data set contents. The application must be in a Docker container along with any needed
              support libraries.

              - **image** *(string) --* **[REQUIRED]**

                The ARN of the Docker container stored in your account. The Docker container contains an
                application and needed support libraries and is used to generate data set contents.

              - **executionRoleArn** *(string) --* **[REQUIRED]**

                The ARN of the role which gives permission to the system to access needed resources in
                order to run the "containerAction". This includes, at minimum, permission to retrieve the
                data set contents which are the input to the containerized application.

              - **resourceConfiguration** *(dict) --* **[REQUIRED]**

                Configuration of the resource which executes the "containerAction".

                - **computeType** *(string) --* **[REQUIRED]**

                  The type of the compute resource used to execute the "containerAction". Possible values
                  are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

                - **volumeSizeInGB** *(integer) --* **[REQUIRED]**

                  The size (in GB) of the persistent storage available to the resource instance used to
                  execute the "containerAction" (min: 1, max: 50).

              - **variables** *(list) --*

                The values of variables used within the context of the execution of the containerized
                application (basically, parameters passed to the application). Each variable must have a
                name and a value given by one of "stringValue", "datasetContentVersionValue", or
                "outputFileUriValue".

                - *(dict) --*

                  An instance of a variable to be passed to the "containerAction" execution. Each variable
                  must have a name and a value given by one of "stringValue", "datasetContentVersionValue",
                  or "outputFileUriValue".

                  - **name** *(string) --* **[REQUIRED]**

                    The name of the variable.

                  - **stringValue** *(string) --*

                    The value of the variable as a string.

                  - **doubleValue** *(float) --*

                    The value of the variable as a double (numeric).

                  - **datasetContentVersionValue** *(dict) --*

                    The value of the variable as a structure that specifies a data set content version.

                    - **datasetName** *(string) --* **[REQUIRED]**

                      The name of the data set whose latest contents are used as input to the notebook or
                      application.

                  - **outputFileUriValue** *(dict) --*

                    The value of the variable as a structure that specifies an output file URI.

                    - **fileName** *(string) --* **[REQUIRED]**

                      The URI of the location where data set contents are stored, usually the URI of a file
                      in an S3 bucket.

        :type triggers: list
        :param triggers:

          A list of triggers. A trigger causes data set contents to be populated at a specified time
          interval or when another data set's contents are created. The list of triggers can be empty or
          contain up to five **DataSetTrigger** objects.

          - *(dict) --*

            The "DatasetTrigger" that specifies when the data set is automatically updated.

            - **schedule** *(dict) --*

              The "Schedule" when the trigger is initiated.

              - **expression** *(string) --*

                The expression that defines when to trigger an update. For more information, see `Schedule
                Expressions for Rules
                <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the
                Amazon CloudWatch Events User Guide.

            - **dataset** *(dict) --*

              The data set whose content creation triggers the creation of this data set's contents.

              - **name** *(string) --* **[REQUIRED]**

                The name of the data set whose content generation triggers the new data set content
                generation.

        :type contentDeliveryRules: list
        :param contentDeliveryRules:

          When data set contents are created they are delivered to destinations specified here.

          - *(dict) --*

            When data set contents are created they are delivered to destination specified here.

            - **entryName** *(string) --*

              The name of the data set content delivery rules entry.

            - **destination** *(dict) --* **[REQUIRED]**

              The destination to which data set contents are delivered.

              - **iotEventsDestinationConfiguration** *(dict) --*

                Configuration information for delivery of data set contents to AWS IoT Events.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input to which data set contents are delivered.

                - **roleArn** *(string) --* **[REQUIRED]**

                  The ARN of the role which grants AWS IoT Analytics permission to deliver data set
                  contents to an AWS IoT Events input.

              - **s3DestinationConfiguration** *(dict) --*

                Configuration information for delivery of data set contents to Amazon S3.

                - **bucket** *(string) --* **[REQUIRED]**

                  The name of the Amazon S3 bucket to which data set contents are delivered.

                - **key** *(string) --* **[REQUIRED]**

                  The key of the data set contents object. Each object in an Amazon S3 bucket has a key
                  that is its unique identifier within the bucket (each object in a bucket has exactly one
                  key). To produce a unique key, you can use "!{iotanalytics:scheduledTime}" to insert the
                  time of the scheduled SQL query run, or "!{iotanalytics:versioned} to insert a unique
                  hash identifying the data set, for example:
                  "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

                - **glueConfiguration** *(dict) --*

                  Configuration information for coordination with the AWS Glue ETL (extract, transform and
                  load) service.

                  - **tableName** *(string) --* **[REQUIRED]**

                    The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
                    (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
                    partitioned data and descriptions of data sources and targets.)

                  - **databaseName** *(string) --* **[REQUIRED]**

                    The name of the database in your AWS Glue Data Catalog in which the table is located.
                    (An AWS Glue Data Catalog database contains Glue Data tables.)

                - **roleArn** *(string) --* **[REQUIRED]**

                  The ARN of the role which grants AWS IoT Analytics permission to interact with your
                  Amazon S3 and AWS Glue resources.

        :type retentionPeriod: dict
        :param retentionPeriod:

          [Optional] How long, in days, versions of data set contents are kept for the data set. If not
          specified or set to null, versions of data set contents are retained for at most 90 days. The
          number of versions of data set contents retained is determined by the ``versioningConfiguration``
          parameter. (For more information, see
          https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)
        https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)

          - **unlimited** *(boolean) --*

            If true, message data is kept indefinitely.

          - **numberOfDays** *(integer) --*

            The number of days that message data is kept. The "unlimited" parameter must be false.

        :type versioningConfiguration: dict
        :param versioningConfiguration:

          [Optional] How many versions of data set contents are kept. If not specified or set to null, only
          the latest version plus the latest succeeded version (if they are different) are kept for the
          time period specified by the "retentionPeriod" parameter. (For more information, see
          https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)
        https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)

          - **unlimited** *(boolean) --*

            If true, unlimited versions of data set contents will be kept.

          - **maxVersions** *(integer) --*

            How many versions of data set contents will be kept. The "unlimited" parameter must be false.

        :type tags: list
        :param tags:

          Metadata which can be used to manage the data set.

          - *(dict) --*

            A set of key/value pairs which are used to manage the resource.

            - **key** *(string) --* **[REQUIRED]**

              The tag's key.

            - **value** *(string) --* **[REQUIRED]**

              The tag's value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'datasetName': 'string',
                'datasetArn': 'string',
                'retentionPeriod': {
                    'unlimited': True|False,
                    'numberOfDays': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            - **datasetName** *(string) --*

              The name of the data set.

            - **datasetArn** *(string) --*

              The ARN of the data set.

            - **retentionPeriod** *(dict) --*

              How long, in days, data set contents are kept for the data set.

              - **unlimited** *(boolean) --*

                If true, message data is kept indefinitely.

              - **numberOfDays** *(integer) --*

                The number of days that message data is kept. The "unlimited" parameter must be false.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataset_content(
        self, datasetName: str
    ) -> ClientCreateDatasetContentResponseTypeDef:
        """
        Creates the content of a data set by applying a "queryAction" (a SQL query) or a "containerAction"
        (executing a containerized application).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateDatasetContent>`_

        **Request Syntax**
        ::

          response = client.create_dataset_content(
              datasetName='string'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]**

          The name of the data set.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'versionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **versionId** *(string) --*

              The version ID of the data set contents which are being created.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_datastore(
        self,
        datastoreName: str,
        datastoreStorage: ClientCreateDatastoredatastoreStorageTypeDef = None,
        retentionPeriod: ClientCreateDatastoreretentionPeriodTypeDef = None,
        tags: List[ClientCreateDatastoretagsTypeDef] = None,
    ) -> ClientCreateDatastoreResponseTypeDef:
        """
        Creates a data store, which is a repository for messages.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateDatastore>`_

        **Request Syntax**
        ::

          response = client.create_datastore(
              datastoreName='string',
              datastoreStorage={
                  'serviceManagedS3': {}
                  ,
                  'customerManagedS3': {
                      'bucket': 'string',
                      'keyPrefix': 'string',
                      'roleArn': 'string'
                  }
              },
              retentionPeriod={
                  'unlimited': True|False,
                  'numberOfDays': 123
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type datastoreName: string
        :param datastoreName: **[REQUIRED]**

          The name of the data store.

        :type datastoreStorage: dict
        :param datastoreStorage:

          Where data store data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
          storage. If not specified, the default is "serviceManagedS3". This cannot be changed after the
          data store is created.

          - **serviceManagedS3** *(dict) --*

            Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics service. The
            choice of service-managed or customer-managed S3 storage cannot be changed after creation of
            the data store.

          - **customerManagedS3** *(dict) --*

            Use this to store data store data in an S3 bucket that you manage. When customer managed
            storage is selected, the "retentionPeriod" parameter is ignored. The choice of service-managed
            or customer-managed S3 storage cannot be changed after creation of the data store.

            - **bucket** *(string) --* **[REQUIRED]**

              The name of the Amazon S3 bucket in which data store data is stored.

            - **keyPrefix** *(string) --*

              [Optional] The prefix used to create the keys of the data store data objects. Each object in
              an Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in
              a bucket has exactly one key). The prefix must end with a '/'.

            - **roleArn** *(string) --* **[REQUIRED]**

              The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
              resources.

        :type retentionPeriod: dict
        :param retentionPeriod:

          How long, in days, message data is kept for the data store. When "customerManagedS3" storage is
          selected, this parameter is ignored.

          - **unlimited** *(boolean) --*

            If true, message data is kept indefinitely.

          - **numberOfDays** *(integer) --*

            The number of days that message data is kept. The "unlimited" parameter must be false.

        :type tags: list
        :param tags:

          Metadata which can be used to manage the data store.

          - *(dict) --*

            A set of key/value pairs which are used to manage the resource.

            - **key** *(string) --* **[REQUIRED]**

              The tag's key.

            - **value** *(string) --* **[REQUIRED]**

              The tag's value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'datastoreName': 'string',
                'datastoreArn': 'string',
                'retentionPeriod': {
                    'unlimited': True|False,
                    'numberOfDays': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            - **datastoreName** *(string) --*

              The name of the data store.

            - **datastoreArn** *(string) --*

              The ARN of the data store.

            - **retentionPeriod** *(dict) --*

              How long, in days, message data is kept for the data store.

              - **unlimited** *(boolean) --*

                If true, message data is kept indefinitely.

              - **numberOfDays** *(integer) --*

                The number of days that message data is kept. The "unlimited" parameter must be false.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_pipeline(
        self,
        pipelineName: str,
        pipelineActivities: List[ClientCreatePipelinepipelineActivitiesTypeDef],
        tags: List[ClientCreatePipelinetagsTypeDef] = None,
    ) -> ClientCreatePipelineResponseTypeDef:
        """
        Creates a pipeline. A pipeline consumes messages from a channel and allows you to process the
        messages before storing them in a data store. You must specify both a ``channel`` and a
        ``datastore`` activity and, optionally, as many as 23 additional activities in the
        ``pipelineActivities`` array.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreatePipeline>`_

        **Request Syntax**
        ::

          response = client.create_pipeline(
              pipelineName='string',
              pipelineActivities=[
                  {
                      'channel': {
                          'name': 'string',
                          'channelName': 'string',
                          'next': 'string'
                      },
                      'lambda': {
                          'name': 'string',
                          'lambdaName': 'string',
                          'batchSize': 123,
                          'next': 'string'
                      },
                      'datastore': {
                          'name': 'string',
                          'datastoreName': 'string'
                      },
                      'addAttributes': {
                          'name': 'string',
                          'attributes': {
                              'string': 'string'
                          },
                          'next': 'string'
                      },
                      'removeAttributes': {
                          'name': 'string',
                          'attributes': [
                              'string',
                          ],
                          'next': 'string'
                      },
                      'selectAttributes': {
                          'name': 'string',
                          'attributes': [
                              'string',
                          ],
                          'next': 'string'
                      },
                      'filter': {
                          'name': 'string',
                          'filter': 'string',
                          'next': 'string'
                      },
                      'math': {
                          'name': 'string',
                          'attribute': 'string',
                          'math': 'string',
                          'next': 'string'
                      },
                      'deviceRegistryEnrich': {
                          'name': 'string',
                          'attribute': 'string',
                          'thingName': 'string',
                          'roleArn': 'string',
                          'next': 'string'
                      },
                      'deviceShadowEnrich': {
                          'name': 'string',
                          'attribute': 'string',
                          'thingName': 'string',
                          'roleArn': 'string',
                          'next': 'string'
                      }
                  },
              ],
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**

          The name of the pipeline.

        :type pipelineActivities: list
        :param pipelineActivities: **[REQUIRED]**

          A list of "PipelineActivity" objects. Activities perform transformations on your messages, such
          as removing, renaming or adding message attributes; filtering messages based on attribute values;
          invoking your Lambda functions on messages for advanced processing; or performing mathematical
          transformations to normalize device data.

          The list can be 2-25 **PipelineActivity** objects and must contain both a ``channel`` and a
          ``datastore`` activity. Each entry in the list must contain only one activity, for example:

           ``pipelineActivities = [ { "channel": { ... } }, { "lambda": { ... } }, ... ]``

          - *(dict) --*

            An activity that performs a transformation on a message.

            - **channel** *(dict) --*

              Determines the source of the messages to be processed.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'channel' activity.

              - **channelName** *(string) --* **[REQUIRED]**

                The name of the channel from which the messages are processed.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **lambda** *(dict) --*

              Runs a Lambda function to modify the message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'lambda' activity.

              - **lambdaName** *(string) --* **[REQUIRED]**

                The name of the Lambda function that is run on the message.

              - **batchSize** *(integer) --* **[REQUIRED]**

                The number of messages passed to the Lambda function for processing.

                The AWS Lambda function must be able to process all of these messages within five minutes,
                which is the maximum timeout duration for Lambda functions.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **datastore** *(dict) --*

              Specifies where to store the processed message data.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'datastore' activity.

              - **datastoreName** *(string) --* **[REQUIRED]**

                The name of the data store where processed messages are stored.

            - **addAttributes** *(dict) --*

              Adds other attributes based on existing attributes in the message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'addAttributes' activity.

              - **attributes** *(dict) --* **[REQUIRED]**

                A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
                attribute.

                .. note::

                  The existing attributes remain in the message, so if you want to remove the originals,
                  use "RemoveAttributeActivity".

                - *(string) --*

                  - *(string) --*

              - **next** *(string) --*

                The next activity in the pipeline.

            - **removeAttributes** *(dict) --*

              Removes attributes from a message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'removeAttributes' activity.

              - **attributes** *(list) --* **[REQUIRED]**

                A list of 1-50 attributes to remove from the message.

                - *(string) --*

              - **next** *(string) --*

                The next activity in the pipeline.

            - **selectAttributes** *(dict) --*

              Creates a new message using only the specified attributes from the original message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'selectAttributes' activity.

              - **attributes** *(list) --* **[REQUIRED]**

                A list of the attributes to select from the message.

                - *(string) --*

              - **next** *(string) --*

                The next activity in the pipeline.

            - **filter** *(dict) --*

              Filters a message based on its attributes.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'filter' activity.

              - **filter** *(string) --* **[REQUIRED]**

                An expression that looks like a SQL WHERE clause that must return a Boolean value.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **math** *(dict) --*

              Computes an arithmetic expression using the message's attributes and adds it to the message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'math' activity.

              - **attribute** *(string) --* **[REQUIRED]**

                The name of the attribute that contains the result of the math operation.

              - **math** *(string) --* **[REQUIRED]**

                An expression that uses one or more existing attributes and must return an integer value.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **deviceRegistryEnrich** *(dict) --*

              Adds data from the AWS IoT device registry to your message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'deviceRegistryEnrich' activity.

              - **attribute** *(string) --* **[REQUIRED]**

                The name of the attribute that is added to the message.

              - **thingName** *(string) --* **[REQUIRED]**

                The name of the IoT device whose registry information is added to the message.

              - **roleArn** *(string) --* **[REQUIRED]**

                The ARN of the role that allows access to the device's registry information.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **deviceShadowEnrich** *(dict) --*

              Adds information from the AWS IoT Device Shadows service to a message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'deviceShadowEnrich' activity.

              - **attribute** *(string) --* **[REQUIRED]**

                The name of the attribute that is added to the message.

              - **thingName** *(string) --* **[REQUIRED]**

                The name of the IoT device whose shadow information is added to the message.

              - **roleArn** *(string) --* **[REQUIRED]**

                The ARN of the role that allows access to the device's shadow.

              - **next** *(string) --*

                The next activity in the pipeline.

        :type tags: list
        :param tags:

          Metadata which can be used to manage the pipeline.

          - *(dict) --*

            A set of key/value pairs which are used to manage the resource.

            - **key** *(string) --* **[REQUIRED]**

              The tag's key.

            - **value** *(string) --* **[REQUIRED]**

              The tag's value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pipelineName': 'string',
                'pipelineArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **pipelineName** *(string) --*

              The name of the pipeline.

            - **pipelineArn** *(string) --*

              The ARN of the pipeline.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_channel(self, channelName: str) -> None:
        """
        Deletes the specified channel.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeleteChannel>`_

        **Request Syntax**
        ::

          response = client.delete_channel(
              channelName='string'
          )
        :type channelName: string
        :param channelName: **[REQUIRED]**

          The name of the channel to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataset(self, datasetName: str) -> None:
        """
        Deletes the specified data set.

        You do not have to delete the content of the data set before you perform this operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeleteDataset>`_

        **Request Syntax**
        ::

          response = client.delete_dataset(
              datasetName='string'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]**

          The name of the data set to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataset_content(self, datasetName: str, versionId: str = None) -> None:
        """
        Deletes the content of the specified data set.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeleteDatasetContent>`_

        **Request Syntax**
        ::

          response = client.delete_dataset_content(
              datasetName='string',
              versionId='string'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]**

          The name of the data set whose content is deleted.

        :type versionId: string
        :param versionId:

          The version of the data set whose content is deleted. You can also use the strings "$LATEST" or
          "$LATEST_SUCCEEDED" to delete the latest or latest successfully completed data set. If not
          specified, "$LATEST_SUCCEEDED" is the default.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_datastore(self, datastoreName: str) -> None:
        """
        Deletes the specified data store.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeleteDatastore>`_

        **Request Syntax**
        ::

          response = client.delete_datastore(
              datastoreName='string'
          )
        :type datastoreName: string
        :param datastoreName: **[REQUIRED]**

          The name of the data store to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_pipeline(self, pipelineName: str) -> None:
        """
        Deletes the specified pipeline.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeletePipeline>`_

        **Request Syntax**
        ::

          response = client.delete_pipeline(
              pipelineName='string'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**

          The name of the pipeline to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_channel(
        self, channelName: str, includeStatistics: bool = None
    ) -> ClientDescribeChannelResponseTypeDef:
        """
        Retrieves information about a channel.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeChannel>`_

        **Request Syntax**
        ::

          response = client.describe_channel(
              channelName='string',
              includeStatistics=True|False
          )
        :type channelName: string
        :param channelName: **[REQUIRED]**

          The name of the channel whose information is retrieved.

        :type includeStatistics: boolean
        :param includeStatistics:

          If true, additional statistical information about the channel is included in the response. This
          feature cannot be used with a channel whose S3 storage is customer-managed.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'channel': {
                    'name': 'string',
                    'storage': {
                        'serviceManagedS3': {},
                        'customerManagedS3': {
                            'bucket': 'string',
                            'keyPrefix': 'string',
                            'roleArn': 'string'
                        }
                    },
                    'arn': 'string',
                    'status': 'CREATING'|'ACTIVE'|'DELETING',
                    'retentionPeriod': {
                        'unlimited': True|False,
                        'numberOfDays': 123
                    },
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdateTime': datetime(2015, 1, 1)
                },
                'statistics': {
                    'size': {
                        'estimatedSizeInBytes': 123.0,
                        'estimatedOn': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **channel** *(dict) --*

              An object that contains information about the channel.

              - **name** *(string) --*

                The name of the channel.

              - **storage** *(dict) --*

                Where channel data is stored. You may choose one of "serviceManagedS3" or
                "customerManagedS3" storage. If not specified, the default is "serviceManagedS3". This
                cannot be changed after creation of the channel.

                - **serviceManagedS3** *(dict) --*

                  Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service.
                  The choice of service-managed or customer-managed S3 storage cannot be changed after
                  creation of the channel.

                - **customerManagedS3** *(dict) --*

                  Use this to store channel data in an S3 bucket that you manage. If customer managed
                  storage is selected, the "retentionPeriod" parameter is ignored. The choice of
                  service-managed or customer-managed S3 storage cannot be changed after creation of the
                  channel.

                  - **bucket** *(string) --*

                    The name of the Amazon S3 bucket in which channel data is stored.

                  - **keyPrefix** *(string) --*

                    [Optional] The prefix used to create the keys of the channel data objects. Each object
                    in an Amazon S3 bucket has a key that is its unique identifier within the bucket (each
                    object in a bucket has exactly one key). The prefix must end with a '/'.

                  - **roleArn** *(string) --*

                    The ARN of the role which grants AWS IoT Analytics permission to interact with your
                    Amazon S3 resources.

              - **arn** *(string) --*

                The ARN of the channel.

              - **status** *(string) --*

                The status of the channel.

              - **retentionPeriod** *(dict) --*

                How long, in days, message data is kept for the channel.

                - **unlimited** *(boolean) --*

                  If true, message data is kept indefinitely.

                - **numberOfDays** *(integer) --*

                  The number of days that message data is kept. The "unlimited" parameter must be false.

              - **creationTime** *(datetime) --*

                When the channel was created.

              - **lastUpdateTime** *(datetime) --*

                When the channel was last updated.

            - **statistics** *(dict) --*

              Statistics about the channel. Included if the 'includeStatistics' parameter is set to true in
              the request.

              - **size** *(dict) --*

                The estimated size of the channel.

                - **estimatedSizeInBytes** *(float) --*

                  The estimated size of the resource in bytes.

                - **estimatedOn** *(datetime) --*

                  The time when the estimate of the size of the resource was made.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dataset(self, datasetName: str) -> Dict[str, Any]:
        """
        Retrieves information about a data set.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeDataset>`_

        **Request Syntax**
        ::

          response = client.describe_dataset(
              datasetName='string'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]**

          The name of the data set whose information is retrieved.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'dataset': {
                    'name': 'string',
                    'arn': 'string',
                    'actions': [
                        {
                            'actionName': 'string',
                            'queryAction': {
                                'sqlQuery': 'string',
                                'filters': [
                                    {
                                        'deltaTime': {
                                            'offsetSeconds': 123,
                                            'timeExpression': 'string'
                                        }
                                    },
                                ]
                            },
                            'containerAction': {
                                'image': 'string',
                                'executionRoleArn': 'string',
                                'resourceConfiguration': {
                                    'computeType': 'ACU_1'|'ACU_2',
                                    'volumeSizeInGB': 123
                                },
                                'variables': [
                                    {
                                        'name': 'string',
                                        'stringValue': 'string',
                                        'doubleValue': 123.0,
                                        'datasetContentVersionValue': {
                                            'datasetName': 'string'
                                        },
                                        'outputFileUriValue': {
                                            'fileName': 'string'
                                        }
                                    },
                                ]
                            }
                        },
                    ],
                    'triggers': [
                        {
                            'schedule': {
                                'expression': 'string'
                            },
                            'dataset': {
                                'name': 'string'
                            }
                        },
                    ],
                    'contentDeliveryRules': [
                        {
                            'entryName': 'string',
                            'destination': {
                                'iotEventsDestinationConfiguration': {
                                    'inputName': 'string',
                                    'roleArn': 'string'
                                },
                                's3DestinationConfiguration': {
                                    'bucket': 'string',
                                    'key': 'string',
                                    'glueConfiguration': {
                                        'tableName': 'string',
                                        'databaseName': 'string'
                                    },
                                    'roleArn': 'string'
                                }
                            }
                        },
                    ],
                    'status': 'CREATING'|'ACTIVE'|'DELETING',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdateTime': datetime(2015, 1, 1),
                    'retentionPeriod': {
                        'unlimited': True|False,
                        'numberOfDays': 123
                    },
                    'versioningConfiguration': {
                        'unlimited': True|False,
                        'maxVersions': 123
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **dataset** *(dict) --*

              An object that contains information about the data set.

              - **name** *(string) --*

                The name of the data set.

              - **arn** *(string) --*

                The ARN of the data set.

              - **actions** *(list) --*

                The "DatasetAction" objects that automatically create the data set contents.

                - *(dict) --*

                  A "DatasetAction" object that specifies how data set contents are automatically created.

                  - **actionName** *(string) --*

                    The name of the data set action by which data set contents are automatically created.

                  - **queryAction** *(dict) --*

                    An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data
                    set contents.

                    - **sqlQuery** *(string) --*

                      A SQL query string.

                    - **filters** *(list) --*

                      Pre-filters applied to message data.

                      - *(dict) --*

                        Information which is used to filter message data, to segregate it according to the
                        time frame in which it arrives.

                        - **deltaTime** *(dict) --*

                          Used to limit data to that which has arrived since the last execution of the
                          action.

                          - **offsetSeconds** *(integer) --*

                            The number of seconds of estimated "in flight" lag time of message data. When
                            you create data set contents using message data from a specified time frame,
                            some message data may still be "in flight" when processing begins, and so will
                            not arrive in time to be processed. Use this field to make allowances for the
                            "in flight" time of your message data, so that data not processed from a
                            previous time frame will be included with the next time frame. Without this,
                            missed message data would be excluded from processing during the next time
                            frame as well, because its timestamp places it within the previous time frame.

                          - **timeExpression** *(string) --*

                            An expression by which the time of the message data may be determined. This may
                            be the name of a timestamp field, or a SQL expression which is used to derive
                            the time the message data was generated.

                  - **containerAction** *(dict) --*

                    Information which allows the system to run a containerized application in order to
                    create the data set contents. The application must be in a Docker container along with
                    any needed support libraries.

                    - **image** *(string) --*

                      The ARN of the Docker container stored in your account. The Docker container contains
                      an application and needed support libraries and is used to generate data set contents.

                    - **executionRoleArn** *(string) --*

                      The ARN of the role which gives permission to the system to access needed resources
                      in order to run the "containerAction". This includes, at minimum, permission to
                      retrieve the data set contents which are the input to the containerized application.

                    - **resourceConfiguration** *(dict) --*

                      Configuration of the resource which executes the "containerAction".

                      - **computeType** *(string) --*

                        The type of the compute resource used to execute the "containerAction". Possible
                        values are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

                      - **volumeSizeInGB** *(integer) --*

                        The size (in GB) of the persistent storage available to the resource instance used
                        to execute the "containerAction" (min: 1, max: 50).

                    - **variables** *(list) --*

                      The values of variables used within the context of the execution of the containerized
                      application (basically, parameters passed to the application). Each variable must
                      have a name and a value given by one of "stringValue", "datasetContentVersionValue",
                      or "outputFileUriValue".

                      - *(dict) --*

                        An instance of a variable to be passed to the "containerAction" execution. Each
                        variable must have a name and a value given by one of "stringValue",
                        "datasetContentVersionValue", or "outputFileUriValue".

                        - **name** *(string) --*

                          The name of the variable.

                        - **stringValue** *(string) --*

                          The value of the variable as a string.

                        - **doubleValue** *(float) --*

                          The value of the variable as a double (numeric).

                        - **datasetContentVersionValue** *(dict) --*

                          The value of the variable as a structure that specifies a data set content
                          version.

                          - **datasetName** *(string) --*

                            The name of the data set whose latest contents are used as input to the
                            notebook or application.

                        - **outputFileUriValue** *(dict) --*

                          The value of the variable as a structure that specifies an output file URI.

                          - **fileName** *(string) --*

                            The URI of the location where data set contents are stored, usually the URI of
                            a file in an S3 bucket.

              - **triggers** *(list) --*

                The "DatasetTrigger" objects that specify when the data set is automatically updated.

                - *(dict) --*

                  The "DatasetTrigger" that specifies when the data set is automatically updated.

                  - **schedule** *(dict) --*

                    The "Schedule" when the trigger is initiated.

                    - **expression** *(string) --*

                      The expression that defines when to trigger an update. For more information, see
                      `Schedule Expressions for Rules
                      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
                      in the Amazon CloudWatch Events User Guide.

                  - **dataset** *(dict) --*

                    The data set whose content creation triggers the creation of this data set's contents.

                    - **name** *(string) --*

                      The name of the data set whose content generation triggers the new data set content
                      generation.

              - **contentDeliveryRules** *(list) --*

                When data set contents are created they are delivered to destinations specified here.

                - *(dict) --*

                  When data set contents are created they are delivered to destination specified here.

                  - **entryName** *(string) --*

                    The name of the data set content delivery rules entry.

                  - **destination** *(dict) --*

                    The destination to which data set contents are delivered.

                    - **iotEventsDestinationConfiguration** *(dict) --*

                      Configuration information for delivery of data set contents to AWS IoT Events.

                      - **inputName** *(string) --*

                        The name of the AWS IoT Events input to which data set contents are delivered.

                      - **roleArn** *(string) --*

                        The ARN of the role which grants AWS IoT Analytics permission to deliver data set
                        contents to an AWS IoT Events input.

                    - **s3DestinationConfiguration** *(dict) --*

                      Configuration information for delivery of data set contents to Amazon S3.

                      - **bucket** *(string) --*

                        The name of the Amazon S3 bucket to which data set contents are delivered.

                      - **key** *(string) --*

                        The key of the data set contents object. Each object in an Amazon S3 bucket has a
                        key that is its unique identifier within the bucket (each object in a bucket has
                        exactly one key). To produce a unique key, you can use
                        "!{iotanalytics:scheduledTime}" to insert the time of the scheduled SQL query run,
                        or "!{iotanalytics:versioned} to insert a unique hash identifying the data set, for
                        example: "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

                      - **glueConfiguration** *(dict) --*

                        Configuration information for coordination with the AWS Glue ETL (extract,
                        transform and load) service.

                        - **tableName** *(string) --*

                          The name of the table in your AWS Glue Data Catalog which is used to perform the
                          ETL (extract, transform and load) operations. (An AWS Glue Data Catalog table
                          contains partitioned data and descriptions of data sources and targets.)

                        - **databaseName** *(string) --*

                          The name of the database in your AWS Glue Data Catalog in which the table is
                          located. (An AWS Glue Data Catalog database contains Glue Data tables.)

                      - **roleArn** *(string) --*

                        The ARN of the role which grants AWS IoT Analytics permission to interact with your
                        Amazon S3 and AWS Glue resources.

              - **status** *(string) --*

                The status of the data set.

              - **creationTime** *(datetime) --*

                When the data set was created.

              - **lastUpdateTime** *(datetime) --*

                The last time the data set was updated.

              - **retentionPeriod** *(dict) --*

                [Optional] How long, in days, message data is kept for the data set.

                - **unlimited** *(boolean) --*

                  If true, message data is kept indefinitely.

                - **numberOfDays** *(integer) --*

                  The number of days that message data is kept. The "unlimited" parameter must be false.

              - **versioningConfiguration** *(dict) --*

                [Optional] How many versions of data set contents are kept. If not specified or set to
                null, only the latest version plus the latest succeeded version (if they are different) are
                kept for the time period specified by the "retentionPeriod" parameter. (For more
                information, see
                https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)
        https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)

                - **unlimited** *(boolean) --*

                  If true, unlimited versions of data set contents will be kept.

                - **maxVersions** *(integer) --*

                  How many versions of data set contents will be kept. The "unlimited" parameter must be
                  false.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_datastore(
        self, datastoreName: str, includeStatistics: bool = None
    ) -> ClientDescribeDatastoreResponseTypeDef:
        """
        Retrieves information about a data store.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeDatastore>`_

        **Request Syntax**
        ::

          response = client.describe_datastore(
              datastoreName='string',
              includeStatistics=True|False
          )
        :type datastoreName: string
        :param datastoreName: **[REQUIRED]**

          The name of the data store

        :type includeStatistics: boolean
        :param includeStatistics:

          If true, additional statistical information about the data store is included in the response.
          This feature cannot be used with a data store whose S3 storage is customer-managed.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'datastore': {
                    'name': 'string',
                    'storage': {
                        'serviceManagedS3': {},
                        'customerManagedS3': {
                            'bucket': 'string',
                            'keyPrefix': 'string',
                            'roleArn': 'string'
                        }
                    },
                    'arn': 'string',
                    'status': 'CREATING'|'ACTIVE'|'DELETING',
                    'retentionPeriod': {
                        'unlimited': True|False,
                        'numberOfDays': 123
                    },
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdateTime': datetime(2015, 1, 1)
                },
                'statistics': {
                    'size': {
                        'estimatedSizeInBytes': 123.0,
                        'estimatedOn': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **datastore** *(dict) --*

              Information about the data store.

              - **name** *(string) --*

                The name of the data store.

              - **storage** *(dict) --*

                Where data store data is stored. You may choose one of "serviceManagedS3" or
                "customerManagedS3" storage. If not specified, the default is "serviceManagedS3". This
                cannot be changed after the data store is created.

                - **serviceManagedS3** *(dict) --*

                  Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics
                  service. The choice of service-managed or customer-managed S3 storage cannot be changed
                  after creation of the data store.

                - **customerManagedS3** *(dict) --*

                  Use this to store data store data in an S3 bucket that you manage. When customer managed
                  storage is selected, the "retentionPeriod" parameter is ignored. The choice of
                  service-managed or customer-managed S3 storage cannot be changed after creation of the
                  data store.

                  - **bucket** *(string) --*

                    The name of the Amazon S3 bucket in which data store data is stored.

                  - **keyPrefix** *(string) --*

                    [Optional] The prefix used to create the keys of the data store data objects. Each
                    object in an Amazon S3 bucket has a key that is its unique identifier within the bucket
                    (each object in a bucket has exactly one key). The prefix must end with a '/'.

                  - **roleArn** *(string) --*

                    The ARN of the role which grants AWS IoT Analytics permission to interact with your
                    Amazon S3 resources.

              - **arn** *(string) --*

                The ARN of the data store.

              - **status** *(string) --*

                The status of a data store:

                  CREATING

                The data store is being created.

                  ACTIVE

                The data store has been created and can be used.

                  DELETING

                The data store is being deleted.

              - **retentionPeriod** *(dict) --*

                How long, in days, message data is kept for the data store. When "customerManagedS3"
                storage is selected, this parameter is ignored.

                - **unlimited** *(boolean) --*

                  If true, message data is kept indefinitely.

                - **numberOfDays** *(integer) --*

                  The number of days that message data is kept. The "unlimited" parameter must be false.

              - **creationTime** *(datetime) --*

                When the data store was created.

              - **lastUpdateTime** *(datetime) --*

                The last time the data store was updated.

            - **statistics** *(dict) --*

              Additional statistical information about the data store. Included if the 'includeStatistics'
              parameter is set to true in the request.

              - **size** *(dict) --*

                The estimated size of the data store.

                - **estimatedSizeInBytes** *(float) --*

                  The estimated size of the resource in bytes.

                - **estimatedOn** *(datetime) --*

                  The time when the estimate of the size of the resource was made.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_logging_options(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeLoggingOptionsResponseTypeDef:
        """
        Retrieves the current settings of the AWS IoT Analytics logging options.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeLoggingOptions>`_

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
                    'level': 'ERROR',
                    'enabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **loggingOptions** *(dict) --*

              The current settings of the AWS IoT Analytics logging options.

              - **roleArn** *(string) --*

                The ARN of the role that grants permission to AWS IoT Analytics to perform logging.

              - **level** *(string) --*

                The logging level. Currently, only "ERROR" is supported.

              - **enabled** *(boolean) --*

                If true, logging is enabled for AWS IoT Analytics.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pipeline(
        self, pipelineName: str
    ) -> ClientDescribePipelineResponseTypeDef:
        """
        Retrieves information about a pipeline.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribePipeline>`_

        **Request Syntax**
        ::

          response = client.describe_pipeline(
              pipelineName='string'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**

          The name of the pipeline whose information is retrieved.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pipeline': {
                    'name': 'string',
                    'arn': 'string',
                    'activities': [
                        {
                            'channel': {
                                'name': 'string',
                                'channelName': 'string',
                                'next': 'string'
                            },
                            'lambda': {
                                'name': 'string',
                                'lambdaName': 'string',
                                'batchSize': 123,
                                'next': 'string'
                            },
                            'datastore': {
                                'name': 'string',
                                'datastoreName': 'string'
                            },
                            'addAttributes': {
                                'name': 'string',
                                'attributes': {
                                    'string': 'string'
                                },
                                'next': 'string'
                            },
                            'removeAttributes': {
                                'name': 'string',
                                'attributes': [
                                    'string',
                                ],
                                'next': 'string'
                            },
                            'selectAttributes': {
                                'name': 'string',
                                'attributes': [
                                    'string',
                                ],
                                'next': 'string'
                            },
                            'filter': {
                                'name': 'string',
                                'filter': 'string',
                                'next': 'string'
                            },
                            'math': {
                                'name': 'string',
                                'attribute': 'string',
                                'math': 'string',
                                'next': 'string'
                            },
                            'deviceRegistryEnrich': {
                                'name': 'string',
                                'attribute': 'string',
                                'thingName': 'string',
                                'roleArn': 'string',
                                'next': 'string'
                            },
                            'deviceShadowEnrich': {
                                'name': 'string',
                                'attribute': 'string',
                                'thingName': 'string',
                                'roleArn': 'string',
                                'next': 'string'
                            }
                        },
                    ],
                    'reprocessingSummaries': [
                        {
                            'id': 'string',
                            'status': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                            'creationTime': datetime(2015, 1, 1)
                        },
                    ],
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdateTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pipeline** *(dict) --*

              A "Pipeline" object that contains information about the pipeline.

              - **name** *(string) --*

                The name of the pipeline.

              - **arn** *(string) --*

                The ARN of the pipeline.

              - **activities** *(list) --*

                The activities that perform transformations on the messages.

                - *(dict) --*

                  An activity that performs a transformation on a message.

                  - **channel** *(dict) --*

                    Determines the source of the messages to be processed.

                    - **name** *(string) --*

                      The name of the 'channel' activity.

                    - **channelName** *(string) --*

                      The name of the channel from which the messages are processed.

                    - **next** *(string) --*

                      The next activity in the pipeline.

                  - **lambda** *(dict) --*

                    Runs a Lambda function to modify the message.

                    - **name** *(string) --*

                      The name of the 'lambda' activity.

                    - **lambdaName** *(string) --*

                      The name of the Lambda function that is run on the message.

                    - **batchSize** *(integer) --*

                      The number of messages passed to the Lambda function for processing.

                      The AWS Lambda function must be able to process all of these messages within five
                      minutes, which is the maximum timeout duration for Lambda functions.

                    - **next** *(string) --*

                      The next activity in the pipeline.

                  - **datastore** *(dict) --*

                    Specifies where to store the processed message data.

                    - **name** *(string) --*

                      The name of the 'datastore' activity.

                    - **datastoreName** *(string) --*

                      The name of the data store where processed messages are stored.

                  - **addAttributes** *(dict) --*

                    Adds other attributes based on existing attributes in the message.

                    - **name** *(string) --*

                      The name of the 'addAttributes' activity.

                    - **attributes** *(dict) --*

                      A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
                      attribute.

                      .. note::

                        The existing attributes remain in the message, so if you want to remove the
                        originals, use "RemoveAttributeActivity".

                      - *(string) --*

                        - *(string) --*

                    - **next** *(string) --*

                      The next activity in the pipeline.

                  - **removeAttributes** *(dict) --*

                    Removes attributes from a message.

                    - **name** *(string) --*

                      The name of the 'removeAttributes' activity.

                    - **attributes** *(list) --*

                      A list of 1-50 attributes to remove from the message.

                      - *(string) --*

                    - **next** *(string) --*

                      The next activity in the pipeline.

                  - **selectAttributes** *(dict) --*

                    Creates a new message using only the specified attributes from the original message.

                    - **name** *(string) --*

                      The name of the 'selectAttributes' activity.

                    - **attributes** *(list) --*

                      A list of the attributes to select from the message.

                      - *(string) --*

                    - **next** *(string) --*

                      The next activity in the pipeline.

                  - **filter** *(dict) --*

                    Filters a message based on its attributes.

                    - **name** *(string) --*

                      The name of the 'filter' activity.

                    - **filter** *(string) --*

                      An expression that looks like a SQL WHERE clause that must return a Boolean value.

                    - **next** *(string) --*

                      The next activity in the pipeline.

                  - **math** *(dict) --*

                    Computes an arithmetic expression using the message's attributes and adds it to the
                    message.

                    - **name** *(string) --*

                      The name of the 'math' activity.

                    - **attribute** *(string) --*

                      The name of the attribute that contains the result of the math operation.

                    - **math** *(string) --*

                      An expression that uses one or more existing attributes and must return an integer
                      value.

                    - **next** *(string) --*

                      The next activity in the pipeline.

                  - **deviceRegistryEnrich** *(dict) --*

                    Adds data from the AWS IoT device registry to your message.

                    - **name** *(string) --*

                      The name of the 'deviceRegistryEnrich' activity.

                    - **attribute** *(string) --*

                      The name of the attribute that is added to the message.

                    - **thingName** *(string) --*

                      The name of the IoT device whose registry information is added to the message.

                    - **roleArn** *(string) --*

                      The ARN of the role that allows access to the device's registry information.

                    - **next** *(string) --*

                      The next activity in the pipeline.

                  - **deviceShadowEnrich** *(dict) --*

                    Adds information from the AWS IoT Device Shadows service to a message.

                    - **name** *(string) --*

                      The name of the 'deviceShadowEnrich' activity.

                    - **attribute** *(string) --*

                      The name of the attribute that is added to the message.

                    - **thingName** *(string) --*

                      The name of the IoT device whose shadow information is added to the message.

                    - **roleArn** *(string) --*

                      The ARN of the role that allows access to the device's shadow.

                    - **next** *(string) --*

                      The next activity in the pipeline.

              - **reprocessingSummaries** *(list) --*

                A summary of information about the pipeline reprocessing.

                - *(dict) --*

                  Information about pipeline reprocessing.

                  - **id** *(string) --*

                    The 'reprocessingId' returned by "StartPipelineReprocessing".

                  - **status** *(string) --*

                    The status of the pipeline reprocessing.

                  - **creationTime** *(datetime) --*

                    The time the pipeline reprocessing was created.

              - **creationTime** *(datetime) --*

                When the pipeline was created.

              - **lastUpdateTime** *(datetime) --*

                The last time the pipeline was updated.

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
    def get_dataset_content(
        self, datasetName: str, versionId: str = None
    ) -> ClientGetDatasetContentResponseTypeDef:
        """
        Retrieves the contents of a data set as pre-signed URIs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/GetDatasetContent>`_

        **Request Syntax**
        ::

          response = client.get_dataset_content(
              datasetName='string',
              versionId='string'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]**

          The name of the data set whose contents are retrieved.

        :type versionId: string
        :param versionId:

          The version of the data set whose contents are retrieved. You can also use the strings "$LATEST"
          or "$LATEST_SUCCEEDED" to retrieve the contents of the latest or latest successfully completed
          data set. If not specified, "$LATEST_SUCCEEDED" is the default.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'entries': [
                    {
                        'entryName': 'string',
                        'dataURI': 'string'
                    },
                ],
                'timestamp': datetime(2015, 1, 1),
                'status': {
                    'state': 'CREATING'|'SUCCEEDED'|'FAILED',
                    'reason': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **entries** *(list) --*

              A list of "DatasetEntry" objects.

              - *(dict) --*

                The reference to a data set entry.

                - **entryName** *(string) --*

                  The name of the data set item.

                - **dataURI** *(string) --*

                  The pre-signed URI of the data set item.

            - **timestamp** *(datetime) --*

              The time when the request was made.

            - **status** *(dict) --*

              The status of the data set content.

              - **state** *(string) --*

                The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
                "FAILED".

              - **reason** *(string) --*

                The reason the data set contents are in this state.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_channels(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListChannelsResponseTypeDef:
        """
        Retrieves a list of channels.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListChannels>`_

        **Request Syntax**
        ::

          response = client.list_channels(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken:

          The token for the next set of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in this request.

          The default value is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'channelSummaries': [
                    {
                        'channelName': 'string',
                        'channelStorage': {
                            'serviceManagedS3': {},
                            'customerManagedS3': {
                                'bucket': 'string',
                                'keyPrefix': 'string',
                                'roleArn': 'string'
                            }
                        },
                        'status': 'CREATING'|'ACTIVE'|'DELETING',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **channelSummaries** *(list) --*

              A list of "ChannelSummary" objects.

              - *(dict) --*

                A summary of information about a channel.

                - **channelName** *(string) --*

                  The name of the channel.

                - **channelStorage** *(dict) --*

                  Where channel data is stored.

                  - **serviceManagedS3** *(dict) --*

                    Used to store channel data in an S3 bucket managed by the AWS IoT Analytics service.

                  - **customerManagedS3** *(dict) --*

                    Used to store channel data in an S3 bucket that you manage.

                    - **bucket** *(string) --*

                      The name of the Amazon S3 bucket in which channel data is stored.

                    - **keyPrefix** *(string) --*

                      [Optional] The prefix used to create the keys of the channel data objects. Each
                      object in an Amazon S3 bucket has a key that is its unique identifier within the
                      bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

                    - **roleArn** *(string) --*

                      The ARN of the role which grants AWS IoT Analytics permission to interact with your
                      Amazon S3 resources.

                - **status** *(string) --*

                  The status of the channel.

                - **creationTime** *(datetime) --*

                  When the channel was created.

                - **lastUpdateTime** *(datetime) --*

                  The last time the channel was updated.

            - **nextToken** *(string) --*

              The token to retrieve the next set of results, or ``null`` if there are no more results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dataset_contents(
        self,
        datasetName: str,
        nextToken: str = None,
        maxResults: int = None,
        scheduledOnOrAfter: datetime = None,
        scheduledBefore: datetime = None,
    ) -> ClientListDatasetContentsResponseTypeDef:
        """
        Lists information about data set contents that have been created.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatasetContents>`_

        **Request Syntax**
        ::

          response = client.list_dataset_contents(
              datasetName='string',
              nextToken='string',
              maxResults=123,
              scheduledOnOrAfter=datetime(2015, 1, 1),
              scheduledBefore=datetime(2015, 1, 1)
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]**

          The name of the data set whose contents information you want to list.

        :type nextToken: string
        :param nextToken:

          The token for the next set of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in this request.

        :type scheduledOnOrAfter: datetime
        :param scheduledOnOrAfter:

          A filter to limit results to those data set contents whose creation is scheduled on or after the
          given time. See the field ``triggers.schedule`` in the CreateDataset request. (timestamp)

        :type scheduledBefore: datetime
        :param scheduledBefore:

          A filter to limit results to those data set contents whose creation is scheduled before the given
          time. See the field ``triggers.schedule`` in the CreateDataset request. (timestamp)

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'datasetContentSummaries': [
                    {
                        'version': 'string',
                        'status': {
                            'state': 'CREATING'|'SUCCEEDED'|'FAILED',
                            'reason': 'string'
                        },
                        'creationTime': datetime(2015, 1, 1),
                        'scheduleTime': datetime(2015, 1, 1),
                        'completionTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **datasetContentSummaries** *(list) --*

              Summary information about data set contents that have been created.

              - *(dict) --*

                Summary information about data set contents.

                - **version** *(string) --*

                  The version of the data set contents.

                - **status** *(dict) --*

                  The status of the data set contents.

                  - **state** *(string) --*

                    The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or
                    "FAILED".

                  - **reason** *(string) --*

                    The reason the data set contents are in this state.

                - **creationTime** *(datetime) --*

                  The actual time the creation of the data set contents was started.

                - **scheduleTime** *(datetime) --*

                  The time the creation of the data set contents was scheduled to start.

                - **completionTime** *(datetime) --*

                  The time the dataset content status was updated to SUCCEEDED or FAILED.

            - **nextToken** *(string) --*

              The token to retrieve the next set of results, or ``null`` if there are no more results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_datasets(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListDatasetsResponseTypeDef:
        """
        Retrieves information about data sets.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatasets>`_

        **Request Syntax**
        ::

          response = client.list_datasets(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken:

          The token for the next set of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in this request.

          The default value is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'datasetSummaries': [
                    {
                        'datasetName': 'string',
                        'status': 'CREATING'|'ACTIVE'|'DELETING',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'triggers': [
                            {
                                'schedule': {
                                    'expression': 'string'
                                },
                                'dataset': {
                                    'name': 'string'
                                }
                            },
                        ],
                        'actions': [
                            {
                                'actionName': 'string',
                                'actionType': 'QUERY'|'CONTAINER'
                            },
                        ]
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **datasetSummaries** *(list) --*

              A list of "DatasetSummary" objects.

              - *(dict) --*

                A summary of information about a data set.

                - **datasetName** *(string) --*

                  The name of the data set.

                - **status** *(string) --*

                  The status of the data set.

                - **creationTime** *(datetime) --*

                  The time the data set was created.

                - **lastUpdateTime** *(datetime) --*

                  The last time the data set was updated.

                - **triggers** *(list) --*

                  A list of triggers. A trigger causes data set content to be populated at a specified time
                  interval or when another data set is populated. The list of triggers can be empty or
                  contain up to five DataSetTrigger objects

                  - *(dict) --*

                    The "DatasetTrigger" that specifies when the data set is automatically updated.

                    - **schedule** *(dict) --*

                      The "Schedule" when the trigger is initiated.

                      - **expression** *(string) --*

                        The expression that defines when to trigger an update. For more information, see
                        `Schedule Expressions for Rules
                        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__
                        in the Amazon CloudWatch Events User Guide.

                    - **dataset** *(dict) --*

                      The data set whose content creation triggers the creation of this data set's contents.

                      - **name** *(string) --*

                        The name of the data set whose content generation triggers the new data set content
                        generation.

                - **actions** *(list) --*

                  A list of "DataActionSummary" objects.

                  - *(dict) --*

                    Information about the action which automatically creates the data set's contents.

                    - **actionName** *(string) --*

                      The name of the action which automatically creates the data set's contents.

                    - **actionType** *(string) --*

                      The type of action by which the data set's contents are automatically created.

            - **nextToken** *(string) --*

              The token to retrieve the next set of results, or ``null`` if there are no more results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_datastores(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListDatastoresResponseTypeDef:
        """
        Retrieves a list of data stores.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatastores>`_

        **Request Syntax**
        ::

          response = client.list_datastores(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken:

          The token for the next set of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in this request.

          The default value is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'datastoreSummaries': [
                    {
                        'datastoreName': 'string',
                        'datastoreStorage': {
                            'serviceManagedS3': {},
                            'customerManagedS3': {
                                'bucket': 'string',
                                'keyPrefix': 'string',
                                'roleArn': 'string'
                            }
                        },
                        'status': 'CREATING'|'ACTIVE'|'DELETING',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **datastoreSummaries** *(list) --*

              A list of "DatastoreSummary" objects.

              - *(dict) --*

                A summary of information about a data store.

                - **datastoreName** *(string) --*

                  The name of the data store.

                - **datastoreStorage** *(dict) --*

                  Where data store data is stored.

                  - **serviceManagedS3** *(dict) --*

                    Used to store data store data in an S3 bucket managed by the AWS IoT Analytics service.

                  - **customerManagedS3** *(dict) --*

                    Used to store data store data in an S3 bucket that you manage.

                    - **bucket** *(string) --*

                      The name of the Amazon S3 bucket in which data store data is stored.

                    - **keyPrefix** *(string) --*

                      [Optional] The prefix used to create the keys of the data store data objects. Each
                      object in an Amazon S3 bucket has a key that is its unique identifier within the
                      bucket (each object in a bucket has exactly one key). The prefix must end with a '/'.

                    - **roleArn** *(string) --*

                      The ARN of the role which grants AWS IoT Analytics permission to interact with your
                      Amazon S3 resources.

                - **status** *(string) --*

                  The status of the data store.

                - **creationTime** *(datetime) --*

                  When the data store was created.

                - **lastUpdateTime** *(datetime) --*

                  The last time the data store was updated.

            - **nextToken** *(string) --*

              The token to retrieve the next set of results, or ``null`` if there are no more results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_pipelines(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListPipelinesResponseTypeDef:
        """
        Retrieves a list of pipelines.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListPipelines>`_

        **Request Syntax**
        ::

          response = client.list_pipelines(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken:

          The token for the next set of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in this request.

          The default value is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pipelineSummaries': [
                    {
                        'pipelineName': 'string',
                        'reprocessingSummaries': [
                            {
                                'id': 'string',
                                'status': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                                'creationTime': datetime(2015, 1, 1)
                            },
                        ],
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **pipelineSummaries** *(list) --*

              A list of "PipelineSummary" objects.

              - *(dict) --*

                A summary of information about a pipeline.

                - **pipelineName** *(string) --*

                  The name of the pipeline.

                - **reprocessingSummaries** *(list) --*

                  A summary of information about the pipeline reprocessing.

                  - *(dict) --*

                    Information about pipeline reprocessing.

                    - **id** *(string) --*

                      The 'reprocessingId' returned by "StartPipelineReprocessing".

                    - **status** *(string) --*

                      The status of the pipeline reprocessing.

                    - **creationTime** *(datetime) --*

                      The time the pipeline reprocessing was created.

                - **creationTime** *(datetime) --*

                  When the pipeline was created.

                - **lastUpdateTime** *(datetime) --*

                  When the pipeline was last updated.

            - **nextToken** *(string) --*

              The token to retrieve the next set of results, or ``null`` if there are no more results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) which you have assigned to the resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The ARN of the resource whose tags you want to list.

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

              The tags (metadata) which you have assigned to the resource.

              - *(dict) --*

                A set of key/value pairs which are used to manage the resource.

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
        Sets or updates the AWS IoT Analytics logging options.

        Note that if you update the value of any ``loggingOptions`` field, it takes up to one minute for
        the change to take effect. Also, if you change the policy attached to the role you specified in the
        roleArn field (for example, to correct an invalid policy) it takes up to 5 minutes for that change
        to take effect.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/PutLoggingOptions>`_

        **Request Syntax**
        ::

          response = client.put_logging_options(
              loggingOptions={
                  'roleArn': 'string',
                  'level': 'ERROR',
                  'enabled': True|False
              }
          )
        :type loggingOptions: dict
        :param loggingOptions: **[REQUIRED]**

          The new values of the AWS IoT Analytics logging options.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the role that grants permission to AWS IoT Analytics to perform logging.

          - **level** *(string) --* **[REQUIRED]**

            The logging level. Currently, only "ERROR" is supported.

          - **enabled** *(boolean) --* **[REQUIRED]**

            If true, logging is enabled for AWS IoT Analytics.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def run_pipeline_activity(
        self,
        pipelineActivity: ClientRunPipelineActivitypipelineActivityTypeDef,
        payloads: List[bytes],
    ) -> ClientRunPipelineActivityResponseTypeDef:
        """
        Simulates the results of running a pipeline activity on a message payload.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/RunPipelineActivity>`_

        **Request Syntax**
        ::

          response = client.run_pipeline_activity(
              pipelineActivity={
                  'channel': {
                      'name': 'string',
                      'channelName': 'string',
                      'next': 'string'
                  },
                  'lambda': {
                      'name': 'string',
                      'lambdaName': 'string',
                      'batchSize': 123,
                      'next': 'string'
                  },
                  'datastore': {
                      'name': 'string',
                      'datastoreName': 'string'
                  },
                  'addAttributes': {
                      'name': 'string',
                      'attributes': {
                          'string': 'string'
                      },
                      'next': 'string'
                  },
                  'removeAttributes': {
                      'name': 'string',
                      'attributes': [
                          'string',
                      ],
                      'next': 'string'
                  },
                  'selectAttributes': {
                      'name': 'string',
                      'attributes': [
                          'string',
                      ],
                      'next': 'string'
                  },
                  'filter': {
                      'name': 'string',
                      'filter': 'string',
                      'next': 'string'
                  },
                  'math': {
                      'name': 'string',
                      'attribute': 'string',
                      'math': 'string',
                      'next': 'string'
                  },
                  'deviceRegistryEnrich': {
                      'name': 'string',
                      'attribute': 'string',
                      'thingName': 'string',
                      'roleArn': 'string',
                      'next': 'string'
                  },
                  'deviceShadowEnrich': {
                      'name': 'string',
                      'attribute': 'string',
                      'thingName': 'string',
                      'roleArn': 'string',
                      'next': 'string'
                  }
              },
              payloads=[
                  b'bytes',
              ]
          )
        :type pipelineActivity: dict
        :param pipelineActivity: **[REQUIRED]**

          The pipeline activity that is run. This must not be a 'channel' activity or a 'datastore'
          activity because these activities are used in a pipeline only to load the original message and to
          store the (possibly) transformed message. If a 'lambda' activity is specified, only short-running
          Lambda functions (those with a timeout of less than 30 seconds or less) can be used.

          - **channel** *(dict) --*

            Determines the source of the messages to be processed.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'channel' activity.

            - **channelName** *(string) --* **[REQUIRED]**

              The name of the channel from which the messages are processed.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **lambda** *(dict) --*

            Runs a Lambda function to modify the message.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'lambda' activity.

            - **lambdaName** *(string) --* **[REQUIRED]**

              The name of the Lambda function that is run on the message.

            - **batchSize** *(integer) --* **[REQUIRED]**

              The number of messages passed to the Lambda function for processing.

              The AWS Lambda function must be able to process all of these messages within five minutes,
              which is the maximum timeout duration for Lambda functions.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **datastore** *(dict) --*

            Specifies where to store the processed message data.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'datastore' activity.

            - **datastoreName** *(string) --* **[REQUIRED]**

              The name of the data store where processed messages are stored.

          - **addAttributes** *(dict) --*

            Adds other attributes based on existing attributes in the message.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'addAttributes' activity.

            - **attributes** *(dict) --* **[REQUIRED]**

              A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
              attribute.

              .. note::

                The existing attributes remain in the message, so if you want to remove the originals, use
                "RemoveAttributeActivity".

              - *(string) --*

                - *(string) --*

            - **next** *(string) --*

              The next activity in the pipeline.

          - **removeAttributes** *(dict) --*

            Removes attributes from a message.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'removeAttributes' activity.

            - **attributes** *(list) --* **[REQUIRED]**

              A list of 1-50 attributes to remove from the message.

              - *(string) --*

            - **next** *(string) --*

              The next activity in the pipeline.

          - **selectAttributes** *(dict) --*

            Creates a new message using only the specified attributes from the original message.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'selectAttributes' activity.

            - **attributes** *(list) --* **[REQUIRED]**

              A list of the attributes to select from the message.

              - *(string) --*

            - **next** *(string) --*

              The next activity in the pipeline.

          - **filter** *(dict) --*

            Filters a message based on its attributes.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'filter' activity.

            - **filter** *(string) --* **[REQUIRED]**

              An expression that looks like a SQL WHERE clause that must return a Boolean value.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **math** *(dict) --*

            Computes an arithmetic expression using the message's attributes and adds it to the message.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'math' activity.

            - **attribute** *(string) --* **[REQUIRED]**

              The name of the attribute that contains the result of the math operation.

            - **math** *(string) --* **[REQUIRED]**

              An expression that uses one or more existing attributes and must return an integer value.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **deviceRegistryEnrich** *(dict) --*

            Adds data from the AWS IoT device registry to your message.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'deviceRegistryEnrich' activity.

            - **attribute** *(string) --* **[REQUIRED]**

              The name of the attribute that is added to the message.

            - **thingName** *(string) --* **[REQUIRED]**

              The name of the IoT device whose registry information is added to the message.

            - **roleArn** *(string) --* **[REQUIRED]**

              The ARN of the role that allows access to the device's registry information.

            - **next** *(string) --*

              The next activity in the pipeline.

          - **deviceShadowEnrich** *(dict) --*

            Adds information from the AWS IoT Device Shadows service to a message.

            - **name** *(string) --* **[REQUIRED]**

              The name of the 'deviceShadowEnrich' activity.

            - **attribute** *(string) --* **[REQUIRED]**

              The name of the attribute that is added to the message.

            - **thingName** *(string) --* **[REQUIRED]**

              The name of the IoT device whose shadow information is added to the message.

            - **roleArn** *(string) --* **[REQUIRED]**

              The ARN of the role that allows access to the device's shadow.

            - **next** *(string) --*

              The next activity in the pipeline.

        :type payloads: list
        :param payloads: **[REQUIRED]**

          The sample message payloads on which the pipeline activity is run.

          - *(bytes) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'payloads': [
                    b'bytes',
                ],
                'logResult': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **payloads** *(list) --*

              The enriched or transformed sample message payloads as base64-encoded strings. (The results
              of running the pipeline activity on each input sample message payload, encoded in base64.)

              - *(bytes) --*

            - **logResult** *(string) --*

              In case the pipeline activity fails, the log message that is generated.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def sample_channel_data(
        self,
        channelName: str,
        maxMessages: int = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> ClientSampleChannelDataResponseTypeDef:
        """
        Retrieves a sample of messages from the specified channel ingested during the specified timeframe.
        Up to 10 messages can be retrieved.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/SampleChannelData>`_

        **Request Syntax**
        ::

          response = client.sample_channel_data(
              channelName='string',
              maxMessages=123,
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1)
          )
        :type channelName: string
        :param channelName: **[REQUIRED]**

          The name of the channel whose message samples are retrieved.

        :type maxMessages: integer
        :param maxMessages:

          The number of sample messages to be retrieved. The limit is 10, the default is also 10.

        :type startTime: datetime
        :param startTime:

          The start of the time window from which sample messages are retrieved.

        :type endTime: datetime
        :param endTime:

          The end of the time window from which sample messages are retrieved.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'payloads': [
                    b'bytes',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **payloads** *(list) --*

              The list of message samples. Each sample message is returned as a base64-encoded string.

              - *(bytes) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_pipeline_reprocessing(
        self, pipelineName: str, startTime: datetime = None, endTime: datetime = None
    ) -> ClientStartPipelineReprocessingResponseTypeDef:
        """
        Starts the reprocessing of raw message data through the pipeline.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/StartPipelineReprocessing>`_

        **Request Syntax**
        ::

          response = client.start_pipeline_reprocessing(
              pipelineName='string',
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1)
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**

          The name of the pipeline on which to start reprocessing.

        :type startTime: datetime
        :param startTime:

          The start time (inclusive) of raw message data that is reprocessed.

        :type endTime: datetime
        :param endTime:

          The end time (exclusive) of raw message data that is reprocessed.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'reprocessingId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **reprocessingId** *(string) --*

              The ID of the pipeline reprocessing activity that was started.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourcetagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a
        resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/TagResource>`_

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

          The ARN of the resource whose tags you want to modify.

        :type tags: list
        :param tags: **[REQUIRED]**

          The new or modified tags for the resource.

          - *(dict) --*

            A set of key/value pairs which are used to manage the resource.

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
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UntagResource>`_

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

          The ARN of the resource whose tags you want to remove.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          The keys of those tags which you want to remove.

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
    def update_channel(
        self,
        channelName: str,
        channelStorage: ClientUpdateChannelchannelStorageTypeDef = None,
        retentionPeriod: ClientUpdateChannelretentionPeriodTypeDef = None,
    ) -> None:
        """
        Updates the settings of a channel.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdateChannel>`_

        **Request Syntax**
        ::

          response = client.update_channel(
              channelName='string',
              channelStorage={
                  'serviceManagedS3': {}
                  ,
                  'customerManagedS3': {
                      'bucket': 'string',
                      'keyPrefix': 'string',
                      'roleArn': 'string'
                  }
              },
              retentionPeriod={
                  'unlimited': True|False,
                  'numberOfDays': 123
              }
          )
        :type channelName: string
        :param channelName: **[REQUIRED]**

          The name of the channel to be updated.

        :type channelStorage: dict
        :param channelStorage:

          Where channel data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
          storage. If not specified, the default is "serviceManagedS3". This cannot be changed after
          creation of the channel.

          - **serviceManagedS3** *(dict) --*

            Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service. The
            choice of service-managed or customer-managed S3 storage cannot be changed after creation of
            the channel.

          - **customerManagedS3** *(dict) --*

            Use this to store channel data in an S3 bucket that you manage. If customer managed storage is
            selected, the "retentionPeriod" parameter is ignored. The choice of service-managed or
            customer-managed S3 storage cannot be changed after creation of the channel.

            - **bucket** *(string) --* **[REQUIRED]**

              The name of the Amazon S3 bucket in which channel data is stored.

            - **keyPrefix** *(string) --*

              [Optional] The prefix used to create the keys of the channel data objects. Each object in an
              Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in a
              bucket has exactly one key). The prefix must end with a '/'.

            - **roleArn** *(string) --* **[REQUIRED]**

              The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
              resources.

        :type retentionPeriod: dict
        :param retentionPeriod:

          How long, in days, message data is kept for the channel. The retention period cannot be updated
          if the channel's S3 storage is customer-managed.

          - **unlimited** *(boolean) --*

            If true, message data is kept indefinitely.

          - **numberOfDays** *(integer) --*

            The number of days that message data is kept. The "unlimited" parameter must be false.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_dataset(
        self,
        datasetName: str,
        actions: List[ClientUpdateDatasetactionsTypeDef],
        triggers: List[ClientUpdateDatasettriggersTypeDef] = None,
        contentDeliveryRules: List[
            ClientUpdateDatasetcontentDeliveryRulesTypeDef
        ] = None,
        retentionPeriod: ClientUpdateDatasetretentionPeriodTypeDef = None,
        versioningConfiguration: Dict = None,
    ) -> None:
        """
        Updates the settings of a data set.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdateDataset>`_

        **Request Syntax**
        ::

          response = client.update_dataset(
              datasetName='string',
              actions=[
                  {
                      'actionName': 'string',
                      'queryAction': {
                          'sqlQuery': 'string',
                          'filters': [
                              {
                                  'deltaTime': {
                                      'offsetSeconds': 123,
                                      'timeExpression': 'string'
                                  }
                              },
                          ]
                      },
                      'containerAction': {
                          'image': 'string',
                          'executionRoleArn': 'string',
                          'resourceConfiguration': {
                              'computeType': 'ACU_1'|'ACU_2',
                              'volumeSizeInGB': 123
                          },
                          'variables': [
                              {
                                  'name': 'string',
                                  'stringValue': 'string',
                                  'doubleValue': 123.0,
                                  'datasetContentVersionValue': {
                                      'datasetName': 'string'
                                  },
                                  'outputFileUriValue': {
                                      'fileName': 'string'
                                  }
                              },
                          ]
                      }
                  },
              ],
              triggers=[
                  {
                      'schedule': {
                          'expression': 'string'
                      },
                      'dataset': {
                          'name': 'string'
                      }
                  },
              ],
              contentDeliveryRules=[
                  {
                      'entryName': 'string',
                      'destination': {
                          'iotEventsDestinationConfiguration': {
                              'inputName': 'string',
                              'roleArn': 'string'
                          },
                          's3DestinationConfiguration': {
                              'bucket': 'string',
                              'key': 'string',
                              'glueConfiguration': {
                                  'tableName': 'string',
                                  'databaseName': 'string'
                              },
                              'roleArn': 'string'
                          }
                      }
                  },
              ],
              retentionPeriod={
                  'unlimited': True|False,
                  'numberOfDays': 123
              },
              versioningConfiguration={
                  'unlimited': True|False,
                  'maxVersions': 123
              }
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]**

          The name of the data set to update.

        :type actions: list
        :param actions: **[REQUIRED]**

          A list of "DatasetAction" objects.

          - *(dict) --*

            A "DatasetAction" object that specifies how data set contents are automatically created.

            - **actionName** *(string) --*

              The name of the data set action by which data set contents are automatically created.

            - **queryAction** *(dict) --*

              An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set
              contents.

              - **sqlQuery** *(string) --* **[REQUIRED]**

                A SQL query string.

              - **filters** *(list) --*

                Pre-filters applied to message data.

                - *(dict) --*

                  Information which is used to filter message data, to segregate it according to the time
                  frame in which it arrives.

                  - **deltaTime** *(dict) --*

                    Used to limit data to that which has arrived since the last execution of the action.

                    - **offsetSeconds** *(integer) --* **[REQUIRED]**

                      The number of seconds of estimated "in flight" lag time of message data. When you
                      create data set contents using message data from a specified time frame, some message
                      data may still be "in flight" when processing begins, and so will not arrive in time
                      to be processed. Use this field to make allowances for the "in flight" time of your
                      message data, so that data not processed from a previous time frame will be included
                      with the next time frame. Without this, missed message data would be excluded from
                      processing during the next time frame as well, because its timestamp places it within
                      the previous time frame.

                    - **timeExpression** *(string) --* **[REQUIRED]**

                      An expression by which the time of the message data may be determined. This may be
                      the name of a timestamp field, or a SQL expression which is used to derive the time
                      the message data was generated.

            - **containerAction** *(dict) --*

              Information which allows the system to run a containerized application in order to create the
              data set contents. The application must be in a Docker container along with any needed
              support libraries.

              - **image** *(string) --* **[REQUIRED]**

                The ARN of the Docker container stored in your account. The Docker container contains an
                application and needed support libraries and is used to generate data set contents.

              - **executionRoleArn** *(string) --* **[REQUIRED]**

                The ARN of the role which gives permission to the system to access needed resources in
                order to run the "containerAction". This includes, at minimum, permission to retrieve the
                data set contents which are the input to the containerized application.

              - **resourceConfiguration** *(dict) --* **[REQUIRED]**

                Configuration of the resource which executes the "containerAction".

                - **computeType** *(string) --* **[REQUIRED]**

                  The type of the compute resource used to execute the "containerAction". Possible values
                  are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).

                - **volumeSizeInGB** *(integer) --* **[REQUIRED]**

                  The size (in GB) of the persistent storage available to the resource instance used to
                  execute the "containerAction" (min: 1, max: 50).

              - **variables** *(list) --*

                The values of variables used within the context of the execution of the containerized
                application (basically, parameters passed to the application). Each variable must have a
                name and a value given by one of "stringValue", "datasetContentVersionValue", or
                "outputFileUriValue".

                - *(dict) --*

                  An instance of a variable to be passed to the "containerAction" execution. Each variable
                  must have a name and a value given by one of "stringValue", "datasetContentVersionValue",
                  or "outputFileUriValue".

                  - **name** *(string) --* **[REQUIRED]**

                    The name of the variable.

                  - **stringValue** *(string) --*

                    The value of the variable as a string.

                  - **doubleValue** *(float) --*

                    The value of the variable as a double (numeric).

                  - **datasetContentVersionValue** *(dict) --*

                    The value of the variable as a structure that specifies a data set content version.

                    - **datasetName** *(string) --* **[REQUIRED]**

                      The name of the data set whose latest contents are used as input to the notebook or
                      application.

                  - **outputFileUriValue** *(dict) --*

                    The value of the variable as a structure that specifies an output file URI.

                    - **fileName** *(string) --* **[REQUIRED]**

                      The URI of the location where data set contents are stored, usually the URI of a file
                      in an S3 bucket.

        :type triggers: list
        :param triggers:

          A list of "DatasetTrigger" objects. The list can be empty or can contain up to five
          **DataSetTrigger** objects.

          - *(dict) --*

            The "DatasetTrigger" that specifies when the data set is automatically updated.

            - **schedule** *(dict) --*

              The "Schedule" when the trigger is initiated.

              - **expression** *(string) --*

                The expression that defines when to trigger an update. For more information, see `Schedule
                Expressions for Rules
                <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the
                Amazon CloudWatch Events User Guide.

            - **dataset** *(dict) --*

              The data set whose content creation triggers the creation of this data set's contents.

              - **name** *(string) --* **[REQUIRED]**

                The name of the data set whose content generation triggers the new data set content
                generation.

        :type contentDeliveryRules: list
        :param contentDeliveryRules:

          When data set contents are created they are delivered to destinations specified here.

          - *(dict) --*

            When data set contents are created they are delivered to destination specified here.

            - **entryName** *(string) --*

              The name of the data set content delivery rules entry.

            - **destination** *(dict) --* **[REQUIRED]**

              The destination to which data set contents are delivered.

              - **iotEventsDestinationConfiguration** *(dict) --*

                Configuration information for delivery of data set contents to AWS IoT Events.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input to which data set contents are delivered.

                - **roleArn** *(string) --* **[REQUIRED]**

                  The ARN of the role which grants AWS IoT Analytics permission to deliver data set
                  contents to an AWS IoT Events input.

              - **s3DestinationConfiguration** *(dict) --*

                Configuration information for delivery of data set contents to Amazon S3.

                - **bucket** *(string) --* **[REQUIRED]**

                  The name of the Amazon S3 bucket to which data set contents are delivered.

                - **key** *(string) --* **[REQUIRED]**

                  The key of the data set contents object. Each object in an Amazon S3 bucket has a key
                  that is its unique identifier within the bucket (each object in a bucket has exactly one
                  key). To produce a unique key, you can use "!{iotanalytics:scheduledTime}" to insert the
                  time of the scheduled SQL query run, or "!{iotanalytics:versioned} to insert a unique
                  hash identifying the data set, for example:
                  "/DataSet/!{iotanalytics:scheduledTime}/!{iotanalytics:versioned}.csv".

                - **glueConfiguration** *(dict) --*

                  Configuration information for coordination with the AWS Glue ETL (extract, transform and
                  load) service.

                  - **tableName** *(string) --* **[REQUIRED]**

                    The name of the table in your AWS Glue Data Catalog which is used to perform the ETL
                    (extract, transform and load) operations. (An AWS Glue Data Catalog table contains
                    partitioned data and descriptions of data sources and targets.)

                  - **databaseName** *(string) --* **[REQUIRED]**

                    The name of the database in your AWS Glue Data Catalog in which the table is located.
                    (An AWS Glue Data Catalog database contains Glue Data tables.)

                - **roleArn** *(string) --* **[REQUIRED]**

                  The ARN of the role which grants AWS IoT Analytics permission to interact with your
                  Amazon S3 and AWS Glue resources.

        :type retentionPeriod: dict
        :param retentionPeriod:

          How long, in days, data set contents are kept for the data set.

          - **unlimited** *(boolean) --*

            If true, message data is kept indefinitely.

          - **numberOfDays** *(integer) --*

            The number of days that message data is kept. The "unlimited" parameter must be false.

        :type versioningConfiguration: dict
        :param versioningConfiguration:

          [Optional] How many versions of data set contents are kept. If not specified or set to null, only
          the latest version plus the latest succeeded version (if they are different) are kept for the
          time period specified by the "retentionPeriod" parameter. (For more information, see
          https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)
        https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)

          - **unlimited** *(boolean) --*

            If true, unlimited versions of data set contents will be kept.

          - **maxVersions** *(integer) --*

            How many versions of data set contents will be kept. The "unlimited" parameter must be false.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_datastore(
        self,
        datastoreName: str,
        retentionPeriod: ClientUpdateDatastoreretentionPeriodTypeDef = None,
        datastoreStorage: ClientUpdateDatastoredatastoreStorageTypeDef = None,
    ) -> None:
        """
        Updates the settings of a data store.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdateDatastore>`_

        **Request Syntax**
        ::

          response = client.update_datastore(
              datastoreName='string',
              retentionPeriod={
                  'unlimited': True|False,
                  'numberOfDays': 123
              },
              datastoreStorage={
                  'serviceManagedS3': {}
                  ,
                  'customerManagedS3': {
                      'bucket': 'string',
                      'keyPrefix': 'string',
                      'roleArn': 'string'
                  }
              }
          )
        :type datastoreName: string
        :param datastoreName: **[REQUIRED]**

          The name of the data store to be updated.

        :type retentionPeriod: dict
        :param retentionPeriod:

          How long, in days, message data is kept for the data store. The retention period cannot be
          updated if the data store's S3 storage is customer-managed.

          - **unlimited** *(boolean) --*

            If true, message data is kept indefinitely.

          - **numberOfDays** *(integer) --*

            The number of days that message data is kept. The "unlimited" parameter must be false.

        :type datastoreStorage: dict
        :param datastoreStorage:

          Where data store data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
          storage. If not specified, the default is "serviceManagedS3". This cannot be changed after the
          data store is created.

          - **serviceManagedS3** *(dict) --*

            Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics service. The
            choice of service-managed or customer-managed S3 storage cannot be changed after creation of
            the data store.

          - **customerManagedS3** *(dict) --*

            Use this to store data store data in an S3 bucket that you manage. When customer managed
            storage is selected, the "retentionPeriod" parameter is ignored. The choice of service-managed
            or customer-managed S3 storage cannot be changed after creation of the data store.

            - **bucket** *(string) --* **[REQUIRED]**

              The name of the Amazon S3 bucket in which data store data is stored.

            - **keyPrefix** *(string) --*

              [Optional] The prefix used to create the keys of the data store data objects. Each object in
              an Amazon S3 bucket has a key that is its unique identifier within the bucket (each object in
              a bucket has exactly one key). The prefix must end with a '/'.

            - **roleArn** *(string) --* **[REQUIRED]**

              The ARN of the role which grants AWS IoT Analytics permission to interact with your Amazon S3
              resources.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pipeline(
        self,
        pipelineName: str,
        pipelineActivities: List[ClientUpdatePipelinepipelineActivitiesTypeDef],
    ) -> None:
        """
        Updates the settings of a pipeline. You must specify both a ``channel`` and a ``datastore``
        activity and, optionally, as many as 23 additional activities in the ``pipelineActivities`` array.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdatePipeline>`_

        **Request Syntax**
        ::

          response = client.update_pipeline(
              pipelineName='string',
              pipelineActivities=[
                  {
                      'channel': {
                          'name': 'string',
                          'channelName': 'string',
                          'next': 'string'
                      },
                      'lambda': {
                          'name': 'string',
                          'lambdaName': 'string',
                          'batchSize': 123,
                          'next': 'string'
                      },
                      'datastore': {
                          'name': 'string',
                          'datastoreName': 'string'
                      },
                      'addAttributes': {
                          'name': 'string',
                          'attributes': {
                              'string': 'string'
                          },
                          'next': 'string'
                      },
                      'removeAttributes': {
                          'name': 'string',
                          'attributes': [
                              'string',
                          ],
                          'next': 'string'
                      },
                      'selectAttributes': {
                          'name': 'string',
                          'attributes': [
                              'string',
                          ],
                          'next': 'string'
                      },
                      'filter': {
                          'name': 'string',
                          'filter': 'string',
                          'next': 'string'
                      },
                      'math': {
                          'name': 'string',
                          'attribute': 'string',
                          'math': 'string',
                          'next': 'string'
                      },
                      'deviceRegistryEnrich': {
                          'name': 'string',
                          'attribute': 'string',
                          'thingName': 'string',
                          'roleArn': 'string',
                          'next': 'string'
                      },
                      'deviceShadowEnrich': {
                          'name': 'string',
                          'attribute': 'string',
                          'thingName': 'string',
                          'roleArn': 'string',
                          'next': 'string'
                      }
                  },
              ]
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**

          The name of the pipeline to update.

        :type pipelineActivities: list
        :param pipelineActivities: **[REQUIRED]**

          A list of "PipelineActivity" objects. Activities perform transformations on your messages, such
          as removing, renaming or adding message attributes; filtering messages based on attribute values;
          invoking your Lambda functions on messages for advanced processing; or performing mathematical
          transformations to normalize device data.

          The list can be 2-25 **PipelineActivity** objects and must contain both a ``channel`` and a
          ``datastore`` activity. Each entry in the list must contain only one activity, for example:

           ``pipelineActivities = [ { "channel": { ... } }, { "lambda": { ... } }, ... ]``

          - *(dict) --*

            An activity that performs a transformation on a message.

            - **channel** *(dict) --*

              Determines the source of the messages to be processed.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'channel' activity.

              - **channelName** *(string) --* **[REQUIRED]**

                The name of the channel from which the messages are processed.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **lambda** *(dict) --*

              Runs a Lambda function to modify the message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'lambda' activity.

              - **lambdaName** *(string) --* **[REQUIRED]**

                The name of the Lambda function that is run on the message.

              - **batchSize** *(integer) --* **[REQUIRED]**

                The number of messages passed to the Lambda function for processing.

                The AWS Lambda function must be able to process all of these messages within five minutes,
                which is the maximum timeout duration for Lambda functions.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **datastore** *(dict) --*

              Specifies where to store the processed message data.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'datastore' activity.

              - **datastoreName** *(string) --* **[REQUIRED]**

                The name of the data store where processed messages are stored.

            - **addAttributes** *(dict) --*

              Adds other attributes based on existing attributes in the message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'addAttributes' activity.

              - **attributes** *(dict) --* **[REQUIRED]**

                A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new
                attribute.

                .. note::

                  The existing attributes remain in the message, so if you want to remove the originals,
                  use "RemoveAttributeActivity".

                - *(string) --*

                  - *(string) --*

              - **next** *(string) --*

                The next activity in the pipeline.

            - **removeAttributes** *(dict) --*

              Removes attributes from a message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'removeAttributes' activity.

              - **attributes** *(list) --* **[REQUIRED]**

                A list of 1-50 attributes to remove from the message.

                - *(string) --*

              - **next** *(string) --*

                The next activity in the pipeline.

            - **selectAttributes** *(dict) --*

              Creates a new message using only the specified attributes from the original message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'selectAttributes' activity.

              - **attributes** *(list) --* **[REQUIRED]**

                A list of the attributes to select from the message.

                - *(string) --*

              - **next** *(string) --*

                The next activity in the pipeline.

            - **filter** *(dict) --*

              Filters a message based on its attributes.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'filter' activity.

              - **filter** *(string) --* **[REQUIRED]**

                An expression that looks like a SQL WHERE clause that must return a Boolean value.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **math** *(dict) --*

              Computes an arithmetic expression using the message's attributes and adds it to the message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'math' activity.

              - **attribute** *(string) --* **[REQUIRED]**

                The name of the attribute that contains the result of the math operation.

              - **math** *(string) --* **[REQUIRED]**

                An expression that uses one or more existing attributes and must return an integer value.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **deviceRegistryEnrich** *(dict) --*

              Adds data from the AWS IoT device registry to your message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'deviceRegistryEnrich' activity.

              - **attribute** *(string) --* **[REQUIRED]**

                The name of the attribute that is added to the message.

              - **thingName** *(string) --* **[REQUIRED]**

                The name of the IoT device whose registry information is added to the message.

              - **roleArn** *(string) --* **[REQUIRED]**

                The ARN of the role that allows access to the device's registry information.

              - **next** *(string) --*

                The next activity in the pipeline.

            - **deviceShadowEnrich** *(dict) --*

              Adds information from the AWS IoT Device Shadows service to a message.

              - **name** *(string) --* **[REQUIRED]**

                The name of the 'deviceShadowEnrich' activity.

              - **attribute** *(string) --* **[REQUIRED]**

                The name of the attribute that is added to the message.

              - **thingName** *(string) --* **[REQUIRED]**

                The name of the IoT device whose shadow information is added to the message.

              - **roleArn** *(string) --* **[REQUIRED]**

                The ARN of the role that allows access to the device's shadow.

              - **next** *(string) --*

                The next activity in the pipeline.

        :returns: None
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_channels"]
    ) -> paginator_scope.ListChannelsPaginator:
        """
        Get Paginator for `list_channels` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dataset_contents"]
    ) -> paginator_scope.ListDatasetContentsPaginator:
        """
        Get Paginator for `list_dataset_contents` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_datasets"]
    ) -> paginator_scope.ListDatasetsPaginator:
        """
        Get Paginator for `list_datasets` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_datastores"]
    ) -> paginator_scope.ListDatastoresPaginator:
        """
        Get Paginator for `list_datastores` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_pipelines"]
    ) -> paginator_scope.ListPipelinesPaginator:
        """
        Get Paginator for `list_pipelines` operation.
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
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
