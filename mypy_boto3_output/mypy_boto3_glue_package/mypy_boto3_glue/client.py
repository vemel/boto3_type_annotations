"Main interface for glue Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_glue.client as client_scope

# pylint: disable=import-self
import mypy_boto3_glue.paginator as paginator_scope
from mypy_boto3_glue.type_defs import (
    ClientBatchCreatePartitionPartitionInputListTypeDef,
    ClientBatchCreatePartitionResponseTypeDef,
    ClientBatchDeleteConnectionResponseTypeDef,
    ClientBatchDeletePartitionPartitionsToDeleteTypeDef,
    ClientBatchDeletePartitionResponseTypeDef,
    ClientBatchDeleteTableResponseTypeDef,
    ClientBatchDeleteTableVersionResponseTypeDef,
    ClientBatchGetCrawlersResponseTypeDef,
    ClientBatchGetDevEndpointsResponseTypeDef,
    ClientBatchGetJobsResponseTypeDef,
    ClientBatchGetPartitionPartitionsToGetTypeDef,
    ClientBatchGetPartitionResponseTypeDef,
    ClientBatchGetTriggersResponseTypeDef,
    ClientBatchGetWorkflowsResponseTypeDef,
    ClientBatchStopJobRunResponseTypeDef,
    ClientCancelMlTaskRunResponseTypeDef,
    ClientCreateClassifierCsvClassifierTypeDef,
    ClientCreateClassifierGrokClassifierTypeDef,
    ClientCreateClassifierJsonClassifierTypeDef,
    ClientCreateClassifierXMLClassifierTypeDef,
    ClientCreateConnectionConnectionInputTypeDef,
    ClientCreateCrawlerSchemaChangePolicyTypeDef,
    ClientCreateCrawlerTargetsTypeDef,
    ClientCreateDatabaseDatabaseInputTypeDef,
    ClientCreateDevEndpointResponseTypeDef,
    ClientCreateJobCommandTypeDef,
    ClientCreateJobConnectionsTypeDef,
    ClientCreateJobExecutionPropertyTypeDef,
    ClientCreateJobNotificationPropertyTypeDef,
    ClientCreateJobResponseTypeDef,
    ClientCreateMlTransformInputRecordTablesTypeDef,
    ClientCreateMlTransformParametersTypeDef,
    ClientCreateMlTransformResponseTypeDef,
    ClientCreatePartitionPartitionInputTypeDef,
    ClientCreateScriptDagEdgesTypeDef,
    ClientCreateScriptDagNodesTypeDef,
    ClientCreateScriptResponseTypeDef,
    ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef,
    ClientCreateSecurityConfigurationResponseTypeDef,
    ClientCreateTableTableInputTypeDef,
    ClientCreateTriggerActionsTypeDef,
    ClientCreateTriggerPredicateTypeDef,
    ClientCreateTriggerResponseTypeDef,
    ClientCreateUserDefinedFunctionFunctionInputTypeDef,
    ClientCreateWorkflowResponseTypeDef,
    ClientDeleteJobResponseTypeDef,
    ClientDeleteMlTransformResponseTypeDef,
    ClientDeleteTriggerResponseTypeDef,
    ClientDeleteWorkflowResponseTypeDef,
    ClientGetCatalogImportStatusResponseTypeDef,
    ClientGetClassifierResponseTypeDef,
    ClientGetClassifiersResponseTypeDef,
    ClientGetConnectionResponseTypeDef,
    ClientGetConnectionsFilterTypeDef,
    ClientGetConnectionsResponseTypeDef,
    ClientGetCrawlerMetricsResponseTypeDef,
    ClientGetCrawlerResponseTypeDef,
    ClientGetCrawlersResponseTypeDef,
    ClientGetDataCatalogEncryptionSettingsResponseTypeDef,
    ClientGetDatabaseResponseTypeDef,
    ClientGetDatabasesResponseTypeDef,
    ClientGetDataflowGraphResponseTypeDef,
    ClientGetDevEndpointResponseTypeDef,
    ClientGetDevEndpointsResponseTypeDef,
    ClientGetJobBookmarkResponseTypeDef,
    ClientGetJobResponseTypeDef,
    ClientGetJobRunResponseTypeDef,
    ClientGetJobRunsResponseTypeDef,
    ClientGetJobsResponseTypeDef,
    ClientGetMappingLocationTypeDef,
    ClientGetMappingResponseTypeDef,
    ClientGetMappingSinksTypeDef,
    ClientGetMappingSourceTypeDef,
    ClientGetMlTaskRunResponseTypeDef,
    ClientGetMlTaskRunsFilterTypeDef,
    ClientGetMlTaskRunsResponseTypeDef,
    ClientGetMlTaskRunsSortTypeDef,
    ClientGetMlTransformResponseTypeDef,
    ClientGetMlTransformsFilterTypeDef,
    ClientGetMlTransformsResponseTypeDef,
    ClientGetMlTransformsSortTypeDef,
    ClientGetPartitionResponseTypeDef,
    ClientGetPartitionsResponseTypeDef,
    ClientGetPartitionsSegmentTypeDef,
    ClientGetPlanLocationTypeDef,
    ClientGetPlanMappingTypeDef,
    ClientGetPlanResponseTypeDef,
    ClientGetPlanSinksTypeDef,
    ClientGetPlanSourceTypeDef,
    ClientGetResourcePolicyResponseTypeDef,
    ClientGetSecurityConfigurationResponseTypeDef,
    ClientGetSecurityConfigurationsResponseTypeDef,
    ClientGetTableResponseTypeDef,
    ClientGetTableVersionResponseTypeDef,
    ClientGetTableVersionsResponseTypeDef,
    ClientGetTablesResponseTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientGetTriggerResponseTypeDef,
    ClientGetTriggersResponseTypeDef,
    ClientGetUserDefinedFunctionResponseTypeDef,
    ClientGetUserDefinedFunctionsResponseTypeDef,
    ClientGetWorkflowResponseTypeDef,
    ClientGetWorkflowRunPropertiesResponseTypeDef,
    ClientGetWorkflowRunResponseTypeDef,
    ClientGetWorkflowRunsResponseTypeDef,
    ClientListCrawlersResponseTypeDef,
    ClientListDevEndpointsResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListTriggersResponseTypeDef,
    ClientListWorkflowsResponseTypeDef,
    ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef,
    ClientPutResourcePolicyResponseTypeDef,
    ClientResetJobBookmarkResponseTypeDef,
    ClientSearchTablesFiltersTypeDef,
    ClientSearchTablesResponseTypeDef,
    ClientSearchTablesSortCriteriaTypeDef,
    ClientStartExportLabelsTaskRunResponseTypeDef,
    ClientStartImportLabelsTaskRunResponseTypeDef,
    ClientStartJobRunNotificationPropertyTypeDef,
    ClientStartJobRunResponseTypeDef,
    ClientStartMlEvaluationTaskRunResponseTypeDef,
    ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef,
    ClientStartTriggerResponseTypeDef,
    ClientStartWorkflowRunResponseTypeDef,
    ClientStopTriggerResponseTypeDef,
    ClientUpdateClassifierCsvClassifierTypeDef,
    ClientUpdateClassifierGrokClassifierTypeDef,
    ClientUpdateClassifierJsonClassifierTypeDef,
    ClientUpdateClassifierXMLClassifierTypeDef,
    ClientUpdateConnectionConnectionInputTypeDef,
    ClientUpdateCrawlerSchemaChangePolicyTypeDef,
    ClientUpdateCrawlerTargetsTypeDef,
    ClientUpdateDatabaseDatabaseInputTypeDef,
    ClientUpdateDevEndpointCustomLibrariesTypeDef,
    ClientUpdateJobJobUpdateTypeDef,
    ClientUpdateJobResponseTypeDef,
    ClientUpdateMlTransformParametersTypeDef,
    ClientUpdateMlTransformResponseTypeDef,
    ClientUpdatePartitionPartitionInputTypeDef,
    ClientUpdateTableTableInputTypeDef,
    ClientUpdateTriggerResponseTypeDef,
    ClientUpdateTriggerTriggerUpdateTypeDef,
    ClientUpdateUserDefinedFunctionFunctionInputTypeDef,
    ClientUpdateWorkflowResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInputList: List[ClientBatchCreatePartitionPartitionInputListTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchCreatePartitionResponseTypeDef:
        """
        Creates one or more partitions in a batch operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchCreatePartition>`_

        **Request Syntax**
        ::

          response = client.batch_create_partition(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              PartitionInputList=[
                  {
                      'Values': [
                          'string',
                      ],
                      'LastAccessTime': datetime(2015, 1, 1),
                      'StorageDescriptor': {
                          'Columns': [
                              {
                                  'Name': 'string',
                                  'Type': 'string',
                                  'Comment': 'string',
                                  'Parameters': {
                                      'string': 'string'
                                  }
                              },
                          ],
                          'Location': 'string',
                          'InputFormat': 'string',
                          'OutputFormat': 'string',
                          'Compressed': True|False,
                          'NumberOfBuckets': 123,
                          'SerdeInfo': {
                              'Name': 'string',
                              'SerializationLibrary': 'string',
                              'Parameters': {
                                  'string': 'string'
                              }
                          },
                          'BucketColumns': [
                              'string',
                          ],
                          'SortColumns': [
                              {
                                  'Column': 'string',
                                  'SortOrder': 123
                              },
                          ],
                          'Parameters': {
                              'string': 'string'
                          },
                          'SkewedInfo': {
                              'SkewedColumnNames': [
                                  'string',
                              ],
                              'SkewedColumnValues': [
                                  'string',
                              ],
                              'SkewedColumnValueLocationMaps': {
                                  'string': 'string'
                              }
                          },
                          'StoredAsSubDirectories': True|False
                      },
                      'Parameters': {
                          'string': 'string'
                      },
                      'LastAnalyzedTime': datetime(2015, 1, 1)
                  },
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the catalog in which the partition is to be created. Currently, this should be the AWS
          account ID.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the metadata database in which the partition is to be created.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the metadata table in which the partition is to be created.

        :type PartitionInputList: list
        :param PartitionInputList: **[REQUIRED]**

          A list of ``PartitionInput`` structures that define the partitions to be created.

          - *(dict) --*

            The structure used to create and update a partition.

            - **Values** *(list) --*

              The values of the partition. Although this parameter is not required by the SDK, you must
              specify this parameter for a valid input.

              The values for the keys for the new partition must be passed as an array of String objects
              that must be ordered in the same order as the partition keys appearing in the Amazon S3
              prefix. Otherwise AWS Glue will add the values to the wrong keys.

              - *(string) --*

            - **LastAccessTime** *(datetime) --*

              The last time at which the partition was accessed.

            - **StorageDescriptor** *(dict) --*

              Provides information about the physical location where the partition is stored.

              - **Columns** *(list) --*

                A list of the ``Columns`` in the table.

                - *(dict) --*

                  A column in a ``Table`` .

                  - **Name** *(string) --* **[REQUIRED]**

                    The name of the ``Column`` .

                  - **Type** *(string) --*

                    The data type of the ``Column`` .

                  - **Comment** *(string) --*

                    A free-form text comment.

                  - **Parameters** *(dict) --*

                    These key-value pairs define properties associated with the column.

                    - *(string) --*

                      - *(string) --*

              - **Location** *(string) --*

                The physical location of the table. By default, this takes the form of the warehouse
                location, followed by the database location in the warehouse, followed by the table name.

              - **InputFormat** *(string) --*

                The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                custom format.

              - **OutputFormat** *(string) --*

                The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat``
                , or a custom format.

              - **Compressed** *(boolean) --*

                 ``True`` if the data in the table is compressed, or ``False`` if not.

              - **NumberOfBuckets** *(integer) --*

                Must be specified if the table contains any dimension columns.

              - **SerdeInfo** *(dict) --*

                The serialization/deserialization (SerDe) information.

                - **Name** *(string) --*

                  Name of the SerDe.

                - **SerializationLibrary** *(string) --*

                  Usually the class that implements the SerDe. An example is
                  ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                - **Parameters** *(dict) --*

                  These key-value pairs define initialization parameters for the SerDe.

                  - *(string) --*

                    - *(string) --*

              - **BucketColumns** *(list) --*

                A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

                - *(string) --*

              - **SortColumns** *(list) --*

                A list specifying the sort order of each bucket in the table.

                - *(dict) --*

                  Specifies the sort order of a sorted column.

                  - **Column** *(string) --* **[REQUIRED]**

                    The name of the column.

                  - **SortOrder** *(integer) --* **[REQUIRED]**

                    Indicates that the column is sorted in ascending order (``== 1`` ), or in descending
                    order (``==0`` ).

              - **Parameters** *(dict) --*

                The user-supplied properties in key-value form.

                - *(string) --*

                  - *(string) --*

              - **SkewedInfo** *(dict) --*

                The information about values that appear frequently in a column (skewed values).

                - **SkewedColumnNames** *(list) --*

                  A list of names of columns that contain skewed values.

                  - *(string) --*

                - **SkewedColumnValues** *(list) --*

                  A list of values that appear so frequently as to be considered skewed.

                  - *(string) --*

                - **SkewedColumnValueLocationMaps** *(dict) --*

                  A mapping of skewed values to the columns that contain them.

                  - *(string) --*

                    - *(string) --*

              - **StoredAsSubDirectories** *(boolean) --*

                 ``True`` if the table data is stored in subdirectories, or ``False`` if not.

            - **Parameters** *(dict) --*

              These key-value pairs define partition parameters.

              - *(string) --*

                - *(string) --*

            - **LastAnalyzedTime** *(datetime) --*

              The last time at which column statistics were computed for this partition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Errors': [
                    {
                        'PartitionValues': [
                            'string',
                        ],
                        'ErrorDetail': {
                            'ErrorCode': 'string',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Errors** *(list) --*

              The errors encountered when trying to create the requested partitions.

              - *(dict) --*

                Contains information about a partition error.

                - **PartitionValues** *(list) --*

                  The values that define the partition.

                  - *(string) --*

                - **ErrorDetail** *(dict) --*

                  The details about the partition error.

                  - **ErrorCode** *(string) --*

                    The code associated with this error.

                  - **ErrorMessage** *(string) --*

                    A message describing the error.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_connection(
        self, ConnectionNameList: List[str], CatalogId: str = None
    ) -> ClientBatchDeleteConnectionResponseTypeDef:
        """
        Deletes a list of connection definitions from the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchDeleteConnection>`_

        **Request Syntax**
        ::

          response = client.batch_delete_connection(
              CatalogId='string',
              ConnectionNameList=[
                  'string',
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the connections reside. If none is provided, the AWS account
          ID is used by default.

        :type ConnectionNameList: list
        :param ConnectionNameList: **[REQUIRED]**

          A list of names of the connections to delete.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Succeeded': [
                    'string',
                ],
                'Errors': {
                    'string': {
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Succeeded** *(list) --*

              A list of names of the connection definitions that were successfully deleted.

              - *(string) --*

            - **Errors** *(dict) --*

              A map of the names of connections that were not successfully deleted to error details.

              - *(string) --*

                - *(dict) --*

                  Contains details about an error.

                  - **ErrorCode** *(string) --*

                    The code associated with this error.

                  - **ErrorMessage** *(string) --*

                    A message describing the error.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToDelete: List[ClientBatchDeletePartitionPartitionsToDeleteTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchDeletePartitionResponseTypeDef:
        """
        Deletes one or more partitions in a batch operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchDeletePartition>`_

        **Request Syntax**
        ::

          response = client.batch_delete_partition(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              PartitionsToDelete=[
                  {
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the
          AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database in which the table in question resides.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the table that contains the partitions to be deleted.

        :type PartitionsToDelete: list
        :param PartitionsToDelete: **[REQUIRED]**

          A list of ``PartitionInput`` structures that define the partitions to be deleted.

          - *(dict) --*

            Contains a list of values defining partitions.

            - **Values** *(list) --* **[REQUIRED]**

              The list of values.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Errors': [
                    {
                        'PartitionValues': [
                            'string',
                        ],
                        'ErrorDetail': {
                            'ErrorCode': 'string',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Errors** *(list) --*

              The errors encountered when trying to delete the requested partitions.

              - *(dict) --*

                Contains information about a partition error.

                - **PartitionValues** *(list) --*

                  The values that define the partition.

                  - *(string) --*

                - **ErrorDetail** *(dict) --*

                  The details about the partition error.

                  - **ErrorCode** *(string) --*

                    The code associated with this error.

                  - **ErrorMessage** *(string) --*

                    A message describing the error.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_table(
        self, DatabaseName: str, TablesToDelete: List[str], CatalogId: str = None
    ) -> ClientBatchDeleteTableResponseTypeDef:
        """
        Deletes multiple tables at once.

        .. note::

          After completing this operation, you no longer have access to the table versions and partitions
          that belong to the deleted table. AWS Glue deletes these "orphaned" resources asynchronously in a
          timely manner, at the discretion of the service.

          To ensure the immediate deletion of all related resources, before calling ``BatchDeleteTable`` ,
          use ``DeleteTableVersion`` or ``BatchDeleteTableVersion`` , and ``DeletePartition`` or
          ``BatchDeletePartition`` , to delete any resources that belong to the table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchDeleteTable>`_

        **Request Syntax**
        ::

          response = client.batch_delete_table(
              CatalogId='string',
              DatabaseName='string',
              TablesToDelete=[
                  'string',
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database in which the tables to delete reside. For Hive compatibility,
          this name is entirely lowercase.

        :type TablesToDelete: list
        :param TablesToDelete: **[REQUIRED]**

          A list of the table to delete.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Errors': [
                    {
                        'TableName': 'string',
                        'ErrorDetail': {
                            'ErrorCode': 'string',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Errors** *(list) --*

              A list of errors encountered in attempting to delete the specified tables.

              - *(dict) --*

                An error record for table operations.

                - **TableName** *(string) --*

                  The name of the table. For Hive compatibility, this must be entirely lowercase.

                - **ErrorDetail** *(dict) --*

                  The details about the error.

                  - **ErrorCode** *(string) --*

                    The code associated with this error.

                  - **ErrorMessage** *(string) --*

                    A message describing the error.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_table_version(
        self,
        DatabaseName: str,
        TableName: str,
        VersionIds: List[str],
        CatalogId: str = None,
    ) -> ClientBatchDeleteTableVersionResponseTypeDef:
        """
        Deletes a specified batch of versions of a table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchDeleteTableVersion>`_

        **Request Syntax**
        ::

          response = client.batch_delete_table_version(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              VersionIds=[
                  'string',
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The database in the catalog in which the table resides. For Hive compatibility, this name is
          entirely lowercase.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the table. For Hive compatibility, this name is entirely lowercase.

        :type VersionIds: list
        :param VersionIds: **[REQUIRED]**

          A list of the IDs of versions to be deleted. A ``VersionId`` is a string representation of an
          integer. Each version is incremented by 1.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Errors': [
                    {
                        'TableName': 'string',
                        'VersionId': 'string',
                        'ErrorDetail': {
                            'ErrorCode': 'string',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Errors** *(list) --*

              A list of errors encountered while trying to delete the specified table versions.

              - *(dict) --*

                An error record for table-version operations.

                - **TableName** *(string) --*

                  The name of the table in question.

                - **VersionId** *(string) --*

                  The ID value of the version in question. A ``VersionID`` is a string representation of an
                  integer. Each version is incremented by 1.

                - **ErrorDetail** *(dict) --*

                  The details about the error.

                  - **ErrorCode** *(string) --*

                    The code associated with this error.

                  - **ErrorMessage** *(string) --*

                    A message describing the error.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_crawlers(
        self, CrawlerNames: List[str]
    ) -> ClientBatchGetCrawlersResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of crawler names. After calling the
        ``ListCrawlers`` operation, you can call this operation to access the data to which you have been
        granted permissions. This operation supports all IAM permissions, including permission conditions
        that uses tags.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchGetCrawlers>`_

        **Request Syntax**
        ::

          response = client.batch_get_crawlers(
              CrawlerNames=[
                  'string',
              ]
          )
        :type CrawlerNames: list
        :param CrawlerNames: **[REQUIRED]**

          A list of crawler names, which might be the names returned from the ``ListCrawlers`` operation.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Crawlers': [
                    {
                        'Name': 'string',
                        'Role': 'string',
                        'Targets': {
                            'S3Targets': [
                                {
                                    'Path': 'string',
                                    'Exclusions': [
                                        'string',
                                    ]
                                },
                            ],
                            'JdbcTargets': [
                                {
                                    'ConnectionName': 'string',
                                    'Path': 'string',
                                    'Exclusions': [
                                        'string',
                                    ]
                                },
                            ],
                            'DynamoDBTargets': [
                                {
                                    'Path': 'string'
                                },
                            ],
                            'CatalogTargets': [
                                {
                                    'DatabaseName': 'string',
                                    'Tables': [
                                        'string',
                                    ]
                                },
                            ]
                        },
                        'DatabaseName': 'string',
                        'Description': 'string',
                        'Classifiers': [
                            'string',
                        ],
                        'SchemaChangePolicy': {
                            'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                            'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
                        },
                        'State': 'READY'|'RUNNING'|'STOPPING',
                        'TablePrefix': 'string',
                        'Schedule': {
                            'ScheduleExpression': 'string',
                            'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
                        },
                        'CrawlElapsedTime': 123,
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'LastCrawl': {
                            'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                            'ErrorMessage': 'string',
                            'LogGroup': 'string',
                            'LogStream': 'string',
                            'MessagePrefix': 'string',
                            'StartTime': datetime(2015, 1, 1)
                        },
                        'Version': 123,
                        'Configuration': 'string',
                        'CrawlerSecurityConfiguration': 'string'
                    },
                ],
                'CrawlersNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Crawlers** *(list) --*

              A list of crawler definitions.

              - *(dict) --*

                Specifies a crawler program that examines a data source and uses classifiers to try to
                determine its schema. If successful, the crawler records metadata concerning the data
                source in the AWS Glue Data Catalog.

                - **Name** *(string) --*

                  The name of the crawler.

                - **Role** *(string) --*

                  The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources,
                  such as Amazon Simple Storage Service (Amazon S3) data.

                - **Targets** *(dict) --*

                  A collection of targets to crawl.

                  - **S3Targets** *(list) --*

                    Specifies Amazon Simple Storage Service (Amazon S3) targets.

                    - *(dict) --*

                      Specifies a data store in Amazon Simple Storage Service (Amazon S3).

                      - **Path** *(string) --*

                        The path to the Amazon S3 target.

                      - **Exclusions** *(list) --*

                        A list of glob patterns used to exclude from the crawl. For more information, see
                        `Catalog Tables with a Crawler
                        <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                        - *(string) --*

                  - **JdbcTargets** *(list) --*

                    Specifies JDBC targets.

                    - *(dict) --*

                      Specifies a JDBC data store to crawl.

                      - **ConnectionName** *(string) --*

                        The name of the connection to use to connect to the JDBC target.

                      - **Path** *(string) --*

                        The path of the JDBC target.

                      - **Exclusions** *(list) --*

                        A list of glob patterns used to exclude from the crawl. For more information, see
                        `Catalog Tables with a Crawler
                        <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                        - *(string) --*

                  - **DynamoDBTargets** *(list) --*

                    Specifies Amazon DynamoDB targets.

                    - *(dict) --*

                      Specifies an Amazon DynamoDB table to crawl.

                      - **Path** *(string) --*

                        The name of the DynamoDB table to crawl.

                  - **CatalogTargets** *(list) --*

                    Specifies AWS Glue Data Catalog targets.

                    - *(dict) --*

                      Specifies an AWS Glue Data Catalog target.

                      - **DatabaseName** *(string) --*

                        The name of the database to be synchronized.

                      - **Tables** *(list) --*

                        A list of the tables to be synchronized.

                        - *(string) --*

                - **DatabaseName** *(string) --*

                  The name of the database in which the crawler's output is stored.

                - **Description** *(string) --*

                  A description of the crawler.

                - **Classifiers** *(list) --*

                  A list of UTF-8 strings that specify the custom classifiers that are associated with the
                  crawler.

                  - *(string) --*

                - **SchemaChangePolicy** *(dict) --*

                  The policy that specifies update and delete behaviors for the crawler.

                  - **UpdateBehavior** *(string) --*

                    The update behavior when the crawler finds a changed schema.

                  - **DeleteBehavior** *(string) --*

                    The deletion behavior when the crawler finds a deleted object.

                - **State** *(string) --*

                  Indicates whether the crawler is running, or whether a run is pending.

                - **TablePrefix** *(string) --*

                  The prefix added to the names of tables that are created.

                - **Schedule** *(dict) --*

                  For scheduled crawlers, the schedule when the crawler runs.

                  - **ScheduleExpression** *(string) --*

                    A ``cron`` expression used to specify the schedule. For more information, see
                    `Time-Based Schedules for Jobs and Crawlers
                    <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ .
                    For example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

                  - **State** *(string) --*

                    The state of the schedule.

                - **CrawlElapsedTime** *(integer) --*

                  If the crawler is running, contains the total time elapsed since the last crawl began.

                - **CreationTime** *(datetime) --*

                  The time that the crawler was created.

                - **LastUpdated** *(datetime) --*

                  The time that the crawler was last updated.

                - **LastCrawl** *(dict) --*

                  The status of the last crawl, and potentially error information if an error occurred.

                  - **Status** *(string) --*

                    Status of the last crawl.

                  - **ErrorMessage** *(string) --*

                    If an error occurred, the error information about the last crawl.

                  - **LogGroup** *(string) --*

                    The log group for the last crawl.

                  - **LogStream** *(string) --*

                    The log stream for the last crawl.

                  - **MessagePrefix** *(string) --*

                    The prefix for a message about this crawl.

                  - **StartTime** *(datetime) --*

                    The time at which the crawl started.

                - **Version** *(integer) --*

                  The version of the crawler.

                - **Configuration** *(string) --*

                  Crawler configuration information. This versioned JSON string allows users to specify
                  aspects of a crawler's behavior. For more information, see `Configuring a Crawler
                  <http://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`__ .

                - **CrawlerSecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used by this crawler.

            - **CrawlersNotFound** *(list) --*

              A list of names of crawlers that were not found.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_dev_endpoints(
        self, DevEndpointNames: List[str]
    ) -> ClientBatchGetDevEndpointsResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of development endpoint names. After calling
        the ``ListDevEndpoints`` operation, you can call this operation to access the data to which you
        have been granted permissions. This operation supports all IAM permissions, including permission
        conditions that uses tags.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchGetDevEndpoints>`_

        **Request Syntax**
        ::

          response = client.batch_get_dev_endpoints(
              DevEndpointNames=[
                  'string',
              ]
          )
        :type DevEndpointNames: list
        :param DevEndpointNames: **[REQUIRED]**

          The list of ``DevEndpoint`` names, which might be the names returned from the ``ListDevEndpoint``
          operation.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DevEndpoints': [
                    {
                        'EndpointName': 'string',
                        'RoleArn': 'string',
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'SubnetId': 'string',
                        'YarnEndpointAddress': 'string',
                        'PrivateAddress': 'string',
                        'ZeppelinRemoteSparkInterpreterPort': 123,
                        'PublicAddress': 'string',
                        'Status': 'string',
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'GlueVersion': 'string',
                        'NumberOfWorkers': 123,
                        'NumberOfNodes': 123,
                        'AvailabilityZone': 'string',
                        'VpcId': 'string',
                        'ExtraPythonLibsS3Path': 'string',
                        'ExtraJarsS3Path': 'string',
                        'FailureReason': 'string',
                        'LastUpdateStatus': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'LastModifiedTimestamp': datetime(2015, 1, 1),
                        'PublicKey': 'string',
                        'PublicKeys': [
                            'string',
                        ],
                        'SecurityConfiguration': 'string',
                        'Arguments': {
                            'string': 'string'
                        }
                    },
                ],
                'DevEndpointsNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **DevEndpoints** *(list) --*

              A list of ``DevEndpoint`` definitions.

              - *(dict) --*

                A development endpoint where a developer can remotely debug extract, transform, and load
                (ETL) scripts.

                - **EndpointName** *(string) --*

                  The name of the ``DevEndpoint`` .

                - **RoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role used in this ``DevEndpoint`` .

                - **SecurityGroupIds** *(list) --*

                  A list of security group identifiers used in this ``DevEndpoint`` .

                  - *(string) --*

                - **SubnetId** *(string) --*

                  The subnet ID for this ``DevEndpoint`` .

                - **YarnEndpointAddress** *(string) --*

                  The YARN endpoint address used by this ``DevEndpoint`` .

                - **PrivateAddress** *(string) --*

                  A private IP address to access the ``DevEndpoint`` within a VPC if the ``DevEndpoint`` is
                  created within one. The ``PrivateAddress`` field is present only when you create the
                  ``DevEndpoint`` within your VPC.

                - **ZeppelinRemoteSparkInterpreterPort** *(integer) --*

                  The Apache Zeppelin port for the remote Apache Spark interpreter.

                - **PublicAddress** *(string) --*

                  The public IP address used by this ``DevEndpoint`` . The ``PublicAddress`` field is
                  present only when you create a non-virtual private cloud (VPC) ``DevEndpoint`` .

                - **Status** *(string) --*

                  The current status of this ``DevEndpoint`` .

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated to the development endpoint. Accepts a
                  value of Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a
                  50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB
                  disk), and provides 1 executor per worker. We recommend this worker type for
                  memory-intensive jobs.

                  * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128
                  GB disk), and provides 1 executor per worker. We recommend this worker type for
                  memory-intensive jobs.

                  Known issue: when a development endpoint is created with the ``G.2X``  ``WorkerType``
                  configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB
                  of memory, and a 64 GB disk.

                - **GlueVersion** *(string) --*

                  Glue version determines the versions of Apache Spark and Python that AWS Glue supports.
                  The Python version indicates the version supported for running your ETL scripts on
                  development endpoints.

                  For more information about the available AWS Glue versions and corresponding Spark and
                  Python versions, see `Glue version
                  <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer guide.

                  Development endpoints that are created without specifying a Glue version default to Glue
                  0.9.

                  You can specify a version of Python support for development endpoints by using the
                  ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no
                  arguments are provided, the version defaults to Python 2.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated to the development
                  endpoint.

                  The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

                - **NumberOfNodes** *(integer) --*

                  The number of AWS Glue Data Processing Units (DPUs) allocated to this ``DevEndpoint`` .

                - **AvailabilityZone** *(string) --*

                  The AWS Availability Zone where this ``DevEndpoint`` is located.

                - **VpcId** *(string) --*

                  The ID of the virtual private cloud (VPC) used by this ``DevEndpoint`` .

                - **ExtraPythonLibsS3Path** *(string) --*

                  The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in
                  your ``DevEndpoint`` . Multiple values must be complete paths separated by a comma.

                  .. note::

                    You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on
                    C extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis
                    library, are not currently supported.

                - **ExtraJarsS3Path** *(string) --*

                  The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your
                  ``DevEndpoint`` .

                  .. note::

                    You can only use pure Java/Scala libraries with a ``DevEndpoint`` .

                - **FailureReason** *(string) --*

                  The reason for a current failure in this ``DevEndpoint`` .

                - **LastUpdateStatus** *(string) --*

                  The status of the last update.

                - **CreatedTimestamp** *(datetime) --*

                  The point in time at which this DevEndpoint was created.

                - **LastModifiedTimestamp** *(datetime) --*

                  The point in time at which this ``DevEndpoint`` was last modified.

                - **PublicKey** *(string) --*

                  The public key to be used by this ``DevEndpoint`` for authentication. This attribute is
                  provided for backward compatibility because the recommended attribute to use is public
                  keys.

                - **PublicKeys** *(list) --*

                  A list of public keys to be used by the ``DevEndpoints`` for authentication. Using this
                  attribute is preferred over a single public key because the public keys allow you to have
                  a different private key per client.

                  .. note::

                    If you previously created an endpoint with a public key, you must remove that key to be
                    able to set a list of public keys. Call the ``UpdateDevEndpoint`` API operation with
                    the public key content in the ``deletePublicKeys`` attribute, and the list of new keys
                    in the ``addPublicKeys`` attribute.

                  - *(string) --*

                - **SecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used with this ``DevEndpoint`` .

                - **Arguments** *(dict) --*

                  A map of arguments used to configure the ``DevEndpoint`` .

                  Valid arguments are:

                  * ``"--enable-glue-datacatalog": ""``

                  * ``"GLUE_PYTHON_VERSION": "3"``

                  * ``"GLUE_PYTHON_VERSION": "2"``

                  You can specify a version of Python support for development endpoints by using the
                  ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no
                  arguments are provided, the version defaults to Python 2.

                  - *(string) --*

                    - *(string) --*

            - **DevEndpointsNotFound** *(list) --*

              A list of ``DevEndpoints`` not found.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_jobs(self, JobNames: List[str]) -> ClientBatchGetJobsResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of job names. After calling the ``ListJobs``
        operation, you can call this operation to access the data to which you have been granted
        permissions. This operation supports all IAM permissions, including permission conditions that uses
        tags.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchGetJobs>`_

        **Request Syntax**
        ::

          response = client.batch_get_jobs(
              JobNames=[
                  'string',
              ]
          )
        :type JobNames: list
        :param JobNames: **[REQUIRED]**

          A list of job names, which might be the names returned from the ``ListJobs`` operation.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Jobs': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'LogUri': 'string',
                        'Role': 'string',
                        'CreatedOn': datetime(2015, 1, 1),
                        'LastModifiedOn': datetime(2015, 1, 1),
                        'ExecutionProperty': {
                            'MaxConcurrentRuns': 123
                        },
                        'Command': {
                            'Name': 'string',
                            'ScriptLocation': 'string',
                            'PythonVersion': 'string'
                        },
                        'DefaultArguments': {
                            'string': 'string'
                        },
                        'Connections': {
                            'Connections': [
                                'string',
                            ]
                        },
                        'MaxRetries': 123,
                        'AllocatedCapacity': 123,
                        'Timeout': 123,
                        'MaxCapacity': 123.0,
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'NumberOfWorkers': 123,
                        'SecurityConfiguration': 'string',
                        'NotificationProperty': {
                            'NotifyDelayAfter': 123
                        },
                        'GlueVersion': 'string'
                    },
                ],
                'JobsNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Jobs** *(list) --*

              A list of job definitions.

              - *(dict) --*

                Specifies a job definition.

                - **Name** *(string) --*

                  The name you assign to this job definition.

                - **Description** *(string) --*

                  A description of the job.

                - **LogUri** *(string) --*

                  This field is reserved for future use.

                - **Role** *(string) --*

                  The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

                - **CreatedOn** *(datetime) --*

                  The time and date that this job definition was created.

                - **LastModifiedOn** *(datetime) --*

                  The last point in time when this job definition was modified.

                - **ExecutionProperty** *(dict) --*

                  An ``ExecutionProperty`` specifying the maximum number of concurrent runs allowed for
                  this job.

                  - **MaxConcurrentRuns** *(integer) --*

                    The maximum number of concurrent runs allowed for the job. The default is 1. An error
                    is returned when this threshold is reached. The maximum value you can specify is
                    controlled by a service limit.

                - **Command** *(dict) --*

                  The ``JobCommand`` that executes this job.

                  - **Name** *(string) --*

                    The name of the job command. For an Apache Spark ETL job, this must be ``glueetl`` .
                    For a Python shell job, it must be ``pythonshell`` .

                  - **ScriptLocation** *(string) --*

                    Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes
                    a job.

                  - **PythonVersion** *(string) --*

                    The Python version being used to execute a Python shell job. Allowed values are 2 or 3.

                - **DefaultArguments** *(dict) --*

                  The default arguments for this job, specified as name-value pairs.

                  You can specify arguments here that your own job-execution script consumes, as well as
                  arguments that AWS Glue itself consumes.

                  For information about how to specify and consume your own Job arguments, see the `Calling
                  AWS Glue APIs in Python
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                  topic in the developer guide.

                  For information about the key-value pairs that AWS Glue consumes to set up your job, see
                  the `Special Parameters Used by AWS Glue
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                  topic in the developer guide.

                  - *(string) --*

                    - *(string) --*

                - **Connections** *(dict) --*

                  The connections used for this job.

                  - **Connections** *(list) --*

                    A list of connections used by the job.

                    - *(string) --*

                - **MaxRetries** *(integer) --*

                  The maximum number of times to retry this job after a JobRun fails.

                - **AllocatedCapacity** *(integer) --*

                  This field is deprecated. Use ``MaxCapacity`` instead.

                  The number of AWS Glue data processing units (DPUs) allocated to runs of this job. You
                  can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of
                  processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For
                  more information, see the `AWS Glue pricing page
                  <https://aws.amazon.com/glue/pricing/>`__ .

                - **Timeout** *(integer) --*

                  The job timeout in minutes. This is the maximum time that a job run can consume resources
                  before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48
                  hours).

                - **MaxCapacity** *(float) --*

                  The number of AWS Glue data processing units (DPUs) that can be allocated when this job
                  runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute
                  capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page
                  <https://aws.amazon.com/glue/pricing/>`__ .

                  Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                  The value that can be allocated for ``MaxCapacity`` depends on whether you are running a
                  Python shell job or an Apache Spark ETL job:

                  * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you can
                  allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                  * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"), you can
                  allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a
                  fractional DPU allocation.

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated when a job runs. Accepts a value of
                  Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a
                  50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB
                  disk), and provides 1 executor per worker. We recommend this worker type for
                  memory-intensive jobs.

                  * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128
                  GB disk), and provides 1 executor per worker. We recommend this worker type for
                  memory-intensive jobs.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated when a job runs.

                  The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

                - **SecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used with this job.

                - **NotificationProperty** *(dict) --*

                  Specifies configuration properties of a job notification.

                  - **NotifyDelayAfter** *(integer) --*

                    After a job run starts, the number of minutes to wait before sending a job run delay
                    notification.

                - **GlueVersion** *(string) --*

                  Glue version determines the versions of Apache Spark and Python that AWS Glue supports.
                  The Python version indicates the version supported for jobs of type Spark.

                  For more information about the available AWS Glue versions and corresponding Spark and
                  Python versions, see `Glue version
                  <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer guide.

                  Jobs that are created without specifying a Glue version default to Glue 0.9.

            - **JobsNotFound** *(list) --*

              A list of names of jobs not found.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToGet: List[ClientBatchGetPartitionPartitionsToGetTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchGetPartitionResponseTypeDef:
        """
        Retrieves partitions in a batch request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchGetPartition>`_

        **Request Syntax**
        ::

          response = client.batch_get_partition(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              PartitionsToGet=[
                  {
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS
          account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the partitions reside.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the partitions' table.

        :type PartitionsToGet: list
        :param PartitionsToGet: **[REQUIRED]**

          A list of partition values identifying the partitions to retrieve.

          - *(dict) --*

            Contains a list of values defining partitions.

            - **Values** *(list) --* **[REQUIRED]**

              The list of values.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Partitions': [
                    {
                        'Values': [
                            'string',
                        ],
                        'DatabaseName': 'string',
                        'TableName': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastAccessTime': datetime(2015, 1, 1),
                        'StorageDescriptor': {
                            'Columns': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'Location': 'string',
                            'InputFormat': 'string',
                            'OutputFormat': 'string',
                            'Compressed': True|False,
                            'NumberOfBuckets': 123,
                            'SerdeInfo': {
                                'Name': 'string',
                                'SerializationLibrary': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                            'BucketColumns': [
                                'string',
                            ],
                            'SortColumns': [
                                {
                                    'Column': 'string',
                                    'SortOrder': 123
                                },
                            ],
                            'Parameters': {
                                'string': 'string'
                            },
                            'SkewedInfo': {
                                'SkewedColumnNames': [
                                    'string',
                                ],
                                'SkewedColumnValues': [
                                    'string',
                                ],
                                'SkewedColumnValueLocationMaps': {
                                    'string': 'string'
                                }
                            },
                            'StoredAsSubDirectories': True|False
                        },
                        'Parameters': {
                            'string': 'string'
                        },
                        'LastAnalyzedTime': datetime(2015, 1, 1)
                    },
                ],
                'UnprocessedKeys': [
                    {
                        'Values': [
                            'string',
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Partitions** *(list) --*

              A list of the requested partitions.

              - *(dict) --*

                Represents a slice of table data.

                - **Values** *(list) --*

                  The values of the partition.

                  - *(string) --*

                - **DatabaseName** *(string) --*

                  The name of the catalog database in which to create the partition.

                - **TableName** *(string) --*

                  The name of the database table in which to create the partition.

                - **CreationTime** *(datetime) --*

                  The time at which the partition was created.

                - **LastAccessTime** *(datetime) --*

                  The last time at which the partition was accessed.

                - **StorageDescriptor** *(dict) --*

                  Provides information about the physical location where the partition is stored.

                  - **Columns** *(list) --*

                    A list of the ``Columns`` in the table.

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **Location** *(string) --*

                    The physical location of the table. By default, this takes the form of the warehouse
                    location, followed by the database location in the warehouse, followed by the table
                    name.

                  - **InputFormat** *(string) --*

                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                    custom format.

                  - **OutputFormat** *(string) --*

                    The output format: ``SequenceFileOutputFormat`` (binary), or
                    ``IgnoreKeyTextOutputFormat`` , or a custom format.

                  - **Compressed** *(boolean) --*

                     ``True`` if the data in the table is compressed, or ``False`` if not.

                  - **NumberOfBuckets** *(integer) --*

                    Must be specified if the table contains any dimension columns.

                  - **SerdeInfo** *(dict) --*

                    The serialization/deserialization (SerDe) information.

                    - **Name** *(string) --*

                      Name of the SerDe.

                    - **SerializationLibrary** *(string) --*

                      Usually the class that implements the SerDe. An example is
                      ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                    - **Parameters** *(dict) --*

                      These key-value pairs define initialization parameters for the SerDe.

                      - *(string) --*

                        - *(string) --*

                  - **BucketColumns** *(list) --*

                    A list of reducer grouping columns, clustering columns, and bucketing columns in the
                    table.

                    - *(string) --*

                  - **SortColumns** *(list) --*

                    A list specifying the sort order of each bucket in the table.

                    - *(dict) --*

                      Specifies the sort order of a sorted column.

                      - **Column** *(string) --*

                        The name of the column.

                      - **SortOrder** *(integer) --*

                        Indicates that the column is sorted in ascending order (``== 1`` ), or in
                        descending order (``==0`` ).

                  - **Parameters** *(dict) --*

                    The user-supplied properties in key-value form.

                    - *(string) --*

                      - *(string) --*

                  - **SkewedInfo** *(dict) --*

                    The information about values that appear frequently in a column (skewed values).

                    - **SkewedColumnNames** *(list) --*

                      A list of names of columns that contain skewed values.

                      - *(string) --*

                    - **SkewedColumnValues** *(list) --*

                      A list of values that appear so frequently as to be considered skewed.

                      - *(string) --*

                    - **SkewedColumnValueLocationMaps** *(dict) --*

                      A mapping of skewed values to the columns that contain them.

                      - *(string) --*

                        - *(string) --*

                  - **StoredAsSubDirectories** *(boolean) --*

                     ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                - **Parameters** *(dict) --*

                  These key-value pairs define partition parameters.

                  - *(string) --*

                    - *(string) --*

                - **LastAnalyzedTime** *(datetime) --*

                  The last time at which column statistics were computed for this partition.

            - **UnprocessedKeys** *(list) --*

              A list of the partition values in the request for which partitions were not returned.

              - *(dict) --*

                Contains a list of values defining partitions.

                - **Values** *(list) --*

                  The list of values.

                  - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_triggers(
        self, TriggerNames: List[str]
    ) -> ClientBatchGetTriggersResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of trigger names. After calling the
        ``ListTriggers`` operation, you can call this operation to access the data to which you have been
        granted permissions. This operation supports all IAM permissions, including permission conditions
        that uses tags.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchGetTriggers>`_

        **Request Syntax**
        ::

          response = client.batch_get_triggers(
              TriggerNames=[
                  'string',
              ]
          )
        :type TriggerNames: list
        :param TriggerNames: **[REQUIRED]**

          A list of trigger names, which may be the names returned from the ``ListTriggers`` operation.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Triggers': [
                    {
                        'Name': 'string',
                        'WorkflowName': 'string',
                        'Id': 'string',
                        'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                        'State':
                        'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'
                        |'DELETING'|'UPDATING',
                        'Description': 'string',
                        'Schedule': 'string',
                        'Actions': [
                            {
                                'JobName': 'string',
                                'Arguments': {
                                    'string': 'string'
                                },
                                'Timeout': 123,
                                'SecurityConfiguration': 'string',
                                'NotificationProperty': {
                                    'NotifyDelayAfter': 123
                                },
                                'CrawlerName': 'string'
                            },
                        ],
                        'Predicate': {
                            'Logical': 'AND'|'ANY',
                            'Conditions': [
                                {
                                    'LogicalOperator': 'EQUALS',
                                    'JobName': 'string',
                                    'State':
                                    'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                                    |'TIMEOUT',
                                    'CrawlerName': 'string',
                                    'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                },
                            ]
                        }
                    },
                ],
                'TriggersNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Triggers** *(list) --*

              A list of trigger definitions.

              - *(dict) --*

                Information about a specific trigger.

                - **Name** *(string) --*

                  The name of the trigger.

                - **WorkflowName** *(string) --*

                  The name of the workflow associated with the trigger.

                - **Id** *(string) --*

                  Reserved for future use.

                - **Type** *(string) --*

                  The type of trigger that this is.

                - **State** *(string) --*

                  The current state of the trigger.

                - **Description** *(string) --*

                  A description of this trigger.

                - **Schedule** *(string) --*

                  A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs
                  and Crawlers
                  <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ .
                  For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * *
                  ? *)`` .

                - **Actions** *(list) --*

                  The actions initiated by this trigger.

                  - *(dict) --*

                    Defines an action to be initiated by a trigger.

                    - **JobName** *(string) --*

                      The name of a job to be executed.

                    - **Arguments** *(dict) --*

                      The job arguments used when this trigger fires. For this job run, they replace the
                      default arguments set in the job definition itself.

                      You can specify arguments here that your own job-execution script consumes, as well
                      as arguments that AWS Glue itself consumes.

                      For information about how to specify and consume your own Job arguments, see the
                      `Calling AWS Glue APIs in Python
                      <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                      topic in the developer guide.

                      For information about the key-value pairs that AWS Glue consumes to set up your job,
                      see the `Special Parameters Used by AWS Glue
                      <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                      topic in the developer guide.

                      - *(string) --*

                        - *(string) --*

                    - **Timeout** *(integer) --*

                      The ``JobRun`` timeout in minutes. This is the maximum time that a job run can
                      consume resources before it is terminated and enters ``TIMEOUT`` status. The default
                      is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

                    - **SecurityConfiguration** *(string) --*

                      The name of the ``SecurityConfiguration`` structure to be used with this action.

                    - **NotificationProperty** *(dict) --*

                      Specifies configuration properties of a job run notification.

                      - **NotifyDelayAfter** *(integer) --*

                        After a job run starts, the number of minutes to wait before sending a job run
                        delay notification.

                    - **CrawlerName** *(string) --*

                      The name of the crawler to be used with this action.

                - **Predicate** *(dict) --*

                  The predicate of this trigger, which defines when it will fire.

                  - **Logical** *(string) --*

                    An optional field if only one condition is listed. If multiple conditions are listed,
                    then this field is required.

                  - **Conditions** *(list) --*

                    A list of the conditions that determine when the trigger will fire.

                    - *(dict) --*

                      Defines a condition under which a trigger fires.

                      - **LogicalOperator** *(string) --*

                        A logical operator.

                      - **JobName** *(string) --*

                        The name of the job whose ``JobRuns`` this condition applies to, and on which this
                        trigger waits.

                      - **State** *(string) --*

                        The condition state. Currently, the values supported are ``SUCCEEDED`` ,
                        ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                      - **CrawlerName** *(string) --*

                        The name of the crawler to which this condition applies.

                      - **CrawlState** *(string) --*

                        The state of the crawler to which this condition applies.

            - **TriggersNotFound** *(list) --*

              A list of names of triggers not found.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_workflows(
        self, Names: List[str], IncludeGraph: bool = None
    ) -> ClientBatchGetWorkflowsResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of workflow names. After calling the
        ``ListWorkflows`` operation, you can call this operation to access the data to which you have been
        granted permissions. This operation supports all IAM permissions, including permission conditions
        that uses tags.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchGetWorkflows>`_

        **Request Syntax**
        ::

          response = client.batch_get_workflows(
              Names=[
                  'string',
              ],
              IncludeGraph=True|False
          )
        :type Names: list
        :param Names: **[REQUIRED]**

          A list of workflow names, which may be the names returned from the ``ListWorkflows`` operation.

          - *(string) --*

        :type IncludeGraph: boolean
        :param IncludeGraph:

          Specifies whether to include a graph when returning the workflow resource metadata.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Workflows': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'DefaultRunProperties': {
                            'string': 'string'
                        },
                        'CreatedOn': datetime(2015, 1, 1),
                        'LastModifiedOn': datetime(2015, 1, 1),
                        'LastRun': {
                            'Name': 'string',
                            'WorkflowRunId': 'string',
                            'WorkflowRunProperties': {
                                'string': 'string'
                            },
                            'StartedOn': datetime(2015, 1, 1),
                            'CompletedOn': datetime(2015, 1, 1),
                            'Status': 'RUNNING'|'COMPLETED',
                            'Statistics': {
                                'TotalActions': 123,
                                'TimeoutActions': 123,
                                'FailedActions': 123,
                                'StoppedActions': 123,
                                'SucceededActions': 123,
                                'RunningActions': 123
                            },
                            'Graph': {
                                'Nodes': [
                                    {
                                        'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                                        'Name': 'string',
                                        'UniqueId': 'string',
                                        'TriggerDetails': {
                                            'Trigger': {
                                                'Name': 'string',
                                                'WorkflowName': 'string',
                                                'Id': 'string',
                                                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                                'State':
                                                'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'
                                                |'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                                'Description': 'string',
                                                'Schedule': 'string',
                                                'Actions': [
                                                    {
                                                        'JobName': 'string',
                                                        'Arguments': {
                                                            'string': 'string'
                                                        },
                                                        'Timeout': 123,
                                                        'SecurityConfiguration': 'string',
                                                        'NotificationProperty': {
                                                            'NotifyDelayAfter': 123
                                                        },
                                                        'CrawlerName': 'string'
                                                    },
                                                ],
                                                'Predicate': {
                                                    'Logical': 'AND'|'ANY',
                                                    'Conditions': [
                                                        {
                                                            'LogicalOperator': 'EQUALS',
                                                            'JobName': 'string',
                                                            'State':
                                                            'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'
                                                            |'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                            'CrawlerName': 'string',
                                                            'CrawlState':
                                                            'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                                        },
                                                    ]
                                                }
                                            }
                                        },
                                        'JobDetails': {
                                            'JobRuns': [
                                                {
                                                    'Id': 'string',
                                                    'Attempt': 123,
                                                    'PreviousRunId': 'string',
                                                    'TriggerName': 'string',
                                                    'JobName': 'string',
                                                    'StartedOn': datetime(2015, 1, 1),
                                                    'LastModifiedOn': datetime(2015, 1, 1),
                                                    'CompletedOn': datetime(2015, 1, 1),
                                                    'JobRunState':
                                                    'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'
                                                    |'FAILED'|'TIMEOUT',
                                                    'Arguments': {
                                                        'string': 'string'
                                                    },
                                                    'ErrorMessage': 'string',
                                                    'PredecessorRuns': [
                                                        {
                                                            'JobName': 'string',
                                                            'RunId': 'string'
                                                        },
                                                    ],
                                                    'AllocatedCapacity': 123,
                                                    'ExecutionTime': 123,
                                                    'Timeout': 123,
                                                    'MaxCapacity': 123.0,
                                                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                                    'NumberOfWorkers': 123,
                                                    'SecurityConfiguration': 'string',
                                                    'LogGroupName': 'string',
                                                    'NotificationProperty': {
                                                        'NotifyDelayAfter': 123
                                                    },
                                                    'GlueVersion': 'string'
                                                },
                                            ]
                                        },
                                        'CrawlerDetails': {
                                            'Crawls': [
                                                {
                                                    'State': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                                                    'StartedOn': datetime(2015, 1, 1),
                                                    'CompletedOn': datetime(2015, 1, 1),
                                                    'ErrorMessage': 'string',
                                                    'LogGroup': 'string',
                                                    'LogStream': 'string'
                                                },
                                            ]
                                        }
                                    },
                                ],
                                'Edges': [
                                    {
                                        'SourceId': 'string',
                                        'DestinationId': 'string'
                                    },
                                ]
                            }
                        },
                        'Graph': {
                            'Nodes': [
                                {
                                    'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                                    'Name': 'string',
                                    'UniqueId': 'string',
                                    'TriggerDetails': {
                                        'Trigger': {
                                            'Name': 'string',
                                            'WorkflowName': 'string',
                                            'Id': 'string',
                                            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                            'State':
                                            'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'
                                            |'DEACTIVATED'|'DELETING'|'UPDATING',
                                            'Description': 'string',
                                            'Schedule': 'string',
                                            'Actions': [
                                                {
                                                    'JobName': 'string',
                                                    'Arguments': {
                                                        'string': 'string'
                                                    },
                                                    'Timeout': 123,
                                                    'SecurityConfiguration': 'string',
                                                    'NotificationProperty': {
                                                        'NotifyDelayAfter': 123
                                                    },
                                                    'CrawlerName': 'string'
                                                },
                                            ],
                                            'Predicate': {
                                                'Logical': 'AND'|'ANY',
                                                'Conditions': [
                                                    {
                                                        'LogicalOperator': 'EQUALS',
                                                        'JobName': 'string',
                                                        'State':
                                                        'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'
                                                        |'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                        'CrawlerName': 'string',
                                                        'CrawlState':
                                                        'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                                    },
                                                ]
                                            }
                                        }
                                    },
                                    'JobDetails': {
                                        'JobRuns': [
                                            {
                                                'Id': 'string',
                                                'Attempt': 123,
                                                'PreviousRunId': 'string',
                                                'TriggerName': 'string',
                                                'JobName': 'string',
                                                'StartedOn': datetime(2015, 1, 1),
                                                'LastModifiedOn': datetime(2015, 1, 1),
                                                'CompletedOn': datetime(2015, 1, 1),
                                                'JobRunState':
                                                'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'
                                                |'FAILED'|'TIMEOUT',
                                                'Arguments': {
                                                    'string': 'string'
                                                },
                                                'ErrorMessage': 'string',
                                                'PredecessorRuns': [
                                                    {
                                                        'JobName': 'string',
                                                        'RunId': 'string'
                                                    },
                                                ],
                                                'AllocatedCapacity': 123,
                                                'ExecutionTime': 123,
                                                'Timeout': 123,
                                                'MaxCapacity': 123.0,
                                                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                                'NumberOfWorkers': 123,
                                                'SecurityConfiguration': 'string',
                                                'LogGroupName': 'string',
                                                'NotificationProperty': {
                                                    'NotifyDelayAfter': 123
                                                },
                                                'GlueVersion': 'string'
                                            },
                                        ]
                                    },
                                    'CrawlerDetails': {
                                        'Crawls': [
                                            {
                                                'State': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                                                'StartedOn': datetime(2015, 1, 1),
                                                'CompletedOn': datetime(2015, 1, 1),
                                                'ErrorMessage': 'string',
                                                'LogGroup': 'string',
                                                'LogStream': 'string'
                                            },
                                        ]
                                    }
                                },
                            ],
                            'Edges': [
                                {
                                    'SourceId': 'string',
                                    'DestinationId': 'string'
                                },
                            ]
                        }
                    },
                ],
                'MissingWorkflows': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Workflows** *(list) --*

              A list of workflow resource metadata.

              - *(dict) --*

                A workflow represents a flow in which AWS Glue components should be executed to complete a
                logical task.

                - **Name** *(string) --*

                  The name of the workflow representing the flow.

                - **Description** *(string) --*

                  A description of the workflow.

                - **DefaultRunProperties** *(dict) --*

                  A collection of properties to be used as part of each execution of the workflow.

                  - *(string) --*

                    - *(string) --*

                - **CreatedOn** *(datetime) --*

                  The date and time when the workflow was created.

                - **LastModifiedOn** *(datetime) --*

                  The date and time when the workflow was last modified.

                - **LastRun** *(dict) --*

                  The information about the last execution of the workflow.

                  - **Name** *(string) --*

                    Name of the workflow which was executed.

                  - **WorkflowRunId** *(string) --*

                    The ID of this workflow run.

                  - **WorkflowRunProperties** *(dict) --*

                    The workflow run properties which were set during the run.

                    - *(string) --*

                      - *(string) --*

                  - **StartedOn** *(datetime) --*

                    The date and time when the workflow run was started.

                  - **CompletedOn** *(datetime) --*

                    The date and time when the workflow run completed.

                  - **Status** *(string) --*

                    The status of the workflow run.

                  - **Statistics** *(dict) --*

                    The statistics of the run.

                    - **TotalActions** *(integer) --*

                      Total number of Actions in the workflow run.

                    - **TimeoutActions** *(integer) --*

                      Total number of Actions which timed out.

                    - **FailedActions** *(integer) --*

                      Total number of Actions which have failed.

                    - **StoppedActions** *(integer) --*

                      Total number of Actions which have stopped.

                    - **SucceededActions** *(integer) --*

                      Total number of Actions which have succeeded.

                    - **RunningActions** *(integer) --*

                      Total number Actions in running state.

                  - **Graph** *(dict) --*

                    The graph representing all the AWS Glue components that belong to the workflow as nodes
                    and directed connections between them as edges.

                    - **Nodes** *(list) --*

                      A list of the the AWS Glue components belong to the workflow represented as nodes.

                      - *(dict) --*

                        A node represents an AWS Glue component like Trigger, Job etc. which is part of a
                        workflow.

                        - **Type** *(string) --*

                          The type of AWS Glue component represented by the node.

                        - **Name** *(string) --*

                          The name of the AWS Glue component represented by the node.

                        - **UniqueId** *(string) --*

                          The unique Id assigned to the node within the workflow.

                        - **TriggerDetails** *(dict) --*

                          Details of the Trigger when the node represents a Trigger.

                          - **Trigger** *(dict) --*

                            The information of the trigger represented by the trigger node.

                            - **Name** *(string) --*

                              The name of the trigger.

                            - **WorkflowName** *(string) --*

                              The name of the workflow associated with the trigger.

                            - **Id** *(string) --*

                              Reserved for future use.

                            - **Type** *(string) --*

                              The type of trigger that this is.

                            - **State** *(string) --*

                              The current state of the trigger.

                            - **Description** *(string) --*

                              A description of this trigger.

                            - **Schedule** *(string) --*

                              A ``cron`` expression used to specify the schedule (see `Time-Based Schedules
                              for Jobs and Crawlers
                              <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__
                              . For example, to run something every day at 12:15 UTC, you would specify:
                              ``cron(15 12 * * ? *)`` .

                            - **Actions** *(list) --*

                              The actions initiated by this trigger.

                              - *(dict) --*

                                Defines an action to be initiated by a trigger.

                                - **JobName** *(string) --*

                                  The name of a job to be executed.

                                - **Arguments** *(dict) --*

                                  The job arguments used when this trigger fires. For this job run, they
                                  replace the default arguments set in the job definition itself.

                                  You can specify arguments here that your own job-execution script
                                  consumes, as well as arguments that AWS Glue itself consumes.

                                  For information about how to specify and consume your own Job arguments,
                                  see the `Calling AWS Glue APIs in Python
                                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                                  topic in the developer guide.

                                  For information about the key-value pairs that AWS Glue consumes to set
                                  up your job, see the `Special Parameters Used by AWS Glue
                                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                                  topic in the developer guide.

                                  - *(string) --*

                                    - *(string) --*

                                - **Timeout** *(integer) --*

                                  The ``JobRun`` timeout in minutes. This is the maximum time that a job
                                  run can consume resources before it is terminated and enters ``TIMEOUT``
                                  status. The default is 2,880 minutes (48 hours). This overrides the
                                  timeout value set in the parent job.

                                - **SecurityConfiguration** *(string) --*

                                  The name of the ``SecurityConfiguration`` structure to be used with this
                                  action.

                                - **NotificationProperty** *(dict) --*

                                  Specifies configuration properties of a job run notification.

                                  - **NotifyDelayAfter** *(integer) --*

                                    After a job run starts, the number of minutes to wait before sending a
                                    job run delay notification.

                                - **CrawlerName** *(string) --*

                                  The name of the crawler to be used with this action.

                            - **Predicate** *(dict) --*

                              The predicate of this trigger, which defines when it will fire.

                              - **Logical** *(string) --*

                                An optional field if only one condition is listed. If multiple conditions
                                are listed, then this field is required.

                              - **Conditions** *(list) --*

                                A list of the conditions that determine when the trigger will fire.

                                - *(dict) --*

                                  Defines a condition under which a trigger fires.

                                  - **LogicalOperator** *(string) --*

                                    A logical operator.

                                  - **JobName** *(string) --*

                                    The name of the job whose ``JobRuns`` this condition applies to, and on
                                    which this trigger waits.

                                  - **State** *(string) --*

                                    The condition state. Currently, the values supported are ``SUCCEEDED``
                                    , ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                                  - **CrawlerName** *(string) --*

                                    The name of the crawler to which this condition applies.

                                  - **CrawlState** *(string) --*

                                    The state of the crawler to which this condition applies.

                        - **JobDetails** *(dict) --*

                          Details of the Job when the node represents a Job.

                          - **JobRuns** *(list) --*

                            The information for the job runs represented by the job node.

                            - *(dict) --*

                              Contains information about a job run.

                              - **Id** *(string) --*

                                The ID of this job run.

                              - **Attempt** *(integer) --*

                                The number of the attempt to run this job.

                              - **PreviousRunId** *(string) --*

                                The ID of the previous run of this job. For example, the ``JobRunId``
                                specified in the ``StartJobRun`` action.

                              - **TriggerName** *(string) --*

                                The name of the trigger that started this job run.

                              - **JobName** *(string) --*

                                The name of the job definition being used in this run.

                              - **StartedOn** *(datetime) --*

                                The date and time at which this job run was started.

                              - **LastModifiedOn** *(datetime) --*

                                The last time that this job run was modified.

                              - **CompletedOn** *(datetime) --*

                                The date and time that this job run completed.

                              - **JobRunState** *(string) --*

                                The current state of the job run.

                              - **Arguments** *(dict) --*

                                The job arguments associated with this run. For this job run, they replace
                                the default arguments set in the job definition itself.

                                You can specify arguments here that your own job-execution script consumes,
                                as well as arguments that AWS Glue itself consumes.

                                For information about how to specify and consume your own job arguments,
                                see the `Calling AWS Glue APIs in Python
                                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                                topic in the developer guide.

                                For information about the key-value pairs that AWS Glue consumes to set up
                                your job, see the `Special Parameters Used by AWS Glue
                                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                                topic in the developer guide.

                                - *(string) --*

                                  - *(string) --*

                              - **ErrorMessage** *(string) --*

                                An error message associated with this job run.

                              - **PredecessorRuns** *(list) --*

                                A list of predecessors to this job run.

                                - *(dict) --*

                                  A job run that was used in the predicate of a conditional trigger that
                                  triggered this job run.

                                  - **JobName** *(string) --*

                                    The name of the job definition used by the predecessor job run.

                                  - **RunId** *(string) --*

                                    The job-run ID of the predecessor job run.

                              - **AllocatedCapacity** *(integer) --*

                                This field is deprecated. Use ``MaxCapacity`` instead.

                                The number of AWS Glue data processing units (DPUs) allocated to this
                                JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
                                relative measure of processing power that consists of 4 vCPUs of compute
                                capacity and 16 GB of memory. For more information, see the `AWS Glue
                                pricing page <https://aws.amazon.com/glue/pricing/>`__ .

                              - **ExecutionTime** *(integer) --*

                                The amount of time (in seconds) that the job run consumed resources.

                              - **Timeout** *(integer) --*

                                The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                                can consume resources before it is terminated and enters ``TIMEOUT``
                                status. The default is 2,880 minutes (48 hours). This overrides the timeout
                                value set in the parent job.

                              - **MaxCapacity** *(float) --*

                                The number of AWS Glue data processing units (DPUs) that can be allocated
                                when this job runs. A DPU is a relative measure of processing power that
                                consists of 4 vCPUs of compute capacity and 16 GB of memory. For more
                                information, see the `AWS Glue pricing page
                                <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                                Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers``
                                .

                                The value that can be allocated for ``MaxCapacity`` depends on whether you
                                are running a Python shell job or an Apache Spark ETL job:

                                * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"),
                                you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                                * When you specify an Apache Spark ETL job (``JobCommand.Name``
                                ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs.
                                This job type cannot have a fractional DPU allocation.

                              - **WorkerType** *(string) --*

                                The type of predefined worker that is allocated when a job runs. Accepts a
                                value of Standard, G.1X, or G.2X.

                                * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of
                                memory and a 50GB disk, and 2 executors per worker.

                                * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of
                                memory and a 64GB disk, and 1 executor per worker.

                                * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of
                                memory and a 128GB disk, and 1 executor per worker.

                              - **NumberOfWorkers** *(integer) --*

                                The number of workers of a defined ``workerType`` that are allocated when a
                                job runs.

                                The maximum number of workers you can define are 299 for ``G.1X`` , and 149
                                for ``G.2X`` .

                              - **SecurityConfiguration** *(string) --*

                                The name of the ``SecurityConfiguration`` structure to be used with this
                                job run.

                              - **LogGroupName** *(string) --*

                                The name of the log group for secure logging that can be server-side
                                encrypted in Amazon CloudWatch using AWS KMS. This name can be
                                ``/aws-glue/jobs/`` , in which case the default encryption is ``NONE`` . If
                                you add a role name and ``SecurityConfiguration`` name (in other words,
                                ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that
                                security configuration is used to encrypt the log group.

                              - **NotificationProperty** *(dict) --*

                                Specifies configuration properties of a job run notification.

                                - **NotifyDelayAfter** *(integer) --*

                                  After a job run starts, the number of minutes to wait before sending a
                                  job run delay notification.

                              - **GlueVersion** *(string) --*

                                Glue version determines the versions of Apache Spark and Python that AWS
                                Glue supports. The Python version indicates the version supported for jobs
                                of type Spark.

                                For more information about the available AWS Glue versions and
                                corresponding Spark and Python versions, see `Glue version
                                <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the
                                developer guide.

                                Jobs that are created without specifying a Glue version default to Glue 0.9.

                        - **CrawlerDetails** *(dict) --*

                          Details of the crawler when the node represents a crawler.

                          - **Crawls** *(list) --*

                            A list of crawls represented by the crawl node.

                            - *(dict) --*

                              The details of a crawl in the workflow.

                              - **State** *(string) --*

                                The state of the crawler.

                              - **StartedOn** *(datetime) --*

                                The date and time on which the crawl started.

                              - **CompletedOn** *(datetime) --*

                                The date and time on which the crawl completed.

                              - **ErrorMessage** *(string) --*

                                The error message associated with the crawl.

                              - **LogGroup** *(string) --*

                                The log group associated with the crawl.

                              - **LogStream** *(string) --*

                                The log stream associated with the crawl.

                    - **Edges** *(list) --*

                      A list of all the directed connections between the nodes belonging to the workflow.

                      - *(dict) --*

                        An edge represents a directed connection between two AWS Glue components which are
                        part of the workflow the edge belongs to.

                        - **SourceId** *(string) --*

                          The unique of the node within the workflow where the edge starts.

                        - **DestinationId** *(string) --*

                          The unique of the node within the workflow where the edge ends.

                - **Graph** *(dict) --*

                  The graph representing all the AWS Glue components that belong to the workflow as nodes
                  and directed connections between them as edges.

                  - **Nodes** *(list) --*

                    A list of the the AWS Glue components belong to the workflow represented as nodes.

                    - *(dict) --*

                      A node represents an AWS Glue component like Trigger, Job etc. which is part of a
                      workflow.

                      - **Type** *(string) --*

                        The type of AWS Glue component represented by the node.

                      - **Name** *(string) --*

                        The name of the AWS Glue component represented by the node.

                      - **UniqueId** *(string) --*

                        The unique Id assigned to the node within the workflow.

                      - **TriggerDetails** *(dict) --*

                        Details of the Trigger when the node represents a Trigger.

                        - **Trigger** *(dict) --*

                          The information of the trigger represented by the trigger node.

                          - **Name** *(string) --*

                            The name of the trigger.

                          - **WorkflowName** *(string) --*

                            The name of the workflow associated with the trigger.

                          - **Id** *(string) --*

                            Reserved for future use.

                          - **Type** *(string) --*

                            The type of trigger that this is.

                          - **State** *(string) --*

                            The current state of the trigger.

                          - **Description** *(string) --*

                            A description of this trigger.

                          - **Schedule** *(string) --*

                            A ``cron`` expression used to specify the schedule (see `Time-Based Schedules
                            for Jobs and Crawlers
                            <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__
                            . For example, to run something every day at 12:15 UTC, you would specify:
                            ``cron(15 12 * * ? *)`` .

                          - **Actions** *(list) --*

                            The actions initiated by this trigger.

                            - *(dict) --*

                              Defines an action to be initiated by a trigger.

                              - **JobName** *(string) --*

                                The name of a job to be executed.

                              - **Arguments** *(dict) --*

                                The job arguments used when this trigger fires. For this job run, they
                                replace the default arguments set in the job definition itself.

                                You can specify arguments here that your own job-execution script consumes,
                                as well as arguments that AWS Glue itself consumes.

                                For information about how to specify and consume your own Job arguments,
                                see the `Calling AWS Glue APIs in Python
                                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                                topic in the developer guide.

                                For information about the key-value pairs that AWS Glue consumes to set up
                                your job, see the `Special Parameters Used by AWS Glue
                                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                                topic in the developer guide.

                                - *(string) --*

                                  - *(string) --*

                              - **Timeout** *(integer) --*

                                The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                                can consume resources before it is terminated and enters ``TIMEOUT``
                                status. The default is 2,880 minutes (48 hours). This overrides the timeout
                                value set in the parent job.

                              - **SecurityConfiguration** *(string) --*

                                The name of the ``SecurityConfiguration`` structure to be used with this
                                action.

                              - **NotificationProperty** *(dict) --*

                                Specifies configuration properties of a job run notification.

                                - **NotifyDelayAfter** *(integer) --*

                                  After a job run starts, the number of minutes to wait before sending a
                                  job run delay notification.

                              - **CrawlerName** *(string) --*

                                The name of the crawler to be used with this action.

                          - **Predicate** *(dict) --*

                            The predicate of this trigger, which defines when it will fire.

                            - **Logical** *(string) --*

                              An optional field if only one condition is listed. If multiple conditions are
                              listed, then this field is required.

                            - **Conditions** *(list) --*

                              A list of the conditions that determine when the trigger will fire.

                              - *(dict) --*

                                Defines a condition under which a trigger fires.

                                - **LogicalOperator** *(string) --*

                                  A logical operator.

                                - **JobName** *(string) --*

                                  The name of the job whose ``JobRuns`` this condition applies to, and on
                                  which this trigger waits.

                                - **State** *(string) --*

                                  The condition state. Currently, the values supported are ``SUCCEEDED`` ,
                                  ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                                - **CrawlerName** *(string) --*

                                  The name of the crawler to which this condition applies.

                                - **CrawlState** *(string) --*

                                  The state of the crawler to which this condition applies.

                      - **JobDetails** *(dict) --*

                        Details of the Job when the node represents a Job.

                        - **JobRuns** *(list) --*

                          The information for the job runs represented by the job node.

                          - *(dict) --*

                            Contains information about a job run.

                            - **Id** *(string) --*

                              The ID of this job run.

                            - **Attempt** *(integer) --*

                              The number of the attempt to run this job.

                            - **PreviousRunId** *(string) --*

                              The ID of the previous run of this job. For example, the ``JobRunId``
                              specified in the ``StartJobRun`` action.

                            - **TriggerName** *(string) --*

                              The name of the trigger that started this job run.

                            - **JobName** *(string) --*

                              The name of the job definition being used in this run.

                            - **StartedOn** *(datetime) --*

                              The date and time at which this job run was started.

                            - **LastModifiedOn** *(datetime) --*

                              The last time that this job run was modified.

                            - **CompletedOn** *(datetime) --*

                              The date and time that this job run completed.

                            - **JobRunState** *(string) --*

                              The current state of the job run.

                            - **Arguments** *(dict) --*

                              The job arguments associated with this run. For this job run, they replace
                              the default arguments set in the job definition itself.

                              You can specify arguments here that your own job-execution script consumes,
                              as well as arguments that AWS Glue itself consumes.

                              For information about how to specify and consume your own job arguments, see
                              the `Calling AWS Glue APIs in Python
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                              topic in the developer guide.

                              For information about the key-value pairs that AWS Glue consumes to set up
                              your job, see the `Special Parameters Used by AWS Glue
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                              topic in the developer guide.

                              - *(string) --*

                                - *(string) --*

                            - **ErrorMessage** *(string) --*

                              An error message associated with this job run.

                            - **PredecessorRuns** *(list) --*

                              A list of predecessors to this job run.

                              - *(dict) --*

                                A job run that was used in the predicate of a conditional trigger that
                                triggered this job run.

                                - **JobName** *(string) --*

                                  The name of the job definition used by the predecessor job run.

                                - **RunId** *(string) --*

                                  The job-run ID of the predecessor job run.

                            - **AllocatedCapacity** *(integer) --*

                              This field is deprecated. Use ``MaxCapacity`` instead.

                              The number of AWS Glue data processing units (DPUs) allocated to this JobRun.
                              From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative
                              measure of processing power that consists of 4 vCPUs of compute capacity and
                              16 GB of memory. For more information, see the `AWS Glue pricing page
                              <https://aws.amazon.com/glue/pricing/>`__ .

                            - **ExecutionTime** *(integer) --*

                              The amount of time (in seconds) that the job run consumed resources.

                            - **Timeout** *(integer) --*

                              The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                              can consume resources before it is terminated and enters ``TIMEOUT`` status.
                              The default is 2,880 minutes (48 hours). This overrides the timeout value set
                              in the parent job.

                            - **MaxCapacity** *(float) --*

                              The number of AWS Glue data processing units (DPUs) that can be allocated
                              when this job runs. A DPU is a relative measure of processing power that
                              consists of 4 vCPUs of compute capacity and 16 GB of memory. For more
                              information, see the `AWS Glue pricing page
                              <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                              Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                              The value that can be allocated for ``MaxCapacity`` depends on whether you
                              are running a Python shell job or an Apache Spark ETL job:

                              * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"),
                              you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                              * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"),
                              you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type
                              cannot have a fractional DPU allocation.

                            - **WorkerType** *(string) --*

                              The type of predefined worker that is allocated when a job runs. Accepts a
                              value of Standard, G.1X, or G.2X.

                              * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of
                              memory and a 50GB disk, and 2 executors per worker.

                              * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory
                              and a 64GB disk, and 1 executor per worker.

                              * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory
                              and a 128GB disk, and 1 executor per worker.

                            - **NumberOfWorkers** *(integer) --*

                              The number of workers of a defined ``workerType`` that are allocated when a
                              job runs.

                              The maximum number of workers you can define are 299 for ``G.1X`` , and 149
                              for ``G.2X`` .

                            - **SecurityConfiguration** *(string) --*

                              The name of the ``SecurityConfiguration`` structure to be used with this job
                              run.

                            - **LogGroupName** *(string) --*

                              The name of the log group for secure logging that can be server-side
                              encrypted in Amazon CloudWatch using AWS KMS. This name can be
                              ``/aws-glue/jobs/`` , in which case the default encryption is ``NONE`` . If
                              you add a role name and ``SecurityConfiguration`` name (in other words,
                              ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that
                              security configuration is used to encrypt the log group.

                            - **NotificationProperty** *(dict) --*

                              Specifies configuration properties of a job run notification.

                              - **NotifyDelayAfter** *(integer) --*

                                After a job run starts, the number of minutes to wait before sending a job
                                run delay notification.

                            - **GlueVersion** *(string) --*

                              Glue version determines the versions of Apache Spark and Python that AWS Glue
                              supports. The Python version indicates the version supported for jobs of type
                              Spark.

                              For more information about the available AWS Glue versions and corresponding
                              Spark and Python versions, see `Glue version
                              <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer
                              guide.

                              Jobs that are created without specifying a Glue version default to Glue 0.9.

                      - **CrawlerDetails** *(dict) --*

                        Details of the crawler when the node represents a crawler.

                        - **Crawls** *(list) --*

                          A list of crawls represented by the crawl node.

                          - *(dict) --*

                            The details of a crawl in the workflow.

                            - **State** *(string) --*

                              The state of the crawler.

                            - **StartedOn** *(datetime) --*

                              The date and time on which the crawl started.

                            - **CompletedOn** *(datetime) --*

                              The date and time on which the crawl completed.

                            - **ErrorMessage** *(string) --*

                              The error message associated with the crawl.

                            - **LogGroup** *(string) --*

                              The log group associated with the crawl.

                            - **LogStream** *(string) --*

                              The log stream associated with the crawl.

                  - **Edges** *(list) --*

                    A list of all the directed connections between the nodes belonging to the workflow.

                    - *(dict) --*

                      An edge represents a directed connection between two AWS Glue components which are
                      part of the workflow the edge belongs to.

                      - **SourceId** *(string) --*

                        The unique of the node within the workflow where the edge starts.

                      - **DestinationId** *(string) --*

                        The unique of the node within the workflow where the edge ends.

            - **MissingWorkflows** *(list) --*

              A list of names of workflows not found.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_stop_job_run(
        self, JobName: str, JobRunIds: List[str]
    ) -> ClientBatchStopJobRunResponseTypeDef:
        """
        Stops one or more job runs for a specified job definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchStopJobRun>`_

        **Request Syntax**
        ::

          response = client.batch_stop_job_run(
              JobName='string',
              JobRunIds=[
                  'string',
              ]
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job definition for which to stop job runs.

        :type JobRunIds: list
        :param JobRunIds: **[REQUIRED]**

          A list of the ``JobRunIds`` that should be stopped for that job definition.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SuccessfulSubmissions': [
                    {
                        'JobName': 'string',
                        'JobRunId': 'string'
                    },
                ],
                'Errors': [
                    {
                        'JobName': 'string',
                        'JobRunId': 'string',
                        'ErrorDetail': {
                            'ErrorCode': 'string',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **SuccessfulSubmissions** *(list) --*

              A list of the JobRuns that were successfully submitted for stopping.

              - *(dict) --*

                Records a successful request to stop a specified ``JobRun`` .

                - **JobName** *(string) --*

                  The name of the job definition used in the job run that was stopped.

                - **JobRunId** *(string) --*

                  The ``JobRunId`` of the job run that was stopped.

            - **Errors** *(list) --*

              A list of the errors that were encountered in trying to stop ``JobRuns`` , including the
              ``JobRunId`` for which each error was encountered and details about the error.

              - *(dict) --*

                Records an error that occurred when attempting to stop a specified job run.

                - **JobName** *(string) --*

                  The name of the job definition that is used in the job run in question.

                - **JobRunId** *(string) --*

                  The ``JobRunId`` of the job run in question.

                - **ErrorDetail** *(dict) --*

                  Specifies details about the error that was encountered.

                  - **ErrorCode** *(string) --*

                    The code associated with this error.

                  - **ErrorMessage** *(string) --*

                    A message describing the error.

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
    def cancel_ml_task_run(
        self, TransformId: str, TaskRunId: str
    ) -> ClientCancelMlTaskRunResponseTypeDef:
        """
        Cancels (stops) a task run. Machine learning task runs are asynchronous tasks that AWS Glue runs on
        your behalf as part of various machine learning workflows. You can cancel a machine learning task
        run at any time by calling ``CancelMLTaskRun`` with a task run's parent transform's ``TransformID``
        and the task run's ``TaskRunId`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CancelMLTaskRun>`_

        **Request Syntax**
        ::

          response = client.cancel_ml_task_run(
              TransformId='string',
              TaskRunId='string'
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the machine learning transform.

        :type TaskRunId: string
        :param TaskRunId: **[REQUIRED]**

          A unique identifier for the task run.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TransformId': 'string',
                'TaskRunId': 'string',
                'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT'
            }
          **Response Structure**

          - *(dict) --*

            - **TransformId** *(string) --*

              The unique identifier of the machine learning transform.

            - **TaskRunId** *(string) --*

              The unique identifier for the task run.

            - **Status** *(string) --*

              The status for this run.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_classifier(
        self,
        GrokClassifier: ClientCreateClassifierGrokClassifierTypeDef = None,
        XMLClassifier: ClientCreateClassifierXMLClassifierTypeDef = None,
        JsonClassifier: ClientCreateClassifierJsonClassifierTypeDef = None,
        CsvClassifier: ClientCreateClassifierCsvClassifierTypeDef = None,
    ) -> Dict[str, Any]:
        """
        Creates a classifier in the user's account. This can be a ``GrokClassifier`` , an ``XMLClassifier``
        , a ``JsonClassifier`` , or a ``CsvClassifier`` , depending on which field of the request is
        present.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateClassifier>`_

        **Request Syntax**
        ::

          response = client.create_classifier(
              GrokClassifier={
                  'Classification': 'string',
                  'Name': 'string',
                  'GrokPattern': 'string',
                  'CustomPatterns': 'string'
              },
              XMLClassifier={
                  'Classification': 'string',
                  'Name': 'string',
                  'RowTag': 'string'
              },
              JsonClassifier={
                  'Name': 'string',
                  'JsonPath': 'string'
              },
              CsvClassifier={
                  'Name': 'string',
                  'Delimiter': 'string',
                  'QuoteSymbol': 'string',
                  'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
                  'Header': [
                      'string',
                  ],
                  'DisableValueTrimming': True|False,
                  'AllowSingleColumn': True|False
              }
          )
        :type GrokClassifier: dict
        :param GrokClassifier:

          A ``GrokClassifier`` object specifying the classifier to create.

          - **Classification** *(string) --* **[REQUIRED]**

            An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture
            logs, Amazon CloudWatch Logs, and so on.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the new classifier.

          - **GrokPattern** *(string) --* **[REQUIRED]**

            The grok pattern used by this classifier.

          - **CustomPatterns** *(string) --*

            Optional custom grok patterns used by this classifier.

        :type XMLClassifier: dict
        :param XMLClassifier:

          An ``XMLClassifier`` object specifying the classifier to create.

          - **Classification** *(string) --* **[REQUIRED]**

            An identifier of the data format that the classifier matches.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the classifier.

          - **RowTag** *(string) --*

            The XML tag designating the element that contains each record in an XML document being parsed.
            This can't identify a self-closing element (closed by ``/>`` ). An empty row element that
            contains only attributes can be parsed as long as it ends with a closing tag (for example,
            ``<row item_a="A" item_b="B"></row>`` is okay, but ``<row item_a="A" item_b="B" />`` is not).

        :type JsonClassifier: dict
        :param JsonClassifier:

          A ``JsonClassifier`` object specifying the classifier to create.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the classifier.

          - **JsonPath** *(string) --* **[REQUIRED]**

            A ``JsonPath`` string defining the JSON data for the classifier to classify. AWS Glue supports
            a subset of ``JsonPath`` , as described in `Writing JsonPath Custom Classifiers
            <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json>`__ .

        :type CsvClassifier: dict
        :param CsvClassifier:

          A ``CsvClassifier`` object specifying the classifier to create.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the classifier.

          - **Delimiter** *(string) --*

            A custom symbol to denote what separates each column entry in the row.

          - **QuoteSymbol** *(string) --*

            A custom symbol to denote what combines content into a single column value. Must be different
            from the column delimiter.

          - **ContainsHeader** *(string) --*

            Indicates whether the CSV file contains a header.

          - **Header** *(list) --*

            A list of strings representing column names.

            - *(string) --*

          - **DisableValueTrimming** *(boolean) --*

            Specifies not to trim values before identifying the type of column values. The default value is
            true.

          - **AllowSingleColumn** *(boolean) --*

            Enables the processing of files that contain only one column.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_connection(
        self,
        ConnectionInput: ClientCreateConnectionConnectionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Creates a connection definition in the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateConnection>`_

        **Request Syntax**
        ::

          response = client.create_connection(
              CatalogId='string',
              ConnectionInput={
                  'Name': 'string',
                  'Description': 'string',
                  'ConnectionType': 'JDBC'|'SFTP',
                  'MatchCriteria': [
                      'string',
                  ],
                  'ConnectionProperties': {
                      'string': 'string'
                  },
                  'PhysicalConnectionRequirements': {
                      'SubnetId': 'string',
                      'SecurityGroupIdList': [
                          'string',
                      ],
                      'AvailabilityZone': 'string'
                  }
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which to create the connection. If none is provided, the AWS
          account ID is used by default.

        :type ConnectionInput: dict
        :param ConnectionInput: **[REQUIRED]**

          A ``ConnectionInput`` object defining the connection to create.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the connection.

          - **Description** *(string) --*

            The description of the connection.

          - **ConnectionType** *(string) --* **[REQUIRED]**

            The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

          - **MatchCriteria** *(list) --*

            A list of criteria that can be used in selecting this connection.

            - *(string) --*

          - **ConnectionProperties** *(dict) --* **[REQUIRED]**

            These key-value pairs define parameters for the connection.

            - *(string) --*

              - *(string) --*

          - **PhysicalConnectionRequirements** *(dict) --*

            A map of physical connection requirements, such as virtual private cloud (VPC) and
            ``SecurityGroup`` , that are needed to successfully make this connection.

            - **SubnetId** *(string) --*

              The subnet ID used by the connection.

            - **SecurityGroupIdList** *(list) --*

              The security group ID list used by the connection.

              - *(string) --*

            - **AvailabilityZone** *(string) --*

              The connection's Availability Zone. This field is redundant because the specified subnet
              implies the Availability Zone to be used. Currently the field must be populated, but it will
              be deprecated in the future.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_crawler(
        self,
        Name: str,
        Role: str,
        Targets: ClientCreateCrawlerTargetsTypeDef,
        DatabaseName: str = None,
        Description: str = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: ClientCreateCrawlerSchemaChangePolicyTypeDef = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
        Tags: List[str] = None,
    ) -> Dict[str, Any]:
        """
        Creates a new crawler with specified targets, role, configuration, and optional schedule. At least
        one crawl target must be specified, in the ``s3Targets`` field, the ``jdbcTargets`` field, or the
        ``DynamoDBTargets`` field.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateCrawler>`_

        **Request Syntax**
        ::

          response = client.create_crawler(
              Name='string',
              Role='string',
              DatabaseName='string',
              Description='string',
              Targets={
                  'S3Targets': [
                      {
                          'Path': 'string',
                          'Exclusions': [
                              'string',
                          ]
                      },
                  ],
                  'JdbcTargets': [
                      {
                          'ConnectionName': 'string',
                          'Path': 'string',
                          'Exclusions': [
                              'string',
                          ]
                      },
                  ],
                  'DynamoDBTargets': [
                      {
                          'Path': 'string'
                      },
                  ],
                  'CatalogTargets': [
                      {
                          'DatabaseName': 'string',
                          'Tables': [
                              'string',
                          ]
                      },
                  ]
              },
              Schedule='string',
              Classifiers=[
                  'string',
              ],
              TablePrefix='string',
              SchemaChangePolicy={
                  'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                  'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
              },
              Configuration='string',
              CrawlerSecurityConfiguration='string',
              Tags={
                  'string': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the new crawler.

        :type Role: string
        :param Role: **[REQUIRED]**

          The IAM role or Amazon Resource Name (ARN) of an IAM role used by the new crawler to access
          customer resources.

        :type DatabaseName: string
        :param DatabaseName:

          The AWS Glue database where results are written, such as:
          ``arn:aws:daylight:us-east-1::database/sometable/*`` .

        :type Description: string
        :param Description:

          A description of the new crawler.

        :type Targets: dict
        :param Targets: **[REQUIRED]**

          A list of collection of targets to crawl.

          - **S3Targets** *(list) --*

            Specifies Amazon Simple Storage Service (Amazon S3) targets.

            - *(dict) --*

              Specifies a data store in Amazon Simple Storage Service (Amazon S3).

              - **Path** *(string) --*

                The path to the Amazon S3 target.

              - **Exclusions** *(list) --*

                A list of glob patterns used to exclude from the crawl. For more information, see `Catalog
                Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                - *(string) --*

          - **JdbcTargets** *(list) --*

            Specifies JDBC targets.

            - *(dict) --*

              Specifies a JDBC data store to crawl.

              - **ConnectionName** *(string) --*

                The name of the connection to use to connect to the JDBC target.

              - **Path** *(string) --*

                The path of the JDBC target.

              - **Exclusions** *(list) --*

                A list of glob patterns used to exclude from the crawl. For more information, see `Catalog
                Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                - *(string) --*

          - **DynamoDBTargets** *(list) --*

            Specifies Amazon DynamoDB targets.

            - *(dict) --*

              Specifies an Amazon DynamoDB table to crawl.

              - **Path** *(string) --*

                The name of the DynamoDB table to crawl.

          - **CatalogTargets** *(list) --*

            Specifies AWS Glue Data Catalog targets.

            - *(dict) --*

              Specifies an AWS Glue Data Catalog target.

              - **DatabaseName** *(string) --* **[REQUIRED]**

                The name of the database to be synchronized.

              - **Tables** *(list) --* **[REQUIRED]**

                A list of the tables to be synchronized.

                - *(string) --*

        :type Schedule: string
        :param Schedule:

          A ``cron`` expression used to specify the schedule. For more information, see `Time-Based
          Schedules for Jobs and Crawlers
          <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For
          example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

        :type Classifiers: list
        :param Classifiers:

          A list of custom classifiers that the user has registered. By default, all built-in classifiers
          are included in a crawl, but these custom classifiers always override the default classifiers for
          a given classification.

          - *(string) --*

        :type TablePrefix: string
        :param TablePrefix:

          The table prefix used for catalog tables that are created.

        :type SchemaChangePolicy: dict
        :param SchemaChangePolicy:

          The policy for the crawler's update and deletion behavior.

          - **UpdateBehavior** *(string) --*

            The update behavior when the crawler finds a changed schema.

          - **DeleteBehavior** *(string) --*

            The deletion behavior when the crawler finds a deleted object.

        :type Configuration: string
        :param Configuration:

          The crawler configuration information. This versioned JSON string allows users to specify aspects
          of a crawler's behavior. For more information, see `Configuring a Crawler
          <http://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`__ .

        :type CrawlerSecurityConfiguration: string
        :param CrawlerSecurityConfiguration:

          The name of the ``SecurityConfiguration`` structure to be used by this crawler.

        :type Tags: dict
        :param Tags:

          The tags to use with this crawler request. You can use tags to limit access to the crawler. For
          more information, see `AWS Tags in AWS Glue
          <http://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`__ .

          - *(string) --*

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
    def create_database(
        self,
        DatabaseInput: ClientCreateDatabaseDatabaseInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Creates a new database in a Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateDatabase>`_

        **Request Syntax**
        ::

          response = client.create_database(
              CatalogId='string',
              DatabaseInput={
                  'Name': 'string',
                  'Description': 'string',
                  'LocationUri': 'string',
                  'Parameters': {
                      'string': 'string'
                  },
                  'CreateTableDefaultPermissions': [
                      {
                          'Principal': {
                              'DataLakePrincipalIdentifier': 'string'
                          },
                          'Permissions': [
                              'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                              |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                          ]
                      },
                  ]
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which to create the database. If none is provided, the AWS account
          ID is used by default.

        :type DatabaseInput: dict
        :param DatabaseInput: **[REQUIRED]**

          The metadata for the database.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.

          - **Description** *(string) --*

            A description of the database.

          - **LocationUri** *(string) --*

            The location of the database (for example, an HDFS path).

          - **Parameters** *(dict) --*

            These key-value pairs define parameters and properties of the database.

            These key-value pairs define parameters and properties of the database.

            - *(string) --*

              - *(string) --*

          - **CreateTableDefaultPermissions** *(list) --*

            Creates a set of default permissions on the table for principals.

            - *(dict) --*

              Permissions granted to a principal.

              - **Principal** *(dict) --*

                The principal who is granted permissions.

                - **DataLakePrincipalIdentifier** *(string) --*

                  An identifier for the AWS Lake Formation principal.

              - **Permissions** *(list) --*

                The permissions that are granted to the principal.

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
    def create_dev_endpoint(
        self,
        EndpointName: str,
        RoleArn: str,
        SecurityGroupIds: List[str] = None,
        SubnetId: str = None,
        PublicKey: str = None,
        PublicKeys: List[str] = None,
        NumberOfNodes: int = None,
        WorkerType: str = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        ExtraPythonLibsS3Path: str = None,
        ExtraJarsS3Path: str = None,
        SecurityConfiguration: str = None,
        Tags: List[str] = None,
        Arguments: Dict[str, str] = None,
    ) -> ClientCreateDevEndpointResponseTypeDef:
        """
        Creates a new development endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateDevEndpoint>`_

        **Request Syntax**
        ::

          response = client.create_dev_endpoint(
              EndpointName='string',
              RoleArn='string',
              SecurityGroupIds=[
                  'string',
              ],
              SubnetId='string',
              PublicKey='string',
              PublicKeys=[
                  'string',
              ],
              NumberOfNodes=123,
              WorkerType='Standard'|'G.1X'|'G.2X',
              GlueVersion='string',
              NumberOfWorkers=123,
              ExtraPythonLibsS3Path='string',
              ExtraJarsS3Path='string',
              SecurityConfiguration='string',
              Tags={
                  'string': 'string'
              },
              Arguments={
                  'string': 'string'
              }
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**

          The name to be assigned to the new ``DevEndpoint`` .

        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**

          The IAM role for the ``DevEndpoint`` .

        :type SecurityGroupIds: list
        :param SecurityGroupIds:

          Security group IDs for the security groups to be used by the new ``DevEndpoint`` .

          - *(string) --*

        :type SubnetId: string
        :param SubnetId:

          The subnet ID for the new ``DevEndpoint`` to use.

        :type PublicKey: string
        :param PublicKey:

          The public key to be used by this ``DevEndpoint`` for authentication. This attribute is provided
          for backward compatibility because the recommended attribute to use is public keys.

        :type PublicKeys: list
        :param PublicKeys:

          A list of public keys to be used by the development endpoints for authentication. The use of this
          attribute is preferred over a single public key because the public keys allow you to have a
          different private key per client.

          .. note::

            If you previously created an endpoint with a public key, you must remove that key to be able to
            set a list of public keys. Call the ``UpdateDevEndpoint`` API with the public key content in
            the ``deletePublicKeys`` attribute, and the list of new keys in the ``addPublicKeys`` attribute.

          - *(string) --*

        :type NumberOfNodes: integer
        :param NumberOfNodes:

          The number of AWS Glue Data Processing Units (DPUs) to allocate to this ``DevEndpoint`` .

        :type WorkerType: string
        :param WorkerType:

          The type of predefined worker that is allocated to the development endpoint. Accepts a value of
          Standard, G.1X, or G.2X.

          * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk,
          and 2 executors per worker.

          * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk),
          and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

          * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk),
          and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

          Known issue: when a development endpoint is created with the ``G.2X``  ``WorkerType``
          configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of
          memory, and a 64 GB disk.

        :type GlueVersion: string
        :param GlueVersion:

          Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The
          Python version indicates the version supported for running your ETL scripts on development
          endpoints.

          For more information about the available AWS Glue versions and corresponding Spark and Python
          versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the
          developer guide.

          Development endpoints that are created without specifying a Glue version default to Glue 0.9.

          You can specify a version of Python support for development endpoints by using the ``Arguments``
          parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no arguments are
          provided, the version defaults to Python 2.

        :type NumberOfWorkers: integer
        :param NumberOfWorkers:

          The number of workers of a defined ``workerType`` that are allocated to the development endpoint.

          The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

        :type ExtraPythonLibsS3Path: string
        :param ExtraPythonLibsS3Path:

          The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your
          ``DevEndpoint`` . Multiple values must be complete paths separated by a comma.

          .. note::

            You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on C
            extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis library,
            are not yet supported.

        :type ExtraJarsS3Path: string
        :param ExtraJarsS3Path:

          The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your
          ``DevEndpoint`` .

        :type SecurityConfiguration: string
        :param SecurityConfiguration:

          The name of the ``SecurityConfiguration`` structure to be used with this ``DevEndpoint`` .

        :type Tags: dict
        :param Tags:

          The tags to use with this DevEndpoint. You may use tags to limit access to the DevEndpoint. For
          more information about tags in AWS Glue, see `AWS Tags in AWS Glue
          <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`__ in the developer guide.

          - *(string) --*

            - *(string) --*

        :type Arguments: dict
        :param Arguments:

          A map of arguments used to configure the ``DevEndpoint`` .

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EndpointName': 'string',
                'Status': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string',
                'RoleArn': 'string',
                'YarnEndpointAddress': 'string',
                'ZeppelinRemoteSparkInterpreterPort': 123,
                'NumberOfNodes': 123,
                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                'GlueVersion': 'string',
                'NumberOfWorkers': 123,
                'AvailabilityZone': 'string',
                'VpcId': 'string',
                'ExtraPythonLibsS3Path': 'string',
                'ExtraJarsS3Path': 'string',
                'FailureReason': 'string',
                'SecurityConfiguration': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'Arguments': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EndpointName** *(string) --*

              The name assigned to the new ``DevEndpoint`` .

            - **Status** *(string) --*

              The current status of the new ``DevEndpoint`` .

            - **SecurityGroupIds** *(list) --*

              The security groups assigned to the new ``DevEndpoint`` .

              - *(string) --*

            - **SubnetId** *(string) --*

              The subnet ID assigned to the new ``DevEndpoint`` .

            - **RoleArn** *(string) --*

              The Amazon Resource Name (ARN) of the role assigned to the new ``DevEndpoint`` .

            - **YarnEndpointAddress** *(string) --*

              The address of the YARN endpoint used by this ``DevEndpoint`` .

            - **ZeppelinRemoteSparkInterpreterPort** *(integer) --*

              The Apache Zeppelin port for the remote Apache Spark interpreter.

            - **NumberOfNodes** *(integer) --*

              The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint.

            - **WorkerType** *(string) --*

              The type of predefined worker that is allocated to the development endpoint. May be a value
              of Standard, G.1X, or G.2X.

            - **GlueVersion** *(string) --*

              Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The
              Python version indicates the version supported for running your ETL scripts on development
              endpoints.

            - **NumberOfWorkers** *(integer) --*

              The number of workers of a defined ``workerType`` that are allocated to the development
              endpoint.

            - **AvailabilityZone** *(string) --*

              The AWS Availability Zone where this ``DevEndpoint`` is located.

            - **VpcId** *(string) --*

              The ID of the virtual private cloud (VPC) used by this ``DevEndpoint`` .

            - **ExtraPythonLibsS3Path** *(string) --*

              The paths to one or more Python libraries in an S3 bucket that will be loaded in your
              ``DevEndpoint`` .

            - **ExtraJarsS3Path** *(string) --*

              Path to one or more Java ``.jar`` files in an S3 bucket that will be loaded in your
              ``DevEndpoint`` .

            - **FailureReason** *(string) --*

              The reason for a current failure in this ``DevEndpoint`` .

            - **SecurityConfiguration** *(string) --*

              The name of the ``SecurityConfiguration`` structure being used with this ``DevEndpoint`` .

            - **CreatedTimestamp** *(datetime) --*

              The point in time at which this ``DevEndpoint`` was created.

            - **Arguments** *(dict) --*

              The map of arguments used to configure this ``DevEndpoint`` .

              Valid arguments are:

              * ``"--enable-glue-datacatalog": ""``

              * ``"GLUE_PYTHON_VERSION": "3"``

              * ``"GLUE_PYTHON_VERSION": "2"``

              You can specify a version of Python support for development endpoints by using the
              ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no
              arguments are provided, the version defaults to Python 2.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        Name: str,
        Role: str,
        Command: ClientCreateJobCommandTypeDef,
        Description: str = None,
        LogUri: str = None,
        ExecutionProperty: ClientCreateJobExecutionPropertyTypeDef = None,
        DefaultArguments: Dict[str, str] = None,
        Connections: ClientCreateJobConnectionsTypeDef = None,
        MaxRetries: int = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        Tags: List[str] = None,
        NotificationProperty: ClientCreateJobNotificationPropertyTypeDef = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        WorkerType: str = None,
    ) -> ClientCreateJobResponseTypeDef:
        """
        Creates a new job definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateJob>`_

        **Request Syntax**
        ::

          response = client.create_job(
              Name='string',
              Description='string',
              LogUri='string',
              Role='string',
              ExecutionProperty={
                  'MaxConcurrentRuns': 123
              },
              Command={
                  'Name': 'string',
                  'ScriptLocation': 'string',
                  'PythonVersion': 'string'
              },
              DefaultArguments={
                  'string': 'string'
              },
              Connections={
                  'Connections': [
                      'string',
                  ]
              },
              MaxRetries=123,
              AllocatedCapacity=123,
              Timeout=123,
              MaxCapacity=123.0,
              SecurityConfiguration='string',
              Tags={
                  'string': 'string'
              },
              NotificationProperty={
                  'NotifyDelayAfter': 123
              },
              GlueVersion='string',
              NumberOfWorkers=123,
              WorkerType='Standard'|'G.1X'|'G.2X'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name you assign to this job definition. It must be unique in your account.

        :type Description: string
        :param Description:

          Description of the job being defined.

        :type LogUri: string
        :param LogUri:

          This field is reserved for future use.

        :type Role: string
        :param Role: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

        :type ExecutionProperty: dict
        :param ExecutionProperty:

          An ``ExecutionProperty`` specifying the maximum number of concurrent runs allowed for this job.

          - **MaxConcurrentRuns** *(integer) --*

            The maximum number of concurrent runs allowed for the job. The default is 1. An error is
            returned when this threshold is reached. The maximum value you can specify is controlled by a
            service limit.

        :type Command: dict
        :param Command: **[REQUIRED]**

          The ``JobCommand`` that executes this job.

          - **Name** *(string) --*

            The name of the job command. For an Apache Spark ETL job, this must be ``glueetl`` . For a
            Python shell job, it must be ``pythonshell`` .

          - **ScriptLocation** *(string) --*

            Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job.

          - **PythonVersion** *(string) --*

            The Python version being used to execute a Python shell job. Allowed values are 2 or 3.

        :type DefaultArguments: dict
        :param DefaultArguments:

          The default arguments for this job.

          You can specify arguments here that your own job-execution script consumes, as well as arguments
          that AWS Glue itself consumes.

          For information about how to specify and consume your own Job arguments, see the `Calling AWS
          Glue APIs in Python
          <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__ topic in
          the developer guide.

          For information about the key-value pairs that AWS Glue consumes to set up your job, see the
          `Special Parameters Used by AWS Glue
          <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
          topic in the developer guide.

          - *(string) --*

            - *(string) --*

        :type Connections: dict
        :param Connections:

          The connections used for this job.

          - **Connections** *(list) --*

            A list of connections used by the job.

            - *(string) --*

        :type MaxRetries: integer
        :param MaxRetries:

          The maximum number of times to retry this job if it fails.

        :type AllocatedCapacity: integer
        :param AllocatedCapacity:

          This parameter is deprecated. Use ``MaxCapacity`` instead.

          The number of AWS Glue data processing units (DPUs) to allocate to this Job. You can allocate
          from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that
          consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS
          Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .

        :type Timeout: integer
        :param Timeout:

          The job timeout in minutes. This is the maximum time that a job run can consume resources before
          it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48 hours).

        :type MaxCapacity: float
        :param MaxCapacity:

          The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A
          DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16
          GB of memory. For more information, see the `AWS Glue pricing page
          <https://aws.amazon.com/glue/pricing/>`__ .

          Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

          The value that can be allocated for ``MaxCapacity`` depends on whether you are running a Python
          shell job or an Apache Spark ETL job:

          * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you can allocate
          either 0.0625 or 1 DPU. The default is 0.0625 DPU.

          * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"), you can allocate
          from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.

        :type SecurityConfiguration: string
        :param SecurityConfiguration:

          The name of the ``SecurityConfiguration`` structure to be used with this job.

        :type Tags: dict
        :param Tags:

          The tags to use with this job. You may use tags to limit access to the job. For more information
          about tags in AWS Glue, see `AWS Tags in AWS Glue
          <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`__ in the developer guide.

          - *(string) --*

            - *(string) --*

        :type NotificationProperty: dict
        :param NotificationProperty:

          Specifies configuration properties of a job notification.

          - **NotifyDelayAfter** *(integer) --*

            After a job run starts, the number of minutes to wait before sending a job run delay
            notification.

        :type GlueVersion: string
        :param GlueVersion:

          Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The
          Python version indicates the version supported for jobs of type Spark.

          For more information about the available AWS Glue versions and corresponding Spark and Python
          versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the
          developer guide.

          Jobs that are created without specifying a Glue version default to Glue 0.9.

        :type NumberOfWorkers: integer
        :param NumberOfWorkers:

          The number of workers of a defined ``workerType`` that are allocated when a job runs.

          The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

        :type WorkerType: string
        :param WorkerType:

          The type of predefined worker that is allocated when a job runs. Accepts a value of Standard,
          G.1X, or G.2X.

          * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk,
          and 2 executors per worker.

          * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk),
          and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

          * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk),
          and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The unique name that was provided for this job definition.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ml_transform(
        self,
        Name: str,
        InputRecordTables: List[ClientCreateMlTransformInputRecordTablesTypeDef],
        Parameters: ClientCreateMlTransformParametersTypeDef,
        Role: str,
        Description: str = None,
        MaxCapacity: float = None,
        WorkerType: str = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
    ) -> ClientCreateMlTransformResponseTypeDef:
        """
        Creates an AWS Glue machine learning transform. This operation creates the transform and all the
        necessary parameters to train it.

        Call this operation as the first step in the process of using a machine learning transform (such as
        the ``FindMatches`` transform) for deduplicating data. You can provide an optional ``Description``
        , in addition to the parameters that you want to use for your algorithm.

        You must also specify certain parameters for the tasks that AWS Glue runs on your behalf as part of
        learning from your data and creating a high-quality machine learning transform. These parameters
        include ``Role`` , and optionally, ``AllocatedCapacity`` , ``Timeout`` , and ``MaxRetries`` . For
        more information, see `Jobs
        <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateMLTransform>`_

        **Request Syntax**
        ::

          response = client.create_ml_transform(
              Name='string',
              Description='string',
              InputRecordTables=[
                  {
                      'DatabaseName': 'string',
                      'TableName': 'string',
                      'CatalogId': 'string',
                      'ConnectionName': 'string'
                  },
              ],
              Parameters={
                  'TransformType': 'FIND_MATCHES',
                  'FindMatchesParameters': {
                      'PrimaryKeyColumnName': 'string',
                      'PrecisionRecallTradeoff': 123.0,
                      'AccuracyCostTradeoff': 123.0,
                      'EnforceProvidedLabels': True|False
                  }
              },
              Role='string',
              MaxCapacity=123.0,
              WorkerType='Standard'|'G.1X'|'G.2X',
              NumberOfWorkers=123,
              Timeout=123,
              MaxRetries=123
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The unique name that you give the transform when you create it.

        :type Description: string
        :param Description:

          A description of the machine learning transform that is being defined. The default is an empty
          string.

        :type InputRecordTables: list
        :param InputRecordTables: **[REQUIRED]**

          A list of AWS Glue table definitions used by the transform.

          - *(dict) --*

            The database and table in the AWS Glue Data Catalog that is used for input or output data.

            - **DatabaseName** *(string) --* **[REQUIRED]**

              A database name in the AWS Glue Data Catalog.

            - **TableName** *(string) --* **[REQUIRED]**

              A table name in the AWS Glue Data Catalog.

            - **CatalogId** *(string) --*

              A unique identifier for the AWS Glue Data Catalog.

            - **ConnectionName** *(string) --*

              The name of the connection to the AWS Glue Data Catalog.

        :type Parameters: dict
        :param Parameters: **[REQUIRED]**

          The algorithmic parameters that are specific to the transform type used. Conditionally dependent
          on the transform type.

          - **TransformType** *(string) --* **[REQUIRED]**

            The type of machine learning transform.

            For information about the types of machine learning transforms, see `Creating Machine Learning
            Transforms
            <http://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html>`__ .

          - **FindMatchesParameters** *(dict) --*

            The parameters for the find matches algorithm.

            - **PrimaryKeyColumnName** *(string) --*

              The name of a column that uniquely identifies rows in the source table. Used to help identify
              matching records.

            - **PrecisionRecallTradeoff** *(float) --*

              The value selected when tuning your transform for a balance between precision and recall. A
              value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a
              value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to
              1.0 means very low recall, and choosing values close to 0.0 results in very low precision.

              The precision metric indicates how often your model is correct when it predicts a match.

              The recall metric indicates that for an actual match, how often your model predicts the match.

            - **AccuracyCostTradeoff** *(float) --*

              The value that is selected when tuning your transform for a balance between accuracy and
              cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of
              1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes
              substantially higher. A value of 0.0 means a bias purely for cost, which results in a less
              accurate ``FindMatches`` transform, sometimes with unacceptable accuracy.

              Accuracy measures how well the transform finds true positives and true negatives. Increasing
              accuracy requires more machine resources and cost. But it also results in increased recall.

              Cost measures how many compute resources, and thus money, are consumed to run the transform.

            - **EnforceProvidedLabels** *(boolean) --*

              The value to switch on or off to force the output to match the provided labels from users. If
              the value is ``True`` , the ``find matches`` transform forces the output to match the
              provided labels. The results override the normal conflation results. If the value is
              ``False`` , the ``find matches`` transform does not ensure all the labels provided are
              respected, and the results rely on the trained model.

              Note that setting this value to true may increase the conflation execution time.

        :type Role: string
        :param Role: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. Ensure that
          this role has permission to your Amazon Simple Storage Service (Amazon S3) sources, targets,
          temporary directory, scripts, and any libraries that are used by the task run for this transform.

        :type MaxCapacity: float
        :param MaxCapacity:

          The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this
          transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of
          processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more
          information, see the `AWS Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .

          When the ``WorkerType`` field is set to a value other than ``Standard`` , the ``MaxCapacity``
          field is set automatically and becomes read-only.

        :type WorkerType: string
        :param WorkerType:

          The type of predefined worker that is allocated when this task runs. Accepts a value of Standard,
          G.1X, or G.2X.

          * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk,
          and 2 executors per worker.

          * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and
          1 executor per worker.

          * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk,
          and 1 executor per worker.

        :type NumberOfWorkers: integer
        :param NumberOfWorkers:

          The number of workers of a defined ``workerType`` that are allocated when this task runs.

        :type Timeout: integer
        :param Timeout:

          The timeout of the task run for this transform in minutes. This is the maximum time that a task
          run for this transform can consume resources before it is terminated and enters ``TIMEOUT``
          status. The default is 2,880 minutes (48 hours).

        :type MaxRetries: integer
        :param MaxRetries:

          The maximum number of times to retry a task for this transform after a task run fails.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TransformId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TransformId** *(string) --*

              A unique identifier that is generated for the transform.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInput: ClientCreatePartitionPartitionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Creates a new partition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreatePartition>`_

        **Request Syntax**
        ::

          response = client.create_partition(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              PartitionInput={
                  'Values': [
                      'string',
                  ],
                  'LastAccessTime': datetime(2015, 1, 1),
                  'StorageDescriptor': {
                      'Columns': [
                          {
                              'Name': 'string',
                              'Type': 'string',
                              'Comment': 'string',
                              'Parameters': {
                                  'string': 'string'
                              }
                          },
                      ],
                      'Location': 'string',
                      'InputFormat': 'string',
                      'OutputFormat': 'string',
                      'Compressed': True|False,
                      'NumberOfBuckets': 123,
                      'SerdeInfo': {
                          'Name': 'string',
                          'SerializationLibrary': 'string',
                          'Parameters': {
                              'string': 'string'
                          }
                      },
                      'BucketColumns': [
                          'string',
                      ],
                      'SortColumns': [
                          {
                              'Column': 'string',
                              'SortOrder': 123
                          },
                      ],
                      'Parameters': {
                          'string': 'string'
                      },
                      'SkewedInfo': {
                          'SkewedColumnNames': [
                              'string',
                          ],
                          'SkewedColumnValues': [
                              'string',
                          ],
                          'SkewedColumnValueLocationMaps': {
                              'string': 'string'
                          }
                      },
                      'StoredAsSubDirectories': True|False
                  },
                  'Parameters': {
                      'string': 'string'
                  },
                  'LastAnalyzedTime': datetime(2015, 1, 1)
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The AWS account ID of the catalog in which the partition is to be created.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the metadata database in which the partition is to be created.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the metadata table in which the partition is to be created.

        :type PartitionInput: dict
        :param PartitionInput: **[REQUIRED]**

          A ``PartitionInput`` structure defining the partition to be created.

          - **Values** *(list) --*

            The values of the partition. Although this parameter is not required by the SDK, you must
            specify this parameter for a valid input.

            The values for the keys for the new partition must be passed as an array of String objects that
            must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix.
            Otherwise AWS Glue will add the values to the wrong keys.

            - *(string) --*

          - **LastAccessTime** *(datetime) --*

            The last time at which the partition was accessed.

          - **StorageDescriptor** *(dict) --*

            Provides information about the physical location where the partition is stored.

            - **Columns** *(list) --*

              A list of the ``Columns`` in the table.

              - *(dict) --*

                A column in a ``Table`` .

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the ``Column`` .

                - **Type** *(string) --*

                  The data type of the ``Column`` .

                - **Comment** *(string) --*

                  A free-form text comment.

                - **Parameters** *(dict) --*

                  These key-value pairs define properties associated with the column.

                  - *(string) --*

                    - *(string) --*

            - **Location** *(string) --*

              The physical location of the table. By default, this takes the form of the warehouse
              location, followed by the database location in the warehouse, followed by the table name.

            - **InputFormat** *(string) --*

              The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom
              format.

            - **OutputFormat** *(string) --*

              The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` ,
              or a custom format.

            - **Compressed** *(boolean) --*

               ``True`` if the data in the table is compressed, or ``False`` if not.

            - **NumberOfBuckets** *(integer) --*

              Must be specified if the table contains any dimension columns.

            - **SerdeInfo** *(dict) --*

              The serialization/deserialization (SerDe) information.

              - **Name** *(string) --*

                Name of the SerDe.

              - **SerializationLibrary** *(string) --*

                Usually the class that implements the SerDe. An example is
                ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

              - **Parameters** *(dict) --*

                These key-value pairs define initialization parameters for the SerDe.

                - *(string) --*

                  - *(string) --*

            - **BucketColumns** *(list) --*

              A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

              - *(string) --*

            - **SortColumns** *(list) --*

              A list specifying the sort order of each bucket in the table.

              - *(dict) --*

                Specifies the sort order of a sorted column.

                - **Column** *(string) --* **[REQUIRED]**

                  The name of the column.

                - **SortOrder** *(integer) --* **[REQUIRED]**

                  Indicates that the column is sorted in ascending order (``== 1`` ), or in descending
                  order (``==0`` ).

            - **Parameters** *(dict) --*

              The user-supplied properties in key-value form.

              - *(string) --*

                - *(string) --*

            - **SkewedInfo** *(dict) --*

              The information about values that appear frequently in a column (skewed values).

              - **SkewedColumnNames** *(list) --*

                A list of names of columns that contain skewed values.

                - *(string) --*

              - **SkewedColumnValues** *(list) --*

                A list of values that appear so frequently as to be considered skewed.

                - *(string) --*

              - **SkewedColumnValueLocationMaps** *(dict) --*

                A mapping of skewed values to the columns that contain them.

                - *(string) --*

                  - *(string) --*

            - **StoredAsSubDirectories** *(boolean) --*

               ``True`` if the table data is stored in subdirectories, or ``False`` if not.

          - **Parameters** *(dict) --*

            These key-value pairs define partition parameters.

            - *(string) --*

              - *(string) --*

          - **LastAnalyzedTime** *(datetime) --*

            The last time at which column statistics were computed for this partition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_script(
        self,
        DagNodes: List[ClientCreateScriptDagNodesTypeDef] = None,
        DagEdges: List[ClientCreateScriptDagEdgesTypeDef] = None,
        Language: str = None,
    ) -> ClientCreateScriptResponseTypeDef:
        """
        Transforms a directed acyclic graph (DAG) into code.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateScript>`_

        **Request Syntax**
        ::

          response = client.create_script(
              DagNodes=[
                  {
                      'Id': 'string',
                      'NodeType': 'string',
                      'Args': [
                          {
                              'Name': 'string',
                              'Value': 'string',
                              'Param': True|False
                          },
                      ],
                      'LineNumber': 123
                  },
              ],
              DagEdges=[
                  {
                      'Source': 'string',
                      'Target': 'string',
                      'TargetParameter': 'string'
                  },
              ],
              Language='PYTHON'|'SCALA'
          )
        :type DagNodes: list
        :param DagNodes:

          A list of the nodes in the DAG.

          - *(dict) --*

            Represents a node in a directed acyclic graph (DAG)

            - **Id** *(string) --* **[REQUIRED]**

              A node identifier that is unique within the node's graph.

            - **NodeType** *(string) --* **[REQUIRED]**

              The type of node that this is.

            - **Args** *(list) --* **[REQUIRED]**

              Properties of the node, in the form of name-value pairs.

              - *(dict) --*

                An argument or property of a node.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the argument or property.

                - **Value** *(string) --* **[REQUIRED]**

                  The value of the argument or property.

                - **Param** *(boolean) --*

                  True if the value is used as a parameter.

            - **LineNumber** *(integer) --*

              The line number of the node.

        :type DagEdges: list
        :param DagEdges:

          A list of the edges in the DAG.

          - *(dict) --*

            Represents a directional edge in a directed acyclic graph (DAG).

            - **Source** *(string) --* **[REQUIRED]**

              The ID of the node at which the edge starts.

            - **Target** *(string) --* **[REQUIRED]**

              The ID of the node at which the edge ends.

            - **TargetParameter** *(string) --*

              The target of the edge.

        :type Language: string
        :param Language:

          The programming language of the resulting code from the DAG.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PythonScript': 'string',
                'ScalaCode': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PythonScript** *(string) --*

              The Python script generated from the DAG.

            - **ScalaCode** *(string) --*

              The Scala code generated from the DAG.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_configuration(
        self,
        Name: str,
        EncryptionConfiguration: ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef,
    ) -> ClientCreateSecurityConfigurationResponseTypeDef:
        """
        Creates a new security configuration. A security configuration is a set of security properties that
        can be used by AWS Glue. You can use a security configuration to encrypt data at rest. For
        information about using security configurations in AWS Glue, see `Encrypting Data Written by
        Crawlers, Jobs, and Development Endpoints
        <https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateSecurityConfiguration>`_

        **Request Syntax**
        ::

          response = client.create_security_configuration(
              Name='string',
              EncryptionConfiguration={
                  'S3Encryption': [
                      {
                          'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                          'KmsKeyArn': 'string'
                      },
                  ],
                  'CloudWatchEncryption': {
                      'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                      'KmsKeyArn': 'string'
                  },
                  'JobBookmarksEncryption': {
                      'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                      'KmsKeyArn': 'string'
                  }
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name for the new security configuration.

        :type EncryptionConfiguration: dict
        :param EncryptionConfiguration: **[REQUIRED]**

          The encryption configuration for the new security configuration.

          - **S3Encryption** *(list) --*

            The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.

            - *(dict) --*

              Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.

              - **S3EncryptionMode** *(string) --*

                The encryption mode to use for Amazon S3 data.

              - **KmsKeyArn** *(string) --*

                The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

          - **CloudWatchEncryption** *(dict) --*

            The encryption configuration for Amazon CloudWatch.

            - **CloudWatchEncryptionMode** *(string) --*

              The encryption mode to use for CloudWatch data.

            - **KmsKeyArn** *(string) --*

              The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

          - **JobBookmarksEncryption** *(dict) --*

            The encryption configuration for job bookmarks.

            - **JobBookmarksEncryptionMode** *(string) --*

              The encryption mode to use for job bookmarks data.

            - **KmsKeyArn** *(string) --*

              The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name assigned to the new security configuration.

            - **CreatedTimestamp** *(datetime) --*

              The time at which the new security configuration was created.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_table(
        self,
        DatabaseName: str,
        TableInput: ClientCreateTableTableInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Creates a new table definition in the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateTable>`_

        **Request Syntax**
        ::

          response = client.create_table(
              CatalogId='string',
              DatabaseName='string',
              TableInput={
                  'Name': 'string',
                  'Description': 'string',
                  'Owner': 'string',
                  'LastAccessTime': datetime(2015, 1, 1),
                  'LastAnalyzedTime': datetime(2015, 1, 1),
                  'Retention': 123,
                  'StorageDescriptor': {
                      'Columns': [
                          {
                              'Name': 'string',
                              'Type': 'string',
                              'Comment': 'string',
                              'Parameters': {
                                  'string': 'string'
                              }
                          },
                      ],
                      'Location': 'string',
                      'InputFormat': 'string',
                      'OutputFormat': 'string',
                      'Compressed': True|False,
                      'NumberOfBuckets': 123,
                      'SerdeInfo': {
                          'Name': 'string',
                          'SerializationLibrary': 'string',
                          'Parameters': {
                              'string': 'string'
                          }
                      },
                      'BucketColumns': [
                          'string',
                      ],
                      'SortColumns': [
                          {
                              'Column': 'string',
                              'SortOrder': 123
                          },
                      ],
                      'Parameters': {
                          'string': 'string'
                      },
                      'SkewedInfo': {
                          'SkewedColumnNames': [
                              'string',
                          ],
                          'SkewedColumnValues': [
                              'string',
                          ],
                          'SkewedColumnValueLocationMaps': {
                              'string': 'string'
                          }
                      },
                      'StoredAsSubDirectories': True|False
                  },
                  'PartitionKeys': [
                      {
                          'Name': 'string',
                          'Type': 'string',
                          'Comment': 'string',
                          'Parameters': {
                              'string': 'string'
                          }
                      },
                  ],
                  'ViewOriginalText': 'string',
                  'ViewExpandedText': 'string',
                  'TableType': 'string',
                  'Parameters': {
                      'string': 'string'
                  }
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which to create the ``Table`` . If none is supplied, the AWS
          account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The catalog database in which to create the new table. For Hive compatibility, this name is
          entirely lowercase.

        :type TableInput: dict
        :param TableInput: **[REQUIRED]**

          The ``TableInput`` object that defines the metadata table to create in the catalog.

          - **Name** *(string) --* **[REQUIRED]**

            The table name. For Hive compatibility, this is folded to lowercase when it is stored.

          - **Description** *(string) --*

            A description of the table.

          - **Owner** *(string) --*

            The table owner.

          - **LastAccessTime** *(datetime) --*

            The last time that the table was accessed.

          - **LastAnalyzedTime** *(datetime) --*

            The last time that column statistics were computed for this table.

          - **Retention** *(integer) --*

            The retention time for this table.

          - **StorageDescriptor** *(dict) --*

            A storage descriptor containing information about the physical storage of this table.

            - **Columns** *(list) --*

              A list of the ``Columns`` in the table.

              - *(dict) --*

                A column in a ``Table`` .

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the ``Column`` .

                - **Type** *(string) --*

                  The data type of the ``Column`` .

                - **Comment** *(string) --*

                  A free-form text comment.

                - **Parameters** *(dict) --*

                  These key-value pairs define properties associated with the column.

                  - *(string) --*

                    - *(string) --*

            - **Location** *(string) --*

              The physical location of the table. By default, this takes the form of the warehouse
              location, followed by the database location in the warehouse, followed by the table name.

            - **InputFormat** *(string) --*

              The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom
              format.

            - **OutputFormat** *(string) --*

              The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` ,
              or a custom format.

            - **Compressed** *(boolean) --*

               ``True`` if the data in the table is compressed, or ``False`` if not.

            - **NumberOfBuckets** *(integer) --*

              Must be specified if the table contains any dimension columns.

            - **SerdeInfo** *(dict) --*

              The serialization/deserialization (SerDe) information.

              - **Name** *(string) --*

                Name of the SerDe.

              - **SerializationLibrary** *(string) --*

                Usually the class that implements the SerDe. An example is
                ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

              - **Parameters** *(dict) --*

                These key-value pairs define initialization parameters for the SerDe.

                - *(string) --*

                  - *(string) --*

            - **BucketColumns** *(list) --*

              A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

              - *(string) --*

            - **SortColumns** *(list) --*

              A list specifying the sort order of each bucket in the table.

              - *(dict) --*

                Specifies the sort order of a sorted column.

                - **Column** *(string) --* **[REQUIRED]**

                  The name of the column.

                - **SortOrder** *(integer) --* **[REQUIRED]**

                  Indicates that the column is sorted in ascending order (``== 1`` ), or in descending
                  order (``==0`` ).

            - **Parameters** *(dict) --*

              The user-supplied properties in key-value form.

              - *(string) --*

                - *(string) --*

            - **SkewedInfo** *(dict) --*

              The information about values that appear frequently in a column (skewed values).

              - **SkewedColumnNames** *(list) --*

                A list of names of columns that contain skewed values.

                - *(string) --*

              - **SkewedColumnValues** *(list) --*

                A list of values that appear so frequently as to be considered skewed.

                - *(string) --*

              - **SkewedColumnValueLocationMaps** *(dict) --*

                A mapping of skewed values to the columns that contain them.

                - *(string) --*

                  - *(string) --*

            - **StoredAsSubDirectories** *(boolean) --*

               ``True`` if the table data is stored in subdirectories, or ``False`` if not.

          - **PartitionKeys** *(list) --*

            A list of columns by which the table is partitioned. Only primitive types are supported as
            partition keys.

            When you create a table used by Amazon Athena, and you do not specify any ``partitionKeys`` ,
            you must at least set the value of ``partitionKeys`` to an empty list. For example:

             ``"PartitionKeys": []``

            - *(dict) --*

              A column in a ``Table`` .

              - **Name** *(string) --* **[REQUIRED]**

                The name of the ``Column`` .

              - **Type** *(string) --*

                The data type of the ``Column`` .

              - **Comment** *(string) --*

                A free-form text comment.

              - **Parameters** *(dict) --*

                These key-value pairs define properties associated with the column.

                - *(string) --*

                  - *(string) --*

          - **ViewOriginalText** *(string) --*

            If the table is a view, the original text of the view; otherwise ``null`` .

          - **ViewExpandedText** *(string) --*

            If the table is a view, the expanded text of the view; otherwise ``null`` .

          - **TableType** *(string) --*

            The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

          - **Parameters** *(dict) --*

            These key-value pairs define properties associated with the table.

            - *(string) --*

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
    def create_trigger(
        self,
        Name: str,
        Type: str,
        Actions: List[ClientCreateTriggerActionsTypeDef],
        WorkflowName: str = None,
        Schedule: str = None,
        Predicate: ClientCreateTriggerPredicateTypeDef = None,
        Description: str = None,
        StartOnCreation: bool = None,
        Tags: List[str] = None,
    ) -> ClientCreateTriggerResponseTypeDef:
        """
        Creates a new trigger.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateTrigger>`_

        **Request Syntax**
        ::

          response = client.create_trigger(
              Name='string',
              WorkflowName='string',
              Type='SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
              Schedule='string',
              Predicate={
                  'Logical': 'AND'|'ANY',
                  'Conditions': [
                      {
                          'LogicalOperator': 'EQUALS',
                          'JobName': 'string',
                          'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                          'CrawlerName': 'string',
                          'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                      },
                  ]
              },
              Actions=[
                  {
                      'JobName': 'string',
                      'Arguments': {
                          'string': 'string'
                      },
                      'Timeout': 123,
                      'SecurityConfiguration': 'string',
                      'NotificationProperty': {
                          'NotifyDelayAfter': 123
                      },
                      'CrawlerName': 'string'
                  },
              ],
              Description='string',
              StartOnCreation=True|False,
              Tags={
                  'string': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the trigger.

        :type WorkflowName: string
        :param WorkflowName:

          The name of the workflow associated with the trigger.

        :type Type: string
        :param Type: **[REQUIRED]**

          The type of the new trigger.

        :type Schedule: string
        :param Schedule:

          A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and
          Crawlers <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ .
          For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

          This field is required when the trigger type is SCHEDULED.

        :type Predicate: dict
        :param Predicate:

          A predicate to specify when the new trigger should fire.

          This field is required when the trigger type is ``CONDITIONAL`` .

          - **Logical** *(string) --*

            An optional field if only one condition is listed. If multiple conditions are listed, then this
            field is required.

          - **Conditions** *(list) --*

            A list of the conditions that determine when the trigger will fire.

            - *(dict) --*

              Defines a condition under which a trigger fires.

              - **LogicalOperator** *(string) --*

                A logical operator.

              - **JobName** *(string) --*

                The name of the job whose ``JobRuns`` this condition applies to, and on which this trigger
                waits.

              - **State** *(string) --*

                The condition state. Currently, the values supported are ``SUCCEEDED`` , ``STOPPED`` ,
                ``TIMEOUT`` , and ``FAILED`` .

              - **CrawlerName** *(string) --*

                The name of the crawler to which this condition applies.

              - **CrawlState** *(string) --*

                The state of the crawler to which this condition applies.

        :type Actions: list
        :param Actions: **[REQUIRED]**

          The actions initiated by this trigger when it fires.

          - *(dict) --*

            Defines an action to be initiated by a trigger.

            - **JobName** *(string) --*

              The name of a job to be executed.

            - **Arguments** *(dict) --*

              The job arguments used when this trigger fires. For this job run, they replace the default
              arguments set in the job definition itself.

              You can specify arguments here that your own job-execution script consumes, as well as
              arguments that AWS Glue itself consumes.

              For information about how to specify and consume your own Job arguments, see the `Calling AWS
              Glue APIs in Python
              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
              topic in the developer guide.

              For information about the key-value pairs that AWS Glue consumes to set up your job, see the
              `Special Parameters Used by AWS Glue
              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
              topic in the developer guide.

              - *(string) --*

                - *(string) --*

            - **Timeout** *(integer) --*

              The ``JobRun`` timeout in minutes. This is the maximum time that a job run can consume
              resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes
              (48 hours). This overrides the timeout value set in the parent job.

            - **SecurityConfiguration** *(string) --*

              The name of the ``SecurityConfiguration`` structure to be used with this action.

            - **NotificationProperty** *(dict) --*

              Specifies configuration properties of a job run notification.

              - **NotifyDelayAfter** *(integer) --*

                After a job run starts, the number of minutes to wait before sending a job run delay
                notification.

            - **CrawlerName** *(string) --*

              The name of the crawler to be used with this action.

        :type Description: string
        :param Description:

          A description of the new trigger.

        :type StartOnCreation: boolean
        :param StartOnCreation:

          Set to ``true`` to start ``SCHEDULED`` and ``CONDITIONAL`` triggers when created. True is not
          supported for ``ON_DEMAND`` triggers.

        :type Tags: dict
        :param Tags:

          The tags to use with this trigger. You may use tags to limit access to the trigger. For more
          information about tags in AWS Glue, see `AWS Tags in AWS Glue
          <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`__ in the developer guide.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the trigger.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user_defined_function(
        self,
        DatabaseName: str,
        FunctionInput: ClientCreateUserDefinedFunctionFunctionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Creates a new function definition in the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateUserDefinedFunction>`_

        **Request Syntax**
        ::

          response = client.create_user_defined_function(
              CatalogId='string',
              DatabaseName='string',
              FunctionInput={
                  'FunctionName': 'string',
                  'ClassName': 'string',
                  'OwnerName': 'string',
                  'OwnerType': 'USER'|'ROLE'|'GROUP',
                  'ResourceUris': [
                      {
                          'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                          'Uri': 'string'
                      },
                  ]
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which to create the function. If none is provided, the AWS account
          ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database in which to create the function.

        :type FunctionInput: dict
        :param FunctionInput: **[REQUIRED]**

          A ``FunctionInput`` object that defines the function to create in the Data Catalog.

          - **FunctionName** *(string) --*

            The name of the function.

          - **ClassName** *(string) --*

            The Java class that contains the function code.

          - **OwnerName** *(string) --*

            The owner of the function.

          - **OwnerType** *(string) --*

            The owner type.

          - **ResourceUris** *(list) --*

            The resource URIs for the function.

            - *(dict) --*

              The URIs for function resources.

              - **ResourceType** *(string) --*

                The type of the resource.

              - **Uri** *(string) --*

                The URI for accessing the resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_workflow(
        self,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, str] = None,
        Tags: List[str] = None,
    ) -> ClientCreateWorkflowResponseTypeDef:
        """
        Creates a new workflow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateWorkflow>`_

        **Request Syntax**
        ::

          response = client.create_workflow(
              Name='string',
              Description='string',
              DefaultRunProperties={
                  'string': 'string'
              },
              Tags={
                  'string': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name to be assigned to the workflow. It should be unique within your account.

        :type Description: string
        :param Description:

          A description of the workflow.

        :type DefaultRunProperties: dict
        :param DefaultRunProperties:

          A collection of properties to be used as part of each execution of the workflow.

          - *(string) --*

            - *(string) --*

        :type Tags: dict
        :param Tags:

          The tags to be used with this workflow.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the workflow which was provided as part of the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_classifier(self, Name: str) -> Dict[str, Any]:
        """
        Removes a classifier from the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteClassifier>`_

        **Request Syntax**
        ::

          response = client.delete_classifier(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the classifier to remove.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connection(
        self, ConnectionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a connection from the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteConnection>`_

        **Request Syntax**
        ::

          response = client.delete_connection(
              CatalogId='string',
              ConnectionName='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the connection resides. If none is provided, the AWS account
          ID is used by default.

        :type ConnectionName: string
        :param ConnectionName: **[REQUIRED]**

          The name of the connection to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_crawler(self, Name: str) -> Dict[str, Any]:
        """
        Removes a specified crawler from the AWS Glue Data Catalog, unless the crawler state is ``RUNNING``
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteCrawler>`_

        **Request Syntax**
        ::

          response = client.delete_crawler(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the crawler to remove.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_database(self, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        Removes a specified database from a Data Catalog.

        .. note::

          After completing this operation, you no longer have access to the tables (and all table versions
          and partitions that might belong to the tables) and the user-defined functions in the deleted
          database. AWS Glue deletes these "orphaned" resources asynchronously in a timely manner, at the
          discretion of the service.

          To ensure the immediate deletion of all related resources, before calling ``DeleteDatabase`` ,
          use ``DeleteTableVersion`` or ``BatchDeleteTableVersion`` , ``DeletePartition`` or
          ``BatchDeletePartition`` , ``DeleteUserDefinedFunction`` , and ``DeleteTable`` or
          ``BatchDeleteTable`` , to delete any resources that belong to the database.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteDatabase>`_

        **Request Syntax**
        ::

          response = client.delete_database(
              CatalogId='string',
              Name='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the database resides. If none is provided, the AWS account ID
          is used by default.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the database to delete. For Hive compatibility, this must be all lowercase.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dev_endpoint(self, EndpointName: str) -> Dict[str, Any]:
        """
        Deletes a specified development endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteDevEndpoint>`_

        **Request Syntax**
        ::

          response = client.delete_dev_endpoint(
              EndpointName='string'
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**

          The name of the ``DevEndpoint`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_job(self, JobName: str) -> ClientDeleteJobResponseTypeDef:
        """
        Deletes a specified job definition. If the job definition is not found, no exception is thrown.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteJob>`_

        **Request Syntax**
        ::

          response = client.delete_job(
              JobName='string'
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job definition to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobName** *(string) --*

              The name of the job definition that was deleted.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ml_transform(
        self, TransformId: str
    ) -> ClientDeleteMlTransformResponseTypeDef:
        """
        Deletes an AWS Glue machine learning transform. Machine learning transforms are a special type of
        transform that use machine learning to learn the details of the transformation to be performed by
        learning from examples provided by humans. These transformations are then saved by AWS Glue. If you
        no longer need a transform, you can delete it by calling ``DeleteMLTransforms`` . However, any AWS
        Glue jobs that still reference the deleted transform will no longer succeed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteMLTransform>`_

        **Request Syntax**
        ::

          response = client.delete_ml_transform(
              TransformId='string'
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the transform to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TransformId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TransformId** *(string) --*

              The unique identifier of the transform that was deleted.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Deletes a specified partition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeletePartition>`_

        **Request Syntax**
        ::

          response = client.delete_partition(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              PartitionValues=[
                  'string',
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the
          AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database in which the table in question resides.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the table that contains the partition to be deleted.

        :type PartitionValues: list
        :param PartitionValues: **[REQUIRED]**

          The values that define the partition.

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
    def delete_resource_policy(self, PolicyHashCondition: str = None) -> Dict[str, Any]:
        """
        Deletes a specified policy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteResourcePolicy>`_

        **Request Syntax**
        ::

          response = client.delete_resource_policy(
              PolicyHashCondition='string'
          )
        :type PolicyHashCondition: string
        :param PolicyHashCondition:

          The hash value returned when this policy was set.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        """
        Deletes a specified security configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteSecurityConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_security_configuration(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the security configuration to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_table(
        self, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        Removes a table definition from the Data Catalog.

        .. note::

          After completing this operation, you no longer have access to the table versions and partitions
          that belong to the deleted table. AWS Glue deletes these "orphaned" resources asynchronously in a
          timely manner, at the discretion of the service.

          To ensure the immediate deletion of all related resources, before calling ``DeleteTable`` , use
          ``DeleteTableVersion`` or ``BatchDeleteTableVersion`` , and ``DeletePartition`` or
          ``BatchDeletePartition`` , to delete any resources that belong to the table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteTable>`_

        **Request Syntax**
        ::

          response = client.delete_table(
              CatalogId='string',
              DatabaseName='string',
              Name='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database in which the table resides. For Hive compatibility, this name is
          entirely lowercase.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the table to be deleted. For Hive compatibility, this name is entirely lowercase.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_table_version(
        self, DatabaseName: str, TableName: str, VersionId: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a specified version of a table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteTableVersion>`_

        **Request Syntax**
        ::

          response = client.delete_table_version(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              VersionId='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The database in the catalog in which the table resides. For Hive compatibility, this name is
          entirely lowercase.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the table. For Hive compatibility, this name is entirely lowercase.

        :type VersionId: string
        :param VersionId: **[REQUIRED]**

          The ID of the table version to be deleted. A ``VersionID`` is a string representation of an
          integer. Each version is incremented by 1.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_trigger(self, Name: str) -> ClientDeleteTriggerResponseTypeDef:
        """
        Deletes a specified trigger. If the trigger is not found, no exception is thrown.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteTrigger>`_

        **Request Syntax**
        ::

          response = client.delete_trigger(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the trigger to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the trigger that was deleted.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        Deletes an existing function definition from the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteUserDefinedFunction>`_

        **Request Syntax**
        ::

          response = client.delete_user_defined_function(
              CatalogId='string',
              DatabaseName='string',
              FunctionName='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the function to be deleted is located. If none is supplied, the
          AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the function is located.

        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the function definition to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_workflow(self, Name: str) -> ClientDeleteWorkflowResponseTypeDef:
        """
        Deletes a workflow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteWorkflow>`_

        **Request Syntax**
        ::

          response = client.delete_workflow(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the workflow to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              Name of the workflow specified in input.

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
    def get_catalog_import_status(
        self, CatalogId: str = None
    ) -> ClientGetCatalogImportStatusResponseTypeDef:
        """
        Retrieves the status of a migration operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCatalogImportStatus>`_

        **Request Syntax**
        ::

          response = client.get_catalog_import_status(
              CatalogId='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the catalog to migrate. Currently, this should be the AWS account ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ImportStatus': {
                    'ImportCompleted': True|False,
                    'ImportTime': datetime(2015, 1, 1),
                    'ImportedBy': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ImportStatus** *(dict) --*

              The status of the specified catalog migration.

              - **ImportCompleted** *(boolean) --*

                 ``True`` if the migration has completed, or ``False`` otherwise.

              - **ImportTime** *(datetime) --*

                The time that the migration was started.

              - **ImportedBy** *(string) --*

                The name of the person who initiated the migration.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_classifier(self, Name: str) -> ClientGetClassifierResponseTypeDef:
        """
        Retrieve a classifier by name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetClassifier>`_

        **Request Syntax**
        ::

          response = client.get_classifier(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the classifier to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Classifier': {
                    'GrokClassifier': {
                        'Name': 'string',
                        'Classification': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'Version': 123,
                        'GrokPattern': 'string',
                        'CustomPatterns': 'string'
                    },
                    'XMLClassifier': {
                        'Name': 'string',
                        'Classification': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'Version': 123,
                        'RowTag': 'string'
                    },
                    'JsonClassifier': {
                        'Name': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'Version': 123,
                        'JsonPath': 'string'
                    },
                    'CsvClassifier': {
                        'Name': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'Version': 123,
                        'Delimiter': 'string',
                        'QuoteSymbol': 'string',
                        'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
                        'Header': [
                            'string',
                        ],
                        'DisableValueTrimming': True|False,
                        'AllowSingleColumn': True|False
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Classifier** *(dict) --*

              The requested classifier.

              - **GrokClassifier** *(dict) --*

                A classifier that uses ``grok`` .

                - **Name** *(string) --*

                  The name of the classifier.

                - **Classification** *(string) --*

                  An identifier of the data format that the classifier matches, such as Twitter, JSON,
                  Omniture logs, and so on.

                - **CreationTime** *(datetime) --*

                  The time that this classifier was registered.

                - **LastUpdated** *(datetime) --*

                  The time that this classifier was last updated.

                - **Version** *(integer) --*

                  The version of this classifier.

                - **GrokPattern** *(string) --*

                  The grok pattern applied to a data store by this classifier. For more information, see
                  built-in patterns in `Writing Custom Classifiers
                  <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

                - **CustomPatterns** *(string) --*

                  Optional custom grok patterns defined by this classifier. For more information, see
                  custom patterns in `Writing Custom Classifiers
                  <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

              - **XMLClassifier** *(dict) --*

                A classifier for XML content.

                - **Name** *(string) --*

                  The name of the classifier.

                - **Classification** *(string) --*

                  An identifier of the data format that the classifier matches.

                - **CreationTime** *(datetime) --*

                  The time that this classifier was registered.

                - **LastUpdated** *(datetime) --*

                  The time that this classifier was last updated.

                - **Version** *(integer) --*

                  The version of this classifier.

                - **RowTag** *(string) --*

                  The XML tag designating the element that contains each record in an XML document being
                  parsed. This can't identify a self-closing element (closed by ``/>`` ). An empty row
                  element that contains only attributes can be parsed as long as it ends with a closing tag
                  (for example, ``<row item_a="A" item_b="B"></row>`` is okay, but ``<row item_a="A"
                  item_b="B" />`` is not).

              - **JsonClassifier** *(dict) --*

                A classifier for JSON content.

                - **Name** *(string) --*

                  The name of the classifier.

                - **CreationTime** *(datetime) --*

                  The time that this classifier was registered.

                - **LastUpdated** *(datetime) --*

                  The time that this classifier was last updated.

                - **Version** *(integer) --*

                  The version of this classifier.

                - **JsonPath** *(string) --*

                  A ``JsonPath`` string defining the JSON data for the classifier to classify. AWS Glue
                  supports a subset of ``JsonPath`` , as described in `Writing JsonPath Custom Classifiers
                  <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json>`__
                  .

              - **CsvClassifier** *(dict) --*

                A classifier for comma-separated values (CSV).

                - **Name** *(string) --*

                  The name of the classifier.

                - **CreationTime** *(datetime) --*

                  The time that this classifier was registered.

                - **LastUpdated** *(datetime) --*

                  The time that this classifier was last updated.

                - **Version** *(integer) --*

                  The version of this classifier.

                - **Delimiter** *(string) --*

                  A custom symbol to denote what separates each column entry in the row.

                - **QuoteSymbol** *(string) --*

                  A custom symbol to denote what combines content into a single column value. It must be
                  different from the column delimiter.

                - **ContainsHeader** *(string) --*

                  Indicates whether the CSV file contains a header.

                - **Header** *(list) --*

                  A list of strings representing column names.

                  - *(string) --*

                - **DisableValueTrimming** *(boolean) --*

                  Specifies not to trim values before identifying the type of column values. The default
                  value is ``true`` .

                - **AllowSingleColumn** *(boolean) --*

                  Enables the processing of files that contain only one column.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_classifiers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetClassifiersResponseTypeDef:
        """
        Lists all classifier objects in the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetClassifiers>`_

        **Request Syntax**
        ::

          response = client.get_classifiers(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The size of the list to return (optional).

        :type NextToken: string
        :param NextToken:

          An optional continuation token.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Classifiers': [
                    {
                        'GrokClassifier': {
                            'Name': 'string',
                            'Classification': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'LastUpdated': datetime(2015, 1, 1),
                            'Version': 123,
                            'GrokPattern': 'string',
                            'CustomPatterns': 'string'
                        },
                        'XMLClassifier': {
                            'Name': 'string',
                            'Classification': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'LastUpdated': datetime(2015, 1, 1),
                            'Version': 123,
                            'RowTag': 'string'
                        },
                        'JsonClassifier': {
                            'Name': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'LastUpdated': datetime(2015, 1, 1),
                            'Version': 123,
                            'JsonPath': 'string'
                        },
                        'CsvClassifier': {
                            'Name': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'LastUpdated': datetime(2015, 1, 1),
                            'Version': 123,
                            'Delimiter': 'string',
                            'QuoteSymbol': 'string',
                            'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
                            'Header': [
                                'string',
                            ],
                            'DisableValueTrimming': True|False,
                            'AllowSingleColumn': True|False
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Classifiers** *(list) --*

              The requested list of classifier objects.

              - *(dict) --*

                Classifiers are triggered during a crawl task. A classifier checks whether a given file is
                in a format it can handle. If it is, the classifier creates a schema in the form of a
                ``StructType`` object that matches that data format.

                You can use the standard classifiers that AWS Glue provides, or you can write your own
                classifiers to best categorize your data sources and specify the appropriate schemas to use
                for them. A classifier can be a ``grok`` classifier, an ``XML`` classifier, a ``JSON``
                classifier, or a custom ``CSV`` classifier, as specified in one of the fields in the
                ``Classifier`` object.

                - **GrokClassifier** *(dict) --*

                  A classifier that uses ``grok`` .

                  - **Name** *(string) --*

                    The name of the classifier.

                  - **Classification** *(string) --*

                    An identifier of the data format that the classifier matches, such as Twitter, JSON,
                    Omniture logs, and so on.

                  - **CreationTime** *(datetime) --*

                    The time that this classifier was registered.

                  - **LastUpdated** *(datetime) --*

                    The time that this classifier was last updated.

                  - **Version** *(integer) --*

                    The version of this classifier.

                  - **GrokPattern** *(string) --*

                    The grok pattern applied to a data store by this classifier. For more information, see
                    built-in patterns in `Writing Custom Classifiers
                    <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

                  - **CustomPatterns** *(string) --*

                    Optional custom grok patterns defined by this classifier. For more information, see
                    custom patterns in `Writing Custom Classifiers
                    <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

                - **XMLClassifier** *(dict) --*

                  A classifier for XML content.

                  - **Name** *(string) --*

                    The name of the classifier.

                  - **Classification** *(string) --*

                    An identifier of the data format that the classifier matches.

                  - **CreationTime** *(datetime) --*

                    The time that this classifier was registered.

                  - **LastUpdated** *(datetime) --*

                    The time that this classifier was last updated.

                  - **Version** *(integer) --*

                    The version of this classifier.

                  - **RowTag** *(string) --*

                    The XML tag designating the element that contains each record in an XML document being
                    parsed. This can't identify a self-closing element (closed by ``/>`` ). An empty row
                    element that contains only attributes can be parsed as long as it ends with a closing
                    tag (for example, ``<row item_a="A" item_b="B"></row>`` is okay, but ``<row item_a="A"
                    item_b="B" />`` is not).

                - **JsonClassifier** *(dict) --*

                  A classifier for JSON content.

                  - **Name** *(string) --*

                    The name of the classifier.

                  - **CreationTime** *(datetime) --*

                    The time that this classifier was registered.

                  - **LastUpdated** *(datetime) --*

                    The time that this classifier was last updated.

                  - **Version** *(integer) --*

                    The version of this classifier.

                  - **JsonPath** *(string) --*

                    A ``JsonPath`` string defining the JSON data for the classifier to classify. AWS Glue
                    supports a subset of ``JsonPath`` , as described in `Writing JsonPath Custom
                    Classifiers
                    <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json>`__
                    .

                - **CsvClassifier** *(dict) --*

                  A classifier for comma-separated values (CSV).

                  - **Name** *(string) --*

                    The name of the classifier.

                  - **CreationTime** *(datetime) --*

                    The time that this classifier was registered.

                  - **LastUpdated** *(datetime) --*

                    The time that this classifier was last updated.

                  - **Version** *(integer) --*

                    The version of this classifier.

                  - **Delimiter** *(string) --*

                    A custom symbol to denote what separates each column entry in the row.

                  - **QuoteSymbol** *(string) --*

                    A custom symbol to denote what combines content into a single column value. It must be
                    different from the column delimiter.

                  - **ContainsHeader** *(string) --*

                    Indicates whether the CSV file contains a header.

                  - **Header** *(list) --*

                    A list of strings representing column names.

                    - *(string) --*

                  - **DisableValueTrimming** *(boolean) --*

                    Specifies not to trim values before identifying the type of column values. The default
                    value is ``true`` .

                  - **AllowSingleColumn** *(boolean) --*

                    Enables the processing of files that contain only one column.

            - **NextToken** *(string) --*

              A continuation token.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connection(
        self, Name: str, CatalogId: str = None, HidePassword: bool = None
    ) -> ClientGetConnectionResponseTypeDef:
        """
        Retrieves a connection definition from the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetConnection>`_

        **Request Syntax**
        ::

          response = client.get_connection(
              CatalogId='string',
              Name='string',
              HidePassword=True|False
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the connection resides. If none is provided, the AWS account
          ID is used by default.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the connection definition to retrieve.

        :type HidePassword: boolean
        :param HidePassword:

          Allows you to retrieve the connection metadata without returning the password. For instance, the
          AWS Glue console uses this flag to retrieve the connection, and does not display the password.
          Set this parameter when the caller might not have permission to use the AWS KMS key to decrypt
          the password, but it does have permission to access the rest of the connection properties.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Connection': {
                    'Name': 'string',
                    'Description': 'string',
                    'ConnectionType': 'JDBC'|'SFTP',
                    'MatchCriteria': [
                        'string',
                    ],
                    'ConnectionProperties': {
                        'string': 'string'
                    },
                    'PhysicalConnectionRequirements': {
                        'SubnetId': 'string',
                        'SecurityGroupIdList': [
                            'string',
                        ],
                        'AvailabilityZone': 'string'
                    },
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdatedTime': datetime(2015, 1, 1),
                    'LastUpdatedBy': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Connection** *(dict) --*

              The requested connection definition.

              - **Name** *(string) --*

                The name of the connection definition.

              - **Description** *(string) --*

                The description of the connection.

              - **ConnectionType** *(string) --*

                The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

              - **MatchCriteria** *(list) --*

                A list of criteria that can be used in selecting this connection.

                - *(string) --*

              - **ConnectionProperties** *(dict) --*

                These key-value pairs define parameters for the connection:

                * ``HOST`` - The host URI: either the fully qualified domain name (FQDN) or the IPv4
                address of the database host.

                * ``PORT`` - The port number, between 1024 and 65535, of the port on which the database
                host is listening for database connections.

                * ``USER_NAME`` - The name under which to log in to the database. The value string for
                ``USER_NAME`` is "``USERNAME`` ".

                * ``PASSWORD`` - A password, if one is used, for the user name.

                * ``ENCRYPTED_PASSWORD`` - When you enable connection password protection by setting
                ``ConnectionPasswordEncryption`` in the Data Catalog encryption settings, this field stores
                the encrypted password.

                * ``JDBC_DRIVER_JAR_URI`` - The Amazon Simple Storage Service (Amazon S3) path of the JAR
                file that contains the JDBC driver to use.

                * ``JDBC_DRIVER_CLASS_NAME`` - The class name of the JDBC driver to use.

                * ``JDBC_ENGINE`` - The name of the JDBC engine to use.

                * ``JDBC_ENGINE_VERSION`` - The version of the JDBC engine to use.

                * ``CONFIG_FILES`` - (Reserved for future use.)

                * ``INSTANCE_ID`` - The instance ID to use.

                * ``JDBC_CONNECTION_URL`` - The URL for the JDBC connection.

                * ``JDBC_ENFORCE_SSL`` - A Boolean string (true, false) specifying whether Secure Sockets
                Layer (SSL) with hostname matching is enforced for the JDBC connection on the client. The
                default is false.

                * ``CUSTOM_JDBC_CERT`` - An Amazon S3 location specifying the customer's root certificate.
                AWS Glue uses this root certificate to validate the customer’s certificate when connecting
                to the customer database. AWS Glue only handles X.509 certificates. The certificate
                provided must be DER-encoded and supplied in Base64 encoding PEM format.

                * ``SKIP_CUSTOM_JDBC_CERT_VALIDATION`` - By default, this is ``false`` . AWS Glue validates
                the Signature algorithm and Subject Public Key Algorithm for the customer certificate. The
                only permitted algorithms for the Signature algorithm are SHA256withRSA, SHA384withRSA or
                SHA512withRSA. For the Subject Public Key Algorithm, the key length must be at least 2048.
                You can set the value of this property to ``true`` to skip AWS Glue’s validation of the
                customer certificate.

                * ``CUSTOM_JDBC_CERT_STRING`` - A custom JDBC certificate string which is used for domain
                match or distinguished name match to prevent a man-in-the-middle attack. In Oracle
                database, this is used as the ``SSL_SERVER_CERT_DN`` ; in Microsoft SQL Server, this is
                used as the ``hostNameInCertificate`` .

                - *(string) --*

                  - *(string) --*

              - **PhysicalConnectionRequirements** *(dict) --*

                A map of physical connection requirements, such as virtual private cloud (VPC) and
                ``SecurityGroup`` , that are needed to make this connection successfully.

                - **SubnetId** *(string) --*

                  The subnet ID used by the connection.

                - **SecurityGroupIdList** *(list) --*

                  The security group ID list used by the connection.

                  - *(string) --*

                - **AvailabilityZone** *(string) --*

                  The connection's Availability Zone. This field is redundant because the specified subnet
                  implies the Availability Zone to be used. Currently the field must be populated, but it
                  will be deprecated in the future.

              - **CreationTime** *(datetime) --*

                The time that this connection definition was created.

              - **LastUpdatedTime** *(datetime) --*

                The last time that this connection definition was updated.

              - **LastUpdatedBy** *(string) --*

                The user, group, or role that last updated this connection definition.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connections(
        self,
        CatalogId: str = None,
        Filter: ClientGetConnectionsFilterTypeDef = None,
        HidePassword: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetConnectionsResponseTypeDef:
        """
        Retrieves a list of connection definitions from the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetConnections>`_

        **Request Syntax**
        ::

          response = client.get_connections(
              CatalogId='string',
              Filter={
                  'MatchCriteria': [
                      'string',
                  ],
                  'ConnectionType': 'JDBC'|'SFTP'
              },
              HidePassword=True|False,
              NextToken='string',
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the connections reside. If none is provided, the AWS account
          ID is used by default.

        :type Filter: dict
        :param Filter:

          A filter that controls which connections are returned.

          - **MatchCriteria** *(list) --*

            A criteria string that must match the criteria recorded in the connection definition for that
            connection definition to be returned.

            - *(string) --*

          - **ConnectionType** *(string) --*

            The type of connections to return. Currently, only JDBC is supported; SFTP is not supported.

        :type HidePassword: boolean
        :param HidePassword:

          Allows you to retrieve the connection metadata without returning the password. For instance, the
          AWS Glue console uses this flag to retrieve the connection, and does not display the password.
          Set this parameter when the caller might not have permission to use the AWS KMS key to decrypt
          the password, but it does have permission to access the rest of the connection properties.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of connections to return in one response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ConnectionList': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'ConnectionType': 'JDBC'|'SFTP',
                        'MatchCriteria': [
                            'string',
                        ],
                        'ConnectionProperties': {
                            'string': 'string'
                        },
                        'PhysicalConnectionRequirements': {
                            'SubnetId': 'string',
                            'SecurityGroupIdList': [
                                'string',
                            ],
                            'AvailabilityZone': 'string'
                        },
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1),
                        'LastUpdatedBy': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ConnectionList** *(list) --*

              A list of requested connection definitions.

              - *(dict) --*

                Defines a connection to a data source.

                - **Name** *(string) --*

                  The name of the connection definition.

                - **Description** *(string) --*

                  The description of the connection.

                - **ConnectionType** *(string) --*

                  The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

                - **MatchCriteria** *(list) --*

                  A list of criteria that can be used in selecting this connection.

                  - *(string) --*

                - **ConnectionProperties** *(dict) --*

                  These key-value pairs define parameters for the connection:

                  * ``HOST`` - The host URI: either the fully qualified domain name (FQDN) or the IPv4
                  address of the database host.

                  * ``PORT`` - The port number, between 1024 and 65535, of the port on which the database
                  host is listening for database connections.

                  * ``USER_NAME`` - The name under which to log in to the database. The value string for
                  ``USER_NAME`` is "``USERNAME`` ".

                  * ``PASSWORD`` - A password, if one is used, for the user name.

                  * ``ENCRYPTED_PASSWORD`` - When you enable connection password protection by setting
                  ``ConnectionPasswordEncryption`` in the Data Catalog encryption settings, this field
                  stores the encrypted password.

                  * ``JDBC_DRIVER_JAR_URI`` - The Amazon Simple Storage Service (Amazon S3) path of the JAR
                  file that contains the JDBC driver to use.

                  * ``JDBC_DRIVER_CLASS_NAME`` - The class name of the JDBC driver to use.

                  * ``JDBC_ENGINE`` - The name of the JDBC engine to use.

                  * ``JDBC_ENGINE_VERSION`` - The version of the JDBC engine to use.

                  * ``CONFIG_FILES`` - (Reserved for future use.)

                  * ``INSTANCE_ID`` - The instance ID to use.

                  * ``JDBC_CONNECTION_URL`` - The URL for the JDBC connection.

                  * ``JDBC_ENFORCE_SSL`` - A Boolean string (true, false) specifying whether Secure Sockets
                  Layer (SSL) with hostname matching is enforced for the JDBC connection on the client. The
                  default is false.

                  * ``CUSTOM_JDBC_CERT`` - An Amazon S3 location specifying the customer's root
                  certificate. AWS Glue uses this root certificate to validate the customer’s certificate
                  when connecting to the customer database. AWS Glue only handles X.509 certificates. The
                  certificate provided must be DER-encoded and supplied in Base64 encoding PEM format.

                  * ``SKIP_CUSTOM_JDBC_CERT_VALIDATION`` - By default, this is ``false`` . AWS Glue
                  validates the Signature algorithm and Subject Public Key Algorithm for the customer
                  certificate. The only permitted algorithms for the Signature algorithm are SHA256withRSA,
                  SHA384withRSA or SHA512withRSA. For the Subject Public Key Algorithm, the key length must
                  be at least 2048. You can set the value of this property to ``true`` to skip AWS Glue’s
                  validation of the customer certificate.

                  * ``CUSTOM_JDBC_CERT_STRING`` - A custom JDBC certificate string which is used for domain
                  match or distinguished name match to prevent a man-in-the-middle attack. In Oracle
                  database, this is used as the ``SSL_SERVER_CERT_DN`` ; in Microsoft SQL Server, this is
                  used as the ``hostNameInCertificate`` .

                  - *(string) --*

                    - *(string) --*

                - **PhysicalConnectionRequirements** *(dict) --*

                  A map of physical connection requirements, such as virtual private cloud (VPC) and
                  ``SecurityGroup`` , that are needed to make this connection successfully.

                  - **SubnetId** *(string) --*

                    The subnet ID used by the connection.

                  - **SecurityGroupIdList** *(list) --*

                    The security group ID list used by the connection.

                    - *(string) --*

                  - **AvailabilityZone** *(string) --*

                    The connection's Availability Zone. This field is redundant because the specified
                    subnet implies the Availability Zone to be used. Currently the field must be populated,
                    but it will be deprecated in the future.

                - **CreationTime** *(datetime) --*

                  The time that this connection definition was created.

                - **LastUpdatedTime** *(datetime) --*

                  The last time that this connection definition was updated.

                - **LastUpdatedBy** *(string) --*

                  The user, group, or role that last updated this connection definition.

            - **NextToken** *(string) --*

              A continuation token, if the list of connections returned does not include the last of the
              filtered connections.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_crawler(self, Name: str) -> ClientGetCrawlerResponseTypeDef:
        """
        Retrieves metadata for a specified crawler.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawler>`_

        **Request Syntax**
        ::

          response = client.get_crawler(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the crawler to retrieve metadata for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Crawler': {
                    'Name': 'string',
                    'Role': 'string',
                    'Targets': {
                        'S3Targets': [
                            {
                                'Path': 'string',
                                'Exclusions': [
                                    'string',
                                ]
                            },
                        ],
                        'JdbcTargets': [
                            {
                                'ConnectionName': 'string',
                                'Path': 'string',
                                'Exclusions': [
                                    'string',
                                ]
                            },
                        ],
                        'DynamoDBTargets': [
                            {
                                'Path': 'string'
                            },
                        ],
                        'CatalogTargets': [
                            {
                                'DatabaseName': 'string',
                                'Tables': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'DatabaseName': 'string',
                    'Description': 'string',
                    'Classifiers': [
                        'string',
                    ],
                    'SchemaChangePolicy': {
                        'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                        'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
                    },
                    'State': 'READY'|'RUNNING'|'STOPPING',
                    'TablePrefix': 'string',
                    'Schedule': {
                        'ScheduleExpression': 'string',
                        'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
                    },
                    'CrawlElapsedTime': 123,
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'LastCrawl': {
                        'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                        'ErrorMessage': 'string',
                        'LogGroup': 'string',
                        'LogStream': 'string',
                        'MessagePrefix': 'string',
                        'StartTime': datetime(2015, 1, 1)
                    },
                    'Version': 123,
                    'Configuration': 'string',
                    'CrawlerSecurityConfiguration': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Crawler** *(dict) --*

              The metadata for the specified crawler.

              - **Name** *(string) --*

                The name of the crawler.

              - **Role** *(string) --*

                The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources,
                such as Amazon Simple Storage Service (Amazon S3) data.

              - **Targets** *(dict) --*

                A collection of targets to crawl.

                - **S3Targets** *(list) --*

                  Specifies Amazon Simple Storage Service (Amazon S3) targets.

                  - *(dict) --*

                    Specifies a data store in Amazon Simple Storage Service (Amazon S3).

                    - **Path** *(string) --*

                      The path to the Amazon S3 target.

                    - **Exclusions** *(list) --*

                      A list of glob patterns used to exclude from the crawl. For more information, see
                      `Catalog Tables with a Crawler
                      <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                      - *(string) --*

                - **JdbcTargets** *(list) --*

                  Specifies JDBC targets.

                  - *(dict) --*

                    Specifies a JDBC data store to crawl.

                    - **ConnectionName** *(string) --*

                      The name of the connection to use to connect to the JDBC target.

                    - **Path** *(string) --*

                      The path of the JDBC target.

                    - **Exclusions** *(list) --*

                      A list of glob patterns used to exclude from the crawl. For more information, see
                      `Catalog Tables with a Crawler
                      <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                      - *(string) --*

                - **DynamoDBTargets** *(list) --*

                  Specifies Amazon DynamoDB targets.

                  - *(dict) --*

                    Specifies an Amazon DynamoDB table to crawl.

                    - **Path** *(string) --*

                      The name of the DynamoDB table to crawl.

                - **CatalogTargets** *(list) --*

                  Specifies AWS Glue Data Catalog targets.

                  - *(dict) --*

                    Specifies an AWS Glue Data Catalog target.

                    - **DatabaseName** *(string) --*

                      The name of the database to be synchronized.

                    - **Tables** *(list) --*

                      A list of the tables to be synchronized.

                      - *(string) --*

              - **DatabaseName** *(string) --*

                The name of the database in which the crawler's output is stored.

              - **Description** *(string) --*

                A description of the crawler.

              - **Classifiers** *(list) --*

                A list of UTF-8 strings that specify the custom classifiers that are associated with the
                crawler.

                - *(string) --*

              - **SchemaChangePolicy** *(dict) --*

                The policy that specifies update and delete behaviors for the crawler.

                - **UpdateBehavior** *(string) --*

                  The update behavior when the crawler finds a changed schema.

                - **DeleteBehavior** *(string) --*

                  The deletion behavior when the crawler finds a deleted object.

              - **State** *(string) --*

                Indicates whether the crawler is running, or whether a run is pending.

              - **TablePrefix** *(string) --*

                The prefix added to the names of tables that are created.

              - **Schedule** *(dict) --*

                For scheduled crawlers, the schedule when the crawler runs.

                - **ScheduleExpression** *(string) --*

                  A ``cron`` expression used to specify the schedule. For more information, see `Time-Based
                  Schedules for Jobs and Crawlers
                  <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For
                  example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

                - **State** *(string) --*

                  The state of the schedule.

              - **CrawlElapsedTime** *(integer) --*

                If the crawler is running, contains the total time elapsed since the last crawl began.

              - **CreationTime** *(datetime) --*

                The time that the crawler was created.

              - **LastUpdated** *(datetime) --*

                The time that the crawler was last updated.

              - **LastCrawl** *(dict) --*

                The status of the last crawl, and potentially error information if an error occurred.

                - **Status** *(string) --*

                  Status of the last crawl.

                - **ErrorMessage** *(string) --*

                  If an error occurred, the error information about the last crawl.

                - **LogGroup** *(string) --*

                  The log group for the last crawl.

                - **LogStream** *(string) --*

                  The log stream for the last crawl.

                - **MessagePrefix** *(string) --*

                  The prefix for a message about this crawl.

                - **StartTime** *(datetime) --*

                  The time at which the crawl started.

              - **Version** *(integer) --*

                The version of the crawler.

              - **Configuration** *(string) --*

                Crawler configuration information. This versioned JSON string allows users to specify
                aspects of a crawler's behavior. For more information, see `Configuring a Crawler
                <http://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`__ .

              - **CrawlerSecurityConfiguration** *(string) --*

                The name of the ``SecurityConfiguration`` structure to be used by this crawler.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_crawler_metrics(
        self,
        CrawlerNameList: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetCrawlerMetricsResponseTypeDef:
        """
        Retrieves metrics about specified crawlers.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawlerMetrics>`_

        **Request Syntax**
        ::

          response = client.get_crawler_metrics(
              CrawlerNameList=[
                  'string',
              ],
              MaxResults=123,
              NextToken='string'
          )
        :type CrawlerNameList: list
        :param CrawlerNameList:

          A list of the names of crawlers about which to retrieve metrics.

          - *(string) --*

        :type MaxResults: integer
        :param MaxResults:

          The maximum size of a list to return.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CrawlerMetricsList': [
                    {
                        'CrawlerName': 'string',
                        'TimeLeftSeconds': 123.0,
                        'StillEstimating': True|False,
                        'LastRuntimeSeconds': 123.0,
                        'MedianRuntimeSeconds': 123.0,
                        'TablesCreated': 123,
                        'TablesUpdated': 123,
                        'TablesDeleted': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **CrawlerMetricsList** *(list) --*

              A list of metrics for the specified crawler.

              - *(dict) --*

                Metrics for a specified crawler.

                - **CrawlerName** *(string) --*

                  The name of the crawler.

                - **TimeLeftSeconds** *(float) --*

                  The estimated time left to complete a running crawl.

                - **StillEstimating** *(boolean) --*

                  True if the crawler is still estimating how long it will take to complete this run.

                - **LastRuntimeSeconds** *(float) --*

                  The duration of the crawler's most recent run, in seconds.

                - **MedianRuntimeSeconds** *(float) --*

                  The median duration of this crawler's runs, in seconds.

                - **TablesCreated** *(integer) --*

                  The number of tables created by this crawler.

                - **TablesUpdated** *(integer) --*

                  The number of tables updated by this crawler.

                - **TablesDeleted** *(integer) --*

                  The number of tables deleted by this crawler.

            - **NextToken** *(string) --*

              A continuation token, if the returned list does not contain the last metric available.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_crawlers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetCrawlersResponseTypeDef:
        """
        Retrieves metadata for all crawlers defined in the customer account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawlers>`_

        **Request Syntax**
        ::

          response = client.get_crawlers(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The number of crawlers to return on each call.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Crawlers': [
                    {
                        'Name': 'string',
                        'Role': 'string',
                        'Targets': {
                            'S3Targets': [
                                {
                                    'Path': 'string',
                                    'Exclusions': [
                                        'string',
                                    ]
                                },
                            ],
                            'JdbcTargets': [
                                {
                                    'ConnectionName': 'string',
                                    'Path': 'string',
                                    'Exclusions': [
                                        'string',
                                    ]
                                },
                            ],
                            'DynamoDBTargets': [
                                {
                                    'Path': 'string'
                                },
                            ],
                            'CatalogTargets': [
                                {
                                    'DatabaseName': 'string',
                                    'Tables': [
                                        'string',
                                    ]
                                },
                            ]
                        },
                        'DatabaseName': 'string',
                        'Description': 'string',
                        'Classifiers': [
                            'string',
                        ],
                        'SchemaChangePolicy': {
                            'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                            'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
                        },
                        'State': 'READY'|'RUNNING'|'STOPPING',
                        'TablePrefix': 'string',
                        'Schedule': {
                            'ScheduleExpression': 'string',
                            'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
                        },
                        'CrawlElapsedTime': 123,
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'LastCrawl': {
                            'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                            'ErrorMessage': 'string',
                            'LogGroup': 'string',
                            'LogStream': 'string',
                            'MessagePrefix': 'string',
                            'StartTime': datetime(2015, 1, 1)
                        },
                        'Version': 123,
                        'Configuration': 'string',
                        'CrawlerSecurityConfiguration': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Crawlers** *(list) --*

              A list of crawler metadata.

              - *(dict) --*

                Specifies a crawler program that examines a data source and uses classifiers to try to
                determine its schema. If successful, the crawler records metadata concerning the data
                source in the AWS Glue Data Catalog.

                - **Name** *(string) --*

                  The name of the crawler.

                - **Role** *(string) --*

                  The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources,
                  such as Amazon Simple Storage Service (Amazon S3) data.

                - **Targets** *(dict) --*

                  A collection of targets to crawl.

                  - **S3Targets** *(list) --*

                    Specifies Amazon Simple Storage Service (Amazon S3) targets.

                    - *(dict) --*

                      Specifies a data store in Amazon Simple Storage Service (Amazon S3).

                      - **Path** *(string) --*

                        The path to the Amazon S3 target.

                      - **Exclusions** *(list) --*

                        A list of glob patterns used to exclude from the crawl. For more information, see
                        `Catalog Tables with a Crawler
                        <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                        - *(string) --*

                  - **JdbcTargets** *(list) --*

                    Specifies JDBC targets.

                    - *(dict) --*

                      Specifies a JDBC data store to crawl.

                      - **ConnectionName** *(string) --*

                        The name of the connection to use to connect to the JDBC target.

                      - **Path** *(string) --*

                        The path of the JDBC target.

                      - **Exclusions** *(list) --*

                        A list of glob patterns used to exclude from the crawl. For more information, see
                        `Catalog Tables with a Crawler
                        <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                        - *(string) --*

                  - **DynamoDBTargets** *(list) --*

                    Specifies Amazon DynamoDB targets.

                    - *(dict) --*

                      Specifies an Amazon DynamoDB table to crawl.

                      - **Path** *(string) --*

                        The name of the DynamoDB table to crawl.

                  - **CatalogTargets** *(list) --*

                    Specifies AWS Glue Data Catalog targets.

                    - *(dict) --*

                      Specifies an AWS Glue Data Catalog target.

                      - **DatabaseName** *(string) --*

                        The name of the database to be synchronized.

                      - **Tables** *(list) --*

                        A list of the tables to be synchronized.

                        - *(string) --*

                - **DatabaseName** *(string) --*

                  The name of the database in which the crawler's output is stored.

                - **Description** *(string) --*

                  A description of the crawler.

                - **Classifiers** *(list) --*

                  A list of UTF-8 strings that specify the custom classifiers that are associated with the
                  crawler.

                  - *(string) --*

                - **SchemaChangePolicy** *(dict) --*

                  The policy that specifies update and delete behaviors for the crawler.

                  - **UpdateBehavior** *(string) --*

                    The update behavior when the crawler finds a changed schema.

                  - **DeleteBehavior** *(string) --*

                    The deletion behavior when the crawler finds a deleted object.

                - **State** *(string) --*

                  Indicates whether the crawler is running, or whether a run is pending.

                - **TablePrefix** *(string) --*

                  The prefix added to the names of tables that are created.

                - **Schedule** *(dict) --*

                  For scheduled crawlers, the schedule when the crawler runs.

                  - **ScheduleExpression** *(string) --*

                    A ``cron`` expression used to specify the schedule. For more information, see
                    `Time-Based Schedules for Jobs and Crawlers
                    <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ .
                    For example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

                  - **State** *(string) --*

                    The state of the schedule.

                - **CrawlElapsedTime** *(integer) --*

                  If the crawler is running, contains the total time elapsed since the last crawl began.

                - **CreationTime** *(datetime) --*

                  The time that the crawler was created.

                - **LastUpdated** *(datetime) --*

                  The time that the crawler was last updated.

                - **LastCrawl** *(dict) --*

                  The status of the last crawl, and potentially error information if an error occurred.

                  - **Status** *(string) --*

                    Status of the last crawl.

                  - **ErrorMessage** *(string) --*

                    If an error occurred, the error information about the last crawl.

                  - **LogGroup** *(string) --*

                    The log group for the last crawl.

                  - **LogStream** *(string) --*

                    The log stream for the last crawl.

                  - **MessagePrefix** *(string) --*

                    The prefix for a message about this crawl.

                  - **StartTime** *(datetime) --*

                    The time at which the crawl started.

                - **Version** *(integer) --*

                  The version of the crawler.

                - **Configuration** *(string) --*

                  Crawler configuration information. This versioned JSON string allows users to specify
                  aspects of a crawler's behavior. For more information, see `Configuring a Crawler
                  <http://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`__ .

                - **CrawlerSecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used by this crawler.

            - **NextToken** *(string) --*

              A continuation token, if the returned list has not reached the end of those defined in this
              customer account.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_data_catalog_encryption_settings(
        self, CatalogId: str = None
    ) -> ClientGetDataCatalogEncryptionSettingsResponseTypeDef:
        """
        Retrieves the security configuration for a specified catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDataCatalogEncryptionSettings>`_

        **Request Syntax**
        ::

          response = client.get_data_catalog_encryption_settings(
              CatalogId='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog to retrieve the security configuration for. If none is provided, the
          AWS account ID is used by default.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DataCatalogEncryptionSettings': {
                    'EncryptionAtRest': {
                        'CatalogEncryptionMode': 'DISABLED'|'SSE-KMS',
                        'SseAwsKmsKeyId': 'string'
                    },
                    'ConnectionPasswordEncryption': {
                        'ReturnConnectionPasswordEncrypted': True|False,
                        'AwsKmsKeyId': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **DataCatalogEncryptionSettings** *(dict) --*

              The requested security configuration.

              - **EncryptionAtRest** *(dict) --*

                Specifies the encryption-at-rest configuration for the Data Catalog.

                - **CatalogEncryptionMode** *(string) --*

                  The encryption-at-rest mode for encrypting Data Catalog data.

                - **SseAwsKmsKeyId** *(string) --*

                  The ID of the AWS KMS key to use for encryption at rest.

              - **ConnectionPasswordEncryption** *(dict) --*

                When connection password protection is enabled, the Data Catalog uses a customer-provided
                key to encrypt the password as part of ``CreateConnection`` or ``UpdateConnection`` and
                store it in the ``ENCRYPTED_PASSWORD`` field in the connection properties. You can enable
                catalog encryption or only password encryption.

                - **ReturnConnectionPasswordEncrypted** *(boolean) --*

                  When the ``ReturnConnectionPasswordEncrypted`` flag is set to "true", passwords remain
                  encrypted in the responses of ``GetConnection`` and ``GetConnections`` . This encryption
                  takes effect independently from catalog encryption.

                - **AwsKmsKeyId** *(string) --*

                  An AWS KMS key that is used to encrypt the connection password.

                  If connection password protection is enabled, the caller of ``CreateConnection`` and
                  ``UpdateConnection`` needs at least ``kms:Encrypt`` permission on the specified AWS KMS
                  key, to encrypt passwords before storing them in the Data Catalog.

                  You can set the decrypt permission to enable or restrict access on the password key
                  according to your security requirements.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_database(
        self, Name: str, CatalogId: str = None
    ) -> ClientGetDatabaseResponseTypeDef:
        """
        Retrieves the definition of a specified database.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDatabase>`_

        **Request Syntax**
        ::

          response = client.get_database(
              CatalogId='string',
              Name='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the database resides. If none is provided, the AWS account ID
          is used by default.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the database to retrieve. For Hive compatibility, this should be all lowercase.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Database': {
                    'Name': 'string',
                    'Description': 'string',
                    'LocationUri': 'string',
                    'Parameters': {
                        'string': 'string'
                    },
                    'CreateTime': datetime(2015, 1, 1),
                    'CreateTableDefaultPermissions': [
                        {
                            'Principal': {
                                'DataLakePrincipalIdentifier': 'string'
                            },
                            'Permissions': [
                                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                                |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Database** *(dict) --*

              The definition of the specified database in the Data Catalog.

              - **Name** *(string) --*

                The name of the database. For Hive compatibility, this is folded to lowercase when it is
                stored.

              - **Description** *(string) --*

                A description of the database.

              - **LocationUri** *(string) --*

                The location of the database (for example, an HDFS path).

              - **Parameters** *(dict) --*

                These key-value pairs define parameters and properties of the database.

                - *(string) --*

                  - *(string) --*

              - **CreateTime** *(datetime) --*

                The time at which the metadata database was created in the catalog.

              - **CreateTableDefaultPermissions** *(list) --*

                Creates a set of default permissions on the table for principals.

                - *(dict) --*

                  Permissions granted to a principal.

                  - **Principal** *(dict) --*

                    The principal who is granted permissions.

                    - **DataLakePrincipalIdentifier** *(string) --*

                      An identifier for the AWS Lake Formation principal.

                  - **Permissions** *(list) --*

                    The permissions that are granted to the principal.

                    - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_databases(
        self, CatalogId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetDatabasesResponseTypeDef:
        """
        Retrieves all databases defined in a given Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDatabases>`_

        **Request Syntax**
        ::

          response = client.get_databases(
              CatalogId='string',
              NextToken='string',
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog from which to retrieve ``Databases`` . If none is provided, the AWS
          account ID is used by default.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of databases to return in one response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DatabaseList': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'LocationUri': 'string',
                        'Parameters': {
                            'string': 'string'
                        },
                        'CreateTime': datetime(2015, 1, 1),
                        'CreateTableDefaultPermissions': [
                            {
                                'Principal': {
                                    'DataLakePrincipalIdentifier': 'string'
                                },
                                'Permissions': [
                                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                                    |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                                ]
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DatabaseList** *(list) --*

              A list of ``Database`` objects from the specified catalog.

              - *(dict) --*

                The ``Database`` object represents a logical grouping of tables that might reside in a Hive
                metastore or an RDBMS.

                - **Name** *(string) --*

                  The name of the database. For Hive compatibility, this is folded to lowercase when it is
                  stored.

                - **Description** *(string) --*

                  A description of the database.

                - **LocationUri** *(string) --*

                  The location of the database (for example, an HDFS path).

                - **Parameters** *(dict) --*

                  These key-value pairs define parameters and properties of the database.

                  - *(string) --*

                    - *(string) --*

                - **CreateTime** *(datetime) --*

                  The time at which the metadata database was created in the catalog.

                - **CreateTableDefaultPermissions** *(list) --*

                  Creates a set of default permissions on the table for principals.

                  - *(dict) --*

                    Permissions granted to a principal.

                    - **Principal** *(dict) --*

                      The principal who is granted permissions.

                      - **DataLakePrincipalIdentifier** *(string) --*

                        An identifier for the AWS Lake Formation principal.

                    - **Permissions** *(list) --*

                      The permissions that are granted to the principal.

                      - *(string) --*

            - **NextToken** *(string) --*

              A continuation token for paginating the returned list of tokens, returned if the current
              segment of the list is not the last.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dataflow_graph(
        self, PythonScript: str = None
    ) -> ClientGetDataflowGraphResponseTypeDef:
        """
        Transforms a Python script into a directed acyclic graph (DAG).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDataflowGraph>`_

        **Request Syntax**
        ::

          response = client.get_dataflow_graph(
              PythonScript='string'
          )
        :type PythonScript: string
        :param PythonScript:

          The Python script to transform.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DagNodes': [
                    {
                        'Id': 'string',
                        'NodeType': 'string',
                        'Args': [
                            {
                                'Name': 'string',
                                'Value': 'string',
                                'Param': True|False
                            },
                        ],
                        'LineNumber': 123
                    },
                ],
                'DagEdges': [
                    {
                        'Source': 'string',
                        'Target': 'string',
                        'TargetParameter': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **DagNodes** *(list) --*

              A list of the nodes in the resulting DAG.

              - *(dict) --*

                Represents a node in a directed acyclic graph (DAG)

                - **Id** *(string) --*

                  A node identifier that is unique within the node's graph.

                - **NodeType** *(string) --*

                  The type of node that this is.

                - **Args** *(list) --*

                  Properties of the node, in the form of name-value pairs.

                  - *(dict) --*

                    An argument or property of a node.

                    - **Name** *(string) --*

                      The name of the argument or property.

                    - **Value** *(string) --*

                      The value of the argument or property.

                    - **Param** *(boolean) --*

                      True if the value is used as a parameter.

                - **LineNumber** *(integer) --*

                  The line number of the node.

            - **DagEdges** *(list) --*

              A list of the edges in the resulting DAG.

              - *(dict) --*

                Represents a directional edge in a directed acyclic graph (DAG).

                - **Source** *(string) --*

                  The ID of the node at which the edge starts.

                - **Target** *(string) --*

                  The ID of the node at which the edge ends.

                - **TargetParameter** *(string) --*

                  The target of the edge.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dev_endpoint(
        self, EndpointName: str
    ) -> ClientGetDevEndpointResponseTypeDef:
        """
        Retrieves information about a specified development endpoint.

        .. note::

          When you create a development endpoint in a virtual private cloud (VPC), AWS Glue returns only a
          private IP address, and the public IP address field is not populated. When you create a non-VPC
          development endpoint, AWS Glue returns only a public IP address.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDevEndpoint>`_

        **Request Syntax**
        ::

          response = client.get_dev_endpoint(
              EndpointName='string'
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**

          Name of the ``DevEndpoint`` to retrieve information for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DevEndpoint': {
                    'EndpointName': 'string',
                    'RoleArn': 'string',
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'SubnetId': 'string',
                    'YarnEndpointAddress': 'string',
                    'PrivateAddress': 'string',
                    'ZeppelinRemoteSparkInterpreterPort': 123,
                    'PublicAddress': 'string',
                    'Status': 'string',
                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                    'GlueVersion': 'string',
                    'NumberOfWorkers': 123,
                    'NumberOfNodes': 123,
                    'AvailabilityZone': 'string',
                    'VpcId': 'string',
                    'ExtraPythonLibsS3Path': 'string',
                    'ExtraJarsS3Path': 'string',
                    'FailureReason': 'string',
                    'LastUpdateStatus': 'string',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'LastModifiedTimestamp': datetime(2015, 1, 1),
                    'PublicKey': 'string',
                    'PublicKeys': [
                        'string',
                    ],
                    'SecurityConfiguration': 'string',
                    'Arguments': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **DevEndpoint** *(dict) --*

              A ``DevEndpoint`` definition.

              - **EndpointName** *(string) --*

                The name of the ``DevEndpoint`` .

              - **RoleArn** *(string) --*

                The Amazon Resource Name (ARN) of the IAM role used in this ``DevEndpoint`` .

              - **SecurityGroupIds** *(list) --*

                A list of security group identifiers used in this ``DevEndpoint`` .

                - *(string) --*

              - **SubnetId** *(string) --*

                The subnet ID for this ``DevEndpoint`` .

              - **YarnEndpointAddress** *(string) --*

                The YARN endpoint address used by this ``DevEndpoint`` .

              - **PrivateAddress** *(string) --*

                A private IP address to access the ``DevEndpoint`` within a VPC if the ``DevEndpoint`` is
                created within one. The ``PrivateAddress`` field is present only when you create the
                ``DevEndpoint`` within your VPC.

              - **ZeppelinRemoteSparkInterpreterPort** *(integer) --*

                The Apache Zeppelin port for the remote Apache Spark interpreter.

              - **PublicAddress** *(string) --*

                The public IP address used by this ``DevEndpoint`` . The ``PublicAddress`` field is present
                only when you create a non-virtual private cloud (VPC) ``DevEndpoint`` .

              - **Status** *(string) --*

                The current status of this ``DevEndpoint`` .

              - **WorkerType** *(string) --*

                The type of predefined worker that is allocated to the development endpoint. Accepts a
                value of Standard, G.1X, or G.2X.

                * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB
                disk, and 2 executors per worker.

                * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB
                disk), and provides 1 executor per worker. We recommend this worker type for
                memory-intensive jobs.

                * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB
                disk), and provides 1 executor per worker. We recommend this worker type for
                memory-intensive jobs.

                Known issue: when a development endpoint is created with the ``G.2X``  ``WorkerType``
                configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of
                memory, and a 64 GB disk.

              - **GlueVersion** *(string) --*

                Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The
                Python version indicates the version supported for running your ETL scripts on development
                endpoints.

                For more information about the available AWS Glue versions and corresponding Spark and
                Python versions, see `Glue version
                <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer guide.

                Development endpoints that are created without specifying a Glue version default to Glue
                0.9.

                You can specify a version of Python support for development endpoints by using the
                ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no
                arguments are provided, the version defaults to Python 2.

              - **NumberOfWorkers** *(integer) --*

                The number of workers of a defined ``workerType`` that are allocated to the development
                endpoint.

                The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

              - **NumberOfNodes** *(integer) --*

                The number of AWS Glue Data Processing Units (DPUs) allocated to this ``DevEndpoint`` .

              - **AvailabilityZone** *(string) --*

                The AWS Availability Zone where this ``DevEndpoint`` is located.

              - **VpcId** *(string) --*

                The ID of the virtual private cloud (VPC) used by this ``DevEndpoint`` .

              - **ExtraPythonLibsS3Path** *(string) --*

                The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in
                your ``DevEndpoint`` . Multiple values must be complete paths separated by a comma.

                .. note::

                  You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on C
                  extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis
                  library, are not currently supported.

              - **ExtraJarsS3Path** *(string) --*

                The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your
                ``DevEndpoint`` .

                .. note::

                  You can only use pure Java/Scala libraries with a ``DevEndpoint`` .

              - **FailureReason** *(string) --*

                The reason for a current failure in this ``DevEndpoint`` .

              - **LastUpdateStatus** *(string) --*

                The status of the last update.

              - **CreatedTimestamp** *(datetime) --*

                The point in time at which this DevEndpoint was created.

              - **LastModifiedTimestamp** *(datetime) --*

                The point in time at which this ``DevEndpoint`` was last modified.

              - **PublicKey** *(string) --*

                The public key to be used by this ``DevEndpoint`` for authentication. This attribute is
                provided for backward compatibility because the recommended attribute to use is public keys.

              - **PublicKeys** *(list) --*

                A list of public keys to be used by the ``DevEndpoints`` for authentication. Using this
                attribute is preferred over a single public key because the public keys allow you to have a
                different private key per client.

                .. note::

                  If you previously created an endpoint with a public key, you must remove that key to be
                  able to set a list of public keys. Call the ``UpdateDevEndpoint`` API operation with the
                  public key content in the ``deletePublicKeys`` attribute, and the list of new keys in the
                  ``addPublicKeys`` attribute.

                - *(string) --*

              - **SecurityConfiguration** *(string) --*

                The name of the ``SecurityConfiguration`` structure to be used with this ``DevEndpoint`` .

              - **Arguments** *(dict) --*

                A map of arguments used to configure the ``DevEndpoint`` .

                Valid arguments are:

                * ``"--enable-glue-datacatalog": ""``

                * ``"GLUE_PYTHON_VERSION": "3"``

                * ``"GLUE_PYTHON_VERSION": "2"``

                You can specify a version of Python support for development endpoints by using the
                ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no
                arguments are provided, the version defaults to Python 2.

                - *(string) --*

                  - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dev_endpoints(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetDevEndpointsResponseTypeDef:
        """
        Retrieves all the development endpoints in this AWS account.

        .. note::

          When you create a development endpoint in a virtual private cloud (VPC), AWS Glue returns only a
          private IP address and the public IP address field is not populated. When you create a non-VPC
          development endpoint, AWS Glue returns only a public IP address.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDevEndpoints>`_

        **Request Syntax**
        ::

          response = client.get_dev_endpoints(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The maximum size of information to return.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DevEndpoints': [
                    {
                        'EndpointName': 'string',
                        'RoleArn': 'string',
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'SubnetId': 'string',
                        'YarnEndpointAddress': 'string',
                        'PrivateAddress': 'string',
                        'ZeppelinRemoteSparkInterpreterPort': 123,
                        'PublicAddress': 'string',
                        'Status': 'string',
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'GlueVersion': 'string',
                        'NumberOfWorkers': 123,
                        'NumberOfNodes': 123,
                        'AvailabilityZone': 'string',
                        'VpcId': 'string',
                        'ExtraPythonLibsS3Path': 'string',
                        'ExtraJarsS3Path': 'string',
                        'FailureReason': 'string',
                        'LastUpdateStatus': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'LastModifiedTimestamp': datetime(2015, 1, 1),
                        'PublicKey': 'string',
                        'PublicKeys': [
                            'string',
                        ],
                        'SecurityConfiguration': 'string',
                        'Arguments': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DevEndpoints** *(list) --*

              A list of ``DevEndpoint`` definitions.

              - *(dict) --*

                A development endpoint where a developer can remotely debug extract, transform, and load
                (ETL) scripts.

                - **EndpointName** *(string) --*

                  The name of the ``DevEndpoint`` .

                - **RoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role used in this ``DevEndpoint`` .

                - **SecurityGroupIds** *(list) --*

                  A list of security group identifiers used in this ``DevEndpoint`` .

                  - *(string) --*

                - **SubnetId** *(string) --*

                  The subnet ID for this ``DevEndpoint`` .

                - **YarnEndpointAddress** *(string) --*

                  The YARN endpoint address used by this ``DevEndpoint`` .

                - **PrivateAddress** *(string) --*

                  A private IP address to access the ``DevEndpoint`` within a VPC if the ``DevEndpoint`` is
                  created within one. The ``PrivateAddress`` field is present only when you create the
                  ``DevEndpoint`` within your VPC.

                - **ZeppelinRemoteSparkInterpreterPort** *(integer) --*

                  The Apache Zeppelin port for the remote Apache Spark interpreter.

                - **PublicAddress** *(string) --*

                  The public IP address used by this ``DevEndpoint`` . The ``PublicAddress`` field is
                  present only when you create a non-virtual private cloud (VPC) ``DevEndpoint`` .

                - **Status** *(string) --*

                  The current status of this ``DevEndpoint`` .

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated to the development endpoint. Accepts a
                  value of Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a
                  50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB
                  disk), and provides 1 executor per worker. We recommend this worker type for
                  memory-intensive jobs.

                  * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128
                  GB disk), and provides 1 executor per worker. We recommend this worker type for
                  memory-intensive jobs.

                  Known issue: when a development endpoint is created with the ``G.2X``  ``WorkerType``
                  configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB
                  of memory, and a 64 GB disk.

                - **GlueVersion** *(string) --*

                  Glue version determines the versions of Apache Spark and Python that AWS Glue supports.
                  The Python version indicates the version supported for running your ETL scripts on
                  development endpoints.

                  For more information about the available AWS Glue versions and corresponding Spark and
                  Python versions, see `Glue version
                  <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer guide.

                  Development endpoints that are created without specifying a Glue version default to Glue
                  0.9.

                  You can specify a version of Python support for development endpoints by using the
                  ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no
                  arguments are provided, the version defaults to Python 2.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated to the development
                  endpoint.

                  The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

                - **NumberOfNodes** *(integer) --*

                  The number of AWS Glue Data Processing Units (DPUs) allocated to this ``DevEndpoint`` .

                - **AvailabilityZone** *(string) --*

                  The AWS Availability Zone where this ``DevEndpoint`` is located.

                - **VpcId** *(string) --*

                  The ID of the virtual private cloud (VPC) used by this ``DevEndpoint`` .

                - **ExtraPythonLibsS3Path** *(string) --*

                  The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in
                  your ``DevEndpoint`` . Multiple values must be complete paths separated by a comma.

                  .. note::

                    You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on
                    C extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis
                    library, are not currently supported.

                - **ExtraJarsS3Path** *(string) --*

                  The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your
                  ``DevEndpoint`` .

                  .. note::

                    You can only use pure Java/Scala libraries with a ``DevEndpoint`` .

                - **FailureReason** *(string) --*

                  The reason for a current failure in this ``DevEndpoint`` .

                - **LastUpdateStatus** *(string) --*

                  The status of the last update.

                - **CreatedTimestamp** *(datetime) --*

                  The point in time at which this DevEndpoint was created.

                - **LastModifiedTimestamp** *(datetime) --*

                  The point in time at which this ``DevEndpoint`` was last modified.

                - **PublicKey** *(string) --*

                  The public key to be used by this ``DevEndpoint`` for authentication. This attribute is
                  provided for backward compatibility because the recommended attribute to use is public
                  keys.

                - **PublicKeys** *(list) --*

                  A list of public keys to be used by the ``DevEndpoints`` for authentication. Using this
                  attribute is preferred over a single public key because the public keys allow you to have
                  a different private key per client.

                  .. note::

                    If you previously created an endpoint with a public key, you must remove that key to be
                    able to set a list of public keys. Call the ``UpdateDevEndpoint`` API operation with
                    the public key content in the ``deletePublicKeys`` attribute, and the list of new keys
                    in the ``addPublicKeys`` attribute.

                  - *(string) --*

                - **SecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used with this ``DevEndpoint`` .

                - **Arguments** *(dict) --*

                  A map of arguments used to configure the ``DevEndpoint`` .

                  Valid arguments are:

                  * ``"--enable-glue-datacatalog": ""``

                  * ``"GLUE_PYTHON_VERSION": "3"``

                  * ``"GLUE_PYTHON_VERSION": "2"``

                  You can specify a version of Python support for development endpoints by using the
                  ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no
                  arguments are provided, the version defaults to Python 2.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A continuation token, if not all ``DevEndpoint`` definitions have yet been returned.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job(self, JobName: str) -> ClientGetJobResponseTypeDef:
        """
        Retrieves an existing job definition.

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJob>`_

        **Request Syntax**
        ::

          response = client.get_job(
              JobName='string'
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job definition to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Job': {
                    'Name': 'string',
                    'Description': 'string',
                    'LogUri': 'string',
                    'Role': 'string',
                    'CreatedOn': datetime(2015, 1, 1),
                    'LastModifiedOn': datetime(2015, 1, 1),
                    'ExecutionProperty': {
                        'MaxConcurrentRuns': 123
                    },
                    'Command': {
                        'Name': 'string',
                        'ScriptLocation': 'string',
                        'PythonVersion': 'string'
                    },
                    'DefaultArguments': {
                        'string': 'string'
                    },
                    'Connections': {
                        'Connections': [
                            'string',
                        ]
                    },
                    'MaxRetries': 123,
                    'AllocatedCapacity': 123,
                    'Timeout': 123,
                    'MaxCapacity': 123.0,
                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                    'NumberOfWorkers': 123,
                    'SecurityConfiguration': 'string',
                    'NotificationProperty': {
                        'NotifyDelayAfter': 123
                    },
                    'GlueVersion': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Job** *(dict) --*

              The requested job definition.

              - **Name** *(string) --*

                The name you assign to this job definition.

              - **Description** *(string) --*

                A description of the job.

              - **LogUri** *(string) --*

                This field is reserved for future use.

              - **Role** *(string) --*

                The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

              - **CreatedOn** *(datetime) --*

                The time and date that this job definition was created.

              - **LastModifiedOn** *(datetime) --*

                The last point in time when this job definition was modified.

              - **ExecutionProperty** *(dict) --*

                An ``ExecutionProperty`` specifying the maximum number of concurrent runs allowed for this
                job.

                - **MaxConcurrentRuns** *(integer) --*

                  The maximum number of concurrent runs allowed for the job. The default is 1. An error is
                  returned when this threshold is reached. The maximum value you can specify is controlled
                  by a service limit.

              - **Command** *(dict) --*

                The ``JobCommand`` that executes this job.

                - **Name** *(string) --*

                  The name of the job command. For an Apache Spark ETL job, this must be ``glueetl`` . For
                  a Python shell job, it must be ``pythonshell`` .

                - **ScriptLocation** *(string) --*

                  Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a
                  job.

                - **PythonVersion** *(string) --*

                  The Python version being used to execute a Python shell job. Allowed values are 2 or 3.

              - **DefaultArguments** *(dict) --*

                The default arguments for this job, specified as name-value pairs.

                You can specify arguments here that your own job-execution script consumes, as well as
                arguments that AWS Glue itself consumes.

                For information about how to specify and consume your own Job arguments, see the `Calling
                AWS Glue APIs in Python
                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                topic in the developer guide.

                For information about the key-value pairs that AWS Glue consumes to set up your job, see
                the `Special Parameters Used by AWS Glue
                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                topic in the developer guide.

                - *(string) --*

                  - *(string) --*

              - **Connections** *(dict) --*

                The connections used for this job.

                - **Connections** *(list) --*

                  A list of connections used by the job.

                  - *(string) --*

              - **MaxRetries** *(integer) --*

                The maximum number of times to retry this job after a JobRun fails.

              - **AllocatedCapacity** *(integer) --*

                This field is deprecated. Use ``MaxCapacity`` instead.

                The number of AWS Glue data processing units (DPUs) allocated to runs of this job. You can
                allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing
                power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more
                information, see the `AWS Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .

              - **Timeout** *(integer) --*

                The job timeout in minutes. This is the maximum time that a job run can consume resources
                before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48
                hours).

              - **MaxCapacity** *(float) --*

                The number of AWS Glue data processing units (DPUs) that can be allocated when this job
                runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute
                capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page
                <https://aws.amazon.com/glue/pricing/>`__ .

                Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                The value that can be allocated for ``MaxCapacity`` depends on whether you are running a
                Python shell job or an Apache Spark ETL job:

                * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you can
                allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"), you can
                allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional
                DPU allocation.

              - **WorkerType** *(string) --*

                The type of predefined worker that is allocated when a job runs. Accepts a value of
                Standard, G.1X, or G.2X.

                * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB
                disk, and 2 executors per worker.

                * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB
                disk), and provides 1 executor per worker. We recommend this worker type for
                memory-intensive jobs.

                * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB
                disk), and provides 1 executor per worker. We recommend this worker type for
                memory-intensive jobs.

              - **NumberOfWorkers** *(integer) --*

                The number of workers of a defined ``workerType`` that are allocated when a job runs.

                The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

              - **SecurityConfiguration** *(string) --*

                The name of the ``SecurityConfiguration`` structure to be used with this job.

              - **NotificationProperty** *(dict) --*

                Specifies configuration properties of a job notification.

                - **NotifyDelayAfter** *(integer) --*

                  After a job run starts, the number of minutes to wait before sending a job run delay
                  notification.

              - **GlueVersion** *(string) --*

                Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The
                Python version indicates the version supported for jobs of type Spark.

                For more information about the available AWS Glue versions and corresponding Spark and
                Python versions, see `Glue version
                <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer guide.

                Jobs that are created without specifying a Glue version default to Glue 0.9.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_bookmark(
        self, JobName: str, RunId: str = None
    ) -> ClientGetJobBookmarkResponseTypeDef:
        """
        Returns information on a job bookmark entry.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobBookmark>`_

        **Request Syntax**
        ::

          response = client.get_job_bookmark(
              JobName='string',
              RunId='string'
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job in question.

        :type RunId: string
        :param RunId:

          The unique run identifier associated with this job run.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobBookmarkEntry': {
                    'JobName': 'string',
                    'Version': 123,
                    'Run': 123,
                    'Attempt': 123,
                    'PreviousRunId': 'string',
                    'RunId': 'string',
                    'JobBookmark': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **JobBookmarkEntry** *(dict) --*

              A structure that defines a point that a job can resume processing.

              - **JobName** *(string) --*

                The name of the job in question.

              - **Version** *(integer) --*

                The version of the job.

              - **Run** *(integer) --*

                The run ID number.

              - **Attempt** *(integer) --*

                The attempt ID number.

              - **PreviousRunId** *(string) --*

                The unique run identifier associated with the previous job run.

              - **RunId** *(string) --*

                The run ID number.

              - **JobBookmark** *(string) --*

                The bookmark itself.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_run(
        self, JobName: str, RunId: str, PredecessorsIncluded: bool = None
    ) -> ClientGetJobRunResponseTypeDef:
        """
        Retrieves the metadata for a given job run.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobRun>`_

        **Request Syntax**
        ::

          response = client.get_job_run(
              JobName='string',
              RunId='string',
              PredecessorsIncluded=True|False
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          Name of the job definition being run.

        :type RunId: string
        :param RunId: **[REQUIRED]**

          The ID of the job run.

        :type PredecessorsIncluded: boolean
        :param PredecessorsIncluded:

          True if a list of predecessor runs should be returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobRun': {
                    'Id': 'string',
                    'Attempt': 123,
                    'PreviousRunId': 'string',
                    'TriggerName': 'string',
                    'JobName': 'string',
                    'StartedOn': datetime(2015, 1, 1),
                    'LastModifiedOn': datetime(2015, 1, 1),
                    'CompletedOn': datetime(2015, 1, 1),
                    'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                    'Arguments': {
                        'string': 'string'
                    },
                    'ErrorMessage': 'string',
                    'PredecessorRuns': [
                        {
                            'JobName': 'string',
                            'RunId': 'string'
                        },
                    ],
                    'AllocatedCapacity': 123,
                    'ExecutionTime': 123,
                    'Timeout': 123,
                    'MaxCapacity': 123.0,
                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                    'NumberOfWorkers': 123,
                    'SecurityConfiguration': 'string',
                    'LogGroupName': 'string',
                    'NotificationProperty': {
                        'NotifyDelayAfter': 123
                    },
                    'GlueVersion': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **JobRun** *(dict) --*

              The requested job-run metadata.

              - **Id** *(string) --*

                The ID of this job run.

              - **Attempt** *(integer) --*

                The number of the attempt to run this job.

              - **PreviousRunId** *(string) --*

                The ID of the previous run of this job. For example, the ``JobRunId`` specified in the
                ``StartJobRun`` action.

              - **TriggerName** *(string) --*

                The name of the trigger that started this job run.

              - **JobName** *(string) --*

                The name of the job definition being used in this run.

              - **StartedOn** *(datetime) --*

                The date and time at which this job run was started.

              - **LastModifiedOn** *(datetime) --*

                The last time that this job run was modified.

              - **CompletedOn** *(datetime) --*

                The date and time that this job run completed.

              - **JobRunState** *(string) --*

                The current state of the job run.

              - **Arguments** *(dict) --*

                The job arguments associated with this run. For this job run, they replace the default
                arguments set in the job definition itself.

                You can specify arguments here that your own job-execution script consumes, as well as
                arguments that AWS Glue itself consumes.

                For information about how to specify and consume your own job arguments, see the `Calling
                AWS Glue APIs in Python
                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                topic in the developer guide.

                For information about the key-value pairs that AWS Glue consumes to set up your job, see
                the `Special Parameters Used by AWS Glue
                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                topic in the developer guide.

                - *(string) --*

                  - *(string) --*

              - **ErrorMessage** *(string) --*

                An error message associated with this job run.

              - **PredecessorRuns** *(list) --*

                A list of predecessors to this job run.

                - *(dict) --*

                  A job run that was used in the predicate of a conditional trigger that triggered this job
                  run.

                  - **JobName** *(string) --*

                    The name of the job definition used by the predecessor job run.

                  - **RunId** *(string) --*

                    The job-run ID of the predecessor job run.

              - **AllocatedCapacity** *(integer) --*

                This field is deprecated. Use ``MaxCapacity`` instead.

                The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100
                DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power
                that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see
                the `AWS Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .

              - **ExecutionTime** *(integer) --*

                The amount of time (in seconds) that the job run consumed resources.

              - **Timeout** *(integer) --*

                The ``JobRun`` timeout in minutes. This is the maximum time that a job run can consume
                resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880
                minutes (48 hours). This overrides the timeout value set in the parent job.

              - **MaxCapacity** *(float) --*

                The number of AWS Glue data processing units (DPUs) that can be allocated when this job
                runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute
                capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page
                <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                The value that can be allocated for ``MaxCapacity`` depends on whether you are running a
                Python shell job or an Apache Spark ETL job:

                * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you can
                allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"), you can
                allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional
                DPU allocation.

              - **WorkerType** *(string) --*

                The type of predefined worker that is allocated when a job runs. Accepts a value of
                Standard, G.1X, or G.2X.

                * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB
                disk, and 2 executors per worker.

                * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB
                disk, and 1 executor per worker.

                * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB
                disk, and 1 executor per worker.

              - **NumberOfWorkers** *(integer) --*

                The number of workers of a defined ``workerType`` that are allocated when a job runs.

                The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

              - **SecurityConfiguration** *(string) --*

                The name of the ``SecurityConfiguration`` structure to be used with this job run.

              - **LogGroupName** *(string) --*

                The name of the log group for secure logging that can be server-side encrypted in Amazon
                CloudWatch using AWS KMS. This name can be ``/aws-glue/jobs/`` , in which case the default
                encryption is ``NONE`` . If you add a role name and ``SecurityConfiguration`` name (in
                other words, ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that
                security configuration is used to encrypt the log group.

              - **NotificationProperty** *(dict) --*

                Specifies configuration properties of a job run notification.

                - **NotifyDelayAfter** *(integer) --*

                  After a job run starts, the number of minutes to wait before sending a job run delay
                  notification.

              - **GlueVersion** *(string) --*

                Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The
                Python version indicates the version supported for jobs of type Spark.

                For more information about the available AWS Glue versions and corresponding Spark and
                Python versions, see `Glue version
                <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer guide.

                Jobs that are created without specifying a Glue version default to Glue 0.9.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_runs(
        self, JobName: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetJobRunsResponseTypeDef:
        """
        Retrieves metadata for all runs of a given job definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobRuns>`_

        **Request Syntax**
        ::

          response = client.get_job_runs(
              JobName='string',
              NextToken='string',
              MaxResults=123
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job definition for which to retrieve all job runs.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :type MaxResults: integer
        :param MaxResults:

          The maximum size of the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobRuns': [
                    {
                        'Id': 'string',
                        'Attempt': 123,
                        'PreviousRunId': 'string',
                        'TriggerName': 'string',
                        'JobName': 'string',
                        'StartedOn': datetime(2015, 1, 1),
                        'LastModifiedOn': datetime(2015, 1, 1),
                        'CompletedOn': datetime(2015, 1, 1),
                        'JobRunState':
                        'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                        'Arguments': {
                            'string': 'string'
                        },
                        'ErrorMessage': 'string',
                        'PredecessorRuns': [
                            {
                                'JobName': 'string',
                                'RunId': 'string'
                            },
                        ],
                        'AllocatedCapacity': 123,
                        'ExecutionTime': 123,
                        'Timeout': 123,
                        'MaxCapacity': 123.0,
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'NumberOfWorkers': 123,
                        'SecurityConfiguration': 'string',
                        'LogGroupName': 'string',
                        'NotificationProperty': {
                            'NotifyDelayAfter': 123
                        },
                        'GlueVersion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobRuns** *(list) --*

              A list of job-run metadata objects.

              - *(dict) --*

                Contains information about a job run.

                - **Id** *(string) --*

                  The ID of this job run.

                - **Attempt** *(integer) --*

                  The number of the attempt to run this job.

                - **PreviousRunId** *(string) --*

                  The ID of the previous run of this job. For example, the ``JobRunId`` specified in the
                  ``StartJobRun`` action.

                - **TriggerName** *(string) --*

                  The name of the trigger that started this job run.

                - **JobName** *(string) --*

                  The name of the job definition being used in this run.

                - **StartedOn** *(datetime) --*

                  The date and time at which this job run was started.

                - **LastModifiedOn** *(datetime) --*

                  The last time that this job run was modified.

                - **CompletedOn** *(datetime) --*

                  The date and time that this job run completed.

                - **JobRunState** *(string) --*

                  The current state of the job run.

                - **Arguments** *(dict) --*

                  The job arguments associated with this run. For this job run, they replace the default
                  arguments set in the job definition itself.

                  You can specify arguments here that your own job-execution script consumes, as well as
                  arguments that AWS Glue itself consumes.

                  For information about how to specify and consume your own job arguments, see the `Calling
                  AWS Glue APIs in Python
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                  topic in the developer guide.

                  For information about the key-value pairs that AWS Glue consumes to set up your job, see
                  the `Special Parameters Used by AWS Glue
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                  topic in the developer guide.

                  - *(string) --*

                    - *(string) --*

                - **ErrorMessage** *(string) --*

                  An error message associated with this job run.

                - **PredecessorRuns** *(list) --*

                  A list of predecessors to this job run.

                  - *(dict) --*

                    A job run that was used in the predicate of a conditional trigger that triggered this
                    job run.

                    - **JobName** *(string) --*

                      The name of the job definition used by the predecessor job run.

                    - **RunId** *(string) --*

                      The job-run ID of the predecessor job run.

                - **AllocatedCapacity** *(integer) --*

                  This field is deprecated. Use ``MaxCapacity`` instead.

                  The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to
                  100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing
                  power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more
                  information, see the `AWS Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .

                - **ExecutionTime** *(integer) --*

                  The amount of time (in seconds) that the job run consumed resources.

                - **Timeout** *(integer) --*

                  The ``JobRun`` timeout in minutes. This is the maximum time that a job run can consume
                  resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880
                  minutes (48 hours). This overrides the timeout value set in the parent job.

                - **MaxCapacity** *(float) --*

                  The number of AWS Glue data processing units (DPUs) that can be allocated when this job
                  runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute
                  capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page
                  <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                  Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                  The value that can be allocated for ``MaxCapacity`` depends on whether you are running a
                  Python shell job or an Apache Spark ETL job:

                  * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you can
                  allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                  * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"), you can
                  allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a
                  fractional DPU allocation.

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated when a job runs. Accepts a value of
                  Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a
                  50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB
                  disk, and 1 executor per worker.

                  * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB
                  disk, and 1 executor per worker.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated when a job runs.

                  The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

                - **SecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used with this job run.

                - **LogGroupName** *(string) --*

                  The name of the log group for secure logging that can be server-side encrypted in Amazon
                  CloudWatch using AWS KMS. This name can be ``/aws-glue/jobs/`` , in which case the
                  default encryption is ``NONE`` . If you add a role name and ``SecurityConfiguration``
                  name (in other words, ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ),
                  then that security configuration is used to encrypt the log group.

                - **NotificationProperty** *(dict) --*

                  Specifies configuration properties of a job run notification.

                  - **NotifyDelayAfter** *(integer) --*

                    After a job run starts, the number of minutes to wait before sending a job run delay
                    notification.

                - **GlueVersion** *(string) --*

                  Glue version determines the versions of Apache Spark and Python that AWS Glue supports.
                  The Python version indicates the version supported for jobs of type Spark.

                  For more information about the available AWS Glue versions and corresponding Spark and
                  Python versions, see `Glue version
                  <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer guide.

                  Jobs that are created without specifying a Glue version default to Glue 0.9.

            - **NextToken** *(string) --*

              A continuation token, if not all requested job runs have been returned.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_jobs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetJobsResponseTypeDef:
        """
        Retrieves all current job definitions.

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobs>`_

        **Request Syntax**
        ::

          response = client.get_jobs(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :type MaxResults: integer
        :param MaxResults:

          The maximum size of the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Jobs': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'LogUri': 'string',
                        'Role': 'string',
                        'CreatedOn': datetime(2015, 1, 1),
                        'LastModifiedOn': datetime(2015, 1, 1),
                        'ExecutionProperty': {
                            'MaxConcurrentRuns': 123
                        },
                        'Command': {
                            'Name': 'string',
                            'ScriptLocation': 'string',
                            'PythonVersion': 'string'
                        },
                        'DefaultArguments': {
                            'string': 'string'
                        },
                        'Connections': {
                            'Connections': [
                                'string',
                            ]
                        },
                        'MaxRetries': 123,
                        'AllocatedCapacity': 123,
                        'Timeout': 123,
                        'MaxCapacity': 123.0,
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'NumberOfWorkers': 123,
                        'SecurityConfiguration': 'string',
                        'NotificationProperty': {
                            'NotifyDelayAfter': 123
                        },
                        'GlueVersion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Jobs** *(list) --*

              A list of job definitions.

              - *(dict) --*

                Specifies a job definition.

                - **Name** *(string) --*

                  The name you assign to this job definition.

                - **Description** *(string) --*

                  A description of the job.

                - **LogUri** *(string) --*

                  This field is reserved for future use.

                - **Role** *(string) --*

                  The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

                - **CreatedOn** *(datetime) --*

                  The time and date that this job definition was created.

                - **LastModifiedOn** *(datetime) --*

                  The last point in time when this job definition was modified.

                - **ExecutionProperty** *(dict) --*

                  An ``ExecutionProperty`` specifying the maximum number of concurrent runs allowed for
                  this job.

                  - **MaxConcurrentRuns** *(integer) --*

                    The maximum number of concurrent runs allowed for the job. The default is 1. An error
                    is returned when this threshold is reached. The maximum value you can specify is
                    controlled by a service limit.

                - **Command** *(dict) --*

                  The ``JobCommand`` that executes this job.

                  - **Name** *(string) --*

                    The name of the job command. For an Apache Spark ETL job, this must be ``glueetl`` .
                    For a Python shell job, it must be ``pythonshell`` .

                  - **ScriptLocation** *(string) --*

                    Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes
                    a job.

                  - **PythonVersion** *(string) --*

                    The Python version being used to execute a Python shell job. Allowed values are 2 or 3.

                - **DefaultArguments** *(dict) --*

                  The default arguments for this job, specified as name-value pairs.

                  You can specify arguments here that your own job-execution script consumes, as well as
                  arguments that AWS Glue itself consumes.

                  For information about how to specify and consume your own Job arguments, see the `Calling
                  AWS Glue APIs in Python
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                  topic in the developer guide.

                  For information about the key-value pairs that AWS Glue consumes to set up your job, see
                  the `Special Parameters Used by AWS Glue
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                  topic in the developer guide.

                  - *(string) --*

                    - *(string) --*

                - **Connections** *(dict) --*

                  The connections used for this job.

                  - **Connections** *(list) --*

                    A list of connections used by the job.

                    - *(string) --*

                - **MaxRetries** *(integer) --*

                  The maximum number of times to retry this job after a JobRun fails.

                - **AllocatedCapacity** *(integer) --*

                  This field is deprecated. Use ``MaxCapacity`` instead.

                  The number of AWS Glue data processing units (DPUs) allocated to runs of this job. You
                  can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of
                  processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For
                  more information, see the `AWS Glue pricing page
                  <https://aws.amazon.com/glue/pricing/>`__ .

                - **Timeout** *(integer) --*

                  The job timeout in minutes. This is the maximum time that a job run can consume resources
                  before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48
                  hours).

                - **MaxCapacity** *(float) --*

                  The number of AWS Glue data processing units (DPUs) that can be allocated when this job
                  runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute
                  capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page
                  <https://aws.amazon.com/glue/pricing/>`__ .

                  Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                  The value that can be allocated for ``MaxCapacity`` depends on whether you are running a
                  Python shell job or an Apache Spark ETL job:

                  * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you can
                  allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                  * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"), you can
                  allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a
                  fractional DPU allocation.

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated when a job runs. Accepts a value of
                  Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a
                  50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB
                  disk), and provides 1 executor per worker. We recommend this worker type for
                  memory-intensive jobs.

                  * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128
                  GB disk), and provides 1 executor per worker. We recommend this worker type for
                  memory-intensive jobs.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated when a job runs.

                  The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

                - **SecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used with this job.

                - **NotificationProperty** *(dict) --*

                  Specifies configuration properties of a job notification.

                  - **NotifyDelayAfter** *(integer) --*

                    After a job run starts, the number of minutes to wait before sending a job run delay
                    notification.

                - **GlueVersion** *(string) --*

                  Glue version determines the versions of Apache Spark and Python that AWS Glue supports.
                  The Python version indicates the version supported for jobs of type Spark.

                  For more information about the available AWS Glue versions and corresponding Spark and
                  Python versions, see `Glue version
                  <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer guide.

                  Jobs that are created without specifying a Glue version default to Glue 0.9.

            - **NextToken** *(string) --*

              A continuation token, if not all job definitions have yet been returned.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_mapping(
        self,
        Source: ClientGetMappingSourceTypeDef,
        Sinks: List[ClientGetMappingSinksTypeDef] = None,
        Location: ClientGetMappingLocationTypeDef = None,
    ) -> ClientGetMappingResponseTypeDef:
        """
        Creates mappings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetMapping>`_

        **Request Syntax**
        ::

          response = client.get_mapping(
              Source={
                  'DatabaseName': 'string',
                  'TableName': 'string'
              },
              Sinks=[
                  {
                      'DatabaseName': 'string',
                      'TableName': 'string'
                  },
              ],
              Location={
                  'Jdbc': [
                      {
                          'Name': 'string',
                          'Value': 'string',
                          'Param': True|False
                      },
                  ],
                  'S3': [
                      {
                          'Name': 'string',
                          'Value': 'string',
                          'Param': True|False
                      },
                  ],
                  'DynamoDB': [
                      {
                          'Name': 'string',
                          'Value': 'string',
                          'Param': True|False
                      },
                  ]
              }
          )
        :type Source: dict
        :param Source: **[REQUIRED]**

          Specifies the source table.

          - **DatabaseName** *(string) --* **[REQUIRED]**

            The database in which the table metadata resides.

          - **TableName** *(string) --* **[REQUIRED]**

            The name of the table in question.

        :type Sinks: list
        :param Sinks:

          A list of target tables.

          - *(dict) --*

            Specifies a table definition in the AWS Glue Data Catalog.

            - **DatabaseName** *(string) --* **[REQUIRED]**

              The database in which the table metadata resides.

            - **TableName** *(string) --* **[REQUIRED]**

              The name of the table in question.

        :type Location: dict
        :param Location:

          Parameters for the mapping.

          - **Jdbc** *(list) --*

            A JDBC location.

            - *(dict) --*

              An argument or property of a node.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the argument or property.

              - **Value** *(string) --* **[REQUIRED]**

                The value of the argument or property.

              - **Param** *(boolean) --*

                True if the value is used as a parameter.

          - **S3** *(list) --*

            An Amazon Simple Storage Service (Amazon S3) location.

            - *(dict) --*

              An argument or property of a node.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the argument or property.

              - **Value** *(string) --* **[REQUIRED]**

                The value of the argument or property.

              - **Param** *(boolean) --*

                True if the value is used as a parameter.

          - **DynamoDB** *(list) --*

            An Amazon DynamoDB table location.

            - *(dict) --*

              An argument or property of a node.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the argument or property.

              - **Value** *(string) --* **[REQUIRED]**

                The value of the argument or property.

              - **Param** *(boolean) --*

                True if the value is used as a parameter.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Mapping': [
                    {
                        'SourceTable': 'string',
                        'SourcePath': 'string',
                        'SourceType': 'string',
                        'TargetTable': 'string',
                        'TargetPath': 'string',
                        'TargetType': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Mapping** *(list) --*

              A list of mappings to the specified targets.

              - *(dict) --*

                Defines a mapping.

                - **SourceTable** *(string) --*

                  The name of the source table.

                - **SourcePath** *(string) --*

                  The source path.

                - **SourceType** *(string) --*

                  The source type.

                - **TargetTable** *(string) --*

                  The target table.

                - **TargetPath** *(string) --*

                  The target path.

                - **TargetType** *(string) --*

                  The target type.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ml_task_run(
        self, TransformId: str, TaskRunId: str
    ) -> ClientGetMlTaskRunResponseTypeDef:
        """
        Gets details for a specific task run on a machine learning transform. Machine learning task runs
        are asynchronous tasks that AWS Glue runs on your behalf as part of various machine learning
        workflows. You can check the stats of any task run by calling ``GetMLTaskRun`` with the
        ``TaskRunID`` and its parent transform's ``TransformID`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetMLTaskRun>`_

        **Request Syntax**
        ::

          response = client.get_ml_task_run(
              TransformId='string',
              TaskRunId='string'
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the machine learning transform.

        :type TaskRunId: string
        :param TaskRunId: **[REQUIRED]**

          The unique identifier of the task run.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TransformId': 'string',
                'TaskRunId': 'string',
                'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                'LogGroupName': 'string',
                'Properties': {
                    'TaskType':
                    'EVALUATION'|'LABELING_SET_GENERATION'|'IMPORT_LABELS'|'EXPORT_LABELS'|'FIND_MATCHES',
                    'ImportLabelsTaskRunProperties': {
                        'InputS3Path': 'string',
                        'Replace': True|False
                    },
                    'ExportLabelsTaskRunProperties': {
                        'OutputS3Path': 'string'
                    },
                    'LabelingSetGenerationTaskRunProperties': {
                        'OutputS3Path': 'string'
                    },
                    'FindMatchesTaskRunProperties': {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobRunId': 'string'
                    }
                },
                'ErrorString': 'string',
                'StartedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'CompletedOn': datetime(2015, 1, 1),
                'ExecutionTime': 123
            }
          **Response Structure**

          - *(dict) --*

            - **TransformId** *(string) --*

              The unique identifier of the task run.

            - **TaskRunId** *(string) --*

              The unique run identifier associated with this run.

            - **Status** *(string) --*

              The status for this task run.

            - **LogGroupName** *(string) --*

              The names of the log groups that are associated with the task run.

            - **Properties** *(dict) --*

              The list of properties that are associated with the task run.

              - **TaskType** *(string) --*

                The type of task run.

              - **ImportLabelsTaskRunProperties** *(dict) --*

                The configuration properties for an importing labels task run.

                - **InputS3Path** *(string) --*

                  The Amazon Simple Storage Service (Amazon S3) path from where you will import the labels.

                - **Replace** *(boolean) --*

                  Indicates whether to overwrite your existing labels.

              - **ExportLabelsTaskRunProperties** *(dict) --*

                The configuration properties for an exporting labels task run.

                - **OutputS3Path** *(string) --*

                  The Amazon Simple Storage Service (Amazon S3) path where you will export the labels.

              - **LabelingSetGenerationTaskRunProperties** *(dict) --*

                The configuration properties for a labeling set generation task run.

                - **OutputS3Path** *(string) --*

                  The Amazon Simple Storage Service (Amazon S3) path where you will generate the labeling
                  set.

              - **FindMatchesTaskRunProperties** *(dict) --*

                The configuration properties for a find matches task run.

                - **JobId** *(string) --*

                  The job ID for the Find Matches task run.

                - **JobName** *(string) --*

                  The name assigned to the job for the Find Matches task run.

                - **JobRunId** *(string) --*

                  The job run ID for the Find Matches task run.

            - **ErrorString** *(string) --*

              The error strings that are associated with the task run.

            - **StartedOn** *(datetime) --*

              The date and time when this task run started.

            - **LastModifiedOn** *(datetime) --*

              The date and time when this task run was last modified.

            - **CompletedOn** *(datetime) --*

              The date and time when this task run was completed.

            - **ExecutionTime** *(integer) --*

              The amount of time (in seconds) that the task run consumed resources.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ml_task_runs(
        self,
        TransformId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: ClientGetMlTaskRunsFilterTypeDef = None,
        Sort: ClientGetMlTaskRunsSortTypeDef = None,
    ) -> ClientGetMlTaskRunsResponseTypeDef:
        """
        Gets a list of runs for a machine learning transform. Machine learning task runs are asynchronous
        tasks that AWS Glue runs on your behalf as part of various machine learning workflows. You can get
        a sortable, filterable list of machine learning task runs by calling ``GetMLTaskRuns`` with their
        parent transform's ``TransformID`` and other optional parameters as documented in this section.

        This operation returns a list of historic runs and must be paginated.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetMLTaskRuns>`_

        **Request Syntax**
        ::

          response = client.get_ml_task_runs(
              TransformId='string',
              NextToken='string',
              MaxResults=123,
              Filter={
                  'TaskRunType':
                  'EVALUATION'|'LABELING_SET_GENERATION'|'IMPORT_LABELS'|'EXPORT_LABELS'|'FIND_MATCHES',
                  'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                  'StartedBefore': datetime(2015, 1, 1),
                  'StartedAfter': datetime(2015, 1, 1)
              },
              Sort={
                  'Column': 'TASK_RUN_TYPE'|'STATUS'|'STARTED',
                  'SortDirection': 'DESCENDING'|'ASCENDING'
              }
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the machine learning transform.

        :type NextToken: string
        :param NextToken:

          A token for pagination of the results. The default is empty.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return.

        :type Filter: dict
        :param Filter:

          The filter criteria, in the ``TaskRunFilterCriteria`` structure, for the task run.

          - **TaskRunType** *(string) --*

            The type of task run.

          - **Status** *(string) --*

            The current status of the task run.

          - **StartedBefore** *(datetime) --*

            Filter on task runs started before this date.

          - **StartedAfter** *(datetime) --*

            Filter on task runs started after this date.

        :type Sort: dict
        :param Sort:

          The sorting criteria, in the ``TaskRunSortCriteria`` structure, for the task run.

          - **Column** *(string) --* **[REQUIRED]**

            The column to be used to sort the list of task runs for the machine learning transform.

          - **SortDirection** *(string) --* **[REQUIRED]**

            The sort direction to be used to sort the list of task runs for the machine learning transform.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TaskRuns': [
                    {
                        'TransformId': 'string',
                        'TaskRunId': 'string',
                        'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                        'LogGroupName': 'string',
                        'Properties': {
                            'TaskType':
                            'EVALUATION'|'LABELING_SET_GENERATION'|'IMPORT_LABELS'|'EXPORT_LABELS'
                            |'FIND_MATCHES',
                            'ImportLabelsTaskRunProperties': {
                                'InputS3Path': 'string',
                                'Replace': True|False
                            },
                            'ExportLabelsTaskRunProperties': {
                                'OutputS3Path': 'string'
                            },
                            'LabelingSetGenerationTaskRunProperties': {
                                'OutputS3Path': 'string'
                            },
                            'FindMatchesTaskRunProperties': {
                                'JobId': 'string',
                                'JobName': 'string',
                                'JobRunId': 'string'
                            }
                        },
                        'ErrorString': 'string',
                        'StartedOn': datetime(2015, 1, 1),
                        'LastModifiedOn': datetime(2015, 1, 1),
                        'CompletedOn': datetime(2015, 1, 1),
                        'ExecutionTime': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TaskRuns** *(list) --*

              A list of task runs that are associated with the transform.

              - *(dict) --*

                The sampling parameters that are associated with the machine learning transform.

                - **TransformId** *(string) --*

                  The unique identifier for the transform.

                - **TaskRunId** *(string) --*

                  The unique identifier for this task run.

                - **Status** *(string) --*

                  The current status of the requested task run.

                - **LogGroupName** *(string) --*

                  The names of the log group for secure logging, associated with this task run.

                - **Properties** *(dict) --*

                  Specifies configuration properties associated with this task run.

                  - **TaskType** *(string) --*

                    The type of task run.

                  - **ImportLabelsTaskRunProperties** *(dict) --*

                    The configuration properties for an importing labels task run.

                    - **InputS3Path** *(string) --*

                      The Amazon Simple Storage Service (Amazon S3) path from where you will import the
                      labels.

                    - **Replace** *(boolean) --*

                      Indicates whether to overwrite your existing labels.

                  - **ExportLabelsTaskRunProperties** *(dict) --*

                    The configuration properties for an exporting labels task run.

                    - **OutputS3Path** *(string) --*

                      The Amazon Simple Storage Service (Amazon S3) path where you will export the labels.

                  - **LabelingSetGenerationTaskRunProperties** *(dict) --*

                    The configuration properties for a labeling set generation task run.

                    - **OutputS3Path** *(string) --*

                      The Amazon Simple Storage Service (Amazon S3) path where you will generate the
                      labeling set.

                  - **FindMatchesTaskRunProperties** *(dict) --*

                    The configuration properties for a find matches task run.

                    - **JobId** *(string) --*

                      The job ID for the Find Matches task run.

                    - **JobName** *(string) --*

                      The name assigned to the job for the Find Matches task run.

                    - **JobRunId** *(string) --*

                      The job run ID for the Find Matches task run.

                - **ErrorString** *(string) --*

                  The list of error strings associated with this task run.

                - **StartedOn** *(datetime) --*

                  The date and time that this task run started.

                - **LastModifiedOn** *(datetime) --*

                  The last point in time that the requested task run was updated.

                - **CompletedOn** *(datetime) --*

                  The last point in time that the requested task run was completed.

                - **ExecutionTime** *(integer) --*

                  The amount of time (in seconds) that the task run consumed resources.

            - **NextToken** *(string) --*

              A pagination token, if more results are available.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ml_transform(self, TransformId: str) -> ClientGetMlTransformResponseTypeDef:
        """
        Gets an AWS Glue machine learning transform artifact and all its corresponding metadata. Machine
        learning transforms are a special type of transform that use machine learning to learn the details
        of the transformation to be performed by learning from examples provided by humans. These
        transformations are then saved by AWS Glue. You can retrieve their metadata by calling
        ``GetMLTransform`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetMLTransform>`_

        **Request Syntax**
        ::

          response = client.get_ml_transform(
              TransformId='string'
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the transform, generated at the time that the transform was created.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TransformId': 'string',
                'Name': 'string',
                'Description': 'string',
                'Status': 'NOT_READY'|'READY'|'DELETING',
                'CreatedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'InputRecordTables': [
                    {
                        'DatabaseName': 'string',
                        'TableName': 'string',
                        'CatalogId': 'string',
                        'ConnectionName': 'string'
                    },
                ],
                'Parameters': {
                    'TransformType': 'FIND_MATCHES',
                    'FindMatchesParameters': {
                        'PrimaryKeyColumnName': 'string',
                        'PrecisionRecallTradeoff': 123.0,
                        'AccuracyCostTradeoff': 123.0,
                        'EnforceProvidedLabels': True|False
                    }
                },
                'EvaluationMetrics': {
                    'TransformType': 'FIND_MATCHES',
                    'FindMatchesMetrics': {
                        'AreaUnderPRCurve': 123.0,
                        'Precision': 123.0,
                        'Recall': 123.0,
                        'F1': 123.0,
                        'ConfusionMatrix': {
                            'NumTruePositives': 123,
                            'NumFalsePositives': 123,
                            'NumTrueNegatives': 123,
                            'NumFalseNegatives': 123
                        }
                    }
                },
                'LabelCount': 123,
                'Schema': [
                    {
                        'Name': 'string',
                        'DataType': 'string'
                    },
                ],
                'Role': 'string',
                'MaxCapacity': 123.0,
                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                'NumberOfWorkers': 123,
                'Timeout': 123,
                'MaxRetries': 123
            }
          **Response Structure**

          - *(dict) --*

            - **TransformId** *(string) --*

              The unique identifier of the transform, generated at the time that the transform was created.

            - **Name** *(string) --*

              The unique name given to the transform when it was created.

            - **Description** *(string) --*

              A description of the transform.

            - **Status** *(string) --*

              The last known status of the transform (to indicate whether it can be used or not). One of
              "NOT_READY", "READY", or "DELETING".

            - **CreatedOn** *(datetime) --*

              The date and time when the transform was created.

            - **LastModifiedOn** *(datetime) --*

              The date and time when the transform was last modified.

            - **InputRecordTables** *(list) --*

              A list of AWS Glue table definitions used by the transform.

              - *(dict) --*

                The database and table in the AWS Glue Data Catalog that is used for input or output data.

                - **DatabaseName** *(string) --*

                  A database name in the AWS Glue Data Catalog.

                - **TableName** *(string) --*

                  A table name in the AWS Glue Data Catalog.

                - **CatalogId** *(string) --*

                  A unique identifier for the AWS Glue Data Catalog.

                - **ConnectionName** *(string) --*

                  The name of the connection to the AWS Glue Data Catalog.

            - **Parameters** *(dict) --*

              The configuration parameters that are specific to the algorithm used.

              - **TransformType** *(string) --*

                The type of machine learning transform.

                For information about the types of machine learning transforms, see `Creating Machine
                Learning Transforms
                <http://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html>`__ .

              - **FindMatchesParameters** *(dict) --*

                The parameters for the find matches algorithm.

                - **PrimaryKeyColumnName** *(string) --*

                  The name of a column that uniquely identifies rows in the source table. Used to help
                  identify matching records.

                - **PrecisionRecallTradeoff** *(float) --*

                  The value selected when tuning your transform for a balance between precision and recall.
                  A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and
                  a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close
                  to 1.0 means very low recall, and choosing values close to 0.0 results in very low
                  precision.

                  The precision metric indicates how often your model is correct when it predicts a match.

                  The recall metric indicates that for an actual match, how often your model predicts the
                  match.

                - **AccuracyCostTradeoff** *(float) --*

                  The value that is selected when tuning your transform for a balance between accuracy and
                  cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value
                  of 1.0 means a bias purely for accuracy, which typically results in a higher cost,
                  sometimes substantially higher. A value of 0.0 means a bias purely for cost, which
                  results in a less accurate ``FindMatches`` transform, sometimes with unacceptable
                  accuracy.

                  Accuracy measures how well the transform finds true positives and true negatives.
                  Increasing accuracy requires more machine resources and cost. But it also results in
                  increased recall.

                  Cost measures how many compute resources, and thus money, are consumed to run the
                  transform.

                - **EnforceProvidedLabels** *(boolean) --*

                  The value to switch on or off to force the output to match the provided labels from
                  users. If the value is ``True`` , the ``find matches`` transform forces the output to
                  match the provided labels. The results override the normal conflation results. If the
                  value is ``False`` , the ``find matches`` transform does not ensure all the labels
                  provided are respected, and the results rely on the trained model.

                  Note that setting this value to true may increase the conflation execution time.

            - **EvaluationMetrics** *(dict) --*

              The latest evaluation metrics.

              - **TransformType** *(string) --*

                The type of machine learning transform.

              - **FindMatchesMetrics** *(dict) --*

                The evaluation metrics for the find matches algorithm.

                - **AreaUnderPRCurve** *(float) --*

                  The area under the precision/recall curve (AUPRC) is a single number measuring the
                  overall quality of the transform, that is independent of the choice made for precision
                  vs. recall. Higher values indicate that you have a more attractive precision vs. recall
                  tradeoff.

                  For more information, see `Precision and recall
                  <https://en.wikipedia.org/wiki/Precision_and_recall>`__ in Wikipedia.

                - **Precision** *(float) --*

                  The precision metric indicates when often your transform is correct when it predicts a
                  match. Specifically, it measures how well the transform finds true positives from the
                  total true positives possible.

                  For more information, see `Precision and recall
                  <https://en.wikipedia.org/wiki/Precision_and_recall>`__ in Wikipedia.

                - **Recall** *(float) --*

                  The recall metric indicates that for an actual match, how often your transform predicts
                  the match. Specifically, it measures how well the transform finds true positives from the
                  total records in the source data.

                  For more information, see `Precision and recall
                  <https://en.wikipedia.org/wiki/Precision_and_recall>`__ in Wikipedia.

                - **F1** *(float) --*

                  The maximum F1 metric indicates the transform's accuracy between 0 and 1, where 1 is the
                  best accuracy.

                  For more information, see `F1 score <https://en.wikipedia.org/wiki/F1_score>`__ in
                  Wikipedia.

                - **ConfusionMatrix** *(dict) --*

                  The confusion matrix shows you what your transform is predicting accurately and what
                  types of errors it is making.

                  For more information, see `Confusion matrix
                  <https://en.wikipedia.org/wiki/Confusion_matrix>`__ in Wikipedia.

                  - **NumTruePositives** *(integer) --*

                    The number of matches in the data that the transform correctly found, in the confusion
                    matrix for your transform.

                  - **NumFalsePositives** *(integer) --*

                    The number of nonmatches in the data that the transform incorrectly classified as a
                    match, in the confusion matrix for your transform.

                  - **NumTrueNegatives** *(integer) --*

                    The number of nonmatches in the data that the transform correctly rejected, in the
                    confusion matrix for your transform.

                  - **NumFalseNegatives** *(integer) --*

                    The number of matches in the data that the transform didn't find, in the confusion
                    matrix for your transform.

            - **LabelCount** *(integer) --*

              The number of labels available for this transform.

            - **Schema** *(list) --*

              The ``Map<Column, Type>`` object that represents the schema that this transform accepts. Has
              an upper bound of 100 columns.

              - *(dict) --*

                A key-value pair representing a column and data type that this transform can run against.
                The ``Schema`` parameter of the ``MLTransform`` may contain up to 100 of these structures.

                - **Name** *(string) --*

                  The name of the column.

                - **DataType** *(string) --*

                  The type of data in the column.

            - **Role** *(string) --*

              The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.

            - **MaxCapacity** *(float) --*

              The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this
              transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative
              measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.
              For more information, see the `AWS Glue pricing page
              <https://aws.amazon.com/glue/pricing/>`__ .

              When the ``WorkerType`` field is set to a value other than ``Standard`` , the ``MaxCapacity``
              field is set automatically and becomes read-only.

            - **WorkerType** *(string) --*

              The type of predefined worker that is allocated when this task runs. Accepts a value of
              Standard, G.1X, or G.2X.

              * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB
              disk, and 2 executors per worker.

              * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk,
              and 1 executor per worker.

              * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB
              disk, and 1 executor per worker.

            - **NumberOfWorkers** *(integer) --*

              The number of workers of a defined ``workerType`` that are allocated when this task runs.

            - **Timeout** *(integer) --*

              The timeout for a task run for this transform in minutes. This is the maximum time that a
              task run for this transform can consume resources before it is terminated and enters
              ``TIMEOUT`` status. The default is 2,880 minutes (48 hours).

            - **MaxRetries** *(integer) --*

              The maximum number of times to retry a task for this transform after a task run fails.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ml_transforms(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: ClientGetMlTransformsFilterTypeDef = None,
        Sort: ClientGetMlTransformsSortTypeDef = None,
    ) -> ClientGetMlTransformsResponseTypeDef:
        """
        Gets a sortable, filterable list of existing AWS Glue machine learning transforms. Machine learning
        transforms are a special type of transform that use machine learning to learn the details of the
        transformation to be performed by learning from examples provided by humans. These transformations
        are then saved by AWS Glue, and you can retrieve their metadata by calling ``GetMLTransforms`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetMLTransforms>`_

        **Request Syntax**
        ::

          response = client.get_ml_transforms(
              NextToken='string',
              MaxResults=123,
              Filter={
                  'Name': 'string',
                  'TransformType': 'FIND_MATCHES',
                  'Status': 'NOT_READY'|'READY'|'DELETING',
                  'CreatedBefore': datetime(2015, 1, 1),
                  'CreatedAfter': datetime(2015, 1, 1),
                  'LastModifiedBefore': datetime(2015, 1, 1),
                  'LastModifiedAfter': datetime(2015, 1, 1),
                  'Schema': [
                      {
                          'Name': 'string',
                          'DataType': 'string'
                      },
                  ]
              },
              Sort={
                  'Column': 'NAME'|'TRANSFORM_TYPE'|'STATUS'|'CREATED'|'LAST_MODIFIED',
                  'SortDirection': 'DESCENDING'|'ASCENDING'
              }
          )
        :type NextToken: string
        :param NextToken:

          A paginated token to offset the results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return.

        :type Filter: dict
        :param Filter:

          The filter transformation criteria.

          - **Name** *(string) --*

            A unique transform name that is used to filter the machine learning transforms.

          - **TransformType** *(string) --*

            The type of machine learning transform that is used to filter the machine learning transforms.

          - **Status** *(string) --*

            Filters the list of machine learning transforms by the last known status of the transforms (to
            indicate whether a transform can be used or not). One of "NOT_READY", "READY", or "DELETING".

          - **CreatedBefore** *(datetime) --*

            The time and date before which the transforms were created.

          - **CreatedAfter** *(datetime) --*

            The time and date after which the transforms were created.

          - **LastModifiedBefore** *(datetime) --*

            Filter on transforms last modified before this date.

          - **LastModifiedAfter** *(datetime) --*

            Filter on transforms last modified after this date.

          - **Schema** *(list) --*

            Filters on datasets with a specific schema. The ``Map<Column, Type>`` object is an array of
            key-value pairs representing the schema this transform accepts, where ``Column`` is the name of
            a column, and ``Type`` is the type of the data such as an integer or string. Has an upper bound
            of 100 columns.

            - *(dict) --*

              A key-value pair representing a column and data type that this transform can run against. The
              ``Schema`` parameter of the ``MLTransform`` may contain up to 100 of these structures.

              - **Name** *(string) --*

                The name of the column.

              - **DataType** *(string) --*

                The type of data in the column.

        :type Sort: dict
        :param Sort:

          The sorting criteria.

          - **Column** *(string) --* **[REQUIRED]**

            The column to be used in the sorting criteria that are associated with the machine learning
            transform.

          - **SortDirection** *(string) --* **[REQUIRED]**

            The sort direction to be used in the sorting criteria that are associated with the machine
            learning transform.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Transforms': [
                    {
                        'TransformId': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'Status': 'NOT_READY'|'READY'|'DELETING',
                        'CreatedOn': datetime(2015, 1, 1),
                        'LastModifiedOn': datetime(2015, 1, 1),
                        'InputRecordTables': [
                            {
                                'DatabaseName': 'string',
                                'TableName': 'string',
                                'CatalogId': 'string',
                                'ConnectionName': 'string'
                            },
                        ],
                        'Parameters': {
                            'TransformType': 'FIND_MATCHES',
                            'FindMatchesParameters': {
                                'PrimaryKeyColumnName': 'string',
                                'PrecisionRecallTradeoff': 123.0,
                                'AccuracyCostTradeoff': 123.0,
                                'EnforceProvidedLabels': True|False
                            }
                        },
                        'EvaluationMetrics': {
                            'TransformType': 'FIND_MATCHES',
                            'FindMatchesMetrics': {
                                'AreaUnderPRCurve': 123.0,
                                'Precision': 123.0,
                                'Recall': 123.0,
                                'F1': 123.0,
                                'ConfusionMatrix': {
                                    'NumTruePositives': 123,
                                    'NumFalsePositives': 123,
                                    'NumTrueNegatives': 123,
                                    'NumFalseNegatives': 123
                                }
                            }
                        },
                        'LabelCount': 123,
                        'Schema': [
                            {
                                'Name': 'string',
                                'DataType': 'string'
                            },
                        ],
                        'Role': 'string',
                        'MaxCapacity': 123.0,
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'NumberOfWorkers': 123,
                        'Timeout': 123,
                        'MaxRetries': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Transforms** *(list) --*

              A list of machine learning transforms.

              - *(dict) --*

                A structure for a machine learning transform.

                - **TransformId** *(string) --*

                  The unique transform ID that is generated for the machine learning transform. The ID is
                  guaranteed to be unique and does not change.

                - **Name** *(string) --*

                  A user-defined name for the machine learning transform. Names are not guaranteed unique
                  and can be changed at any time.

                - **Description** *(string) --*

                  A user-defined, long-form description text for the machine learning transform.
                  Descriptions are not guaranteed to be unique and can be changed at any time.

                - **Status** *(string) --*

                  The current status of the machine learning transform.

                - **CreatedOn** *(datetime) --*

                  A timestamp. The time and date that this machine learning transform was created.

                - **LastModifiedOn** *(datetime) --*

                  A timestamp. The last point in time when this machine learning transform was modified.

                - **InputRecordTables** *(list) --*

                  A list of AWS Glue table definitions used by the transform.

                  - *(dict) --*

                    The database and table in the AWS Glue Data Catalog that is used for input or output
                    data.

                    - **DatabaseName** *(string) --*

                      A database name in the AWS Glue Data Catalog.

                    - **TableName** *(string) --*

                      A table name in the AWS Glue Data Catalog.

                    - **CatalogId** *(string) --*

                      A unique identifier for the AWS Glue Data Catalog.

                    - **ConnectionName** *(string) --*

                      The name of the connection to the AWS Glue Data Catalog.

                - **Parameters** *(dict) --*

                  A ``TransformParameters`` object. You can use parameters to tune (customize) the behavior
                  of the machine learning transform by specifying what data it learns from and your
                  preference on various tradeoffs (such as precious vs. recall, or accuracy vs. cost).

                  - **TransformType** *(string) --*

                    The type of machine learning transform.

                    For information about the types of machine learning transforms, see `Creating Machine
                    Learning Transforms
                    <http://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html>`__ .

                  - **FindMatchesParameters** *(dict) --*

                    The parameters for the find matches algorithm.

                    - **PrimaryKeyColumnName** *(string) --*

                      The name of a column that uniquely identifies rows in the source table. Used to help
                      identify matching records.

                    - **PrecisionRecallTradeoff** *(float) --*

                      The value selected when tuning your transform for a balance between precision and
                      recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for
                      precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff,
                      choosing values close to 1.0 means very low recall, and choosing values close to 0.0
                      results in very low precision.

                      The precision metric indicates how often your model is correct when it predicts a
                      match.

                      The recall metric indicates that for an actual match, how often your model predicts
                      the match.

                    - **AccuracyCostTradeoff** *(float) --*

                      The value that is selected when tuning your transform for a balance between accuracy
                      and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A
                      value of 1.0 means a bias purely for accuracy, which typically results in a higher
                      cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost,
                      which results in a less accurate ``FindMatches`` transform, sometimes with
                      unacceptable accuracy.

                      Accuracy measures how well the transform finds true positives and true negatives.
                      Increasing accuracy requires more machine resources and cost. But it also results in
                      increased recall.

                      Cost measures how many compute resources, and thus money, are consumed to run the
                      transform.

                    - **EnforceProvidedLabels** *(boolean) --*

                      The value to switch on or off to force the output to match the provided labels from
                      users. If the value is ``True`` , the ``find matches`` transform forces the output to
                      match the provided labels. The results override the normal conflation results. If the
                      value is ``False`` , the ``find matches`` transform does not ensure all the labels
                      provided are respected, and the results rely on the trained model.

                      Note that setting this value to true may increase the conflation execution time.

                - **EvaluationMetrics** *(dict) --*

                  An ``EvaluationMetrics`` object. Evaluation metrics provide an estimate of the quality of
                  your machine learning transform.

                  - **TransformType** *(string) --*

                    The type of machine learning transform.

                  - **FindMatchesMetrics** *(dict) --*

                    The evaluation metrics for the find matches algorithm.

                    - **AreaUnderPRCurve** *(float) --*

                      The area under the precision/recall curve (AUPRC) is a single number measuring the
                      overall quality of the transform, that is independent of the choice made for
                      precision vs. recall. Higher values indicate that you have a more attractive
                      precision vs. recall tradeoff.

                      For more information, see `Precision and recall
                      <https://en.wikipedia.org/wiki/Precision_and_recall>`__ in Wikipedia.

                    - **Precision** *(float) --*

                      The precision metric indicates when often your transform is correct when it predicts
                      a match. Specifically, it measures how well the transform finds true positives from
                      the total true positives possible.

                      For more information, see `Precision and recall
                      <https://en.wikipedia.org/wiki/Precision_and_recall>`__ in Wikipedia.

                    - **Recall** *(float) --*

                      The recall metric indicates that for an actual match, how often your transform
                      predicts the match. Specifically, it measures how well the transform finds true
                      positives from the total records in the source data.

                      For more information, see `Precision and recall
                      <https://en.wikipedia.org/wiki/Precision_and_recall>`__ in Wikipedia.

                    - **F1** *(float) --*

                      The maximum F1 metric indicates the transform's accuracy between 0 and 1, where 1 is
                      the best accuracy.

                      For more information, see `F1 score <https://en.wikipedia.org/wiki/F1_score>`__ in
                      Wikipedia.

                    - **ConfusionMatrix** *(dict) --*

                      The confusion matrix shows you what your transform is predicting accurately and what
                      types of errors it is making.

                      For more information, see `Confusion matrix
                      <https://en.wikipedia.org/wiki/Confusion_matrix>`__ in Wikipedia.

                      - **NumTruePositives** *(integer) --*

                        The number of matches in the data that the transform correctly found, in the
                        confusion matrix for your transform.

                      - **NumFalsePositives** *(integer) --*

                        The number of nonmatches in the data that the transform incorrectly classified as a
                        match, in the confusion matrix for your transform.

                      - **NumTrueNegatives** *(integer) --*

                        The number of nonmatches in the data that the transform correctly rejected, in the
                        confusion matrix for your transform.

                      - **NumFalseNegatives** *(integer) --*

                        The number of matches in the data that the transform didn't find, in the confusion
                        matrix for your transform.

                - **LabelCount** *(integer) --*

                  A count identifier for the labeling files generated by AWS Glue for this transform. As
                  you create a better transform, you can iteratively download, label, and upload the
                  labeling file.

                - **Schema** *(list) --*

                  A map of key-value pairs representing the columns and data types that this transform can
                  run against. Has an upper bound of 100 columns.

                  - *(dict) --*

                    A key-value pair representing a column and data type that this transform can run
                    against. The ``Schema`` parameter of the ``MLTransform`` may contain up to 100 of these
                    structures.

                    - **Name** *(string) --*

                      The name of the column.

                    - **DataType** *(string) --*

                      The type of data in the column.

                - **Role** *(string) --*

                  The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.
                  This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources,
                  targets, temporary directory, scripts, and any libraries used by the task run for this
                  transform.

                - **MaxCapacity** *(float) --*

                  The number of AWS Glue data processing units (DPUs) that are allocated to task runs for
                  this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a
                  relative measure of processing power that consists of 4 vCPUs of compute capacity and 16
                  GB of memory. For more information, see the `AWS Glue pricing page
                  <https://aws.amazon.com/glue/pricing/>`__ .

                  When the ``WorkerType`` field is set to a value other than ``Standard`` , the
                  ``MaxCapacity`` field is set automatically and becomes read-only.

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated when a task of this transform runs.
                  Accepts a value of Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a
                  50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB
                  disk, and 1 executor per worker.

                  * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB
                  disk, and 1 executor per worker.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated when a task of the
                  transform runs.

                - **Timeout** *(integer) --*

                  The timeout in minutes of the machine learning transform.

                - **MaxRetries** *(integer) --*

                  The maximum number of times to retry after an ``MLTaskRun`` of the machine learning
                  transform fails.

            - **NextToken** *(string) --*

              A pagination token, if more results are available.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        CatalogId: str = None,
    ) -> ClientGetPartitionResponseTypeDef:
        """
        Retrieves information about a specified partition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPartition>`_

        **Request Syntax**
        ::

          response = client.get_partition(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              PartitionValues=[
                  'string',
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the partition in question resides. If none is provided, the AWS
          account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the partition resides.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the partition's table.

        :type PartitionValues: list
        :param PartitionValues: **[REQUIRED]**

          The values that define the partition.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Partition': {
                    'Values': [
                        'string',
                    ],
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastAccessTime': datetime(2015, 1, 1),
                    'StorageDescriptor': {
                        'Columns': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'Location': 'string',
                        'InputFormat': 'string',
                        'OutputFormat': 'string',
                        'Compressed': True|False,
                        'NumberOfBuckets': 123,
                        'SerdeInfo': {
                            'Name': 'string',
                            'SerializationLibrary': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                        'BucketColumns': [
                            'string',
                        ],
                        'SortColumns': [
                            {
                                'Column': 'string',
                                'SortOrder': 123
                            },
                        ],
                        'Parameters': {
                            'string': 'string'
                        },
                        'SkewedInfo': {
                            'SkewedColumnNames': [
                                'string',
                            ],
                            'SkewedColumnValues': [
                                'string',
                            ],
                            'SkewedColumnValueLocationMaps': {
                                'string': 'string'
                            }
                        },
                        'StoredAsSubDirectories': True|False
                    },
                    'Parameters': {
                        'string': 'string'
                    },
                    'LastAnalyzedTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Partition** *(dict) --*

              The requested information, in the form of a ``Partition`` object.

              - **Values** *(list) --*

                The values of the partition.

                - *(string) --*

              - **DatabaseName** *(string) --*

                The name of the catalog database in which to create the partition.

              - **TableName** *(string) --*

                The name of the database table in which to create the partition.

              - **CreationTime** *(datetime) --*

                The time at which the partition was created.

              - **LastAccessTime** *(datetime) --*

                The last time at which the partition was accessed.

              - **StorageDescriptor** *(dict) --*

                Provides information about the physical location where the partition is stored.

                - **Columns** *(list) --*

                  A list of the ``Columns`` in the table.

                  - *(dict) --*

                    A column in a ``Table`` .

                    - **Name** *(string) --*

                      The name of the ``Column`` .

                    - **Type** *(string) --*

                      The data type of the ``Column`` .

                    - **Comment** *(string) --*

                      A free-form text comment.

                    - **Parameters** *(dict) --*

                      These key-value pairs define properties associated with the column.

                      - *(string) --*

                        - *(string) --*

                - **Location** *(string) --*

                  The physical location of the table. By default, this takes the form of the warehouse
                  location, followed by the database location in the warehouse, followed by the table name.

                - **InputFormat** *(string) --*

                  The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                  custom format.

                - **OutputFormat** *(string) --*

                  The output format: ``SequenceFileOutputFormat`` (binary), or
                  ``IgnoreKeyTextOutputFormat`` , or a custom format.

                - **Compressed** *(boolean) --*

                   ``True`` if the data in the table is compressed, or ``False`` if not.

                - **NumberOfBuckets** *(integer) --*

                  Must be specified if the table contains any dimension columns.

                - **SerdeInfo** *(dict) --*

                  The serialization/deserialization (SerDe) information.

                  - **Name** *(string) --*

                    Name of the SerDe.

                  - **SerializationLibrary** *(string) --*

                    Usually the class that implements the SerDe. An example is
                    ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                  - **Parameters** *(dict) --*

                    These key-value pairs define initialization parameters for the SerDe.

                    - *(string) --*

                      - *(string) --*

                - **BucketColumns** *(list) --*

                  A list of reducer grouping columns, clustering columns, and bucketing columns in the
                  table.

                  - *(string) --*

                - **SortColumns** *(list) --*

                  A list specifying the sort order of each bucket in the table.

                  - *(dict) --*

                    Specifies the sort order of a sorted column.

                    - **Column** *(string) --*

                      The name of the column.

                    - **SortOrder** *(integer) --*

                      Indicates that the column is sorted in ascending order (``== 1`` ), or in descending
                      order (``==0`` ).

                - **Parameters** *(dict) --*

                  The user-supplied properties in key-value form.

                  - *(string) --*

                    - *(string) --*

                - **SkewedInfo** *(dict) --*

                  The information about values that appear frequently in a column (skewed values).

                  - **SkewedColumnNames** *(list) --*

                    A list of names of columns that contain skewed values.

                    - *(string) --*

                  - **SkewedColumnValues** *(list) --*

                    A list of values that appear so frequently as to be considered skewed.

                    - *(string) --*

                  - **SkewedColumnValueLocationMaps** *(dict) --*

                    A mapping of skewed values to the columns that contain them.

                    - *(string) --*

                      - *(string) --*

                - **StoredAsSubDirectories** *(boolean) --*

                   ``True`` if the table data is stored in subdirectories, or ``False`` if not.

              - **Parameters** *(dict) --*

                These key-value pairs define partition parameters.

                - *(string) --*

                  - *(string) --*

              - **LastAnalyzedTime** *(datetime) --*

                The last time at which column statistics were computed for this partition.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_partitions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        Segment: ClientGetPartitionsSegmentTypeDef = None,
        MaxResults: int = None,
    ) -> ClientGetPartitionsResponseTypeDef:
        """
        Retrieves information about the partitions in a table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPartitions>`_

        **Request Syntax**
        ::

          response = client.get_partitions(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              Expression='string',
              NextToken='string',
              Segment={
                  'SegmentNumber': 123,
                  'TotalSegments': 123
              },
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the partitions in question reside. If none is provided, the AWS
          account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the partitions reside.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the partitions' table.

        :type Expression: string
        :param Expression:

          An expression that filters the partitions to be returned.

          The expression uses SQL syntax similar to the SQL ``WHERE`` filter clause. The SQL statement
          parser `JSQLParser <http://jsqlparser.sourceforge.net/home.php>`__ parses the expression.

           *Operators* : The following are the operators that you can use in the ``Expression`` API call:

            =

          Checks whether the values of the two operands are equal; if yes, then the condition becomes true.

          Example: Assume 'variable a' holds 10 and 'variable b' holds 20.

          (a = b) is not true.

            < >

          Checks whether the values of two operands are equal; if the values are not equal, then the
          condition becomes true.

          Example: (a < > b) is true.

            >

          Checks whether the value of the left operand is greater than the value of the right operand; if
          yes, then the condition becomes true.

          Example: (a > b) is not true.

            <

          Checks whether the value of the left operand is less than the value of the right operand; if yes,
          then the condition becomes true.

          Example: (a < b) is true.

            >=

          Checks whether the value of the left operand is greater than or equal to the value of the right
          operand; if yes, then the condition becomes true.

          Example: (a >= b) is not true.

            <=

          Checks whether the value of the left operand is less than or equal to the value of the right
          operand; if yes, then the condition becomes true.

          Example: (a <= b) is true.

            AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL

          Logical operators.

           *Supported Partition Key Types* : The following are the supported partition keys.

          * ``string``

          * ``date``

          * ``timestamp``

          * ``int``

          * ``bigint``

          * ``long``

          * ``tinyint``

          * ``smallint``

          * ``decimal``

          If an invalid type is encountered, an exception is thrown.

          The following list shows the valid operators on each type. When you define a crawler, the
          ``partitionKey`` type is created as a ``STRING`` , to be compatible with the catalog partitions.

           *Sample API Call* :

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is not the first call to retrieve these partitions.

        :type Segment: dict
        :param Segment:

          The segment of the table's partitions to scan in this request.

          - **SegmentNumber** *(integer) --* **[REQUIRED]**

            The zero-based index number of the segment. For example, if the total number of segments is 4,
            ``SegmentNumber`` values range from 0 through 3.

          - **TotalSegments** *(integer) --* **[REQUIRED]**

            The total number of segments.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of partitions to return in a single response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Partitions': [
                    {
                        'Values': [
                            'string',
                        ],
                        'DatabaseName': 'string',
                        'TableName': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastAccessTime': datetime(2015, 1, 1),
                        'StorageDescriptor': {
                            'Columns': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'Location': 'string',
                            'InputFormat': 'string',
                            'OutputFormat': 'string',
                            'Compressed': True|False,
                            'NumberOfBuckets': 123,
                            'SerdeInfo': {
                                'Name': 'string',
                                'SerializationLibrary': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                            'BucketColumns': [
                                'string',
                            ],
                            'SortColumns': [
                                {
                                    'Column': 'string',
                                    'SortOrder': 123
                                },
                            ],
                            'Parameters': {
                                'string': 'string'
                            },
                            'SkewedInfo': {
                                'SkewedColumnNames': [
                                    'string',
                                ],
                                'SkewedColumnValues': [
                                    'string',
                                ],
                                'SkewedColumnValueLocationMaps': {
                                    'string': 'string'
                                }
                            },
                            'StoredAsSubDirectories': True|False
                        },
                        'Parameters': {
                            'string': 'string'
                        },
                        'LastAnalyzedTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Partitions** *(list) --*

              A list of requested partitions.

              - *(dict) --*

                Represents a slice of table data.

                - **Values** *(list) --*

                  The values of the partition.

                  - *(string) --*

                - **DatabaseName** *(string) --*

                  The name of the catalog database in which to create the partition.

                - **TableName** *(string) --*

                  The name of the database table in which to create the partition.

                - **CreationTime** *(datetime) --*

                  The time at which the partition was created.

                - **LastAccessTime** *(datetime) --*

                  The last time at which the partition was accessed.

                - **StorageDescriptor** *(dict) --*

                  Provides information about the physical location where the partition is stored.

                  - **Columns** *(list) --*

                    A list of the ``Columns`` in the table.

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **Location** *(string) --*

                    The physical location of the table. By default, this takes the form of the warehouse
                    location, followed by the database location in the warehouse, followed by the table
                    name.

                  - **InputFormat** *(string) --*

                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                    custom format.

                  - **OutputFormat** *(string) --*

                    The output format: ``SequenceFileOutputFormat`` (binary), or
                    ``IgnoreKeyTextOutputFormat`` , or a custom format.

                  - **Compressed** *(boolean) --*

                     ``True`` if the data in the table is compressed, or ``False`` if not.

                  - **NumberOfBuckets** *(integer) --*

                    Must be specified if the table contains any dimension columns.

                  - **SerdeInfo** *(dict) --*

                    The serialization/deserialization (SerDe) information.

                    - **Name** *(string) --*

                      Name of the SerDe.

                    - **SerializationLibrary** *(string) --*

                      Usually the class that implements the SerDe. An example is
                      ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                    - **Parameters** *(dict) --*

                      These key-value pairs define initialization parameters for the SerDe.

                      - *(string) --*

                        - *(string) --*

                  - **BucketColumns** *(list) --*

                    A list of reducer grouping columns, clustering columns, and bucketing columns in the
                    table.

                    - *(string) --*

                  - **SortColumns** *(list) --*

                    A list specifying the sort order of each bucket in the table.

                    - *(dict) --*

                      Specifies the sort order of a sorted column.

                      - **Column** *(string) --*

                        The name of the column.

                      - **SortOrder** *(integer) --*

                        Indicates that the column is sorted in ascending order (``== 1`` ), or in
                        descending order (``==0`` ).

                  - **Parameters** *(dict) --*

                    The user-supplied properties in key-value form.

                    - *(string) --*

                      - *(string) --*

                  - **SkewedInfo** *(dict) --*

                    The information about values that appear frequently in a column (skewed values).

                    - **SkewedColumnNames** *(list) --*

                      A list of names of columns that contain skewed values.

                      - *(string) --*

                    - **SkewedColumnValues** *(list) --*

                      A list of values that appear so frequently as to be considered skewed.

                      - *(string) --*

                    - **SkewedColumnValueLocationMaps** *(dict) --*

                      A mapping of skewed values to the columns that contain them.

                      - *(string) --*

                        - *(string) --*

                  - **StoredAsSubDirectories** *(boolean) --*

                     ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                - **Parameters** *(dict) --*

                  These key-value pairs define partition parameters.

                  - *(string) --*

                    - *(string) --*

                - **LastAnalyzedTime** *(datetime) --*

                  The last time at which column statistics were computed for this partition.

            - **NextToken** *(string) --*

              A continuation token, if the returned list of partitions does not include the last one.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_plan(
        self,
        Mapping: List[ClientGetPlanMappingTypeDef],
        Source: ClientGetPlanSourceTypeDef,
        Sinks: List[ClientGetPlanSinksTypeDef] = None,
        Location: ClientGetPlanLocationTypeDef = None,
        Language: str = None,
    ) -> ClientGetPlanResponseTypeDef:
        """
        Gets code to perform a specified mapping.

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPlan>`_

        **Request Syntax**
        ::

          response = client.get_plan(
              Mapping=[
                  {
                      'SourceTable': 'string',
                      'SourcePath': 'string',
                      'SourceType': 'string',
                      'TargetTable': 'string',
                      'TargetPath': 'string',
                      'TargetType': 'string'
                  },
              ],
              Source={
                  'DatabaseName': 'string',
                  'TableName': 'string'
              },
              Sinks=[
                  {
                      'DatabaseName': 'string',
                      'TableName': 'string'
                  },
              ],
              Location={
                  'Jdbc': [
                      {
                          'Name': 'string',
                          'Value': 'string',
                          'Param': True|False
                      },
                  ],
                  'S3': [
                      {
                          'Name': 'string',
                          'Value': 'string',
                          'Param': True|False
                      },
                  ],
                  'DynamoDB': [
                      {
                          'Name': 'string',
                          'Value': 'string',
                          'Param': True|False
                      },
                  ]
              },
              Language='PYTHON'|'SCALA'
          )
        :type Mapping: list
        :param Mapping: **[REQUIRED]**

          The list of mappings from a source table to target tables.

          - *(dict) --*

            Defines a mapping.

            - **SourceTable** *(string) --*

              The name of the source table.

            - **SourcePath** *(string) --*

              The source path.

            - **SourceType** *(string) --*

              The source type.

            - **TargetTable** *(string) --*

              The target table.

            - **TargetPath** *(string) --*

              The target path.

            - **TargetType** *(string) --*

              The target type.

        :type Source: dict
        :param Source: **[REQUIRED]**

          The source table.

          - **DatabaseName** *(string) --* **[REQUIRED]**

            The database in which the table metadata resides.

          - **TableName** *(string) --* **[REQUIRED]**

            The name of the table in question.

        :type Sinks: list
        :param Sinks:

          The target tables.

          - *(dict) --*

            Specifies a table definition in the AWS Glue Data Catalog.

            - **DatabaseName** *(string) --* **[REQUIRED]**

              The database in which the table metadata resides.

            - **TableName** *(string) --* **[REQUIRED]**

              The name of the table in question.

        :type Location: dict
        :param Location:

          The parameters for the mapping.

          - **Jdbc** *(list) --*

            A JDBC location.

            - *(dict) --*

              An argument or property of a node.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the argument or property.

              - **Value** *(string) --* **[REQUIRED]**

                The value of the argument or property.

              - **Param** *(boolean) --*

                True if the value is used as a parameter.

          - **S3** *(list) --*

            An Amazon Simple Storage Service (Amazon S3) location.

            - *(dict) --*

              An argument or property of a node.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the argument or property.

              - **Value** *(string) --* **[REQUIRED]**

                The value of the argument or property.

              - **Param** *(boolean) --*

                True if the value is used as a parameter.

          - **DynamoDB** *(list) --*

            An Amazon DynamoDB table location.

            - *(dict) --*

              An argument or property of a node.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the argument or property.

              - **Value** *(string) --* **[REQUIRED]**

                The value of the argument or property.

              - **Param** *(boolean) --*

                True if the value is used as a parameter.

        :type Language: string
        :param Language:

          The programming language of the code to perform the mapping.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PythonScript': 'string',
                'ScalaCode': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PythonScript** *(string) --*

              A Python script to perform the mapping.

            - **ScalaCode** *(string) --*

              The Scala code to perform the mapping.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_policy(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetResourcePolicyResponseTypeDef:
        """
        Retrieves a specified resource policy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetResourcePolicy>`_

        **Request Syntax**
        ::

          response = client.get_resource_policy()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyInJson': 'string',
                'PolicyHash': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'UpdateTime': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyInJson** *(string) --*

              Contains the requested policy document, in JSON format.

            - **PolicyHash** *(string) --*

              Contains the hash value associated with this policy.

            - **CreateTime** *(datetime) --*

              The date and time at which the policy was created.

            - **UpdateTime** *(datetime) --*

              The date and time at which the policy was last updated.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_security_configuration(
        self, Name: str
    ) -> ClientGetSecurityConfigurationResponseTypeDef:
        """
        Retrieves a specified security configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetSecurityConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_security_configuration(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the security configuration to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SecurityConfiguration': {
                    'Name': 'string',
                    'CreatedTimeStamp': datetime(2015, 1, 1),
                    'EncryptionConfiguration': {
                        'S3Encryption': [
                            {
                                'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                                'KmsKeyArn': 'string'
                            },
                        ],
                        'CloudWatchEncryption': {
                            'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                            'KmsKeyArn': 'string'
                        },
                        'JobBookmarksEncryption': {
                            'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                            'KmsKeyArn': 'string'
                        }
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **SecurityConfiguration** *(dict) --*

              The requested security configuration.

              - **Name** *(string) --*

                The name of the security configuration.

              - **CreatedTimeStamp** *(datetime) --*

                The time at which this security configuration was created.

              - **EncryptionConfiguration** *(dict) --*

                The encryption configuration associated with this security configuration.

                - **S3Encryption** *(list) --*

                  The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.

                  - *(dict) --*

                    Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.

                    - **S3EncryptionMode** *(string) --*

                      The encryption mode to use for Amazon S3 data.

                    - **KmsKeyArn** *(string) --*

                      The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

                - **CloudWatchEncryption** *(dict) --*

                  The encryption configuration for Amazon CloudWatch.

                  - **CloudWatchEncryptionMode** *(string) --*

                    The encryption mode to use for CloudWatch data.

                  - **KmsKeyArn** *(string) --*

                    The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

                - **JobBookmarksEncryption** *(dict) --*

                  The encryption configuration for job bookmarks.

                  - **JobBookmarksEncryptionMode** *(string) --*

                    The encryption mode to use for job bookmarks data.

                  - **KmsKeyArn** *(string) --*

                    The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_security_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetSecurityConfigurationsResponseTypeDef:
        """
        Retrieves a list of all security configurations.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetSecurityConfigurations>`_

        **Request Syntax**
        ::

          response = client.get_security_configurations(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SecurityConfigurations': [
                    {
                        'Name': 'string',
                        'CreatedTimeStamp': datetime(2015, 1, 1),
                        'EncryptionConfiguration': {
                            'S3Encryption': [
                                {
                                    'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                                    'KmsKeyArn': 'string'
                                },
                            ],
                            'CloudWatchEncryption': {
                                'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                                'KmsKeyArn': 'string'
                            },
                            'JobBookmarksEncryption': {
                                'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                                'KmsKeyArn': 'string'
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **SecurityConfigurations** *(list) --*

              A list of security configurations.

              - *(dict) --*

                Specifies a security configuration.

                - **Name** *(string) --*

                  The name of the security configuration.

                - **CreatedTimeStamp** *(datetime) --*

                  The time at which this security configuration was created.

                - **EncryptionConfiguration** *(dict) --*

                  The encryption configuration associated with this security configuration.

                  - **S3Encryption** *(list) --*

                    The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.

                    - *(dict) --*

                      Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.

                      - **S3EncryptionMode** *(string) --*

                        The encryption mode to use for Amazon S3 data.

                      - **KmsKeyArn** *(string) --*

                        The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

                  - **CloudWatchEncryption** *(dict) --*

                    The encryption configuration for Amazon CloudWatch.

                    - **CloudWatchEncryptionMode** *(string) --*

                      The encryption mode to use for CloudWatch data.

                    - **KmsKeyArn** *(string) --*

                      The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

                  - **JobBookmarksEncryption** *(dict) --*

                    The encryption configuration for job bookmarks.

                    - **JobBookmarksEncryptionMode** *(string) --*

                      The encryption mode to use for job bookmarks data.

                    - **KmsKeyArn** *(string) --*

                      The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

            - **NextToken** *(string) --*

              A continuation token, if there are more security configurations to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_table(
        self, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> ClientGetTableResponseTypeDef:
        """
        Retrieves the ``Table`` definition in a Data Catalog for a specified table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTable>`_

        **Request Syntax**
        ::

          response = client.get_table(
              CatalogId='string',
              DatabaseName='string',
              Name='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the database in the catalog in which the table resides. For Hive compatibility, this
          name is entirely lowercase.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the table for which to retrieve the definition. For Hive compatibility, this name is
          entirely lowercase.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Table': {
                    'Name': 'string',
                    'DatabaseName': 'string',
                    'Description': 'string',
                    'Owner': 'string',
                    'CreateTime': datetime(2015, 1, 1),
                    'UpdateTime': datetime(2015, 1, 1),
                    'LastAccessTime': datetime(2015, 1, 1),
                    'LastAnalyzedTime': datetime(2015, 1, 1),
                    'Retention': 123,
                    'StorageDescriptor': {
                        'Columns': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'Location': 'string',
                        'InputFormat': 'string',
                        'OutputFormat': 'string',
                        'Compressed': True|False,
                        'NumberOfBuckets': 123,
                        'SerdeInfo': {
                            'Name': 'string',
                            'SerializationLibrary': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                        'BucketColumns': [
                            'string',
                        ],
                        'SortColumns': [
                            {
                                'Column': 'string',
                                'SortOrder': 123
                            },
                        ],
                        'Parameters': {
                            'string': 'string'
                        },
                        'SkewedInfo': {
                            'SkewedColumnNames': [
                                'string',
                            ],
                            'SkewedColumnValues': [
                                'string',
                            ],
                            'SkewedColumnValueLocationMaps': {
                                'string': 'string'
                            }
                        },
                        'StoredAsSubDirectories': True|False
                    },
                    'PartitionKeys': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'ViewOriginalText': 'string',
                    'ViewExpandedText': 'string',
                    'TableType': 'string',
                    'Parameters': {
                        'string': 'string'
                    },
                    'CreatedBy': 'string',
                    'IsRegisteredWithLakeFormation': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Table** *(dict) --*

              The ``Table`` object that defines the specified table.

              - **Name** *(string) --*

                The table name. For Hive compatibility, this must be entirely lowercase.

              - **DatabaseName** *(string) --*

                The name of the database where the table metadata resides. For Hive compatibility, this
                must be all lowercase.

              - **Description** *(string) --*

                A description of the table.

              - **Owner** *(string) --*

                The owner of the table.

              - **CreateTime** *(datetime) --*

                The time when the table definition was created in the Data Catalog.

              - **UpdateTime** *(datetime) --*

                The last time that the table was updated.

              - **LastAccessTime** *(datetime) --*

                The last time that the table was accessed. This is usually taken from HDFS, and might not
                be reliable.

              - **LastAnalyzedTime** *(datetime) --*

                The last time that column statistics were computed for this table.

              - **Retention** *(integer) --*

                The retention time for this table.

              - **StorageDescriptor** *(dict) --*

                A storage descriptor containing information about the physical storage of this table.

                - **Columns** *(list) --*

                  A list of the ``Columns`` in the table.

                  - *(dict) --*

                    A column in a ``Table`` .

                    - **Name** *(string) --*

                      The name of the ``Column`` .

                    - **Type** *(string) --*

                      The data type of the ``Column`` .

                    - **Comment** *(string) --*

                      A free-form text comment.

                    - **Parameters** *(dict) --*

                      These key-value pairs define properties associated with the column.

                      - *(string) --*

                        - *(string) --*

                - **Location** *(string) --*

                  The physical location of the table. By default, this takes the form of the warehouse
                  location, followed by the database location in the warehouse, followed by the table name.

                - **InputFormat** *(string) --*

                  The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                  custom format.

                - **OutputFormat** *(string) --*

                  The output format: ``SequenceFileOutputFormat`` (binary), or
                  ``IgnoreKeyTextOutputFormat`` , or a custom format.

                - **Compressed** *(boolean) --*

                   ``True`` if the data in the table is compressed, or ``False`` if not.

                - **NumberOfBuckets** *(integer) --*

                  Must be specified if the table contains any dimension columns.

                - **SerdeInfo** *(dict) --*

                  The serialization/deserialization (SerDe) information.

                  - **Name** *(string) --*

                    Name of the SerDe.

                  - **SerializationLibrary** *(string) --*

                    Usually the class that implements the SerDe. An example is
                    ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                  - **Parameters** *(dict) --*

                    These key-value pairs define initialization parameters for the SerDe.

                    - *(string) --*

                      - *(string) --*

                - **BucketColumns** *(list) --*

                  A list of reducer grouping columns, clustering columns, and bucketing columns in the
                  table.

                  - *(string) --*

                - **SortColumns** *(list) --*

                  A list specifying the sort order of each bucket in the table.

                  - *(dict) --*

                    Specifies the sort order of a sorted column.

                    - **Column** *(string) --*

                      The name of the column.

                    - **SortOrder** *(integer) --*

                      Indicates that the column is sorted in ascending order (``== 1`` ), or in descending
                      order (``==0`` ).

                - **Parameters** *(dict) --*

                  The user-supplied properties in key-value form.

                  - *(string) --*

                    - *(string) --*

                - **SkewedInfo** *(dict) --*

                  The information about values that appear frequently in a column (skewed values).

                  - **SkewedColumnNames** *(list) --*

                    A list of names of columns that contain skewed values.

                    - *(string) --*

                  - **SkewedColumnValues** *(list) --*

                    A list of values that appear so frequently as to be considered skewed.

                    - *(string) --*

                  - **SkewedColumnValueLocationMaps** *(dict) --*

                    A mapping of skewed values to the columns that contain them.

                    - *(string) --*

                      - *(string) --*

                - **StoredAsSubDirectories** *(boolean) --*

                   ``True`` if the table data is stored in subdirectories, or ``False`` if not.

              - **PartitionKeys** *(list) --*

                A list of columns by which the table is partitioned. Only primitive types are supported as
                partition keys.

                When you create a table used by Amazon Athena, and you do not specify any ``partitionKeys``
                , you must at least set the value of ``partitionKeys`` to an empty list. For example:

                 ``"PartitionKeys": []``

                - *(dict) --*

                  A column in a ``Table`` .

                  - **Name** *(string) --*

                    The name of the ``Column`` .

                  - **Type** *(string) --*

                    The data type of the ``Column`` .

                  - **Comment** *(string) --*

                    A free-form text comment.

                  - **Parameters** *(dict) --*

                    These key-value pairs define properties associated with the column.

                    - *(string) --*

                      - *(string) --*

              - **ViewOriginalText** *(string) --*

                If the table is a view, the original text of the view; otherwise ``null`` .

              - **ViewExpandedText** *(string) --*

                If the table is a view, the expanded text of the view; otherwise ``null`` .

              - **TableType** *(string) --*

                The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

              - **Parameters** *(dict) --*

                These key-value pairs define properties associated with the table.

                - *(string) --*

                  - *(string) --*

              - **CreatedBy** *(string) --*

                The person or entity who created the table.

              - **IsRegisteredWithLakeFormation** *(boolean) --*

                Indicates whether the table has been registered with AWS Lake Formation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_table_version(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        VersionId: str = None,
    ) -> ClientGetTableVersionResponseTypeDef:
        """
        Retrieves a specified version of a table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTableVersion>`_

        **Request Syntax**
        ::

          response = client.get_table_version(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              VersionId='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The database in the catalog in which the table resides. For Hive compatibility, this name is
          entirely lowercase.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the table. For Hive compatibility, this name is entirely lowercase.

        :type VersionId: string
        :param VersionId:

          The ID value of the table version to be retrieved. A ``VersionID`` is a string representation of
          an integer. Each version is incremented by 1.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TableVersion': {
                    'Table': {
                        'Name': 'string',
                        'DatabaseName': 'string',
                        'Description': 'string',
                        'Owner': 'string',
                        'CreateTime': datetime(2015, 1, 1),
                        'UpdateTime': datetime(2015, 1, 1),
                        'LastAccessTime': datetime(2015, 1, 1),
                        'LastAnalyzedTime': datetime(2015, 1, 1),
                        'Retention': 123,
                        'StorageDescriptor': {
                            'Columns': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'Location': 'string',
                            'InputFormat': 'string',
                            'OutputFormat': 'string',
                            'Compressed': True|False,
                            'NumberOfBuckets': 123,
                            'SerdeInfo': {
                                'Name': 'string',
                                'SerializationLibrary': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                            'BucketColumns': [
                                'string',
                            ],
                            'SortColumns': [
                                {
                                    'Column': 'string',
                                    'SortOrder': 123
                                },
                            ],
                            'Parameters': {
                                'string': 'string'
                            },
                            'SkewedInfo': {
                                'SkewedColumnNames': [
                                    'string',
                                ],
                                'SkewedColumnValues': [
                                    'string',
                                ],
                                'SkewedColumnValueLocationMaps': {
                                    'string': 'string'
                                }
                            },
                            'StoredAsSubDirectories': True|False
                        },
                        'PartitionKeys': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'ViewOriginalText': 'string',
                        'ViewExpandedText': 'string',
                        'TableType': 'string',
                        'Parameters': {
                            'string': 'string'
                        },
                        'CreatedBy': 'string',
                        'IsRegisteredWithLakeFormation': True|False
                    },
                    'VersionId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **TableVersion** *(dict) --*

              The requested table version.

              - **Table** *(dict) --*

                The table in question.

                - **Name** *(string) --*

                  The table name. For Hive compatibility, this must be entirely lowercase.

                - **DatabaseName** *(string) --*

                  The name of the database where the table metadata resides. For Hive compatibility, this
                  must be all lowercase.

                - **Description** *(string) --*

                  A description of the table.

                - **Owner** *(string) --*

                  The owner of the table.

                - **CreateTime** *(datetime) --*

                  The time when the table definition was created in the Data Catalog.

                - **UpdateTime** *(datetime) --*

                  The last time that the table was updated.

                - **LastAccessTime** *(datetime) --*

                  The last time that the table was accessed. This is usually taken from HDFS, and might not
                  be reliable.

                - **LastAnalyzedTime** *(datetime) --*

                  The last time that column statistics were computed for this table.

                - **Retention** *(integer) --*

                  The retention time for this table.

                - **StorageDescriptor** *(dict) --*

                  A storage descriptor containing information about the physical storage of this table.

                  - **Columns** *(list) --*

                    A list of the ``Columns`` in the table.

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **Location** *(string) --*

                    The physical location of the table. By default, this takes the form of the warehouse
                    location, followed by the database location in the warehouse, followed by the table
                    name.

                  - **InputFormat** *(string) --*

                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                    custom format.

                  - **OutputFormat** *(string) --*

                    The output format: ``SequenceFileOutputFormat`` (binary), or
                    ``IgnoreKeyTextOutputFormat`` , or a custom format.

                  - **Compressed** *(boolean) --*

                     ``True`` if the data in the table is compressed, or ``False`` if not.

                  - **NumberOfBuckets** *(integer) --*

                    Must be specified if the table contains any dimension columns.

                  - **SerdeInfo** *(dict) --*

                    The serialization/deserialization (SerDe) information.

                    - **Name** *(string) --*

                      Name of the SerDe.

                    - **SerializationLibrary** *(string) --*

                      Usually the class that implements the SerDe. An example is
                      ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                    - **Parameters** *(dict) --*

                      These key-value pairs define initialization parameters for the SerDe.

                      - *(string) --*

                        - *(string) --*

                  - **BucketColumns** *(list) --*

                    A list of reducer grouping columns, clustering columns, and bucketing columns in the
                    table.

                    - *(string) --*

                  - **SortColumns** *(list) --*

                    A list specifying the sort order of each bucket in the table.

                    - *(dict) --*

                      Specifies the sort order of a sorted column.

                      - **Column** *(string) --*

                        The name of the column.

                      - **SortOrder** *(integer) --*

                        Indicates that the column is sorted in ascending order (``== 1`` ), or in
                        descending order (``==0`` ).

                  - **Parameters** *(dict) --*

                    The user-supplied properties in key-value form.

                    - *(string) --*

                      - *(string) --*

                  - **SkewedInfo** *(dict) --*

                    The information about values that appear frequently in a column (skewed values).

                    - **SkewedColumnNames** *(list) --*

                      A list of names of columns that contain skewed values.

                      - *(string) --*

                    - **SkewedColumnValues** *(list) --*

                      A list of values that appear so frequently as to be considered skewed.

                      - *(string) --*

                    - **SkewedColumnValueLocationMaps** *(dict) --*

                      A mapping of skewed values to the columns that contain them.

                      - *(string) --*

                        - *(string) --*

                  - **StoredAsSubDirectories** *(boolean) --*

                     ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                - **PartitionKeys** *(list) --*

                  A list of columns by which the table is partitioned. Only primitive types are supported
                  as partition keys.

                  When you create a table used by Amazon Athena, and you do not specify any
                  ``partitionKeys`` , you must at least set the value of ``partitionKeys`` to an empty
                  list. For example:

                   ``"PartitionKeys": []``

                  - *(dict) --*

                    A column in a ``Table`` .

                    - **Name** *(string) --*

                      The name of the ``Column`` .

                    - **Type** *(string) --*

                      The data type of the ``Column`` .

                    - **Comment** *(string) --*

                      A free-form text comment.

                    - **Parameters** *(dict) --*

                      These key-value pairs define properties associated with the column.

                      - *(string) --*

                        - *(string) --*

                - **ViewOriginalText** *(string) --*

                  If the table is a view, the original text of the view; otherwise ``null`` .

                - **ViewExpandedText** *(string) --*

                  If the table is a view, the expanded text of the view; otherwise ``null`` .

                - **TableType** *(string) --*

                  The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

                - **Parameters** *(dict) --*

                  These key-value pairs define properties associated with the table.

                  - *(string) --*

                    - *(string) --*

                - **CreatedBy** *(string) --*

                  The person or entity who created the table.

                - **IsRegisteredWithLakeFormation** *(boolean) --*

                  Indicates whether the table has been registered with AWS Lake Formation.

              - **VersionId** *(string) --*

                The ID value that identifies this table version. A ``VersionId`` is a string representation
                of an integer. Each version is incremented by 1.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_table_versions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetTableVersionsResponseTypeDef:
        """
        Retrieves a list of strings that identify available versions of a specified table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTableVersions>`_

        **Request Syntax**
        ::

          response = client.get_table_versions(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              NextToken='string',
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The database in the catalog in which the table resides. For Hive compatibility, this name is
          entirely lowercase.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the table. For Hive compatibility, this name is entirely lowercase.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is not the first call.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of table versions to return in one response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TableVersions': [
                    {
                        'Table': {
                            'Name': 'string',
                            'DatabaseName': 'string',
                            'Description': 'string',
                            'Owner': 'string',
                            'CreateTime': datetime(2015, 1, 1),
                            'UpdateTime': datetime(2015, 1, 1),
                            'LastAccessTime': datetime(2015, 1, 1),
                            'LastAnalyzedTime': datetime(2015, 1, 1),
                            'Retention': 123,
                            'StorageDescriptor': {
                                'Columns': [
                                    {
                                        'Name': 'string',
                                        'Type': 'string',
                                        'Comment': 'string',
                                        'Parameters': {
                                            'string': 'string'
                                        }
                                    },
                                ],
                                'Location': 'string',
                                'InputFormat': 'string',
                                'OutputFormat': 'string',
                                'Compressed': True|False,
                                'NumberOfBuckets': 123,
                                'SerdeInfo': {
                                    'Name': 'string',
                                    'SerializationLibrary': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                                'BucketColumns': [
                                    'string',
                                ],
                                'SortColumns': [
                                    {
                                        'Column': 'string',
                                        'SortOrder': 123
                                    },
                                ],
                                'Parameters': {
                                    'string': 'string'
                                },
                                'SkewedInfo': {
                                    'SkewedColumnNames': [
                                        'string',
                                    ],
                                    'SkewedColumnValues': [
                                        'string',
                                    ],
                                    'SkewedColumnValueLocationMaps': {
                                        'string': 'string'
                                    }
                                },
                                'StoredAsSubDirectories': True|False
                            },
                            'PartitionKeys': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'ViewOriginalText': 'string',
                            'ViewExpandedText': 'string',
                            'TableType': 'string',
                            'Parameters': {
                                'string': 'string'
                            },
                            'CreatedBy': 'string',
                            'IsRegisteredWithLakeFormation': True|False
                        },
                        'VersionId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TableVersions** *(list) --*

              A list of strings identifying available versions of the specified table.

              - *(dict) --*

                Specifies a version of a table.

                - **Table** *(dict) --*

                  The table in question.

                  - **Name** *(string) --*

                    The table name. For Hive compatibility, this must be entirely lowercase.

                  - **DatabaseName** *(string) --*

                    The name of the database where the table metadata resides. For Hive compatibility, this
                    must be all lowercase.

                  - **Description** *(string) --*

                    A description of the table.

                  - **Owner** *(string) --*

                    The owner of the table.

                  - **CreateTime** *(datetime) --*

                    The time when the table definition was created in the Data Catalog.

                  - **UpdateTime** *(datetime) --*

                    The last time that the table was updated.

                  - **LastAccessTime** *(datetime) --*

                    The last time that the table was accessed. This is usually taken from HDFS, and might
                    not be reliable.

                  - **LastAnalyzedTime** *(datetime) --*

                    The last time that column statistics were computed for this table.

                  - **Retention** *(integer) --*

                    The retention time for this table.

                  - **StorageDescriptor** *(dict) --*

                    A storage descriptor containing information about the physical storage of this table.

                    - **Columns** *(list) --*

                      A list of the ``Columns`` in the table.

                      - *(dict) --*

                        A column in a ``Table`` .

                        - **Name** *(string) --*

                          The name of the ``Column`` .

                        - **Type** *(string) --*

                          The data type of the ``Column`` .

                        - **Comment** *(string) --*

                          A free-form text comment.

                        - **Parameters** *(dict) --*

                          These key-value pairs define properties associated with the column.

                          - *(string) --*

                            - *(string) --*

                    - **Location** *(string) --*

                      The physical location of the table. By default, this takes the form of the warehouse
                      location, followed by the database location in the warehouse, followed by the table
                      name.

                    - **InputFormat** *(string) --*

                      The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                      custom format.

                    - **OutputFormat** *(string) --*

                      The output format: ``SequenceFileOutputFormat`` (binary), or
                      ``IgnoreKeyTextOutputFormat`` , or a custom format.

                    - **Compressed** *(boolean) --*

                       ``True`` if the data in the table is compressed, or ``False`` if not.

                    - **NumberOfBuckets** *(integer) --*

                      Must be specified if the table contains any dimension columns.

                    - **SerdeInfo** *(dict) --*

                      The serialization/deserialization (SerDe) information.

                      - **Name** *(string) --*

                        Name of the SerDe.

                      - **SerializationLibrary** *(string) --*

                        Usually the class that implements the SerDe. An example is
                        ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                      - **Parameters** *(dict) --*

                        These key-value pairs define initialization parameters for the SerDe.

                        - *(string) --*

                          - *(string) --*

                    - **BucketColumns** *(list) --*

                      A list of reducer grouping columns, clustering columns, and bucketing columns in the
                      table.

                      - *(string) --*

                    - **SortColumns** *(list) --*

                      A list specifying the sort order of each bucket in the table.

                      - *(dict) --*

                        Specifies the sort order of a sorted column.

                        - **Column** *(string) --*

                          The name of the column.

                        - **SortOrder** *(integer) --*

                          Indicates that the column is sorted in ascending order (``== 1`` ), or in
                          descending order (``==0`` ).

                    - **Parameters** *(dict) --*

                      The user-supplied properties in key-value form.

                      - *(string) --*

                        - *(string) --*

                    - **SkewedInfo** *(dict) --*

                      The information about values that appear frequently in a column (skewed values).

                      - **SkewedColumnNames** *(list) --*

                        A list of names of columns that contain skewed values.

                        - *(string) --*

                      - **SkewedColumnValues** *(list) --*

                        A list of values that appear so frequently as to be considered skewed.

                        - *(string) --*

                      - **SkewedColumnValueLocationMaps** *(dict) --*

                        A mapping of skewed values to the columns that contain them.

                        - *(string) --*

                          - *(string) --*

                    - **StoredAsSubDirectories** *(boolean) --*

                       ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                  - **PartitionKeys** *(list) --*

                    A list of columns by which the table is partitioned. Only primitive types are supported
                    as partition keys.

                    When you create a table used by Amazon Athena, and you do not specify any
                    ``partitionKeys`` , you must at least set the value of ``partitionKeys`` to an empty
                    list. For example:

                     ``"PartitionKeys": []``

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **ViewOriginalText** *(string) --*

                    If the table is a view, the original text of the view; otherwise ``null`` .

                  - **ViewExpandedText** *(string) --*

                    If the table is a view, the expanded text of the view; otherwise ``null`` .

                  - **TableType** *(string) --*

                    The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

                  - **Parameters** *(dict) --*

                    These key-value pairs define properties associated with the table.

                    - *(string) --*

                      - *(string) --*

                  - **CreatedBy** *(string) --*

                    The person or entity who created the table.

                  - **IsRegisteredWithLakeFormation** *(boolean) --*

                    Indicates whether the table has been registered with AWS Lake Formation.

                - **VersionId** *(string) --*

                  The ID value that identifies this table version. A ``VersionId`` is a string
                  representation of an integer. Each version is incremented by 1.

            - **NextToken** *(string) --*

              A continuation token, if the list of available versions does not include the last one.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tables(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetTablesResponseTypeDef:
        """
        Retrieves the definitions of some or all of the tables in a given ``Database`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTables>`_

        **Request Syntax**
        ::

          response = client.get_tables(
              CatalogId='string',
              DatabaseName='string',
              Expression='string',
              NextToken='string',
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The database in the catalog whose tables to list. For Hive compatibility, this name is entirely
          lowercase.

        :type Expression: string
        :param Expression:

          A regular expression pattern. If present, only those tables whose names match the pattern are
          returned.

        :type NextToken: string
        :param NextToken:

          A continuation token, included if this is a continuation call.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of tables to return in a single response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TableList': [
                    {
                        'Name': 'string',
                        'DatabaseName': 'string',
                        'Description': 'string',
                        'Owner': 'string',
                        'CreateTime': datetime(2015, 1, 1),
                        'UpdateTime': datetime(2015, 1, 1),
                        'LastAccessTime': datetime(2015, 1, 1),
                        'LastAnalyzedTime': datetime(2015, 1, 1),
                        'Retention': 123,
                        'StorageDescriptor': {
                            'Columns': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'Location': 'string',
                            'InputFormat': 'string',
                            'OutputFormat': 'string',
                            'Compressed': True|False,
                            'NumberOfBuckets': 123,
                            'SerdeInfo': {
                                'Name': 'string',
                                'SerializationLibrary': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                            'BucketColumns': [
                                'string',
                            ],
                            'SortColumns': [
                                {
                                    'Column': 'string',
                                    'SortOrder': 123
                                },
                            ],
                            'Parameters': {
                                'string': 'string'
                            },
                            'SkewedInfo': {
                                'SkewedColumnNames': [
                                    'string',
                                ],
                                'SkewedColumnValues': [
                                    'string',
                                ],
                                'SkewedColumnValueLocationMaps': {
                                    'string': 'string'
                                }
                            },
                            'StoredAsSubDirectories': True|False
                        },
                        'PartitionKeys': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'ViewOriginalText': 'string',
                        'ViewExpandedText': 'string',
                        'TableType': 'string',
                        'Parameters': {
                            'string': 'string'
                        },
                        'CreatedBy': 'string',
                        'IsRegisteredWithLakeFormation': True|False
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TableList** *(list) --*

              A list of the requested ``Table`` objects.

              - *(dict) --*

                Represents a collection of related data organized in columns and rows.

                - **Name** *(string) --*

                  The table name. For Hive compatibility, this must be entirely lowercase.

                - **DatabaseName** *(string) --*

                  The name of the database where the table metadata resides. For Hive compatibility, this
                  must be all lowercase.

                - **Description** *(string) --*

                  A description of the table.

                - **Owner** *(string) --*

                  The owner of the table.

                - **CreateTime** *(datetime) --*

                  The time when the table definition was created in the Data Catalog.

                - **UpdateTime** *(datetime) --*

                  The last time that the table was updated.

                - **LastAccessTime** *(datetime) --*

                  The last time that the table was accessed. This is usually taken from HDFS, and might not
                  be reliable.

                - **LastAnalyzedTime** *(datetime) --*

                  The last time that column statistics were computed for this table.

                - **Retention** *(integer) --*

                  The retention time for this table.

                - **StorageDescriptor** *(dict) --*

                  A storage descriptor containing information about the physical storage of this table.

                  - **Columns** *(list) --*

                    A list of the ``Columns`` in the table.

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **Location** *(string) --*

                    The physical location of the table. By default, this takes the form of the warehouse
                    location, followed by the database location in the warehouse, followed by the table
                    name.

                  - **InputFormat** *(string) --*

                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                    custom format.

                  - **OutputFormat** *(string) --*

                    The output format: ``SequenceFileOutputFormat`` (binary), or
                    ``IgnoreKeyTextOutputFormat`` , or a custom format.

                  - **Compressed** *(boolean) --*

                     ``True`` if the data in the table is compressed, or ``False`` if not.

                  - **NumberOfBuckets** *(integer) --*

                    Must be specified if the table contains any dimension columns.

                  - **SerdeInfo** *(dict) --*

                    The serialization/deserialization (SerDe) information.

                    - **Name** *(string) --*

                      Name of the SerDe.

                    - **SerializationLibrary** *(string) --*

                      Usually the class that implements the SerDe. An example is
                      ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                    - **Parameters** *(dict) --*

                      These key-value pairs define initialization parameters for the SerDe.

                      - *(string) --*

                        - *(string) --*

                  - **BucketColumns** *(list) --*

                    A list of reducer grouping columns, clustering columns, and bucketing columns in the
                    table.

                    - *(string) --*

                  - **SortColumns** *(list) --*

                    A list specifying the sort order of each bucket in the table.

                    - *(dict) --*

                      Specifies the sort order of a sorted column.

                      - **Column** *(string) --*

                        The name of the column.

                      - **SortOrder** *(integer) --*

                        Indicates that the column is sorted in ascending order (``== 1`` ), or in
                        descending order (``==0`` ).

                  - **Parameters** *(dict) --*

                    The user-supplied properties in key-value form.

                    - *(string) --*

                      - *(string) --*

                  - **SkewedInfo** *(dict) --*

                    The information about values that appear frequently in a column (skewed values).

                    - **SkewedColumnNames** *(list) --*

                      A list of names of columns that contain skewed values.

                      - *(string) --*

                    - **SkewedColumnValues** *(list) --*

                      A list of values that appear so frequently as to be considered skewed.

                      - *(string) --*

                    - **SkewedColumnValueLocationMaps** *(dict) --*

                      A mapping of skewed values to the columns that contain them.

                      - *(string) --*

                        - *(string) --*

                  - **StoredAsSubDirectories** *(boolean) --*

                     ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                - **PartitionKeys** *(list) --*

                  A list of columns by which the table is partitioned. Only primitive types are supported
                  as partition keys.

                  When you create a table used by Amazon Athena, and you do not specify any
                  ``partitionKeys`` , you must at least set the value of ``partitionKeys`` to an empty
                  list. For example:

                   ``"PartitionKeys": []``

                  - *(dict) --*

                    A column in a ``Table`` .

                    - **Name** *(string) --*

                      The name of the ``Column`` .

                    - **Type** *(string) --*

                      The data type of the ``Column`` .

                    - **Comment** *(string) --*

                      A free-form text comment.

                    - **Parameters** *(dict) --*

                      These key-value pairs define properties associated with the column.

                      - *(string) --*

                        - *(string) --*

                - **ViewOriginalText** *(string) --*

                  If the table is a view, the original text of the view; otherwise ``null`` .

                - **ViewExpandedText** *(string) --*

                  If the table is a view, the expanded text of the view; otherwise ``null`` .

                - **TableType** *(string) --*

                  The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

                - **Parameters** *(dict) --*

                  These key-value pairs define properties associated with the table.

                  - *(string) --*

                    - *(string) --*

                - **CreatedBy** *(string) --*

                  The person or entity who created the table.

                - **IsRegisteredWithLakeFormation** *(boolean) --*

                  Indicates whether the table has been registered with AWS Lake Formation.

            - **NextToken** *(string) --*

              A continuation token, present if the current list segment is not the last.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tags(self, ResourceArn: str) -> ClientGetTagsResponseTypeDef:
        """
        Retrieves a list of tags associated with a resource.

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTags>`_

        **Request Syntax**
        ::

          response = client.get_tags(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource for which to retrieve tags.

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

              The requested tags.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_trigger(self, Name: str) -> ClientGetTriggerResponseTypeDef:
        """
        Retrieves the definition of a trigger.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTrigger>`_

        **Request Syntax**
        ::

          response = client.get_trigger(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the trigger to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Trigger': {
                    'Name': 'string',
                    'WorkflowName': 'string',
                    'Id': 'string',
                    'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                    'State':
                    'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'
                    |'UPDATING',
                    'Description': 'string',
                    'Schedule': 'string',
                    'Actions': [
                        {
                            'JobName': 'string',
                            'Arguments': {
                                'string': 'string'
                            },
                            'Timeout': 123,
                            'SecurityConfiguration': 'string',
                            'NotificationProperty': {
                                'NotifyDelayAfter': 123
                            },
                            'CrawlerName': 'string'
                        },
                    ],
                    'Predicate': {
                        'Logical': 'AND'|'ANY',
                        'Conditions': [
                            {
                                'LogicalOperator': 'EQUALS',
                                'JobName': 'string',
                                'State':
                                'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                'CrawlerName': 'string',
                                'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                            },
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Trigger** *(dict) --*

              The requested trigger definition.

              - **Name** *(string) --*

                The name of the trigger.

              - **WorkflowName** *(string) --*

                The name of the workflow associated with the trigger.

              - **Id** *(string) --*

                Reserved for future use.

              - **Type** *(string) --*

                The type of trigger that this is.

              - **State** *(string) --*

                The current state of the trigger.

              - **Description** *(string) --*

                A description of this trigger.

              - **Schedule** *(string) --*

                A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and
                Crawlers
                <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For
                example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ?
                *)`` .

              - **Actions** *(list) --*

                The actions initiated by this trigger.

                - *(dict) --*

                  Defines an action to be initiated by a trigger.

                  - **JobName** *(string) --*

                    The name of a job to be executed.

                  - **Arguments** *(dict) --*

                    The job arguments used when this trigger fires. For this job run, they replace the
                    default arguments set in the job definition itself.

                    You can specify arguments here that your own job-execution script consumes, as well as
                    arguments that AWS Glue itself consumes.

                    For information about how to specify and consume your own Job arguments, see the
                    `Calling AWS Glue APIs in Python
                    <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                    topic in the developer guide.

                    For information about the key-value pairs that AWS Glue consumes to set up your job,
                    see the `Special Parameters Used by AWS Glue
                    <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                    topic in the developer guide.

                    - *(string) --*

                      - *(string) --*

                  - **Timeout** *(integer) --*

                    The ``JobRun`` timeout in minutes. This is the maximum time that a job run can consume
                    resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880
                    minutes (48 hours). This overrides the timeout value set in the parent job.

                  - **SecurityConfiguration** *(string) --*

                    The name of the ``SecurityConfiguration`` structure to be used with this action.

                  - **NotificationProperty** *(dict) --*

                    Specifies configuration properties of a job run notification.

                    - **NotifyDelayAfter** *(integer) --*

                      After a job run starts, the number of minutes to wait before sending a job run delay
                      notification.

                  - **CrawlerName** *(string) --*

                    The name of the crawler to be used with this action.

              - **Predicate** *(dict) --*

                The predicate of this trigger, which defines when it will fire.

                - **Logical** *(string) --*

                  An optional field if only one condition is listed. If multiple conditions are listed,
                  then this field is required.

                - **Conditions** *(list) --*

                  A list of the conditions that determine when the trigger will fire.

                  - *(dict) --*

                    Defines a condition under which a trigger fires.

                    - **LogicalOperator** *(string) --*

                      A logical operator.

                    - **JobName** *(string) --*

                      The name of the job whose ``JobRuns`` this condition applies to, and on which this
                      trigger waits.

                    - **State** *(string) --*

                      The condition state. Currently, the values supported are ``SUCCEEDED`` , ``STOPPED``
                      , ``TIMEOUT`` , and ``FAILED`` .

                    - **CrawlerName** *(string) --*

                      The name of the crawler to which this condition applies.

                    - **CrawlState** *(string) --*

                      The state of the crawler to which this condition applies.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_triggers(
        self,
        NextToken: str = None,
        DependentJobName: str = None,
        MaxResults: int = None,
    ) -> ClientGetTriggersResponseTypeDef:
        """
        Gets all the triggers associated with a job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTriggers>`_

        **Request Syntax**
        ::

          response = client.get_triggers(
              NextToken='string',
              DependentJobName='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :type DependentJobName: string
        :param DependentJobName:

          The name of the job to retrieve triggers for. The trigger that can start this job is returned,
          and if there is no such trigger, all triggers are returned.

        :type MaxResults: integer
        :param MaxResults:

          The maximum size of the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Triggers': [
                    {
                        'Name': 'string',
                        'WorkflowName': 'string',
                        'Id': 'string',
                        'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                        'State':
                        'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'
                        |'DELETING'|'UPDATING',
                        'Description': 'string',
                        'Schedule': 'string',
                        'Actions': [
                            {
                                'JobName': 'string',
                                'Arguments': {
                                    'string': 'string'
                                },
                                'Timeout': 123,
                                'SecurityConfiguration': 'string',
                                'NotificationProperty': {
                                    'NotifyDelayAfter': 123
                                },
                                'CrawlerName': 'string'
                            },
                        ],
                        'Predicate': {
                            'Logical': 'AND'|'ANY',
                            'Conditions': [
                                {
                                    'LogicalOperator': 'EQUALS',
                                    'JobName': 'string',
                                    'State':
                                    'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                                    |'TIMEOUT',
                                    'CrawlerName': 'string',
                                    'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                },
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Triggers** *(list) --*

              A list of triggers for the specified job.

              - *(dict) --*

                Information about a specific trigger.

                - **Name** *(string) --*

                  The name of the trigger.

                - **WorkflowName** *(string) --*

                  The name of the workflow associated with the trigger.

                - **Id** *(string) --*

                  Reserved for future use.

                - **Type** *(string) --*

                  The type of trigger that this is.

                - **State** *(string) --*

                  The current state of the trigger.

                - **Description** *(string) --*

                  A description of this trigger.

                - **Schedule** *(string) --*

                  A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs
                  and Crawlers
                  <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ .
                  For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * *
                  ? *)`` .

                - **Actions** *(list) --*

                  The actions initiated by this trigger.

                  - *(dict) --*

                    Defines an action to be initiated by a trigger.

                    - **JobName** *(string) --*

                      The name of a job to be executed.

                    - **Arguments** *(dict) --*

                      The job arguments used when this trigger fires. For this job run, they replace the
                      default arguments set in the job definition itself.

                      You can specify arguments here that your own job-execution script consumes, as well
                      as arguments that AWS Glue itself consumes.

                      For information about how to specify and consume your own Job arguments, see the
                      `Calling AWS Glue APIs in Python
                      <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                      topic in the developer guide.

                      For information about the key-value pairs that AWS Glue consumes to set up your job,
                      see the `Special Parameters Used by AWS Glue
                      <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                      topic in the developer guide.

                      - *(string) --*

                        - *(string) --*

                    - **Timeout** *(integer) --*

                      The ``JobRun`` timeout in minutes. This is the maximum time that a job run can
                      consume resources before it is terminated and enters ``TIMEOUT`` status. The default
                      is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

                    - **SecurityConfiguration** *(string) --*

                      The name of the ``SecurityConfiguration`` structure to be used with this action.

                    - **NotificationProperty** *(dict) --*

                      Specifies configuration properties of a job run notification.

                      - **NotifyDelayAfter** *(integer) --*

                        After a job run starts, the number of minutes to wait before sending a job run
                        delay notification.

                    - **CrawlerName** *(string) --*

                      The name of the crawler to be used with this action.

                - **Predicate** *(dict) --*

                  The predicate of this trigger, which defines when it will fire.

                  - **Logical** *(string) --*

                    An optional field if only one condition is listed. If multiple conditions are listed,
                    then this field is required.

                  - **Conditions** *(list) --*

                    A list of the conditions that determine when the trigger will fire.

                    - *(dict) --*

                      Defines a condition under which a trigger fires.

                      - **LogicalOperator** *(string) --*

                        A logical operator.

                      - **JobName** *(string) --*

                        The name of the job whose ``JobRuns`` this condition applies to, and on which this
                        trigger waits.

                      - **State** *(string) --*

                        The condition state. Currently, the values supported are ``SUCCEEDED`` ,
                        ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                      - **CrawlerName** *(string) --*

                        The name of the crawler to which this condition applies.

                      - **CrawlState** *(string) --*

                        The state of the crawler to which this condition applies.

            - **NextToken** *(string) --*

              A continuation token, if not all the requested triggers have yet been returned.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> ClientGetUserDefinedFunctionResponseTypeDef:
        """
        Retrieves a specified function definition from the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetUserDefinedFunction>`_

        **Request Syntax**
        ::

          response = client.get_user_defined_function(
              CatalogId='string',
              DatabaseName='string',
              FunctionName='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the function to be retrieved is located. If none is provided,
          the AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the function is located.

        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserDefinedFunction': {
                    'FunctionName': 'string',
                    'ClassName': 'string',
                    'OwnerName': 'string',
                    'OwnerType': 'USER'|'ROLE'|'GROUP',
                    'CreateTime': datetime(2015, 1, 1),
                    'ResourceUris': [
                        {
                            'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                            'Uri': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **UserDefinedFunction** *(dict) --*

              The requested function definition.

              - **FunctionName** *(string) --*

                The name of the function.

              - **ClassName** *(string) --*

                The Java class that contains the function code.

              - **OwnerName** *(string) --*

                The owner of the function.

              - **OwnerType** *(string) --*

                The owner type.

              - **CreateTime** *(datetime) --*

                The time at which the function was created.

              - **ResourceUris** *(list) --*

                The resource URIs for the function.

                - *(dict) --*

                  The URIs for function resources.

                  - **ResourceType** *(string) --*

                    The type of the resource.

                  - **Uri** *(string) --*

                    The URI for accessing the resource.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_defined_functions(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetUserDefinedFunctionsResponseTypeDef:
        """
        Retrieves multiple function definitions from the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetUserDefinedFunctions>`_

        **Request Syntax**
        ::

          response = client.get_user_defined_functions(
              CatalogId='string',
              DatabaseName='string',
              Pattern='string',
              NextToken='string',
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the functions to be retrieved are located. If none is provided,
          the AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the functions are located.

        :type Pattern: string
        :param Pattern: **[REQUIRED]**

          An optional function-name pattern string that filters the function definitions returned.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation call.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of functions to return in one response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserDefinedFunctions': [
                    {
                        'FunctionName': 'string',
                        'ClassName': 'string',
                        'OwnerName': 'string',
                        'OwnerType': 'USER'|'ROLE'|'GROUP',
                        'CreateTime': datetime(2015, 1, 1),
                        'ResourceUris': [
                            {
                                'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                                'Uri': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **UserDefinedFunctions** *(list) --*

              A list of requested function definitions.

              - *(dict) --*

                Represents the equivalent of a Hive user-defined function (``UDF`` ) definition.

                - **FunctionName** *(string) --*

                  The name of the function.

                - **ClassName** *(string) --*

                  The Java class that contains the function code.

                - **OwnerName** *(string) --*

                  The owner of the function.

                - **OwnerType** *(string) --*

                  The owner type.

                - **CreateTime** *(datetime) --*

                  The time at which the function was created.

                - **ResourceUris** *(list) --*

                  The resource URIs for the function.

                  - *(dict) --*

                    The URIs for function resources.

                    - **ResourceType** *(string) --*

                      The type of the resource.

                    - **Uri** *(string) --*

                      The URI for accessing the resource.

            - **NextToken** *(string) --*

              A continuation token, if the list of functions returned does not include the last requested
              function.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_workflow(
        self, Name: str, IncludeGraph: bool = None
    ) -> ClientGetWorkflowResponseTypeDef:
        """
        Retrieves resource metadata for a workflow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetWorkflow>`_

        **Request Syntax**
        ::

          response = client.get_workflow(
              Name='string',
              IncludeGraph=True|False
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the workflow to retrieve.

        :type IncludeGraph: boolean
        :param IncludeGraph:

          Specifies whether to include a graph when returning the workflow resource metadata.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Workflow': {
                    'Name': 'string',
                    'Description': 'string',
                    'DefaultRunProperties': {
                        'string': 'string'
                    },
                    'CreatedOn': datetime(2015, 1, 1),
                    'LastModifiedOn': datetime(2015, 1, 1),
                    'LastRun': {
                        'Name': 'string',
                        'WorkflowRunId': 'string',
                        'WorkflowRunProperties': {
                            'string': 'string'
                        },
                        'StartedOn': datetime(2015, 1, 1),
                        'CompletedOn': datetime(2015, 1, 1),
                        'Status': 'RUNNING'|'COMPLETED',
                        'Statistics': {
                            'TotalActions': 123,
                            'TimeoutActions': 123,
                            'FailedActions': 123,
                            'StoppedActions': 123,
                            'SucceededActions': 123,
                            'RunningActions': 123
                        },
                        'Graph': {
                            'Nodes': [
                                {
                                    'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                                    'Name': 'string',
                                    'UniqueId': 'string',
                                    'TriggerDetails': {
                                        'Trigger': {
                                            'Name': 'string',
                                            'WorkflowName': 'string',
                                            'Id': 'string',
                                            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                            'State':
                                            'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'
                                            |'DEACTIVATED'|'DELETING'|'UPDATING',
                                            'Description': 'string',
                                            'Schedule': 'string',
                                            'Actions': [
                                                {
                                                    'JobName': 'string',
                                                    'Arguments': {
                                                        'string': 'string'
                                                    },
                                                    'Timeout': 123,
                                                    'SecurityConfiguration': 'string',
                                                    'NotificationProperty': {
                                                        'NotifyDelayAfter': 123
                                                    },
                                                    'CrawlerName': 'string'
                                                },
                                            ],
                                            'Predicate': {
                                                'Logical': 'AND'|'ANY',
                                                'Conditions': [
                                                    {
                                                        'LogicalOperator': 'EQUALS',
                                                        'JobName': 'string',
                                                        'State':
                                                        'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'
                                                        |'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                        'CrawlerName': 'string',
                                                        'CrawlState':
                                                        'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                                    },
                                                ]
                                            }
                                        }
                                    },
                                    'JobDetails': {
                                        'JobRuns': [
                                            {
                                                'Id': 'string',
                                                'Attempt': 123,
                                                'PreviousRunId': 'string',
                                                'TriggerName': 'string',
                                                'JobName': 'string',
                                                'StartedOn': datetime(2015, 1, 1),
                                                'LastModifiedOn': datetime(2015, 1, 1),
                                                'CompletedOn': datetime(2015, 1, 1),
                                                'JobRunState':
                                                'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'
                                                |'FAILED'|'TIMEOUT',
                                                'Arguments': {
                                                    'string': 'string'
                                                },
                                                'ErrorMessage': 'string',
                                                'PredecessorRuns': [
                                                    {
                                                        'JobName': 'string',
                                                        'RunId': 'string'
                                                    },
                                                ],
                                                'AllocatedCapacity': 123,
                                                'ExecutionTime': 123,
                                                'Timeout': 123,
                                                'MaxCapacity': 123.0,
                                                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                                'NumberOfWorkers': 123,
                                                'SecurityConfiguration': 'string',
                                                'LogGroupName': 'string',
                                                'NotificationProperty': {
                                                    'NotifyDelayAfter': 123
                                                },
                                                'GlueVersion': 'string'
                                            },
                                        ]
                                    },
                                    'CrawlerDetails': {
                                        'Crawls': [
                                            {
                                                'State': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                                                'StartedOn': datetime(2015, 1, 1),
                                                'CompletedOn': datetime(2015, 1, 1),
                                                'ErrorMessage': 'string',
                                                'LogGroup': 'string',
                                                'LogStream': 'string'
                                            },
                                        ]
                                    }
                                },
                            ],
                            'Edges': [
                                {
                                    'SourceId': 'string',
                                    'DestinationId': 'string'
                                },
                            ]
                        }
                    },
                    'Graph': {
                        'Nodes': [
                            {
                                'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                                'Name': 'string',
                                'UniqueId': 'string',
                                'TriggerDetails': {
                                    'Trigger': {
                                        'Name': 'string',
                                        'WorkflowName': 'string',
                                        'Id': 'string',
                                        'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                        'State':
                                        'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'
                                        |'DEACTIVATED'|'DELETING'|'UPDATING',
                                        'Description': 'string',
                                        'Schedule': 'string',
                                        'Actions': [
                                            {
                                                'JobName': 'string',
                                                'Arguments': {
                                                    'string': 'string'
                                                },
                                                'Timeout': 123,
                                                'SecurityConfiguration': 'string',
                                                'NotificationProperty': {
                                                    'NotifyDelayAfter': 123
                                                },
                                                'CrawlerName': 'string'
                                            },
                                        ],
                                        'Predicate': {
                                            'Logical': 'AND'|'ANY',
                                            'Conditions': [
                                                {
                                                    'LogicalOperator': 'EQUALS',
                                                    'JobName': 'string',
                                                    'State':
                                                    'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'
                                                    |'FAILED'|'TIMEOUT',
                                                    'CrawlerName': 'string',
                                                    'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                                },
                                            ]
                                        }
                                    }
                                },
                                'JobDetails': {
                                    'JobRuns': [
                                        {
                                            'Id': 'string',
                                            'Attempt': 123,
                                            'PreviousRunId': 'string',
                                            'TriggerName': 'string',
                                            'JobName': 'string',
                                            'StartedOn': datetime(2015, 1, 1),
                                            'LastModifiedOn': datetime(2015, 1, 1),
                                            'CompletedOn': datetime(2015, 1, 1),
                                            'JobRunState':
                                            'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                                            |'TIMEOUT',
                                            'Arguments': {
                                                'string': 'string'
                                            },
                                            'ErrorMessage': 'string',
                                            'PredecessorRuns': [
                                                {
                                                    'JobName': 'string',
                                                    'RunId': 'string'
                                                },
                                            ],
                                            'AllocatedCapacity': 123,
                                            'ExecutionTime': 123,
                                            'Timeout': 123,
                                            'MaxCapacity': 123.0,
                                            'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                            'NumberOfWorkers': 123,
                                            'SecurityConfiguration': 'string',
                                            'LogGroupName': 'string',
                                            'NotificationProperty': {
                                                'NotifyDelayAfter': 123
                                            },
                                            'GlueVersion': 'string'
                                        },
                                    ]
                                },
                                'CrawlerDetails': {
                                    'Crawls': [
                                        {
                                            'State': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                                            'StartedOn': datetime(2015, 1, 1),
                                            'CompletedOn': datetime(2015, 1, 1),
                                            'ErrorMessage': 'string',
                                            'LogGroup': 'string',
                                            'LogStream': 'string'
                                        },
                                    ]
                                }
                            },
                        ],
                        'Edges': [
                            {
                                'SourceId': 'string',
                                'DestinationId': 'string'
                            },
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Workflow** *(dict) --*

              The resource metadata for the workflow.

              - **Name** *(string) --*

                The name of the workflow representing the flow.

              - **Description** *(string) --*

                A description of the workflow.

              - **DefaultRunProperties** *(dict) --*

                A collection of properties to be used as part of each execution of the workflow.

                - *(string) --*

                  - *(string) --*

              - **CreatedOn** *(datetime) --*

                The date and time when the workflow was created.

              - **LastModifiedOn** *(datetime) --*

                The date and time when the workflow was last modified.

              - **LastRun** *(dict) --*

                The information about the last execution of the workflow.

                - **Name** *(string) --*

                  Name of the workflow which was executed.

                - **WorkflowRunId** *(string) --*

                  The ID of this workflow run.

                - **WorkflowRunProperties** *(dict) --*

                  The workflow run properties which were set during the run.

                  - *(string) --*

                    - *(string) --*

                - **StartedOn** *(datetime) --*

                  The date and time when the workflow run was started.

                - **CompletedOn** *(datetime) --*

                  The date and time when the workflow run completed.

                - **Status** *(string) --*

                  The status of the workflow run.

                - **Statistics** *(dict) --*

                  The statistics of the run.

                  - **TotalActions** *(integer) --*

                    Total number of Actions in the workflow run.

                  - **TimeoutActions** *(integer) --*

                    Total number of Actions which timed out.

                  - **FailedActions** *(integer) --*

                    Total number of Actions which have failed.

                  - **StoppedActions** *(integer) --*

                    Total number of Actions which have stopped.

                  - **SucceededActions** *(integer) --*

                    Total number of Actions which have succeeded.

                  - **RunningActions** *(integer) --*

                    Total number Actions in running state.

                - **Graph** *(dict) --*

                  The graph representing all the AWS Glue components that belong to the workflow as nodes
                  and directed connections between them as edges.

                  - **Nodes** *(list) --*

                    A list of the the AWS Glue components belong to the workflow represented as nodes.

                    - *(dict) --*

                      A node represents an AWS Glue component like Trigger, Job etc. which is part of a
                      workflow.

                      - **Type** *(string) --*

                        The type of AWS Glue component represented by the node.

                      - **Name** *(string) --*

                        The name of the AWS Glue component represented by the node.

                      - **UniqueId** *(string) --*

                        The unique Id assigned to the node within the workflow.

                      - **TriggerDetails** *(dict) --*

                        Details of the Trigger when the node represents a Trigger.

                        - **Trigger** *(dict) --*

                          The information of the trigger represented by the trigger node.

                          - **Name** *(string) --*

                            The name of the trigger.

                          - **WorkflowName** *(string) --*

                            The name of the workflow associated with the trigger.

                          - **Id** *(string) --*

                            Reserved for future use.

                          - **Type** *(string) --*

                            The type of trigger that this is.

                          - **State** *(string) --*

                            The current state of the trigger.

                          - **Description** *(string) --*

                            A description of this trigger.

                          - **Schedule** *(string) --*

                            A ``cron`` expression used to specify the schedule (see `Time-Based Schedules
                            for Jobs and Crawlers
                            <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__
                            . For example, to run something every day at 12:15 UTC, you would specify:
                            ``cron(15 12 * * ? *)`` .

                          - **Actions** *(list) --*

                            The actions initiated by this trigger.

                            - *(dict) --*

                              Defines an action to be initiated by a trigger.

                              - **JobName** *(string) --*

                                The name of a job to be executed.

                              - **Arguments** *(dict) --*

                                The job arguments used when this trigger fires. For this job run, they
                                replace the default arguments set in the job definition itself.

                                You can specify arguments here that your own job-execution script consumes,
                                as well as arguments that AWS Glue itself consumes.

                                For information about how to specify and consume your own Job arguments,
                                see the `Calling AWS Glue APIs in Python
                                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                                topic in the developer guide.

                                For information about the key-value pairs that AWS Glue consumes to set up
                                your job, see the `Special Parameters Used by AWS Glue
                                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                                topic in the developer guide.

                                - *(string) --*

                                  - *(string) --*

                              - **Timeout** *(integer) --*

                                The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                                can consume resources before it is terminated and enters ``TIMEOUT``
                                status. The default is 2,880 minutes (48 hours). This overrides the timeout
                                value set in the parent job.

                              - **SecurityConfiguration** *(string) --*

                                The name of the ``SecurityConfiguration`` structure to be used with this
                                action.

                              - **NotificationProperty** *(dict) --*

                                Specifies configuration properties of a job run notification.

                                - **NotifyDelayAfter** *(integer) --*

                                  After a job run starts, the number of minutes to wait before sending a
                                  job run delay notification.

                              - **CrawlerName** *(string) --*

                                The name of the crawler to be used with this action.

                          - **Predicate** *(dict) --*

                            The predicate of this trigger, which defines when it will fire.

                            - **Logical** *(string) --*

                              An optional field if only one condition is listed. If multiple conditions are
                              listed, then this field is required.

                            - **Conditions** *(list) --*

                              A list of the conditions that determine when the trigger will fire.

                              - *(dict) --*

                                Defines a condition under which a trigger fires.

                                - **LogicalOperator** *(string) --*

                                  A logical operator.

                                - **JobName** *(string) --*

                                  The name of the job whose ``JobRuns`` this condition applies to, and on
                                  which this trigger waits.

                                - **State** *(string) --*

                                  The condition state. Currently, the values supported are ``SUCCEEDED`` ,
                                  ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                                - **CrawlerName** *(string) --*

                                  The name of the crawler to which this condition applies.

                                - **CrawlState** *(string) --*

                                  The state of the crawler to which this condition applies.

                      - **JobDetails** *(dict) --*

                        Details of the Job when the node represents a Job.

                        - **JobRuns** *(list) --*

                          The information for the job runs represented by the job node.

                          - *(dict) --*

                            Contains information about a job run.

                            - **Id** *(string) --*

                              The ID of this job run.

                            - **Attempt** *(integer) --*

                              The number of the attempt to run this job.

                            - **PreviousRunId** *(string) --*

                              The ID of the previous run of this job. For example, the ``JobRunId``
                              specified in the ``StartJobRun`` action.

                            - **TriggerName** *(string) --*

                              The name of the trigger that started this job run.

                            - **JobName** *(string) --*

                              The name of the job definition being used in this run.

                            - **StartedOn** *(datetime) --*

                              The date and time at which this job run was started.

                            - **LastModifiedOn** *(datetime) --*

                              The last time that this job run was modified.

                            - **CompletedOn** *(datetime) --*

                              The date and time that this job run completed.

                            - **JobRunState** *(string) --*

                              The current state of the job run.

                            - **Arguments** *(dict) --*

                              The job arguments associated with this run. For this job run, they replace
                              the default arguments set in the job definition itself.

                              You can specify arguments here that your own job-execution script consumes,
                              as well as arguments that AWS Glue itself consumes.

                              For information about how to specify and consume your own job arguments, see
                              the `Calling AWS Glue APIs in Python
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                              topic in the developer guide.

                              For information about the key-value pairs that AWS Glue consumes to set up
                              your job, see the `Special Parameters Used by AWS Glue
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                              topic in the developer guide.

                              - *(string) --*

                                - *(string) --*

                            - **ErrorMessage** *(string) --*

                              An error message associated with this job run.

                            - **PredecessorRuns** *(list) --*

                              A list of predecessors to this job run.

                              - *(dict) --*

                                A job run that was used in the predicate of a conditional trigger that
                                triggered this job run.

                                - **JobName** *(string) --*

                                  The name of the job definition used by the predecessor job run.

                                - **RunId** *(string) --*

                                  The job-run ID of the predecessor job run.

                            - **AllocatedCapacity** *(integer) --*

                              This field is deprecated. Use ``MaxCapacity`` instead.

                              The number of AWS Glue data processing units (DPUs) allocated to this JobRun.
                              From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative
                              measure of processing power that consists of 4 vCPUs of compute capacity and
                              16 GB of memory. For more information, see the `AWS Glue pricing page
                              <https://aws.amazon.com/glue/pricing/>`__ .

                            - **ExecutionTime** *(integer) --*

                              The amount of time (in seconds) that the job run consumed resources.

                            - **Timeout** *(integer) --*

                              The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                              can consume resources before it is terminated and enters ``TIMEOUT`` status.
                              The default is 2,880 minutes (48 hours). This overrides the timeout value set
                              in the parent job.

                            - **MaxCapacity** *(float) --*

                              The number of AWS Glue data processing units (DPUs) that can be allocated
                              when this job runs. A DPU is a relative measure of processing power that
                              consists of 4 vCPUs of compute capacity and 16 GB of memory. For more
                              information, see the `AWS Glue pricing page
                              <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                              Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                              The value that can be allocated for ``MaxCapacity`` depends on whether you
                              are running a Python shell job or an Apache Spark ETL job:

                              * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"),
                              you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                              * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"),
                              you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type
                              cannot have a fractional DPU allocation.

                            - **WorkerType** *(string) --*

                              The type of predefined worker that is allocated when a job runs. Accepts a
                              value of Standard, G.1X, or G.2X.

                              * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of
                              memory and a 50GB disk, and 2 executors per worker.

                              * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory
                              and a 64GB disk, and 1 executor per worker.

                              * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory
                              and a 128GB disk, and 1 executor per worker.

                            - **NumberOfWorkers** *(integer) --*

                              The number of workers of a defined ``workerType`` that are allocated when a
                              job runs.

                              The maximum number of workers you can define are 299 for ``G.1X`` , and 149
                              for ``G.2X`` .

                            - **SecurityConfiguration** *(string) --*

                              The name of the ``SecurityConfiguration`` structure to be used with this job
                              run.

                            - **LogGroupName** *(string) --*

                              The name of the log group for secure logging that can be server-side
                              encrypted in Amazon CloudWatch using AWS KMS. This name can be
                              ``/aws-glue/jobs/`` , in which case the default encryption is ``NONE`` . If
                              you add a role name and ``SecurityConfiguration`` name (in other words,
                              ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that
                              security configuration is used to encrypt the log group.

                            - **NotificationProperty** *(dict) --*

                              Specifies configuration properties of a job run notification.

                              - **NotifyDelayAfter** *(integer) --*

                                After a job run starts, the number of minutes to wait before sending a job
                                run delay notification.

                            - **GlueVersion** *(string) --*

                              Glue version determines the versions of Apache Spark and Python that AWS Glue
                              supports. The Python version indicates the version supported for jobs of type
                              Spark.

                              For more information about the available AWS Glue versions and corresponding
                              Spark and Python versions, see `Glue version
                              <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer
                              guide.

                              Jobs that are created without specifying a Glue version default to Glue 0.9.

                      - **CrawlerDetails** *(dict) --*

                        Details of the crawler when the node represents a crawler.

                        - **Crawls** *(list) --*

                          A list of crawls represented by the crawl node.

                          - *(dict) --*

                            The details of a crawl in the workflow.

                            - **State** *(string) --*

                              The state of the crawler.

                            - **StartedOn** *(datetime) --*

                              The date and time on which the crawl started.

                            - **CompletedOn** *(datetime) --*

                              The date and time on which the crawl completed.

                            - **ErrorMessage** *(string) --*

                              The error message associated with the crawl.

                            - **LogGroup** *(string) --*

                              The log group associated with the crawl.

                            - **LogStream** *(string) --*

                              The log stream associated with the crawl.

                  - **Edges** *(list) --*

                    A list of all the directed connections between the nodes belonging to the workflow.

                    - *(dict) --*

                      An edge represents a directed connection between two AWS Glue components which are
                      part of the workflow the edge belongs to.

                      - **SourceId** *(string) --*

                        The unique of the node within the workflow where the edge starts.

                      - **DestinationId** *(string) --*

                        The unique of the node within the workflow where the edge ends.

              - **Graph** *(dict) --*

                The graph representing all the AWS Glue components that belong to the workflow as nodes and
                directed connections between them as edges.

                - **Nodes** *(list) --*

                  A list of the the AWS Glue components belong to the workflow represented as nodes.

                  - *(dict) --*

                    A node represents an AWS Glue component like Trigger, Job etc. which is part of a
                    workflow.

                    - **Type** *(string) --*

                      The type of AWS Glue component represented by the node.

                    - **Name** *(string) --*

                      The name of the AWS Glue component represented by the node.

                    - **UniqueId** *(string) --*

                      The unique Id assigned to the node within the workflow.

                    - **TriggerDetails** *(dict) --*

                      Details of the Trigger when the node represents a Trigger.

                      - **Trigger** *(dict) --*

                        The information of the trigger represented by the trigger node.

                        - **Name** *(string) --*

                          The name of the trigger.

                        - **WorkflowName** *(string) --*

                          The name of the workflow associated with the trigger.

                        - **Id** *(string) --*

                          Reserved for future use.

                        - **Type** *(string) --*

                          The type of trigger that this is.

                        - **State** *(string) --*

                          The current state of the trigger.

                        - **Description** *(string) --*

                          A description of this trigger.

                        - **Schedule** *(string) --*

                          A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for
                          Jobs and Crawlers
                          <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__
                          . For example, to run something every day at 12:15 UTC, you would specify:
                          ``cron(15 12 * * ? *)`` .

                        - **Actions** *(list) --*

                          The actions initiated by this trigger.

                          - *(dict) --*

                            Defines an action to be initiated by a trigger.

                            - **JobName** *(string) --*

                              The name of a job to be executed.

                            - **Arguments** *(dict) --*

                              The job arguments used when this trigger fires. For this job run, they
                              replace the default arguments set in the job definition itself.

                              You can specify arguments here that your own job-execution script consumes,
                              as well as arguments that AWS Glue itself consumes.

                              For information about how to specify and consume your own Job arguments, see
                              the `Calling AWS Glue APIs in Python
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                              topic in the developer guide.

                              For information about the key-value pairs that AWS Glue consumes to set up
                              your job, see the `Special Parameters Used by AWS Glue
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                              topic in the developer guide.

                              - *(string) --*

                                - *(string) --*

                            - **Timeout** *(integer) --*

                              The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                              can consume resources before it is terminated and enters ``TIMEOUT`` status.
                              The default is 2,880 minutes (48 hours). This overrides the timeout value set
                              in the parent job.

                            - **SecurityConfiguration** *(string) --*

                              The name of the ``SecurityConfiguration`` structure to be used with this
                              action.

                            - **NotificationProperty** *(dict) --*

                              Specifies configuration properties of a job run notification.

                              - **NotifyDelayAfter** *(integer) --*

                                After a job run starts, the number of minutes to wait before sending a job
                                run delay notification.

                            - **CrawlerName** *(string) --*

                              The name of the crawler to be used with this action.

                        - **Predicate** *(dict) --*

                          The predicate of this trigger, which defines when it will fire.

                          - **Logical** *(string) --*

                            An optional field if only one condition is listed. If multiple conditions are
                            listed, then this field is required.

                          - **Conditions** *(list) --*

                            A list of the conditions that determine when the trigger will fire.

                            - *(dict) --*

                              Defines a condition under which a trigger fires.

                              - **LogicalOperator** *(string) --*

                                A logical operator.

                              - **JobName** *(string) --*

                                The name of the job whose ``JobRuns`` this condition applies to, and on
                                which this trigger waits.

                              - **State** *(string) --*

                                The condition state. Currently, the values supported are ``SUCCEEDED`` ,
                                ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                              - **CrawlerName** *(string) --*

                                The name of the crawler to which this condition applies.

                              - **CrawlState** *(string) --*

                                The state of the crawler to which this condition applies.

                    - **JobDetails** *(dict) --*

                      Details of the Job when the node represents a Job.

                      - **JobRuns** *(list) --*

                        The information for the job runs represented by the job node.

                        - *(dict) --*

                          Contains information about a job run.

                          - **Id** *(string) --*

                            The ID of this job run.

                          - **Attempt** *(integer) --*

                            The number of the attempt to run this job.

                          - **PreviousRunId** *(string) --*

                            The ID of the previous run of this job. For example, the ``JobRunId`` specified
                            in the ``StartJobRun`` action.

                          - **TriggerName** *(string) --*

                            The name of the trigger that started this job run.

                          - **JobName** *(string) --*

                            The name of the job definition being used in this run.

                          - **StartedOn** *(datetime) --*

                            The date and time at which this job run was started.

                          - **LastModifiedOn** *(datetime) --*

                            The last time that this job run was modified.

                          - **CompletedOn** *(datetime) --*

                            The date and time that this job run completed.

                          - **JobRunState** *(string) --*

                            The current state of the job run.

                          - **Arguments** *(dict) --*

                            The job arguments associated with this run. For this job run, they replace the
                            default arguments set in the job definition itself.

                            You can specify arguments here that your own job-execution script consumes, as
                            well as arguments that AWS Glue itself consumes.

                            For information about how to specify and consume your own job arguments, see
                            the `Calling AWS Glue APIs in Python
                            <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                            topic in the developer guide.

                            For information about the key-value pairs that AWS Glue consumes to set up your
                            job, see the `Special Parameters Used by AWS Glue
                            <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                            topic in the developer guide.

                            - *(string) --*

                              - *(string) --*

                          - **ErrorMessage** *(string) --*

                            An error message associated with this job run.

                          - **PredecessorRuns** *(list) --*

                            A list of predecessors to this job run.

                            - *(dict) --*

                              A job run that was used in the predicate of a conditional trigger that
                              triggered this job run.

                              - **JobName** *(string) --*

                                The name of the job definition used by the predecessor job run.

                              - **RunId** *(string) --*

                                The job-run ID of the predecessor job run.

                          - **AllocatedCapacity** *(integer) --*

                            This field is deprecated. Use ``MaxCapacity`` instead.

                            The number of AWS Glue data processing units (DPUs) allocated to this JobRun.
                            From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative
                            measure of processing power that consists of 4 vCPUs of compute capacity and 16
                            GB of memory. For more information, see the `AWS Glue pricing page
                            <https://aws.amazon.com/glue/pricing/>`__ .

                          - **ExecutionTime** *(integer) --*

                            The amount of time (in seconds) that the job run consumed resources.

                          - **Timeout** *(integer) --*

                            The ``JobRun`` timeout in minutes. This is the maximum time that a job run can
                            consume resources before it is terminated and enters ``TIMEOUT`` status. The
                            default is 2,880 minutes (48 hours). This overrides the timeout value set in
                            the parent job.

                          - **MaxCapacity** *(float) --*

                            The number of AWS Glue data processing units (DPUs) that can be allocated when
                            this job runs. A DPU is a relative measure of processing power that consists of
                            4 vCPUs of compute capacity and 16 GB of memory. For more information, see the
                            `AWS Glue pricing page
                            <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                            Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                            The value that can be allocated for ``MaxCapacity`` depends on whether you are
                            running a Python shell job or an Apache Spark ETL job:

                            * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you
                            can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                            * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"),
                            you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type
                            cannot have a fractional DPU allocation.

                          - **WorkerType** *(string) --*

                            The type of predefined worker that is allocated when a job runs. Accepts a
                            value of Standard, G.1X, or G.2X.

                            * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of
                            memory and a 50GB disk, and 2 executors per worker.

                            * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory
                            and a 64GB disk, and 1 executor per worker.

                            * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory
                            and a 128GB disk, and 1 executor per worker.

                          - **NumberOfWorkers** *(integer) --*

                            The number of workers of a defined ``workerType`` that are allocated when a job
                            runs.

                            The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for
                            ``G.2X`` .

                          - **SecurityConfiguration** *(string) --*

                            The name of the ``SecurityConfiguration`` structure to be used with this job
                            run.

                          - **LogGroupName** *(string) --*

                            The name of the log group for secure logging that can be server-side encrypted
                            in Amazon CloudWatch using AWS KMS. This name can be ``/aws-glue/jobs/`` , in
                            which case the default encryption is ``NONE`` . If you add a role name and
                            ``SecurityConfiguration`` name (in other words,
                            ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that
                            security configuration is used to encrypt the log group.

                          - **NotificationProperty** *(dict) --*

                            Specifies configuration properties of a job run notification.

                            - **NotifyDelayAfter** *(integer) --*

                              After a job run starts, the number of minutes to wait before sending a job
                              run delay notification.

                          - **GlueVersion** *(string) --*

                            Glue version determines the versions of Apache Spark and Python that AWS Glue
                            supports. The Python version indicates the version supported for jobs of type
                            Spark.

                            For more information about the available AWS Glue versions and corresponding
                            Spark and Python versions, see `Glue version
                            <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer
                            guide.

                            Jobs that are created without specifying a Glue version default to Glue 0.9.

                    - **CrawlerDetails** *(dict) --*

                      Details of the crawler when the node represents a crawler.

                      - **Crawls** *(list) --*

                        A list of crawls represented by the crawl node.

                        - *(dict) --*

                          The details of a crawl in the workflow.

                          - **State** *(string) --*

                            The state of the crawler.

                          - **StartedOn** *(datetime) --*

                            The date and time on which the crawl started.

                          - **CompletedOn** *(datetime) --*

                            The date and time on which the crawl completed.

                          - **ErrorMessage** *(string) --*

                            The error message associated with the crawl.

                          - **LogGroup** *(string) --*

                            The log group associated with the crawl.

                          - **LogStream** *(string) --*

                            The log stream associated with the crawl.

                - **Edges** *(list) --*

                  A list of all the directed connections between the nodes belonging to the workflow.

                  - *(dict) --*

                    An edge represents a directed connection between two AWS Glue components which are part
                    of the workflow the edge belongs to.

                    - **SourceId** *(string) --*

                      The unique of the node within the workflow where the edge starts.

                    - **DestinationId** *(string) --*

                      The unique of the node within the workflow where the edge ends.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_workflow_run(
        self, Name: str, RunId: str, IncludeGraph: bool = None
    ) -> ClientGetWorkflowRunResponseTypeDef:
        """
        Retrieves the metadata for a given workflow run.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetWorkflowRun>`_

        **Request Syntax**
        ::

          response = client.get_workflow_run(
              Name='string',
              RunId='string',
              IncludeGraph=True|False
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the workflow being run.

        :type RunId: string
        :param RunId: **[REQUIRED]**

          The ID of the workflow run.

        :type IncludeGraph: boolean
        :param IncludeGraph:

          Specifies whether to include the workflow graph in response or not.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Run': {
                    'Name': 'string',
                    'WorkflowRunId': 'string',
                    'WorkflowRunProperties': {
                        'string': 'string'
                    },
                    'StartedOn': datetime(2015, 1, 1),
                    'CompletedOn': datetime(2015, 1, 1),
                    'Status': 'RUNNING'|'COMPLETED',
                    'Statistics': {
                        'TotalActions': 123,
                        'TimeoutActions': 123,
                        'FailedActions': 123,
                        'StoppedActions': 123,
                        'SucceededActions': 123,
                        'RunningActions': 123
                    },
                    'Graph': {
                        'Nodes': [
                            {
                                'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                                'Name': 'string',
                                'UniqueId': 'string',
                                'TriggerDetails': {
                                    'Trigger': {
                                        'Name': 'string',
                                        'WorkflowName': 'string',
                                        'Id': 'string',
                                        'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                        'State':
                                        'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'
                                        |'DEACTIVATED'|'DELETING'|'UPDATING',
                                        'Description': 'string',
                                        'Schedule': 'string',
                                        'Actions': [
                                            {
                                                'JobName': 'string',
                                                'Arguments': {
                                                    'string': 'string'
                                                },
                                                'Timeout': 123,
                                                'SecurityConfiguration': 'string',
                                                'NotificationProperty': {
                                                    'NotifyDelayAfter': 123
                                                },
                                                'CrawlerName': 'string'
                                            },
                                        ],
                                        'Predicate': {
                                            'Logical': 'AND'|'ANY',
                                            'Conditions': [
                                                {
                                                    'LogicalOperator': 'EQUALS',
                                                    'JobName': 'string',
                                                    'State':
                                                    'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'
                                                    |'FAILED'|'TIMEOUT',
                                                    'CrawlerName': 'string',
                                                    'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                                },
                                            ]
                                        }
                                    }
                                },
                                'JobDetails': {
                                    'JobRuns': [
                                        {
                                            'Id': 'string',
                                            'Attempt': 123,
                                            'PreviousRunId': 'string',
                                            'TriggerName': 'string',
                                            'JobName': 'string',
                                            'StartedOn': datetime(2015, 1, 1),
                                            'LastModifiedOn': datetime(2015, 1, 1),
                                            'CompletedOn': datetime(2015, 1, 1),
                                            'JobRunState':
                                            'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                                            |'TIMEOUT',
                                            'Arguments': {
                                                'string': 'string'
                                            },
                                            'ErrorMessage': 'string',
                                            'PredecessorRuns': [
                                                {
                                                    'JobName': 'string',
                                                    'RunId': 'string'
                                                },
                                            ],
                                            'AllocatedCapacity': 123,
                                            'ExecutionTime': 123,
                                            'Timeout': 123,
                                            'MaxCapacity': 123.0,
                                            'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                            'NumberOfWorkers': 123,
                                            'SecurityConfiguration': 'string',
                                            'LogGroupName': 'string',
                                            'NotificationProperty': {
                                                'NotifyDelayAfter': 123
                                            },
                                            'GlueVersion': 'string'
                                        },
                                    ]
                                },
                                'CrawlerDetails': {
                                    'Crawls': [
                                        {
                                            'State': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                                            'StartedOn': datetime(2015, 1, 1),
                                            'CompletedOn': datetime(2015, 1, 1),
                                            'ErrorMessage': 'string',
                                            'LogGroup': 'string',
                                            'LogStream': 'string'
                                        },
                                    ]
                                }
                            },
                        ],
                        'Edges': [
                            {
                                'SourceId': 'string',
                                'DestinationId': 'string'
                            },
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Run** *(dict) --*

              The requested workflow run metadata.

              - **Name** *(string) --*

                Name of the workflow which was executed.

              - **WorkflowRunId** *(string) --*

                The ID of this workflow run.

              - **WorkflowRunProperties** *(dict) --*

                The workflow run properties which were set during the run.

                - *(string) --*

                  - *(string) --*

              - **StartedOn** *(datetime) --*

                The date and time when the workflow run was started.

              - **CompletedOn** *(datetime) --*

                The date and time when the workflow run completed.

              - **Status** *(string) --*

                The status of the workflow run.

              - **Statistics** *(dict) --*

                The statistics of the run.

                - **TotalActions** *(integer) --*

                  Total number of Actions in the workflow run.

                - **TimeoutActions** *(integer) --*

                  Total number of Actions which timed out.

                - **FailedActions** *(integer) --*

                  Total number of Actions which have failed.

                - **StoppedActions** *(integer) --*

                  Total number of Actions which have stopped.

                - **SucceededActions** *(integer) --*

                  Total number of Actions which have succeeded.

                - **RunningActions** *(integer) --*

                  Total number Actions in running state.

              - **Graph** *(dict) --*

                The graph representing all the AWS Glue components that belong to the workflow as nodes and
                directed connections between them as edges.

                - **Nodes** *(list) --*

                  A list of the the AWS Glue components belong to the workflow represented as nodes.

                  - *(dict) --*

                    A node represents an AWS Glue component like Trigger, Job etc. which is part of a
                    workflow.

                    - **Type** *(string) --*

                      The type of AWS Glue component represented by the node.

                    - **Name** *(string) --*

                      The name of the AWS Glue component represented by the node.

                    - **UniqueId** *(string) --*

                      The unique Id assigned to the node within the workflow.

                    - **TriggerDetails** *(dict) --*

                      Details of the Trigger when the node represents a Trigger.

                      - **Trigger** *(dict) --*

                        The information of the trigger represented by the trigger node.

                        - **Name** *(string) --*

                          The name of the trigger.

                        - **WorkflowName** *(string) --*

                          The name of the workflow associated with the trigger.

                        - **Id** *(string) --*

                          Reserved for future use.

                        - **Type** *(string) --*

                          The type of trigger that this is.

                        - **State** *(string) --*

                          The current state of the trigger.

                        - **Description** *(string) --*

                          A description of this trigger.

                        - **Schedule** *(string) --*

                          A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for
                          Jobs and Crawlers
                          <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__
                          . For example, to run something every day at 12:15 UTC, you would specify:
                          ``cron(15 12 * * ? *)`` .

                        - **Actions** *(list) --*

                          The actions initiated by this trigger.

                          - *(dict) --*

                            Defines an action to be initiated by a trigger.

                            - **JobName** *(string) --*

                              The name of a job to be executed.

                            - **Arguments** *(dict) --*

                              The job arguments used when this trigger fires. For this job run, they
                              replace the default arguments set in the job definition itself.

                              You can specify arguments here that your own job-execution script consumes,
                              as well as arguments that AWS Glue itself consumes.

                              For information about how to specify and consume your own Job arguments, see
                              the `Calling AWS Glue APIs in Python
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                              topic in the developer guide.

                              For information about the key-value pairs that AWS Glue consumes to set up
                              your job, see the `Special Parameters Used by AWS Glue
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                              topic in the developer guide.

                              - *(string) --*

                                - *(string) --*

                            - **Timeout** *(integer) --*

                              The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                              can consume resources before it is terminated and enters ``TIMEOUT`` status.
                              The default is 2,880 minutes (48 hours). This overrides the timeout value set
                              in the parent job.

                            - **SecurityConfiguration** *(string) --*

                              The name of the ``SecurityConfiguration`` structure to be used with this
                              action.

                            - **NotificationProperty** *(dict) --*

                              Specifies configuration properties of a job run notification.

                              - **NotifyDelayAfter** *(integer) --*

                                After a job run starts, the number of minutes to wait before sending a job
                                run delay notification.

                            - **CrawlerName** *(string) --*

                              The name of the crawler to be used with this action.

                        - **Predicate** *(dict) --*

                          The predicate of this trigger, which defines when it will fire.

                          - **Logical** *(string) --*

                            An optional field if only one condition is listed. If multiple conditions are
                            listed, then this field is required.

                          - **Conditions** *(list) --*

                            A list of the conditions that determine when the trigger will fire.

                            - *(dict) --*

                              Defines a condition under which a trigger fires.

                              - **LogicalOperator** *(string) --*

                                A logical operator.

                              - **JobName** *(string) --*

                                The name of the job whose ``JobRuns`` this condition applies to, and on
                                which this trigger waits.

                              - **State** *(string) --*

                                The condition state. Currently, the values supported are ``SUCCEEDED`` ,
                                ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                              - **CrawlerName** *(string) --*

                                The name of the crawler to which this condition applies.

                              - **CrawlState** *(string) --*

                                The state of the crawler to which this condition applies.

                    - **JobDetails** *(dict) --*

                      Details of the Job when the node represents a Job.

                      - **JobRuns** *(list) --*

                        The information for the job runs represented by the job node.

                        - *(dict) --*

                          Contains information about a job run.

                          - **Id** *(string) --*

                            The ID of this job run.

                          - **Attempt** *(integer) --*

                            The number of the attempt to run this job.

                          - **PreviousRunId** *(string) --*

                            The ID of the previous run of this job. For example, the ``JobRunId`` specified
                            in the ``StartJobRun`` action.

                          - **TriggerName** *(string) --*

                            The name of the trigger that started this job run.

                          - **JobName** *(string) --*

                            The name of the job definition being used in this run.

                          - **StartedOn** *(datetime) --*

                            The date and time at which this job run was started.

                          - **LastModifiedOn** *(datetime) --*

                            The last time that this job run was modified.

                          - **CompletedOn** *(datetime) --*

                            The date and time that this job run completed.

                          - **JobRunState** *(string) --*

                            The current state of the job run.

                          - **Arguments** *(dict) --*

                            The job arguments associated with this run. For this job run, they replace the
                            default arguments set in the job definition itself.

                            You can specify arguments here that your own job-execution script consumes, as
                            well as arguments that AWS Glue itself consumes.

                            For information about how to specify and consume your own job arguments, see
                            the `Calling AWS Glue APIs in Python
                            <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                            topic in the developer guide.

                            For information about the key-value pairs that AWS Glue consumes to set up your
                            job, see the `Special Parameters Used by AWS Glue
                            <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                            topic in the developer guide.

                            - *(string) --*

                              - *(string) --*

                          - **ErrorMessage** *(string) --*

                            An error message associated with this job run.

                          - **PredecessorRuns** *(list) --*

                            A list of predecessors to this job run.

                            - *(dict) --*

                              A job run that was used in the predicate of a conditional trigger that
                              triggered this job run.

                              - **JobName** *(string) --*

                                The name of the job definition used by the predecessor job run.

                              - **RunId** *(string) --*

                                The job-run ID of the predecessor job run.

                          - **AllocatedCapacity** *(integer) --*

                            This field is deprecated. Use ``MaxCapacity`` instead.

                            The number of AWS Glue data processing units (DPUs) allocated to this JobRun.
                            From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative
                            measure of processing power that consists of 4 vCPUs of compute capacity and 16
                            GB of memory. For more information, see the `AWS Glue pricing page
                            <https://aws.amazon.com/glue/pricing/>`__ .

                          - **ExecutionTime** *(integer) --*

                            The amount of time (in seconds) that the job run consumed resources.

                          - **Timeout** *(integer) --*

                            The ``JobRun`` timeout in minutes. This is the maximum time that a job run can
                            consume resources before it is terminated and enters ``TIMEOUT`` status. The
                            default is 2,880 minutes (48 hours). This overrides the timeout value set in
                            the parent job.

                          - **MaxCapacity** *(float) --*

                            The number of AWS Glue data processing units (DPUs) that can be allocated when
                            this job runs. A DPU is a relative measure of processing power that consists of
                            4 vCPUs of compute capacity and 16 GB of memory. For more information, see the
                            `AWS Glue pricing page
                            <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                            Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                            The value that can be allocated for ``MaxCapacity`` depends on whether you are
                            running a Python shell job or an Apache Spark ETL job:

                            * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you
                            can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                            * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"),
                            you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type
                            cannot have a fractional DPU allocation.

                          - **WorkerType** *(string) --*

                            The type of predefined worker that is allocated when a job runs. Accepts a
                            value of Standard, G.1X, or G.2X.

                            * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of
                            memory and a 50GB disk, and 2 executors per worker.

                            * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory
                            and a 64GB disk, and 1 executor per worker.

                            * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory
                            and a 128GB disk, and 1 executor per worker.

                          - **NumberOfWorkers** *(integer) --*

                            The number of workers of a defined ``workerType`` that are allocated when a job
                            runs.

                            The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for
                            ``G.2X`` .

                          - **SecurityConfiguration** *(string) --*

                            The name of the ``SecurityConfiguration`` structure to be used with this job
                            run.

                          - **LogGroupName** *(string) --*

                            The name of the log group for secure logging that can be server-side encrypted
                            in Amazon CloudWatch using AWS KMS. This name can be ``/aws-glue/jobs/`` , in
                            which case the default encryption is ``NONE`` . If you add a role name and
                            ``SecurityConfiguration`` name (in other words,
                            ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that
                            security configuration is used to encrypt the log group.

                          - **NotificationProperty** *(dict) --*

                            Specifies configuration properties of a job run notification.

                            - **NotifyDelayAfter** *(integer) --*

                              After a job run starts, the number of minutes to wait before sending a job
                              run delay notification.

                          - **GlueVersion** *(string) --*

                            Glue version determines the versions of Apache Spark and Python that AWS Glue
                            supports. The Python version indicates the version supported for jobs of type
                            Spark.

                            For more information about the available AWS Glue versions and corresponding
                            Spark and Python versions, see `Glue version
                            <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer
                            guide.

                            Jobs that are created without specifying a Glue version default to Glue 0.9.

                    - **CrawlerDetails** *(dict) --*

                      Details of the crawler when the node represents a crawler.

                      - **Crawls** *(list) --*

                        A list of crawls represented by the crawl node.

                        - *(dict) --*

                          The details of a crawl in the workflow.

                          - **State** *(string) --*

                            The state of the crawler.

                          - **StartedOn** *(datetime) --*

                            The date and time on which the crawl started.

                          - **CompletedOn** *(datetime) --*

                            The date and time on which the crawl completed.

                          - **ErrorMessage** *(string) --*

                            The error message associated with the crawl.

                          - **LogGroup** *(string) --*

                            The log group associated with the crawl.

                          - **LogStream** *(string) --*

                            The log stream associated with the crawl.

                - **Edges** *(list) --*

                  A list of all the directed connections between the nodes belonging to the workflow.

                  - *(dict) --*

                    An edge represents a directed connection between two AWS Glue components which are part
                    of the workflow the edge belongs to.

                    - **SourceId** *(string) --*

                      The unique of the node within the workflow where the edge starts.

                    - **DestinationId** *(string) --*

                      The unique of the node within the workflow where the edge ends.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_workflow_run_properties(
        self, Name: str, RunId: str
    ) -> ClientGetWorkflowRunPropertiesResponseTypeDef:
        """
        Retrieves the workflow run properties which were set during the run.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetWorkflowRunProperties>`_

        **Request Syntax**
        ::

          response = client.get_workflow_run_properties(
              Name='string',
              RunId='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the workflow which was run.

        :type RunId: string
        :param RunId: **[REQUIRED]**

          The ID of the workflow run whose run properties should be returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RunProperties': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **RunProperties** *(dict) --*

              The workflow run properties which were set during the specified run.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_workflow_runs(
        self,
        Name: str,
        IncludeGraph: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetWorkflowRunsResponseTypeDef:
        """
        Retrieves metadata for all runs of a given workflow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetWorkflowRuns>`_

        **Request Syntax**
        ::

          response = client.get_workflow_runs(
              Name='string',
              IncludeGraph=True|False,
              NextToken='string',
              MaxResults=123
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the workflow whose metadata of runs should be returned.

        :type IncludeGraph: boolean
        :param IncludeGraph:

          Specifies whether to include the workflow graph in response or not.

        :type NextToken: string
        :param NextToken:

          The maximum size of the response.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of workflow runs to be included in the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Runs': [
                    {
                        'Name': 'string',
                        'WorkflowRunId': 'string',
                        'WorkflowRunProperties': {
                            'string': 'string'
                        },
                        'StartedOn': datetime(2015, 1, 1),
                        'CompletedOn': datetime(2015, 1, 1),
                        'Status': 'RUNNING'|'COMPLETED',
                        'Statistics': {
                            'TotalActions': 123,
                            'TimeoutActions': 123,
                            'FailedActions': 123,
                            'StoppedActions': 123,
                            'SucceededActions': 123,
                            'RunningActions': 123
                        },
                        'Graph': {
                            'Nodes': [
                                {
                                    'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                                    'Name': 'string',
                                    'UniqueId': 'string',
                                    'TriggerDetails': {
                                        'Trigger': {
                                            'Name': 'string',
                                            'WorkflowName': 'string',
                                            'Id': 'string',
                                            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                            'State':
                                            'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'
                                            |'DEACTIVATED'|'DELETING'|'UPDATING',
                                            'Description': 'string',
                                            'Schedule': 'string',
                                            'Actions': [
                                                {
                                                    'JobName': 'string',
                                                    'Arguments': {
                                                        'string': 'string'
                                                    },
                                                    'Timeout': 123,
                                                    'SecurityConfiguration': 'string',
                                                    'NotificationProperty': {
                                                        'NotifyDelayAfter': 123
                                                    },
                                                    'CrawlerName': 'string'
                                                },
                                            ],
                                            'Predicate': {
                                                'Logical': 'AND'|'ANY',
                                                'Conditions': [
                                                    {
                                                        'LogicalOperator': 'EQUALS',
                                                        'JobName': 'string',
                                                        'State':
                                                        'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'
                                                        |'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                        'CrawlerName': 'string',
                                                        'CrawlState':
                                                        'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                                    },
                                                ]
                                            }
                                        }
                                    },
                                    'JobDetails': {
                                        'JobRuns': [
                                            {
                                                'Id': 'string',
                                                'Attempt': 123,
                                                'PreviousRunId': 'string',
                                                'TriggerName': 'string',
                                                'JobName': 'string',
                                                'StartedOn': datetime(2015, 1, 1),
                                                'LastModifiedOn': datetime(2015, 1, 1),
                                                'CompletedOn': datetime(2015, 1, 1),
                                                'JobRunState':
                                                'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'
                                                |'FAILED'|'TIMEOUT',
                                                'Arguments': {
                                                    'string': 'string'
                                                },
                                                'ErrorMessage': 'string',
                                                'PredecessorRuns': [
                                                    {
                                                        'JobName': 'string',
                                                        'RunId': 'string'
                                                    },
                                                ],
                                                'AllocatedCapacity': 123,
                                                'ExecutionTime': 123,
                                                'Timeout': 123,
                                                'MaxCapacity': 123.0,
                                                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                                'NumberOfWorkers': 123,
                                                'SecurityConfiguration': 'string',
                                                'LogGroupName': 'string',
                                                'NotificationProperty': {
                                                    'NotifyDelayAfter': 123
                                                },
                                                'GlueVersion': 'string'
                                            },
                                        ]
                                    },
                                    'CrawlerDetails': {
                                        'Crawls': [
                                            {
                                                'State': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                                                'StartedOn': datetime(2015, 1, 1),
                                                'CompletedOn': datetime(2015, 1, 1),
                                                'ErrorMessage': 'string',
                                                'LogGroup': 'string',
                                                'LogStream': 'string'
                                            },
                                        ]
                                    }
                                },
                            ],
                            'Edges': [
                                {
                                    'SourceId': 'string',
                                    'DestinationId': 'string'
                                },
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Runs** *(list) --*

              A list of workflow run metadata objects.

              - *(dict) --*

                A workflow run is an execution of a workflow providing all the runtime information.

                - **Name** *(string) --*

                  Name of the workflow which was executed.

                - **WorkflowRunId** *(string) --*

                  The ID of this workflow run.

                - **WorkflowRunProperties** *(dict) --*

                  The workflow run properties which were set during the run.

                  - *(string) --*

                    - *(string) --*

                - **StartedOn** *(datetime) --*

                  The date and time when the workflow run was started.

                - **CompletedOn** *(datetime) --*

                  The date and time when the workflow run completed.

                - **Status** *(string) --*

                  The status of the workflow run.

                - **Statistics** *(dict) --*

                  The statistics of the run.

                  - **TotalActions** *(integer) --*

                    Total number of Actions in the workflow run.

                  - **TimeoutActions** *(integer) --*

                    Total number of Actions which timed out.

                  - **FailedActions** *(integer) --*

                    Total number of Actions which have failed.

                  - **StoppedActions** *(integer) --*

                    Total number of Actions which have stopped.

                  - **SucceededActions** *(integer) --*

                    Total number of Actions which have succeeded.

                  - **RunningActions** *(integer) --*

                    Total number Actions in running state.

                - **Graph** *(dict) --*

                  The graph representing all the AWS Glue components that belong to the workflow as nodes
                  and directed connections between them as edges.

                  - **Nodes** *(list) --*

                    A list of the the AWS Glue components belong to the workflow represented as nodes.

                    - *(dict) --*

                      A node represents an AWS Glue component like Trigger, Job etc. which is part of a
                      workflow.

                      - **Type** *(string) --*

                        The type of AWS Glue component represented by the node.

                      - **Name** *(string) --*

                        The name of the AWS Glue component represented by the node.

                      - **UniqueId** *(string) --*

                        The unique Id assigned to the node within the workflow.

                      - **TriggerDetails** *(dict) --*

                        Details of the Trigger when the node represents a Trigger.

                        - **Trigger** *(dict) --*

                          The information of the trigger represented by the trigger node.

                          - **Name** *(string) --*

                            The name of the trigger.

                          - **WorkflowName** *(string) --*

                            The name of the workflow associated with the trigger.

                          - **Id** *(string) --*

                            Reserved for future use.

                          - **Type** *(string) --*

                            The type of trigger that this is.

                          - **State** *(string) --*

                            The current state of the trigger.

                          - **Description** *(string) --*

                            A description of this trigger.

                          - **Schedule** *(string) --*

                            A ``cron`` expression used to specify the schedule (see `Time-Based Schedules
                            for Jobs and Crawlers
                            <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__
                            . For example, to run something every day at 12:15 UTC, you would specify:
                            ``cron(15 12 * * ? *)`` .

                          - **Actions** *(list) --*

                            The actions initiated by this trigger.

                            - *(dict) --*

                              Defines an action to be initiated by a trigger.

                              - **JobName** *(string) --*

                                The name of a job to be executed.

                              - **Arguments** *(dict) --*

                                The job arguments used when this trigger fires. For this job run, they
                                replace the default arguments set in the job definition itself.

                                You can specify arguments here that your own job-execution script consumes,
                                as well as arguments that AWS Glue itself consumes.

                                For information about how to specify and consume your own Job arguments,
                                see the `Calling AWS Glue APIs in Python
                                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                                topic in the developer guide.

                                For information about the key-value pairs that AWS Glue consumes to set up
                                your job, see the `Special Parameters Used by AWS Glue
                                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                                topic in the developer guide.

                                - *(string) --*

                                  - *(string) --*

                              - **Timeout** *(integer) --*

                                The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                                can consume resources before it is terminated and enters ``TIMEOUT``
                                status. The default is 2,880 minutes (48 hours). This overrides the timeout
                                value set in the parent job.

                              - **SecurityConfiguration** *(string) --*

                                The name of the ``SecurityConfiguration`` structure to be used with this
                                action.

                              - **NotificationProperty** *(dict) --*

                                Specifies configuration properties of a job run notification.

                                - **NotifyDelayAfter** *(integer) --*

                                  After a job run starts, the number of minutes to wait before sending a
                                  job run delay notification.

                              - **CrawlerName** *(string) --*

                                The name of the crawler to be used with this action.

                          - **Predicate** *(dict) --*

                            The predicate of this trigger, which defines when it will fire.

                            - **Logical** *(string) --*

                              An optional field if only one condition is listed. If multiple conditions are
                              listed, then this field is required.

                            - **Conditions** *(list) --*

                              A list of the conditions that determine when the trigger will fire.

                              - *(dict) --*

                                Defines a condition under which a trigger fires.

                                - **LogicalOperator** *(string) --*

                                  A logical operator.

                                - **JobName** *(string) --*

                                  The name of the job whose ``JobRuns`` this condition applies to, and on
                                  which this trigger waits.

                                - **State** *(string) --*

                                  The condition state. Currently, the values supported are ``SUCCEEDED`` ,
                                  ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                                - **CrawlerName** *(string) --*

                                  The name of the crawler to which this condition applies.

                                - **CrawlState** *(string) --*

                                  The state of the crawler to which this condition applies.

                      - **JobDetails** *(dict) --*

                        Details of the Job when the node represents a Job.

                        - **JobRuns** *(list) --*

                          The information for the job runs represented by the job node.

                          - *(dict) --*

                            Contains information about a job run.

                            - **Id** *(string) --*

                              The ID of this job run.

                            - **Attempt** *(integer) --*

                              The number of the attempt to run this job.

                            - **PreviousRunId** *(string) --*

                              The ID of the previous run of this job. For example, the ``JobRunId``
                              specified in the ``StartJobRun`` action.

                            - **TriggerName** *(string) --*

                              The name of the trigger that started this job run.

                            - **JobName** *(string) --*

                              The name of the job definition being used in this run.

                            - **StartedOn** *(datetime) --*

                              The date and time at which this job run was started.

                            - **LastModifiedOn** *(datetime) --*

                              The last time that this job run was modified.

                            - **CompletedOn** *(datetime) --*

                              The date and time that this job run completed.

                            - **JobRunState** *(string) --*

                              The current state of the job run.

                            - **Arguments** *(dict) --*

                              The job arguments associated with this run. For this job run, they replace
                              the default arguments set in the job definition itself.

                              You can specify arguments here that your own job-execution script consumes,
                              as well as arguments that AWS Glue itself consumes.

                              For information about how to specify and consume your own job arguments, see
                              the `Calling AWS Glue APIs in Python
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                              topic in the developer guide.

                              For information about the key-value pairs that AWS Glue consumes to set up
                              your job, see the `Special Parameters Used by AWS Glue
                              <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                              topic in the developer guide.

                              - *(string) --*

                                - *(string) --*

                            - **ErrorMessage** *(string) --*

                              An error message associated with this job run.

                            - **PredecessorRuns** *(list) --*

                              A list of predecessors to this job run.

                              - *(dict) --*

                                A job run that was used in the predicate of a conditional trigger that
                                triggered this job run.

                                - **JobName** *(string) --*

                                  The name of the job definition used by the predecessor job run.

                                - **RunId** *(string) --*

                                  The job-run ID of the predecessor job run.

                            - **AllocatedCapacity** *(integer) --*

                              This field is deprecated. Use ``MaxCapacity`` instead.

                              The number of AWS Glue data processing units (DPUs) allocated to this JobRun.
                              From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative
                              measure of processing power that consists of 4 vCPUs of compute capacity and
                              16 GB of memory. For more information, see the `AWS Glue pricing page
                              <https://aws.amazon.com/glue/pricing/>`__ .

                            - **ExecutionTime** *(integer) --*

                              The amount of time (in seconds) that the job run consumed resources.

                            - **Timeout** *(integer) --*

                              The ``JobRun`` timeout in minutes. This is the maximum time that a job run
                              can consume resources before it is terminated and enters ``TIMEOUT`` status.
                              The default is 2,880 minutes (48 hours). This overrides the timeout value set
                              in the parent job.

                            - **MaxCapacity** *(float) --*

                              The number of AWS Glue data processing units (DPUs) that can be allocated
                              when this job runs. A DPU is a relative measure of processing power that
                              consists of 4 vCPUs of compute capacity and 16 GB of memory. For more
                              information, see the `AWS Glue pricing page
                              <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                              Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                              The value that can be allocated for ``MaxCapacity`` depends on whether you
                              are running a Python shell job or an Apache Spark ETL job:

                              * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"),
                              you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                              * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"),
                              you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type
                              cannot have a fractional DPU allocation.

                            - **WorkerType** *(string) --*

                              The type of predefined worker that is allocated when a job runs. Accepts a
                              value of Standard, G.1X, or G.2X.

                              * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of
                              memory and a 50GB disk, and 2 executors per worker.

                              * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory
                              and a 64GB disk, and 1 executor per worker.

                              * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory
                              and a 128GB disk, and 1 executor per worker.

                            - **NumberOfWorkers** *(integer) --*

                              The number of workers of a defined ``workerType`` that are allocated when a
                              job runs.

                              The maximum number of workers you can define are 299 for ``G.1X`` , and 149
                              for ``G.2X`` .

                            - **SecurityConfiguration** *(string) --*

                              The name of the ``SecurityConfiguration`` structure to be used with this job
                              run.

                            - **LogGroupName** *(string) --*

                              The name of the log group for secure logging that can be server-side
                              encrypted in Amazon CloudWatch using AWS KMS. This name can be
                              ``/aws-glue/jobs/`` , in which case the default encryption is ``NONE`` . If
                              you add a role name and ``SecurityConfiguration`` name (in other words,
                              ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that
                              security configuration is used to encrypt the log group.

                            - **NotificationProperty** *(dict) --*

                              Specifies configuration properties of a job run notification.

                              - **NotifyDelayAfter** *(integer) --*

                                After a job run starts, the number of minutes to wait before sending a job
                                run delay notification.

                            - **GlueVersion** *(string) --*

                              Glue version determines the versions of Apache Spark and Python that AWS Glue
                              supports. The Python version indicates the version supported for jobs of type
                              Spark.

                              For more information about the available AWS Glue versions and corresponding
                              Spark and Python versions, see `Glue version
                              <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer
                              guide.

                              Jobs that are created without specifying a Glue version default to Glue 0.9.

                      - **CrawlerDetails** *(dict) --*

                        Details of the crawler when the node represents a crawler.

                        - **Crawls** *(list) --*

                          A list of crawls represented by the crawl node.

                          - *(dict) --*

                            The details of a crawl in the workflow.

                            - **State** *(string) --*

                              The state of the crawler.

                            - **StartedOn** *(datetime) --*

                              The date and time on which the crawl started.

                            - **CompletedOn** *(datetime) --*

                              The date and time on which the crawl completed.

                            - **ErrorMessage** *(string) --*

                              The error message associated with the crawl.

                            - **LogGroup** *(string) --*

                              The log group associated with the crawl.

                            - **LogStream** *(string) --*

                              The log stream associated with the crawl.

                  - **Edges** *(list) --*

                    A list of all the directed connections between the nodes belonging to the workflow.

                    - *(dict) --*

                      An edge represents a directed connection between two AWS Glue components which are
                      part of the workflow the edge belongs to.

                      - **SourceId** *(string) --*

                        The unique of the node within the workflow where the edge starts.

                      - **DestinationId** *(string) --*

                        The unique of the node within the workflow where the edge ends.

            - **NextToken** *(string) --*

              A continuation token, if not all requested workflow runs have been returned.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_catalog_to_glue(self, CatalogId: str = None) -> Dict[str, Any]:
        """
        Imports an existing Amazon Athena Data Catalog to AWS Glue

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ImportCatalogToGlue>`_

        **Request Syntax**
        ::

          response = client.import_catalog_to_glue(
              CatalogId='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the catalog to import. Currently, this should be the AWS account ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_crawlers(
        self, MaxResults: int = None, NextToken: str = None, Tags: List[str] = None
    ) -> ClientListCrawlersResponseTypeDef:
        """
        Retrieves the names of all crawler resources in this AWS account, or the resources with the
        specified tag. This operation allows you to see which resources are available in your account, and
        their names.

        This operation takes the optional ``Tags`` field, which you can use as a filter on the response so
        that tagged resources can be retrieved as a group. If you choose to use tags filtering, only
        resources with the tag are retrieved.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ListCrawlers>`_

        **Request Syntax**
        ::

          response = client.list_crawlers(
              MaxResults=123,
              NextToken='string',
              Tags={
                  'string': 'string'
              }
          )
        :type MaxResults: integer
        :param MaxResults:

          The maximum size of a list to return.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation request.

        :type Tags: dict
        :param Tags:

          Specifies to return only these tagged resources.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CrawlerNames': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **CrawlerNames** *(list) --*

              The names of all crawlers in the account, or the crawlers with the specified tags.

              - *(string) --*

            - **NextToken** *(string) --*

              A continuation token, if the returned list does not contain the last metric available.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dev_endpoints(
        self, NextToken: str = None, MaxResults: int = None, Tags: List[str] = None
    ) -> ClientListDevEndpointsResponseTypeDef:
        """
        Retrieves the names of all ``DevEndpoint`` resources in this AWS account, or the resources with the
        specified tag. This operation allows you to see which resources are available in your account, and
        their names.

        This operation takes the optional ``Tags`` field, which you can use as a filter on the response so
        that tagged resources can be retrieved as a group. If you choose to use tags filtering, only
        resources with the tag are retrieved.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ListDevEndpoints>`_

        **Request Syntax**
        ::

          response = client.list_dev_endpoints(
              NextToken='string',
              MaxResults=123,
              Tags={
                  'string': 'string'
              }
          )
        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation request.

        :type MaxResults: integer
        :param MaxResults:

          The maximum size of a list to return.

        :type Tags: dict
        :param Tags:

          Specifies to return only these tagged resources.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DevEndpointNames': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DevEndpointNames** *(list) --*

              The names of all the ``DevEndpoint`` s in the account, or the ``DevEndpoint`` s with the
              specified tags.

              - *(string) --*

            - **NextToken** *(string) --*

              A continuation token, if the returned list does not contain the last metric available.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self, NextToken: str = None, MaxResults: int = None, Tags: List[str] = None
    ) -> ClientListJobsResponseTypeDef:
        """
        Retrieves the names of all job resources in this AWS account, or the resources with the specified
        tag. This operation allows you to see which resources are available in your account, and their
        names.

        This operation takes the optional ``Tags`` field, which you can use as a filter on the response so
        that tagged resources can be retrieved as a group. If you choose to use tags filtering, only
        resources with the tag are retrieved.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ListJobs>`_

        **Request Syntax**
        ::

          response = client.list_jobs(
              NextToken='string',
              MaxResults=123,
              Tags={
                  'string': 'string'
              }
          )
        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation request.

        :type MaxResults: integer
        :param MaxResults:

          The maximum size of a list to return.

        :type Tags: dict
        :param Tags:

          Specifies to return only these tagged resources.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobNames': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobNames** *(list) --*

              The names of all jobs in the account, or the jobs with the specified tags.

              - *(string) --*

            - **NextToken** *(string) --*

              A continuation token, if the returned list does not contain the last metric available.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_triggers(
        self,
        NextToken: str = None,
        DependentJobName: str = None,
        MaxResults: int = None,
        Tags: List[str] = None,
    ) -> ClientListTriggersResponseTypeDef:
        """
        Retrieves the names of all trigger resources in this AWS account, or the resources with the
        specified tag. This operation allows you to see which resources are available in your account, and
        their names.

        This operation takes the optional ``Tags`` field, which you can use as a filter on the response so
        that tagged resources can be retrieved as a group. If you choose to use tags filtering, only
        resources with the tag are retrieved.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ListTriggers>`_

        **Request Syntax**
        ::

          response = client.list_triggers(
              NextToken='string',
              DependentJobName='string',
              MaxResults=123,
              Tags={
                  'string': 'string'
              }
          )
        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation request.

        :type DependentJobName: string
        :param DependentJobName:

          The name of the job for which to retrieve triggers. The trigger that can start this job is
          returned. If there is no such trigger, all triggers are returned.

        :type MaxResults: integer
        :param MaxResults:

          The maximum size of a list to return.

        :type Tags: dict
        :param Tags:

          Specifies to return only these tagged resources.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TriggerNames': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TriggerNames** *(list) --*

              The names of all triggers in the account, or the triggers with the specified tags.

              - *(string) --*

            - **NextToken** *(string) --*

              A continuation token, if the returned list does not contain the last metric available.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_workflows(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListWorkflowsResponseTypeDef:
        """
        Lists names of workflows created in the account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ListWorkflows>`_

        **Request Syntax**
        ::

          response = client.list_workflows(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          A continuation token, if this is a continuation request.

        :type MaxResults: integer
        :param MaxResults:

          The maximum size of a list to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Workflows': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Workflows** *(list) --*

              List of names of workflows in the account.

              - *(string) --*

            - **NextToken** *(string) --*

              A continuation token, if not all workflow names have been returned.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_data_catalog_encryption_settings(
        self,
        DataCatalogEncryptionSettings: ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Sets the security configuration for a specified catalog. After the configuration has been set, the
        specified encryption is applied to every catalog write thereafter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/PutDataCatalogEncryptionSettings>`_

        **Request Syntax**
        ::

          response = client.put_data_catalog_encryption_settings(
              CatalogId='string',
              DataCatalogEncryptionSettings={
                  'EncryptionAtRest': {
                      'CatalogEncryptionMode': 'DISABLED'|'SSE-KMS',
                      'SseAwsKmsKeyId': 'string'
                  },
                  'ConnectionPasswordEncryption': {
                      'ReturnConnectionPasswordEncrypted': True|False,
                      'AwsKmsKeyId': 'string'
                  }
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS
          account ID is used by default.

        :type DataCatalogEncryptionSettings: dict
        :param DataCatalogEncryptionSettings: **[REQUIRED]**

          The security configuration to set.

          - **EncryptionAtRest** *(dict) --*

            Specifies the encryption-at-rest configuration for the Data Catalog.

            - **CatalogEncryptionMode** *(string) --* **[REQUIRED]**

              The encryption-at-rest mode for encrypting Data Catalog data.

            - **SseAwsKmsKeyId** *(string) --*

              The ID of the AWS KMS key to use for encryption at rest.

          - **ConnectionPasswordEncryption** *(dict) --*

            When connection password protection is enabled, the Data Catalog uses a customer-provided key
            to encrypt the password as part of ``CreateConnection`` or ``UpdateConnection`` and store it in
            the ``ENCRYPTED_PASSWORD`` field in the connection properties. You can enable catalog
            encryption or only password encryption.

            - **ReturnConnectionPasswordEncrypted** *(boolean) --* **[REQUIRED]**

              When the ``ReturnConnectionPasswordEncrypted`` flag is set to "true", passwords remain
              encrypted in the responses of ``GetConnection`` and ``GetConnections`` . This encryption
              takes effect independently from catalog encryption.

            - **AwsKmsKeyId** *(string) --*

              An AWS KMS key that is used to encrypt the connection password.

              If connection password protection is enabled, the caller of ``CreateConnection`` and
              ``UpdateConnection`` needs at least ``kms:Encrypt`` permission on the specified AWS KMS key,
              to encrypt passwords before storing them in the Data Catalog.

              You can set the decrypt permission to enable or restrict access on the password key according
              to your security requirements.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_resource_policy(
        self,
        PolicyInJson: str,
        PolicyHashCondition: str = None,
        PolicyExistsCondition: str = None,
    ) -> ClientPutResourcePolicyResponseTypeDef:
        """
        Sets the Data Catalog resource policy for access control.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/PutResourcePolicy>`_

        **Request Syntax**
        ::

          response = client.put_resource_policy(
              PolicyInJson='string',
              PolicyHashCondition='string',
              PolicyExistsCondition='MUST_EXIST'|'NOT_EXIST'|'NONE'
          )
        :type PolicyInJson: string
        :param PolicyInJson: **[REQUIRED]**

          Contains the policy document to set, in JSON format.

        :type PolicyHashCondition: string
        :param PolicyHashCondition:

          The hash value returned when the previous policy was set using ``PutResourcePolicy`` . Its
          purpose is to prevent concurrent modifications of a policy. Do not use this parameter if no
          previous policy has been set.

        :type PolicyExistsCondition: string
        :param PolicyExistsCondition:

          A value of ``MUST_EXIST`` is used to update a policy. A value of ``NOT_EXIST`` is used to create
          a new policy. If a value of ``NONE`` or a null value is used, the call will not depend on the
          existence of a policy.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyHash': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyHash** *(string) --*

              A hash of the policy that has just been set. This must be included in a subsequent call that
              overwrites or updates this policy.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_workflow_run_properties(
        self, Name: str, RunId: str, RunProperties: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Puts the specified workflow run properties for the given workflow run. If a property already exists
        for the specified run, then it overrides the value otherwise adds the property to existing
        properties.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/PutWorkflowRunProperties>`_

        **Request Syntax**
        ::

          response = client.put_workflow_run_properties(
              Name='string',
              RunId='string',
              RunProperties={
                  'string': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the workflow which was run.

        :type RunId: string
        :param RunId: **[REQUIRED]**

          The ID of the workflow run for which the run properties should be updated.

        :type RunProperties: dict
        :param RunProperties: **[REQUIRED]**

          The properties to put for the specified run.

          - *(string) --*

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
    def reset_job_bookmark(
        self, JobName: str, RunId: str = None
    ) -> ClientResetJobBookmarkResponseTypeDef:
        """
        Resets a bookmark entry.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ResetJobBookmark>`_

        **Request Syntax**
        ::

          response = client.reset_job_bookmark(
              JobName='string',
              RunId='string'
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job in question.

        :type RunId: string
        :param RunId:

          The unique run identifier associated with this job run.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobBookmarkEntry': {
                    'JobName': 'string',
                    'Version': 123,
                    'Run': 123,
                    'Attempt': 123,
                    'PreviousRunId': 'string',
                    'RunId': 'string',
                    'JobBookmark': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **JobBookmarkEntry** *(dict) --*

              The reset bookmark entry.

              - **JobName** *(string) --*

                The name of the job in question.

              - **Version** *(integer) --*

                The version of the job.

              - **Run** *(integer) --*

                The run ID number.

              - **Attempt** *(integer) --*

                The attempt ID number.

              - **PreviousRunId** *(string) --*

                The unique run identifier associated with the previous job run.

              - **RunId** *(string) --*

                The run ID number.

              - **JobBookmark** *(string) --*

                The bookmark itself.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_tables(
        self,
        CatalogId: str = None,
        NextToken: str = None,
        Filters: List[ClientSearchTablesFiltersTypeDef] = None,
        SearchText: str = None,
        SortCriteria: List[ClientSearchTablesSortCriteriaTypeDef] = None,
        MaxResults: int = None,
    ) -> ClientSearchTablesResponseTypeDef:
        """
        Searches a set of tables based on properties in the table metadata as well as on the parent
        database. You can search against text or filter conditions.

        You can only get tables that you have access to based on the security policies defined in Lake
        Formation. You need at least a read-only access to the table for it to be returned. If you do not
        have access to all the columns in the table, these columns will not be searched against when
        returning the list of tables back to you. If you have access to the columns but not the data in the
        columns, those columns and the associated metadata for those columns will be included in the search.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/SearchTables>`_

        **Request Syntax**
        ::

          response = client.search_tables(
              CatalogId='string',
              NextToken='string',
              Filters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'Comparator':
                      'EQUALS'|'GREATER_THAN'|'LESS_THAN'|'GREATER_THAN_EQUALS'|'LESS_THAN_EQUALS'
                  },
              ],
              SearchText='string',
              SortCriteria=[
                  {
                      'FieldName': 'string',
                      'Sort': 'ASC'|'DESC'
                  },
              ],
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          A unique identifier, consisting of `` *account_id* /datalake`` .

        :type NextToken: string
        :param NextToken:

          A continuation token, included if this is a continuation call.

        :type Filters: list
        :param Filters:

          A list of key-value pairs, and a comparator used to filter the search results. Returns all
          entities matching the predicate.

          - *(dict) --*

            Defines a property predicate.

            - **Key** *(string) --*

              The key of the property.

            - **Value** *(string) --*

              The value of the property.

            - **Comparator** *(string) --*

              The comparator used to compare this property to others.

        :type SearchText: string
        :param SearchText:

          A string used for a text search.

          Specifying a value in quotes filters based on an exact match to the value.

        :type SortCriteria: list
        :param SortCriteria:

          A list of criteria for sorting the results by a field name, in an ascending or descending order.

          - *(dict) --*

            Specifies a field to sort by and a sort order.

            - **FieldName** *(string) --*

              The name of the field on which to sort.

            - **Sort** *(string) --*

              An ascending or descending sort.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of tables to return in a single response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'TableList': [
                    {
                        'Name': 'string',
                        'DatabaseName': 'string',
                        'Description': 'string',
                        'Owner': 'string',
                        'CreateTime': datetime(2015, 1, 1),
                        'UpdateTime': datetime(2015, 1, 1),
                        'LastAccessTime': datetime(2015, 1, 1),
                        'LastAnalyzedTime': datetime(2015, 1, 1),
                        'Retention': 123,
                        'StorageDescriptor': {
                            'Columns': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'Location': 'string',
                            'InputFormat': 'string',
                            'OutputFormat': 'string',
                            'Compressed': True|False,
                            'NumberOfBuckets': 123,
                            'SerdeInfo': {
                                'Name': 'string',
                                'SerializationLibrary': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                            'BucketColumns': [
                                'string',
                            ],
                            'SortColumns': [
                                {
                                    'Column': 'string',
                                    'SortOrder': 123
                                },
                            ],
                            'Parameters': {
                                'string': 'string'
                            },
                            'SkewedInfo': {
                                'SkewedColumnNames': [
                                    'string',
                                ],
                                'SkewedColumnValues': [
                                    'string',
                                ],
                                'SkewedColumnValueLocationMaps': {
                                    'string': 'string'
                                }
                            },
                            'StoredAsSubDirectories': True|False
                        },
                        'PartitionKeys': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'ViewOriginalText': 'string',
                        'ViewExpandedText': 'string',
                        'TableType': 'string',
                        'Parameters': {
                            'string': 'string'
                        },
                        'CreatedBy': 'string',
                        'IsRegisteredWithLakeFormation': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              A continuation token, present if the current list segment is not the last.

            - **TableList** *(list) --*

              A list of the requested ``Table`` objects. The ``SearchTables`` response returns only the
              tables that you have access to.

              - *(dict) --*

                Represents a collection of related data organized in columns and rows.

                - **Name** *(string) --*

                  The table name. For Hive compatibility, this must be entirely lowercase.

                - **DatabaseName** *(string) --*

                  The name of the database where the table metadata resides. For Hive compatibility, this
                  must be all lowercase.

                - **Description** *(string) --*

                  A description of the table.

                - **Owner** *(string) --*

                  The owner of the table.

                - **CreateTime** *(datetime) --*

                  The time when the table definition was created in the Data Catalog.

                - **UpdateTime** *(datetime) --*

                  The last time that the table was updated.

                - **LastAccessTime** *(datetime) --*

                  The last time that the table was accessed. This is usually taken from HDFS, and might not
                  be reliable.

                - **LastAnalyzedTime** *(datetime) --*

                  The last time that column statistics were computed for this table.

                - **Retention** *(integer) --*

                  The retention time for this table.

                - **StorageDescriptor** *(dict) --*

                  A storage descriptor containing information about the physical storage of this table.

                  - **Columns** *(list) --*

                    A list of the ``Columns`` in the table.

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **Location** *(string) --*

                    The physical location of the table. By default, this takes the form of the warehouse
                    location, followed by the database location in the warehouse, followed by the table
                    name.

                  - **InputFormat** *(string) --*

                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a
                    custom format.

                  - **OutputFormat** *(string) --*

                    The output format: ``SequenceFileOutputFormat`` (binary), or
                    ``IgnoreKeyTextOutputFormat`` , or a custom format.

                  - **Compressed** *(boolean) --*

                     ``True`` if the data in the table is compressed, or ``False`` if not.

                  - **NumberOfBuckets** *(integer) --*

                    Must be specified if the table contains any dimension columns.

                  - **SerdeInfo** *(dict) --*

                    The serialization/deserialization (SerDe) information.

                    - **Name** *(string) --*

                      Name of the SerDe.

                    - **SerializationLibrary** *(string) --*

                      Usually the class that implements the SerDe. An example is
                      ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                    - **Parameters** *(dict) --*

                      These key-value pairs define initialization parameters for the SerDe.

                      - *(string) --*

                        - *(string) --*

                  - **BucketColumns** *(list) --*

                    A list of reducer grouping columns, clustering columns, and bucketing columns in the
                    table.

                    - *(string) --*

                  - **SortColumns** *(list) --*

                    A list specifying the sort order of each bucket in the table.

                    - *(dict) --*

                      Specifies the sort order of a sorted column.

                      - **Column** *(string) --*

                        The name of the column.

                      - **SortOrder** *(integer) --*

                        Indicates that the column is sorted in ascending order (``== 1`` ), or in
                        descending order (``==0`` ).

                  - **Parameters** *(dict) --*

                    The user-supplied properties in key-value form.

                    - *(string) --*

                      - *(string) --*

                  - **SkewedInfo** *(dict) --*

                    The information about values that appear frequently in a column (skewed values).

                    - **SkewedColumnNames** *(list) --*

                      A list of names of columns that contain skewed values.

                      - *(string) --*

                    - **SkewedColumnValues** *(list) --*

                      A list of values that appear so frequently as to be considered skewed.

                      - *(string) --*

                    - **SkewedColumnValueLocationMaps** *(dict) --*

                      A mapping of skewed values to the columns that contain them.

                      - *(string) --*

                        - *(string) --*

                  - **StoredAsSubDirectories** *(boolean) --*

                     ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                - **PartitionKeys** *(list) --*

                  A list of columns by which the table is partitioned. Only primitive types are supported
                  as partition keys.

                  When you create a table used by Amazon Athena, and you do not specify any
                  ``partitionKeys`` , you must at least set the value of ``partitionKeys`` to an empty
                  list. For example:

                   ``"PartitionKeys": []``

                  - *(dict) --*

                    A column in a ``Table`` .

                    - **Name** *(string) --*

                      The name of the ``Column`` .

                    - **Type** *(string) --*

                      The data type of the ``Column`` .

                    - **Comment** *(string) --*

                      A free-form text comment.

                    - **Parameters** *(dict) --*

                      These key-value pairs define properties associated with the column.

                      - *(string) --*

                        - *(string) --*

                - **ViewOriginalText** *(string) --*

                  If the table is a view, the original text of the view; otherwise ``null`` .

                - **ViewExpandedText** *(string) --*

                  If the table is a view, the expanded text of the view; otherwise ``null`` .

                - **TableType** *(string) --*

                  The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

                - **Parameters** *(dict) --*

                  These key-value pairs define properties associated with the table.

                  - *(string) --*

                    - *(string) --*

                - **CreatedBy** *(string) --*

                  The person or entity who created the table.

                - **IsRegisteredWithLakeFormation** *(boolean) --*

                  Indicates whether the table has been registered with AWS Lake Formation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_crawler(self, Name: str) -> Dict[str, Any]:
        """
        Starts a crawl using the specified crawler, regardless of what is scheduled. If the crawler is
        already running, returns a `CrawlerRunningException
        <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-exceptions.html#aws-glue-api-exceptions-CrawlerRunningException>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartCrawler>`_

        **Request Syntax**
        ::

          response = client.start_crawler(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the crawler to start.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        """
        Changes the schedule state of the specified crawler to ``SCHEDULED`` , unless the crawler is
        already running or the schedule state is already ``SCHEDULED`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartCrawlerSchedule>`_

        **Request Syntax**
        ::

          response = client.start_crawler_schedule(
              CrawlerName='string'
          )
        :type CrawlerName: string
        :param CrawlerName: **[REQUIRED]**

          Name of the crawler to schedule.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_export_labels_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> ClientStartExportLabelsTaskRunResponseTypeDef:
        """
        Begins an asynchronous task to export all labeled data for a particular transform. This task is the
        only label-related API call that is not part of the typical active learning workflow. You typically
        use ``StartExportLabelsTaskRun`` when you want to work with all of your existing labels at the same
        time, such as when you want to remove or change labels that were previously submitted as truth.
        This API operation accepts the ``TransformId`` whose labels you want to export and an Amazon Simple
        Storage Service (Amazon S3) path to export the labels to. The operation returns a ``TaskRunId`` .
        You can check on the status of your task run by calling the ``GetMLTaskRun`` API.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartExportLabelsTaskRun>`_

        **Request Syntax**
        ::

          response = client.start_export_labels_task_run(
              TransformId='string',
              OutputS3Path='string'
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the machine learning transform.

        :type OutputS3Path: string
        :param OutputS3Path: **[REQUIRED]**

          The Amazon S3 path where you export the labels.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TaskRunId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TaskRunId** *(string) --*

              The unique identifier for the task run.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_import_labels_task_run(
        self, TransformId: str, InputS3Path: str, ReplaceAllLabels: bool = None
    ) -> ClientStartImportLabelsTaskRunResponseTypeDef:
        """
        Enables you to provide additional labels (examples of truth) to be used to teach the machine
        learning transform and improve its quality. This API operation is generally used as part of the
        active learning workflow that starts with the ``StartMLLabelingSetGenerationTaskRun`` call and that
        ultimately results in improving the quality of your machine learning transform.

        After the ``StartMLLabelingSetGenerationTaskRun`` finishes, AWS Glue machine learning will have
        generated a series of questions for humans to answer. (Answering these questions is often called
        'labeling' in the machine learning workflows). In the case of the ``FindMatches`` transform, these
        questions are of the form, “What is the correct way to group these rows together into groups
        composed entirely of matching records?” After the labeling process is finished, users upload their
        answers/labels with a call to ``StartImportLabelsTaskRun`` . After ``StartImportLabelsTaskRun``
        finishes, all future runs of the machine learning transform use the new and improved labels and
        perform a higher-quality transformation.

        By default, ``StartMLLabelingSetGenerationTaskRun`` continually learns from and combines all labels
        that you upload unless you set ``Replace`` to true. If you set ``Replace`` to true,
        ``StartImportLabelsTaskRun`` deletes and forgets all previously uploaded labels and learns only
        from the exact set that you upload. Replacing labels can be helpful if you realize that you
        previously uploaded incorrect labels, and you believe that they are having a negative effect on
        your transform quality.

        You can check on the status of your task run by calling the ``GetMLTaskRun`` operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartImportLabelsTaskRun>`_

        **Request Syntax**
        ::

          response = client.start_import_labels_task_run(
              TransformId='string',
              InputS3Path='string',
              ReplaceAllLabels=True|False
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the machine learning transform.

        :type InputS3Path: string
        :param InputS3Path: **[REQUIRED]**

          The Amazon Simple Storage Service (Amazon S3) path from where you import the labels.

        :type ReplaceAllLabels: boolean
        :param ReplaceAllLabels:

          Indicates whether to overwrite your existing labels.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TaskRunId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TaskRunId** *(string) --*

              The unique identifier for the task run.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_job_run(
        self,
        JobName: str,
        JobRunId: str = None,
        Arguments: Dict[str, str] = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        NotificationProperty: ClientStartJobRunNotificationPropertyTypeDef = None,
        WorkerType: str = None,
        NumberOfWorkers: int = None,
    ) -> ClientStartJobRunResponseTypeDef:
        """
        Starts a job run using a job definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartJobRun>`_

        **Request Syntax**
        ::

          response = client.start_job_run(
              JobName='string',
              JobRunId='string',
              Arguments={
                  'string': 'string'
              },
              AllocatedCapacity=123,
              Timeout=123,
              MaxCapacity=123.0,
              SecurityConfiguration='string',
              NotificationProperty={
                  'NotifyDelayAfter': 123
              },
              WorkerType='Standard'|'G.1X'|'G.2X',
              NumberOfWorkers=123
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job definition to use.

        :type JobRunId: string
        :param JobRunId:

          The ID of a previous ``JobRun`` to retry.

        :type Arguments: dict
        :param Arguments:

          The job arguments specifically for this run. For this job run, they replace the default arguments
          set in the job definition itself.

          You can specify arguments here that your own job-execution script consumes, as well as arguments
          that AWS Glue itself consumes.

          For information about how to specify and consume your own Job arguments, see the `Calling AWS
          Glue APIs in Python
          <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__ topic in
          the developer guide.

          For information about the key-value pairs that AWS Glue consumes to set up your job, see the
          `Special Parameters Used by AWS Glue
          <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
          topic in the developer guide.

          - *(string) --*

            - *(string) --*

        :type AllocatedCapacity: integer
        :param AllocatedCapacity:

          This field is deprecated. Use ``MaxCapacity`` instead.

          The number of AWS Glue data processing units (DPUs) to allocate to this JobRun. From 2 to 100
          DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that
          consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS
          Glue pricing page <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

        :type Timeout: integer
        :param Timeout:

          The ``JobRun`` timeout in minutes. This is the maximum time that a job run can consume resources
          before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48 hours).
          This overrides the timeout value set in the parent job.

        :type MaxCapacity: float
        :param MaxCapacity:

          The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A
          DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16
          GB of memory. For more information, see the `AWS Glue pricing page
          <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

          Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

          The value that can be allocated for ``MaxCapacity`` depends on whether you are running a Python
          shell job, or an Apache Spark ETL job:

          * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you can allocate
          either 0.0625 or 1 DPU. The default is 0.0625 DPU.

          * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"), you can allocate
          from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.

        :type SecurityConfiguration: string
        :param SecurityConfiguration:

          The name of the ``SecurityConfiguration`` structure to be used with this job run.

        :type NotificationProperty: dict
        :param NotificationProperty:

          Specifies configuration properties of a job run notification.

          - **NotifyDelayAfter** *(integer) --*

            After a job run starts, the number of minutes to wait before sending a job run delay
            notification.

        :type WorkerType: string
        :param WorkerType:

          The type of predefined worker that is allocated when a job runs. Accepts a value of Standard,
          G.1X, or G.2X.

          * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk,
          and 2 executors per worker.

          * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and
          1 executor per worker.

          * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk,
          and 1 executor per worker.

        :type NumberOfWorkers: integer
        :param NumberOfWorkers:

          The number of workers of a defined ``workerType`` that are allocated when a job runs.

          The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobRunId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobRunId** *(string) --*

              The ID assigned to this job run.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_ml_evaluation_task_run(
        self, TransformId: str
    ) -> ClientStartMlEvaluationTaskRunResponseTypeDef:
        """
        Starts a task to estimate the quality of the transform.

        When you provide label sets as examples of truth, AWS Glue machine learning uses some of those
        examples to learn from them. The rest of the labels are used as a test to estimate quality.

        Returns a unique identifier for the run. You can call ``GetMLTaskRun`` to get more information
        about the stats of the ``EvaluationTaskRun`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartMLEvaluationTaskRun>`_

        **Request Syntax**
        ::

          response = client.start_ml_evaluation_task_run(
              TransformId='string'
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the machine learning transform.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TaskRunId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TaskRunId** *(string) --*

              The unique identifier associated with this run.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_ml_labeling_set_generation_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef:
        """
        Starts the active learning workflow for your machine learning transform to improve the transform's
        quality by generating label sets and adding labels.

        When the ``StartMLLabelingSetGenerationTaskRun`` finishes, AWS Glue will have generated a "labeling
        set" or a set of questions for humans to answer.

        In the case of the ``FindMatches`` transform, these questions are of the form, “What is the correct
        way to group these rows together into groups composed entirely of matching records?”

        After the labeling process is finished, you can upload your labels with a call to
        ``StartImportLabelsTaskRun`` . After ``StartImportLabelsTaskRun`` finishes, all future runs of the
        machine learning transform will use the new and improved labels and perform a higher-quality
        transformation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun>`_

        **Request Syntax**
        ::

          response = client.start_ml_labeling_set_generation_task_run(
              TransformId='string',
              OutputS3Path='string'
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          The unique identifier of the machine learning transform.

        :type OutputS3Path: string
        :param OutputS3Path: **[REQUIRED]**

          The Amazon Simple Storage Service (Amazon S3) path where you generate the labeling set.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TaskRunId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TaskRunId** *(string) --*

              The unique run identifier that is associated with this task run.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_trigger(self, Name: str) -> ClientStartTriggerResponseTypeDef:
        """
        Starts an existing trigger. See `Triggering Jobs
        <https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html>`__ for information about how
        different types of trigger are started.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartTrigger>`_

        **Request Syntax**
        ::

          response = client.start_trigger(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the trigger to start.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the trigger that was started.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_workflow_run(self, Name: str) -> ClientStartWorkflowRunResponseTypeDef:
        """
        Starts a new run of the specified workflow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartWorkflowRun>`_

        **Request Syntax**
        ::

          response = client.start_workflow_run(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the workflow to start.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RunId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **RunId** *(string) --*

              An Id for the new run.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_crawler(self, Name: str) -> Dict[str, Any]:
        """
        If the specified crawler is running, stops the crawl.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StopCrawler>`_

        **Request Syntax**
        ::

          response = client.stop_crawler(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the crawler to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        """
        Sets the schedule state of the specified crawler to ``NOT_SCHEDULED`` , but does not stop the
        crawler if it is already running.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StopCrawlerSchedule>`_

        **Request Syntax**
        ::

          response = client.stop_crawler_schedule(
              CrawlerName='string'
          )
        :type CrawlerName: string
        :param CrawlerName: **[REQUIRED]**

          Name of the crawler whose schedule state to set.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_trigger(self, Name: str) -> ClientStopTriggerResponseTypeDef:
        """
        Stops a specified trigger.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StopTrigger>`_

        **Request Syntax**
        ::

          response = client.stop_trigger(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the trigger to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the trigger that was stopped.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceArn: str, TagsToAdd: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Adds tags to a resource. A tag is a label you can assign to an AWS resource. In AWS Glue, you can
        tag only certain resources. For information about what resources you can tag, see `AWS Tags in AWS
        Glue <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              TagsToAdd={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The ARN of the AWS Glue resource to which to add the tags. For more information about AWS Glue
          resource ARNs, see the `AWS Glue ARN string pattern
          <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-common.html#aws-glue-api-regex-aws-glue-arn-id>`__
          .

        :type TagsToAdd: dict
        :param TagsToAdd: **[REQUIRED]**

          Tags to add to this resource.

          - *(string) --*

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
    def untag_resource(
        self, ResourceArn: str, TagsToRemove: List[str]
    ) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagsToRemove=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource from which to remove the tags.

        :type TagsToRemove: list
        :param TagsToRemove: **[REQUIRED]**

          Tags to remove from this resource.

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
    def update_classifier(
        self,
        GrokClassifier: ClientUpdateClassifierGrokClassifierTypeDef = None,
        XMLClassifier: ClientUpdateClassifierXMLClassifierTypeDef = None,
        JsonClassifier: ClientUpdateClassifierJsonClassifierTypeDef = None,
        CsvClassifier: ClientUpdateClassifierCsvClassifierTypeDef = None,
    ) -> Dict[str, Any]:
        """
        Modifies an existing classifier (a ``GrokClassifier`` , an ``XMLClassifier`` , a ``JsonClassifier``
        , or a ``CsvClassifier`` , depending on which field is present).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateClassifier>`_

        **Request Syntax**
        ::

          response = client.update_classifier(
              GrokClassifier={
                  'Name': 'string',
                  'Classification': 'string',
                  'GrokPattern': 'string',
                  'CustomPatterns': 'string'
              },
              XMLClassifier={
                  'Name': 'string',
                  'Classification': 'string',
                  'RowTag': 'string'
              },
              JsonClassifier={
                  'Name': 'string',
                  'JsonPath': 'string'
              },
              CsvClassifier={
                  'Name': 'string',
                  'Delimiter': 'string',
                  'QuoteSymbol': 'string',
                  'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
                  'Header': [
                      'string',
                  ],
                  'DisableValueTrimming': True|False,
                  'AllowSingleColumn': True|False
              }
          )
        :type GrokClassifier: dict
        :param GrokClassifier:

          A ``GrokClassifier`` object with updated fields.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the ``GrokClassifier`` .

          - **Classification** *(string) --*

            An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture
            logs, Amazon CloudWatch Logs, and so on.

          - **GrokPattern** *(string) --*

            The grok pattern used by this classifier.

          - **CustomPatterns** *(string) --*

            Optional custom grok patterns used by this classifier.

        :type XMLClassifier: dict
        :param XMLClassifier:

          An ``XMLClassifier`` object with updated fields.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the classifier.

          - **Classification** *(string) --*

            An identifier of the data format that the classifier matches.

          - **RowTag** *(string) --*

            The XML tag designating the element that contains each record in an XML document being parsed.
            This cannot identify a self-closing element (closed by ``/>`` ). An empty row element that
            contains only attributes can be parsed as long as it ends with a closing tag (for example,
            ``<row item_a="A" item_b="B"></row>`` is okay, but ``<row item_a="A" item_b="B" />`` is not).

        :type JsonClassifier: dict
        :param JsonClassifier:

          A ``JsonClassifier`` object with updated fields.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the classifier.

          - **JsonPath** *(string) --*

            A ``JsonPath`` string defining the JSON data for the classifier to classify. AWS Glue supports
            a subset of ``JsonPath`` , as described in `Writing JsonPath Custom Classifiers
            <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json>`__ .

        :type CsvClassifier: dict
        :param CsvClassifier:

          A ``CsvClassifier`` object with updated fields.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the classifier.

          - **Delimiter** *(string) --*

            A custom symbol to denote what separates each column entry in the row.

          - **QuoteSymbol** *(string) --*

            A custom symbol to denote what combines content into a single column value. It must be
            different from the column delimiter.

          - **ContainsHeader** *(string) --*

            Indicates whether the CSV file contains a header.

          - **Header** *(list) --*

            A list of strings representing column names.

            - *(string) --*

          - **DisableValueTrimming** *(boolean) --*

            Specifies not to trim values before identifying the type of column values. The default value is
            true.

          - **AllowSingleColumn** *(boolean) --*

            Enables the processing of files that contain only one column.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_connection(
        self,
        Name: str,
        ConnectionInput: ClientUpdateConnectionConnectionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Updates a connection definition in the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateConnection>`_

        **Request Syntax**
        ::

          response = client.update_connection(
              CatalogId='string',
              Name='string',
              ConnectionInput={
                  'Name': 'string',
                  'Description': 'string',
                  'ConnectionType': 'JDBC'|'SFTP',
                  'MatchCriteria': [
                      'string',
                  ],
                  'ConnectionProperties': {
                      'string': 'string'
                  },
                  'PhysicalConnectionRequirements': {
                      'SubnetId': 'string',
                      'SecurityGroupIdList': [
                          'string',
                      ],
                      'AvailabilityZone': 'string'
                  }
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the connection resides. If none is provided, the AWS account
          ID is used by default.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the connection definition to update.

        :type ConnectionInput: dict
        :param ConnectionInput: **[REQUIRED]**

          A ``ConnectionInput`` object that redefines the connection in question.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the connection.

          - **Description** *(string) --*

            The description of the connection.

          - **ConnectionType** *(string) --* **[REQUIRED]**

            The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

          - **MatchCriteria** *(list) --*

            A list of criteria that can be used in selecting this connection.

            - *(string) --*

          - **ConnectionProperties** *(dict) --* **[REQUIRED]**

            These key-value pairs define parameters for the connection.

            - *(string) --*

              - *(string) --*

          - **PhysicalConnectionRequirements** *(dict) --*

            A map of physical connection requirements, such as virtual private cloud (VPC) and
            ``SecurityGroup`` , that are needed to successfully make this connection.

            - **SubnetId** *(string) --*

              The subnet ID used by the connection.

            - **SecurityGroupIdList** *(list) --*

              The security group ID list used by the connection.

              - *(string) --*

            - **AvailabilityZone** *(string) --*

              The connection's Availability Zone. This field is redundant because the specified subnet
              implies the Availability Zone to be used. Currently the field must be populated, but it will
              be deprecated in the future.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_crawler(
        self,
        Name: str,
        Role: str = None,
        DatabaseName: str = None,
        Description: str = None,
        Targets: ClientUpdateCrawlerTargetsTypeDef = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: ClientUpdateCrawlerSchemaChangePolicyTypeDef = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
    ) -> Dict[str, Any]:
        """
        Updates a crawler. If a crawler is running, you must stop it using ``StopCrawler`` before updating
        it.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateCrawler>`_

        **Request Syntax**
        ::

          response = client.update_crawler(
              Name='string',
              Role='string',
              DatabaseName='string',
              Description='string',
              Targets={
                  'S3Targets': [
                      {
                          'Path': 'string',
                          'Exclusions': [
                              'string',
                          ]
                      },
                  ],
                  'JdbcTargets': [
                      {
                          'ConnectionName': 'string',
                          'Path': 'string',
                          'Exclusions': [
                              'string',
                          ]
                      },
                  ],
                  'DynamoDBTargets': [
                      {
                          'Path': 'string'
                      },
                  ],
                  'CatalogTargets': [
                      {
                          'DatabaseName': 'string',
                          'Tables': [
                              'string',
                          ]
                      },
                  ]
              },
              Schedule='string',
              Classifiers=[
                  'string',
              ],
              TablePrefix='string',
              SchemaChangePolicy={
                  'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                  'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
              },
              Configuration='string',
              CrawlerSecurityConfiguration='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the new crawler.

        :type Role: string
        :param Role:

          The IAM role or Amazon Resource Name (ARN) of an IAM role that is used by the new crawler to
          access customer resources.

        :type DatabaseName: string
        :param DatabaseName:

          The AWS Glue database where results are stored, such as:
          ``arn:aws:daylight:us-east-1::database/sometable/*`` .

        :type Description: string
        :param Description:

          A description of the new crawler.

        :type Targets: dict
        :param Targets:

          A list of targets to crawl.

          - **S3Targets** *(list) --*

            Specifies Amazon Simple Storage Service (Amazon S3) targets.

            - *(dict) --*

              Specifies a data store in Amazon Simple Storage Service (Amazon S3).

              - **Path** *(string) --*

                The path to the Amazon S3 target.

              - **Exclusions** *(list) --*

                A list of glob patterns used to exclude from the crawl. For more information, see `Catalog
                Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                - *(string) --*

          - **JdbcTargets** *(list) --*

            Specifies JDBC targets.

            - *(dict) --*

              Specifies a JDBC data store to crawl.

              - **ConnectionName** *(string) --*

                The name of the connection to use to connect to the JDBC target.

              - **Path** *(string) --*

                The path of the JDBC target.

              - **Exclusions** *(list) --*

                A list of glob patterns used to exclude from the crawl. For more information, see `Catalog
                Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                - *(string) --*

          - **DynamoDBTargets** *(list) --*

            Specifies Amazon DynamoDB targets.

            - *(dict) --*

              Specifies an Amazon DynamoDB table to crawl.

              - **Path** *(string) --*

                The name of the DynamoDB table to crawl.

          - **CatalogTargets** *(list) --*

            Specifies AWS Glue Data Catalog targets.

            - *(dict) --*

              Specifies an AWS Glue Data Catalog target.

              - **DatabaseName** *(string) --* **[REQUIRED]**

                The name of the database to be synchronized.

              - **Tables** *(list) --* **[REQUIRED]**

                A list of the tables to be synchronized.

                - *(string) --*

        :type Schedule: string
        :param Schedule:

          A ``cron`` expression used to specify the schedule. For more information, see `Time-Based
          Schedules for Jobs and Crawlers
          <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For
          example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

        :type Classifiers: list
        :param Classifiers:

          A list of custom classifiers that the user has registered. By default, all built-in classifiers
          are included in a crawl, but these custom classifiers always override the default classifiers for
          a given classification.

          - *(string) --*

        :type TablePrefix: string
        :param TablePrefix:

          The table prefix used for catalog tables that are created.

        :type SchemaChangePolicy: dict
        :param SchemaChangePolicy:

          The policy for the crawler's update and deletion behavior.

          - **UpdateBehavior** *(string) --*

            The update behavior when the crawler finds a changed schema.

          - **DeleteBehavior** *(string) --*

            The deletion behavior when the crawler finds a deleted object.

        :type Configuration: string
        :param Configuration:

          The crawler configuration information. This versioned JSON string allows users to specify aspects
          of a crawler's behavior. For more information, see `Configuring a Crawler
          <http://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`__ .

        :type CrawlerSecurityConfiguration: string
        :param CrawlerSecurityConfiguration:

          The name of the ``SecurityConfiguration`` structure to be used by this crawler.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_crawler_schedule(
        self, CrawlerName: str, Schedule: str = None
    ) -> Dict[str, Any]:
        """
        Updates the schedule of a crawler using a ``cron`` expression.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateCrawlerSchedule>`_

        **Request Syntax**
        ::

          response = client.update_crawler_schedule(
              CrawlerName='string',
              Schedule='string'
          )
        :type CrawlerName: string
        :param CrawlerName: **[REQUIRED]**

          The name of the crawler whose schedule to update.

        :type Schedule: string
        :param Schedule:

          The updated ``cron`` expression used to specify the schedule. For more information, see
          `Time-Based Schedules for Jobs and Crawlers
          <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For
          example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_database(
        self,
        Name: str,
        DatabaseInput: ClientUpdateDatabaseDatabaseInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Updates an existing database definition in a Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateDatabase>`_

        **Request Syntax**
        ::

          response = client.update_database(
              CatalogId='string',
              Name='string',
              DatabaseInput={
                  'Name': 'string',
                  'Description': 'string',
                  'LocationUri': 'string',
                  'Parameters': {
                      'string': 'string'
                  },
                  'CreateTableDefaultPermissions': [
                      {
                          'Principal': {
                              'DataLakePrincipalIdentifier': 'string'
                          },
                          'Permissions': [
                              'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                              |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                          ]
                      },
                  ]
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the metadata database resides. If none is provided, the AWS
          account ID is used by default.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the database to update in the catalog. For Hive compatibility, this is folded to
          lowercase.

        :type DatabaseInput: dict
        :param DatabaseInput: **[REQUIRED]**

          A ``DatabaseInput`` object specifying the new definition of the metadata database in the catalog.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.

          - **Description** *(string) --*

            A description of the database.

          - **LocationUri** *(string) --*

            The location of the database (for example, an HDFS path).

          - **Parameters** *(dict) --*

            These key-value pairs define parameters and properties of the database.

            These key-value pairs define parameters and properties of the database.

            - *(string) --*

              - *(string) --*

          - **CreateTableDefaultPermissions** *(list) --*

            Creates a set of default permissions on the table for principals.

            - *(dict) --*

              Permissions granted to a principal.

              - **Principal** *(dict) --*

                The principal who is granted permissions.

                - **DataLakePrincipalIdentifier** *(string) --*

                  An identifier for the AWS Lake Formation principal.

              - **Permissions** *(list) --*

                The permissions that are granted to the principal.

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
    def update_dev_endpoint(
        self,
        EndpointName: str,
        PublicKey: str = None,
        AddPublicKeys: List[str] = None,
        DeletePublicKeys: List[str] = None,
        CustomLibraries: ClientUpdateDevEndpointCustomLibrariesTypeDef = None,
        UpdateEtlLibraries: bool = None,
        DeleteArguments: List[str] = None,
        AddArguments: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        Updates a specified development endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateDevEndpoint>`_

        **Request Syntax**
        ::

          response = client.update_dev_endpoint(
              EndpointName='string',
              PublicKey='string',
              AddPublicKeys=[
                  'string',
              ],
              DeletePublicKeys=[
                  'string',
              ],
              CustomLibraries={
                  'ExtraPythonLibsS3Path': 'string',
                  'ExtraJarsS3Path': 'string'
              },
              UpdateEtlLibraries=True|False,
              DeleteArguments=[
                  'string',
              ],
              AddArguments={
                  'string': 'string'
              }
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**

          The name of the ``DevEndpoint`` to be updated.

        :type PublicKey: string
        :param PublicKey:

          The public key for the ``DevEndpoint`` to use.

        :type AddPublicKeys: list
        :param AddPublicKeys:

          The list of public keys for the ``DevEndpoint`` to use.

          - *(string) --*

        :type DeletePublicKeys: list
        :param DeletePublicKeys:

          The list of public keys to be deleted from the ``DevEndpoint`` .

          - *(string) --*

        :type CustomLibraries: dict
        :param CustomLibraries:

          Custom Python or Java libraries to be loaded in the ``DevEndpoint`` .

          - **ExtraPythonLibsS3Path** *(string) --*

            The paths to one or more Python libraries in an Amazon Simple Storage Service (Amazon S3)
            bucket that should be loaded in your ``DevEndpoint`` . Multiple values must be complete paths
            separated by a comma.

            .. note::

              You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on C
              extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis library,
              are not currently supported.

          - **ExtraJarsS3Path** *(string) --*

            The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your
            ``DevEndpoint`` .

            .. note::

              You can only use pure Java/Scala libraries with a ``DevEndpoint`` .

        :type UpdateEtlLibraries: boolean
        :param UpdateEtlLibraries:

           ``True`` if the list of custom libraries to be loaded in the development endpoint needs to be
           updated, or ``False`` if otherwise.

        :type DeleteArguments: list
        :param DeleteArguments:

          The list of argument keys to be deleted from the map of arguments used to configure the
          ``DevEndpoint`` .

          - *(string) --*

        :type AddArguments: dict
        :param AddArguments:

          The map of arguments to add the map of arguments used to configure the ``DevEndpoint`` .

          Valid arguments are:

          * ``"--enable-glue-datacatalog": ""``

          * ``"GLUE_PYTHON_VERSION": "3"``

          * ``"GLUE_PYTHON_VERSION": "2"``

          You can specify a version of Python support for development endpoints by using the ``Arguments``
          parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no arguments are
          provided, the version defaults to Python 2.

          - *(string) --*

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
    def update_job(
        self, JobName: str, JobUpdate: ClientUpdateJobJobUpdateTypeDef
    ) -> ClientUpdateJobResponseTypeDef:
        """
        Updates an existing job definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateJob>`_

        **Request Syntax**
        ::

          response = client.update_job(
              JobName='string',
              JobUpdate={
                  'Description': 'string',
                  'LogUri': 'string',
                  'Role': 'string',
                  'ExecutionProperty': {
                      'MaxConcurrentRuns': 123
                  },
                  'Command': {
                      'Name': 'string',
                      'ScriptLocation': 'string',
                      'PythonVersion': 'string'
                  },
                  'DefaultArguments': {
                      'string': 'string'
                  },
                  'Connections': {
                      'Connections': [
                          'string',
                      ]
                  },
                  'MaxRetries': 123,
                  'AllocatedCapacity': 123,
                  'Timeout': 123,
                  'MaxCapacity': 123.0,
                  'WorkerType': 'Standard'|'G.1X'|'G.2X',
                  'NumberOfWorkers': 123,
                  'SecurityConfiguration': 'string',
                  'NotificationProperty': {
                      'NotifyDelayAfter': 123
                  },
                  'GlueVersion': 'string'
              }
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job definition to update.

        :type JobUpdate: dict
        :param JobUpdate: **[REQUIRED]**

          Specifies the values with which to update the job definition.

          - **Description** *(string) --*

            Description of the job being defined.

          - **LogUri** *(string) --*

            This field is reserved for future use.

          - **Role** *(string) --*

            The name or Amazon Resource Name (ARN) of the IAM role associated with this job (required).

          - **ExecutionProperty** *(dict) --*

            An ``ExecutionProperty`` specifying the maximum number of concurrent runs allowed for this job.

            - **MaxConcurrentRuns** *(integer) --*

              The maximum number of concurrent runs allowed for the job. The default is 1. An error is
              returned when this threshold is reached. The maximum value you can specify is controlled by a
              service limit.

          - **Command** *(dict) --*

            The ``JobCommand`` that executes this job (required).

            - **Name** *(string) --*

              The name of the job command. For an Apache Spark ETL job, this must be ``glueetl`` . For a
              Python shell job, it must be ``pythonshell`` .

            - **ScriptLocation** *(string) --*

              Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job.

            - **PythonVersion** *(string) --*

              The Python version being used to execute a Python shell job. Allowed values are 2 or 3.

          - **DefaultArguments** *(dict) --*

            The default arguments for this job.

            You can specify arguments here that your own job-execution script consumes, as well as
            arguments that AWS Glue itself consumes.

            For information about how to specify and consume your own Job arguments, see the `Calling AWS
            Glue APIs in Python
            <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__ topic
            in the developer guide.

            For information about the key-value pairs that AWS Glue consumes to set up your job, see the
            `Special Parameters Used by AWS Glue
            <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
            topic in the developer guide.

            - *(string) --*

              - *(string) --*

          - **Connections** *(dict) --*

            The connections used for this job.

            - **Connections** *(list) --*

              A list of connections used by the job.

              - *(string) --*

          - **MaxRetries** *(integer) --*

            The maximum number of times to retry this job if it fails.

          - **AllocatedCapacity** *(integer) --*

            This field is deprecated. Use ``MaxCapacity`` instead.

            The number of AWS Glue data processing units (DPUs) to allocate to this job. You can allocate
            from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that
            consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS
            Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .

          - **Timeout** *(integer) --*

            The job timeout in minutes. This is the maximum time that a job run can consume resources
            before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48 hours).

          - **MaxCapacity** *(float) --*

            The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A
            DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and
            16 GB of memory. For more information, see the `AWS Glue pricing page
            <https://aws.amazon.com/glue/pricing/>`__ .

            Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

            The value that can be allocated for ``MaxCapacity`` depends on whether you are running a Python
            shell job or an Apache Spark ETL job:

            * When you specify a Python shell job (``JobCommand.Name`` ="pythonshell"), you can allocate
            either 0.0625 or 1 DPU. The default is 0.0625 DPU.

            * When you specify an Apache Spark ETL job (``JobCommand.Name`` ="glueetl"), you can allocate
            from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU
            allocation.

          - **WorkerType** *(string) --*

            The type of predefined worker that is allocated when a job runs. Accepts a value of Standard,
            G.1X, or G.2X.

            * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB
            disk, and 2 executors per worker.

            * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB
            disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive
            jobs.

            * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB
            disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive
            jobs.

          - **NumberOfWorkers** *(integer) --*

            The number of workers of a defined ``workerType`` that are allocated when a job runs.

            The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

          - **SecurityConfiguration** *(string) --*

            The name of the ``SecurityConfiguration`` structure to be used with this job.

          - **NotificationProperty** *(dict) --*

            Specifies the configuration properties of a job notification.

            - **NotifyDelayAfter** *(integer) --*

              After a job run starts, the number of minutes to wait before sending a job run delay
              notification.

          - **GlueVersion** *(string) --*

            Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The
            Python version indicates the version supported for jobs of type Spark.

            For more information about the available AWS Glue versions and corresponding Spark and Python
            versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the
            developer guide.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobName** *(string) --*

              Returns the name of the updated job definition.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_ml_transform(
        self,
        TransformId: str,
        Name: str = None,
        Description: str = None,
        Parameters: ClientUpdateMlTransformParametersTypeDef = None,
        Role: str = None,
        MaxCapacity: float = None,
        WorkerType: str = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
    ) -> ClientUpdateMlTransformResponseTypeDef:
        """
        Updates an existing machine learning transform. Call this operation to tune the algorithm
        parameters to achieve better results.

        After calling this operation, you can call the ``StartMLEvaluationTaskRun`` operation to assess how
        well your new parameters achieved your goals (such as improving the quality of your machine
        learning transform, or making it more cost-effective).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateMLTransform>`_

        **Request Syntax**
        ::

          response = client.update_ml_transform(
              TransformId='string',
              Name='string',
              Description='string',
              Parameters={
                  'TransformType': 'FIND_MATCHES',
                  'FindMatchesParameters': {
                      'PrimaryKeyColumnName': 'string',
                      'PrecisionRecallTradeoff': 123.0,
                      'AccuracyCostTradeoff': 123.0,
                      'EnforceProvidedLabels': True|False
                  }
              },
              Role='string',
              MaxCapacity=123.0,
              WorkerType='Standard'|'G.1X'|'G.2X',
              NumberOfWorkers=123,
              Timeout=123,
              MaxRetries=123
          )
        :type TransformId: string
        :param TransformId: **[REQUIRED]**

          A unique identifier that was generated when the transform was created.

        :type Name: string
        :param Name:

          The unique name that you gave the transform when you created it.

        :type Description: string
        :param Description:

          A description of the transform. The default is an empty string.

        :type Parameters: dict
        :param Parameters:

          The configuration parameters that are specific to the transform type (algorithm) used.
          Conditionally dependent on the transform type.

          - **TransformType** *(string) --* **[REQUIRED]**

            The type of machine learning transform.

            For information about the types of machine learning transforms, see `Creating Machine Learning
            Transforms
            <http://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html>`__ .

          - **FindMatchesParameters** *(dict) --*

            The parameters for the find matches algorithm.

            - **PrimaryKeyColumnName** *(string) --*

              The name of a column that uniquely identifies rows in the source table. Used to help identify
              matching records.

            - **PrecisionRecallTradeoff** *(float) --*

              The value selected when tuning your transform for a balance between precision and recall. A
              value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a
              value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to
              1.0 means very low recall, and choosing values close to 0.0 results in very low precision.

              The precision metric indicates how often your model is correct when it predicts a match.

              The recall metric indicates that for an actual match, how often your model predicts the match.

            - **AccuracyCostTradeoff** *(float) --*

              The value that is selected when tuning your transform for a balance between accuracy and
              cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of
              1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes
              substantially higher. A value of 0.0 means a bias purely for cost, which results in a less
              accurate ``FindMatches`` transform, sometimes with unacceptable accuracy.

              Accuracy measures how well the transform finds true positives and true negatives. Increasing
              accuracy requires more machine resources and cost. But it also results in increased recall.

              Cost measures how many compute resources, and thus money, are consumed to run the transform.

            - **EnforceProvidedLabels** *(boolean) --*

              The value to switch on or off to force the output to match the provided labels from users. If
              the value is ``True`` , the ``find matches`` transform forces the output to match the
              provided labels. The results override the normal conflation results. If the value is
              ``False`` , the ``find matches`` transform does not ensure all the labels provided are
              respected, and the results rely on the trained model.

              Note that setting this value to true may increase the conflation execution time.

        :type Role: string
        :param Role:

          The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.

        :type MaxCapacity: float
        :param MaxCapacity:

          The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this
          transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of
          processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more
          information, see the `AWS Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .

          When the ``WorkerType`` field is set to a value other than ``Standard`` , the ``MaxCapacity``
          field is set automatically and becomes read-only.

        :type WorkerType: string
        :param WorkerType:

          The type of predefined worker that is allocated when this task runs. Accepts a value of Standard,
          G.1X, or G.2X.

          * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk,
          and 2 executors per worker.

          * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and
          1 executor per worker.

          * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk,
          and 1 executor per worker.

        :type NumberOfWorkers: integer
        :param NumberOfWorkers:

          The number of workers of a defined ``workerType`` that are allocated when this task runs.

        :type Timeout: integer
        :param Timeout:

          The timeout for a task run for this transform in minutes. This is the maximum time that a task
          run for this transform can consume resources before it is terminated and enters ``TIMEOUT``
          status. The default is 2,880 minutes (48 hours).

        :type MaxRetries: integer
        :param MaxRetries:

          The maximum number of times to retry a task for this transform after a task run fails.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TransformId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TransformId** *(string) --*

              The unique identifier for the transform that was updated.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValueList: List[str],
        PartitionInput: ClientUpdatePartitionPartitionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Updates a partition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdatePartition>`_

        **Request Syntax**
        ::

          response = client.update_partition(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              PartitionValueList=[
                  'string',
              ],
              PartitionInput={
                  'Values': [
                      'string',
                  ],
                  'LastAccessTime': datetime(2015, 1, 1),
                  'StorageDescriptor': {
                      'Columns': [
                          {
                              'Name': 'string',
                              'Type': 'string',
                              'Comment': 'string',
                              'Parameters': {
                                  'string': 'string'
                              }
                          },
                      ],
                      'Location': 'string',
                      'InputFormat': 'string',
                      'OutputFormat': 'string',
                      'Compressed': True|False,
                      'NumberOfBuckets': 123,
                      'SerdeInfo': {
                          'Name': 'string',
                          'SerializationLibrary': 'string',
                          'Parameters': {
                              'string': 'string'
                          }
                      },
                      'BucketColumns': [
                          'string',
                      ],
                      'SortColumns': [
                          {
                              'Column': 'string',
                              'SortOrder': 123
                          },
                      ],
                      'Parameters': {
                          'string': 'string'
                      },
                      'SkewedInfo': {
                          'SkewedColumnNames': [
                              'string',
                          ],
                          'SkewedColumnValues': [
                              'string',
                          ],
                          'SkewedColumnValueLocationMaps': {
                              'string': 'string'
                          }
                      },
                      'StoredAsSubDirectories': True|False
                  },
                  'Parameters': {
                      'string': 'string'
                  },
                  'LastAnalyzedTime': datetime(2015, 1, 1)
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the partition to be updated resides. If none is provided, the
          AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database in which the table in question resides.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the table in which the partition to be updated is located.

        :type PartitionValueList: list
        :param PartitionValueList: **[REQUIRED]**

          A list of the values defining the partition.

          - *(string) --*

        :type PartitionInput: dict
        :param PartitionInput: **[REQUIRED]**

          The new partition object to update the partition to.

          - **Values** *(list) --*

            The values of the partition. Although this parameter is not required by the SDK, you must
            specify this parameter for a valid input.

            The values for the keys for the new partition must be passed as an array of String objects that
            must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix.
            Otherwise AWS Glue will add the values to the wrong keys.

            - *(string) --*

          - **LastAccessTime** *(datetime) --*

            The last time at which the partition was accessed.

          - **StorageDescriptor** *(dict) --*

            Provides information about the physical location where the partition is stored.

            - **Columns** *(list) --*

              A list of the ``Columns`` in the table.

              - *(dict) --*

                A column in a ``Table`` .

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the ``Column`` .

                - **Type** *(string) --*

                  The data type of the ``Column`` .

                - **Comment** *(string) --*

                  A free-form text comment.

                - **Parameters** *(dict) --*

                  These key-value pairs define properties associated with the column.

                  - *(string) --*

                    - *(string) --*

            - **Location** *(string) --*

              The physical location of the table. By default, this takes the form of the warehouse
              location, followed by the database location in the warehouse, followed by the table name.

            - **InputFormat** *(string) --*

              The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom
              format.

            - **OutputFormat** *(string) --*

              The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` ,
              or a custom format.

            - **Compressed** *(boolean) --*

               ``True`` if the data in the table is compressed, or ``False`` if not.

            - **NumberOfBuckets** *(integer) --*

              Must be specified if the table contains any dimension columns.

            - **SerdeInfo** *(dict) --*

              The serialization/deserialization (SerDe) information.

              - **Name** *(string) --*

                Name of the SerDe.

              - **SerializationLibrary** *(string) --*

                Usually the class that implements the SerDe. An example is
                ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

              - **Parameters** *(dict) --*

                These key-value pairs define initialization parameters for the SerDe.

                - *(string) --*

                  - *(string) --*

            - **BucketColumns** *(list) --*

              A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

              - *(string) --*

            - **SortColumns** *(list) --*

              A list specifying the sort order of each bucket in the table.

              - *(dict) --*

                Specifies the sort order of a sorted column.

                - **Column** *(string) --* **[REQUIRED]**

                  The name of the column.

                - **SortOrder** *(integer) --* **[REQUIRED]**

                  Indicates that the column is sorted in ascending order (``== 1`` ), or in descending
                  order (``==0`` ).

            - **Parameters** *(dict) --*

              The user-supplied properties in key-value form.

              - *(string) --*

                - *(string) --*

            - **SkewedInfo** *(dict) --*

              The information about values that appear frequently in a column (skewed values).

              - **SkewedColumnNames** *(list) --*

                A list of names of columns that contain skewed values.

                - *(string) --*

              - **SkewedColumnValues** *(list) --*

                A list of values that appear so frequently as to be considered skewed.

                - *(string) --*

              - **SkewedColumnValueLocationMaps** *(dict) --*

                A mapping of skewed values to the columns that contain them.

                - *(string) --*

                  - *(string) --*

            - **StoredAsSubDirectories** *(boolean) --*

               ``True`` if the table data is stored in subdirectories, or ``False`` if not.

          - **Parameters** *(dict) --*

            These key-value pairs define partition parameters.

            - *(string) --*

              - *(string) --*

          - **LastAnalyzedTime** *(datetime) --*

            The last time at which column statistics were computed for this partition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_table(
        self,
        DatabaseName: str,
        TableInput: ClientUpdateTableTableInputTypeDef,
        CatalogId: str = None,
        SkipArchive: bool = None,
    ) -> Dict[str, Any]:
        """
        Updates a metadata table in the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateTable>`_

        **Request Syntax**
        ::

          response = client.update_table(
              CatalogId='string',
              DatabaseName='string',
              TableInput={
                  'Name': 'string',
                  'Description': 'string',
                  'Owner': 'string',
                  'LastAccessTime': datetime(2015, 1, 1),
                  'LastAnalyzedTime': datetime(2015, 1, 1),
                  'Retention': 123,
                  'StorageDescriptor': {
                      'Columns': [
                          {
                              'Name': 'string',
                              'Type': 'string',
                              'Comment': 'string',
                              'Parameters': {
                                  'string': 'string'
                              }
                          },
                      ],
                      'Location': 'string',
                      'InputFormat': 'string',
                      'OutputFormat': 'string',
                      'Compressed': True|False,
                      'NumberOfBuckets': 123,
                      'SerdeInfo': {
                          'Name': 'string',
                          'SerializationLibrary': 'string',
                          'Parameters': {
                              'string': 'string'
                          }
                      },
                      'BucketColumns': [
                          'string',
                      ],
                      'SortColumns': [
                          {
                              'Column': 'string',
                              'SortOrder': 123
                          },
                      ],
                      'Parameters': {
                          'string': 'string'
                      },
                      'SkewedInfo': {
                          'SkewedColumnNames': [
                              'string',
                          ],
                          'SkewedColumnValues': [
                              'string',
                          ],
                          'SkewedColumnValueLocationMaps': {
                              'string': 'string'
                          }
                      },
                      'StoredAsSubDirectories': True|False
                  },
                  'PartitionKeys': [
                      {
                          'Name': 'string',
                          'Type': 'string',
                          'Comment': 'string',
                          'Parameters': {
                              'string': 'string'
                          }
                      },
                  ],
                  'ViewOriginalText': 'string',
                  'ViewExpandedText': 'string',
                  'TableType': 'string',
                  'Parameters': {
                      'string': 'string'
                  }
              },
              SkipArchive=True|False
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is
          used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database in which the table resides. For Hive compatibility, this name is
          entirely lowercase.

        :type TableInput: dict
        :param TableInput: **[REQUIRED]**

          An updated ``TableInput`` object to define the metadata table in the catalog.

          - **Name** *(string) --* **[REQUIRED]**

            The table name. For Hive compatibility, this is folded to lowercase when it is stored.

          - **Description** *(string) --*

            A description of the table.

          - **Owner** *(string) --*

            The table owner.

          - **LastAccessTime** *(datetime) --*

            The last time that the table was accessed.

          - **LastAnalyzedTime** *(datetime) --*

            The last time that column statistics were computed for this table.

          - **Retention** *(integer) --*

            The retention time for this table.

          - **StorageDescriptor** *(dict) --*

            A storage descriptor containing information about the physical storage of this table.

            - **Columns** *(list) --*

              A list of the ``Columns`` in the table.

              - *(dict) --*

                A column in a ``Table`` .

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the ``Column`` .

                - **Type** *(string) --*

                  The data type of the ``Column`` .

                - **Comment** *(string) --*

                  A free-form text comment.

                - **Parameters** *(dict) --*

                  These key-value pairs define properties associated with the column.

                  - *(string) --*

                    - *(string) --*

            - **Location** *(string) --*

              The physical location of the table. By default, this takes the form of the warehouse
              location, followed by the database location in the warehouse, followed by the table name.

            - **InputFormat** *(string) --*

              The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom
              format.

            - **OutputFormat** *(string) --*

              The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` ,
              or a custom format.

            - **Compressed** *(boolean) --*

               ``True`` if the data in the table is compressed, or ``False`` if not.

            - **NumberOfBuckets** *(integer) --*

              Must be specified if the table contains any dimension columns.

            - **SerdeInfo** *(dict) --*

              The serialization/deserialization (SerDe) information.

              - **Name** *(string) --*

                Name of the SerDe.

              - **SerializationLibrary** *(string) --*

                Usually the class that implements the SerDe. An example is
                ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

              - **Parameters** *(dict) --*

                These key-value pairs define initialization parameters for the SerDe.

                - *(string) --*

                  - *(string) --*

            - **BucketColumns** *(list) --*

              A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

              - *(string) --*

            - **SortColumns** *(list) --*

              A list specifying the sort order of each bucket in the table.

              - *(dict) --*

                Specifies the sort order of a sorted column.

                - **Column** *(string) --* **[REQUIRED]**

                  The name of the column.

                - **SortOrder** *(integer) --* **[REQUIRED]**

                  Indicates that the column is sorted in ascending order (``== 1`` ), or in descending
                  order (``==0`` ).

            - **Parameters** *(dict) --*

              The user-supplied properties in key-value form.

              - *(string) --*

                - *(string) --*

            - **SkewedInfo** *(dict) --*

              The information about values that appear frequently in a column (skewed values).

              - **SkewedColumnNames** *(list) --*

                A list of names of columns that contain skewed values.

                - *(string) --*

              - **SkewedColumnValues** *(list) --*

                A list of values that appear so frequently as to be considered skewed.

                - *(string) --*

              - **SkewedColumnValueLocationMaps** *(dict) --*

                A mapping of skewed values to the columns that contain them.

                - *(string) --*

                  - *(string) --*

            - **StoredAsSubDirectories** *(boolean) --*

               ``True`` if the table data is stored in subdirectories, or ``False`` if not.

          - **PartitionKeys** *(list) --*

            A list of columns by which the table is partitioned. Only primitive types are supported as
            partition keys.

            When you create a table used by Amazon Athena, and you do not specify any ``partitionKeys`` ,
            you must at least set the value of ``partitionKeys`` to an empty list. For example:

             ``"PartitionKeys": []``

            - *(dict) --*

              A column in a ``Table`` .

              - **Name** *(string) --* **[REQUIRED]**

                The name of the ``Column`` .

              - **Type** *(string) --*

                The data type of the ``Column`` .

              - **Comment** *(string) --*

                A free-form text comment.

              - **Parameters** *(dict) --*

                These key-value pairs define properties associated with the column.

                - *(string) --*

                  - *(string) --*

          - **ViewOriginalText** *(string) --*

            If the table is a view, the original text of the view; otherwise ``null`` .

          - **ViewExpandedText** *(string) --*

            If the table is a view, the expanded text of the view; otherwise ``null`` .

          - **TableType** *(string) --*

            The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

          - **Parameters** *(dict) --*

            These key-value pairs define properties associated with the table.

            - *(string) --*

              - *(string) --*

        :type SkipArchive: boolean
        :param SkipArchive:

          By default, ``UpdateTable`` always creates an archived version of the table before updating it.
          However, if ``skipArchive`` is set to true, ``UpdateTable`` does not create the archived version.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_trigger(
        self, Name: str, TriggerUpdate: ClientUpdateTriggerTriggerUpdateTypeDef
    ) -> ClientUpdateTriggerResponseTypeDef:
        """
        Updates a trigger definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateTrigger>`_

        **Request Syntax**
        ::

          response = client.update_trigger(
              Name='string',
              TriggerUpdate={
                  'Name': 'string',
                  'Description': 'string',
                  'Schedule': 'string',
                  'Actions': [
                      {
                          'JobName': 'string',
                          'Arguments': {
                              'string': 'string'
                          },
                          'Timeout': 123,
                          'SecurityConfiguration': 'string',
                          'NotificationProperty': {
                              'NotifyDelayAfter': 123
                          },
                          'CrawlerName': 'string'
                      },
                  ],
                  'Predicate': {
                      'Logical': 'AND'|'ANY',
                      'Conditions': [
                          {
                              'LogicalOperator': 'EQUALS',
                              'JobName': 'string',
                              'State':
                              'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                              'CrawlerName': 'string',
                              'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                          },
                      ]
                  }
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the trigger to update.

        :type TriggerUpdate: dict
        :param TriggerUpdate: **[REQUIRED]**

          The new values with which to update the trigger.

          - **Name** *(string) --*

            Reserved for future use.

          - **Description** *(string) --*

            A description of this trigger.

          - **Schedule** *(string) --*

            A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and
            Crawlers <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ .
            For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ?
            *)`` .

          - **Actions** *(list) --*

            The actions initiated by this trigger.

            - *(dict) --*

              Defines an action to be initiated by a trigger.

              - **JobName** *(string) --*

                The name of a job to be executed.

              - **Arguments** *(dict) --*

                The job arguments used when this trigger fires. For this job run, they replace the default
                arguments set in the job definition itself.

                You can specify arguments here that your own job-execution script consumes, as well as
                arguments that AWS Glue itself consumes.

                For information about how to specify and consume your own Job arguments, see the `Calling
                AWS Glue APIs in Python
                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                topic in the developer guide.

                For information about the key-value pairs that AWS Glue consumes to set up your job, see
                the `Special Parameters Used by AWS Glue
                <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                topic in the developer guide.

                - *(string) --*

                  - *(string) --*

              - **Timeout** *(integer) --*

                The ``JobRun`` timeout in minutes. This is the maximum time that a job run can consume
                resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880
                minutes (48 hours). This overrides the timeout value set in the parent job.

              - **SecurityConfiguration** *(string) --*

                The name of the ``SecurityConfiguration`` structure to be used with this action.

              - **NotificationProperty** *(dict) --*

                Specifies configuration properties of a job run notification.

                - **NotifyDelayAfter** *(integer) --*

                  After a job run starts, the number of minutes to wait before sending a job run delay
                  notification.

              - **CrawlerName** *(string) --*

                The name of the crawler to be used with this action.

          - **Predicate** *(dict) --*

            The predicate of this trigger, which defines when it will fire.

            - **Logical** *(string) --*

              An optional field if only one condition is listed. If multiple conditions are listed, then
              this field is required.

            - **Conditions** *(list) --*

              A list of the conditions that determine when the trigger will fire.

              - *(dict) --*

                Defines a condition under which a trigger fires.

                - **LogicalOperator** *(string) --*

                  A logical operator.

                - **JobName** *(string) --*

                  The name of the job whose ``JobRuns`` this condition applies to, and on which this
                  trigger waits.

                - **State** *(string) --*

                  The condition state. Currently, the values supported are ``SUCCEEDED`` , ``STOPPED`` ,
                  ``TIMEOUT`` , and ``FAILED`` .

                - **CrawlerName** *(string) --*

                  The name of the crawler to which this condition applies.

                - **CrawlState** *(string) --*

                  The state of the crawler to which this condition applies.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Trigger': {
                    'Name': 'string',
                    'WorkflowName': 'string',
                    'Id': 'string',
                    'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                    'State':
                    'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'
                    |'UPDATING',
                    'Description': 'string',
                    'Schedule': 'string',
                    'Actions': [
                        {
                            'JobName': 'string',
                            'Arguments': {
                                'string': 'string'
                            },
                            'Timeout': 123,
                            'SecurityConfiguration': 'string',
                            'NotificationProperty': {
                                'NotifyDelayAfter': 123
                            },
                            'CrawlerName': 'string'
                        },
                    ],
                    'Predicate': {
                        'Logical': 'AND'|'ANY',
                        'Conditions': [
                            {
                                'LogicalOperator': 'EQUALS',
                                'JobName': 'string',
                                'State':
                                'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                'CrawlerName': 'string',
                                'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                            },
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Trigger** *(dict) --*

              The resulting trigger definition.

              - **Name** *(string) --*

                The name of the trigger.

              - **WorkflowName** *(string) --*

                The name of the workflow associated with the trigger.

              - **Id** *(string) --*

                Reserved for future use.

              - **Type** *(string) --*

                The type of trigger that this is.

              - **State** *(string) --*

                The current state of the trigger.

              - **Description** *(string) --*

                A description of this trigger.

              - **Schedule** *(string) --*

                A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and
                Crawlers
                <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For
                example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ?
                *)`` .

              - **Actions** *(list) --*

                The actions initiated by this trigger.

                - *(dict) --*

                  Defines an action to be initiated by a trigger.

                  - **JobName** *(string) --*

                    The name of a job to be executed.

                  - **Arguments** *(dict) --*

                    The job arguments used when this trigger fires. For this job run, they replace the
                    default arguments set in the job definition itself.

                    You can specify arguments here that your own job-execution script consumes, as well as
                    arguments that AWS Glue itself consumes.

                    For information about how to specify and consume your own Job arguments, see the
                    `Calling AWS Glue APIs in Python
                    <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                    topic in the developer guide.

                    For information about the key-value pairs that AWS Glue consumes to set up your job,
                    see the `Special Parameters Used by AWS Glue
                    <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                    topic in the developer guide.

                    - *(string) --*

                      - *(string) --*

                  - **Timeout** *(integer) --*

                    The ``JobRun`` timeout in minutes. This is the maximum time that a job run can consume
                    resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880
                    minutes (48 hours). This overrides the timeout value set in the parent job.

                  - **SecurityConfiguration** *(string) --*

                    The name of the ``SecurityConfiguration`` structure to be used with this action.

                  - **NotificationProperty** *(dict) --*

                    Specifies configuration properties of a job run notification.

                    - **NotifyDelayAfter** *(integer) --*

                      After a job run starts, the number of minutes to wait before sending a job run delay
                      notification.

                  - **CrawlerName** *(string) --*

                    The name of the crawler to be used with this action.

              - **Predicate** *(dict) --*

                The predicate of this trigger, which defines when it will fire.

                - **Logical** *(string) --*

                  An optional field if only one condition is listed. If multiple conditions are listed,
                  then this field is required.

                - **Conditions** *(list) --*

                  A list of the conditions that determine when the trigger will fire.

                  - *(dict) --*

                    Defines a condition under which a trigger fires.

                    - **LogicalOperator** *(string) --*

                      A logical operator.

                    - **JobName** *(string) --*

                      The name of the job whose ``JobRuns`` this condition applies to, and on which this
                      trigger waits.

                    - **State** *(string) --*

                      The condition state. Currently, the values supported are ``SUCCEEDED`` , ``STOPPED``
                      , ``TIMEOUT`` , and ``FAILED`` .

                    - **CrawlerName** *(string) --*

                      The name of the crawler to which this condition applies.

                    - **CrawlState** *(string) --*

                      The state of the crawler to which this condition applies.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_defined_function(
        self,
        DatabaseName: str,
        FunctionName: str,
        FunctionInput: ClientUpdateUserDefinedFunctionFunctionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        Updates an existing function definition in the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateUserDefinedFunction>`_

        **Request Syntax**
        ::

          response = client.update_user_defined_function(
              CatalogId='string',
              DatabaseName='string',
              FunctionName='string',
              FunctionInput={
                  'FunctionName': 'string',
                  'ClassName': 'string',
                  'OwnerName': 'string',
                  'OwnerType': 'USER'|'ROLE'|'GROUP',
                  'ResourceUris': [
                      {
                          'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                          'Uri': 'string'
                      },
                  ]
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the function to be updated is located. If none is provided, the
          AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the function to be updated is located.

        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the function.

        :type FunctionInput: dict
        :param FunctionInput: **[REQUIRED]**

          A ``FunctionInput`` object that redefines the function in the Data Catalog.

          - **FunctionName** *(string) --*

            The name of the function.

          - **ClassName** *(string) --*

            The Java class that contains the function code.

          - **OwnerName** *(string) --*

            The owner of the function.

          - **OwnerType** *(string) --*

            The owner type.

          - **ResourceUris** *(list) --*

            The resource URIs for the function.

            - *(dict) --*

              The URIs for function resources.

              - **ResourceType** *(string) --*

                The type of the resource.

              - **Uri** *(string) --*

                The URI for accessing the resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_workflow(
        self,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, str] = None,
    ) -> ClientUpdateWorkflowResponseTypeDef:
        """
        Updates an existing workflow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateWorkflow>`_

        **Request Syntax**
        ::

          response = client.update_workflow(
              Name='string',
              Description='string',
              DefaultRunProperties={
                  'string': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the workflow to be updated.

        :type Description: string
        :param Description:

          The description of the workflow.

        :type DefaultRunProperties: dict
        :param DefaultRunProperties:

          A collection of properties to be used as part of each execution of the workflow.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the workflow which was specified in input.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_classifiers"]
    ) -> paginator_scope.GetClassifiersPaginator:
        """
        Get Paginator for `get_classifiers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_connections"]
    ) -> paginator_scope.GetConnectionsPaginator:
        """
        Get Paginator for `get_connections` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_crawler_metrics"]
    ) -> paginator_scope.GetCrawlerMetricsPaginator:
        """
        Get Paginator for `get_crawler_metrics` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_crawlers"]
    ) -> paginator_scope.GetCrawlersPaginator:
        """
        Get Paginator for `get_crawlers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_databases"]
    ) -> paginator_scope.GetDatabasesPaginator:
        """
        Get Paginator for `get_databases` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_dev_endpoints"]
    ) -> paginator_scope.GetDevEndpointsPaginator:
        """
        Get Paginator for `get_dev_endpoints` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_job_runs"]
    ) -> paginator_scope.GetJobRunsPaginator:
        """
        Get Paginator for `get_job_runs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_jobs"]
    ) -> paginator_scope.GetJobsPaginator:
        """
        Get Paginator for `get_jobs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_partitions"]
    ) -> paginator_scope.GetPartitionsPaginator:
        """
        Get Paginator for `get_partitions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_security_configurations"]
    ) -> paginator_scope.GetSecurityConfigurationsPaginator:
        """
        Get Paginator for `get_security_configurations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_table_versions"]
    ) -> paginator_scope.GetTableVersionsPaginator:
        """
        Get Paginator for `get_table_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_tables"]
    ) -> paginator_scope.GetTablesPaginator:
        """
        Get Paginator for `get_tables` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_triggers"]
    ) -> paginator_scope.GetTriggersPaginator:
        """
        Get Paginator for `get_triggers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_user_defined_functions"]
    ) -> paginator_scope.GetUserDefinedFunctionsPaginator:
        """
        Get Paginator for `get_user_defined_functions` operation.
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
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConcurrentRunsExceededException: Boto3ClientError
    ConditionCheckFailureException: Boto3ClientError
    CrawlerNotRunningException: Boto3ClientError
    CrawlerRunningException: Boto3ClientError
    CrawlerStoppingException: Boto3ClientError
    EntityNotFoundException: Boto3ClientError
    GlueEncryptionException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    MLTransformNotReadyException: Boto3ClientError
    NoScheduleException: Boto3ClientError
    OperationTimeoutException: Boto3ClientError
    ResourceNumberLimitExceededException: Boto3ClientError
    SchedulerNotRunningException: Boto3ClientError
    SchedulerRunningException: Boto3ClientError
    SchedulerTransitioningException: Boto3ClientError
    ValidationException: Boto3ClientError
    VersionMismatchException: Boto3ClientError
