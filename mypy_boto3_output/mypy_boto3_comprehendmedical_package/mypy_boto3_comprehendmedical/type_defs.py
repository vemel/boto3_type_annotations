"Main interface for comprehendmedical type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    "ClientDescribePhiDetectionJobResponseTypeDef",
    "ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectEntitiesResponseEntitiesAttributesTypeDef",
    "ClientDetectEntitiesResponseEntitiesTraitsTypeDef",
    "ClientDetectEntitiesResponseEntitiesTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesTypeDef",
    "ClientDetectEntitiesResponseTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef",
    "ClientDetectEntitiesV2ResponseTypeDef",
    "ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectPhiResponseEntitiesAttributesTypeDef",
    "ClientDetectPhiResponseEntitiesTraitsTypeDef",
    "ClientDetectPhiResponseEntitiesTypeDef",
    "ClientDetectPhiResponseTypeDef",
    "ClientListEntitiesDetectionV2JobsFilterTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseTypeDef",
    "ClientListPhiDetectionJobsFilterTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    "ClientListPhiDetectionJobsResponseTypeDef",
    "ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef",
    "ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef",
    "ClientStartEntitiesDetectionV2JobResponseTypeDef",
    "ClientStartPhiDetectionJobInputDataConfigTypeDef",
    "ClientStartPhiDetectionJobOutputDataConfigTypeDef",
    "ClientStartPhiDetectionJobResponseTypeDef",
    "ClientStopEntitiesDetectionV2JobResponseTypeDef",
    "ClientStopPhiDetectionJobResponseTypeDef",
)


_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobProperties` `InputDataConfig`

    The input data configuration that you supplied when you created the detection job.

    - **S3Bucket** *(string) --*

      The URI of the S3 bucket that contains the input data. The bucket must be in the same
      region as the API endpoint that you are calling.

      Each file in the document collection must be less than 40 KB. You can store a maximum of
      30 GB in the bucket.

    - **S3Key** *(string) --*

      The path to the input data files in the S3 bucket.
    """


_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobProperties` `OutputDataConfig`

    The output data configuration that you supplied when you created the detection job.

    - **S3Bucket** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix
      for the actual location of the output.

    - **S3Key** *(string) --*

      The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an
      output directory using the job ID so that the output from one job does not overwrite the
      output of another.
    """


_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef(
    _ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionV2JobResponse` `ComprehendMedicalAsyncJobProperties`

    An object that contains the properties associated with a detection job.

    - **JobId** *(string) --*

      The identifier assigned to the detection job.

    - **JobName** *(string) --*

      The name that you assigned to the detection job.

    - **JobStatus** *(string) --*

      The current status of the detection job. If the status is ``FAILED`` , the ``Message``
      field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the detection job completed.

    - **ExpirationTime** *(datetime) --*

      The date and time that job metadata is deleted from the server. Output files in your S3
      bucket will not be deleted. After the metadata is deleted, the job will no longer appear in
      the results of the ``ListEntitiesDetectionV2Job`` or the ``ListPHIDetectionJobs`` operation.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the detection job.

      - **S3Bucket** *(string) --*

        The URI of the S3 bucket that contains the input data. The bucket must be in the same
        region as the API endpoint that you are calling.

        Each file in the document collection must be less than 40 KB. You can store a maximum of
        30 GB in the bucket.

      - **S3Key** *(string) --*

        The path to the input data files in the S3 bucket.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the detection job.

      - **S3Bucket** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the prefix
        for the actual location of the output.

      - **S3Key** *(string) --*

        The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an
        output directory using the job ID so that the output from one job does not overwrite the
        output of another.

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your
      input data.

    - **ManifestFilePath** *(string) --*

      The path to the file that describes the results of a batch job.

    - **KMSKey** *(string) --*

      The AWS Key Management Service key, if any, used to encrypt the output files.

    - **ModelVersion** *(string) --*

      The version of the model used to analyze the documents. The version number looks like
      X.X.X. You can use this information to track the model used for a particular batch of
      documents.
    """


_ClientDescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionV2JobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeEntitiesDetectionV2JobResponseTypeDef(
    _ClientDescribeEntitiesDetectionV2JobResponseTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionV2Job` `Response`

    - **ComprehendMedicalAsyncJobProperties** *(dict) --*

      An object that contains the properties associated with a detection job.

      - **JobId** *(string) --*

        The identifier assigned to the detection job.

      - **JobName** *(string) --*

        The name that you assigned to the detection job.

      - **JobStatus** *(string) --*

        The current status of the detection job. If the status is ``FAILED`` , the ``Message``
        field shows the reason for the failure.

      - **Message** *(string) --*

        A description of the status of a job.

      - **SubmitTime** *(datetime) --*

        The time that the detection job was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the detection job completed.

      - **ExpirationTime** *(datetime) --*

        The date and time that job metadata is deleted from the server. Output files in your S3
        bucket will not be deleted. After the metadata is deleted, the job will no longer appear in
        the results of the ``ListEntitiesDetectionV2Job`` or the ``ListPHIDetectionJobs`` operation.

      - **InputDataConfig** *(dict) --*

        The input data configuration that you supplied when you created the detection job.

        - **S3Bucket** *(string) --*

          The URI of the S3 bucket that contains the input data. The bucket must be in the same
          region as the API endpoint that you are calling.

          Each file in the document collection must be less than 40 KB. You can store a maximum of
          30 GB in the bucket.

        - **S3Key** *(string) --*

          The path to the input data files in the S3 bucket.

      - **OutputDataConfig** *(dict) --*

        The output data configuration that you supplied when you created the detection job.

        - **S3Bucket** *(string) --*

          When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
          the Amazon S3 location where you want to write the output data. The URI must be in the
          same region as the API endpoint that you are calling. The location is used as the prefix
          for the actual location of the output.

        - **S3Key** *(string) --*

          The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an
          output directory using the job ID so that the output from one job does not overwrite the
          output of another.

      - **LanguageCode** *(string) --*

        The language code of the input documents.

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your
        input data.

      - **ManifestFilePath** *(string) --*

        The path to the file that describes the results of a batch job.

      - **KMSKey** *(string) --*

        The AWS Key Management Service key, if any, used to encrypt the output files.

      - **ModelVersion** *(string) --*

        The version of the model used to analyze the documents. The version number looks like
        X.X.X. You can use this information to track the model used for a particular batch of
        documents.
    """


_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef(
    _ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobProperties` `InputDataConfig`

    The input data configuration that you supplied when you created the detection job.

    - **S3Bucket** *(string) --*

      The URI of the S3 bucket that contains the input data. The bucket must be in the same
      region as the API endpoint that you are calling.

      Each file in the document collection must be less than 40 KB. You can store a maximum of
      30 GB in the bucket.

    - **S3Key** *(string) --*

      The path to the input data files in the S3 bucket.
    """


_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobProperties` `OutputDataConfig`

    The output data configuration that you supplied when you created the detection job.

    - **S3Bucket** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix
      for the actual location of the output.

    - **S3Key** *(string) --*

      The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an
      output directory using the job ID so that the output from one job does not overwrite the
      output of another.
    """


_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef(
    _ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef
):
    """
    Type definition for `ClientDescribePhiDetectionJobResponse` `ComprehendMedicalAsyncJobProperties`

    An object that contains the properties associated with a detection job.

    - **JobId** *(string) --*

      The identifier assigned to the detection job.

    - **JobName** *(string) --*

      The name that you assigned to the detection job.

    - **JobStatus** *(string) --*

      The current status of the detection job. If the status is ``FAILED`` , the ``Message``
      field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the detection job completed.

    - **ExpirationTime** *(datetime) --*

      The date and time that job metadata is deleted from the server. Output files in your S3
      bucket will not be deleted. After the metadata is deleted, the job will no longer appear in
      the results of the ``ListEntitiesDetectionV2Job`` or the ``ListPHIDetectionJobs`` operation.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the detection job.

      - **S3Bucket** *(string) --*

        The URI of the S3 bucket that contains the input data. The bucket must be in the same
        region as the API endpoint that you are calling.

        Each file in the document collection must be less than 40 KB. You can store a maximum of
        30 GB in the bucket.

      - **S3Key** *(string) --*

        The path to the input data files in the S3 bucket.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the detection job.

      - **S3Bucket** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the prefix
        for the actual location of the output.

      - **S3Key** *(string) --*

        The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an
        output directory using the job ID so that the output from one job does not overwrite the
        output of another.

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your
      input data.

    - **ManifestFilePath** *(string) --*

      The path to the file that describes the results of a batch job.

    - **KMSKey** *(string) --*

      The AWS Key Management Service key, if any, used to encrypt the output files.

    - **ModelVersion** *(string) --*

      The version of the model used to analyze the documents. The version number looks like
      X.X.X. You can use this information to track the model used for a particular batch of
      documents.
    """


_ClientDescribePhiDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribePhiDetectionJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribePhiDetectionJobResponseTypeDef(
    _ClientDescribePhiDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientDescribePhiDetectionJob` `Response`

    - **ComprehendMedicalAsyncJobProperties** *(dict) --*

      An object that contains the properties associated with a detection job.

      - **JobId** *(string) --*

        The identifier assigned to the detection job.

      - **JobName** *(string) --*

        The name that you assigned to the detection job.

      - **JobStatus** *(string) --*

        The current status of the detection job. If the status is ``FAILED`` , the ``Message``
        field shows the reason for the failure.

      - **Message** *(string) --*

        A description of the status of a job.

      - **SubmitTime** *(datetime) --*

        The time that the detection job was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the detection job completed.

      - **ExpirationTime** *(datetime) --*

        The date and time that job metadata is deleted from the server. Output files in your S3
        bucket will not be deleted. After the metadata is deleted, the job will no longer appear in
        the results of the ``ListEntitiesDetectionV2Job`` or the ``ListPHIDetectionJobs`` operation.

      - **InputDataConfig** *(dict) --*

        The input data configuration that you supplied when you created the detection job.

        - **S3Bucket** *(string) --*

          The URI of the S3 bucket that contains the input data. The bucket must be in the same
          region as the API endpoint that you are calling.

          Each file in the document collection must be less than 40 KB. You can store a maximum of
          30 GB in the bucket.

        - **S3Key** *(string) --*

          The path to the input data files in the S3 bucket.

      - **OutputDataConfig** *(dict) --*

        The output data configuration that you supplied when you created the detection job.

        - **S3Bucket** *(string) --*

          When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
          the Amazon S3 location where you want to write the output data. The URI must be in the
          same region as the API endpoint that you are calling. The location is used as the prefix
          for the actual location of the output.

        - **S3Key** *(string) --*

          The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an
          output directory using the job ID so that the output from one job does not overwrite the
          output of another.

      - **LanguageCode** *(string) --*

        The language code of the input documents.

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your
        input data.

      - **ManifestFilePath** *(string) --*

        The path to the file that describes the results of a batch job.

      - **KMSKey** *(string) --*

        The AWS Key Management Service key, if any, used to encrypt the output files.

      - **ModelVersion** *(string) --*

        The version of the model used to analyze the documents. The version number looks like
        X.X.X. You can use this information to track the model used for a particular batch of
        documents.
    """


_ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef",
    {"Name": str, "Score": float},
    total=False,
)


class ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef(
    _ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef
):
    """
    Type definition for `ClientDetectEntitiesResponseEntitiesAttributes` `Traits`

    Provides contextual information about the extracted entity.

    - **Name** *(string) --*

      Provides a name or contextual description about the trait.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of
      this trait.
    """


_ClientDetectEntitiesResponseEntitiesAttributesTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesAttributesTypeDef",
    {
        "Type": str,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesResponseEntitiesAttributesTypeDef(
    _ClientDetectEntitiesResponseEntitiesAttributesTypeDef
):
    """
    Type definition for `ClientDetectEntitiesResponseEntities` `Attributes`

    An extracted segment of the text that is an attribute of an entity, or otherwise
    related to an entity, such as the dosage of a medication taken. It contains information
    about the attribute such as id, begin and end offset within the input text, and the
    segment of the input text.

    - **Type** *(string) --*

      The type of attribute.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that the segment of text
      is correctly recognized as an attribute.

    - **RelationshipScore** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that this attribute is
      correctly related to this entity.

    - **Id** *(integer) --*

      The numeric identifier for this attribute. This is a monotonically increasing id
      unique within this response rather than a global unique identifier.

    - **BeginOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute begins.
      The offset returns the UTF-8 code point in the string.

    - **EndOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute ends.
      The offset returns the UTF-8 code point in the string.

    - **Text** *(string) --*

      The segment of input text extracted as this attribute.

    - **Traits** *(list) --*

      Contextual information for this attribute.

      - *(dict) --*

        Provides contextual information about the extracted entity.

        - **Name** *(string) --*

          Provides a name or contextual description about the trait.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of
          this trait.
    """


_ClientDetectEntitiesResponseEntitiesTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesTraitsTypeDef",
    {"Name": str, "Score": float},
    total=False,
)


class ClientDetectEntitiesResponseEntitiesTraitsTypeDef(
    _ClientDetectEntitiesResponseEntitiesTraitsTypeDef
):
    """
    Type definition for `ClientDetectEntitiesResponseEntities` `Traits`

    Provides contextual information about the extracted entity.

    - **Name** *(string) --*

      Provides a name or contextual description about the trait.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of this
      trait.
    """


_ClientDetectEntitiesResponseEntitiesTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": float,
        "Text": str,
        "Category": str,
        "Type": str,
        "Traits": List[ClientDetectEntitiesResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectEntitiesResponseEntitiesAttributesTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesResponseEntitiesTypeDef(
    _ClientDetectEntitiesResponseEntitiesTypeDef
):
    """
    Type definition for `ClientDetectEntitiesResponse` `Entities`

    Provides information about an extracted medical entity.

    - **Id** *(integer) --*

      The numeric identifier for the entity. This is a monotonically increasing id unique
      within this response rather than a global unique identifier.

    - **BeginOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the entity begins. The
      offset returns the UTF-8 code point in the string.

    - **EndOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the entity ends. The
      offset returns the UTF-8 code point in the string.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of the
      detection.

    - **Text** *(string) --*

      The segment of input text extracted as this entity.

    - **Category** *(string) --*

      The category of the entity.

    - **Type** *(string) --*

      Describes the specific type of entity with category of entities.

    - **Traits** *(list) --*

      Contextual information for the entity

      - *(dict) --*

        Provides contextual information about the extracted entity.

        - **Name** *(string) --*

          Provides a name or contextual description about the trait.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of this
          trait.

    - **Attributes** *(list) --*

      The extracted attributes that relate to this entity.

      - *(dict) --*

        An extracted segment of the text that is an attribute of an entity, or otherwise
        related to an entity, such as the dosage of a medication taken. It contains information
        about the attribute such as id, begin and end offset within the input text, and the
        segment of the input text.

        - **Type** *(string) --*

          The type of attribute.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has that the segment of text
          is correctly recognized as an attribute.

        - **RelationshipScore** *(float) --*

          The level of confidence that Amazon Comprehend Medical has that this attribute is
          correctly related to this entity.

        - **Id** *(integer) --*

          The numeric identifier for this attribute. This is a monotonically increasing id
          unique within this response rather than a global unique identifier.

        - **BeginOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the attribute begins.
          The offset returns the UTF-8 code point in the string.

        - **EndOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the attribute ends.
          The offset returns the UTF-8 code point in the string.

        - **Text** *(string) --*

          The segment of input text extracted as this attribute.

        - **Traits** *(list) --*

          Contextual information for this attribute.

          - *(dict) --*

            Provides contextual information about the extracted entity.

            - **Name** *(string) --*

              Provides a name or contextual description about the trait.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has in the accuracy of
              this trait.
    """


_ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef",
    {"Name": str, "Score": float},
    total=False,
)


class ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef(
    _ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef
):
    """
    Type definition for `ClientDetectEntitiesResponseUnmappedAttributesAttribute` `Traits`

    Provides contextual information about the extracted entity.

    - **Name** *(string) --*

      Provides a name or contextual description about the trait.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of this
      trait.
    """


_ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef",
    {
        "Type": str,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[
            ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef
        ],
    },
    total=False,
)


class ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef(
    _ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef
):
    """
    Type definition for `ClientDetectEntitiesResponseUnmappedAttributes` `Attribute`

    The specific attribute that has been extracted but not mapped to an entity.

    - **Type** *(string) --*

      The type of attribute.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that the segment of text is
      correctly recognized as an attribute.

    - **RelationshipScore** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that this attribute is
      correctly related to this entity.

    - **Id** *(integer) --*

      The numeric identifier for this attribute. This is a monotonically increasing id unique
      within this response rather than a global unique identifier.

    - **BeginOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute begins.
      The offset returns the UTF-8 code point in the string.

    - **EndOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute ends. The
      offset returns the UTF-8 code point in the string.

    - **Text** *(string) --*

      The segment of input text extracted as this attribute.

    - **Traits** *(list) --*

      Contextual information for this attribute.

      - *(dict) --*

        Provides contextual information about the extracted entity.

        - **Name** *(string) --*

          Provides a name or contextual description about the trait.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of this
          trait.
    """


_ClientDetectEntitiesResponseUnmappedAttributesTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseUnmappedAttributesTypeDef",
    {
        "Type": str,
        "Attribute": ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef,
    },
    total=False,
)


class ClientDetectEntitiesResponseUnmappedAttributesTypeDef(
    _ClientDetectEntitiesResponseUnmappedAttributesTypeDef
):
    """
    Type definition for `ClientDetectEntitiesResponse` `UnmappedAttributes`

    An attribute that we extracted, but were unable to relate to an entity.

    - **Type** *(string) --*

      The type of the attribute, could be one of the following values: "MEDICATION",
      "MEDICAL_CONDITION", "ANATOMY", "TEST_AND_TREATMENT_PROCEDURE" or
      "PROTECTED_HEALTH_INFORMATION".

    - **Attribute** *(dict) --*

      The specific attribute that has been extracted but not mapped to an entity.

      - **Type** *(string) --*

        The type of attribute.

      - **Score** *(float) --*

        The level of confidence that Amazon Comprehend Medical has that the segment of text is
        correctly recognized as an attribute.

      - **RelationshipScore** *(float) --*

        The level of confidence that Amazon Comprehend Medical has that this attribute is
        correctly related to this entity.

      - **Id** *(integer) --*

        The numeric identifier for this attribute. This is a monotonically increasing id unique
        within this response rather than a global unique identifier.

      - **BeginOffset** *(integer) --*

        The 0-based character offset in the input text that shows where the attribute begins.
        The offset returns the UTF-8 code point in the string.

      - **EndOffset** *(integer) --*

        The 0-based character offset in the input text that shows where the attribute ends. The
        offset returns the UTF-8 code point in the string.

      - **Text** *(string) --*

        The segment of input text extracted as this attribute.

      - **Traits** *(list) --*

        Contextual information for this attribute.

        - *(dict) --*

          Provides contextual information about the extracted entity.

          - **Name** *(string) --*

            Provides a name or contextual description about the trait.

          - **Score** *(float) --*

            The level of confidence that Amazon Comprehend Medical has in the accuracy of this
            trait.
    """


_ClientDetectEntitiesResponseTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseTypeDef",
    {
        "Entities": List[ClientDetectEntitiesResponseEntitiesTypeDef],
        "UnmappedAttributes": List[
            ClientDetectEntitiesResponseUnmappedAttributesTypeDef
        ],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDetectEntitiesResponseTypeDef(_ClientDetectEntitiesResponseTypeDef):
    """
    Type definition for `ClientDetectEntities` `Response`

    - **Entities** *(list) --*

      The collection of medical entities extracted from the input text and their associated
      information. For each entity, the response provides the entity text, the entity category,
      where the entity text begins and ends, and the level of confidence that Amazon Comprehend
      Medical has in the detection and analysis. Attributes and traits of the entity are also
      returned.

      - *(dict) --*

        Provides information about an extracted medical entity.

        - **Id** *(integer) --*

          The numeric identifier for the entity. This is a monotonically increasing id unique
          within this response rather than a global unique identifier.

        - **BeginOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the entity begins. The
          offset returns the UTF-8 code point in the string.

        - **EndOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the entity ends. The
          offset returns the UTF-8 code point in the string.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of the
          detection.

        - **Text** *(string) --*

          The segment of input text extracted as this entity.

        - **Category** *(string) --*

          The category of the entity.

        - **Type** *(string) --*

          Describes the specific type of entity with category of entities.

        - **Traits** *(list) --*

          Contextual information for the entity

          - *(dict) --*

            Provides contextual information about the extracted entity.

            - **Name** *(string) --*

              Provides a name or contextual description about the trait.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has in the accuracy of this
              trait.

        - **Attributes** *(list) --*

          The extracted attributes that relate to this entity.

          - *(dict) --*

            An extracted segment of the text that is an attribute of an entity, or otherwise
            related to an entity, such as the dosage of a medication taken. It contains information
            about the attribute such as id, begin and end offset within the input text, and the
            segment of the input text.

            - **Type** *(string) --*

              The type of attribute.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has that the segment of text
              is correctly recognized as an attribute.

            - **RelationshipScore** *(float) --*

              The level of confidence that Amazon Comprehend Medical has that this attribute is
              correctly related to this entity.

            - **Id** *(integer) --*

              The numeric identifier for this attribute. This is a monotonically increasing id
              unique within this response rather than a global unique identifier.

            - **BeginOffset** *(integer) --*

              The 0-based character offset in the input text that shows where the attribute begins.
              The offset returns the UTF-8 code point in the string.

            - **EndOffset** *(integer) --*

              The 0-based character offset in the input text that shows where the attribute ends.
              The offset returns the UTF-8 code point in the string.

            - **Text** *(string) --*

              The segment of input text extracted as this attribute.

            - **Traits** *(list) --*

              Contextual information for this attribute.

              - *(dict) --*

                Provides contextual information about the extracted entity.

                - **Name** *(string) --*

                  Provides a name or contextual description about the trait.

                - **Score** *(float) --*

                  The level of confidence that Amazon Comprehend Medical has in the accuracy of
                  this trait.

    - **UnmappedAttributes** *(list) --*

      Attributes extracted from the input text that we were unable to relate to an entity.

      - *(dict) --*

        An attribute that we extracted, but were unable to relate to an entity.

        - **Type** *(string) --*

          The type of the attribute, could be one of the following values: "MEDICATION",
          "MEDICAL_CONDITION", "ANATOMY", "TEST_AND_TREATMENT_PROCEDURE" or
          "PROTECTED_HEALTH_INFORMATION".

        - **Attribute** *(dict) --*

          The specific attribute that has been extracted but not mapped to an entity.

          - **Type** *(string) --*

            The type of attribute.

          - **Score** *(float) --*

            The level of confidence that Amazon Comprehend Medical has that the segment of text is
            correctly recognized as an attribute.

          - **RelationshipScore** *(float) --*

            The level of confidence that Amazon Comprehend Medical has that this attribute is
            correctly related to this entity.

          - **Id** *(integer) --*

            The numeric identifier for this attribute. This is a monotonically increasing id unique
            within this response rather than a global unique identifier.

          - **BeginOffset** *(integer) --*

            The 0-based character offset in the input text that shows where the attribute begins.
            The offset returns the UTF-8 code point in the string.

          - **EndOffset** *(integer) --*

            The 0-based character offset in the input text that shows where the attribute ends. The
            offset returns the UTF-8 code point in the string.

          - **Text** *(string) --*

            The segment of input text extracted as this attribute.

          - **Traits** *(list) --*

            Contextual information for this attribute.

            - *(dict) --*

              Provides contextual information about the extracted entity.

              - **Name** *(string) --*

                Provides a name or contextual description about the trait.

              - **Score** *(float) --*

                The level of confidence that Amazon Comprehend Medical has in the accuracy of this
                trait.

    - **PaginationToken** *(string) --*

      If the result of the previous request to ``DetectEntities`` was truncated, include the
      ``PaginationToken`` to fetch the next page of entities.

    - **ModelVersion** *(string) --*

      The version of the model used to analyze the documents. The version number looks like X.X.X.
      You can use this information to track the model used for a particular batch of documents.
    """


_ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef",
    {"Name": str, "Score": float},
    total=False,
)


class ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef(
    _ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef
):
    """
    Type definition for `ClientDetectEntitiesV2ResponseEntitiesAttributes` `Traits`

    Provides contextual information about the extracted entity.

    - **Name** *(string) --*

      Provides a name or contextual description about the trait.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of
      this trait.
    """


_ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef",
    {
        "Type": str,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef(
    _ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef
):
    """
    Type definition for `ClientDetectEntitiesV2ResponseEntities` `Attributes`

    An extracted segment of the text that is an attribute of an entity, or otherwise
    related to an entity, such as the dosage of a medication taken. It contains information
    about the attribute such as id, begin and end offset within the input text, and the
    segment of the input text.

    - **Type** *(string) --*

      The type of attribute.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that the segment of text
      is correctly recognized as an attribute.

    - **RelationshipScore** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that this attribute is
      correctly related to this entity.

    - **Id** *(integer) --*

      The numeric identifier for this attribute. This is a monotonically increasing id
      unique within this response rather than a global unique identifier.

    - **BeginOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute begins.
      The offset returns the UTF-8 code point in the string.

    - **EndOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute ends.
      The offset returns the UTF-8 code point in the string.

    - **Text** *(string) --*

      The segment of input text extracted as this attribute.

    - **Traits** *(list) --*

      Contextual information for this attribute.

      - *(dict) --*

        Provides contextual information about the extracted entity.

        - **Name** *(string) --*

          Provides a name or contextual description about the trait.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of
          this trait.
    """


_ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef",
    {"Name": str, "Score": float},
    total=False,
)


class ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef(
    _ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef
):
    """
    Type definition for `ClientDetectEntitiesV2ResponseEntities` `Traits`

    Provides contextual information about the extracted entity.

    - **Name** *(string) --*

      Provides a name or contextual description about the trait.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of this
      trait.
    """


_ClientDetectEntitiesV2ResponseEntitiesTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": float,
        "Text": str,
        "Category": str,
        "Type": str,
        "Traits": List[ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseEntitiesTypeDef(
    _ClientDetectEntitiesV2ResponseEntitiesTypeDef
):
    """
    Type definition for `ClientDetectEntitiesV2Response` `Entities`

    Provides information about an extracted medical entity.

    - **Id** *(integer) --*

      The numeric identifier for the entity. This is a monotonically increasing id unique
      within this response rather than a global unique identifier.

    - **BeginOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the entity begins. The
      offset returns the UTF-8 code point in the string.

    - **EndOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the entity ends. The
      offset returns the UTF-8 code point in the string.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of the
      detection.

    - **Text** *(string) --*

      The segment of input text extracted as this entity.

    - **Category** *(string) --*

      The category of the entity.

    - **Type** *(string) --*

      Describes the specific type of entity with category of entities.

    - **Traits** *(list) --*

      Contextual information for the entity

      - *(dict) --*

        Provides contextual information about the extracted entity.

        - **Name** *(string) --*

          Provides a name or contextual description about the trait.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of this
          trait.

    - **Attributes** *(list) --*

      The extracted attributes that relate to this entity.

      - *(dict) --*

        An extracted segment of the text that is an attribute of an entity, or otherwise
        related to an entity, such as the dosage of a medication taken. It contains information
        about the attribute such as id, begin and end offset within the input text, and the
        segment of the input text.

        - **Type** *(string) --*

          The type of attribute.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has that the segment of text
          is correctly recognized as an attribute.

        - **RelationshipScore** *(float) --*

          The level of confidence that Amazon Comprehend Medical has that this attribute is
          correctly related to this entity.

        - **Id** *(integer) --*

          The numeric identifier for this attribute. This is a monotonically increasing id
          unique within this response rather than a global unique identifier.

        - **BeginOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the attribute begins.
          The offset returns the UTF-8 code point in the string.

        - **EndOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the attribute ends.
          The offset returns the UTF-8 code point in the string.

        - **Text** *(string) --*

          The segment of input text extracted as this attribute.

        - **Traits** *(list) --*

          Contextual information for this attribute.

          - *(dict) --*

            Provides contextual information about the extracted entity.

            - **Name** *(string) --*

              Provides a name or contextual description about the trait.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has in the accuracy of
              this trait.
    """


_ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef",
    {"Name": str, "Score": float},
    total=False,
)


class ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef(
    _ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef
):
    """
    Type definition for `ClientDetectEntitiesV2ResponseUnmappedAttributesAttribute` `Traits`

    Provides contextual information about the extracted entity.

    - **Name** *(string) --*

      Provides a name or contextual description about the trait.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of this
      trait.
    """


_ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef",
    {
        "Type": str,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[
            ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef
        ],
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef(
    _ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef
):
    """
    Type definition for `ClientDetectEntitiesV2ResponseUnmappedAttributes` `Attribute`

    The specific attribute that has been extracted but not mapped to an entity.

    - **Type** *(string) --*

      The type of attribute.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that the segment of text is
      correctly recognized as an attribute.

    - **RelationshipScore** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that this attribute is
      correctly related to this entity.

    - **Id** *(integer) --*

      The numeric identifier for this attribute. This is a monotonically increasing id unique
      within this response rather than a global unique identifier.

    - **BeginOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute begins.
      The offset returns the UTF-8 code point in the string.

    - **EndOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute ends. The
      offset returns the UTF-8 code point in the string.

    - **Text** *(string) --*

      The segment of input text extracted as this attribute.

    - **Traits** *(list) --*

      Contextual information for this attribute.

      - *(dict) --*

        Provides contextual information about the extracted entity.

        - **Name** *(string) --*

          Provides a name or contextual description about the trait.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of this
          trait.
    """


_ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef",
    {
        "Type": str,
        "Attribute": ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef,
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef(
    _ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef
):
    """
    Type definition for `ClientDetectEntitiesV2Response` `UnmappedAttributes`

    An attribute that we extracted, but were unable to relate to an entity.

    - **Type** *(string) --*

      The type of the attribute, could be one of the following values: "MEDICATION",
      "MEDICAL_CONDITION", "ANATOMY", "TEST_AND_TREATMENT_PROCEDURE" or
      "PROTECTED_HEALTH_INFORMATION".

    - **Attribute** *(dict) --*

      The specific attribute that has been extracted but not mapped to an entity.

      - **Type** *(string) --*

        The type of attribute.

      - **Score** *(float) --*

        The level of confidence that Amazon Comprehend Medical has that the segment of text is
        correctly recognized as an attribute.

      - **RelationshipScore** *(float) --*

        The level of confidence that Amazon Comprehend Medical has that this attribute is
        correctly related to this entity.

      - **Id** *(integer) --*

        The numeric identifier for this attribute. This is a monotonically increasing id unique
        within this response rather than a global unique identifier.

      - **BeginOffset** *(integer) --*

        The 0-based character offset in the input text that shows where the attribute begins.
        The offset returns the UTF-8 code point in the string.

      - **EndOffset** *(integer) --*

        The 0-based character offset in the input text that shows where the attribute ends. The
        offset returns the UTF-8 code point in the string.

      - **Text** *(string) --*

        The segment of input text extracted as this attribute.

      - **Traits** *(list) --*

        Contextual information for this attribute.

        - *(dict) --*

          Provides contextual information about the extracted entity.

          - **Name** *(string) --*

            Provides a name or contextual description about the trait.

          - **Score** *(float) --*

            The level of confidence that Amazon Comprehend Medical has in the accuracy of this
            trait.
    """


_ClientDetectEntitiesV2ResponseTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseTypeDef",
    {
        "Entities": List[ClientDetectEntitiesV2ResponseEntitiesTypeDef],
        "UnmappedAttributes": List[
            ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef
        ],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseTypeDef(_ClientDetectEntitiesV2ResponseTypeDef):
    """
    Type definition for `ClientDetectEntitiesV2` `Response`

    - **Entities** *(list) --*

      The collection of medical entities extracted from the input text and their associated
      information. For each entity, the response provides the entity text, the entity category,
      where the entity text begins and ends, and the level of confidence in the detection and
      analysis. Attributes and traits of the entity are also returned.

      - *(dict) --*

        Provides information about an extracted medical entity.

        - **Id** *(integer) --*

          The numeric identifier for the entity. This is a monotonically increasing id unique
          within this response rather than a global unique identifier.

        - **BeginOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the entity begins. The
          offset returns the UTF-8 code point in the string.

        - **EndOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the entity ends. The
          offset returns the UTF-8 code point in the string.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of the
          detection.

        - **Text** *(string) --*

          The segment of input text extracted as this entity.

        - **Category** *(string) --*

          The category of the entity.

        - **Type** *(string) --*

          Describes the specific type of entity with category of entities.

        - **Traits** *(list) --*

          Contextual information for the entity

          - *(dict) --*

            Provides contextual information about the extracted entity.

            - **Name** *(string) --*

              Provides a name or contextual description about the trait.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has in the accuracy of this
              trait.

        - **Attributes** *(list) --*

          The extracted attributes that relate to this entity.

          - *(dict) --*

            An extracted segment of the text that is an attribute of an entity, or otherwise
            related to an entity, such as the dosage of a medication taken. It contains information
            about the attribute such as id, begin and end offset within the input text, and the
            segment of the input text.

            - **Type** *(string) --*

              The type of attribute.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has that the segment of text
              is correctly recognized as an attribute.

            - **RelationshipScore** *(float) --*

              The level of confidence that Amazon Comprehend Medical has that this attribute is
              correctly related to this entity.

            - **Id** *(integer) --*

              The numeric identifier for this attribute. This is a monotonically increasing id
              unique within this response rather than a global unique identifier.

            - **BeginOffset** *(integer) --*

              The 0-based character offset in the input text that shows where the attribute begins.
              The offset returns the UTF-8 code point in the string.

            - **EndOffset** *(integer) --*

              The 0-based character offset in the input text that shows where the attribute ends.
              The offset returns the UTF-8 code point in the string.

            - **Text** *(string) --*

              The segment of input text extracted as this attribute.

            - **Traits** *(list) --*

              Contextual information for this attribute.

              - *(dict) --*

                Provides contextual information about the extracted entity.

                - **Name** *(string) --*

                  Provides a name or contextual description about the trait.

                - **Score** *(float) --*

                  The level of confidence that Amazon Comprehend Medical has in the accuracy of
                  this trait.

    - **UnmappedAttributes** *(list) --*

      Attributes extracted from the input text that couldn't be related to an entity.

      - *(dict) --*

        An attribute that we extracted, but were unable to relate to an entity.

        - **Type** *(string) --*

          The type of the attribute, could be one of the following values: "MEDICATION",
          "MEDICAL_CONDITION", "ANATOMY", "TEST_AND_TREATMENT_PROCEDURE" or
          "PROTECTED_HEALTH_INFORMATION".

        - **Attribute** *(dict) --*

          The specific attribute that has been extracted but not mapped to an entity.

          - **Type** *(string) --*

            The type of attribute.

          - **Score** *(float) --*

            The level of confidence that Amazon Comprehend Medical has that the segment of text is
            correctly recognized as an attribute.

          - **RelationshipScore** *(float) --*

            The level of confidence that Amazon Comprehend Medical has that this attribute is
            correctly related to this entity.

          - **Id** *(integer) --*

            The numeric identifier for this attribute. This is a monotonically increasing id unique
            within this response rather than a global unique identifier.

          - **BeginOffset** *(integer) --*

            The 0-based character offset in the input text that shows where the attribute begins.
            The offset returns the UTF-8 code point in the string.

          - **EndOffset** *(integer) --*

            The 0-based character offset in the input text that shows where the attribute ends. The
            offset returns the UTF-8 code point in the string.

          - **Text** *(string) --*

            The segment of input text extracted as this attribute.

          - **Traits** *(list) --*

            Contextual information for this attribute.

            - *(dict) --*

              Provides contextual information about the extracted entity.

              - **Name** *(string) --*

                Provides a name or contextual description about the trait.

              - **Score** *(float) --*

                The level of confidence that Amazon Comprehend Medical has in the accuracy of this
                trait.

    - **PaginationToken** *(string) --*

      If the result to the ``DetectEntitiesV2`` operation was truncated, include the
      ``PaginationToken`` to fetch the next page of entities.

    - **ModelVersion** *(string) --*

      The version of the model used to analyze the documents. The version number looks like X.X.X.
      You can use this information to track the model used for a particular batch of documents.
    """


_ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "_ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef",
    {"Name": str, "Score": float},
    total=False,
)


class ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef(
    _ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef
):
    """
    Type definition for `ClientDetectPhiResponseEntitiesAttributes` `Traits`

    Provides contextual information about the extracted entity.

    - **Name** *(string) --*

      Provides a name or contextual description about the trait.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of
      this trait.
    """


_ClientDetectPhiResponseEntitiesAttributesTypeDef = TypedDict(
    "_ClientDetectPhiResponseEntitiesAttributesTypeDef",
    {
        "Type": str,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)


class ClientDetectPhiResponseEntitiesAttributesTypeDef(
    _ClientDetectPhiResponseEntitiesAttributesTypeDef
):
    """
    Type definition for `ClientDetectPhiResponseEntities` `Attributes`

    An extracted segment of the text that is an attribute of an entity, or otherwise
    related to an entity, such as the dosage of a medication taken. It contains information
    about the attribute such as id, begin and end offset within the input text, and the
    segment of the input text.

    - **Type** *(string) --*

      The type of attribute.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that the segment of text
      is correctly recognized as an attribute.

    - **RelationshipScore** *(float) --*

      The level of confidence that Amazon Comprehend Medical has that this attribute is
      correctly related to this entity.

    - **Id** *(integer) --*

      The numeric identifier for this attribute. This is a monotonically increasing id
      unique within this response rather than a global unique identifier.

    - **BeginOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute begins.
      The offset returns the UTF-8 code point in the string.

    - **EndOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the attribute ends.
      The offset returns the UTF-8 code point in the string.

    - **Text** *(string) --*

      The segment of input text extracted as this attribute.

    - **Traits** *(list) --*

      Contextual information for this attribute.

      - *(dict) --*

        Provides contextual information about the extracted entity.

        - **Name** *(string) --*

          Provides a name or contextual description about the trait.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of
          this trait.
    """


_ClientDetectPhiResponseEntitiesTraitsTypeDef = TypedDict(
    "_ClientDetectPhiResponseEntitiesTraitsTypeDef",
    {"Name": str, "Score": float},
    total=False,
)


class ClientDetectPhiResponseEntitiesTraitsTypeDef(
    _ClientDetectPhiResponseEntitiesTraitsTypeDef
):
    """
    Type definition for `ClientDetectPhiResponseEntities` `Traits`

    Provides contextual information about the extracted entity.

    - **Name** *(string) --*

      Provides a name or contextual description about the trait.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of this
      trait.
    """


_ClientDetectPhiResponseEntitiesTypeDef = TypedDict(
    "_ClientDetectPhiResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": float,
        "Text": str,
        "Category": str,
        "Type": str,
        "Traits": List[ClientDetectPhiResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectPhiResponseEntitiesAttributesTypeDef],
    },
    total=False,
)


class ClientDetectPhiResponseEntitiesTypeDef(_ClientDetectPhiResponseEntitiesTypeDef):
    """
    Type definition for `ClientDetectPhiResponse` `Entities`

    Provides information about an extracted medical entity.

    - **Id** *(integer) --*

      The numeric identifier for the entity. This is a monotonically increasing id unique
      within this response rather than a global unique identifier.

    - **BeginOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the entity begins. The
      offset returns the UTF-8 code point in the string.

    - **EndOffset** *(integer) --*

      The 0-based character offset in the input text that shows where the entity ends. The
      offset returns the UTF-8 code point in the string.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend Medical has in the accuracy of the
      detection.

    - **Text** *(string) --*

      The segment of input text extracted as this entity.

    - **Category** *(string) --*

      The category of the entity.

    - **Type** *(string) --*

      Describes the specific type of entity with category of entities.

    - **Traits** *(list) --*

      Contextual information for the entity

      - *(dict) --*

        Provides contextual information about the extracted entity.

        - **Name** *(string) --*

          Provides a name or contextual description about the trait.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of this
          trait.

    - **Attributes** *(list) --*

      The extracted attributes that relate to this entity.

      - *(dict) --*

        An extracted segment of the text that is an attribute of an entity, or otherwise
        related to an entity, such as the dosage of a medication taken. It contains information
        about the attribute such as id, begin and end offset within the input text, and the
        segment of the input text.

        - **Type** *(string) --*

          The type of attribute.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has that the segment of text
          is correctly recognized as an attribute.

        - **RelationshipScore** *(float) --*

          The level of confidence that Amazon Comprehend Medical has that this attribute is
          correctly related to this entity.

        - **Id** *(integer) --*

          The numeric identifier for this attribute. This is a monotonically increasing id
          unique within this response rather than a global unique identifier.

        - **BeginOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the attribute begins.
          The offset returns the UTF-8 code point in the string.

        - **EndOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the attribute ends.
          The offset returns the UTF-8 code point in the string.

        - **Text** *(string) --*

          The segment of input text extracted as this attribute.

        - **Traits** *(list) --*

          Contextual information for this attribute.

          - *(dict) --*

            Provides contextual information about the extracted entity.

            - **Name** *(string) --*

              Provides a name or contextual description about the trait.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has in the accuracy of
              this trait.
    """


_ClientDetectPhiResponseTypeDef = TypedDict(
    "_ClientDetectPhiResponseTypeDef",
    {
        "Entities": List[ClientDetectPhiResponseEntitiesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDetectPhiResponseTypeDef(_ClientDetectPhiResponseTypeDef):
    """
    Type definition for `ClientDetectPhi` `Response`

    - **Entities** *(list) --*

      The collection of PHI entities extracted from the input text and their associated
      information. For each entity, the response provides the entity text, the entity category,
      where the entity text begins and ends, and the level of confidence that Amazon Comprehend
      Medical has in its detection.

      - *(dict) --*

        Provides information about an extracted medical entity.

        - **Id** *(integer) --*

          The numeric identifier for the entity. This is a monotonically increasing id unique
          within this response rather than a global unique identifier.

        - **BeginOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the entity begins. The
          offset returns the UTF-8 code point in the string.

        - **EndOffset** *(integer) --*

          The 0-based character offset in the input text that shows where the entity ends. The
          offset returns the UTF-8 code point in the string.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend Medical has in the accuracy of the
          detection.

        - **Text** *(string) --*

          The segment of input text extracted as this entity.

        - **Category** *(string) --*

          The category of the entity.

        - **Type** *(string) --*

          Describes the specific type of entity with category of entities.

        - **Traits** *(list) --*

          Contextual information for the entity

          - *(dict) --*

            Provides contextual information about the extracted entity.

            - **Name** *(string) --*

              Provides a name or contextual description about the trait.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has in the accuracy of this
              trait.

        - **Attributes** *(list) --*

          The extracted attributes that relate to this entity.

          - *(dict) --*

            An extracted segment of the text that is an attribute of an entity, or otherwise
            related to an entity, such as the dosage of a medication taken. It contains information
            about the attribute such as id, begin and end offset within the input text, and the
            segment of the input text.

            - **Type** *(string) --*

              The type of attribute.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend Medical has that the segment of text
              is correctly recognized as an attribute.

            - **RelationshipScore** *(float) --*

              The level of confidence that Amazon Comprehend Medical has that this attribute is
              correctly related to this entity.

            - **Id** *(integer) --*

              The numeric identifier for this attribute. This is a monotonically increasing id
              unique within this response rather than a global unique identifier.

            - **BeginOffset** *(integer) --*

              The 0-based character offset in the input text that shows where the attribute begins.
              The offset returns the UTF-8 code point in the string.

            - **EndOffset** *(integer) --*

              The 0-based character offset in the input text that shows where the attribute ends.
              The offset returns the UTF-8 code point in the string.

            - **Text** *(string) --*

              The segment of input text extracted as this attribute.

            - **Traits** *(list) --*

              Contextual information for this attribute.

              - *(dict) --*

                Provides contextual information about the extracted entity.

                - **Name** *(string) --*

                  Provides a name or contextual description about the trait.

                - **Score** *(float) --*

                  The level of confidence that Amazon Comprehend Medical has in the accuracy of
                  this trait.

    - **PaginationToken** *(string) --*

      If the result of the previous request to ``DetectPHI`` was truncated, include the
      ``PaginationToken`` to fetch the next page of PHI entities.

    - **ModelVersion** *(string) --*

      The version of the model used to analyze the documents. The version number looks like X.X.X.
      You can use this information to track the model used for a particular batch of documents.
    """


_ClientListEntitiesDetectionV2JobsFilterTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListEntitiesDetectionV2JobsFilterTypeDef(
    _ClientListEntitiesDetectionV2JobsFilterTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionV2Jobs` `Filter`

    Filters the jobs that are returned. You can filter jobs based on their names, status, or the date
    and time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef(
    _ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the detection job.

    - **S3Bucket** *(string) --*

      The URI of the S3 bucket that contains the input data. The bucket must be in the same
      region as the API endpoint that you are calling.

      Each file in the document collection must be less than 40 KB. You can store a maximum
      of 30 GB in the bucket.

    - **S3Key** *(string) --*

      The path to the input data files in the S3 bucket.
    """


_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef(
    _ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the detection job.

    - **S3Bucket** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output.

    - **S3Key** *(string) --*

      The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates
      an output directory using the job ID so that the output from one job does not overwrite
      the output of another.
    """


_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef(
    _ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionV2JobsResponse` `ComprehendMedicalAsyncJobPropertiesList`

    Provides information about a detection job.

    - **JobId** *(string) --*

      The identifier assigned to the detection job.

    - **JobName** *(string) --*

      The name that you assigned to the detection job.

    - **JobStatus** *(string) --*

      The current status of the detection job. If the status is ``FAILED`` , the ``Message``
      field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the detection job completed.

    - **ExpirationTime** *(datetime) --*

      The date and time that job metadata is deleted from the server. Output files in your S3
      bucket will not be deleted. After the metadata is deleted, the job will no longer appear
      in the results of the ``ListEntitiesDetectionV2Job`` or the ``ListPHIDetectionJobs``
      operation.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the detection job.

      - **S3Bucket** *(string) --*

        The URI of the S3 bucket that contains the input data. The bucket must be in the same
        region as the API endpoint that you are calling.

        Each file in the document collection must be less than 40 KB. You can store a maximum
        of 30 GB in the bucket.

      - **S3Key** *(string) --*

        The path to the input data files in the S3 bucket.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the detection job.

      - **S3Bucket** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output.

      - **S3Key** *(string) --*

        The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates
        an output directory using the job ID so that the output from one job does not overwrite
        the output of another.

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your
      input data.

    - **ManifestFilePath** *(string) --*

      The path to the file that describes the results of a batch job.

    - **KMSKey** *(string) --*

      The AWS Key Management Service key, if any, used to encrypt the output files.

    - **ModelVersion** *(string) --*

      The version of the model used to analyze the documents. The version number looks like
      X.X.X. You can use this information to track the model used for a particular batch of
      documents.
    """


_ClientListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListEntitiesDetectionV2JobsResponseTypeDef(
    _ClientListEntitiesDetectionV2JobsResponseTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionV2Jobs` `Response`

    - **ComprehendMedicalAsyncJobPropertiesList** *(list) --*

      A list containing the properties of each job returned.

      - *(dict) --*

        Provides information about a detection job.

        - **JobId** *(string) --*

          The identifier assigned to the detection job.

        - **JobName** *(string) --*

          The name that you assigned to the detection job.

        - **JobStatus** *(string) --*

          The current status of the detection job. If the status is ``FAILED`` , the ``Message``
          field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the detection job completed.

        - **ExpirationTime** *(datetime) --*

          The date and time that job metadata is deleted from the server. Output files in your S3
          bucket will not be deleted. After the metadata is deleted, the job will no longer appear
          in the results of the ``ListEntitiesDetectionV2Job`` or the ``ListPHIDetectionJobs``
          operation.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the detection job.

          - **S3Bucket** *(string) --*

            The URI of the S3 bucket that contains the input data. The bucket must be in the same
            region as the API endpoint that you are calling.

            Each file in the document collection must be less than 40 KB. You can store a maximum
            of 30 GB in the bucket.

          - **S3Key** *(string) --*

            The path to the input data files in the S3 bucket.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the detection job.

          - **S3Bucket** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output.

          - **S3Key** *(string) --*

            The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates
            an output directory using the job ID so that the output from one job does not overwrite
            the output of another.

        - **LanguageCode** *(string) --*

          The language code of the input documents.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your
          input data.

        - **ManifestFilePath** *(string) --*

          The path to the file that describes the results of a batch job.

        - **KMSKey** *(string) --*

          The AWS Key Management Service key, if any, used to encrypt the output files.

        - **ModelVersion** *(string) --*

          The version of the model used to analyze the documents. The version number looks like
          X.X.X. You can use this information to track the model used for a particular batch of
          documents.

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_ClientListPhiDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListPhiDetectionJobsFilterTypeDef(_ClientListPhiDetectionJobsFilterTypeDef):
    """
    Type definition for `ClientListPhiDetectionJobs` `Filter`

    Filters the jobs that are returned. You can filter jobs based on their names, status, or the date
    and time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef(
    _ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the detection job.

    - **S3Bucket** *(string) --*

      The URI of the S3 bucket that contains the input data. The bucket must be in the same
      region as the API endpoint that you are calling.

      Each file in the document collection must be less than 40 KB. You can store a maximum
      of 30 GB in the bucket.

    - **S3Key** *(string) --*

      The path to the input data files in the S3 bucket.
    """


_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef(
    _ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the detection job.

    - **S3Bucket** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output.

    - **S3Key** *(string) --*

      The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates
      an output directory using the job ID so that the output from one job does not overwrite
      the output of another.
    """


_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef(
    _ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
):
    """
    Type definition for `ClientListPhiDetectionJobsResponse` `ComprehendMedicalAsyncJobPropertiesList`

    Provides information about a detection job.

    - **JobId** *(string) --*

      The identifier assigned to the detection job.

    - **JobName** *(string) --*

      The name that you assigned to the detection job.

    - **JobStatus** *(string) --*

      The current status of the detection job. If the status is ``FAILED`` , the ``Message``
      field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the detection job completed.

    - **ExpirationTime** *(datetime) --*

      The date and time that job metadata is deleted from the server. Output files in your S3
      bucket will not be deleted. After the metadata is deleted, the job will no longer appear
      in the results of the ``ListEntitiesDetectionV2Job`` or the ``ListPHIDetectionJobs``
      operation.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the detection job.

      - **S3Bucket** *(string) --*

        The URI of the S3 bucket that contains the input data. The bucket must be in the same
        region as the API endpoint that you are calling.

        Each file in the document collection must be less than 40 KB. You can store a maximum
        of 30 GB in the bucket.

      - **S3Key** *(string) --*

        The path to the input data files in the S3 bucket.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the detection job.

      - **S3Bucket** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output.

      - **S3Key** *(string) --*

        The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates
        an output directory using the job ID so that the output from one job does not overwrite
        the output of another.

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your
      input data.

    - **ManifestFilePath** *(string) --*

      The path to the file that describes the results of a batch job.

    - **KMSKey** *(string) --*

      The AWS Key Management Service key, if any, used to encrypt the output files.

    - **ModelVersion** *(string) --*

      The version of the model used to analyze the documents. The version number looks like
      X.X.X. You can use this information to track the model used for a particular batch of
      documents.
    """


_ClientListPhiDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPhiDetectionJobsResponseTypeDef(
    _ClientListPhiDetectionJobsResponseTypeDef
):
    """
    Type definition for `ClientListPhiDetectionJobs` `Response`

    - **ComprehendMedicalAsyncJobPropertiesList** *(list) --*

      A list containing the properties of each job returned.

      - *(dict) --*

        Provides information about a detection job.

        - **JobId** *(string) --*

          The identifier assigned to the detection job.

        - **JobName** *(string) --*

          The name that you assigned to the detection job.

        - **JobStatus** *(string) --*

          The current status of the detection job. If the status is ``FAILED`` , the ``Message``
          field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the detection job completed.

        - **ExpirationTime** *(datetime) --*

          The date and time that job metadata is deleted from the server. Output files in your S3
          bucket will not be deleted. After the metadata is deleted, the job will no longer appear
          in the results of the ``ListEntitiesDetectionV2Job`` or the ``ListPHIDetectionJobs``
          operation.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the detection job.

          - **S3Bucket** *(string) --*

            The URI of the S3 bucket that contains the input data. The bucket must be in the same
            region as the API endpoint that you are calling.

            Each file in the document collection must be less than 40 KB. You can store a maximum
            of 30 GB in the bucket.

          - **S3Key** *(string) --*

            The path to the input data files in the S3 bucket.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the detection job.

          - **S3Bucket** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output.

          - **S3Key** *(string) --*

            The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates
            an output directory using the job ID so that the output from one job does not overwrite
            the output of another.

        - **LanguageCode** *(string) --*

          The language code of the input documents.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your
          input data.

        - **ManifestFilePath** *(string) --*

          The path to the file that describes the results of a batch job.

        - **KMSKey** *(string) --*

          The AWS Key Management Service key, if any, used to encrypt the output files.

        - **ModelVersion** *(string) --*

          The version of the model used to analyze the documents. The version number looks like
          X.X.X. You can use this information to track the model used for a particular batch of
          documents.

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef",
    {"S3Bucket": str},
)
_OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef",
    {"S3Key": str},
    total=False,
)


class ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartEntitiesDetectionV2Job` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Bucket** *(string) --* **[REQUIRED]**

      The URI of the S3 bucket that contains the input data. The bucket must be in the same region as
      the API endpoint that you are calling.

      Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB
      in the bucket.

    - **S3Key** *(string) --*

      The path to the input data files in the S3 bucket.
    """


_RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef",
    {"S3Bucket": str},
)
_OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef",
    {"S3Key": str},
    total=False,
)


class ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartEntitiesDetectionV2Job` `OutputDataConfig`

    Specifies where to send the output files.

    - **S3Bucket** *(string) --* **[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output.

    - **S3Key** *(string) --*

      The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output
      directory using the job ID so that the output from one job does not overwrite the output of
      another.
    """


_ClientStartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "_ClientStartEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartEntitiesDetectionV2JobResponseTypeDef(
    _ClientStartEntitiesDetectionV2JobResponseTypeDef
):
    """
    Type definition for `ClientStartEntitiesDetectionV2Job` `Response`

    - **JobId** *(string) --*

      The identifier generated for the job. To get the status of a job, use this identifier with
      the ``DescribeEntitiesDetectionV2Job`` operation.
    """


_RequiredClientStartPhiDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartPhiDetectionJobInputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartPhiDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartPhiDetectionJobInputDataConfigTypeDef",
    {"S3Key": str},
    total=False,
)


class ClientStartPhiDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartPhiDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartPhiDetectionJobInputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartPhiDetectionJob` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Bucket** *(string) --* **[REQUIRED]**

      The URI of the S3 bucket that contains the input data. The bucket must be in the same region as
      the API endpoint that you are calling.

      Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB
      in the bucket.

    - **S3Key** *(string) --*

      The path to the input data files in the S3 bucket.
    """


_RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef",
    {"S3Key": str},
    total=False,
)


class ClientStartPhiDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartPhiDetectionJob` `OutputDataConfig`

    Specifies where to send the output files.

    - **S3Bucket** *(string) --* **[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output.

    - **S3Key** *(string) --*

      The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output
      directory using the job ID so that the output from one job does not overwrite the output of
      another.
    """


_ClientStartPhiDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartPhiDetectionJobResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartPhiDetectionJobResponseTypeDef(
    _ClientStartPhiDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStartPhiDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier generated for the job. To get the status of a job, use this identifier with
      the ``DescribePHIDetectionJob`` operation.
    """


_ClientStopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "_ClientStopEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)


class ClientStopEntitiesDetectionV2JobResponseTypeDef(
    _ClientStopEntitiesDetectionV2JobResponseTypeDef
):
    """
    Type definition for `ClientStopEntitiesDetectionV2Job` `Response`

    - **JobId** *(string) --*

      The identifier of the medical entities detection job that was stopped.
    """


_ClientStopPhiDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopPhiDetectionJobResponseTypeDef", {"JobId": str}, total=False
)


class ClientStopPhiDetectionJobResponseTypeDef(
    _ClientStopPhiDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStopPhiDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier of the PHI detection job that was stopped.
    """
