"Main interface for machinelearning type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import TypedDict


__all__ = (
    "BatchPredictionAvailableWaitWaiterConfigTypeDef",
    "ClientAddTagsResponseTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCreateBatchPredictionResponseTypeDef",
    "ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef",
    "ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef",
    "ClientCreateDataSourceFromRdsRDSDataTypeDef",
    "ClientCreateDataSourceFromRdsResponseTypeDef",
    "ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef",
    "ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef",
    "ClientCreateDataSourceFromRedshiftDataSpecTypeDef",
    "ClientCreateDataSourceFromRedshiftResponseTypeDef",
    "ClientCreateDataSourceFromS3DataSpecTypeDef",
    "ClientCreateDataSourceFromS3ResponseTypeDef",
    "ClientCreateEvaluationResponseTypeDef",
    "ClientCreateMlModelResponseTypeDef",
    "ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    "ClientCreateRealtimeEndpointResponseTypeDef",
    "ClientDeleteBatchPredictionResponseTypeDef",
    "ClientDeleteDataSourceResponseTypeDef",
    "ClientDeleteEvaluationResponseTypeDef",
    "ClientDeleteMlModelResponseTypeDef",
    "ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    "ClientDeleteRealtimeEndpointResponseTypeDef",
    "ClientDeleteTagsResponseTypeDef",
    "ClientDescribeBatchPredictionsResponseResultsTypeDef",
    "ClientDescribeBatchPredictionsResponseTypeDef",
    "ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef",
    "ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef",
    "ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    "ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef",
    "ClientDescribeDataSourcesResponseResultsTypeDef",
    "ClientDescribeDataSourcesResponseTypeDef",
    "ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef",
    "ClientDescribeEvaluationsResponseResultsTypeDef",
    "ClientDescribeEvaluationsResponseTypeDef",
    "ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef",
    "ClientDescribeMlModelsResponseResultsTypeDef",
    "ClientDescribeMlModelsResponseTypeDef",
    "ClientDescribeTagsResponseTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientGetBatchPredictionResponseTypeDef",
    "ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef",
    "ClientGetDataSourceResponseRDSMetadataTypeDef",
    "ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef",
    "ClientGetDataSourceResponseRedshiftMetadataTypeDef",
    "ClientGetDataSourceResponseTypeDef",
    "ClientGetEvaluationResponsePerformanceMetricsTypeDef",
    "ClientGetEvaluationResponseTypeDef",
    "ClientGetMlModelResponseEndpointInfoTypeDef",
    "ClientGetMlModelResponseTypeDef",
    "ClientPredictResponsePredictionTypeDef",
    "ClientPredictResponseTypeDef",
    "ClientUpdateBatchPredictionResponseTypeDef",
    "ClientUpdateDataSourceResponseTypeDef",
    "ClientUpdateEvaluationResponseTypeDef",
    "ClientUpdateMlModelResponseTypeDef",
    "DataSourceAvailableWaitWaiterConfigTypeDef",
    "DescribeBatchPredictionsPaginatePaginationConfigTypeDef",
    "DescribeBatchPredictionsPaginateResponseResultsTypeDef",
    "DescribeBatchPredictionsPaginateResponseTypeDef",
    "DescribeDataSourcesPaginatePaginationConfigTypeDef",
    "DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef",
    "DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef",
    "DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    "DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef",
    "DescribeDataSourcesPaginateResponseResultsTypeDef",
    "DescribeDataSourcesPaginateResponseTypeDef",
    "DescribeEvaluationsPaginatePaginationConfigTypeDef",
    "DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef",
    "DescribeEvaluationsPaginateResponseResultsTypeDef",
    "DescribeEvaluationsPaginateResponseTypeDef",
    "DescribeMLModelsPaginatePaginationConfigTypeDef",
    "DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef",
    "DescribeMLModelsPaginateResponseResultsTypeDef",
    "DescribeMLModelsPaginateResponseTypeDef",
    "EvaluationAvailableWaitWaiterConfigTypeDef",
    "MlModelAvailableWaitWaiterConfigTypeDef",
)


_BatchPredictionAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_BatchPredictionAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class BatchPredictionAvailableWaitWaiterConfigTypeDef(
    _BatchPredictionAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `BatchPredictionAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ClientAddTagsResponseTypeDef = TypedDict(
    "_ClientAddTagsResponseTypeDef",
    {"ResourceId": str, "ResourceType": str},
    total=False,
)


class ClientAddTagsResponseTypeDef(_ClientAddTagsResponseTypeDef):
    """
    Type definition for `ClientAddTags` `Response`

    Amazon ML returns the following elements.

    - **ResourceId** *(string) --*

      The ID of the ML object that was tagged.

    - **ResourceType** *(string) --*

      The type of the ML object that was tagged.
    """


_ClientAddTagsTagsTypeDef = TypedDict(
    "_ClientAddTagsTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(_ClientAddTagsTagsTypeDef):
    """
    Type definition for `ClientAddTags` `Tags`

    A custom key-value pair associated with an ML object, such as an ML model.

    - **Key** *(string) --*

      A unique identifier for the tag. Valid characters include Unicode letters, digits, white
      space, _, ., /, =, +, -, %, and @.

    - **Value** *(string) --*

      An optional string, typically used to describe or define the tag. Valid characters include
      Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.
    """


_ClientCreateBatchPredictionResponseTypeDef = TypedDict(
    "_ClientCreateBatchPredictionResponseTypeDef",
    {"BatchPredictionId": str},
    total=False,
)


class ClientCreateBatchPredictionResponseTypeDef(
    _ClientCreateBatchPredictionResponseTypeDef
):
    """
    Type definition for `ClientCreateBatchPrediction` `Response`

    Represents the output of a ``CreateBatchPrediction`` operation, and is an acknowledgement that
    Amazon ML received the request.

    The ``CreateBatchPrediction`` operation is asynchronous. You can poll for status updates by
    using the ``>GetBatchPrediction`` operation and checking the ``Status`` parameter of the result.

    - **BatchPredictionId** *(string) --*

      A user-supplied ID that uniquely identifies the ``BatchPrediction`` . This value is identical
      to the value of the ``BatchPredictionId`` in the request.
    """


_ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef",
    {"Username": str, "Password": str},
)


class ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef(
    _ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef
):
    """
    Type definition for `ClientCreateDataSourceFromRdsRDSData` `DatabaseCredentials`

    The AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon
    RDS database.

    - **Username** *(string) --* **[REQUIRED]**

      The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The
      username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.

    - **Password** *(string) --* **[REQUIRED]**

      The password to be used by Amazon ML to connect to a database on an RDS DB instance. The
      password should have sufficient permissions to execute the ``RDSSelectQuery`` query.
    """


_ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
)


class ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef(
    _ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef
):
    """
    Type definition for `ClientCreateDataSourceFromRdsRDSData` `DatabaseInformation`

    Describes the ``DatabaseName`` and ``InstanceIdentifier`` of an Amazon RDS database.

    - **InstanceIdentifier** *(string) --* **[REQUIRED]**

      The ID of an RDS DB instance.

    - **DatabaseName** *(string) --* **[REQUIRED]**

      The name of a database hosted on an RDS DB instance.
    """


_RequiredClientCreateDataSourceFromRdsRDSDataTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceFromRdsRDSDataTypeDef",
    {
        "DatabaseInformation": ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef,
        "SelectSqlQuery": str,
        "DatabaseCredentials": ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef,
        "S3StagingLocation": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "SubnetId": str,
        "SecurityGroupIds": List[str],
    },
)
_OptionalClientCreateDataSourceFromRdsRDSDataTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceFromRdsRDSDataTypeDef",
    {"DataRearrangement": str, "DataSchema": str, "DataSchemaUri": str},
    total=False,
)


class ClientCreateDataSourceFromRdsRDSDataTypeDef(
    _RequiredClientCreateDataSourceFromRdsRDSDataTypeDef,
    _OptionalClientCreateDataSourceFromRdsRDSDataTypeDef,
):
    """
    Type definition for `ClientCreateDataSourceFromRds` `RDSData`

    The data specification of an Amazon RDS ``DataSource`` :

    * DatabaseInformation -

      * ``DatabaseName`` - The name of the Amazon RDS database.

      * ``InstanceIdentifier`` - A unique identifier for the Amazon RDS database instance.

    * DatabaseCredentials - AWS Identity and Access Management (IAM) credentials that are used to
    connect to the Amazon RDS database.

    * ResourceRole - A role (DataPipelineDefaultResourceRole) assumed by an EC2 instance to carry out
    the copy task from Amazon RDS to Amazon Simple Storage Service (Amazon S3). For more information,
    see `Role templates
    <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data
    pipelines.

    * ServiceRole - A role (DataPipelineDefaultRole) assumed by the AWS Data Pipeline service to
    monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see
    `Role templates
    <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data
    pipelines.

    * SecurityInfo - The security information to use to access an RDS DB instance. You need to set up
    appropriate ingress rules for the security entity IDs provided to allow access to the Amazon RDS
    instance. Specify a [``SubnetId`` , ``SecurityGroupIds`` ] pair for a VPC-based RDS DB instance.

    * SelectSqlQuery - A query that is used to retrieve the observation data for the ``Datasource`` .

    * S3StagingLocation - The Amazon S3 location for staging Amazon RDS data. The data retrieved from
    Amazon RDS using ``SelectSqlQuery`` is stored in this location.

    * DataSchemaUri - The Amazon S3 location of the ``DataSchema`` .

    * DataSchema - A JSON string representing the schema. This is not required if ``DataSchemaUri``
    is specified.

    * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements
    for the ``Datasource`` .   Sample -
    ``"{\\"splitting\\":{\\"percentBegin\\":10,\\"percentEnd\\":60}}"``

    - **DatabaseInformation** *(dict) --* **[REQUIRED]**

      Describes the ``DatabaseName`` and ``InstanceIdentifier`` of an Amazon RDS database.

      - **InstanceIdentifier** *(string) --* **[REQUIRED]**

        The ID of an RDS DB instance.

      - **DatabaseName** *(string) --* **[REQUIRED]**

        The name of a database hosted on an RDS DB instance.

    - **SelectSqlQuery** *(string) --* **[REQUIRED]**

      The query that is used to retrieve the observation data for the ``DataSource`` .

    - **DatabaseCredentials** *(dict) --* **[REQUIRED]**

      The AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon
      RDS database.

      - **Username** *(string) --* **[REQUIRED]**

        The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The
        username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.

      - **Password** *(string) --* **[REQUIRED]**

        The password to be used by Amazon ML to connect to a database on an RDS DB instance. The
        password should have sufficient permissions to execute the ``RDSSelectQuery`` query.

    - **S3StagingLocation** *(string) --* **[REQUIRED]**

      The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using
      ``SelectSqlQuery`` is stored in this location.

    - **DataRearrangement** *(string) --*

      A JSON string that represents the splitting and rearrangement processing to be applied to a
      ``DataSource`` . If the ``DataRearrangement`` parameter is not provided, all of the input data
      is used to create the ``Datasource`` .

      There are multiple parameters that control what data is used to create a datasource:

      * **``percentBegin``**  Use ``percentBegin`` to indicate the beginning of the range of the data
      used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` ,
      Amazon ML includes all of the data when creating the datasource.

      * **``percentEnd``**  Use ``percentEnd`` to indicate the end of the range of the data used to
      create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML
      includes all of the data when creating the datasource.

      * **``complement``**  The ``complement`` parameter instructs Amazon ML to use the data that is
      not included in the range of ``percentBegin`` to ``percentEnd`` to create a datasource. The
      ``complement`` parameter is useful if you need to create complementary datasources for training
      and evaluation. To create a complementary datasource, use the same values for ``percentBegin``
      and ``percentEnd`` , along with the ``complement`` parameter. For example, the following two
      datasources do not share any data, and can be used to train and evaluate a model. The first
      datasource has 25 percent of the data, and the second one has 75 percent of the data.
      Datasource for evaluation: ``{"splitting":{"percentBegin":0, "percentEnd":25}}``  Datasource
      for training: ``{"splitting":{"percentBegin":0, "percentEnd":25, "complement":"true"}}``

      * **``strategy``**  To change how Amazon ML splits the data for a datasource, use the
      ``strategy`` parameter. The default value for the ``strategy`` parameter is ``sequential`` ,
      meaning that Amazon ML takes all of the data records between the ``percentBegin`` and
      ``percentEnd`` parameters for the datasource, in the order that the records appear in the input
      data. The following two ``DataRearrangement`` lines are examples of sequentially ordered
      training and evaluation datasources: Datasource for evaluation:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}``  Datasource
      for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential",
      "complement":"true"}}``  To randomly split the input data into the proportions indicated by the
      percentBegin and percentEnd parameters, set the ``strategy`` parameter to ``random`` and
      provide a string that is used as the seed value for the random data splitting (for example, you
      can use the S3 path to your data as the random seed string). If you choose the random split
      strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then
      selects the rows that have an assigned number between ``percentBegin`` and ``percentEnd`` .
      Pseudo-random numbers are assigned using both the input seed string value and the byte offset
      as a seed, so changing the data results in a different split. Any existing ordering is
      preserved. The random splitting strategy ensures that variables in the training and evaluation
      data are distributed similarly. It is useful in the cases where the input data may have an
      implicit sort order, which would otherwise result in training and evaluation datasources
      containing non-similar data records. The following two ``DataRearrangement`` lines are examples
      of non-sequentially ordered training and evaluation datasources: Datasource for evaluation:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random",
      "randomSeed"="s3://my_s3_path/bucket/file.csv"}}``  Datasource for training:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random",
      "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}``

    - **DataSchema** *(string) --*

      A JSON string that represents the schema for an Amazon RDS ``DataSource`` . The ``DataSchema``
      defines the structure of the observation data in the data file(s) referenced in the
      ``DataSource`` .

      A ``DataSchema`` is not required if you specify a ``DataSchemaUri``

      Define your ``DataSchema`` as a series of key-value pairs. ``attributes`` and
      ``excludedVariableNames`` have an array of key-value pairs for their value. Use the following
      format to define your ``DataSchema`` .

      { "version": "1.0",

      "recordAnnotationFieldName": "F1",

      "recordWeightFieldName": "F2",

      "targetFieldName": "F3",

      "dataFormat": "CSV",

      "dataFileContainsHeader": true,

      "attributes": [

      { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2", "fieldType": "NUMERIC" }, {
      "fieldName": "F3", "fieldType": "CATEGORICAL" }, { "fieldName": "F4", "fieldType": "NUMERIC" },
      { "fieldName": "F5", "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" },
      { "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName": "F8", "fieldType":
      "WEIGHTED_STRING_SEQUENCE" } ],

      "excludedVariableNames": [ "F6" ] }

    - **DataSchemaUri** *(string) --*

      The Amazon S3 location of the ``DataSchema`` .

    - **ResourceRole** *(string) --* **[REQUIRED]**

      The role (DataPipelineDefaultResourceRole) assumed by an Amazon Elastic Compute Cloud (Amazon
      EC2) instance to carry out the copy operation from Amazon RDS to an Amazon S3 task. For more
      information, see `Role templates
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data
      pipelines.

    - **ServiceRole** *(string) --* **[REQUIRED]**

      The role (DataPipelineDefaultRole) assumed by AWS Data Pipeline service to monitor the progress
      of the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data
      pipelines.

    - **SubnetId** *(string) --* **[REQUIRED]**

      The subnet ID to be used to access a VPC-based RDS DB instance. This attribute is used by Data
      Pipeline to carry out the copy task from Amazon RDS to Amazon S3.

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The security group IDs to be used to access a VPC-based RDS DB instance. Ensure that there are
      appropriate ingress rules set up to allow access to the RDS DB instance. This attribute is used
      by Data Pipeline to carry out the copy operation from Amazon RDS to an Amazon S3 task.

      - *(string) --*
    """


_ClientCreateDataSourceFromRdsResponseTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRdsResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientCreateDataSourceFromRdsResponseTypeDef(
    _ClientCreateDataSourceFromRdsResponseTypeDef
):
    """
    Type definition for `ClientCreateDataSourceFromRds` `Response`

    Represents the output of a ``CreateDataSourceFromRDS`` operation, and is an acknowledgement
    that Amazon ML received the request.

    The ``CreateDataSourceFromRDS`` > operation is asynchronous. You can poll for updates by using
    the ``GetBatchPrediction`` operation and checking the ``Status`` parameter. You can inspect the
    ``Message`` when ``Status`` shows up as ``FAILED`` . You can also check the progress of the
    copy operation by going to the ``DataPipeline`` console and looking up the pipeline using the
    ``pipelineId`` from the describe call.

    - **DataSourceId** *(string) --*

      A user-supplied ID that uniquely identifies the datasource. This value should be identical to
      the value of the ``DataSourceID`` in the request.
    """


_ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef",
    {"Username": str, "Password": str},
)


class ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef(
    _ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef
):
    """
    Type definition for `ClientCreateDataSourceFromRedshiftDataSpec` `DatabaseCredentials`

    Describes AWS Identity and Access Management (IAM) credentials that are used connect to the
    Amazon Redshift database.

    - **Username** *(string) --* **[REQUIRED]**

      A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an
      Amazon Redshift cluster. The username should have sufficient permissions to execute the
      ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER
      <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

    - **Password** *(string) --* **[REQUIRED]**

      A password to be used by Amazon ML to connect to a database on an Amazon Redshift cluster.
      The password should have sufficient permissions to execute a ``RedshiftSelectSqlQuery``
      query. The password should be valid for an Amazon Redshift `USER
      <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .
    """


_ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
)


class ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef(
    _ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef
):
    """
    Type definition for `ClientCreateDataSourceFromRedshiftDataSpec` `DatabaseInformation`

    Describes the ``DatabaseName`` and ``ClusterIdentifier`` for an Amazon Redshift ``DataSource`` .

    - **DatabaseName** *(string) --* **[REQUIRED]**

      The name of a database hosted on an Amazon Redshift cluster.

    - **ClusterIdentifier** *(string) --* **[REQUIRED]**

      The ID of an Amazon Redshift cluster.
    """


_RequiredClientCreateDataSourceFromRedshiftDataSpecTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceFromRedshiftDataSpecTypeDef",
    {
        "DatabaseInformation": ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef,
        "SelectSqlQuery": str,
        "DatabaseCredentials": ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef,
        "S3StagingLocation": str,
    },
)
_OptionalClientCreateDataSourceFromRedshiftDataSpecTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceFromRedshiftDataSpecTypeDef",
    {"DataRearrangement": str, "DataSchema": str, "DataSchemaUri": str},
    total=False,
)


class ClientCreateDataSourceFromRedshiftDataSpecTypeDef(
    _RequiredClientCreateDataSourceFromRedshiftDataSpecTypeDef,
    _OptionalClientCreateDataSourceFromRedshiftDataSpecTypeDef,
):
    """
    Type definition for `ClientCreateDataSourceFromRedshift` `DataSpec`

    The data specification of an Amazon Redshift ``DataSource`` :

    * DatabaseInformation -

      * ``DatabaseName`` - The name of the Amazon Redshift database.

      * ``ClusterIdentifier`` - The unique ID for the Amazon Redshift cluster.

    * DatabaseCredentials - The AWS Identity and Access Management (IAM) credentials that are used to
    connect to the Amazon Redshift database.

    * SelectSqlQuery - The query that is used to retrieve the observation data for the ``Datasource``
    .

    * S3StagingLocation - The Amazon Simple Storage Service (Amazon S3) location for staging Amazon
    Redshift data. The data retrieved from Amazon Redshift using the ``SelectSqlQuery`` query is
    stored in this location.

    * DataSchemaUri - The Amazon S3 location of the ``DataSchema`` .

    * DataSchema - A JSON string representing the schema. This is not required if ``DataSchemaUri``
    is specified.

    * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements
    for the ``DataSource`` . Sample -
    ``"{\\"splitting\\":{\\"percentBegin\\":10,\\"percentEnd\\":60}}"``

    - **DatabaseInformation** *(dict) --* **[REQUIRED]**

      Describes the ``DatabaseName`` and ``ClusterIdentifier`` for an Amazon Redshift ``DataSource`` .

      - **DatabaseName** *(string) --* **[REQUIRED]**

        The name of a database hosted on an Amazon Redshift cluster.

      - **ClusterIdentifier** *(string) --* **[REQUIRED]**

        The ID of an Amazon Redshift cluster.

    - **SelectSqlQuery** *(string) --* **[REQUIRED]**

      Describes the SQL Query to execute on an Amazon Redshift database for an Amazon Redshift
      ``DataSource`` .

    - **DatabaseCredentials** *(dict) --* **[REQUIRED]**

      Describes AWS Identity and Access Management (IAM) credentials that are used connect to the
      Amazon Redshift database.

      - **Username** *(string) --* **[REQUIRED]**

        A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an
        Amazon Redshift cluster. The username should have sufficient permissions to execute the
        ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER
        <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

      - **Password** *(string) --* **[REQUIRED]**

        A password to be used by Amazon ML to connect to a database on an Amazon Redshift cluster.
        The password should have sufficient permissions to execute a ``RedshiftSelectSqlQuery``
        query. The password should be valid for an Amazon Redshift `USER
        <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

    - **S3StagingLocation** *(string) --* **[REQUIRED]**

      Describes an Amazon S3 location to store the result set of the ``SelectSqlQuery`` query.

    - **DataRearrangement** *(string) --*

      A JSON string that represents the splitting and rearrangement processing to be applied to a
      ``DataSource`` . If the ``DataRearrangement`` parameter is not provided, all of the input data
      is used to create the ``Datasource`` .

      There are multiple parameters that control what data is used to create a datasource:

      * **``percentBegin``**  Use ``percentBegin`` to indicate the beginning of the range of the data
      used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` ,
      Amazon ML includes all of the data when creating the datasource.

      * **``percentEnd``**  Use ``percentEnd`` to indicate the end of the range of the data used to
      create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML
      includes all of the data when creating the datasource.

      * **``complement``**  The ``complement`` parameter instructs Amazon ML to use the data that is
      not included in the range of ``percentBegin`` to ``percentEnd`` to create a datasource. The
      ``complement`` parameter is useful if you need to create complementary datasources for training
      and evaluation. To create a complementary datasource, use the same values for ``percentBegin``
      and ``percentEnd`` , along with the ``complement`` parameter. For example, the following two
      datasources do not share any data, and can be used to train and evaluate a model. The first
      datasource has 25 percent of the data, and the second one has 75 percent of the data.
      Datasource for evaluation: ``{"splitting":{"percentBegin":0, "percentEnd":25}}``  Datasource
      for training: ``{"splitting":{"percentBegin":0, "percentEnd":25, "complement":"true"}}``

      * **``strategy``**  To change how Amazon ML splits the data for a datasource, use the
      ``strategy`` parameter. The default value for the ``strategy`` parameter is ``sequential`` ,
      meaning that Amazon ML takes all of the data records between the ``percentBegin`` and
      ``percentEnd`` parameters for the datasource, in the order that the records appear in the input
      data. The following two ``DataRearrangement`` lines are examples of sequentially ordered
      training and evaluation datasources: Datasource for evaluation:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}``  Datasource
      for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential",
      "complement":"true"}}``  To randomly split the input data into the proportions indicated by the
      percentBegin and percentEnd parameters, set the ``strategy`` parameter to ``random`` and
      provide a string that is used as the seed value for the random data splitting (for example, you
      can use the S3 path to your data as the random seed string). If you choose the random split
      strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then
      selects the rows that have an assigned number between ``percentBegin`` and ``percentEnd`` .
      Pseudo-random numbers are assigned using both the input seed string value and the byte offset
      as a seed, so changing the data results in a different split. Any existing ordering is
      preserved. The random splitting strategy ensures that variables in the training and evaluation
      data are distributed similarly. It is useful in the cases where the input data may have an
      implicit sort order, which would otherwise result in training and evaluation datasources
      containing non-similar data records. The following two ``DataRearrangement`` lines are examples
      of non-sequentially ordered training and evaluation datasources: Datasource for evaluation:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random",
      "randomSeed"="s3://my_s3_path/bucket/file.csv"}}``  Datasource for training:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random",
      "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}``

    - **DataSchema** *(string) --*

      A JSON string that represents the schema for an Amazon Redshift ``DataSource`` . The
      ``DataSchema`` defines the structure of the observation data in the data file(s) referenced in
      the ``DataSource`` .

      A ``DataSchema`` is not required if you specify a ``DataSchemaUri`` .

      Define your ``DataSchema`` as a series of key-value pairs. ``attributes`` and
      ``excludedVariableNames`` have an array of key-value pairs for their value. Use the following
      format to define your ``DataSchema`` .

      { "version": "1.0",

      "recordAnnotationFieldName": "F1",

      "recordWeightFieldName": "F2",

      "targetFieldName": "F3",

      "dataFormat": "CSV",

      "dataFileContainsHeader": true,

      "attributes": [

      { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2", "fieldType": "NUMERIC" }, {
      "fieldName": "F3", "fieldType": "CATEGORICAL" }, { "fieldName": "F4", "fieldType": "NUMERIC" },
      { "fieldName": "F5", "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" },
      { "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName": "F8", "fieldType":
      "WEIGHTED_STRING_SEQUENCE" } ],

      "excludedVariableNames": [ "F6" ] }

    - **DataSchemaUri** *(string) --*

      Describes the schema location for an Amazon Redshift ``DataSource`` .
    """


_ClientCreateDataSourceFromRedshiftResponseTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRedshiftResponseTypeDef",
    {"DataSourceId": str},
    total=False,
)


class ClientCreateDataSourceFromRedshiftResponseTypeDef(
    _ClientCreateDataSourceFromRedshiftResponseTypeDef
):
    """
    Type definition for `ClientCreateDataSourceFromRedshift` `Response`

    Represents the output of a ``CreateDataSourceFromRedshift`` operation, and is an
    acknowledgement that Amazon ML received the request.

    The ``CreateDataSourceFromRedshift`` operation is asynchronous. You can poll for updates by
    using the ``GetBatchPrediction`` operation and checking the ``Status`` parameter.

    - **DataSourceId** *(string) --*

      A user-supplied ID that uniquely identifies the datasource. This value should be identical to
      the value of the ``DataSourceID`` in the request.
    """


_RequiredClientCreateDataSourceFromS3DataSpecTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceFromS3DataSpecTypeDef", {"DataLocationS3": str}
)
_OptionalClientCreateDataSourceFromS3DataSpecTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceFromS3DataSpecTypeDef",
    {"DataRearrangement": str, "DataSchema": str, "DataSchemaLocationS3": str},
    total=False,
)


class ClientCreateDataSourceFromS3DataSpecTypeDef(
    _RequiredClientCreateDataSourceFromS3DataSpecTypeDef,
    _OptionalClientCreateDataSourceFromS3DataSpecTypeDef,
):
    """
    Type definition for `ClientCreateDataSourceFromS3` `DataSpec`

    The data specification of a ``DataSource`` :

    * DataLocationS3 - The Amazon S3 location of the observation data.

    * DataSchemaLocationS3 - The Amazon S3 location of the ``DataSchema`` .

    * DataSchema - A JSON string representing the schema. This is not required if ``DataSchemaUri``
    is specified.

    * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements
    for the ``Datasource`` .  Sample -
    ``"{\\"splitting\\":{\\"percentBegin\\":10,\\"percentEnd\\":60}}"``

    - **DataLocationS3** *(string) --* **[REQUIRED]**

      The location of the data file(s) used by a ``DataSource`` . The URI specifies a data file or an
      Amazon Simple Storage Service (Amazon S3) directory or bucket containing data files.

    - **DataRearrangement** *(string) --*

      A JSON string that represents the splitting and rearrangement processing to be applied to a
      ``DataSource`` . If the ``DataRearrangement`` parameter is not provided, all of the input data
      is used to create the ``Datasource`` .

      There are multiple parameters that control what data is used to create a datasource:

      * **``percentBegin``**  Use ``percentBegin`` to indicate the beginning of the range of the data
      used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` ,
      Amazon ML includes all of the data when creating the datasource.

      * **``percentEnd``**  Use ``percentEnd`` to indicate the end of the range of the data used to
      create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML
      includes all of the data when creating the datasource.

      * **``complement``**  The ``complement`` parameter instructs Amazon ML to use the data that is
      not included in the range of ``percentBegin`` to ``percentEnd`` to create a datasource. The
      ``complement`` parameter is useful if you need to create complementary datasources for training
      and evaluation. To create a complementary datasource, use the same values for ``percentBegin``
      and ``percentEnd`` , along with the ``complement`` parameter. For example, the following two
      datasources do not share any data, and can be used to train and evaluate a model. The first
      datasource has 25 percent of the data, and the second one has 75 percent of the data.
      Datasource for evaluation: ``{"splitting":{"percentBegin":0, "percentEnd":25}}``  Datasource
      for training: ``{"splitting":{"percentBegin":0, "percentEnd":25, "complement":"true"}}``

      * **``strategy``**  To change how Amazon ML splits the data for a datasource, use the
      ``strategy`` parameter. The default value for the ``strategy`` parameter is ``sequential`` ,
      meaning that Amazon ML takes all of the data records between the ``percentBegin`` and
      ``percentEnd`` parameters for the datasource, in the order that the records appear in the input
      data. The following two ``DataRearrangement`` lines are examples of sequentially ordered
      training and evaluation datasources: Datasource for evaluation:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}``  Datasource
      for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential",
      "complement":"true"}}``  To randomly split the input data into the proportions indicated by the
      percentBegin and percentEnd parameters, set the ``strategy`` parameter to ``random`` and
      provide a string that is used as the seed value for the random data splitting (for example, you
      can use the S3 path to your data as the random seed string). If you choose the random split
      strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then
      selects the rows that have an assigned number between ``percentBegin`` and ``percentEnd`` .
      Pseudo-random numbers are assigned using both the input seed string value and the byte offset
      as a seed, so changing the data results in a different split. Any existing ordering is
      preserved. The random splitting strategy ensures that variables in the training and evaluation
      data are distributed similarly. It is useful in the cases where the input data may have an
      implicit sort order, which would otherwise result in training and evaluation datasources
      containing non-similar data records. The following two ``DataRearrangement`` lines are examples
      of non-sequentially ordered training and evaluation datasources: Datasource for evaluation:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random",
      "randomSeed"="s3://my_s3_path/bucket/file.csv"}}``  Datasource for training:
      ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random",
      "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}``

    - **DataSchema** *(string) --*

      A JSON string that represents the schema for an Amazon S3 ``DataSource`` . The ``DataSchema``
      defines the structure of the observation data in the data file(s) referenced in the
      ``DataSource`` .

      You must provide either the ``DataSchema`` or the ``DataSchemaLocationS3`` .

      Define your ``DataSchema`` as a series of key-value pairs. ``attributes`` and
      ``excludedVariableNames`` have an array of key-value pairs for their value. Use the following
      format to define your ``DataSchema`` .

      { "version": "1.0",

      "recordAnnotationFieldName": "F1",

      "recordWeightFieldName": "F2",

      "targetFieldName": "F3",

      "dataFormat": "CSV",

      "dataFileContainsHeader": true,

      "attributes": [

      { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2", "fieldType": "NUMERIC" }, {
      "fieldName": "F3", "fieldType": "CATEGORICAL" }, { "fieldName": "F4", "fieldType": "NUMERIC" },
      { "fieldName": "F5", "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" },
      { "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName": "F8", "fieldType":
      "WEIGHTED_STRING_SEQUENCE" } ],

      "excludedVariableNames": [ "F6" ] }

    - **DataSchemaLocationS3** *(string) --*

      Describes the schema location in Amazon S3. You must provide either the ``DataSchema`` or the
      ``DataSchemaLocationS3`` .
    """


_ClientCreateDataSourceFromS3ResponseTypeDef = TypedDict(
    "_ClientCreateDataSourceFromS3ResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientCreateDataSourceFromS3ResponseTypeDef(
    _ClientCreateDataSourceFromS3ResponseTypeDef
):
    """
    Type definition for `ClientCreateDataSourceFromS3` `Response`

    Represents the output of a ``CreateDataSourceFromS3`` operation, and is an acknowledgement that
    Amazon ML received the request.

    The ``CreateDataSourceFromS3`` operation is asynchronous. You can poll for updates by using the
    ``GetBatchPrediction`` operation and checking the ``Status`` parameter.

    - **DataSourceId** *(string) --*

      A user-supplied ID that uniquely identifies the ``DataSource`` . This value should be
      identical to the value of the ``DataSourceID`` in the request.
    """


_ClientCreateEvaluationResponseTypeDef = TypedDict(
    "_ClientCreateEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)


class ClientCreateEvaluationResponseTypeDef(_ClientCreateEvaluationResponseTypeDef):
    """
    Type definition for `ClientCreateEvaluation` `Response`

    Represents the output of a ``CreateEvaluation`` operation, and is an acknowledgement that
    Amazon ML received the request.

    ``CreateEvaluation`` operation is asynchronous. You can poll for status updates by using the
    ``GetEvcaluation`` operation and checking the ``Status`` parameter.

    - **EvaluationId** *(string) --*

      The user-supplied ID that uniquely identifies the ``Evaluation`` . This value should be
      identical to the value of the ``EvaluationId`` in the request.
    """


_ClientCreateMlModelResponseTypeDef = TypedDict(
    "_ClientCreateMlModelResponseTypeDef", {"MLModelId": str}, total=False
)


class ClientCreateMlModelResponseTypeDef(_ClientCreateMlModelResponseTypeDef):
    """
    Type definition for `ClientCreateMlModel` `Response`

    Represents the output of a ``CreateMLModel`` operation, and is an acknowledgement that Amazon
    ML received the request.

    The ``CreateMLModel`` operation is asynchronous. You can poll for status updates by using the
    ``GetMLModel`` operation and checking the ``Status`` parameter.

    - **MLModelId** *(string) --*

      A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical
      to the value of the ``MLModelId`` in the request.
    """


_ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef = TypedDict(
    "_ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": str,
    },
    total=False,
)


class ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef(
    _ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef
):
    """
    Type definition for `ClientCreateRealtimeEndpointResponse` `RealtimeEndpointInfo`

    The endpoint information of the ``MLModel``

    - **PeakRequestsPerSecond** *(integer) --*

      The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
      incoming requests per second.

    - **CreatedAt** *(datetime) --*

      The time that the request to create the real-time endpoint for the ``MLModel`` was
      received. The time is expressed in epoch time.

    - **EndpointUrl** *(string) --*

      The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

      .. note::

        Note

        The application must wait until the real-time endpoint is ready before using this URI.

    - **EndpointStatus** *(string) --*

      The current status of the real-time endpoint for the ``MLModel`` . This element can have
      one of the following values:

      * ``NONE`` - Endpoint does not exist or was previously deleted.

      * ``READY`` - Endpoint is ready to be used for real-time predictions.

      * ``UPDATING`` - Updating/creating the endpoint.
    """


_ClientCreateRealtimeEndpointResponseTypeDef = TypedDict(
    "_ClientCreateRealtimeEndpointResponseTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef,
    },
    total=False,
)


class ClientCreateRealtimeEndpointResponseTypeDef(
    _ClientCreateRealtimeEndpointResponseTypeDef
):
    """
    Type definition for `ClientCreateRealtimeEndpoint` `Response`

    Represents the output of an ``CreateRealtimeEndpoint`` operation.

    The result contains the ``MLModelId`` and the endpoint information for the ``MLModel`` .

    .. note::

      The endpoint information includes the URI of the ``MLModel`` ; that is, the location to send
      online prediction requests for the specified ``MLModel`` .

    - **MLModelId** *(string) --*

      A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical
      to the value of the ``MLModelId`` in the request.

    - **RealtimeEndpointInfo** *(dict) --*

      The endpoint information of the ``MLModel``

      - **PeakRequestsPerSecond** *(integer) --*

        The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
        incoming requests per second.

      - **CreatedAt** *(datetime) --*

        The time that the request to create the real-time endpoint for the ``MLModel`` was
        received. The time is expressed in epoch time.

      - **EndpointUrl** *(string) --*

        The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

        .. note::

          Note

          The application must wait until the real-time endpoint is ready before using this URI.

      - **EndpointStatus** *(string) --*

        The current status of the real-time endpoint for the ``MLModel`` . This element can have
        one of the following values:

        * ``NONE`` - Endpoint does not exist or was previously deleted.

        * ``READY`` - Endpoint is ready to be used for real-time predictions.

        * ``UPDATING`` - Updating/creating the endpoint.
    """


_ClientDeleteBatchPredictionResponseTypeDef = TypedDict(
    "_ClientDeleteBatchPredictionResponseTypeDef",
    {"BatchPredictionId": str},
    total=False,
)


class ClientDeleteBatchPredictionResponseTypeDef(
    _ClientDeleteBatchPredictionResponseTypeDef
):
    """
    Type definition for `ClientDeleteBatchPrediction` `Response`

    Represents the output of a ``DeleteBatchPrediction`` operation.

    You can use the ``GetBatchPrediction`` operation and check the value of the ``Status``
    parameter to see whether a ``BatchPrediction`` is marked as ``DELETED`` .

    - **BatchPredictionId** *(string) --*

      A user-supplied ID that uniquely identifies the ``BatchPrediction`` . This value should be
      identical to the value of the ``BatchPredictionID`` in the request.
    """


_ClientDeleteDataSourceResponseTypeDef = TypedDict(
    "_ClientDeleteDataSourceResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientDeleteDataSourceResponseTypeDef(_ClientDeleteDataSourceResponseTypeDef):
    """
    Type definition for `ClientDeleteDataSource` `Response`

    Represents the output of a ``DeleteDataSource`` operation.

    - **DataSourceId** *(string) --*

      A user-supplied ID that uniquely identifies the ``DataSource`` . This value should be
      identical to the value of the ``DataSourceID`` in the request.
    """


_ClientDeleteEvaluationResponseTypeDef = TypedDict(
    "_ClientDeleteEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)


class ClientDeleteEvaluationResponseTypeDef(_ClientDeleteEvaluationResponseTypeDef):
    """
    Type definition for `ClientDeleteEvaluation` `Response`

    Represents the output of a ``DeleteEvaluation`` operation. The output indicates that Amazon
    Machine Learning (Amazon ML) received the request.

    You can use the ``GetEvaluation`` operation and check the value of the ``Status`` parameter to
    see whether an ``Evaluation`` is marked as ``DELETED`` .

    - **EvaluationId** *(string) --*

      A user-supplied ID that uniquely identifies the ``Evaluation`` . This value should be
      identical to the value of the ``EvaluationId`` in the request.
    """


_ClientDeleteMlModelResponseTypeDef = TypedDict(
    "_ClientDeleteMlModelResponseTypeDef", {"MLModelId": str}, total=False
)


class ClientDeleteMlModelResponseTypeDef(_ClientDeleteMlModelResponseTypeDef):
    """
    Type definition for `ClientDeleteMlModel` `Response`

    Represents the output of a ``DeleteMLModel`` operation.

    You can use the ``GetMLModel`` operation and check the value of the ``Status`` parameter to see
    whether an ``MLModel`` is marked as ``DELETED`` .

    - **MLModelId** *(string) --*

      A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical
      to the value of the ``MLModelID`` in the request.
    """


_ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef = TypedDict(
    "_ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": str,
    },
    total=False,
)


class ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef(
    _ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef
):
    """
    Type definition for `ClientDeleteRealtimeEndpointResponse` `RealtimeEndpointInfo`

    The endpoint information of the ``MLModel``

    - **PeakRequestsPerSecond** *(integer) --*

      The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
      incoming requests per second.

    - **CreatedAt** *(datetime) --*

      The time that the request to create the real-time endpoint for the ``MLModel`` was
      received. The time is expressed in epoch time.

    - **EndpointUrl** *(string) --*

      The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

      .. note::

        Note

        The application must wait until the real-time endpoint is ready before using this URI.

    - **EndpointStatus** *(string) --*

      The current status of the real-time endpoint for the ``MLModel`` . This element can have
      one of the following values:

      * ``NONE`` - Endpoint does not exist or was previously deleted.

      * ``READY`` - Endpoint is ready to be used for real-time predictions.

      * ``UPDATING`` - Updating/creating the endpoint.
    """


_ClientDeleteRealtimeEndpointResponseTypeDef = TypedDict(
    "_ClientDeleteRealtimeEndpointResponseTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef,
    },
    total=False,
)


class ClientDeleteRealtimeEndpointResponseTypeDef(
    _ClientDeleteRealtimeEndpointResponseTypeDef
):
    """
    Type definition for `ClientDeleteRealtimeEndpoint` `Response`

    Represents the output of an ``DeleteRealtimeEndpoint`` operation.

    The result contains the ``MLModelId`` and the endpoint information for the ``MLModel`` .

    - **MLModelId** *(string) --*

      A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical
      to the value of the ``MLModelId`` in the request.

    - **RealtimeEndpointInfo** *(dict) --*

      The endpoint information of the ``MLModel``

      - **PeakRequestsPerSecond** *(integer) --*

        The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
        incoming requests per second.

      - **CreatedAt** *(datetime) --*

        The time that the request to create the real-time endpoint for the ``MLModel`` was
        received. The time is expressed in epoch time.

      - **EndpointUrl** *(string) --*

        The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

        .. note::

          Note

          The application must wait until the real-time endpoint is ready before using this URI.

      - **EndpointStatus** *(string) --*

        The current status of the real-time endpoint for the ``MLModel`` . This element can have
        one of the following values:

        * ``NONE`` - Endpoint does not exist or was previously deleted.

        * ``READY`` - Endpoint is ready to be used for real-time predictions.

        * ``UPDATING`` - Updating/creating the endpoint.
    """


_ClientDeleteTagsResponseTypeDef = TypedDict(
    "_ClientDeleteTagsResponseTypeDef",
    {"ResourceId": str, "ResourceType": str},
    total=False,
)


class ClientDeleteTagsResponseTypeDef(_ClientDeleteTagsResponseTypeDef):
    """
    Type definition for `ClientDeleteTags` `Response`

    Amazon ML returns the following elements.

    - **ResourceId** *(string) --*

      The ID of the ML object from which tags were deleted.

    - **ResourceType** *(string) --*

      The type of the ML object from which tags were deleted.
    """


_ClientDescribeBatchPredictionsResponseResultsTypeDef = TypedDict(
    "_ClientDescribeBatchPredictionsResponseResultsTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "OutputUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)


class ClientDescribeBatchPredictionsResponseResultsTypeDef(
    _ClientDescribeBatchPredictionsResponseResultsTypeDef
):
    """
    Type definition for `ClientDescribeBatchPredictionsResponse` `Results`

    Represents the output of a ``GetBatchPrediction`` operation.

    The content consists of the detailed metadata, the status, and the data file information of
    a ``Batch Prediction`` .

    - **BatchPredictionId** *(string) --*

      The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to
      the value of the ``BatchPredictionID`` in the request.

    - **MLModelId** *(string) --*

      The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.

    - **BatchPredictionDataSourceId** *(string) --*

      The ID of the ``DataSource`` that points to the group of observations to predict.

    - **InputDataLocationS3** *(string) --*

      The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

    - **CreatedByIamUser** *(string) --*

      The AWS user account that invoked the ``BatchPrediction`` . The account type can be
      either an AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``BatchPrediction`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in
      epoch time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``BatchPrediction`` .

    - **Status** *(string) --*

      The status of the ``BatchPrediction`` . This element can have one of the following values:

      * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate
      predictions for a batch of observations.

      * ``INPROGRESS`` - The process is underway.

      * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is
      not usable.

      * ``COMPLETED`` - The batch prediction process completed successfully.

      * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.

    - **OutputUri** *(string) --*

      The location of an Amazon S3 bucket or directory to receive the operation results. The
      following substrings are not allowed in the ``s3 key`` portion of the ``outputURI``
      field: ':', '//', '/./', '/../'.

    - **Message** *(string) --*

      A description of the most recent details about processing the batch prediction request.

    - **ComputeTime** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **FinishedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **StartedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **TotalRecordCount** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **InvalidRecordCount** *(integer) --*

      Long integer type that is a 64-bit signed number.
    """


_ClientDescribeBatchPredictionsResponseTypeDef = TypedDict(
    "_ClientDescribeBatchPredictionsResponseTypeDef",
    {
        "Results": List[ClientDescribeBatchPredictionsResponseResultsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeBatchPredictionsResponseTypeDef(
    _ClientDescribeBatchPredictionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeBatchPredictions` `Response`

    Represents the output of a ``DescribeBatchPredictions`` operation. The content is essentially a
    list of ``BatchPrediction`` s.

    - **Results** *(list) --*

      A list of ``BatchPrediction`` objects that meet the search criteria.

      - *(dict) --*

        Represents the output of a ``GetBatchPrediction`` operation.

        The content consists of the detailed metadata, the status, and the data file information of
        a ``Batch Prediction`` .

        - **BatchPredictionId** *(string) --*

          The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to
          the value of the ``BatchPredictionID`` in the request.

        - **MLModelId** *(string) --*

          The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.

        - **BatchPredictionDataSourceId** *(string) --*

          The ID of the ``DataSource`` that points to the group of observations to predict.

        - **InputDataLocationS3** *(string) --*

          The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

        - **CreatedByIamUser** *(string) --*

          The AWS user account that invoked the ``BatchPrediction`` . The account type can be
          either an AWS root account or an AWS Identity and Access Management (IAM) user account.

        - **CreatedAt** *(datetime) --*

          The time that the ``BatchPrediction`` was created. The time is expressed in epoch time.

        - **LastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in
          epoch time.

        - **Name** *(string) --*

          A user-supplied name or description of the ``BatchPrediction`` .

        - **Status** *(string) --*

          The status of the ``BatchPrediction`` . This element can have one of the following values:

          * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate
          predictions for a batch of observations.

          * ``INPROGRESS`` - The process is underway.

          * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is
          not usable.

          * ``COMPLETED`` - The batch prediction process completed successfully.

          * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.

        - **OutputUri** *(string) --*

          The location of an Amazon S3 bucket or directory to receive the operation results. The
          following substrings are not allowed in the ``s3 key`` portion of the ``outputURI``
          field: ':', '//', '/./', '/../'.

        - **Message** *(string) --*

          A description of the most recent details about processing the batch prediction request.

        - **ComputeTime** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **FinishedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **StartedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **TotalRecordCount** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **InvalidRecordCount** *(integer) --*

          Long integer type that is a 64-bit signed number.

    - **NextToken** *(string) --*

      The ID of the next page in the paginated results that indicates at least one more page
      follows.
    """


_ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)


class ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef(
    _ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef
):
    """
    Type definition for `ClientDescribeDataSourcesResponseResultsRDSMetadata` `Database`

    The database details required to connect to an Amazon RDS.

    - **InstanceIdentifier** *(string) --*

      The ID of an RDS DB instance.

    - **DatabaseName** *(string) --*

      The name of a database hosted on an RDS DB instance.
    """


_ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef",
    {
        "Database": ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "DataPipelineId": str,
    },
    total=False,
)


class ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef(
    _ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef
):
    """
    Type definition for `ClientDescribeDataSourcesResponseResults` `RDSMetadata`

    The datasource details that are specific to Amazon RDS.

    - **Database** *(dict) --*

      The database details required to connect to an Amazon RDS.

      - **InstanceIdentifier** *(string) --*

        The ID of an RDS DB instance.

      - **DatabaseName** *(string) --*

        The name of a database hosted on an RDS DB instance.

    - **DatabaseUserName** *(string) --*

      The username to be used by Amazon ML to connect to database on an Amazon RDS instance.
      The username should have sufficient permissions to execute an ``RDSSelectSqlQuery``
      query.

    - **SelectSqlQuery** *(string) --*

      The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if
      ``Verbose`` is true in ``GetDataSourceInput`` .

    - **ResourceRole** *(string) --*

      The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry
      out the copy task from Amazon RDS to Amazon S3. For more information, see `Role
      templates
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
      for data pipelines.

    - **ServiceRole** *(string) --*

      The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the
      progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role
      templates
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
      for data pipelines.

    - **DataPipelineId** *(string) --*

      The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS
      to Amazon S3. You can use the ID to find details about the instance in the Data
      Pipeline console.
    """


_ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)


class ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef(
    _ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef
):
    """
    Type definition for `ClientDescribeDataSourcesResponseResultsRedshiftMetadata` `RedshiftDatabase`

    Describes the database details required to connect to an Amazon Redshift database.

    - **DatabaseName** *(string) --*

      The name of a database hosted on an Amazon Redshift cluster.

    - **ClusterIdentifier** *(string) --*

      The ID of an Amazon Redshift cluster.
    """


_ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)


class ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef(
    _ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef
):
    """
    Type definition for `ClientDescribeDataSourcesResponseResults` `RedshiftMetadata`

    Describes the ``DataSource`` details specific to Amazon Redshift.

    - **RedshiftDatabase** *(dict) --*

      Describes the database details required to connect to an Amazon Redshift database.

      - **DatabaseName** *(string) --*

        The name of a database hosted on an Amazon Redshift cluster.

      - **ClusterIdentifier** *(string) --*

        The ID of an Amazon Redshift cluster.

    - **DatabaseUserName** *(string) --*

      A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on
      an Amazon Redshift cluster. The username should have sufficient permissions to execute
      the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon
      Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

    - **SelectSqlQuery** *(string) --*

      The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if
      ``Verbose`` is true in GetDataSourceInput.
    """


_ClientDescribeDataSourcesResponseResultsTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": str,
        "Message": str,
        "RedshiftMetadata": ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef,
        "RDSMetadata": ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef,
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class ClientDescribeDataSourcesResponseResultsTypeDef(
    _ClientDescribeDataSourcesResponseResultsTypeDef
):
    """
    Type definition for `ClientDescribeDataSourcesResponse` `Results`

    Represents the output of the ``GetDataSource`` operation.

    The content consists of the detailed metadata and data file information and the current
    status of the ``DataSource`` .

    - **DataSourceId** *(string) --*

      The ID that is assigned to the ``DataSource`` during creation.

    - **DataLocationS3** *(string) --*

      The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is
      used by a ``DataSource`` .

    - **DataRearrangement** *(string) --*

      A JSON string that represents the splitting and rearrangement requirement used when this
      ``DataSource`` was created.

    - **CreatedByIamUser** *(string) --*

      The AWS user account from which the ``DataSource`` was created. The account type can be
      either an AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``DataSource`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in
      epoch time.

    - **DataSizeInBytes** *(integer) --*

      The total number of observations contained in the data files that the ``DataSource``
      references.

    - **NumberOfFiles** *(integer) --*

      The number of data files referenced by the ``DataSource`` .

    - **Name** *(string) --*

      A user-supplied name or description of the ``DataSource`` .

    - **Status** *(string) --*

      The current status of the ``DataSource`` . This element can have one of the following
      values:

      * PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a
      ``DataSource`` .

      * INPROGRESS - The creation process is underway.

      * FAILED - The request to create a ``DataSource`` did not run to completion. It is not
      usable.

      * COMPLETED - The creation process completed successfully.

      * DELETED - The ``DataSource`` is marked as deleted. It is not usable.

    - **Message** *(string) --*

      A description of the most recent details about creating the ``DataSource`` .

    - **RedshiftMetadata** *(dict) --*

      Describes the ``DataSource`` details specific to Amazon Redshift.

      - **RedshiftDatabase** *(dict) --*

        Describes the database details required to connect to an Amazon Redshift database.

        - **DatabaseName** *(string) --*

          The name of a database hosted on an Amazon Redshift cluster.

        - **ClusterIdentifier** *(string) --*

          The ID of an Amazon Redshift cluster.

      - **DatabaseUserName** *(string) --*

        A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on
        an Amazon Redshift cluster. The username should have sufficient permissions to execute
        the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon
        Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

      - **SelectSqlQuery** *(string) --*

        The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if
        ``Verbose`` is true in GetDataSourceInput.

    - **RDSMetadata** *(dict) --*

      The datasource details that are specific to Amazon RDS.

      - **Database** *(dict) --*

        The database details required to connect to an Amazon RDS.

        - **InstanceIdentifier** *(string) --*

          The ID of an RDS DB instance.

        - **DatabaseName** *(string) --*

          The name of a database hosted on an RDS DB instance.

      - **DatabaseUserName** *(string) --*

        The username to be used by Amazon ML to connect to database on an Amazon RDS instance.
        The username should have sufficient permissions to execute an ``RDSSelectSqlQuery``
        query.

      - **SelectSqlQuery** *(string) --*

        The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if
        ``Verbose`` is true in ``GetDataSourceInput`` .

      - **ResourceRole** *(string) --*

        The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry
        out the copy task from Amazon RDS to Amazon S3. For more information, see `Role
        templates
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
        for data pipelines.

      - **ServiceRole** *(string) --*

        The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the
        progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role
        templates
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
        for data pipelines.

      - **DataPipelineId** *(string) --*

        The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS
        to Amazon S3. You can use the ID to find details about the instance in the Data
        Pipeline console.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of an `AWS IAM Role
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__
      , such as the following: arn:aws:iam::account:role/rolename.

    - **ComputeStatistics** *(boolean) --*

      The parameter is ``true`` if statistics need to be generated from the observation data.

    - **ComputeTime** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **FinishedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **StartedAt** *(datetime) --*

      A timestamp represented in epoch time.
    """


_ClientDescribeDataSourcesResponseTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseTypeDef",
    {
        "Results": List[ClientDescribeDataSourcesResponseResultsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDataSourcesResponseTypeDef(
    _ClientDescribeDataSourcesResponseTypeDef
):
    """
    Type definition for `ClientDescribeDataSources` `Response`

    Represents the query results from a  DescribeDataSources operation. The content is essentially
    a list of ``DataSource`` .

    - **Results** *(list) --*

      A list of ``DataSource`` that meet the search criteria.

      - *(dict) --*

        Represents the output of the ``GetDataSource`` operation.

        The content consists of the detailed metadata and data file information and the current
        status of the ``DataSource`` .

        - **DataSourceId** *(string) --*

          The ID that is assigned to the ``DataSource`` during creation.

        - **DataLocationS3** *(string) --*

          The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is
          used by a ``DataSource`` .

        - **DataRearrangement** *(string) --*

          A JSON string that represents the splitting and rearrangement requirement used when this
          ``DataSource`` was created.

        - **CreatedByIamUser** *(string) --*

          The AWS user account from which the ``DataSource`` was created. The account type can be
          either an AWS root account or an AWS Identity and Access Management (IAM) user account.

        - **CreatedAt** *(datetime) --*

          The time that the ``DataSource`` was created. The time is expressed in epoch time.

        - **LastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in
          epoch time.

        - **DataSizeInBytes** *(integer) --*

          The total number of observations contained in the data files that the ``DataSource``
          references.

        - **NumberOfFiles** *(integer) --*

          The number of data files referenced by the ``DataSource`` .

        - **Name** *(string) --*

          A user-supplied name or description of the ``DataSource`` .

        - **Status** *(string) --*

          The current status of the ``DataSource`` . This element can have one of the following
          values:

          * PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a
          ``DataSource`` .

          * INPROGRESS - The creation process is underway.

          * FAILED - The request to create a ``DataSource`` did not run to completion. It is not
          usable.

          * COMPLETED - The creation process completed successfully.

          * DELETED - The ``DataSource`` is marked as deleted. It is not usable.

        - **Message** *(string) --*

          A description of the most recent details about creating the ``DataSource`` .

        - **RedshiftMetadata** *(dict) --*

          Describes the ``DataSource`` details specific to Amazon Redshift.

          - **RedshiftDatabase** *(dict) --*

            Describes the database details required to connect to an Amazon Redshift database.

            - **DatabaseName** *(string) --*

              The name of a database hosted on an Amazon Redshift cluster.

            - **ClusterIdentifier** *(string) --*

              The ID of an Amazon Redshift cluster.

          - **DatabaseUserName** *(string) --*

            A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on
            an Amazon Redshift cluster. The username should have sufficient permissions to execute
            the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon
            Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

          - **SelectSqlQuery** *(string) --*

            The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if
            ``Verbose`` is true in GetDataSourceInput.

        - **RDSMetadata** *(dict) --*

          The datasource details that are specific to Amazon RDS.

          - **Database** *(dict) --*

            The database details required to connect to an Amazon RDS.

            - **InstanceIdentifier** *(string) --*

              The ID of an RDS DB instance.

            - **DatabaseName** *(string) --*

              The name of a database hosted on an RDS DB instance.

          - **DatabaseUserName** *(string) --*

            The username to be used by Amazon ML to connect to database on an Amazon RDS instance.
            The username should have sufficient permissions to execute an ``RDSSelectSqlQuery``
            query.

          - **SelectSqlQuery** *(string) --*

            The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if
            ``Verbose`` is true in ``GetDataSourceInput`` .

          - **ResourceRole** *(string) --*

            The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry
            out the copy task from Amazon RDS to Amazon S3. For more information, see `Role
            templates
            <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
            for data pipelines.

          - **ServiceRole** *(string) --*

            The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the
            progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role
            templates
            <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
            for data pipelines.

          - **DataPipelineId** *(string) --*

            The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS
            to Amazon S3. You can use the ID to find details about the instance in the Data
            Pipeline console.

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of an `AWS IAM Role
          <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__
          , such as the following: arn:aws:iam::account:role/rolename.

        - **ComputeStatistics** *(boolean) --*

          The parameter is ``true`` if statistics need to be generated from the observation data.

        - **ComputeTime** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **FinishedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **StartedAt** *(datetime) --*

          A timestamp represented in epoch time.

    - **NextToken** *(string) --*

      An ID of the next page in the paginated results that indicates at least one more page follows.
    """


_ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef = TypedDict(
    "_ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)


class ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef(
    _ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef
):
    """
    Type definition for `ClientDescribeEvaluationsResponseResults` `PerformanceMetrics`

    Measurements of how well the ``MLModel`` performed, using observations referenced by the
    ``DataSource`` . One of the following metrics is returned, based on the type of the
    ``MLModel`` :

    * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to
    measure performance.

    * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE)
    technique to measure performance. RMSE measures the difference between predicted and
    actual values for a single variable.

    * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure
    performance.

    For more information about performance metrics, please see the `Amazon Machine Learning
    Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

    - **Properties** *(dict) --*

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeEvaluationsResponseResultsTypeDef = TypedDict(
    "_ClientDescribeEvaluationsResponseResultsTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "PerformanceMetrics": ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class ClientDescribeEvaluationsResponseResultsTypeDef(
    _ClientDescribeEvaluationsResponseResultsTypeDef
):
    """
    Type definition for `ClientDescribeEvaluationsResponse` `Results`

    Represents the output of ``GetEvaluation`` operation.

    The content consists of the detailed metadata and data file information and the current
    status of the ``Evaluation`` .

    - **EvaluationId** *(string) --*

      The ID that is assigned to the ``Evaluation`` at creation.

    - **MLModelId** *(string) --*

      The ID of the ``MLModel`` that is the focus of the evaluation.

    - **EvaluationDataSourceId** *(string) --*

      The ID of the ``DataSource`` that is used to evaluate the ``MLModel`` .

    - **InputDataLocationS3** *(string) --*

      The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is
      used in the evaluation.

    - **CreatedByIamUser** *(string) --*

      The AWS user account that invoked the evaluation. The account type can be either an AWS
      root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``Evaluation`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch
      time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``Evaluation`` .

    - **Status** *(string) --*

      The status of the evaluation. This element can have one of the following values:

      * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an
      ``MLModel`` .

      * ``INPROGRESS`` - The evaluation is underway.

      * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is
      not usable.

      * ``COMPLETED`` - The evaluation process completed successfully.

      * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.

    - **PerformanceMetrics** *(dict) --*

      Measurements of how well the ``MLModel`` performed, using observations referenced by the
      ``DataSource`` . One of the following metrics is returned, based on the type of the
      ``MLModel`` :

      * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to
      measure performance.

      * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE)
      technique to measure performance. RMSE measures the difference between predicted and
      actual values for a single variable.

      * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure
      performance.

      For more information about performance metrics, please see the `Amazon Machine Learning
      Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

      - **Properties** *(dict) --*

        - *(string) --*

          - *(string) --*

    - **Message** *(string) --*

      A description of the most recent details about evaluating the ``MLModel`` .

    - **ComputeTime** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **FinishedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **StartedAt** *(datetime) --*

      A timestamp represented in epoch time.
    """


_ClientDescribeEvaluationsResponseTypeDef = TypedDict(
    "_ClientDescribeEvaluationsResponseTypeDef",
    {
        "Results": List[ClientDescribeEvaluationsResponseResultsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeEvaluationsResponseTypeDef(
    _ClientDescribeEvaluationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEvaluations` `Response`

    Represents the query results from a ``DescribeEvaluations`` operation. The content is
    essentially a list of ``Evaluation`` .

    - **Results** *(list) --*

      A list of ``Evaluation`` that meet the search criteria.

      - *(dict) --*

        Represents the output of ``GetEvaluation`` operation.

        The content consists of the detailed metadata and data file information and the current
        status of the ``Evaluation`` .

        - **EvaluationId** *(string) --*

          The ID that is assigned to the ``Evaluation`` at creation.

        - **MLModelId** *(string) --*

          The ID of the ``MLModel`` that is the focus of the evaluation.

        - **EvaluationDataSourceId** *(string) --*

          The ID of the ``DataSource`` that is used to evaluate the ``MLModel`` .

        - **InputDataLocationS3** *(string) --*

          The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is
          used in the evaluation.

        - **CreatedByIamUser** *(string) --*

          The AWS user account that invoked the evaluation. The account type can be either an AWS
          root account or an AWS Identity and Access Management (IAM) user account.

        - **CreatedAt** *(datetime) --*

          The time that the ``Evaluation`` was created. The time is expressed in epoch time.

        - **LastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch
          time.

        - **Name** *(string) --*

          A user-supplied name or description of the ``Evaluation`` .

        - **Status** *(string) --*

          The status of the evaluation. This element can have one of the following values:

          * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an
          ``MLModel`` .

          * ``INPROGRESS`` - The evaluation is underway.

          * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is
          not usable.

          * ``COMPLETED`` - The evaluation process completed successfully.

          * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.

        - **PerformanceMetrics** *(dict) --*

          Measurements of how well the ``MLModel`` performed, using observations referenced by the
          ``DataSource`` . One of the following metrics is returned, based on the type of the
          ``MLModel`` :

          * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to
          measure performance.

          * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE)
          technique to measure performance. RMSE measures the difference between predicted and
          actual values for a single variable.

          * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure
          performance.

          For more information about performance metrics, please see the `Amazon Machine Learning
          Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

          - **Properties** *(dict) --*

            - *(string) --*

              - *(string) --*

        - **Message** *(string) --*

          A description of the most recent details about evaluating the ``MLModel`` .

        - **ComputeTime** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **FinishedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **StartedAt** *(datetime) --*

          A timestamp represented in epoch time.

    - **NextToken** *(string) --*

      The ID of the next page in the paginated results that indicates at least one more page
      follows.
    """


_ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef = TypedDict(
    "_ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": str,
    },
    total=False,
)


class ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef(
    _ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef
):
    """
    Type definition for `ClientDescribeMlModelsResponseResults` `EndpointInfo`

    The current endpoint of the ``MLModel`` .

    - **PeakRequestsPerSecond** *(integer) --*

      The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
      incoming requests per second.

    - **CreatedAt** *(datetime) --*

      The time that the request to create the real-time endpoint for the ``MLModel`` was
      received. The time is expressed in epoch time.

    - **EndpointUrl** *(string) --*

      The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

      .. note::

        Note

        The application must wait until the real-time endpoint is ready before using this URI.

    - **EndpointStatus** *(string) --*

      The current status of the real-time endpoint for the ``MLModel`` . This element can
      have one of the following values:

      * ``NONE`` - Endpoint does not exist or was previously deleted.

      * ``READY`` - Endpoint is ready to be used for real-time predictions.

      * ``UPDATING`` - Updating/creating the endpoint.
    """


_ClientDescribeMlModelsResponseResultsTypeDef = TypedDict(
    "_ClientDescribeMlModelsResponseResultsTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "SizeInBytes": int,
        "EndpointInfo": ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef,
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "Algorithm": str,
        "MLModelType": str,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class ClientDescribeMlModelsResponseResultsTypeDef(
    _ClientDescribeMlModelsResponseResultsTypeDef
):
    """
    Type definition for `ClientDescribeMlModelsResponse` `Results`

    Represents the output of a ``GetMLModel`` operation.

    The content consists of the detailed metadata and the current status of the ``MLModel`` .

    - **MLModelId** *(string) --*

      The ID assigned to the ``MLModel`` at creation.

    - **TrainingDataSourceId** *(string) --*

      The ID of the training ``DataSource`` . The ``CreateMLModel`` operation uses the
      ``TrainingDataSourceId`` .

    - **CreatedByIamUser** *(string) --*

      The AWS user account from which the ``MLModel`` was created. The account type can be
      either an AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``MLModel`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``MLModel`` .

    - **Status** *(string) --*

      The current status of an ``MLModel`` . This element can have one of the following values:

      * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to create an
      ``MLModel`` .

      * ``INPROGRESS`` - The creation process is underway.

      * ``FAILED`` - The request to create an ``MLModel`` didn't run to completion. The model
      isn't usable.

      * ``COMPLETED`` - The creation process completed successfully.

      * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn't usable.

    - **SizeInBytes** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **EndpointInfo** *(dict) --*

      The current endpoint of the ``MLModel`` .

      - **PeakRequestsPerSecond** *(integer) --*

        The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
        incoming requests per second.

      - **CreatedAt** *(datetime) --*

        The time that the request to create the real-time endpoint for the ``MLModel`` was
        received. The time is expressed in epoch time.

      - **EndpointUrl** *(string) --*

        The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

        .. note::

          Note

          The application must wait until the real-time endpoint is ready before using this URI.

      - **EndpointStatus** *(string) --*

        The current status of the real-time endpoint for the ``MLModel`` . This element can
        have one of the following values:

        * ``NONE`` - Endpoint does not exist or was previously deleted.

        * ``READY`` - Endpoint is ready to be used for real-time predictions.

        * ``UPDATING`` - Updating/creating the endpoint.

    - **TrainingParameters** *(dict) --*

      A list of the training parameters in the ``MLModel`` . The list is implemented as a map
      of key-value pairs.

      The following is the current set of training parameters:

      * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the
      input data, the size of the model might affect its performance. The value is an integer
      that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` .

      * ``sgd.maxPasses`` - The number of times that the training process traverses the
      observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to
      ``10000`` . The default value is ``10`` .

      * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling the data
      improves a model's ability to find the optimal solution for a variety of data types. The
      valid values are ``auto`` and ``none`` . The default value is ``none`` .

      * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm, which controls
      overfitting the data by penalizing large coefficients. This parameter tends to drive
      coefficients to zero, resulting in sparse feature set. If you use this parameter, start
      by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from
      ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter
      can't be used when ``L2`` is specified. Use this parameter sparingly.

      * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm, which controls
      overfitting the data by penalizing large coefficients. This tends to drive coefficients
      to small, nonzero values. If you use this parameter, start by specifying a small value,
      such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` .
      The default is to not use L2 normalization. This parameter can't be used when ``L1`` is
      specified. Use this parameter sparingly.

      - *(string) --*

        String type.

        - *(string) --*

          String type.

    - **InputDataLocationS3** *(string) --*

      The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

    - **Algorithm** *(string) --*

      The algorithm used to train the ``MLModel`` . The following algorithm is supported:

      * ``SGD`` -- Stochastic gradient descent. The goal of ``SGD`` is to minimize the gradient
      of the loss function.

    - **MLModelType** *(string) --*

      Identifies the ``MLModel`` category. The following are the available types:

      * ``REGRESSION`` - Produces a numeric result. For example, "What price should a house be
      listed at?"

      * ``BINARY`` - Produces one of two possible results. For example, "Is this a
      child-friendly web site?".

      * ``MULTICLASS`` - Produces one of several possible results. For example, "Is this a
      HIGH-, LOW-, or MEDIUM-risk trade?".

    - **ScoreThreshold** *(float) --*

    - **ScoreThresholdLastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in
      epoch time.

    - **Message** *(string) --*

      A description of the most recent details about accessing the ``MLModel`` .

    - **ComputeTime** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **FinishedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **StartedAt** *(datetime) --*

      A timestamp represented in epoch time.
    """


_ClientDescribeMlModelsResponseTypeDef = TypedDict(
    "_ClientDescribeMlModelsResponseTypeDef",
    {"Results": List[ClientDescribeMlModelsResponseResultsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeMlModelsResponseTypeDef(_ClientDescribeMlModelsResponseTypeDef):
    """
    Type definition for `ClientDescribeMlModels` `Response`

    Represents the output of a ``DescribeMLModels`` operation. The content is essentially a list of
    ``MLModel`` .

    - **Results** *(list) --*

      A list of ``MLModel`` that meet the search criteria.

      - *(dict) --*

        Represents the output of a ``GetMLModel`` operation.

        The content consists of the detailed metadata and the current status of the ``MLModel`` .

        - **MLModelId** *(string) --*

          The ID assigned to the ``MLModel`` at creation.

        - **TrainingDataSourceId** *(string) --*

          The ID of the training ``DataSource`` . The ``CreateMLModel`` operation uses the
          ``TrainingDataSourceId`` .

        - **CreatedByIamUser** *(string) --*

          The AWS user account from which the ``MLModel`` was created. The account type can be
          either an AWS root account or an AWS Identity and Access Management (IAM) user account.

        - **CreatedAt** *(datetime) --*

          The time that the ``MLModel`` was created. The time is expressed in epoch time.

        - **LastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.

        - **Name** *(string) --*

          A user-supplied name or description of the ``MLModel`` .

        - **Status** *(string) --*

          The current status of an ``MLModel`` . This element can have one of the following values:

          * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to create an
          ``MLModel`` .

          * ``INPROGRESS`` - The creation process is underway.

          * ``FAILED`` - The request to create an ``MLModel`` didn't run to completion. The model
          isn't usable.

          * ``COMPLETED`` - The creation process completed successfully.

          * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn't usable.

        - **SizeInBytes** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **EndpointInfo** *(dict) --*

          The current endpoint of the ``MLModel`` .

          - **PeakRequestsPerSecond** *(integer) --*

            The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
            incoming requests per second.

          - **CreatedAt** *(datetime) --*

            The time that the request to create the real-time endpoint for the ``MLModel`` was
            received. The time is expressed in epoch time.

          - **EndpointUrl** *(string) --*

            The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

            .. note::

              Note

              The application must wait until the real-time endpoint is ready before using this URI.

          - **EndpointStatus** *(string) --*

            The current status of the real-time endpoint for the ``MLModel`` . This element can
            have one of the following values:

            * ``NONE`` - Endpoint does not exist or was previously deleted.

            * ``READY`` - Endpoint is ready to be used for real-time predictions.

            * ``UPDATING`` - Updating/creating the endpoint.

        - **TrainingParameters** *(dict) --*

          A list of the training parameters in the ``MLModel`` . The list is implemented as a map
          of key-value pairs.

          The following is the current set of training parameters:

          * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the
          input data, the size of the model might affect its performance. The value is an integer
          that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` .

          * ``sgd.maxPasses`` - The number of times that the training process traverses the
          observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to
          ``10000`` . The default value is ``10`` .

          * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling the data
          improves a model's ability to find the optimal solution for a variety of data types. The
          valid values are ``auto`` and ``none`` . The default value is ``none`` .

          * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm, which controls
          overfitting the data by penalizing large coefficients. This parameter tends to drive
          coefficients to zero, resulting in sparse feature set. If you use this parameter, start
          by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from
          ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter
          can't be used when ``L2`` is specified. Use this parameter sparingly.

          * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm, which controls
          overfitting the data by penalizing large coefficients. This tends to drive coefficients
          to small, nonzero values. If you use this parameter, start by specifying a small value,
          such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` .
          The default is to not use L2 normalization. This parameter can't be used when ``L1`` is
          specified. Use this parameter sparingly.

          - *(string) --*

            String type.

            - *(string) --*

              String type.

        - **InputDataLocationS3** *(string) --*

          The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

        - **Algorithm** *(string) --*

          The algorithm used to train the ``MLModel`` . The following algorithm is supported:

          * ``SGD`` -- Stochastic gradient descent. The goal of ``SGD`` is to minimize the gradient
          of the loss function.

        - **MLModelType** *(string) --*

          Identifies the ``MLModel`` category. The following are the available types:

          * ``REGRESSION`` - Produces a numeric result. For example, "What price should a house be
          listed at?"

          * ``BINARY`` - Produces one of two possible results. For example, "Is this a
          child-friendly web site?".

          * ``MULTICLASS`` - Produces one of several possible results. For example, "Is this a
          HIGH-, LOW-, or MEDIUM-risk trade?".

        - **ScoreThreshold** *(float) --*

        - **ScoreThresholdLastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in
          epoch time.

        - **Message** *(string) --*

          A description of the most recent details about accessing the ``MLModel`` .

        - **ComputeTime** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **FinishedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **StartedAt** *(datetime) --*

          A timestamp represented in epoch time.

    - **NextToken** *(string) --*

      The ID of the next page in the paginated results that indicates at least one more page
      follows.
    """


_ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeTagsResponseTagsTypeDef(_ClientDescribeTagsResponseTagsTypeDef):
    """
    Type definition for `ClientDescribeTagsResponse` `Tags`

    A custom key-value pair associated with an ML object, such as an ML model.

    - **Key** *(string) --*

      A unique identifier for the tag. Valid characters include Unicode letters, digits, white
      space, _, ., /, =, +, -, %, and @.

    - **Value** *(string) --*

      An optional string, typically used to describe or define the tag. Valid characters
      include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "Tags": List[ClientDescribeTagsResponseTagsTypeDef],
    },
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    Type definition for `ClientDescribeTags` `Response`

    Amazon ML returns the following elements.

    - **ResourceId** *(string) --*

      The ID of the tagged ML object.

    - **ResourceType** *(string) --*

      The type of the tagged ML object.

    - **Tags** *(list) --*

      A list of tags associated with the ML object.

      - *(dict) --*

        A custom key-value pair associated with an ML object, such as an ML model.

        - **Key** *(string) --*

          A unique identifier for the tag. Valid characters include Unicode letters, digits, white
          space, _, ., /, =, +, -, %, and @.

        - **Value** *(string) --*

          An optional string, typically used to describe or define the tag. Valid characters
          include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.
    """


_ClientGetBatchPredictionResponseTypeDef = TypedDict(
    "_ClientGetBatchPredictionResponseTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "OutputUri": str,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)


class ClientGetBatchPredictionResponseTypeDef(_ClientGetBatchPredictionResponseTypeDef):
    """
    Type definition for `ClientGetBatchPrediction` `Response`

    Represents the output of a ``GetBatchPrediction`` operation and describes a ``BatchPrediction``
    .

    - **BatchPredictionId** *(string) --*

      An ID assigned to the ``BatchPrediction`` at creation. This value should be identical to the
      value of the ``BatchPredictionID`` in the request.

    - **MLModelId** *(string) --*

      The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.

    - **BatchPredictionDataSourceId** *(string) --*

      The ID of the ``DataSource`` that was used to create the ``BatchPrediction`` .

    - **InputDataLocationS3** *(string) --*

      The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

    - **CreatedByIamUser** *(string) --*

      The AWS user account that invoked the ``BatchPrediction`` . The account type can be either an
      AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time when the ``BatchPrediction`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to ``BatchPrediction`` . The time is expressed in epoch time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``BatchPrediction`` .

    - **Status** *(string) --*

      The status of the ``BatchPrediction`` , which can be one of the following values:

      * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate batch
      predictions.

      * ``INPROGRESS`` - The batch predictions are in progress.

      * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is not
      usable.

      * ``COMPLETED`` - The batch prediction process completed successfully.

      * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.

    - **OutputUri** *(string) --*

      The location of an Amazon S3 bucket or directory to receive the operation results.

    - **LogUri** *(string) --*

      A link to the file that contains logs of the ``CreateBatchPrediction`` operation.

    - **Message** *(string) --*

      A description of the most recent details about processing the batch prediction request.

    - **ComputeTime** *(integer) --*

      The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the
      ``BatchPrediction`` , normalized and scaled on computation resources. ``ComputeTime`` is only
      available if the ``BatchPrediction`` is in the ``COMPLETED`` state.

    - **FinishedAt** *(datetime) --*

      The epoch time when Amazon Machine Learning marked the ``BatchPrediction`` as ``COMPLETED``
      or ``FAILED`` . ``FinishedAt`` is only available when the ``BatchPrediction`` is in the
      ``COMPLETED`` or ``FAILED`` state.

    - **StartedAt** *(datetime) --*

      The epoch time when Amazon Machine Learning marked the ``BatchPrediction`` as ``INPROGRESS``
      . ``StartedAt`` isn't available if the ``BatchPrediction`` is in the ``PENDING`` state.

    - **TotalRecordCount** *(integer) --*

      The number of total records that Amazon Machine Learning saw while processing the
      ``BatchPrediction`` .

    - **InvalidRecordCount** *(integer) --*

      The number of invalid records that Amazon Machine Learning saw while processing the
      ``BatchPrediction`` .
    """


_ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef = TypedDict(
    "_ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)


class ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef(
    _ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef
):
    """
    Type definition for `ClientGetDataSourceResponseRDSMetadata` `Database`

    The database details required to connect to an Amazon RDS.

    - **InstanceIdentifier** *(string) --*

      The ID of an RDS DB instance.

    - **DatabaseName** *(string) --*

      The name of a database hosted on an RDS DB instance.
    """


_ClientGetDataSourceResponseRDSMetadataTypeDef = TypedDict(
    "_ClientGetDataSourceResponseRDSMetadataTypeDef",
    {
        "Database": ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "DataPipelineId": str,
    },
    total=False,
)


class ClientGetDataSourceResponseRDSMetadataTypeDef(
    _ClientGetDataSourceResponseRDSMetadataTypeDef
):
    """
    Type definition for `ClientGetDataSourceResponse` `RDSMetadata`

    The datasource details that are specific to Amazon RDS.

    - **Database** *(dict) --*

      The database details required to connect to an Amazon RDS.

      - **InstanceIdentifier** *(string) --*

        The ID of an RDS DB instance.

      - **DatabaseName** *(string) --*

        The name of a database hosted on an RDS DB instance.

    - **DatabaseUserName** *(string) --*

      The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The
      username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.

    - **SelectSqlQuery** *(string) --*

      The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if
      ``Verbose`` is true in ``GetDataSourceInput`` .

    - **ResourceRole** *(string) --*

      The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out
      the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for
      data pipelines.

    - **ServiceRole** *(string) --*

      The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the
      progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role
      templates
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for
      data pipelines.

    - **DataPipelineId** *(string) --*

      The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to
      Amazon S3. You can use the ID to find details about the instance in the Data Pipeline
      console.
    """


_ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "_ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)


class ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef(
    _ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef
):
    """
    Type definition for `ClientGetDataSourceResponseRedshiftMetadata` `RedshiftDatabase`

    Describes the database details required to connect to an Amazon Redshift database.

    - **DatabaseName** *(string) --*

      The name of a database hosted on an Amazon Redshift cluster.

    - **ClusterIdentifier** *(string) --*

      The ID of an Amazon Redshift cluster.
    """


_ClientGetDataSourceResponseRedshiftMetadataTypeDef = TypedDict(
    "_ClientGetDataSourceResponseRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)


class ClientGetDataSourceResponseRedshiftMetadataTypeDef(
    _ClientGetDataSourceResponseRedshiftMetadataTypeDef
):
    """
    Type definition for `ClientGetDataSourceResponse` `RedshiftMetadata`

    Describes the ``DataSource`` details specific to Amazon Redshift.

    - **RedshiftDatabase** *(dict) --*

      Describes the database details required to connect to an Amazon Redshift database.

      - **DatabaseName** *(string) --*

        The name of a database hosted on an Amazon Redshift cluster.

      - **ClusterIdentifier** *(string) --*

        The ID of an Amazon Redshift cluster.

    - **DatabaseUserName** *(string) --*

      A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an
      Amazon Redshift cluster. The username should have sufficient permissions to execute the
      ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER
      <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

    - **SelectSqlQuery** *(string) --*

      The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if
      ``Verbose`` is true in GetDataSourceInput.
    """


_ClientGetDataSourceResponseTypeDef = TypedDict(
    "_ClientGetDataSourceResponseTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": str,
        "LogUri": str,
        "Message": str,
        "RedshiftMetadata": ClientGetDataSourceResponseRedshiftMetadataTypeDef,
        "RDSMetadata": ClientGetDataSourceResponseRDSMetadataTypeDef,
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "DataSourceSchema": str,
    },
    total=False,
)


class ClientGetDataSourceResponseTypeDef(_ClientGetDataSourceResponseTypeDef):
    """
    Type definition for `ClientGetDataSource` `Response`

    Represents the output of a ``GetDataSource`` operation and describes a ``DataSource`` .

    - **DataSourceId** *(string) --*

      The ID assigned to the ``DataSource`` at creation. This value should be identical to the
      value of the ``DataSourceId`` in the request.

    - **DataLocationS3** *(string) --*

      The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

    - **DataRearrangement** *(string) --*

      A JSON string that represents the splitting and rearrangement requirement used when this
      ``DataSource`` was created.

    - **CreatedByIamUser** *(string) --*

      The AWS user account from which the ``DataSource`` was created. The account type can be
      either an AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``DataSource`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``DataSource`` . The time is expressed in epoch time.

    - **DataSizeInBytes** *(integer) --*

      The total size of observations in the data files.

    - **NumberOfFiles** *(integer) --*

      The number of data files referenced by the ``DataSource`` .

    - **Name** *(string) --*

      A user-supplied name or description of the ``DataSource`` .

    - **Status** *(string) --*

      The current status of the ``DataSource`` . This element can have one of the following values:

      * ``PENDING`` - Amazon ML submitted a request to create a ``DataSource`` .

      * ``INPROGRESS`` - The creation process is underway.

      * ``FAILED`` - The request to create a ``DataSource`` did not run to completion. It is not
      usable.

      * ``COMPLETED`` - The creation process completed successfully.

      * ``DELETED`` - The ``DataSource`` is marked as deleted. It is not usable.

    - **LogUri** *(string) --*

      A link to the file containing logs of ``CreateDataSourceFrom*`` operations.

    - **Message** *(string) --*

      The user-supplied description of the most recent details about creating the ``DataSource`` .

    - **RedshiftMetadata** *(dict) --*

      Describes the ``DataSource`` details specific to Amazon Redshift.

      - **RedshiftDatabase** *(dict) --*

        Describes the database details required to connect to an Amazon Redshift database.

        - **DatabaseName** *(string) --*

          The name of a database hosted on an Amazon Redshift cluster.

        - **ClusterIdentifier** *(string) --*

          The ID of an Amazon Redshift cluster.

      - **DatabaseUserName** *(string) --*

        A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an
        Amazon Redshift cluster. The username should have sufficient permissions to execute the
        ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER
        <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

      - **SelectSqlQuery** *(string) --*

        The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if
        ``Verbose`` is true in GetDataSourceInput.

    - **RDSMetadata** *(dict) --*

      The datasource details that are specific to Amazon RDS.

      - **Database** *(dict) --*

        The database details required to connect to an Amazon RDS.

        - **InstanceIdentifier** *(string) --*

          The ID of an RDS DB instance.

        - **DatabaseName** *(string) --*

          The name of a database hosted on an RDS DB instance.

      - **DatabaseUserName** *(string) --*

        The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The
        username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.

      - **SelectSqlQuery** *(string) --*

        The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if
        ``Verbose`` is true in ``GetDataSourceInput`` .

      - **ResourceRole** *(string) --*

        The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out
        the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for
        data pipelines.

      - **ServiceRole** *(string) --*

        The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the
        progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role
        templates
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for
        data pipelines.

      - **DataPipelineId** *(string) --*

        The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to
        Amazon S3. You can use the ID to find details about the instance in the Data Pipeline
        console.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of an `AWS IAM Role
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__
      , such as the following: arn:aws:iam::account:role/rolename.

    - **ComputeStatistics** *(boolean) --*

      The parameter is ``true`` if statistics need to be generated from the observation data.

    - **ComputeTime** *(integer) --*

      The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the
      ``DataSource`` , normalized and scaled on computation resources. ``ComputeTime`` is only
      available if the ``DataSource`` is in the ``COMPLETED`` state and the ``ComputeStatistics``
      is set to true.

    - **FinishedAt** *(datetime) --*

      The epoch time when Amazon Machine Learning marked the ``DataSource`` as ``COMPLETED`` or
      ``FAILED`` . ``FinishedAt`` is only available when the ``DataSource`` is in the ``COMPLETED``
      or ``FAILED`` state.

    - **StartedAt** *(datetime) --*

      The epoch time when Amazon Machine Learning marked the ``DataSource`` as ``INPROGRESS`` .
      ``StartedAt`` isn't available if the ``DataSource`` is in the ``PENDING`` state.

    - **DataSourceSchema** *(string) --*

      The schema used by all of the data files of this ``DataSource`` .

      .. note::

        Note

        This parameter is provided as part of the verbose format.
    """


_ClientGetEvaluationResponsePerformanceMetricsTypeDef = TypedDict(
    "_ClientGetEvaluationResponsePerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)


class ClientGetEvaluationResponsePerformanceMetricsTypeDef(
    _ClientGetEvaluationResponsePerformanceMetricsTypeDef
):
    """
    Type definition for `ClientGetEvaluationResponse` `PerformanceMetrics`

    Measurements of how well the ``MLModel`` performed using observations referenced by the
    ``DataSource`` . One of the following metric is returned based on the type of the ``MLModel``
    :

    * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to measure
    performance.

    * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE) technique
    to measure performance. RMSE measures the difference between predicted and actual values for
    a single variable.

    * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure
    performance.

    For more information about performance metrics, please see the `Amazon Machine Learning
    Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

    - **Properties** *(dict) --*

      - *(string) --*

        - *(string) --*
    """


_ClientGetEvaluationResponseTypeDef = TypedDict(
    "_ClientGetEvaluationResponseTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "PerformanceMetrics": ClientGetEvaluationResponsePerformanceMetricsTypeDef,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class ClientGetEvaluationResponseTypeDef(_ClientGetEvaluationResponseTypeDef):
    """
    Type definition for `ClientGetEvaluation` `Response`

    Represents the output of a ``GetEvaluation`` operation and describes an ``Evaluation`` .

    - **EvaluationId** *(string) --*

      The evaluation ID which is same as the ``EvaluationId`` in the request.

    - **MLModelId** *(string) --*

      The ID of the ``MLModel`` that was the focus of the evaluation.

    - **EvaluationDataSourceId** *(string) --*

      The ``DataSource`` used for this evaluation.

    - **InputDataLocationS3** *(string) --*

      The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

    - **CreatedByIamUser** *(string) --*

      The AWS user account that invoked the evaluation. The account type can be either an AWS root
      account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``Evaluation`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``Evaluation`` .

    - **Status** *(string) --*

      The status of the evaluation. This element can have one of the following values:

      * ``PENDING`` - Amazon Machine Language (Amazon ML) submitted a request to evaluate an
      ``MLModel`` .

      * ``INPROGRESS`` - The evaluation is underway.

      * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is not
      usable.

      * ``COMPLETED`` - The evaluation process completed successfully.

      * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.

    - **PerformanceMetrics** *(dict) --*

      Measurements of how well the ``MLModel`` performed using observations referenced by the
      ``DataSource`` . One of the following metric is returned based on the type of the ``MLModel``
      :

      * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to measure
      performance.

      * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE) technique
      to measure performance. RMSE measures the difference between predicted and actual values for
      a single variable.

      * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure
      performance.

      For more information about performance metrics, please see the `Amazon Machine Learning
      Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

      - **Properties** *(dict) --*

        - *(string) --*

          - *(string) --*

    - **LogUri** *(string) --*

      A link to the file that contains logs of the ``CreateEvaluation`` operation.

    - **Message** *(string) --*

      A description of the most recent details about evaluating the ``MLModel`` .

    - **ComputeTime** *(integer) --*

      The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the
      ``Evaluation`` , normalized and scaled on computation resources. ``ComputeTime`` is only
      available if the ``Evaluation`` is in the ``COMPLETED`` state.

    - **FinishedAt** *(datetime) --*

      The epoch time when Amazon Machine Learning marked the ``Evaluation`` as ``COMPLETED`` or
      ``FAILED`` . ``FinishedAt`` is only available when the ``Evaluation`` is in the ``COMPLETED``
      or ``FAILED`` state.

    - **StartedAt** *(datetime) --*

      The epoch time when Amazon Machine Learning marked the ``Evaluation`` as ``INPROGRESS`` .
      ``StartedAt`` isn't available if the ``Evaluation`` is in the ``PENDING`` state.
    """


_ClientGetMlModelResponseEndpointInfoTypeDef = TypedDict(
    "_ClientGetMlModelResponseEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": str,
    },
    total=False,
)


class ClientGetMlModelResponseEndpointInfoTypeDef(
    _ClientGetMlModelResponseEndpointInfoTypeDef
):
    """
    Type definition for `ClientGetMlModelResponse` `EndpointInfo`

    The current endpoint of the ``MLModel``

    - **PeakRequestsPerSecond** *(integer) --*

      The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
      incoming requests per second.

    - **CreatedAt** *(datetime) --*

      The time that the request to create the real-time endpoint for the ``MLModel`` was
      received. The time is expressed in epoch time.

    - **EndpointUrl** *(string) --*

      The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

      .. note::

        Note

        The application must wait until the real-time endpoint is ready before using this URI.

    - **EndpointStatus** *(string) --*

      The current status of the real-time endpoint for the ``MLModel`` . This element can have
      one of the following values:

      * ``NONE`` - Endpoint does not exist or was previously deleted.

      * ``READY`` - Endpoint is ready to be used for real-time predictions.

      * ``UPDATING`` - Updating/creating the endpoint.
    """


_ClientGetMlModelResponseTypeDef = TypedDict(
    "_ClientGetMlModelResponseTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "SizeInBytes": int,
        "EndpointInfo": ClientGetMlModelResponseEndpointInfoTypeDef,
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "MLModelType": str,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "Recipe": str,
        "Schema": str,
    },
    total=False,
)


class ClientGetMlModelResponseTypeDef(_ClientGetMlModelResponseTypeDef):
    """
    Type definition for `ClientGetMlModel` `Response`

    Represents the output of a ``GetMLModel`` operation, and provides detailed information about a
    ``MLModel`` .

    - **MLModelId** *(string) --*

      The MLModel ID,which is same as the ``MLModelId`` in the request.

    - **TrainingDataSourceId** *(string) --*

      The ID of the training ``DataSource`` .

    - **CreatedByIamUser** *(string) --*

      The AWS user account from which the ``MLModel`` was created. The account type can be either
      an AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``MLModel`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``MLModel`` .

    - **Status** *(string) --*

      The current status of the ``MLModel`` . This element can have one of the following values:

      * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to describe a
      ``MLModel`` .

      * ``INPROGRESS`` - The request is processing.

      * ``FAILED`` - The request did not run to completion. The ML model isn't usable.

      * ``COMPLETED`` - The request completed successfully.

      * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn't usable.

    - **SizeInBytes** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **EndpointInfo** *(dict) --*

      The current endpoint of the ``MLModel``

      - **PeakRequestsPerSecond** *(integer) --*

        The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
        incoming requests per second.

      - **CreatedAt** *(datetime) --*

        The time that the request to create the real-time endpoint for the ``MLModel`` was
        received. The time is expressed in epoch time.

      - **EndpointUrl** *(string) --*

        The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

        .. note::

          Note

          The application must wait until the real-time endpoint is ready before using this URI.

      - **EndpointStatus** *(string) --*

        The current status of the real-time endpoint for the ``MLModel`` . This element can have
        one of the following values:

        * ``NONE`` - Endpoint does not exist or was previously deleted.

        * ``READY`` - Endpoint is ready to be used for real-time predictions.

        * ``UPDATING`` - Updating/creating the endpoint.

    - **TrainingParameters** *(dict) --*

      A list of the training parameters in the ``MLModel`` . The list is implemented as a map of
      key-value pairs.

      The following is the current set of training parameters:

      * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the
      input data, the size of the model might affect its performance. The value is an integer that
      ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` .

      * ``sgd.maxPasses`` - The number of times that the training process traverses the
      observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to
      ``10000`` . The default value is ``10`` .

      * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling data improves
      a model's ability to find the optimal solution for a variety of data types. The valid values
      are ``auto`` and ``none`` . The default value is ``none`` . We strongly recommend that you
      shuffle your data.

      * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm. It controls
      overfitting the data by penalizing large coefficients. This tends to drive coefficients to
      zero, resulting in a sparse feature set. If you use this parameter, start by specifying a
      small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to
      ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter can't be used
      when ``L2`` is specified. Use this parameter sparingly.

      * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm. It controls
      overfitting the data by penalizing large coefficients. This tends to drive coefficients to
      small, nonzero values. If you use this parameter, start by specifying a small value, such as
      ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is
      to not use L2 normalization. This parameter can't be used when ``L1`` is specified. Use this
      parameter sparingly.

      - *(string) --*

        String type.

        - *(string) --*

          String type.

    - **InputDataLocationS3** *(string) --*

      The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

    - **MLModelType** *(string) --*

      Identifies the ``MLModel`` category. The following are the available types:

      * REGRESSION -- Produces a numeric result. For example, "What price should a house be listed
      at?"

      * BINARY -- Produces one of two possible results. For example, "Is this an e-commerce
      website?"

      * MULTICLASS -- Produces one of several possible results. For example, "Is this a HIGH, LOW
      or MEDIUM risk trade?"

    - **ScoreThreshold** *(float) --*

      The scoring threshold is used in binary classification ``MLModel``  models. It marks the
      boundary between a positive prediction and a negative prediction.

      Output values greater than or equal to the threshold receive a positive result from the
      MLModel, such as ``true`` . Output values less than the threshold receive a negative response
      from the MLModel, such as ``false`` .

    - **ScoreThresholdLastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in epoch
      time.

    - **LogUri** *(string) --*

      A link to the file that contains logs of the ``CreateMLModel`` operation.

    - **Message** *(string) --*

      A description of the most recent details about accessing the ``MLModel`` .

    - **ComputeTime** *(integer) --*

      The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the
      ``MLModel`` , normalized and scaled on computation resources. ``ComputeTime`` is only
      available if the ``MLModel`` is in the ``COMPLETED`` state.

    - **FinishedAt** *(datetime) --*

      The epoch time when Amazon Machine Learning marked the ``MLModel`` as ``COMPLETED`` or
      ``FAILED`` . ``FinishedAt`` is only available when the ``MLModel`` is in the ``COMPLETED`` or
      ``FAILED`` state.

    - **StartedAt** *(datetime) --*

      The epoch time when Amazon Machine Learning marked the ``MLModel`` as ``INPROGRESS`` .
      ``StartedAt`` isn't available if the ``MLModel`` is in the ``PENDING`` state.

    - **Recipe** *(string) --*

      The recipe to use when training the ``MLModel`` . The ``Recipe`` provides detailed
      information about the observation data to use during training, and manipulations to perform
      on the observation data during training.

      .. note::

        Note

        This parameter is provided as part of the verbose format.

    - **Schema** *(string) --*

      The schema used by all of the data files referenced by the ``DataSource`` .

      .. note::

        Note

        This parameter is provided as part of the verbose format.
    """


_ClientPredictResponsePredictionTypeDef = TypedDict(
    "_ClientPredictResponsePredictionTypeDef",
    {
        "predictedLabel": str,
        "predictedValue": float,
        "predictedScores": Dict[str, Any],
        "details": Dict[str, Any],
    },
    total=False,
)


class ClientPredictResponsePredictionTypeDef(_ClientPredictResponsePredictionTypeDef):
    """
    Type definition for `ClientPredictResponse` `Prediction`

    The output from a ``Predict`` operation:

    * ``Details`` - Contains the following attributes: ``DetailsAttributes.PREDICTIVE_MODEL_TYPE
    - REGRESSION | BINARY | MULTICLASS``  ``DetailsAttributes.ALGORITHM - SGD``

    * ``PredictedLabel`` - Present for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` request.

    * ``PredictedScores`` - Contains the raw classification score corresponding to each label.

    * ``PredictedValue`` - Present for a ``REGRESSION``  ``MLModel`` request.

    - **predictedLabel** *(string) --*

      The prediction label for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` .

    - **predictedValue** *(float) --* The prediction value for ``REGRESSION``  ``MLModel`` .

    - **predictedScores** *(dict) --* Provides the raw classification score corresponding to each
    label.

      - *(string) --*

        - *(float) --*

    - **details** *(dict) --* Provides any additional details regarding the prediction.

      - *(string) --* Contains the key values of ``DetailsMap`` : ``PredictiveModelType`` -
      Indicates the type of the ``MLModel`` . ``Algorithm`` - Indicates the algorithm that was
      used for the ``MLModel`` .

        - *(string) --*
    """


_ClientPredictResponseTypeDef = TypedDict(
    "_ClientPredictResponseTypeDef",
    {"Prediction": ClientPredictResponsePredictionTypeDef},
    total=False,
)


class ClientPredictResponseTypeDef(_ClientPredictResponseTypeDef):
    """
    Type definition for `ClientPredict` `Response`

    - **Prediction** *(dict) --*

      The output from a ``Predict`` operation:

      * ``Details`` - Contains the following attributes: ``DetailsAttributes.PREDICTIVE_MODEL_TYPE
      - REGRESSION | BINARY | MULTICLASS``  ``DetailsAttributes.ALGORITHM - SGD``

      * ``PredictedLabel`` - Present for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` request.

      * ``PredictedScores`` - Contains the raw classification score corresponding to each label.

      * ``PredictedValue`` - Present for a ``REGRESSION``  ``MLModel`` request.

      - **predictedLabel** *(string) --*

        The prediction label for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` .

      - **predictedValue** *(float) --* The prediction value for ``REGRESSION``  ``MLModel`` .

      - **predictedScores** *(dict) --* Provides the raw classification score corresponding to each
      label.

        - *(string) --*

          - *(float) --*

      - **details** *(dict) --* Provides any additional details regarding the prediction.

        - *(string) --* Contains the key values of ``DetailsMap`` : ``PredictiveModelType`` -
        Indicates the type of the ``MLModel`` . ``Algorithm`` - Indicates the algorithm that was
        used for the ``MLModel`` .

          - *(string) --*
    """


_ClientUpdateBatchPredictionResponseTypeDef = TypedDict(
    "_ClientUpdateBatchPredictionResponseTypeDef",
    {"BatchPredictionId": str},
    total=False,
)


class ClientUpdateBatchPredictionResponseTypeDef(
    _ClientUpdateBatchPredictionResponseTypeDef
):
    """
    Type definition for `ClientUpdateBatchPrediction` `Response`

    Represents the output of an ``UpdateBatchPrediction`` operation.

    You can see the updated content by using the ``GetBatchPrediction`` operation.

    - **BatchPredictionId** *(string) --*

      The ID assigned to the ``BatchPrediction`` during creation. This value should be identical to
      the value of the ``BatchPredictionId`` in the request.
    """


_ClientUpdateDataSourceResponseTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientUpdateDataSourceResponseTypeDef(_ClientUpdateDataSourceResponseTypeDef):
    """
    Type definition for `ClientUpdateDataSource` `Response`

    Represents the output of an ``UpdateDataSource`` operation.

    You can see the updated content by using the ``GetBatchPrediction`` operation.

    - **DataSourceId** *(string) --*

      The ID assigned to the ``DataSource`` during creation. This value should be identical to the
      value of the ``DataSourceID`` in the request.
    """


_ClientUpdateEvaluationResponseTypeDef = TypedDict(
    "_ClientUpdateEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)


class ClientUpdateEvaluationResponseTypeDef(_ClientUpdateEvaluationResponseTypeDef):
    """
    Type definition for `ClientUpdateEvaluation` `Response`

    Represents the output of an ``UpdateEvaluation`` operation.

    You can see the updated content by using the ``GetEvaluation`` operation.

    - **EvaluationId** *(string) --*

      The ID assigned to the ``Evaluation`` during creation. This value should be identical to the
      value of the ``Evaluation`` in the request.
    """


_ClientUpdateMlModelResponseTypeDef = TypedDict(
    "_ClientUpdateMlModelResponseTypeDef", {"MLModelId": str}, total=False
)


class ClientUpdateMlModelResponseTypeDef(_ClientUpdateMlModelResponseTypeDef):
    """
    Type definition for `ClientUpdateMlModel` `Response`

    Represents the output of an ``UpdateMLModel`` operation.

    You can see the updated content by using the ``GetMLModel`` operation.

    - **MLModelId** *(string) --*

      The ID assigned to the ``MLModel`` during creation. This value should be identical to the
      value of the ``MLModelID`` in the request.
    """


_DataSourceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_DataSourceAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DataSourceAvailableWaitWaiterConfigTypeDef(
    _DataSourceAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `DataSourceAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_DescribeBatchPredictionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeBatchPredictionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeBatchPredictionsPaginatePaginationConfigTypeDef(
    _DescribeBatchPredictionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeBatchPredictionsPaginate` `PaginationConfig`

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


_DescribeBatchPredictionsPaginateResponseResultsTypeDef = TypedDict(
    "_DescribeBatchPredictionsPaginateResponseResultsTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "OutputUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)


class DescribeBatchPredictionsPaginateResponseResultsTypeDef(
    _DescribeBatchPredictionsPaginateResponseResultsTypeDef
):
    """
    Type definition for `DescribeBatchPredictionsPaginateResponse` `Results`

    Represents the output of a ``GetBatchPrediction`` operation.

    The content consists of the detailed metadata, the status, and the data file information of
    a ``Batch Prediction`` .

    - **BatchPredictionId** *(string) --*

      The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to
      the value of the ``BatchPredictionID`` in the request.

    - **MLModelId** *(string) --*

      The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.

    - **BatchPredictionDataSourceId** *(string) --*

      The ID of the ``DataSource`` that points to the group of observations to predict.

    - **InputDataLocationS3** *(string) --*

      The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

    - **CreatedByIamUser** *(string) --*

      The AWS user account that invoked the ``BatchPrediction`` . The account type can be
      either an AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``BatchPrediction`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in
      epoch time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``BatchPrediction`` .

    - **Status** *(string) --*

      The status of the ``BatchPrediction`` . This element can have one of the following values:

      * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate
      predictions for a batch of observations.

      * ``INPROGRESS`` - The process is underway.

      * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is
      not usable.

      * ``COMPLETED`` - The batch prediction process completed successfully.

      * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.

    - **OutputUri** *(string) --*

      The location of an Amazon S3 bucket or directory to receive the operation results. The
      following substrings are not allowed in the ``s3 key`` portion of the ``outputURI``
      field: ':', '//', '/./', '/../'.

    - **Message** *(string) --*

      A description of the most recent details about processing the batch prediction request.

    - **ComputeTime** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **FinishedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **StartedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **TotalRecordCount** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **InvalidRecordCount** *(integer) --*

      Long integer type that is a 64-bit signed number.
    """


_DescribeBatchPredictionsPaginateResponseTypeDef = TypedDict(
    "_DescribeBatchPredictionsPaginateResponseTypeDef",
    {"Results": List[DescribeBatchPredictionsPaginateResponseResultsTypeDef]},
    total=False,
)


class DescribeBatchPredictionsPaginateResponseTypeDef(
    _DescribeBatchPredictionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeBatchPredictionsPaginate` `Response`

    Represents the output of a ``DescribeBatchPredictions`` operation. The content is essentially a
    list of ``BatchPrediction`` s.

    - **Results** *(list) --*

      A list of ``BatchPrediction`` objects that meet the search criteria.

      - *(dict) --*

        Represents the output of a ``GetBatchPrediction`` operation.

        The content consists of the detailed metadata, the status, and the data file information of
        a ``Batch Prediction`` .

        - **BatchPredictionId** *(string) --*

          The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to
          the value of the ``BatchPredictionID`` in the request.

        - **MLModelId** *(string) --*

          The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.

        - **BatchPredictionDataSourceId** *(string) --*

          The ID of the ``DataSource`` that points to the group of observations to predict.

        - **InputDataLocationS3** *(string) --*

          The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

        - **CreatedByIamUser** *(string) --*

          The AWS user account that invoked the ``BatchPrediction`` . The account type can be
          either an AWS root account or an AWS Identity and Access Management (IAM) user account.

        - **CreatedAt** *(datetime) --*

          The time that the ``BatchPrediction`` was created. The time is expressed in epoch time.

        - **LastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in
          epoch time.

        - **Name** *(string) --*

          A user-supplied name or description of the ``BatchPrediction`` .

        - **Status** *(string) --*

          The status of the ``BatchPrediction`` . This element can have one of the following values:

          * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate
          predictions for a batch of observations.

          * ``INPROGRESS`` - The process is underway.

          * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is
          not usable.

          * ``COMPLETED`` - The batch prediction process completed successfully.

          * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.

        - **OutputUri** *(string) --*

          The location of an Amazon S3 bucket or directory to receive the operation results. The
          following substrings are not allowed in the ``s3 key`` portion of the ``outputURI``
          field: ':', '//', '/./', '/../'.

        - **Message** *(string) --*

          A description of the most recent details about processing the batch prediction request.

        - **ComputeTime** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **FinishedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **StartedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **TotalRecordCount** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **InvalidRecordCount** *(integer) --*

          Long integer type that is a 64-bit signed number.
    """


_DescribeDataSourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDataSourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDataSourcesPaginatePaginationConfigTypeDef(
    _DescribeDataSourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDataSourcesPaginate` `PaginationConfig`

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


_DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef(
    _DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef
):
    """
    Type definition for `DescribeDataSourcesPaginateResponseResultsRDSMetadata` `Database`

    The database details required to connect to an Amazon RDS.

    - **InstanceIdentifier** *(string) --*

      The ID of an RDS DB instance.

    - **DatabaseName** *(string) --*

      The name of a database hosted on an RDS DB instance.
    """


_DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef",
    {
        "Database": DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "DataPipelineId": str,
    },
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef(
    _DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef
):
    """
    Type definition for `DescribeDataSourcesPaginateResponseResults` `RDSMetadata`

    The datasource details that are specific to Amazon RDS.

    - **Database** *(dict) --*

      The database details required to connect to an Amazon RDS.

      - **InstanceIdentifier** *(string) --*

        The ID of an RDS DB instance.

      - **DatabaseName** *(string) --*

        The name of a database hosted on an RDS DB instance.

    - **DatabaseUserName** *(string) --*

      The username to be used by Amazon ML to connect to database on an Amazon RDS instance.
      The username should have sufficient permissions to execute an ``RDSSelectSqlQuery``
      query.

    - **SelectSqlQuery** *(string) --*

      The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if
      ``Verbose`` is true in ``GetDataSourceInput`` .

    - **ResourceRole** *(string) --*

      The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry
      out the copy task from Amazon RDS to Amazon S3. For more information, see `Role
      templates
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
      for data pipelines.

    - **ServiceRole** *(string) --*

      The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the
      progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role
      templates
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
      for data pipelines.

    - **DataPipelineId** *(string) --*

      The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS
      to Amazon S3. You can use the ID to find details about the instance in the Data
      Pipeline console.
    """


_DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef(
    _DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef
):
    """
    Type definition for `DescribeDataSourcesPaginateResponseResultsRedshiftMetadata` `RedshiftDatabase`

    Describes the database details required to connect to an Amazon Redshift database.

    - **DatabaseName** *(string) --*

      The name of a database hosted on an Amazon Redshift cluster.

    - **ClusterIdentifier** *(string) --*

      The ID of an Amazon Redshift cluster.
    """


_DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef(
    _DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef
):
    """
    Type definition for `DescribeDataSourcesPaginateResponseResults` `RedshiftMetadata`

    Describes the ``DataSource`` details specific to Amazon Redshift.

    - **RedshiftDatabase** *(dict) --*

      Describes the database details required to connect to an Amazon Redshift database.

      - **DatabaseName** *(string) --*

        The name of a database hosted on an Amazon Redshift cluster.

      - **ClusterIdentifier** *(string) --*

        The ID of an Amazon Redshift cluster.

    - **DatabaseUserName** *(string) --*

      A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on
      an Amazon Redshift cluster. The username should have sufficient permissions to execute
      the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon
      Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

    - **SelectSqlQuery** *(string) --*

      The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if
      ``Verbose`` is true in GetDataSourceInput.
    """


_DescribeDataSourcesPaginateResponseResultsTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": str,
        "Message": str,
        "RedshiftMetadata": DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef,
        "RDSMetadata": DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef,
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsTypeDef(
    _DescribeDataSourcesPaginateResponseResultsTypeDef
):
    """
    Type definition for `DescribeDataSourcesPaginateResponse` `Results`

    Represents the output of the ``GetDataSource`` operation.

    The content consists of the detailed metadata and data file information and the current
    status of the ``DataSource`` .

    - **DataSourceId** *(string) --*

      The ID that is assigned to the ``DataSource`` during creation.

    - **DataLocationS3** *(string) --*

      The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is
      used by a ``DataSource`` .

    - **DataRearrangement** *(string) --*

      A JSON string that represents the splitting and rearrangement requirement used when this
      ``DataSource`` was created.

    - **CreatedByIamUser** *(string) --*

      The AWS user account from which the ``DataSource`` was created. The account type can be
      either an AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``DataSource`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in
      epoch time.

    - **DataSizeInBytes** *(integer) --*

      The total number of observations contained in the data files that the ``DataSource``
      references.

    - **NumberOfFiles** *(integer) --*

      The number of data files referenced by the ``DataSource`` .

    - **Name** *(string) --*

      A user-supplied name or description of the ``DataSource`` .

    - **Status** *(string) --*

      The current status of the ``DataSource`` . This element can have one of the following
      values:

      * PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a
      ``DataSource`` .

      * INPROGRESS - The creation process is underway.

      * FAILED - The request to create a ``DataSource`` did not run to completion. It is not
      usable.

      * COMPLETED - The creation process completed successfully.

      * DELETED - The ``DataSource`` is marked as deleted. It is not usable.

    - **Message** *(string) --*

      A description of the most recent details about creating the ``DataSource`` .

    - **RedshiftMetadata** *(dict) --*

      Describes the ``DataSource`` details specific to Amazon Redshift.

      - **RedshiftDatabase** *(dict) --*

        Describes the database details required to connect to an Amazon Redshift database.

        - **DatabaseName** *(string) --*

          The name of a database hosted on an Amazon Redshift cluster.

        - **ClusterIdentifier** *(string) --*

          The ID of an Amazon Redshift cluster.

      - **DatabaseUserName** *(string) --*

        A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on
        an Amazon Redshift cluster. The username should have sufficient permissions to execute
        the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon
        Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

      - **SelectSqlQuery** *(string) --*

        The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if
        ``Verbose`` is true in GetDataSourceInput.

    - **RDSMetadata** *(dict) --*

      The datasource details that are specific to Amazon RDS.

      - **Database** *(dict) --*

        The database details required to connect to an Amazon RDS.

        - **InstanceIdentifier** *(string) --*

          The ID of an RDS DB instance.

        - **DatabaseName** *(string) --*

          The name of a database hosted on an RDS DB instance.

      - **DatabaseUserName** *(string) --*

        The username to be used by Amazon ML to connect to database on an Amazon RDS instance.
        The username should have sufficient permissions to execute an ``RDSSelectSqlQuery``
        query.

      - **SelectSqlQuery** *(string) --*

        The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if
        ``Verbose`` is true in ``GetDataSourceInput`` .

      - **ResourceRole** *(string) --*

        The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry
        out the copy task from Amazon RDS to Amazon S3. For more information, see `Role
        templates
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
        for data pipelines.

      - **ServiceRole** *(string) --*

        The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the
        progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role
        templates
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
        for data pipelines.

      - **DataPipelineId** *(string) --*

        The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS
        to Amazon S3. You can use the ID to find details about the instance in the Data
        Pipeline console.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of an `AWS IAM Role
      <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__
      , such as the following: arn:aws:iam::account:role/rolename.

    - **ComputeStatistics** *(boolean) --*

      The parameter is ``true`` if statistics need to be generated from the observation data.

    - **ComputeTime** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **FinishedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **StartedAt** *(datetime) --*

      A timestamp represented in epoch time.
    """


_DescribeDataSourcesPaginateResponseTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseTypeDef",
    {"Results": List[DescribeDataSourcesPaginateResponseResultsTypeDef]},
    total=False,
)


class DescribeDataSourcesPaginateResponseTypeDef(
    _DescribeDataSourcesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDataSourcesPaginate` `Response`

    Represents the query results from a  DescribeDataSources operation. The content is essentially
    a list of ``DataSource`` .

    - **Results** *(list) --*

      A list of ``DataSource`` that meet the search criteria.

      - *(dict) --*

        Represents the output of the ``GetDataSource`` operation.

        The content consists of the detailed metadata and data file information and the current
        status of the ``DataSource`` .

        - **DataSourceId** *(string) --*

          The ID that is assigned to the ``DataSource`` during creation.

        - **DataLocationS3** *(string) --*

          The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is
          used by a ``DataSource`` .

        - **DataRearrangement** *(string) --*

          A JSON string that represents the splitting and rearrangement requirement used when this
          ``DataSource`` was created.

        - **CreatedByIamUser** *(string) --*

          The AWS user account from which the ``DataSource`` was created. The account type can be
          either an AWS root account or an AWS Identity and Access Management (IAM) user account.

        - **CreatedAt** *(datetime) --*

          The time that the ``DataSource`` was created. The time is expressed in epoch time.

        - **LastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in
          epoch time.

        - **DataSizeInBytes** *(integer) --*

          The total number of observations contained in the data files that the ``DataSource``
          references.

        - **NumberOfFiles** *(integer) --*

          The number of data files referenced by the ``DataSource`` .

        - **Name** *(string) --*

          A user-supplied name or description of the ``DataSource`` .

        - **Status** *(string) --*

          The current status of the ``DataSource`` . This element can have one of the following
          values:

          * PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a
          ``DataSource`` .

          * INPROGRESS - The creation process is underway.

          * FAILED - The request to create a ``DataSource`` did not run to completion. It is not
          usable.

          * COMPLETED - The creation process completed successfully.

          * DELETED - The ``DataSource`` is marked as deleted. It is not usable.

        - **Message** *(string) --*

          A description of the most recent details about creating the ``DataSource`` .

        - **RedshiftMetadata** *(dict) --*

          Describes the ``DataSource`` details specific to Amazon Redshift.

          - **RedshiftDatabase** *(dict) --*

            Describes the database details required to connect to an Amazon Redshift database.

            - **DatabaseName** *(string) --*

              The name of a database hosted on an Amazon Redshift cluster.

            - **ClusterIdentifier** *(string) --*

              The ID of an Amazon Redshift cluster.

          - **DatabaseUserName** *(string) --*

            A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on
            an Amazon Redshift cluster. The username should have sufficient permissions to execute
            the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon
            Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

          - **SelectSqlQuery** *(string) --*

            The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if
            ``Verbose`` is true in GetDataSourceInput.

        - **RDSMetadata** *(dict) --*

          The datasource details that are specific to Amazon RDS.

          - **Database** *(dict) --*

            The database details required to connect to an Amazon RDS.

            - **InstanceIdentifier** *(string) --*

              The ID of an RDS DB instance.

            - **DatabaseName** *(string) --*

              The name of a database hosted on an RDS DB instance.

          - **DatabaseUserName** *(string) --*

            The username to be used by Amazon ML to connect to database on an Amazon RDS instance.
            The username should have sufficient permissions to execute an ``RDSSelectSqlQuery``
            query.

          - **SelectSqlQuery** *(string) --*

            The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if
            ``Verbose`` is true in ``GetDataSourceInput`` .

          - **ResourceRole** *(string) --*

            The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry
            out the copy task from Amazon RDS to Amazon S3. For more information, see `Role
            templates
            <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
            for data pipelines.

          - **ServiceRole** *(string) --*

            The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the
            progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role
            templates
            <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__
            for data pipelines.

          - **DataPipelineId** *(string) --*

            The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS
            to Amazon S3. You can use the ID to find details about the instance in the Data
            Pipeline console.

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of an `AWS IAM Role
          <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__
          , such as the following: arn:aws:iam::account:role/rolename.

        - **ComputeStatistics** *(boolean) --*

          The parameter is ``true`` if statistics need to be generated from the observation data.

        - **ComputeTime** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **FinishedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **StartedAt** *(datetime) --*

          A timestamp represented in epoch time.
    """


_DescribeEvaluationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEvaluationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEvaluationsPaginatePaginationConfigTypeDef(
    _DescribeEvaluationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEvaluationsPaginate` `PaginationConfig`

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


_DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef = TypedDict(
    "_DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)


class DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef(
    _DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef
):
    """
    Type definition for `DescribeEvaluationsPaginateResponseResults` `PerformanceMetrics`

    Measurements of how well the ``MLModel`` performed, using observations referenced by the
    ``DataSource`` . One of the following metrics is returned, based on the type of the
    ``MLModel`` :

    * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to
    measure performance.

    * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE)
    technique to measure performance. RMSE measures the difference between predicted and
    actual values for a single variable.

    * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure
    performance.

    For more information about performance metrics, please see the `Amazon Machine Learning
    Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

    - **Properties** *(dict) --*

      - *(string) --*

        - *(string) --*
    """


_DescribeEvaluationsPaginateResponseResultsTypeDef = TypedDict(
    "_DescribeEvaluationsPaginateResponseResultsTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "PerformanceMetrics": DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class DescribeEvaluationsPaginateResponseResultsTypeDef(
    _DescribeEvaluationsPaginateResponseResultsTypeDef
):
    """
    Type definition for `DescribeEvaluationsPaginateResponse` `Results`

    Represents the output of ``GetEvaluation`` operation.

    The content consists of the detailed metadata and data file information and the current
    status of the ``Evaluation`` .

    - **EvaluationId** *(string) --*

      The ID that is assigned to the ``Evaluation`` at creation.

    - **MLModelId** *(string) --*

      The ID of the ``MLModel`` that is the focus of the evaluation.

    - **EvaluationDataSourceId** *(string) --*

      The ID of the ``DataSource`` that is used to evaluate the ``MLModel`` .

    - **InputDataLocationS3** *(string) --*

      The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is
      used in the evaluation.

    - **CreatedByIamUser** *(string) --*

      The AWS user account that invoked the evaluation. The account type can be either an AWS
      root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``Evaluation`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch
      time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``Evaluation`` .

    - **Status** *(string) --*

      The status of the evaluation. This element can have one of the following values:

      * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an
      ``MLModel`` .

      * ``INPROGRESS`` - The evaluation is underway.

      * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is
      not usable.

      * ``COMPLETED`` - The evaluation process completed successfully.

      * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.

    - **PerformanceMetrics** *(dict) --*

      Measurements of how well the ``MLModel`` performed, using observations referenced by the
      ``DataSource`` . One of the following metrics is returned, based on the type of the
      ``MLModel`` :

      * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to
      measure performance.

      * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE)
      technique to measure performance. RMSE measures the difference between predicted and
      actual values for a single variable.

      * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure
      performance.

      For more information about performance metrics, please see the `Amazon Machine Learning
      Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

      - **Properties** *(dict) --*

        - *(string) --*

          - *(string) --*

    - **Message** *(string) --*

      A description of the most recent details about evaluating the ``MLModel`` .

    - **ComputeTime** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **FinishedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **StartedAt** *(datetime) --*

      A timestamp represented in epoch time.
    """


_DescribeEvaluationsPaginateResponseTypeDef = TypedDict(
    "_DescribeEvaluationsPaginateResponseTypeDef",
    {"Results": List[DescribeEvaluationsPaginateResponseResultsTypeDef]},
    total=False,
)


class DescribeEvaluationsPaginateResponseTypeDef(
    _DescribeEvaluationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEvaluationsPaginate` `Response`

    Represents the query results from a ``DescribeEvaluations`` operation. The content is
    essentially a list of ``Evaluation`` .

    - **Results** *(list) --*

      A list of ``Evaluation`` that meet the search criteria.

      - *(dict) --*

        Represents the output of ``GetEvaluation`` operation.

        The content consists of the detailed metadata and data file information and the current
        status of the ``Evaluation`` .

        - **EvaluationId** *(string) --*

          The ID that is assigned to the ``Evaluation`` at creation.

        - **MLModelId** *(string) --*

          The ID of the ``MLModel`` that is the focus of the evaluation.

        - **EvaluationDataSourceId** *(string) --*

          The ID of the ``DataSource`` that is used to evaluate the ``MLModel`` .

        - **InputDataLocationS3** *(string) --*

          The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is
          used in the evaluation.

        - **CreatedByIamUser** *(string) --*

          The AWS user account that invoked the evaluation. The account type can be either an AWS
          root account or an AWS Identity and Access Management (IAM) user account.

        - **CreatedAt** *(datetime) --*

          The time that the ``Evaluation`` was created. The time is expressed in epoch time.

        - **LastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch
          time.

        - **Name** *(string) --*

          A user-supplied name or description of the ``Evaluation`` .

        - **Status** *(string) --*

          The status of the evaluation. This element can have one of the following values:

          * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an
          ``MLModel`` .

          * ``INPROGRESS`` - The evaluation is underway.

          * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is
          not usable.

          * ``COMPLETED`` - The evaluation process completed successfully.

          * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.

        - **PerformanceMetrics** *(dict) --*

          Measurements of how well the ``MLModel`` performed, using observations referenced by the
          ``DataSource`` . One of the following metrics is returned, based on the type of the
          ``MLModel`` :

          * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to
          measure performance.

          * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE)
          technique to measure performance. RMSE measures the difference between predicted and
          actual values for a single variable.

          * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure
          performance.

          For more information about performance metrics, please see the `Amazon Machine Learning
          Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

          - **Properties** *(dict) --*

            - *(string) --*

              - *(string) --*

        - **Message** *(string) --*

          A description of the most recent details about evaluating the ``MLModel`` .

        - **ComputeTime** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **FinishedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **StartedAt** *(datetime) --*

          A timestamp represented in epoch time.
    """


_DescribeMLModelsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMLModelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMLModelsPaginatePaginationConfigTypeDef(
    _DescribeMLModelsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeMLModelsPaginate` `PaginationConfig`

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


_DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef = TypedDict(
    "_DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": str,
    },
    total=False,
)


class DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef(
    _DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef
):
    """
    Type definition for `DescribeMLModelsPaginateResponseResults` `EndpointInfo`

    The current endpoint of the ``MLModel`` .

    - **PeakRequestsPerSecond** *(integer) --*

      The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
      incoming requests per second.

    - **CreatedAt** *(datetime) --*

      The time that the request to create the real-time endpoint for the ``MLModel`` was
      received. The time is expressed in epoch time.

    - **EndpointUrl** *(string) --*

      The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

      .. note::

        Note

        The application must wait until the real-time endpoint is ready before using this URI.

    - **EndpointStatus** *(string) --*

      The current status of the real-time endpoint for the ``MLModel`` . This element can
      have one of the following values:

      * ``NONE`` - Endpoint does not exist or was previously deleted.

      * ``READY`` - Endpoint is ready to be used for real-time predictions.

      * ``UPDATING`` - Updating/creating the endpoint.
    """


_DescribeMLModelsPaginateResponseResultsTypeDef = TypedDict(
    "_DescribeMLModelsPaginateResponseResultsTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": str,
        "SizeInBytes": int,
        "EndpointInfo": DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef,
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "Algorithm": str,
        "MLModelType": str,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class DescribeMLModelsPaginateResponseResultsTypeDef(
    _DescribeMLModelsPaginateResponseResultsTypeDef
):
    """
    Type definition for `DescribeMLModelsPaginateResponse` `Results`

    Represents the output of a ``GetMLModel`` operation.

    The content consists of the detailed metadata and the current status of the ``MLModel`` .

    - **MLModelId** *(string) --*

      The ID assigned to the ``MLModel`` at creation.

    - **TrainingDataSourceId** *(string) --*

      The ID of the training ``DataSource`` . The ``CreateMLModel`` operation uses the
      ``TrainingDataSourceId`` .

    - **CreatedByIamUser** *(string) --*

      The AWS user account from which the ``MLModel`` was created. The account type can be
      either an AWS root account or an AWS Identity and Access Management (IAM) user account.

    - **CreatedAt** *(datetime) --*

      The time that the ``MLModel`` was created. The time is expressed in epoch time.

    - **LastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.

    - **Name** *(string) --*

      A user-supplied name or description of the ``MLModel`` .

    - **Status** *(string) --*

      The current status of an ``MLModel`` . This element can have one of the following values:

      * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to create an
      ``MLModel`` .

      * ``INPROGRESS`` - The creation process is underway.

      * ``FAILED`` - The request to create an ``MLModel`` didn't run to completion. The model
      isn't usable.

      * ``COMPLETED`` - The creation process completed successfully.

      * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn't usable.

    - **SizeInBytes** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **EndpointInfo** *(dict) --*

      The current endpoint of the ``MLModel`` .

      - **PeakRequestsPerSecond** *(integer) --*

        The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
        incoming requests per second.

      - **CreatedAt** *(datetime) --*

        The time that the request to create the real-time endpoint for the ``MLModel`` was
        received. The time is expressed in epoch time.

      - **EndpointUrl** *(string) --*

        The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

        .. note::

          Note

          The application must wait until the real-time endpoint is ready before using this URI.

      - **EndpointStatus** *(string) --*

        The current status of the real-time endpoint for the ``MLModel`` . This element can
        have one of the following values:

        * ``NONE`` - Endpoint does not exist or was previously deleted.

        * ``READY`` - Endpoint is ready to be used for real-time predictions.

        * ``UPDATING`` - Updating/creating the endpoint.

    - **TrainingParameters** *(dict) --*

      A list of the training parameters in the ``MLModel`` . The list is implemented as a map
      of key-value pairs.

      The following is the current set of training parameters:

      * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the
      input data, the size of the model might affect its performance. The value is an integer
      that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` .

      * ``sgd.maxPasses`` - The number of times that the training process traverses the
      observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to
      ``10000`` . The default value is ``10`` .

      * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling the data
      improves a model's ability to find the optimal solution for a variety of data types. The
      valid values are ``auto`` and ``none`` . The default value is ``none`` .

      * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm, which controls
      overfitting the data by penalizing large coefficients. This parameter tends to drive
      coefficients to zero, resulting in sparse feature set. If you use this parameter, start
      by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from
      ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter
      can't be used when ``L2`` is specified. Use this parameter sparingly.

      * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm, which controls
      overfitting the data by penalizing large coefficients. This tends to drive coefficients
      to small, nonzero values. If you use this parameter, start by specifying a small value,
      such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` .
      The default is to not use L2 normalization. This parameter can't be used when ``L1`` is
      specified. Use this parameter sparingly.

      - *(string) --*

        String type.

        - *(string) --*

          String type.

    - **InputDataLocationS3** *(string) --*

      The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

    - **Algorithm** *(string) --*

      The algorithm used to train the ``MLModel`` . The following algorithm is supported:

      * ``SGD`` -- Stochastic gradient descent. The goal of ``SGD`` is to minimize the gradient
      of the loss function.

    - **MLModelType** *(string) --*

      Identifies the ``MLModel`` category. The following are the available types:

      * ``REGRESSION`` - Produces a numeric result. For example, "What price should a house be
      listed at?"

      * ``BINARY`` - Produces one of two possible results. For example, "Is this a
      child-friendly web site?".

      * ``MULTICLASS`` - Produces one of several possible results. For example, "Is this a
      HIGH-, LOW-, or MEDIUM-risk trade?".

    - **ScoreThreshold** *(float) --*

    - **ScoreThresholdLastUpdatedAt** *(datetime) --*

      The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in
      epoch time.

    - **Message** *(string) --*

      A description of the most recent details about accessing the ``MLModel`` .

    - **ComputeTime** *(integer) --*

      Long integer type that is a 64-bit signed number.

    - **FinishedAt** *(datetime) --*

      A timestamp represented in epoch time.

    - **StartedAt** *(datetime) --*

      A timestamp represented in epoch time.
    """


_DescribeMLModelsPaginateResponseTypeDef = TypedDict(
    "_DescribeMLModelsPaginateResponseTypeDef",
    {"Results": List[DescribeMLModelsPaginateResponseResultsTypeDef]},
    total=False,
)


class DescribeMLModelsPaginateResponseTypeDef(_DescribeMLModelsPaginateResponseTypeDef):
    """
    Type definition for `DescribeMLModelsPaginate` `Response`

    Represents the output of a ``DescribeMLModels`` operation. The content is essentially a list of
    ``MLModel`` .

    - **Results** *(list) --*

      A list of ``MLModel`` that meet the search criteria.

      - *(dict) --*

        Represents the output of a ``GetMLModel`` operation.

        The content consists of the detailed metadata and the current status of the ``MLModel`` .

        - **MLModelId** *(string) --*

          The ID assigned to the ``MLModel`` at creation.

        - **TrainingDataSourceId** *(string) --*

          The ID of the training ``DataSource`` . The ``CreateMLModel`` operation uses the
          ``TrainingDataSourceId`` .

        - **CreatedByIamUser** *(string) --*

          The AWS user account from which the ``MLModel`` was created. The account type can be
          either an AWS root account or an AWS Identity and Access Management (IAM) user account.

        - **CreatedAt** *(datetime) --*

          The time that the ``MLModel`` was created. The time is expressed in epoch time.

        - **LastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.

        - **Name** *(string) --*

          A user-supplied name or description of the ``MLModel`` .

        - **Status** *(string) --*

          The current status of an ``MLModel`` . This element can have one of the following values:

          * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to create an
          ``MLModel`` .

          * ``INPROGRESS`` - The creation process is underway.

          * ``FAILED`` - The request to create an ``MLModel`` didn't run to completion. The model
          isn't usable.

          * ``COMPLETED`` - The creation process completed successfully.

          * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn't usable.

        - **SizeInBytes** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **EndpointInfo** *(dict) --*

          The current endpoint of the ``MLModel`` .

          - **PeakRequestsPerSecond** *(integer) --*

            The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in
            incoming requests per second.

          - **CreatedAt** *(datetime) --*

            The time that the request to create the real-time endpoint for the ``MLModel`` was
            received. The time is expressed in epoch time.

          - **EndpointUrl** *(string) --*

            The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

            .. note::

              Note

              The application must wait until the real-time endpoint is ready before using this URI.

          - **EndpointStatus** *(string) --*

            The current status of the real-time endpoint for the ``MLModel`` . This element can
            have one of the following values:

            * ``NONE`` - Endpoint does not exist or was previously deleted.

            * ``READY`` - Endpoint is ready to be used for real-time predictions.

            * ``UPDATING`` - Updating/creating the endpoint.

        - **TrainingParameters** *(dict) --*

          A list of the training parameters in the ``MLModel`` . The list is implemented as a map
          of key-value pairs.

          The following is the current set of training parameters:

          * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the
          input data, the size of the model might affect its performance. The value is an integer
          that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` .

          * ``sgd.maxPasses`` - The number of times that the training process traverses the
          observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to
          ``10000`` . The default value is ``10`` .

          * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling the data
          improves a model's ability to find the optimal solution for a variety of data types. The
          valid values are ``auto`` and ``none`` . The default value is ``none`` .

          * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm, which controls
          overfitting the data by penalizing large coefficients. This parameter tends to drive
          coefficients to zero, resulting in sparse feature set. If you use this parameter, start
          by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from
          ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter
          can't be used when ``L2`` is specified. Use this parameter sparingly.

          * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm, which controls
          overfitting the data by penalizing large coefficients. This tends to drive coefficients
          to small, nonzero values. If you use this parameter, start by specifying a small value,
          such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` .
          The default is to not use L2 normalization. This parameter can't be used when ``L1`` is
          specified. Use this parameter sparingly.

          - *(string) --*

            String type.

            - *(string) --*

              String type.

        - **InputDataLocationS3** *(string) --*

          The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

        - **Algorithm** *(string) --*

          The algorithm used to train the ``MLModel`` . The following algorithm is supported:

          * ``SGD`` -- Stochastic gradient descent. The goal of ``SGD`` is to minimize the gradient
          of the loss function.

        - **MLModelType** *(string) --*

          Identifies the ``MLModel`` category. The following are the available types:

          * ``REGRESSION`` - Produces a numeric result. For example, "What price should a house be
          listed at?"

          * ``BINARY`` - Produces one of two possible results. For example, "Is this a
          child-friendly web site?".

          * ``MULTICLASS`` - Produces one of several possible results. For example, "Is this a
          HIGH-, LOW-, or MEDIUM-risk trade?".

        - **ScoreThreshold** *(float) --*

        - **ScoreThresholdLastUpdatedAt** *(datetime) --*

          The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in
          epoch time.

        - **Message** *(string) --*

          A description of the most recent details about accessing the ``MLModel`` .

        - **ComputeTime** *(integer) --*

          Long integer type that is a 64-bit signed number.

        - **FinishedAt** *(datetime) --*

          A timestamp represented in epoch time.

        - **StartedAt** *(datetime) --*

          A timestamp represented in epoch time.
    """


_EvaluationAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_EvaluationAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class EvaluationAvailableWaitWaiterConfigTypeDef(
    _EvaluationAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `EvaluationAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_MlModelAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_MlModelAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class MlModelAvailableWaitWaiterConfigTypeDef(_MlModelAvailableWaitWaiterConfigTypeDef):
    """
    Type definition for `MlModelAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """
