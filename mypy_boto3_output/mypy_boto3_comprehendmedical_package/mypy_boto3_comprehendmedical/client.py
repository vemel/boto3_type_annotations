"Main interface for comprehendmedical Client"
from __future__ import annotations

from typing import Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_comprehendmedical.client as client_scope
from mypy_boto3_comprehendmedical.type_defs import (
    ClientDescribeEntitiesDetectionV2JobResponseTypeDef,
    ClientDescribePhiDetectionJobResponseTypeDef,
    ClientDetectEntitiesResponseTypeDef,
    ClientDetectEntitiesV2ResponseTypeDef,
    ClientDetectPhiResponseTypeDef,
    ClientListEntitiesDetectionV2JobsFilterTypeDef,
    ClientListEntitiesDetectionV2JobsResponseTypeDef,
    ClientListPhiDetectionJobsFilterTypeDef,
    ClientListPhiDetectionJobsResponseTypeDef,
    ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
    ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
    ClientStartEntitiesDetectionV2JobResponseTypeDef,
    ClientStartPhiDetectionJobInputDataConfigTypeDef,
    ClientStartPhiDetectionJobOutputDataConfigTypeDef,
    ClientStartPhiDetectionJobResponseTypeDef,
    ClientStopEntitiesDetectionV2JobResponseTypeDef,
    ClientStopPhiDetectionJobResponseTypeDef,
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
    def describe_entities_detection_v2_job(
        self, JobId: str
    ) -> ClientDescribeEntitiesDetectionV2JobResponseTypeDef:
        """
        Gets the properties associated with a medical entities detection job. Use this operation to get the
        status of a detection job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DescribeEntitiesDetectionV2Job>`_
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DescribeEntitiesDetectionV2Job>`_

        **Request Syntax**
        ::

          response = client.describe_entities_detection_v2_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier that Amazon Comprehend Medical generated for the job. The
          ``StartEntitiesDetectionV2Job`` operation returns this identifier in its response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ComprehendMedicalAsyncJobProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus':
                    'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'
                    |'STOPPED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'ExpirationTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'S3Bucket': 'string',
                        'S3Key': 'string'
                    },
                    'OutputDataConfig': {
                        'S3Bucket': 'string',
                        'S3Key': 'string'
                    },
                    'LanguageCode': 'en',
                    'DataAccessRoleArn': 'string',
                    'ManifestFilePath': 'string',
                    'KMSKey': 'string',
                    'ModelVersion': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_phi_detection_job(
        self, JobId: str
    ) -> ClientDescribePhiDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a protected health information (PHI) detection job. Use this
        operation to get the status of a detection job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DescribePHIDetectionJob>`_

        **Request Syntax**
        ::

          response = client.describe_phi_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier that Amazon Comprehend Medical generated for the job. The ``StartPHIDetectionJob``
          operation returns this identifier in its response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ComprehendMedicalAsyncJobProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus':
                    'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'
                    |'STOPPED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'ExpirationTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'S3Bucket': 'string',
                        'S3Key': 'string'
                    },
                    'OutputDataConfig': {
                        'S3Bucket': 'string',
                        'S3Key': 'string'
                    },
                    'LanguageCode': 'en',
                    'DataAccessRoleArn': 'string',
                    'ManifestFilePath': 'string',
                    'KMSKey': 'string',
                    'ModelVersion': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_entities(self, Text: str) -> ClientDetectEntitiesResponseTypeDef:
        """
        The ``DetectEntities`` operation is deprecated. You should use the  DetectEntitiesV2 operation
        instead.

        Inspects the clinical text for a variety of medical entities and returns specific information about
        them such as entity category, location, and confidence score on that information .

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not be
            used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DetectEntities>`_

        **Request Syntax**
        ::

          response = client.detect_entities(
              Text='string'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          A UTF-8 text string containing the clinical content being examined for entities. Each string must
          contain fewer than 20,000 bytes of characters.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Entities': [
                    {
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Score': ...,
                        'Text': 'string',
                        'Category':
                        'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'
                        |'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                        'Type':
                        'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'
                        |'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'
                        |'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'
                        |'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'
                        |'QUALITY'|'QUANTITY',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ],
                        'Attributes': [
                            {
                                'Type':
                                'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'
                                |'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'
                                |'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'
                                |'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'
                                |'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                                'Score': ...,
                                'RelationshipScore': ...,
                                'Id': 123,
                                'BeginOffset': 123,
                                'EndOffset': 123,
                                'Text': 'string',
                                'Traits': [
                                    {
                                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                        'Score': ...
                                    },
                                ]
                            },
                        ]
                    },
                ],
                'UnmappedAttributes': [
                    {
                        'Type':
                        'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'
                        |'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                        'Attribute': {
                            'Type':
                            'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'
                            |'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'
                            |'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'
                            |'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'
                            |'QUALITY'|'QUANTITY',
                            'Score': ...,
                            'RelationshipScore': ...,
                            'Id': 123,
                            'BeginOffset': 123,
                            'EndOffset': 123,
                            'Text': 'string',
                            'Traits': [
                                {
                                    'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                    'Score': ...
                                },
                            ]
                        }
                    },
                ],
                'PaginationToken': 'string',
                'ModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_entities_v2(self, Text: str) -> ClientDetectEntitiesV2ResponseTypeDef:
        """
        Inspects the clinical text for a variety of medical entities and returns specific information about
        them such as entity category, location, and confidence score on that information.

        The ``DetectEntitiesV2`` operation replaces the  DetectEntities operation. This new action uses a
        different model for determining the entities in your medical text and changes the way that some
        entities are returned in the output. You should use the ``DetectEntitiesV2`` operation in all new
        applications.

        The ``DetectEntitiesV2`` operation returns the ``Acuity`` and ``Direction`` entities as attributes
        instead of types. It does not return the ``Quality`` or ``Quantity`` entities.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DetectEntitiesV2>`_

        **Request Syntax**
        ::

          response = client.detect_entities_v2(
              Text='string'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          A UTF-8 string containing the clinical content being examined for entities. Each string must
          contain fewer than 20,000 bytes of characters.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Entities': [
                    {
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Score': ...,
                        'Text': 'string',
                        'Category':
                        'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'
                        |'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                        'Type':
                        'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'
                        |'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'
                        |'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'
                        |'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'
                        |'QUALITY'|'QUANTITY',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ],
                        'Attributes': [
                            {
                                'Type':
                                'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'
                                |'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'
                                |'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'
                                |'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'
                                |'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                                'Score': ...,
                                'RelationshipScore': ...,
                                'Id': 123,
                                'BeginOffset': 123,
                                'EndOffset': 123,
                                'Text': 'string',
                                'Traits': [
                                    {
                                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                        'Score': ...
                                    },
                                ]
                            },
                        ]
                    },
                ],
                'UnmappedAttributes': [
                    {
                        'Type':
                        'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'
                        |'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                        'Attribute': {
                            'Type':
                            'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'
                            |'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'
                            |'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'
                            |'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'
                            |'QUALITY'|'QUANTITY',
                            'Score': ...,
                            'RelationshipScore': ...,
                            'Id': 123,
                            'BeginOffset': 123,
                            'EndOffset': 123,
                            'Text': 'string',
                            'Traits': [
                                {
                                    'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                    'Score': ...
                                },
                            ]
                        }
                    },
                ],
                'PaginationToken': 'string',
                'ModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_phi(self, Text: str) -> ClientDetectPhiResponseTypeDef:
        """
        Inspects the clinical text for protected health information (PHI) entities and entity category,
        location, and confidence score on that information.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DetectPHI>`_

        **Request Syntax**
        ::

          response = client.detect_phi(
              Text='string'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          A UTF-8 text string containing the clinical content being examined for PHI entities. Each string
          must contain fewer than 20,000 bytes of characters.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Entities': [
                    {
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Score': ...,
                        'Text': 'string',
                        'Category':
                        'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'
                        |'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                        'Type':
                        'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'
                        |'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'
                        |'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'
                        |'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'
                        |'QUALITY'|'QUANTITY',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ],
                        'Attributes': [
                            {
                                'Type':
                                'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'
                                |'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'
                                |'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'
                                |'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'
                                |'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                                'Score': ...,
                                'RelationshipScore': ...,
                                'Id': 123,
                                'BeginOffset': 123,
                                'EndOffset': 123,
                                'Text': 'string',
                                'Traits': [
                                    {
                                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                        'Score': ...
                                    },
                                ]
                            },
                        ]
                    },
                ],
                'PaginationToken': 'string',
                'ModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

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
    def list_entities_detection_v2_jobs(
        self,
        Filter: ClientListEntitiesDetectionV2JobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEntitiesDetectionV2JobsResponseTypeDef:
        """
        Gets a list of medical entity detection jobs that you have submitted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/ListEntitiesDetectionV2Jobs>`_

        **Request Syntax**
        ::

          response = client.list_entities_detection_v2_jobs(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

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

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ComprehendMedicalAsyncJobPropertiesList': [
                    {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobStatus':
                        'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'
                        |'STOPPED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'ExpirationTime': datetime(2015, 1, 1),
                        'InputDataConfig': {
                            'S3Bucket': 'string',
                            'S3Key': 'string'
                        },
                        'OutputDataConfig': {
                            'S3Bucket': 'string',
                            'S3Key': 'string'
                        },
                        'LanguageCode': 'en',
                        'DataAccessRoleArn': 'string',
                        'ManifestFilePath': 'string',
                        'KMSKey': 'string',
                        'ModelVersion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_phi_detection_jobs(
        self,
        Filter: ClientListPhiDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListPhiDetectionJobsResponseTypeDef:
        """
        Gets a list of protected health information (PHI) detection jobs that you have submitted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/ListPHIDetectionJobs>`_

        **Request Syntax**
        ::

          response = client.list_phi_detection_jobs(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

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

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ComprehendMedicalAsyncJobPropertiesList': [
                    {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobStatus':
                        'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'
                        |'STOPPED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'ExpirationTime': datetime(2015, 1, 1),
                        'InputDataConfig': {
                            'S3Bucket': 'string',
                            'S3Key': 'string'
                        },
                        'OutputDataConfig': {
                            'S3Bucket': 'string',
                            'S3Key': 'string'
                        },
                        'LanguageCode': 'en',
                        'DataAccessRoleArn': 'string',
                        'ManifestFilePath': 'string',
                        'KMSKey': 'string',
                        'ModelVersion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_entities_detection_v2_job(
        self,
        InputDataConfig: ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> ClientStartEntitiesDetectionV2JobResponseTypeDef:
        """
        Starts an asynchronous medical entity detection job for a collection of documents. Use the
        ``DescribeEntitiesDetectionV2Job`` operation to track the status of a job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/StartEntitiesDetectionV2Job>`_

        **Request Syntax**
        ::

          response = client.start_entities_detection_v2_job(
              InputDataConfig={
                  'S3Bucket': 'string',
                  'S3Key': 'string'
              },
              OutputDataConfig={
                  'S3Bucket': 'string',
                  'S3Key': 'string'
              },
              DataAccessRoleArn='string',
              JobName='string',
              ClientRequestToken='string',
              KMSKey='string',
              LanguageCode='en'
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Bucket** *(string) --* **[REQUIRED]**

            The URI of the S3 bucket that contains the input data. The bucket must be in the same region as
            the API endpoint that you are calling.

            Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB
            in the bucket.

          - **S3Key** *(string) --*

            The path to the input data files in the S3 bucket.

        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**

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

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants
          Amazon Comprehend Medical read access to your input data. For more information, see `Role-Based
          Permissions Required for Asynchronous Operations
          <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med>`__
          .

        :type JobName: string
        :param JobName:

          The identifier of the job.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you don't set the client request token, Amazon Comprehend
          Medical generates one.

          This field is autopopulated if not provided.

        :type KMSKey: string
        :param KMSKey:

          An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the
          files are written in plain text.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier generated for the job. To get the status of a job, use this identifier with
              the ``DescribeEntitiesDetectionV2Job`` operation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_phi_detection_job(
        self,
        InputDataConfig: ClientStartPhiDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartPhiDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> ClientStartPhiDetectionJobResponseTypeDef:
        """
        Starts an asynchronous job to detect protected health information (PHI). Use the
        ``DescribePHIDetectionJob`` operation to track the status of a job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/StartPHIDetectionJob>`_

        **Request Syntax**
        ::

          response = client.start_phi_detection_job(
              InputDataConfig={
                  'S3Bucket': 'string',
                  'S3Key': 'string'
              },
              OutputDataConfig={
                  'S3Bucket': 'string',
                  'S3Key': 'string'
              },
              DataAccessRoleArn='string',
              JobName='string',
              ClientRequestToken='string',
              KMSKey='string',
              LanguageCode='en'
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Bucket** *(string) --* **[REQUIRED]**

            The URI of the S3 bucket that contains the input data. The bucket must be in the same region as
            the API endpoint that you are calling.

            Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB
            in the bucket.

          - **S3Key** *(string) --*

            The path to the input data files in the S3 bucket.

        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**

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

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants
          Amazon Comprehend Medical read access to your input data. For more information, see `Role-Based
          Permissions Required for Asynchronous Operations
          <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med>`__
          .

        :type JobName: string
        :param JobName:

          The identifier of the job.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you don't set the client request token, Amazon Comprehend
          Medical generates one.

          This field is autopopulated if not provided.

        :type KMSKey: string
        :param KMSKey:

          An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the
          files are written in plain text.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier generated for the job. To get the status of a job, use this identifier with
              the ``DescribePHIDetectionJob`` operation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_entities_detection_v2_job(
        self, JobId: str
    ) -> ClientStopEntitiesDetectionV2JobResponseTypeDef:
        """
        Stops a medical entities detection job in progress.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/StopEntitiesDetectionV2Job>`_

        **Request Syntax**
        ::

          response = client.stop_entities_detection_v2_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier of the medical entities job to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier of the medical entities detection job that was stopped.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_phi_detection_job(
        self, JobId: str
    ) -> ClientStopPhiDetectionJobResponseTypeDef:
        """
        Stops a protected health information (PHI) detection job in progress.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/StopPHIDetectionJob>`_

        **Request Syntax**
        ::

          response = client.stop_phi_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier of the PHI detection job to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier of the PHI detection job that was stopped.

        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidEncodingException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TextSizeLimitExceededException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    ValidationException: Boto3ClientError
