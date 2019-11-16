"Main interface for personalize type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateBatchInferenceJobResponseTypeDef",
    "ClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef",
    "ClientCreateBatchInferenceJobjobInputTypeDef",
    "ClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef",
    "ClientCreateBatchInferenceJobjobOutputTypeDef",
    "ClientCreateCampaignResponseTypeDef",
    "ClientCreateDatasetGroupResponseTypeDef",
    "ClientCreateDatasetImportJobResponseTypeDef",
    "ClientCreateDatasetImportJobdataSourceTypeDef",
    "ClientCreateDatasetResponseTypeDef",
    "ClientCreateEventTrackerResponseTypeDef",
    "ClientCreateSchemaResponseTypeDef",
    "ClientCreateSolutionResponseTypeDef",
    "ClientCreateSolutionVersionResponseTypeDef",
    "ClientCreateSolutionsolutionConfigautoMLConfigTypeDef",
    "ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientCreateSolutionsolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientCreateSolutionsolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientCreateSolutionsolutionConfighpoConfigTypeDef",
    "ClientCreateSolutionsolutionConfigTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmTypeDef",
    "ClientDescribeAlgorithmResponseTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef",
    "ClientDescribeBatchInferenceJobResponseTypeDef",
    "ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef",
    "ClientDescribeCampaignResponsecampaignTypeDef",
    "ClientDescribeCampaignResponseTypeDef",
    "ClientDescribeDatasetGroupResponsedatasetGroupTypeDef",
    "ClientDescribeDatasetGroupResponseTypeDef",
    "ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef",
    "ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef",
    "ClientDescribeDatasetImportJobResponseTypeDef",
    "ClientDescribeDatasetResponsedatasetTypeDef",
    "ClientDescribeDatasetResponseTypeDef",
    "ClientDescribeEventTrackerResponseeventTrackerTypeDef",
    "ClientDescribeEventTrackerResponseTypeDef",
    "ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef",
    "ClientDescribeFeatureTransformationResponseTypeDef",
    "ClientDescribeRecipeResponserecipeTypeDef",
    "ClientDescribeRecipeResponseTypeDef",
    "ClientDescribeSchemaResponseschemaTypeDef",
    "ClientDescribeSchemaResponseTypeDef",
    "ClientDescribeSolutionResponsesolutionautoMLResultTypeDef",
    "ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionTypeDef",
    "ClientDescribeSolutionResponseTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionTypeDef",
    "ClientDescribeSolutionVersionResponseTypeDef",
    "ClientGetSolutionMetricsResponseTypeDef",
    "ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef",
    "ClientListBatchInferenceJobsResponseTypeDef",
    "ClientListCampaignsResponsecampaignsTypeDef",
    "ClientListCampaignsResponseTypeDef",
    "ClientListDatasetGroupsResponsedatasetGroupsTypeDef",
    "ClientListDatasetGroupsResponseTypeDef",
    "ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef",
    "ClientListDatasetImportJobsResponseTypeDef",
    "ClientListDatasetsResponsedatasetsTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListEventTrackersResponseeventTrackersTypeDef",
    "ClientListEventTrackersResponseTypeDef",
    "ClientListRecipesResponserecipesTypeDef",
    "ClientListRecipesResponseTypeDef",
    "ClientListSchemasResponseschemasTypeDef",
    "ClientListSchemasResponseTypeDef",
    "ClientListSolutionVersionsResponsesolutionVersionsTypeDef",
    "ClientListSolutionVersionsResponseTypeDef",
    "ClientListSolutionsResponsesolutionsTypeDef",
    "ClientListSolutionsResponseTypeDef",
    "ClientUpdateCampaignResponseTypeDef",
    "ListBatchInferenceJobsPaginatePaginationConfigTypeDef",
    "ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef",
    "ListBatchInferenceJobsPaginateResponseTypeDef",
    "ListCampaignsPaginatePaginationConfigTypeDef",
    "ListCampaignsPaginateResponsecampaignsTypeDef",
    "ListCampaignsPaginateResponseTypeDef",
    "ListDatasetGroupsPaginatePaginationConfigTypeDef",
    "ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef",
    "ListDatasetGroupsPaginateResponseTypeDef",
    "ListDatasetImportJobsPaginatePaginationConfigTypeDef",
    "ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef",
    "ListDatasetImportJobsPaginateResponseTypeDef",
    "ListDatasetsPaginatePaginationConfigTypeDef",
    "ListDatasetsPaginateResponsedatasetsTypeDef",
    "ListDatasetsPaginateResponseTypeDef",
    "ListEventTrackersPaginatePaginationConfigTypeDef",
    "ListEventTrackersPaginateResponseeventTrackersTypeDef",
    "ListEventTrackersPaginateResponseTypeDef",
    "ListRecipesPaginatePaginationConfigTypeDef",
    "ListRecipesPaginateResponserecipesTypeDef",
    "ListRecipesPaginateResponseTypeDef",
    "ListSchemasPaginatePaginationConfigTypeDef",
    "ListSchemasPaginateResponseschemasTypeDef",
    "ListSchemasPaginateResponseTypeDef",
    "ListSolutionVersionsPaginatePaginationConfigTypeDef",
    "ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef",
    "ListSolutionVersionsPaginateResponseTypeDef",
    "ListSolutionsPaginatePaginationConfigTypeDef",
    "ListSolutionsPaginateResponsesolutionsTypeDef",
    "ListSolutionsPaginateResponseTypeDef",
)


_ClientCreateBatchInferenceJobResponseTypeDef = TypedDict(
    "_ClientCreateBatchInferenceJobResponseTypeDef",
    {"batchInferenceJobArn": str},
    total=False,
)


class ClientCreateBatchInferenceJobResponseTypeDef(
    _ClientCreateBatchInferenceJobResponseTypeDef
):
    """
    Type definition for `ClientCreateBatchInferenceJob` `Response`

    - **batchInferenceJobArn** *(string) --*

      The ARN of the batch inference job.
    """


_RequiredClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef = TypedDict(
    "_RequiredClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef", {"path": str}
)
_OptionalClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef = TypedDict(
    "_OptionalClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef",
    {"kmsKeyArn": str},
    total=False,
)


class ClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef(
    _RequiredClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef,
    _OptionalClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef,
):
    """
    Type definition for `ClientCreateBatchInferenceJobjobInput` `s3DataSource`

    The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be
    in the same region as the API endpoint you are calling.

    - **path** *(string) --* **[REQUIRED]**

      The file path of the Amazon S3 bucket.

    - **kmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that Amazon
      Personalize uses to encrypt or decrypt the input and output files of a batch inference job.
    """


_ClientCreateBatchInferenceJobjobInputTypeDef = TypedDict(
    "_ClientCreateBatchInferenceJobjobInputTypeDef",
    {"s3DataSource": ClientCreateBatchInferenceJobjobInputs3DataSourceTypeDef},
)


class ClientCreateBatchInferenceJobjobInputTypeDef(
    _ClientCreateBatchInferenceJobjobInputTypeDef
):
    """
    Type definition for `ClientCreateBatchInferenceJob` `jobInput`

    The Amazon S3 path that leads to the input file to base your recommendations on. The input
    material must be in JSON format.

    - **s3DataSource** *(dict) --* **[REQUIRED]**

      The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be
      in the same region as the API endpoint you are calling.

      - **path** *(string) --* **[REQUIRED]**

        The file path of the Amazon S3 bucket.

      - **kmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that Amazon
        Personalize uses to encrypt or decrypt the input and output files of a batch inference job.
    """


_RequiredClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef = TypedDict(
    "_RequiredClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef",
    {"path": str},
)
_OptionalClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef = TypedDict(
    "_OptionalClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef",
    {"kmsKeyArn": str},
    total=False,
)


class ClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef(
    _RequiredClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef,
    _OptionalClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef,
):
    """
    Type definition for `ClientCreateBatchInferenceJobjobOutput` `s3DataDestination`

    Information on the Amazon S3 bucket in which the batch inference job's output is stored.

    - **path** *(string) --* **[REQUIRED]**

      The file path of the Amazon S3 bucket.

    - **kmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that Amazon
      Personalize uses to encrypt or decrypt the input and output files of a batch inference job.
    """


_ClientCreateBatchInferenceJobjobOutputTypeDef = TypedDict(
    "_ClientCreateBatchInferenceJobjobOutputTypeDef",
    {
        "s3DataDestination": ClientCreateBatchInferenceJobjobOutputs3DataDestinationTypeDef
    },
)


class ClientCreateBatchInferenceJobjobOutputTypeDef(
    _ClientCreateBatchInferenceJobjobOutputTypeDef
):
    """
    Type definition for `ClientCreateBatchInferenceJob` `jobOutput`

    The path to the Amazon S3 bucket where the job's output will be stored.

    - **s3DataDestination** *(dict) --* **[REQUIRED]**

      Information on the Amazon S3 bucket in which the batch inference job's output is stored.

      - **path** *(string) --* **[REQUIRED]**

        The file path of the Amazon S3 bucket.

      - **kmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that Amazon
        Personalize uses to encrypt or decrypt the input and output files of a batch inference job.
    """


_ClientCreateCampaignResponseTypeDef = TypedDict(
    "_ClientCreateCampaignResponseTypeDef", {"campaignArn": str}, total=False
)


class ClientCreateCampaignResponseTypeDef(_ClientCreateCampaignResponseTypeDef):
    """
    Type definition for `ClientCreateCampaign` `Response`

    - **campaignArn** *(string) --*

      The Amazon Resource Name (ARN) of the campaign.
    """


_ClientCreateDatasetGroupResponseTypeDef = TypedDict(
    "_ClientCreateDatasetGroupResponseTypeDef", {"datasetGroupArn": str}, total=False
)


class ClientCreateDatasetGroupResponseTypeDef(_ClientCreateDatasetGroupResponseTypeDef):
    """
    Type definition for `ClientCreateDatasetGroup` `Response`

    - **datasetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the new dataset group.
    """


_ClientCreateDatasetImportJobResponseTypeDef = TypedDict(
    "_ClientCreateDatasetImportJobResponseTypeDef",
    {"datasetImportJobArn": str},
    total=False,
)


class ClientCreateDatasetImportJobResponseTypeDef(
    _ClientCreateDatasetImportJobResponseTypeDef
):
    """
    Type definition for `ClientCreateDatasetImportJob` `Response`

    - **datasetImportJobArn** *(string) --*

      The ARN of the dataset import job.
    """


_ClientCreateDatasetImportJobdataSourceTypeDef = TypedDict(
    "_ClientCreateDatasetImportJobdataSourceTypeDef", {"dataLocation": str}, total=False
)


class ClientCreateDatasetImportJobdataSourceTypeDef(
    _ClientCreateDatasetImportJobdataSourceTypeDef
):
    """
    Type definition for `ClientCreateDatasetImportJob` `dataSource`

    The Amazon S3 bucket that contains the training data to import.

    - **dataLocation** *(string) --*

      The path to the Amazon S3 bucket where the data that you want to upload to your dataset is
      stored. For example:

       ``s3://bucket-name/training-data.csv``
    """


_ClientCreateDatasetResponseTypeDef = TypedDict(
    "_ClientCreateDatasetResponseTypeDef", {"datasetArn": str}, total=False
)


class ClientCreateDatasetResponseTypeDef(_ClientCreateDatasetResponseTypeDef):
    """
    Type definition for `ClientCreateDataset` `Response`

    - **datasetArn** *(string) --*

      The ARN of the dataset.
    """


_ClientCreateEventTrackerResponseTypeDef = TypedDict(
    "_ClientCreateEventTrackerResponseTypeDef",
    {"eventTrackerArn": str, "trackingId": str},
    total=False,
)


class ClientCreateEventTrackerResponseTypeDef(_ClientCreateEventTrackerResponseTypeDef):
    """
    Type definition for `ClientCreateEventTracker` `Response`

    - **eventTrackerArn** *(string) --*

      The ARN of the event tracker.

    - **trackingId** *(string) --*

      The ID of the event tracker. Include this ID in requests to the `PutEvents
      <https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html>`__ API.
    """


_ClientCreateSchemaResponseTypeDef = TypedDict(
    "_ClientCreateSchemaResponseTypeDef", {"schemaArn": str}, total=False
)


class ClientCreateSchemaResponseTypeDef(_ClientCreateSchemaResponseTypeDef):
    """
    Type definition for `ClientCreateSchema` `Response`

    - **schemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the created schema.
    """


_ClientCreateSolutionResponseTypeDef = TypedDict(
    "_ClientCreateSolutionResponseTypeDef", {"solutionArn": str}, total=False
)


class ClientCreateSolutionResponseTypeDef(_ClientCreateSolutionResponseTypeDef):
    """
    Type definition for `ClientCreateSolution` `Response`

    - **solutionArn** *(string) --*

      The ARN of the solution.
    """


_ClientCreateSolutionVersionResponseTypeDef = TypedDict(
    "_ClientCreateSolutionVersionResponseTypeDef",
    {"solutionVersionArn": str},
    total=False,
)


class ClientCreateSolutionVersionResponseTypeDef(
    _ClientCreateSolutionVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateSolutionVersion` `Response`

    - **solutionVersionArn** *(string) --*

      The ARN of the new solution version.
    """


_ClientCreateSolutionsolutionConfigautoMLConfigTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)


class ClientCreateSolutionsolutionConfigautoMLConfigTypeDef(
    _ClientCreateSolutionsolutionConfigautoMLConfigTypeDef
):
    """
    Type definition for `ClientCreateSolutionsolutionConfig` `autoMLConfig`

    The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

    - **metricName** *(string) --*

      The metric to optimize.

    - **recipeList** *(list) --*

      The list of candidate recipes.

      - *(string) --*
    """


_ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef(
    _ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRanges` `categoricalHyperParameterRanges`

    Provides the name and range of a categorical hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **values** *(list) --*

      A list of the categories for the hyperparameter.

      - *(string) --*
    """


_ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)


class ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef(
    _ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRanges` `continuousHyperParameterRanges`

    Provides the name and range of a continuous hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **minValue** *(float) --*

      The minimum allowable value for the hyperparameter.

    - **maxValue** *(float) --*

      The maximum allowable value for the hyperparameter.
    """


_ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)


class ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef(
    _ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRanges` `integerHyperParameterRanges`

    Provides the name and range of an integer-valued hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **minValue** *(integer) --*

      The minimum allowable value for the hyperparameter.

    - **maxValue** *(integer) --*

      The maximum allowable value for the hyperparameter.
    """


_ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef(
    _ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientCreateSolutionsolutionConfighpoConfig` `algorithmHyperParameterRanges`

    The hyperparameters and their allowable ranges.

    - **integerHyperParameterRanges** *(list) --*

      The integer-valued hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of an integer-valued hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **minValue** *(integer) --*

          The minimum allowable value for the hyperparameter.

        - **maxValue** *(integer) --*

          The maximum allowable value for the hyperparameter.

    - **continuousHyperParameterRanges** *(list) --*

      The continuous hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of a continuous hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **minValue** *(float) --*

          The minimum allowable value for the hyperparameter.

        - **maxValue** *(float) --*

          The maximum allowable value for the hyperparameter.

    - **categoricalHyperParameterRanges** *(list) --*

      The categorical hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of a categorical hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **values** *(list) --*

          A list of the categories for the hyperparameter.

          - *(string) --*
    """


_ClientCreateSolutionsolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)


class ClientCreateSolutionsolutionConfighpoConfighpoObjectiveTypeDef(
    _ClientCreateSolutionsolutionConfighpoConfighpoObjectiveTypeDef
):
    """
    Type definition for `ClientCreateSolutionsolutionConfighpoConfig` `hpoObjective`

    The metric to optimize during HPO.

    - **type** *(string) --*

      The data type of the metric.

    - **metricName** *(string) --*

      The name of the metric.

    - **metricRegex** *(string) --*

      A regular expression for finding the metric in the training job logs.
    """


_ClientCreateSolutionsolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)


class ClientCreateSolutionsolutionConfighpoConfighpoResourceConfigTypeDef(
    _ClientCreateSolutionsolutionConfighpoConfighpoResourceConfigTypeDef
):
    """
    Type definition for `ClientCreateSolutionsolutionConfighpoConfig` `hpoResourceConfig`

    Describes the resource configuration for HPO.

    - **maxNumberOfTrainingJobs** *(string) --*

      The maximum number of training jobs when you create a solution version. The maximum value
      for ``maxNumberOfTrainingJobs`` is ``40`` .

    - **maxParallelTrainingJobs** *(string) --*

      The maximum number of parallel training jobs when you create a solution version. The
      maximum value for ``maxParallelTrainingJobs`` is ``10`` .
    """


_ClientCreateSolutionsolutionConfighpoConfigTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientCreateSolutionsolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientCreateSolutionsolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientCreateSolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)


class ClientCreateSolutionsolutionConfighpoConfigTypeDef(
    _ClientCreateSolutionsolutionConfighpoConfigTypeDef
):
    """
    Type definition for `ClientCreateSolutionsolutionConfig` `hpoConfig`

    Describes the properties for hyperparameter optimization (HPO).

    - **hpoObjective** *(dict) --*

      The metric to optimize during HPO.

      - **type** *(string) --*

        The data type of the metric.

      - **metricName** *(string) --*

        The name of the metric.

      - **metricRegex** *(string) --*

        A regular expression for finding the metric in the training job logs.

    - **hpoResourceConfig** *(dict) --*

      Describes the resource configuration for HPO.

      - **maxNumberOfTrainingJobs** *(string) --*

        The maximum number of training jobs when you create a solution version. The maximum value
        for ``maxNumberOfTrainingJobs`` is ``40`` .

      - **maxParallelTrainingJobs** *(string) --*

        The maximum number of parallel training jobs when you create a solution version. The
        maximum value for ``maxParallelTrainingJobs`` is ``10`` .

    - **algorithmHyperParameterRanges** *(dict) --*

      The hyperparameters and their allowable ranges.

      - **integerHyperParameterRanges** *(list) --*

        The integer-valued hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of an integer-valued hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **minValue** *(integer) --*

            The minimum allowable value for the hyperparameter.

          - **maxValue** *(integer) --*

            The maximum allowable value for the hyperparameter.

      - **continuousHyperParameterRanges** *(list) --*

        The continuous hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of a continuous hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **minValue** *(float) --*

            The minimum allowable value for the hyperparameter.

          - **maxValue** *(float) --*

            The maximum allowable value for the hyperparameter.

      - **categoricalHyperParameterRanges** *(list) --*

        The categorical hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of a categorical hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **values** *(list) --*

            A list of the categories for the hyperparameter.

            - *(string) --*
    """


_ClientCreateSolutionsolutionConfigTypeDef = TypedDict(
    "_ClientCreateSolutionsolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientCreateSolutionsolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientCreateSolutionsolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)


class ClientCreateSolutionsolutionConfigTypeDef(
    _ClientCreateSolutionsolutionConfigTypeDef
):
    """
    Type definition for `ClientCreateSolution` `solutionConfig`

    The configuration to use with the solution. When ``performAutoML`` is set to true, Amazon
    Personalize only evaluates the ``autoMLConfig`` section of the solution configuration.

    - **eventValueThreshold** *(string) --*

      Only events with a value greater than or equal to this threshold are used for training a model.

    - **hpoConfig** *(dict) --*

      Describes the properties for hyperparameter optimization (HPO).

      - **hpoObjective** *(dict) --*

        The metric to optimize during HPO.

        - **type** *(string) --*

          The data type of the metric.

        - **metricName** *(string) --*

          The name of the metric.

        - **metricRegex** *(string) --*

          A regular expression for finding the metric in the training job logs.

      - **hpoResourceConfig** *(dict) --*

        Describes the resource configuration for HPO.

        - **maxNumberOfTrainingJobs** *(string) --*

          The maximum number of training jobs when you create a solution version. The maximum value
          for ``maxNumberOfTrainingJobs`` is ``40`` .

        - **maxParallelTrainingJobs** *(string) --*

          The maximum number of parallel training jobs when you create a solution version. The
          maximum value for ``maxParallelTrainingJobs`` is ``10`` .

      - **algorithmHyperParameterRanges** *(dict) --*

        The hyperparameters and their allowable ranges.

        - **integerHyperParameterRanges** *(list) --*

          The integer-valued hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of an integer-valued hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **minValue** *(integer) --*

              The minimum allowable value for the hyperparameter.

            - **maxValue** *(integer) --*

              The maximum allowable value for the hyperparameter.

        - **continuousHyperParameterRanges** *(list) --*

          The continuous hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of a continuous hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **minValue** *(float) --*

              The minimum allowable value for the hyperparameter.

            - **maxValue** *(float) --*

              The maximum allowable value for the hyperparameter.

        - **categoricalHyperParameterRanges** *(list) --*

          The categorical hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of a categorical hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **values** *(list) --*

              A list of the categories for the hyperparameter.

              - *(string) --*

    - **algorithmHyperParameters** *(dict) --*

      Lists the hyperparameter names and ranges.

      - *(string) --*

        - *(string) --*

    - **featureTransformationParameters** *(dict) --*

      Lists the feature transformation parameters.

      - *(string) --*

        - *(string) --*

    - **autoMLConfig** *(dict) --*

      The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

      - **metricName** *(string) --*

        The metric to optimize.

      - **recipeList** *(list) --*

        The list of candidate recipes.

        - *(string) --*
    """


_ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef",
    {"name": str, "dockerURI": str},
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef
):
    """
    Type definition for `ClientDescribeAlgorithmResponsealgorithm` `algorithmImage`

    The URI of the Docker container for the algorithm image.

    - **name** *(string) --*

      The name of the algorithm image.

    - **dockerURI** *(string) --*

      The URI of the Docker container for the algorithm image.
    """


_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str], "isTunable": bool},
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRanges` `categoricalHyperParameterRanges`

    Provides the name and default range of a categorical hyperparameter and whether the
    hyperparameter is tunable. A tunable hyperparameter can have its value determined
    during hyperparameter optimization (HPO).

    - **name** *(string) --*

      The name of the hyperparameter.

    - **values** *(list) --*

      A list of the categories for the hyperparameter.

      - *(string) --*

    - **isTunable** *(boolean) --*

      Whether the hyperparameter is tunable.
    """


_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float, "isTunable": bool},
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRanges` `continuousHyperParameterRanges`

    Provides the name and default range of a continuous hyperparameter and whether the
    hyperparameter is tunable. A tunable hyperparameter can have its value determined
    during hyperparameter optimization (HPO).

    - **name** *(string) --*

      The name of the hyperparameter.

    - **minValue** *(float) --*

      The minimum allowable value for the hyperparameter.

    - **maxValue** *(float) --*

      The maximum allowable value for the hyperparameter.

    - **isTunable** *(boolean) --*

      Whether the hyperparameter is tunable.
    """


_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int, "isTunable": bool},
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRanges` `integerHyperParameterRanges`

    Provides the name and default range of a integer-valued hyperparameter and whether the
    hyperparameter is tunable. A tunable hyperparameter can have its value determined
    during hyperparameter optimization (HPO).

    - **name** *(string) --*

      The name of the hyperparameter.

    - **minValue** *(integer) --*

      The minimum allowable value for the hyperparameter.

    - **maxValue** *(integer) --*

      The maximum allowable value for the hyperparameter.

    - **isTunable** *(boolean) --*

      Indicates whether the hyperparameter is tunable.
    """


_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeAlgorithmResponsealgorithm` `defaultHyperParameterRanges`

    Specifies the default hyperparameters, their ranges, and whether they are tunable. A
    tunable hyperparameter can have its value determined during hyperparameter optimization
    (HPO).

    - **integerHyperParameterRanges** *(list) --*

      The integer-valued hyperparameters and their default ranges.

      - *(dict) --*

        Provides the name and default range of a integer-valued hyperparameter and whether the
        hyperparameter is tunable. A tunable hyperparameter can have its value determined
        during hyperparameter optimization (HPO).

        - **name** *(string) --*

          The name of the hyperparameter.

        - **minValue** *(integer) --*

          The minimum allowable value for the hyperparameter.

        - **maxValue** *(integer) --*

          The maximum allowable value for the hyperparameter.

        - **isTunable** *(boolean) --*

          Indicates whether the hyperparameter is tunable.

    - **continuousHyperParameterRanges** *(list) --*

      The continuous hyperparameters and their default ranges.

      - *(dict) --*

        Provides the name and default range of a continuous hyperparameter and whether the
        hyperparameter is tunable. A tunable hyperparameter can have its value determined
        during hyperparameter optimization (HPO).

        - **name** *(string) --*

          The name of the hyperparameter.

        - **minValue** *(float) --*

          The minimum allowable value for the hyperparameter.

        - **maxValue** *(float) --*

          The maximum allowable value for the hyperparameter.

        - **isTunable** *(boolean) --*

          Whether the hyperparameter is tunable.

    - **categoricalHyperParameterRanges** *(list) --*

      The categorical hyperparameters and their default ranges.

      - *(dict) --*

        Provides the name and default range of a categorical hyperparameter and whether the
        hyperparameter is tunable. A tunable hyperparameter can have its value determined
        during hyperparameter optimization (HPO).

        - **name** *(string) --*

          The name of the hyperparameter.

        - **values** *(list) --*

          A list of the categories for the hyperparameter.

          - *(string) --*

        - **isTunable** *(boolean) --*

          Whether the hyperparameter is tunable.
    """


_ClientDescribeAlgorithmResponsealgorithmTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmTypeDef",
    {
        "name": str,
        "algorithmArn": str,
        "algorithmImage": ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef,
        "defaultHyperParameters": Dict[str, str],
        "defaultHyperParameterRanges": ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef,
        "defaultResourceConfig": Dict[str, str],
        "trainingInputMode": str,
        "roleArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmTypeDef
):
    """
    Type definition for `ClientDescribeAlgorithmResponse` `algorithm`

    A listing of the properties of the algorithm.

    - **name** *(string) --*

      The name of the algorithm.

    - **algorithmArn** *(string) --*

      The Amazon Resource Name (ARN) of the algorithm.

    - **algorithmImage** *(dict) --*

      The URI of the Docker container for the algorithm image.

      - **name** *(string) --*

        The name of the algorithm image.

      - **dockerURI** *(string) --*

        The URI of the Docker container for the algorithm image.

    - **defaultHyperParameters** *(dict) --*

      Specifies the default hyperparameters.

      - *(string) --*

        - *(string) --*

    - **defaultHyperParameterRanges** *(dict) --*

      Specifies the default hyperparameters, their ranges, and whether they are tunable. A
      tunable hyperparameter can have its value determined during hyperparameter optimization
      (HPO).

      - **integerHyperParameterRanges** *(list) --*

        The integer-valued hyperparameters and their default ranges.

        - *(dict) --*

          Provides the name and default range of a integer-valued hyperparameter and whether the
          hyperparameter is tunable. A tunable hyperparameter can have its value determined
          during hyperparameter optimization (HPO).

          - **name** *(string) --*

            The name of the hyperparameter.

          - **minValue** *(integer) --*

            The minimum allowable value for the hyperparameter.

          - **maxValue** *(integer) --*

            The maximum allowable value for the hyperparameter.

          - **isTunable** *(boolean) --*

            Indicates whether the hyperparameter is tunable.

      - **continuousHyperParameterRanges** *(list) --*

        The continuous hyperparameters and their default ranges.

        - *(dict) --*

          Provides the name and default range of a continuous hyperparameter and whether the
          hyperparameter is tunable. A tunable hyperparameter can have its value determined
          during hyperparameter optimization (HPO).

          - **name** *(string) --*

            The name of the hyperparameter.

          - **minValue** *(float) --*

            The minimum allowable value for the hyperparameter.

          - **maxValue** *(float) --*

            The maximum allowable value for the hyperparameter.

          - **isTunable** *(boolean) --*

            Whether the hyperparameter is tunable.

      - **categoricalHyperParameterRanges** *(list) --*

        The categorical hyperparameters and their default ranges.

        - *(dict) --*

          Provides the name and default range of a categorical hyperparameter and whether the
          hyperparameter is tunable. A tunable hyperparameter can have its value determined
          during hyperparameter optimization (HPO).

          - **name** *(string) --*

            The name of the hyperparameter.

          - **values** *(list) --*

            A list of the categories for the hyperparameter.

            - *(string) --*

          - **isTunable** *(boolean) --*

            Whether the hyperparameter is tunable.

    - **defaultResourceConfig** *(dict) --*

      Specifies the default maximum number of training jobs and parallel training jobs.

      - *(string) --*

        - *(string) --*

    - **trainingInputMode** *(string) --*

      The training input mode.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) of the role.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the algorithm was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the algorithm was last updated.
    """


_ClientDescribeAlgorithmResponseTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTypeDef",
    {"algorithm": ClientDescribeAlgorithmResponsealgorithmTypeDef},
    total=False,
)


class ClientDescribeAlgorithmResponseTypeDef(_ClientDescribeAlgorithmResponseTypeDef):
    """
    Type definition for `ClientDescribeAlgorithm` `Response`

    - **algorithm** *(dict) --*

      A listing of the properties of the algorithm.

      - **name** *(string) --*

        The name of the algorithm.

      - **algorithmArn** *(string) --*

        The Amazon Resource Name (ARN) of the algorithm.

      - **algorithmImage** *(dict) --*

        The URI of the Docker container for the algorithm image.

        - **name** *(string) --*

          The name of the algorithm image.

        - **dockerURI** *(string) --*

          The URI of the Docker container for the algorithm image.

      - **defaultHyperParameters** *(dict) --*

        Specifies the default hyperparameters.

        - *(string) --*

          - *(string) --*

      - **defaultHyperParameterRanges** *(dict) --*

        Specifies the default hyperparameters, their ranges, and whether they are tunable. A
        tunable hyperparameter can have its value determined during hyperparameter optimization
        (HPO).

        - **integerHyperParameterRanges** *(list) --*

          The integer-valued hyperparameters and their default ranges.

          - *(dict) --*

            Provides the name and default range of a integer-valued hyperparameter and whether the
            hyperparameter is tunable. A tunable hyperparameter can have its value determined
            during hyperparameter optimization (HPO).

            - **name** *(string) --*

              The name of the hyperparameter.

            - **minValue** *(integer) --*

              The minimum allowable value for the hyperparameter.

            - **maxValue** *(integer) --*

              The maximum allowable value for the hyperparameter.

            - **isTunable** *(boolean) --*

              Indicates whether the hyperparameter is tunable.

        - **continuousHyperParameterRanges** *(list) --*

          The continuous hyperparameters and their default ranges.

          - *(dict) --*

            Provides the name and default range of a continuous hyperparameter and whether the
            hyperparameter is tunable. A tunable hyperparameter can have its value determined
            during hyperparameter optimization (HPO).

            - **name** *(string) --*

              The name of the hyperparameter.

            - **minValue** *(float) --*

              The minimum allowable value for the hyperparameter.

            - **maxValue** *(float) --*

              The maximum allowable value for the hyperparameter.

            - **isTunable** *(boolean) --*

              Whether the hyperparameter is tunable.

        - **categoricalHyperParameterRanges** *(list) --*

          The categorical hyperparameters and their default ranges.

          - *(dict) --*

            Provides the name and default range of a categorical hyperparameter and whether the
            hyperparameter is tunable. A tunable hyperparameter can have its value determined
            during hyperparameter optimization (HPO).

            - **name** *(string) --*

              The name of the hyperparameter.

            - **values** *(list) --*

              A list of the categories for the hyperparameter.

              - *(string) --*

            - **isTunable** *(boolean) --*

              Whether the hyperparameter is tunable.

      - **defaultResourceConfig** *(dict) --*

        Specifies the default maximum number of training jobs and parallel training jobs.

        - *(string) --*

          - *(string) --*

      - **trainingInputMode** *(string) --*

        The training input mode.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) of the role.

      - **creationDateTime** *(datetime) --*

        The date and time (in Unix time) that the algorithm was created.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix time) that the algorithm was last updated.
    """


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef",
    {"path": str, "kmsKeyArn": str},
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef
):
    """
    Type definition for `ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInput` `s3DataSource`

    The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket
    must be in the same region as the API endpoint you are calling.

    - **path** *(string) --*

      The file path of the Amazon S3 bucket.

    - **kmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that
      Amazon Personalize uses to encrypt or decrypt the input and output files of a batch
      inference job.
    """


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef",
    {
        "s3DataSource": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef
    },
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef
):
    """
    Type definition for `ClientDescribeBatchInferenceJobResponsebatchInferenceJob` `jobInput`

    The Amazon S3 path that leads to the input data used to generate the batch inference job.

    - **s3DataSource** *(dict) --*

      The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket
      must be in the same region as the API endpoint you are calling.

      - **path** *(string) --*

        The file path of the Amazon S3 bucket.

      - **kmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that
        Amazon Personalize uses to encrypt or decrypt the input and output files of a batch
        inference job.
    """


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef",
    {"path": str, "kmsKeyArn": str},
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef
):
    """
    Type definition for `ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutput` `s3DataDestination`

    Information on the Amazon S3 bucket in which the batch inference job's output is stored.

    - **path** *(string) --*

      The file path of the Amazon S3 bucket.

    - **kmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that
      Amazon Personalize uses to encrypt or decrypt the input and output files of a batch
      inference job.
    """


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef",
    {
        "s3DataDestination": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef
    },
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef
):
    """
    Type definition for `ClientDescribeBatchInferenceJobResponsebatchInferenceJob` `jobOutput`

    The Amazon S3 bucket that contains the output data generated by the batch inference job.

    - **s3DataDestination** *(dict) --*

      Information on the Amazon S3 bucket in which the batch inference job's output is stored.

      - **path** *(string) --*

        The file path of the Amazon S3 bucket.

      - **kmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that
        Amazon Personalize uses to encrypt or decrypt the input and output files of a batch
        inference job.
    """


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef",
    {
        "jobName": str,
        "batchInferenceJobArn": str,
        "failureReason": str,
        "solutionVersionArn": str,
        "numResults": int,
        "jobInput": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef,
        "jobOutput": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef,
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef
):
    """
    Type definition for `ClientDescribeBatchInferenceJobResponse` `batchInferenceJob`

    Information on the specified batch inference job.

    - **jobName** *(string) --*

      The name of the batch inference job.

    - **batchInferenceJobArn** *(string) --*

      The Amazon Resource Name (ARN) of the batch inference job.

    - **failureReason** *(string) --*

      If the batch inference job failed, the reason for the failure.

    - **solutionVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the solution version from which the batch inference job
      was created.

    - **numResults** *(integer) --*

      The number of recommendations generated by the batch inference job. This number includes
      the error messages generated for failed input records.

    - **jobInput** *(dict) --*

      The Amazon S3 path that leads to the input data used to generate the batch inference job.

      - **s3DataSource** *(dict) --*

        The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket
        must be in the same region as the API endpoint you are calling.

        - **path** *(string) --*

          The file path of the Amazon S3 bucket.

        - **kmsKeyArn** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that
          Amazon Personalize uses to encrypt or decrypt the input and output files of a batch
          inference job.

    - **jobOutput** *(dict) --*

      The Amazon S3 bucket that contains the output data generated by the batch inference job.

      - **s3DataDestination** *(dict) --*

        Information on the Amazon S3 bucket in which the batch inference job's output is stored.

        - **path** *(string) --*

          The file path of the Amazon S3 bucket.

        - **kmsKeyArn** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that
          Amazon Personalize uses to encrypt or decrypt the input and output files of a batch
          inference job.

    - **roleArn** *(string) --*

      The ARN of the Amazon Identity and Access Management (IAM) role that requested the batch
      inference job.

    - **status** *(string) --*

      The status of the batch inference job. The status is one of the following values:

      * PENDING

      * IN PROGRESS

      * ACTIVE

      * CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The time at which the batch inference job was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The time at which the batch inference job was last updated.
    """


_ClientDescribeBatchInferenceJobResponseTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponseTypeDef",
    {
        "batchInferenceJob": ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef
    },
    total=False,
)


class ClientDescribeBatchInferenceJobResponseTypeDef(
    _ClientDescribeBatchInferenceJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeBatchInferenceJob` `Response`

    - **batchInferenceJob** *(dict) --*

      Information on the specified batch inference job.

      - **jobName** *(string) --*

        The name of the batch inference job.

      - **batchInferenceJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the batch inference job.

      - **failureReason** *(string) --*

        If the batch inference job failed, the reason for the failure.

      - **solutionVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the solution version from which the batch inference job
        was created.

      - **numResults** *(integer) --*

        The number of recommendations generated by the batch inference job. This number includes
        the error messages generated for failed input records.

      - **jobInput** *(dict) --*

        The Amazon S3 path that leads to the input data used to generate the batch inference job.

        - **s3DataSource** *(dict) --*

          The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket
          must be in the same region as the API endpoint you are calling.

          - **path** *(string) --*

            The file path of the Amazon S3 bucket.

          - **kmsKeyArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that
            Amazon Personalize uses to encrypt or decrypt the input and output files of a batch
            inference job.

      - **jobOutput** *(dict) --*

        The Amazon S3 bucket that contains the output data generated by the batch inference job.

        - **s3DataDestination** *(dict) --*

          Information on the Amazon S3 bucket in which the batch inference job's output is stored.

          - **path** *(string) --*

            The file path of the Amazon S3 bucket.

          - **kmsKeyArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that
            Amazon Personalize uses to encrypt or decrypt the input and output files of a batch
            inference job.

      - **roleArn** *(string) --*

        The ARN of the Amazon Identity and Access Management (IAM) role that requested the batch
        inference job.

      - **status** *(string) --*

        The status of the batch inference job. The status is one of the following values:

        * PENDING

        * IN PROGRESS

        * ACTIVE

        * CREATE FAILED

      - **creationDateTime** *(datetime) --*

        The time at which the batch inference job was created.

      - **lastUpdatedDateTime** *(datetime) --*

        The time at which the batch inference job was last updated.
    """


_ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef = TypedDict(
    "_ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef",
    {
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef(
    _ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef
):
    """
    Type definition for `ClientDescribeCampaignResponsecampaign` `latestCampaignUpdate`

    Provides a summary of the properties of a campaign update. For a complete listing, call the
     DescribeCampaign API.

    - **solutionVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the deployed solution version.

    - **minProvisionedTPS** *(integer) --*

      Specifies the requested minimum provisioned transactions (recommendations) per second
      that Amazon Personalize will support.

    - **status** *(string) --*

      The status of the campaign update.

      A campaign update can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **failureReason** *(string) --*

      If a campaign update fails, the reason behind the failure.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the campaign update was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the campaign update was last updated.
    """


_ClientDescribeCampaignResponsecampaignTypeDef = TypedDict(
    "_ClientDescribeCampaignResponsecampaignTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestCampaignUpdate": ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef,
    },
    total=False,
)


class ClientDescribeCampaignResponsecampaignTypeDef(
    _ClientDescribeCampaignResponsecampaignTypeDef
):
    """
    Type definition for `ClientDescribeCampaignResponse` `campaign`

    The properties of the campaign.

    - **name** *(string) --*

      The name of the campaign.

    - **campaignArn** *(string) --*

      The Amazon Resource Name (ARN) of the campaign.

    - **solutionVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of a specific version of the solution.

    - **minProvisionedTPS** *(integer) --*

      Specifies the requested minimum provisioned transactions (recommendations) per second.

    - **status** *(string) --*

      The status of the campaign.

      A campaign can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **failureReason** *(string) --*

      If a campaign fails, the reason behind the failure.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix format) that the campaign was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix format) that the campaign was last updated.

    - **latestCampaignUpdate** *(dict) --*

      Provides a summary of the properties of a campaign update. For a complete listing, call the
       DescribeCampaign API.

      - **solutionVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the deployed solution version.

      - **minProvisionedTPS** *(integer) --*

        Specifies the requested minimum provisioned transactions (recommendations) per second
        that Amazon Personalize will support.

      - **status** *(string) --*

        The status of the campaign update.

        A campaign update can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        * DELETE PENDING > DELETE IN_PROGRESS

      - **failureReason** *(string) --*

        If a campaign update fails, the reason behind the failure.

      - **creationDateTime** *(datetime) --*

        The date and time (in Unix time) that the campaign update was created.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix time) that the campaign update was last updated.
    """


_ClientDescribeCampaignResponseTypeDef = TypedDict(
    "_ClientDescribeCampaignResponseTypeDef",
    {"campaign": ClientDescribeCampaignResponsecampaignTypeDef},
    total=False,
)


class ClientDescribeCampaignResponseTypeDef(_ClientDescribeCampaignResponseTypeDef):
    """
    Type definition for `ClientDescribeCampaign` `Response`

    - **campaign** *(dict) --*

      The properties of the campaign.

      - **name** *(string) --*

        The name of the campaign.

      - **campaignArn** *(string) --*

        The Amazon Resource Name (ARN) of the campaign.

      - **solutionVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of a specific version of the solution.

      - **minProvisionedTPS** *(integer) --*

        Specifies the requested minimum provisioned transactions (recommendations) per second.

      - **status** *(string) --*

        The status of the campaign.

        A campaign can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        * DELETE PENDING > DELETE IN_PROGRESS

      - **failureReason** *(string) --*

        If a campaign fails, the reason behind the failure.

      - **creationDateTime** *(datetime) --*

        The date and time (in Unix format) that the campaign was created.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix format) that the campaign was last updated.

      - **latestCampaignUpdate** *(dict) --*

        Provides a summary of the properties of a campaign update. For a complete listing, call the
         DescribeCampaign API.

        - **solutionVersionArn** *(string) --*

          The Amazon Resource Name (ARN) of the deployed solution version.

        - **minProvisionedTPS** *(integer) --*

          Specifies the requested minimum provisioned transactions (recommendations) per second
          that Amazon Personalize will support.

        - **status** *(string) --*

          The status of the campaign update.

          A campaign update can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **failureReason** *(string) --*

          If a campaign update fails, the reason behind the failure.

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the campaign update was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the campaign update was last updated.
    """


_ClientDescribeDatasetGroupResponsedatasetGroupTypeDef = TypedDict(
    "_ClientDescribeDatasetGroupResponsedatasetGroupTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "roleArn": str,
        "kmsKeyArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientDescribeDatasetGroupResponsedatasetGroupTypeDef(
    _ClientDescribeDatasetGroupResponsedatasetGroupTypeDef
):
    """
    Type definition for `ClientDescribeDatasetGroupResponse` `datasetGroup`

    A listing of the dataset group's properties.

    - **name** *(string) --*

      The name of the dataset group.

    - **datasetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset group.

    - **status** *(string) --*

      The current status of the dataset group.

      A dataset group can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING

    - **roleArn** *(string) --*

      The ARN of the IAM role that has permissions to create the dataset group.

    - **kmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) of the KMS key used to encrypt the datasets.

    - **creationDateTime** *(datetime) --*

      The creation date and time (in Unix time) of the dataset group.

    - **lastUpdatedDateTime** *(datetime) --*

      The last update date and time (in Unix time) of the dataset group.

    - **failureReason** *(string) --*

      If creating a dataset group fails, provides the reason why.
    """


_ClientDescribeDatasetGroupResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetGroupResponseTypeDef",
    {"datasetGroup": ClientDescribeDatasetGroupResponsedatasetGroupTypeDef},
    total=False,
)


class ClientDescribeDatasetGroupResponseTypeDef(
    _ClientDescribeDatasetGroupResponseTypeDef
):
    """
    Type definition for `ClientDescribeDatasetGroup` `Response`

    - **datasetGroup** *(dict) --*

      A listing of the dataset group's properties.

      - **name** *(string) --*

        The name of the dataset group.

      - **datasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset group.

      - **status** *(string) --*

        The current status of the dataset group.

        A dataset group can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        * DELETE PENDING

      - **roleArn** *(string) --*

        The ARN of the IAM role that has permissions to create the dataset group.

      - **kmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) of the KMS key used to encrypt the datasets.

      - **creationDateTime** *(datetime) --*

        The creation date and time (in Unix time) of the dataset group.

      - **lastUpdatedDateTime** *(datetime) --*

        The last update date and time (in Unix time) of the dataset group.

      - **failureReason** *(string) --*

        If creating a dataset group fails, provides the reason why.
    """


_ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef",
    {"dataLocation": str},
    total=False,
)


class ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef(
    _ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef
):
    """
    Type definition for `ClientDescribeDatasetImportJobResponsedatasetImportJob` `dataSource`

    The Amazon S3 bucket that contains the training data to import.

    - **dataLocation** *(string) --*

      The path to the Amazon S3 bucket where the data that you want to upload to your dataset
      is stored. For example:

       ``s3://bucket-name/training-data.csv``
    """


_ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef",
    {
        "jobName": str,
        "datasetImportJobArn": str,
        "datasetArn": str,
        "dataSource": ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef,
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef(
    _ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef
):
    """
    Type definition for `ClientDescribeDatasetImportJobResponse` `datasetImportJob`

    Information about the dataset import job, including the status.

    The status is one of the following values:

    * CREATE PENDING

    * CREATE IN_PROGRESS

    * ACTIVE

    * CREATE FAILED

    - **jobName** *(string) --*

      The name of the import job.

    - **datasetImportJobArn** *(string) --*

      The ARN of the dataset import job.

    - **datasetArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset that receives the imported data.

    - **dataSource** *(dict) --*

      The Amazon S3 bucket that contains the training data to import.

      - **dataLocation** *(string) --*

        The path to the Amazon S3 bucket where the data that you want to upload to your dataset
        is stored. For example:

         ``s3://bucket-name/training-data.csv``

    - **roleArn** *(string) --*

      The ARN of the AWS Identity and Access Management (IAM) role that has permissions to read
      from the Amazon S3 data source.

    - **status** *(string) --*

      The status of the dataset import job.

      A dataset import job can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The creation date and time (in Unix time) of the dataset import job.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) the dataset was last updated.

    - **failureReason** *(string) --*

      If a dataset import job fails, provides the reason why.
    """


_ClientDescribeDatasetImportJobResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponseTypeDef",
    {"datasetImportJob": ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef},
    total=False,
)


class ClientDescribeDatasetImportJobResponseTypeDef(
    _ClientDescribeDatasetImportJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeDatasetImportJob` `Response`

    - **datasetImportJob** *(dict) --*

      Information about the dataset import job, including the status.

      The status is one of the following values:

      * CREATE PENDING

      * CREATE IN_PROGRESS

      * ACTIVE

      * CREATE FAILED

      - **jobName** *(string) --*

        The name of the import job.

      - **datasetImportJobArn** *(string) --*

        The ARN of the dataset import job.

      - **datasetArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset that receives the imported data.

      - **dataSource** *(dict) --*

        The Amazon S3 bucket that contains the training data to import.

        - **dataLocation** *(string) --*

          The path to the Amazon S3 bucket where the data that you want to upload to your dataset
          is stored. For example:

           ``s3://bucket-name/training-data.csv``

      - **roleArn** *(string) --*

        The ARN of the AWS Identity and Access Management (IAM) role that has permissions to read
        from the Amazon S3 data source.

      - **status** *(string) --*

        The status of the dataset import job.

        A dataset import job can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      - **creationDateTime** *(datetime) --*

        The creation date and time (in Unix time) of the dataset import job.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix time) the dataset was last updated.

      - **failureReason** *(string) --*

        If a dataset import job fails, provides the reason why.
    """


_ClientDescribeDatasetResponsedatasetTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
        "schemaArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetTypeDef(
    _ClientDescribeDatasetResponsedatasetTypeDef
):
    """
    Type definition for `ClientDescribeDatasetResponse` `dataset`

    A listing of the dataset's properties.

    - **name** *(string) --*

      The name of the dataset.

    - **datasetArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset that you want metadata for.

    - **datasetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset group.

    - **datasetType** *(string) --*

      One of the following values:

      * Interactions

      * Items

      * Users

    - **schemaArn** *(string) --*

      The ARN of the associated schema.

    - **status** *(string) --*

      The status of the dataset.

      A dataset can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The creation date and time (in Unix time) of the dataset.

    - **lastUpdatedDateTime** *(datetime) --*

      A time stamp that shows when the dataset was updated.
    """


_ClientDescribeDatasetResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetResponseTypeDef",
    {"dataset": ClientDescribeDatasetResponsedatasetTypeDef},
    total=False,
)


class ClientDescribeDatasetResponseTypeDef(_ClientDescribeDatasetResponseTypeDef):
    """
    Type definition for `ClientDescribeDataset` `Response`

    - **dataset** *(dict) --*

      A listing of the dataset's properties.

      - **name** *(string) --*

        The name of the dataset.

      - **datasetArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset that you want metadata for.

      - **datasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset group.

      - **datasetType** *(string) --*

        One of the following values:

        * Interactions

        * Items

        * Users

      - **schemaArn** *(string) --*

        The ARN of the associated schema.

      - **status** *(string) --*

        The status of the dataset.

        A dataset can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        * DELETE PENDING > DELETE IN_PROGRESS

      - **creationDateTime** *(datetime) --*

        The creation date and time (in Unix time) of the dataset.

      - **lastUpdatedDateTime** *(datetime) --*

        A time stamp that shows when the dataset was updated.
    """


_ClientDescribeEventTrackerResponseeventTrackerTypeDef = TypedDict(
    "_ClientDescribeEventTrackerResponseeventTrackerTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "accountId": str,
        "trackingId": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeEventTrackerResponseeventTrackerTypeDef(
    _ClientDescribeEventTrackerResponseeventTrackerTypeDef
):
    """
    Type definition for `ClientDescribeEventTrackerResponse` `eventTracker`

    An object that describes the event tracker.

    - **name** *(string) --*

      The name of the event tracker.

    - **eventTrackerArn** *(string) --*

      The ARN of the event tracker.

    - **accountId** *(string) --*

      The Amazon AWS account that owns the event tracker.

    - **trackingId** *(string) --*

      The ID of the event tracker. Include this ID in requests to the `PutEvents
      <https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html>`__ API.

    - **datasetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset group that receives the event data.

    - **status** *(string) --*

      The status of the event tracker.

      An event tracker can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix format) that the event tracker was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the event tracker was last updated.
    """


_ClientDescribeEventTrackerResponseTypeDef = TypedDict(
    "_ClientDescribeEventTrackerResponseTypeDef",
    {"eventTracker": ClientDescribeEventTrackerResponseeventTrackerTypeDef},
    total=False,
)


class ClientDescribeEventTrackerResponseTypeDef(
    _ClientDescribeEventTrackerResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventTracker` `Response`

    - **eventTracker** *(dict) --*

      An object that describes the event tracker.

      - **name** *(string) --*

        The name of the event tracker.

      - **eventTrackerArn** *(string) --*

        The ARN of the event tracker.

      - **accountId** *(string) --*

        The Amazon AWS account that owns the event tracker.

      - **trackingId** *(string) --*

        The ID of the event tracker. Include this ID in requests to the `PutEvents
        <https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html>`__ API.

      - **datasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset group that receives the event data.

      - **status** *(string) --*

        The status of the event tracker.

        An event tracker can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        * DELETE PENDING > DELETE IN_PROGRESS

      - **creationDateTime** *(datetime) --*

        The date and time (in Unix format) that the event tracker was created.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix time) that the event tracker was last updated.
    """


_ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef = TypedDict(
    "_ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef",
    {
        "name": str,
        "featureTransformationArn": str,
        "defaultParameters": Dict[str, str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef(
    _ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef
):
    """
    Type definition for `ClientDescribeFeatureTransformationResponse` `featureTransformation`

    A listing of the FeatureTransformation properties.

    - **name** *(string) --*

      The name of the feature transformation.

    - **featureTransformationArn** *(string) --*

      The Amazon Resource Name (ARN) of the FeatureTransformation object.

    - **defaultParameters** *(dict) --*

      Provides the default parameters for feature transformation.

      - *(string) --*

        - *(string) --*

    - **creationDateTime** *(datetime) --*

      The creation date and time (in Unix time) of the feature transformation.

    - **lastUpdatedDateTime** *(datetime) --*

      The last update date and time (in Unix time) of the feature transformation.

    - **status** *(string) --*

      The status of the feature transformation.

      A feature transformation can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    """


_ClientDescribeFeatureTransformationResponseTypeDef = TypedDict(
    "_ClientDescribeFeatureTransformationResponseTypeDef",
    {
        "featureTransformation": ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef
    },
    total=False,
)


class ClientDescribeFeatureTransformationResponseTypeDef(
    _ClientDescribeFeatureTransformationResponseTypeDef
):
    """
    Type definition for `ClientDescribeFeatureTransformation` `Response`

    - **featureTransformation** *(dict) --*

      A listing of the FeatureTransformation properties.

      - **name** *(string) --*

        The name of the feature transformation.

      - **featureTransformationArn** *(string) --*

        The Amazon Resource Name (ARN) of the FeatureTransformation object.

      - **defaultParameters** *(dict) --*

        Provides the default parameters for feature transformation.

        - *(string) --*

          - *(string) --*

      - **creationDateTime** *(datetime) --*

        The creation date and time (in Unix time) of the feature transformation.

      - **lastUpdatedDateTime** *(datetime) --*

        The last update date and time (in Unix time) of the feature transformation.

      - **status** *(string) --*

        The status of the feature transformation.

        A feature transformation can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    """


_ClientDescribeRecipeResponserecipeTypeDef = TypedDict(
    "_ClientDescribeRecipeResponserecipeTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "algorithmArn": str,
        "featureTransformationArn": str,
        "status": str,
        "description": str,
        "creationDateTime": datetime,
        "recipeType": str,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeRecipeResponserecipeTypeDef(
    _ClientDescribeRecipeResponserecipeTypeDef
):
    """
    Type definition for `ClientDescribeRecipeResponse` `recipe`

    An object that describes the recipe.

    - **name** *(string) --*

      The name of the recipe.

    - **recipeArn** *(string) --*

      The Amazon Resource Name (ARN) of the recipe.

    - **algorithmArn** *(string) --*

      The Amazon Resource Name (ARN) of the algorithm that Amazon Personalize uses to train the
      model.

    - **featureTransformationArn** *(string) --*

      The ARN of the FeatureTransformation object.

    - **status** *(string) --*

      The status of the recipe.

    - **description** *(string) --*

      The description of the recipe.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix format) that the recipe was created.

    - **recipeType** *(string) --*

      One of the following values:

      * PERSONALIZED_RANKING

      * RELATED_ITEMS

      * USER_PERSONALIZATION

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix format) that the recipe was last updated.
    """


_ClientDescribeRecipeResponseTypeDef = TypedDict(
    "_ClientDescribeRecipeResponseTypeDef",
    {"recipe": ClientDescribeRecipeResponserecipeTypeDef},
    total=False,
)


class ClientDescribeRecipeResponseTypeDef(_ClientDescribeRecipeResponseTypeDef):
    """
    Type definition for `ClientDescribeRecipe` `Response`

    - **recipe** *(dict) --*

      An object that describes the recipe.

      - **name** *(string) --*

        The name of the recipe.

      - **recipeArn** *(string) --*

        The Amazon Resource Name (ARN) of the recipe.

      - **algorithmArn** *(string) --*

        The Amazon Resource Name (ARN) of the algorithm that Amazon Personalize uses to train the
        model.

      - **featureTransformationArn** *(string) --*

        The ARN of the FeatureTransformation object.

      - **status** *(string) --*

        The status of the recipe.

      - **description** *(string) --*

        The description of the recipe.

      - **creationDateTime** *(datetime) --*

        The date and time (in Unix format) that the recipe was created.

      - **recipeType** *(string) --*

        One of the following values:

        * PERSONALIZED_RANKING

        * RELATED_ITEMS

        * USER_PERSONALIZATION

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix format) that the recipe was last updated.
    """


_ClientDescribeSchemaResponseschemaTypeDef = TypedDict(
    "_ClientDescribeSchemaResponseschemaTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "schema": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeSchemaResponseschemaTypeDef(
    _ClientDescribeSchemaResponseschemaTypeDef
):
    """
    Type definition for `ClientDescribeSchemaResponse` `schema`

    The requested schema.

    - **name** *(string) --*

      The name of the schema.

    - **schemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema.

    - **schema** *(string) --*

      The schema.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the schema was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the schema was last updated.
    """


_ClientDescribeSchemaResponseTypeDef = TypedDict(
    "_ClientDescribeSchemaResponseTypeDef",
    {"schema": ClientDescribeSchemaResponseschemaTypeDef},
    total=False,
)


class ClientDescribeSchemaResponseTypeDef(_ClientDescribeSchemaResponseTypeDef):
    """
    Type definition for `ClientDescribeSchema` `Response`

    - **schema** *(dict) --*

      The requested schema.

      - **name** *(string) --*

        The name of the schema.

      - **schemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema.

      - **schema** *(string) --*

        The schema.

      - **creationDateTime** *(datetime) --*

        The date and time (in Unix time) that the schema was created.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix time) that the schema was last updated.
    """


_ClientDescribeSolutionResponsesolutionautoMLResultTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionautoMLResultTypeDef",
    {"bestRecipeArn": str},
    total=False,
)


class ClientDescribeSolutionResponsesolutionautoMLResultTypeDef(
    _ClientDescribeSolutionResponsesolutionautoMLResultTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolution` `autoMLResult`

    When ``performAutoML`` is true, specifies the best recipe found.

    - **bestRecipeArn** *(string) --*

      The Amazon Resource Name (ARN) of the best recipe.
    """


_ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef(
    _ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolution` `latestSolutionVersion`

    Describes the latest version of the solution, including the status and the ARN.

    - **solutionVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the solution version.

    - **status** *(string) --*

      The status of the solution version.

      A solution version can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that this version of a solution was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution version was last updated.

    - **failureReason** *(string) --*

      If a solution version fails, the reason behind the failure.
    """


_ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolutionsolutionConfig` `autoMLConfig`

    The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

    - **metricName** *(string) --*

      The metric to optimize.

    - **recipeList** *(list) --*

      The list of candidate recipes.

      - *(string) --*
    """


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRanges` `categoricalHyperParameterRanges`

    Provides the name and range of a categorical hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **values** *(list) --*

      A list of the categories for the hyperparameter.

      - *(string) --*
    """


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRanges` `continuousHyperParameterRanges`

    Provides the name and range of a continuous hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **minValue** *(float) --*

      The minimum allowable value for the hyperparameter.

    - **maxValue** *(float) --*

      The maximum allowable value for the hyperparameter.
    """


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRanges` `integerHyperParameterRanges`

    Provides the name and range of an integer-valued hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **minValue** *(integer) --*

      The minimum allowable value for the hyperparameter.

    - **maxValue** *(integer) --*

      The maximum allowable value for the hyperparameter.
    """


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolutionsolutionConfighpoConfig` `algorithmHyperParameterRanges`

    The hyperparameters and their allowable ranges.

    - **integerHyperParameterRanges** *(list) --*

      The integer-valued hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of an integer-valued hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **minValue** *(integer) --*

          The minimum allowable value for the hyperparameter.

        - **maxValue** *(integer) --*

          The maximum allowable value for the hyperparameter.

    - **continuousHyperParameterRanges** *(list) --*

      The continuous hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of a continuous hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **minValue** *(float) --*

          The minimum allowable value for the hyperparameter.

        - **maxValue** *(float) --*

          The maximum allowable value for the hyperparameter.

    - **categoricalHyperParameterRanges** *(list) --*

      The categorical hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of a categorical hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **values** *(list) --*

          A list of the categories for the hyperparameter.

          - *(string) --*
    """


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolutionsolutionConfighpoConfig` `hpoObjective`

    The metric to optimize during HPO.

    - **type** *(string) --*

      The data type of the metric.

    - **metricName** *(string) --*

      The name of the metric.

    - **metricRegex** *(string) --*

      A regular expression for finding the metric in the training job logs.
    """


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolutionsolutionConfighpoConfig` `hpoResourceConfig`

    Describes the resource configuration for HPO.

    - **maxNumberOfTrainingJobs** *(string) --*

      The maximum number of training jobs when you create a solution version. The maximum
      value for ``maxNumberOfTrainingJobs`` is ``40`` .

    - **maxParallelTrainingJobs** *(string) --*

      The maximum number of parallel training jobs when you create a solution version. The
      maximum value for ``maxParallelTrainingJobs`` is ``10`` .
    """


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolutionsolutionConfig` `hpoConfig`

    Describes the properties for hyperparameter optimization (HPO).

    - **hpoObjective** *(dict) --*

      The metric to optimize during HPO.

      - **type** *(string) --*

        The data type of the metric.

      - **metricName** *(string) --*

        The name of the metric.

      - **metricRegex** *(string) --*

        A regular expression for finding the metric in the training job logs.

    - **hpoResourceConfig** *(dict) --*

      Describes the resource configuration for HPO.

      - **maxNumberOfTrainingJobs** *(string) --*

        The maximum number of training jobs when you create a solution version. The maximum
        value for ``maxNumberOfTrainingJobs`` is ``40`` .

      - **maxParallelTrainingJobs** *(string) --*

        The maximum number of parallel training jobs when you create a solution version. The
        maximum value for ``maxParallelTrainingJobs`` is ``10`` .

    - **algorithmHyperParameterRanges** *(dict) --*

      The hyperparameters and their allowable ranges.

      - **integerHyperParameterRanges** *(list) --*

        The integer-valued hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of an integer-valued hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **minValue** *(integer) --*

            The minimum allowable value for the hyperparameter.

          - **maxValue** *(integer) --*

            The maximum allowable value for the hyperparameter.

      - **continuousHyperParameterRanges** *(list) --*

        The continuous hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of a continuous hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **minValue** *(float) --*

            The minimum allowable value for the hyperparameter.

          - **maxValue** *(float) --*

            The maximum allowable value for the hyperparameter.

      - **categoricalHyperParameterRanges** *(list) --*

        The categorical hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of a categorical hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **values** *(list) --*

            A list of the categories for the hyperparameter.

            - *(string) --*
    """


_ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponsesolution` `solutionConfig`

    Describes the configuration properties for the solution.

    - **eventValueThreshold** *(string) --*

      Only events with a value greater than or equal to this threshold are used for training a
      model.

    - **hpoConfig** *(dict) --*

      Describes the properties for hyperparameter optimization (HPO).

      - **hpoObjective** *(dict) --*

        The metric to optimize during HPO.

        - **type** *(string) --*

          The data type of the metric.

        - **metricName** *(string) --*

          The name of the metric.

        - **metricRegex** *(string) --*

          A regular expression for finding the metric in the training job logs.

      - **hpoResourceConfig** *(dict) --*

        Describes the resource configuration for HPO.

        - **maxNumberOfTrainingJobs** *(string) --*

          The maximum number of training jobs when you create a solution version. The maximum
          value for ``maxNumberOfTrainingJobs`` is ``40`` .

        - **maxParallelTrainingJobs** *(string) --*

          The maximum number of parallel training jobs when you create a solution version. The
          maximum value for ``maxParallelTrainingJobs`` is ``10`` .

      - **algorithmHyperParameterRanges** *(dict) --*

        The hyperparameters and their allowable ranges.

        - **integerHyperParameterRanges** *(list) --*

          The integer-valued hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of an integer-valued hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **minValue** *(integer) --*

              The minimum allowable value for the hyperparameter.

            - **maxValue** *(integer) --*

              The maximum allowable value for the hyperparameter.

        - **continuousHyperParameterRanges** *(list) --*

          The continuous hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of a continuous hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **minValue** *(float) --*

              The minimum allowable value for the hyperparameter.

            - **maxValue** *(float) --*

              The maximum allowable value for the hyperparameter.

        - **categoricalHyperParameterRanges** *(list) --*

          The categorical hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of a categorical hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **values** *(list) --*

              A list of the categories for the hyperparameter.

              - *(string) --*

    - **algorithmHyperParameters** *(dict) --*

      Lists the hyperparameter names and ranges.

      - *(string) --*

        - *(string) --*

    - **featureTransformationParameters** *(dict) --*

      Lists the feature transformation parameters.

      - *(string) --*

        - *(string) --*

    - **autoMLConfig** *(dict) --*

      The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

      - **metricName** *(string) --*

        The metric to optimize.

      - **recipeList** *(list) --*

        The list of candidate recipes.

        - *(string) --*
    """


_ClientDescribeSolutionResponsesolutionTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "datasetGroupArn": str,
        "eventType": str,
        "solutionConfig": ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef,
        "autoMLResult": ClientDescribeSolutionResponsesolutionautoMLResultTypeDef,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestSolutionVersion": ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionTypeDef(
    _ClientDescribeSolutionResponsesolutionTypeDef
):
    """
    Type definition for `ClientDescribeSolutionResponse` `solution`

    An object that describes the solution.

    - **name** *(string) --*

      The name of the solution.

    - **solutionArn** *(string) --*

      The ARN of the solution.

    - **performHPO** *(boolean) --*

      Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is
      ``false`` .

    - **performAutoML** *(boolean) --*

      When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe
      from the list specified in the solution configuration (``recipeArn`` must not be
      specified). When false (the default), Amazon Personalize uses ``recipeArn`` for training.

    - **recipeArn** *(string) --*

      The ARN of the recipe used to create the solution.

    - **datasetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset group that provides the training data.

    - **eventType** *(string) --*

      The event type (for example, 'click' or 'like') that is used for training the model.

    - **solutionConfig** *(dict) --*

      Describes the configuration properties for the solution.

      - **eventValueThreshold** *(string) --*

        Only events with a value greater than or equal to this threshold are used for training a
        model.

      - **hpoConfig** *(dict) --*

        Describes the properties for hyperparameter optimization (HPO).

        - **hpoObjective** *(dict) --*

          The metric to optimize during HPO.

          - **type** *(string) --*

            The data type of the metric.

          - **metricName** *(string) --*

            The name of the metric.

          - **metricRegex** *(string) --*

            A regular expression for finding the metric in the training job logs.

        - **hpoResourceConfig** *(dict) --*

          Describes the resource configuration for HPO.

          - **maxNumberOfTrainingJobs** *(string) --*

            The maximum number of training jobs when you create a solution version. The maximum
            value for ``maxNumberOfTrainingJobs`` is ``40`` .

          - **maxParallelTrainingJobs** *(string) --*

            The maximum number of parallel training jobs when you create a solution version. The
            maximum value for ``maxParallelTrainingJobs`` is ``10`` .

        - **algorithmHyperParameterRanges** *(dict) --*

          The hyperparameters and their allowable ranges.

          - **integerHyperParameterRanges** *(list) --*

            The integer-valued hyperparameters and their ranges.

            - *(dict) --*

              Provides the name and range of an integer-valued hyperparameter.

              - **name** *(string) --*

                The name of the hyperparameter.

              - **minValue** *(integer) --*

                The minimum allowable value for the hyperparameter.

              - **maxValue** *(integer) --*

                The maximum allowable value for the hyperparameter.

          - **continuousHyperParameterRanges** *(list) --*

            The continuous hyperparameters and their ranges.

            - *(dict) --*

              Provides the name and range of a continuous hyperparameter.

              - **name** *(string) --*

                The name of the hyperparameter.

              - **minValue** *(float) --*

                The minimum allowable value for the hyperparameter.

              - **maxValue** *(float) --*

                The maximum allowable value for the hyperparameter.

          - **categoricalHyperParameterRanges** *(list) --*

            The categorical hyperparameters and their ranges.

            - *(dict) --*

              Provides the name and range of a categorical hyperparameter.

              - **name** *(string) --*

                The name of the hyperparameter.

              - **values** *(list) --*

                A list of the categories for the hyperparameter.

                - *(string) --*

      - **algorithmHyperParameters** *(dict) --*

        Lists the hyperparameter names and ranges.

        - *(string) --*

          - *(string) --*

      - **featureTransformationParameters** *(dict) --*

        Lists the feature transformation parameters.

        - *(string) --*

          - *(string) --*

      - **autoMLConfig** *(dict) --*

        The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

        - **metricName** *(string) --*

          The metric to optimize.

        - **recipeList** *(list) --*

          The list of candidate recipes.

          - *(string) --*

    - **autoMLResult** *(dict) --*

      When ``performAutoML`` is true, specifies the best recipe found.

      - **bestRecipeArn** *(string) --*

        The Amazon Resource Name (ARN) of the best recipe.

    - **status** *(string) --*

      The status of the solution.

      A solution can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The creation date and time (in Unix time) of the solution.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution was last updated.

    - **latestSolutionVersion** *(dict) --*

      Describes the latest version of the solution, including the status and the ARN.

      - **solutionVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the solution version.

      - **status** *(string) --*

        The status of the solution version.

        A solution version can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      - **creationDateTime** *(datetime) --*

        The date and time (in Unix time) that this version of a solution was created.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix time) that the solution version was last updated.

      - **failureReason** *(string) --*

        If a solution version fails, the reason behind the failure.
    """


_ClientDescribeSolutionResponseTypeDef = TypedDict(
    "_ClientDescribeSolutionResponseTypeDef",
    {"solution": ClientDescribeSolutionResponsesolutionTypeDef},
    total=False,
)


class ClientDescribeSolutionResponseTypeDef(_ClientDescribeSolutionResponseTypeDef):
    """
    Type definition for `ClientDescribeSolution` `Response`

    - **solution** *(dict) --*

      An object that describes the solution.

      - **name** *(string) --*

        The name of the solution.

      - **solutionArn** *(string) --*

        The ARN of the solution.

      - **performHPO** *(boolean) --*

        Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is
        ``false`` .

      - **performAutoML** *(boolean) --*

        When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe
        from the list specified in the solution configuration (``recipeArn`` must not be
        specified). When false (the default), Amazon Personalize uses ``recipeArn`` for training.

      - **recipeArn** *(string) --*

        The ARN of the recipe used to create the solution.

      - **datasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset group that provides the training data.

      - **eventType** *(string) --*

        The event type (for example, 'click' or 'like') that is used for training the model.

      - **solutionConfig** *(dict) --*

        Describes the configuration properties for the solution.

        - **eventValueThreshold** *(string) --*

          Only events with a value greater than or equal to this threshold are used for training a
          model.

        - **hpoConfig** *(dict) --*

          Describes the properties for hyperparameter optimization (HPO).

          - **hpoObjective** *(dict) --*

            The metric to optimize during HPO.

            - **type** *(string) --*

              The data type of the metric.

            - **metricName** *(string) --*

              The name of the metric.

            - **metricRegex** *(string) --*

              A regular expression for finding the metric in the training job logs.

          - **hpoResourceConfig** *(dict) --*

            Describes the resource configuration for HPO.

            - **maxNumberOfTrainingJobs** *(string) --*

              The maximum number of training jobs when you create a solution version. The maximum
              value for ``maxNumberOfTrainingJobs`` is ``40`` .

            - **maxParallelTrainingJobs** *(string) --*

              The maximum number of parallel training jobs when you create a solution version. The
              maximum value for ``maxParallelTrainingJobs`` is ``10`` .

          - **algorithmHyperParameterRanges** *(dict) --*

            The hyperparameters and their allowable ranges.

            - **integerHyperParameterRanges** *(list) --*

              The integer-valued hyperparameters and their ranges.

              - *(dict) --*

                Provides the name and range of an integer-valued hyperparameter.

                - **name** *(string) --*

                  The name of the hyperparameter.

                - **minValue** *(integer) --*

                  The minimum allowable value for the hyperparameter.

                - **maxValue** *(integer) --*

                  The maximum allowable value for the hyperparameter.

            - **continuousHyperParameterRanges** *(list) --*

              The continuous hyperparameters and their ranges.

              - *(dict) --*

                Provides the name and range of a continuous hyperparameter.

                - **name** *(string) --*

                  The name of the hyperparameter.

                - **minValue** *(float) --*

                  The minimum allowable value for the hyperparameter.

                - **maxValue** *(float) --*

                  The maximum allowable value for the hyperparameter.

            - **categoricalHyperParameterRanges** *(list) --*

              The categorical hyperparameters and their ranges.

              - *(dict) --*

                Provides the name and range of a categorical hyperparameter.

                - **name** *(string) --*

                  The name of the hyperparameter.

                - **values** *(list) --*

                  A list of the categories for the hyperparameter.

                  - *(string) --*

        - **algorithmHyperParameters** *(dict) --*

          Lists the hyperparameter names and ranges.

          - *(string) --*

            - *(string) --*

        - **featureTransformationParameters** *(dict) --*

          Lists the feature transformation parameters.

          - *(string) --*

            - *(string) --*

        - **autoMLConfig** *(dict) --*

          The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

          - **metricName** *(string) --*

            The metric to optimize.

          - **recipeList** *(list) --*

            The list of candidate recipes.

            - *(string) --*

      - **autoMLResult** *(dict) --*

        When ``performAutoML`` is true, specifies the best recipe found.

        - **bestRecipeArn** *(string) --*

          The Amazon Resource Name (ARN) of the best recipe.

      - **status** *(string) --*

        The status of the solution.

        A solution can be in one of the following states:

        * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        * DELETE PENDING > DELETE IN_PROGRESS

      - **creationDateTime** *(datetime) --*

        The creation date and time (in Unix time) of the solution.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix time) that the solution was last updated.

      - **latestSolutionVersion** *(dict) --*

        Describes the latest version of the solution, including the status and the ARN.

        - **solutionVersionArn** *(string) --*

          The Amazon Resource Name (ARN) of the solution version.

        - **status** *(string) --*

          The status of the solution version.

          A solution version can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that this version of a solution was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the solution version was last updated.

        - **failureReason** *(string) --*

          If a solution version fails, the reason behind the failure.
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfig` `autoMLConfig`

    The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

    - **metricName** *(string) --*

      The metric to optimize.

    - **recipeList** *(list) --*

      The list of candidate recipes.

      - *(string) --*
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRanges` `categoricalHyperParameterRanges`

    Provides the name and range of a categorical hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **values** *(list) --*

      A list of the categories for the hyperparameter.

      - *(string) --*
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRanges` `continuousHyperParameterRanges`

    Provides the name and range of a continuous hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **minValue** *(float) --*

      The minimum allowable value for the hyperparameter.

    - **maxValue** *(float) --*

      The maximum allowable value for the hyperparameter.
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRanges` `integerHyperParameterRanges`

    Provides the name and range of an integer-valued hyperparameter.

    - **name** *(string) --*

      The name of the hyperparameter.

    - **minValue** *(integer) --*

      The minimum allowable value for the hyperparameter.

    - **maxValue** *(integer) --*

      The maximum allowable value for the hyperparameter.
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfig` `algorithmHyperParameterRanges`

    The hyperparameters and their allowable ranges.

    - **integerHyperParameterRanges** *(list) --*

      The integer-valued hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of an integer-valued hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **minValue** *(integer) --*

          The minimum allowable value for the hyperparameter.

        - **maxValue** *(integer) --*

          The maximum allowable value for the hyperparameter.

    - **continuousHyperParameterRanges** *(list) --*

      The continuous hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of a continuous hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **minValue** *(float) --*

          The minimum allowable value for the hyperparameter.

        - **maxValue** *(float) --*

          The maximum allowable value for the hyperparameter.

    - **categoricalHyperParameterRanges** *(list) --*

      The categorical hyperparameters and their ranges.

      - *(dict) --*

        Provides the name and range of a categorical hyperparameter.

        - **name** *(string) --*

          The name of the hyperparameter.

        - **values** *(list) --*

          A list of the categories for the hyperparameter.

          - *(string) --*
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfig` `hpoObjective`

    The metric to optimize during HPO.

    - **type** *(string) --*

      The data type of the metric.

    - **metricName** *(string) --*

      The name of the metric.

    - **metricRegex** *(string) --*

      A regular expression for finding the metric in the training job logs.
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfig` `hpoResourceConfig`

    Describes the resource configuration for HPO.

    - **maxNumberOfTrainingJobs** *(string) --*

      The maximum number of training jobs when you create a solution version. The maximum
      value for ``maxNumberOfTrainingJobs`` is ``40`` .

    - **maxParallelTrainingJobs** *(string) --*

      The maximum number of parallel training jobs when you create a solution version. The
      maximum value for ``maxParallelTrainingJobs`` is ``10`` .
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfig` `hpoConfig`

    Describes the properties for hyperparameter optimization (HPO).

    - **hpoObjective** *(dict) --*

      The metric to optimize during HPO.

      - **type** *(string) --*

        The data type of the metric.

      - **metricName** *(string) --*

        The name of the metric.

      - **metricRegex** *(string) --*

        A regular expression for finding the metric in the training job logs.

    - **hpoResourceConfig** *(dict) --*

      Describes the resource configuration for HPO.

      - **maxNumberOfTrainingJobs** *(string) --*

        The maximum number of training jobs when you create a solution version. The maximum
        value for ``maxNumberOfTrainingJobs`` is ``40`` .

      - **maxParallelTrainingJobs** *(string) --*

        The maximum number of parallel training jobs when you create a solution version. The
        maximum value for ``maxParallelTrainingJobs`` is ``10`` .

    - **algorithmHyperParameterRanges** *(dict) --*

      The hyperparameters and their allowable ranges.

      - **integerHyperParameterRanges** *(list) --*

        The integer-valued hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of an integer-valued hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **minValue** *(integer) --*

            The minimum allowable value for the hyperparameter.

          - **maxValue** *(integer) --*

            The maximum allowable value for the hyperparameter.

      - **continuousHyperParameterRanges** *(list) --*

        The continuous hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of a continuous hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **minValue** *(float) --*

            The minimum allowable value for the hyperparameter.

          - **maxValue** *(float) --*

            The maximum allowable value for the hyperparameter.

      - **categoricalHyperParameterRanges** *(list) --*

        The categorical hyperparameters and their ranges.

        - *(dict) --*

          Provides the name and range of a categorical hyperparameter.

          - **name** *(string) --*

            The name of the hyperparameter.

          - **values** *(list) --*

            A list of the categories for the hyperparameter.

            - *(string) --*
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponsesolutionVersion` `solutionConfig`

    Describes the configuration properties for the solution.

    - **eventValueThreshold** *(string) --*

      Only events with a value greater than or equal to this threshold are used for training a
      model.

    - **hpoConfig** *(dict) --*

      Describes the properties for hyperparameter optimization (HPO).

      - **hpoObjective** *(dict) --*

        The metric to optimize during HPO.

        - **type** *(string) --*

          The data type of the metric.

        - **metricName** *(string) --*

          The name of the metric.

        - **metricRegex** *(string) --*

          A regular expression for finding the metric in the training job logs.

      - **hpoResourceConfig** *(dict) --*

        Describes the resource configuration for HPO.

        - **maxNumberOfTrainingJobs** *(string) --*

          The maximum number of training jobs when you create a solution version. The maximum
          value for ``maxNumberOfTrainingJobs`` is ``40`` .

        - **maxParallelTrainingJobs** *(string) --*

          The maximum number of parallel training jobs when you create a solution version. The
          maximum value for ``maxParallelTrainingJobs`` is ``10`` .

      - **algorithmHyperParameterRanges** *(dict) --*

        The hyperparameters and their allowable ranges.

        - **integerHyperParameterRanges** *(list) --*

          The integer-valued hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of an integer-valued hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **minValue** *(integer) --*

              The minimum allowable value for the hyperparameter.

            - **maxValue** *(integer) --*

              The maximum allowable value for the hyperparameter.

        - **continuousHyperParameterRanges** *(list) --*

          The continuous hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of a continuous hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **minValue** *(float) --*

              The minimum allowable value for the hyperparameter.

            - **maxValue** *(float) --*

              The maximum allowable value for the hyperparameter.

        - **categoricalHyperParameterRanges** *(list) --*

          The categorical hyperparameters and their ranges.

          - *(dict) --*

            Provides the name and range of a categorical hyperparameter.

            - **name** *(string) --*

              The name of the hyperparameter.

            - **values** *(list) --*

              A list of the categories for the hyperparameter.

              - *(string) --*

    - **algorithmHyperParameters** *(dict) --*

      Lists the hyperparameter names and ranges.

      - *(string) --*

        - *(string) --*

    - **featureTransformationParameters** *(dict) --*

      Lists the feature transformation parameters.

      - *(string) --*

        - *(string) --*

    - **autoMLConfig** *(dict) --*

      The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

      - **metricName** *(string) --*

        The metric to optimize.

      - **recipeList** *(list) --*

        The list of candidate recipes.

        - *(string) --*
    """


_ClientDescribeSolutionVersionResponsesolutionVersionTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionTypeDef",
    {
        "solutionVersionArn": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "eventType": str,
        "datasetGroupArn": str,
        "solutionConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef,
        "trainingHours": float,
        "trainingMode": str,
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersionResponse` `solutionVersion`

    The solution version.

    - **solutionVersionArn** *(string) --*

      The ARN of the solution version.

    - **solutionArn** *(string) --*

      The ARN of the solution.

    - **performHPO** *(boolean) --*

      Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is
      ``false`` .

    - **performAutoML** *(boolean) --*

      When true, Amazon Personalize searches for the most optimal recipe according to the
      solution configuration. When false (the default), Amazon Personalize uses ``recipeArn`` .

    - **recipeArn** *(string) --*

      The ARN of the recipe used in the solution.

    - **eventType** *(string) --*

      The event type (for example, 'click' or 'like') that is used for training the model.

    - **datasetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset group providing the training data.

    - **solutionConfig** *(dict) --*

      Describes the configuration properties for the solution.

      - **eventValueThreshold** *(string) --*

        Only events with a value greater than or equal to this threshold are used for training a
        model.

      - **hpoConfig** *(dict) --*

        Describes the properties for hyperparameter optimization (HPO).

        - **hpoObjective** *(dict) --*

          The metric to optimize during HPO.

          - **type** *(string) --*

            The data type of the metric.

          - **metricName** *(string) --*

            The name of the metric.

          - **metricRegex** *(string) --*

            A regular expression for finding the metric in the training job logs.

        - **hpoResourceConfig** *(dict) --*

          Describes the resource configuration for HPO.

          - **maxNumberOfTrainingJobs** *(string) --*

            The maximum number of training jobs when you create a solution version. The maximum
            value for ``maxNumberOfTrainingJobs`` is ``40`` .

          - **maxParallelTrainingJobs** *(string) --*

            The maximum number of parallel training jobs when you create a solution version. The
            maximum value for ``maxParallelTrainingJobs`` is ``10`` .

        - **algorithmHyperParameterRanges** *(dict) --*

          The hyperparameters and their allowable ranges.

          - **integerHyperParameterRanges** *(list) --*

            The integer-valued hyperparameters and their ranges.

            - *(dict) --*

              Provides the name and range of an integer-valued hyperparameter.

              - **name** *(string) --*

                The name of the hyperparameter.

              - **minValue** *(integer) --*

                The minimum allowable value for the hyperparameter.

              - **maxValue** *(integer) --*

                The maximum allowable value for the hyperparameter.

          - **continuousHyperParameterRanges** *(list) --*

            The continuous hyperparameters and their ranges.

            - *(dict) --*

              Provides the name and range of a continuous hyperparameter.

              - **name** *(string) --*

                The name of the hyperparameter.

              - **minValue** *(float) --*

                The minimum allowable value for the hyperparameter.

              - **maxValue** *(float) --*

                The maximum allowable value for the hyperparameter.

          - **categoricalHyperParameterRanges** *(list) --*

            The categorical hyperparameters and their ranges.

            - *(dict) --*

              Provides the name and range of a categorical hyperparameter.

              - **name** *(string) --*

                The name of the hyperparameter.

              - **values** *(list) --*

                A list of the categories for the hyperparameter.

                - *(string) --*

      - **algorithmHyperParameters** *(dict) --*

        Lists the hyperparameter names and ranges.

        - *(string) --*

          - *(string) --*

      - **featureTransformationParameters** *(dict) --*

        Lists the feature transformation parameters.

        - *(string) --*

          - *(string) --*

      - **autoMLConfig** *(dict) --*

        The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

        - **metricName** *(string) --*

          The metric to optimize.

        - **recipeList** *(list) --*

          The list of candidate recipes.

          - *(string) --*

    - **trainingHours** *(float) --*

      The time used to train the model. You are billed for the time it takes to train a model.
      This field is visible only after Amazon Personalize successfully trains a model.

    - **trainingMode** *(string) --*

      The scope of training used to create the solution version. The ``FULL`` option trains the
      solution version based on the entirety of the input solution's training data, while the
      ``UPDATE`` option processes only the training data that has changed since the creation of
      the last solution version. Choose ``UPDATE`` when you want to start recommending items
      added to the dataset without retraining the model.

      .. warning::

        The ``UPDATE`` option can only be used after you've created a solution version with the
        ``FULL`` option and the training solution uses the  native-recipe-hrnn-coldstart .

    - **status** *(string) --*

      The status of the solution version.

      A solution version can be in one of the following states:

      * CREATE PENDING

      * CREATE IN_PROGRESS

      * ACTIVE

      * CREATE FAILED

    - **failureReason** *(string) --*

      If training a solution version fails, the reason for the failure.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that this version of the solution was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution was last updated.
    """


_ClientDescribeSolutionVersionResponseTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponseTypeDef",
    {"solutionVersion": ClientDescribeSolutionVersionResponsesolutionVersionTypeDef},
    total=False,
)


class ClientDescribeSolutionVersionResponseTypeDef(
    _ClientDescribeSolutionVersionResponseTypeDef
):
    """
    Type definition for `ClientDescribeSolutionVersion` `Response`

    - **solutionVersion** *(dict) --*

      The solution version.

      - **solutionVersionArn** *(string) --*

        The ARN of the solution version.

      - **solutionArn** *(string) --*

        The ARN of the solution.

      - **performHPO** *(boolean) --*

        Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is
        ``false`` .

      - **performAutoML** *(boolean) --*

        When true, Amazon Personalize searches for the most optimal recipe according to the
        solution configuration. When false (the default), Amazon Personalize uses ``recipeArn`` .

      - **recipeArn** *(string) --*

        The ARN of the recipe used in the solution.

      - **eventType** *(string) --*

        The event type (for example, 'click' or 'like') that is used for training the model.

      - **datasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset group providing the training data.

      - **solutionConfig** *(dict) --*

        Describes the configuration properties for the solution.

        - **eventValueThreshold** *(string) --*

          Only events with a value greater than or equal to this threshold are used for training a
          model.

        - **hpoConfig** *(dict) --*

          Describes the properties for hyperparameter optimization (HPO).

          - **hpoObjective** *(dict) --*

            The metric to optimize during HPO.

            - **type** *(string) --*

              The data type of the metric.

            - **metricName** *(string) --*

              The name of the metric.

            - **metricRegex** *(string) --*

              A regular expression for finding the metric in the training job logs.

          - **hpoResourceConfig** *(dict) --*

            Describes the resource configuration for HPO.

            - **maxNumberOfTrainingJobs** *(string) --*

              The maximum number of training jobs when you create a solution version. The maximum
              value for ``maxNumberOfTrainingJobs`` is ``40`` .

            - **maxParallelTrainingJobs** *(string) --*

              The maximum number of parallel training jobs when you create a solution version. The
              maximum value for ``maxParallelTrainingJobs`` is ``10`` .

          - **algorithmHyperParameterRanges** *(dict) --*

            The hyperparameters and their allowable ranges.

            - **integerHyperParameterRanges** *(list) --*

              The integer-valued hyperparameters and their ranges.

              - *(dict) --*

                Provides the name and range of an integer-valued hyperparameter.

                - **name** *(string) --*

                  The name of the hyperparameter.

                - **minValue** *(integer) --*

                  The minimum allowable value for the hyperparameter.

                - **maxValue** *(integer) --*

                  The maximum allowable value for the hyperparameter.

            - **continuousHyperParameterRanges** *(list) --*

              The continuous hyperparameters and their ranges.

              - *(dict) --*

                Provides the name and range of a continuous hyperparameter.

                - **name** *(string) --*

                  The name of the hyperparameter.

                - **minValue** *(float) --*

                  The minimum allowable value for the hyperparameter.

                - **maxValue** *(float) --*

                  The maximum allowable value for the hyperparameter.

            - **categoricalHyperParameterRanges** *(list) --*

              The categorical hyperparameters and their ranges.

              - *(dict) --*

                Provides the name and range of a categorical hyperparameter.

                - **name** *(string) --*

                  The name of the hyperparameter.

                - **values** *(list) --*

                  A list of the categories for the hyperparameter.

                  - *(string) --*

        - **algorithmHyperParameters** *(dict) --*

          Lists the hyperparameter names and ranges.

          - *(string) --*

            - *(string) --*

        - **featureTransformationParameters** *(dict) --*

          Lists the feature transformation parameters.

          - *(string) --*

            - *(string) --*

        - **autoMLConfig** *(dict) --*

          The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

          - **metricName** *(string) --*

            The metric to optimize.

          - **recipeList** *(list) --*

            The list of candidate recipes.

            - *(string) --*

      - **trainingHours** *(float) --*

        The time used to train the model. You are billed for the time it takes to train a model.
        This field is visible only after Amazon Personalize successfully trains a model.

      - **trainingMode** *(string) --*

        The scope of training used to create the solution version. The ``FULL`` option trains the
        solution version based on the entirety of the input solution's training data, while the
        ``UPDATE`` option processes only the training data that has changed since the creation of
        the last solution version. Choose ``UPDATE`` when you want to start recommending items
        added to the dataset without retraining the model.

        .. warning::

          The ``UPDATE`` option can only be used after you've created a solution version with the
          ``FULL`` option and the training solution uses the  native-recipe-hrnn-coldstart .

      - **status** *(string) --*

        The status of the solution version.

        A solution version can be in one of the following states:

        * CREATE PENDING

        * CREATE IN_PROGRESS

        * ACTIVE

        * CREATE FAILED

      - **failureReason** *(string) --*

        If training a solution version fails, the reason for the failure.

      - **creationDateTime** *(datetime) --*

        The date and time (in Unix time) that this version of the solution was created.

      - **lastUpdatedDateTime** *(datetime) --*

        The date and time (in Unix time) that the solution was last updated.
    """


_ClientGetSolutionMetricsResponseTypeDef = TypedDict(
    "_ClientGetSolutionMetricsResponseTypeDef",
    {"solutionVersionArn": str, "metrics": Dict[str, float]},
    total=False,
)


class ClientGetSolutionMetricsResponseTypeDef(_ClientGetSolutionMetricsResponseTypeDef):
    """
    Type definition for `ClientGetSolutionMetrics` `Response`

    - **solutionVersionArn** *(string) --*

      The same solution version ARN as specified in the request.

    - **metrics** *(dict) --*

      The metrics for the solution version.

      - *(string) --*

        - *(float) --*
    """


_ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef = TypedDict(
    "_ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef",
    {
        "batchInferenceJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef(
    _ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef
):
    """
    Type definition for `ClientListBatchInferenceJobsResponse` `batchInferenceJobs`

    A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs
    operation returns a list of batch inference job summaries.

    - **batchInferenceJobArn** *(string) --*

      The Amazon Resource Name (ARN) of the batch inference job.

    - **jobName** *(string) --*

      The name of the batch inference job.

    - **status** *(string) --*

      The status of the batch inference job. The status is one of the following values:

      * PENDING

      * IN PROGRESS

      * ACTIVE

      * CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The time at which the batch inference job was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The time at which the batch inference job was last updated.

    - **failureReason** *(string) --*

      If the batch inference job failed, the reason for the failure.
    """


_ClientListBatchInferenceJobsResponseTypeDef = TypedDict(
    "_ClientListBatchInferenceJobsResponseTypeDef",
    {
        "batchInferenceJobs": List[
            ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListBatchInferenceJobsResponseTypeDef(
    _ClientListBatchInferenceJobsResponseTypeDef
):
    """
    Type definition for `ClientListBatchInferenceJobs` `Response`

    - **batchInferenceJobs** *(list) --*

      A list containing information on each job that is returned.

      - *(dict) --*

        A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs
        operation returns a list of batch inference job summaries.

        - **batchInferenceJobArn** *(string) --*

          The Amazon Resource Name (ARN) of the batch inference job.

        - **jobName** *(string) --*

          The name of the batch inference job.

        - **status** *(string) --*

          The status of the batch inference job. The status is one of the following values:

          * PENDING

          * IN PROGRESS

          * ACTIVE

          * CREATE FAILED

        - **creationDateTime** *(datetime) --*

          The time at which the batch inference job was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The time at which the batch inference job was last updated.

        - **failureReason** *(string) --*

          If the batch inference job failed, the reason for the failure.

    - **nextToken** *(string) --*

      The token to use to retreive the next page of results. The value is ``null`` when there are
      no more results to return.
    """


_ClientListCampaignsResponsecampaignsTypeDef = TypedDict(
    "_ClientListCampaignsResponsecampaignsTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListCampaignsResponsecampaignsTypeDef(
    _ClientListCampaignsResponsecampaignsTypeDef
):
    """
    Type definition for `ClientListCampaignsResponse` `campaigns`

    Provides a summary of the properties of a campaign. For a complete listing, call the
    DescribeCampaign API.

    - **name** *(string) --*

      The name of the campaign.

    - **campaignArn** *(string) --*

      The Amazon Resource Name (ARN) of the campaign.

    - **status** *(string) --*

      The status of the campaign.

      A campaign can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the campaign was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the campaign was last updated.

    - **failureReason** *(string) --*

      If a campaign fails, the reason behind the failure.
    """


_ClientListCampaignsResponseTypeDef = TypedDict(
    "_ClientListCampaignsResponseTypeDef",
    {"campaigns": List[ClientListCampaignsResponsecampaignsTypeDef], "nextToken": str},
    total=False,
)


class ClientListCampaignsResponseTypeDef(_ClientListCampaignsResponseTypeDef):
    """
    Type definition for `ClientListCampaigns` `Response`

    - **campaigns** *(list) --*

      A list of the campaigns.

      - *(dict) --*

        Provides a summary of the properties of a campaign. For a complete listing, call the
        DescribeCampaign API.

        - **name** *(string) --*

          The name of the campaign.

        - **campaignArn** *(string) --*

          The Amazon Resource Name (ARN) of the campaign.

        - **status** *(string) --*

          The status of the campaign.

          A campaign can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the campaign was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the campaign was last updated.

        - **failureReason** *(string) --*

          If a campaign fails, the reason behind the failure.

    - **nextToken** *(string) --*

      A token for getting the next set of campaigns (if they exist).
    """


_ClientListDatasetGroupsResponsedatasetGroupsTypeDef = TypedDict(
    "_ClientListDatasetGroupsResponsedatasetGroupsTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListDatasetGroupsResponsedatasetGroupsTypeDef(
    _ClientListDatasetGroupsResponsedatasetGroupsTypeDef
):
    """
    Type definition for `ClientListDatasetGroupsResponse` `datasetGroups`

    Provides a summary of the properties of a dataset group. For a complete listing, call the
    DescribeDatasetGroup API.

    - **name** *(string) --*

      The name of the dataset group.

    - **datasetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset group.

    - **status** *(string) --*

      The status of the dataset group.

      A dataset group can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset group was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset group was last updated.

    - **failureReason** *(string) --*

      If creating a dataset group fails, the reason behind the failure.
    """


_ClientListDatasetGroupsResponseTypeDef = TypedDict(
    "_ClientListDatasetGroupsResponseTypeDef",
    {
        "datasetGroups": List[ClientListDatasetGroupsResponsedatasetGroupsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDatasetGroupsResponseTypeDef(_ClientListDatasetGroupsResponseTypeDef):
    """
    Type definition for `ClientListDatasetGroups` `Response`

    - **datasetGroups** *(list) --*

      The list of your dataset groups.

      - *(dict) --*

        Provides a summary of the properties of a dataset group. For a complete listing, call the
        DescribeDatasetGroup API.

        - **name** *(string) --*

          The name of the dataset group.

        - **datasetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the dataset group.

        - **status** *(string) --*

          The status of the dataset group.

          A dataset group can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset group was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset group was last updated.

        - **failureReason** *(string) --*

          If creating a dataset group fails, the reason behind the failure.

    - **nextToken** *(string) --*

      A token for getting the next set of dataset groups (if they exist).
    """


_ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef = TypedDict(
    "_ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef",
    {
        "datasetImportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef(
    _ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef
):
    """
    Type definition for `ClientListDatasetImportJobsResponse` `datasetImportJobs`

    Provides a summary of the properties of a dataset import job. For a complete listing, call
    the  DescribeDatasetImportJob API.

    - **datasetImportJobArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset import job.

    - **jobName** *(string) --*

      The name of the dataset import job.

    - **status** *(string) --*

      The status of the dataset import job.

      A dataset import job can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset import job was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset was last updated.

    - **failureReason** *(string) --*

      If a dataset import job fails, the reason behind the failure.
    """


_ClientListDatasetImportJobsResponseTypeDef = TypedDict(
    "_ClientListDatasetImportJobsResponseTypeDef",
    {
        "datasetImportJobs": List[
            ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDatasetImportJobsResponseTypeDef(
    _ClientListDatasetImportJobsResponseTypeDef
):
    """
    Type definition for `ClientListDatasetImportJobs` `Response`

    - **datasetImportJobs** *(list) --*

      The list of dataset import jobs.

      - *(dict) --*

        Provides a summary of the properties of a dataset import job. For a complete listing, call
        the  DescribeDatasetImportJob API.

        - **datasetImportJobArn** *(string) --*

          The Amazon Resource Name (ARN) of the dataset import job.

        - **jobName** *(string) --*

          The name of the dataset import job.

        - **status** *(string) --*

          The status of the dataset import job.

          A dataset import job can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset import job was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset was last updated.

        - **failureReason** *(string) --*

          If a dataset import job fails, the reason behind the failure.

    - **nextToken** *(string) --*

      A token for getting the next set of dataset import jobs (if they exist).
    """


_ClientListDatasetsResponsedatasetsTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetsTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetType": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListDatasetsResponsedatasetsTypeDef(
    _ClientListDatasetsResponsedatasetsTypeDef
):
    """
    Type definition for `ClientListDatasetsResponse` `datasets`

    Provides a summary of the properties of a dataset. For a complete listing, call the
    DescribeDataset API.

    - **name** *(string) --*

      The name of the dataset.

    - **datasetArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset.

    - **datasetType** *(string) --*

      The dataset type. One of the following values:

      * Interactions

      * Items

      * Users

      * Event-Interactions

    - **status** *(string) --*

      The status of the dataset.

      A dataset can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset was last updated.
    """


_ClientListDatasetsResponseTypeDef = TypedDict(
    "_ClientListDatasetsResponseTypeDef",
    {"datasets": List[ClientListDatasetsResponsedatasetsTypeDef], "nextToken": str},
    total=False,
)


class ClientListDatasetsResponseTypeDef(_ClientListDatasetsResponseTypeDef):
    """
    Type definition for `ClientListDatasets` `Response`

    - **datasets** *(list) --*

      An array of ``Dataset`` objects. Each object provides metadata information.

      - *(dict) --*

        Provides a summary of the properties of a dataset. For a complete listing, call the
        DescribeDataset API.

        - **name** *(string) --*

          The name of the dataset.

        - **datasetArn** *(string) --*

          The Amazon Resource Name (ARN) of the dataset.

        - **datasetType** *(string) --*

          The dataset type. One of the following values:

          * Interactions

          * Items

          * Users

          * Event-Interactions

        - **status** *(string) --*

          The status of the dataset.

          A dataset can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset was last updated.

    - **nextToken** *(string) --*

      A token for getting the next set of datasets (if they exist).
    """


_ClientListEventTrackersResponseeventTrackersTypeDef = TypedDict(
    "_ClientListEventTrackersResponseeventTrackersTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListEventTrackersResponseeventTrackersTypeDef(
    _ClientListEventTrackersResponseeventTrackersTypeDef
):
    """
    Type definition for `ClientListEventTrackersResponse` `eventTrackers`

    Provides a summary of the properties of an event tracker. For a complete listing, call the
    DescribeEventTracker API.

    - **name** *(string) --*

      The name of the event tracker.

    - **eventTrackerArn** *(string) --*

      The Amazon Resource Name (ARN) of the event tracker.

    - **status** *(string) --*

      The status of the event tracker.

      An event tracker can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the event tracker was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the event tracker was last updated.
    """


_ClientListEventTrackersResponseTypeDef = TypedDict(
    "_ClientListEventTrackersResponseTypeDef",
    {
        "eventTrackers": List[ClientListEventTrackersResponseeventTrackersTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListEventTrackersResponseTypeDef(_ClientListEventTrackersResponseTypeDef):
    """
    Type definition for `ClientListEventTrackers` `Response`

    - **eventTrackers** *(list) --*

      A list of event trackers.

      - *(dict) --*

        Provides a summary of the properties of an event tracker. For a complete listing, call the
        DescribeEventTracker API.

        - **name** *(string) --*

          The name of the event tracker.

        - **eventTrackerArn** *(string) --*

          The Amazon Resource Name (ARN) of the event tracker.

        - **status** *(string) --*

          The status of the event tracker.

          An event tracker can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the event tracker was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the event tracker was last updated.

    - **nextToken** *(string) --*

      A token for getting the next set of event trackers (if they exist).
    """


_ClientListRecipesResponserecipesTypeDef = TypedDict(
    "_ClientListRecipesResponserecipesTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListRecipesResponserecipesTypeDef(_ClientListRecipesResponserecipesTypeDef):
    """
    Type definition for `ClientListRecipesResponse` `recipes`

    Provides a summary of the properties of a recipe. For a complete listing, call the
    DescribeRecipe API.

    - **name** *(string) --*

      The name of the recipe.

    - **recipeArn** *(string) --*

      The Amazon Resource Name (ARN) of the recipe.

    - **status** *(string) --*

      The status of the recipe.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the recipe was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the recipe was last updated.
    """


_ClientListRecipesResponseTypeDef = TypedDict(
    "_ClientListRecipesResponseTypeDef",
    {"recipes": List[ClientListRecipesResponserecipesTypeDef], "nextToken": str},
    total=False,
)


class ClientListRecipesResponseTypeDef(_ClientListRecipesResponseTypeDef):
    """
    Type definition for `ClientListRecipes` `Response`

    - **recipes** *(list) --*

      The list of available recipes.

      - *(dict) --*

        Provides a summary of the properties of a recipe. For a complete listing, call the
        DescribeRecipe API.

        - **name** *(string) --*

          The name of the recipe.

        - **recipeArn** *(string) --*

          The Amazon Resource Name (ARN) of the recipe.

        - **status** *(string) --*

          The status of the recipe.

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the recipe was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the recipe was last updated.

    - **nextToken** *(string) --*

      A token for getting the next set of recipes.
    """


_ClientListSchemasResponseschemasTypeDef = TypedDict(
    "_ClientListSchemasResponseschemasTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListSchemasResponseschemasTypeDef(_ClientListSchemasResponseschemasTypeDef):
    """
    Type definition for `ClientListSchemasResponse` `schemas`

    Provides a summary of the properties of a dataset schema. For a complete listing, call the
    DescribeSchema API.

    - **name** *(string) --*

      The name of the schema.

    - **schemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the schema was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the schema was last updated.
    """


_ClientListSchemasResponseTypeDef = TypedDict(
    "_ClientListSchemasResponseTypeDef",
    {"schemas": List[ClientListSchemasResponseschemasTypeDef], "nextToken": str},
    total=False,
)


class ClientListSchemasResponseTypeDef(_ClientListSchemasResponseTypeDef):
    """
    Type definition for `ClientListSchemas` `Response`

    - **schemas** *(list) --*

      A list of schemas.

      - *(dict) --*

        Provides a summary of the properties of a dataset schema. For a complete listing, call the
        DescribeSchema API.

        - **name** *(string) --*

          The name of the schema.

        - **schemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema.

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the schema was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the schema was last updated.

    - **nextToken** *(string) --*

      A token used to get the next set of schemas (if they exist).
    """


_ClientListSolutionVersionsResponsesolutionVersionsTypeDef = TypedDict(
    "_ClientListSolutionVersionsResponsesolutionVersionsTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListSolutionVersionsResponsesolutionVersionsTypeDef(
    _ClientListSolutionVersionsResponsesolutionVersionsTypeDef
):
    """
    Type definition for `ClientListSolutionVersionsResponse` `solutionVersions`

    Provides a summary of the properties of a solution version. For a complete listing, call
    the  DescribeSolutionVersion API.

    - **solutionVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the solution version.

    - **status** *(string) --*

      The status of the solution version.

      A solution version can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that this version of a solution was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution version was last updated.

    - **failureReason** *(string) --*

      If a solution version fails, the reason behind the failure.
    """


_ClientListSolutionVersionsResponseTypeDef = TypedDict(
    "_ClientListSolutionVersionsResponseTypeDef",
    {
        "solutionVersions": List[
            ClientListSolutionVersionsResponsesolutionVersionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSolutionVersionsResponseTypeDef(
    _ClientListSolutionVersionsResponseTypeDef
):
    """
    Type definition for `ClientListSolutionVersions` `Response`

    - **solutionVersions** *(list) --*

      A list of solution versions describing the version properties.

      - *(dict) --*

        Provides a summary of the properties of a solution version. For a complete listing, call
        the  DescribeSolutionVersion API.

        - **solutionVersionArn** *(string) --*

          The Amazon Resource Name (ARN) of the solution version.

        - **status** *(string) --*

          The status of the solution version.

          A solution version can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that this version of a solution was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the solution version was last updated.

        - **failureReason** *(string) --*

          If a solution version fails, the reason behind the failure.

    - **nextToken** *(string) --*

      A token for getting the next set of solution versions (if they exist).
    """


_ClientListSolutionsResponsesolutionsTypeDef = TypedDict(
    "_ClientListSolutionsResponsesolutionsTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListSolutionsResponsesolutionsTypeDef(
    _ClientListSolutionsResponsesolutionsTypeDef
):
    """
    Type definition for `ClientListSolutionsResponse` `solutions`

    Provides a summary of the properties of a solution. For a complete listing, call the
    DescribeSolution API.

    - **name** *(string) --*

      The name of the solution.

    - **solutionArn** *(string) --*

      The Amazon Resource Name (ARN) of the solution.

    - **status** *(string) --*

      The status of the solution.

      A solution can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution was last updated.
    """


_ClientListSolutionsResponseTypeDef = TypedDict(
    "_ClientListSolutionsResponseTypeDef",
    {"solutions": List[ClientListSolutionsResponsesolutionsTypeDef], "nextToken": str},
    total=False,
)


class ClientListSolutionsResponseTypeDef(_ClientListSolutionsResponseTypeDef):
    """
    Type definition for `ClientListSolutions` `Response`

    - **solutions** *(list) --*

      A list of the current solutions.

      - *(dict) --*

        Provides a summary of the properties of a solution. For a complete listing, call the
        DescribeSolution API.

        - **name** *(string) --*

          The name of the solution.

        - **solutionArn** *(string) --*

          The Amazon Resource Name (ARN) of the solution.

        - **status** *(string) --*

          The status of the solution.

          A solution can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the solution was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the solution was last updated.

    - **nextToken** *(string) --*

      A token for getting the next set of solutions (if they exist).
    """


_ClientUpdateCampaignResponseTypeDef = TypedDict(
    "_ClientUpdateCampaignResponseTypeDef", {"campaignArn": str}, total=False
)


class ClientUpdateCampaignResponseTypeDef(_ClientUpdateCampaignResponseTypeDef):
    """
    Type definition for `ClientUpdateCampaign` `Response`

    - **campaignArn** *(string) --*

      The same campaign ARN as given in the request.
    """


_ListBatchInferenceJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBatchInferenceJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBatchInferenceJobsPaginatePaginationConfigTypeDef(
    _ListBatchInferenceJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBatchInferenceJobsPaginate` `PaginationConfig`

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


_ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef = TypedDict(
    "_ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef",
    {
        "batchInferenceJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef(
    _ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef
):
    """
    Type definition for `ListBatchInferenceJobsPaginateResponse` `batchInferenceJobs`

    A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs
    operation returns a list of batch inference job summaries.

    - **batchInferenceJobArn** *(string) --*

      The Amazon Resource Name (ARN) of the batch inference job.

    - **jobName** *(string) --*

      The name of the batch inference job.

    - **status** *(string) --*

      The status of the batch inference job. The status is one of the following values:

      * PENDING

      * IN PROGRESS

      * ACTIVE

      * CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The time at which the batch inference job was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The time at which the batch inference job was last updated.

    - **failureReason** *(string) --*

      If the batch inference job failed, the reason for the failure.
    """


_ListBatchInferenceJobsPaginateResponseTypeDef = TypedDict(
    "_ListBatchInferenceJobsPaginateResponseTypeDef",
    {
        "batchInferenceJobs": List[
            ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListBatchInferenceJobsPaginateResponseTypeDef(
    _ListBatchInferenceJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListBatchInferenceJobsPaginate` `Response`

    - **batchInferenceJobs** *(list) --*

      A list containing information on each job that is returned.

      - *(dict) --*

        A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs
        operation returns a list of batch inference job summaries.

        - **batchInferenceJobArn** *(string) --*

          The Amazon Resource Name (ARN) of the batch inference job.

        - **jobName** *(string) --*

          The name of the batch inference job.

        - **status** *(string) --*

          The status of the batch inference job. The status is one of the following values:

          * PENDING

          * IN PROGRESS

          * ACTIVE

          * CREATE FAILED

        - **creationDateTime** *(datetime) --*

          The time at which the batch inference job was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The time at which the batch inference job was last updated.

        - **failureReason** *(string) --*

          If the batch inference job failed, the reason for the failure.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListCampaignsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCampaignsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCampaignsPaginatePaginationConfigTypeDef(
    _ListCampaignsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCampaignsPaginate` `PaginationConfig`

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


_ListCampaignsPaginateResponsecampaignsTypeDef = TypedDict(
    "_ListCampaignsPaginateResponsecampaignsTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListCampaignsPaginateResponsecampaignsTypeDef(
    _ListCampaignsPaginateResponsecampaignsTypeDef
):
    """
    Type definition for `ListCampaignsPaginateResponse` `campaigns`

    Provides a summary of the properties of a campaign. For a complete listing, call the
    DescribeCampaign API.

    - **name** *(string) --*

      The name of the campaign.

    - **campaignArn** *(string) --*

      The Amazon Resource Name (ARN) of the campaign.

    - **status** *(string) --*

      The status of the campaign.

      A campaign can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the campaign was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the campaign was last updated.

    - **failureReason** *(string) --*

      If a campaign fails, the reason behind the failure.
    """


_ListCampaignsPaginateResponseTypeDef = TypedDict(
    "_ListCampaignsPaginateResponseTypeDef",
    {
        "campaigns": List[ListCampaignsPaginateResponsecampaignsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListCampaignsPaginateResponseTypeDef(_ListCampaignsPaginateResponseTypeDef):
    """
    Type definition for `ListCampaignsPaginate` `Response`

    - **campaigns** *(list) --*

      A list of the campaigns.

      - *(dict) --*

        Provides a summary of the properties of a campaign. For a complete listing, call the
        DescribeCampaign API.

        - **name** *(string) --*

          The name of the campaign.

        - **campaignArn** *(string) --*

          The Amazon Resource Name (ARN) of the campaign.

        - **status** *(string) --*

          The status of the campaign.

          A campaign can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the campaign was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the campaign was last updated.

        - **failureReason** *(string) --*

          If a campaign fails, the reason behind the failure.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDatasetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetGroupsPaginatePaginationConfigTypeDef(
    _ListDatasetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDatasetGroupsPaginate` `PaginationConfig`

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


_ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef = TypedDict(
    "_ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef(
    _ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef
):
    """
    Type definition for `ListDatasetGroupsPaginateResponse` `datasetGroups`

    Provides a summary of the properties of a dataset group. For a complete listing, call the
    DescribeDatasetGroup API.

    - **name** *(string) --*

      The name of the dataset group.

    - **datasetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset group.

    - **status** *(string) --*

      The status of the dataset group.

      A dataset group can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset group was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset group was last updated.

    - **failureReason** *(string) --*

      If creating a dataset group fails, the reason behind the failure.
    """


_ListDatasetGroupsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetGroupsPaginateResponseTypeDef",
    {
        "datasetGroups": List[ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDatasetGroupsPaginateResponseTypeDef(
    _ListDatasetGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListDatasetGroupsPaginate` `Response`

    - **datasetGroups** *(list) --*

      The list of your dataset groups.

      - *(dict) --*

        Provides a summary of the properties of a dataset group. For a complete listing, call the
        DescribeDatasetGroup API.

        - **name** *(string) --*

          The name of the dataset group.

        - **datasetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the dataset group.

        - **status** *(string) --*

          The status of the dataset group.

          A dataset group can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset group was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset group was last updated.

        - **failureReason** *(string) --*

          If creating a dataset group fails, the reason behind the failure.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDatasetImportJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetImportJobsPaginatePaginationConfigTypeDef(
    _ListDatasetImportJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDatasetImportJobsPaginate` `PaginationConfig`

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


_ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef",
    {
        "datasetImportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef(
    _ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef
):
    """
    Type definition for `ListDatasetImportJobsPaginateResponse` `datasetImportJobs`

    Provides a summary of the properties of a dataset import job. For a complete listing, call
    the  DescribeDatasetImportJob API.

    - **datasetImportJobArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset import job.

    - **jobName** *(string) --*

      The name of the dataset import job.

    - **status** *(string) --*

      The status of the dataset import job.

      A dataset import job can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset import job was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset was last updated.

    - **failureReason** *(string) --*

      If a dataset import job fails, the reason behind the failure.
    """


_ListDatasetImportJobsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateResponseTypeDef",
    {
        "datasetImportJobs": List[
            ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDatasetImportJobsPaginateResponseTypeDef(
    _ListDatasetImportJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListDatasetImportJobsPaginate` `Response`

    - **datasetImportJobs** *(list) --*

      The list of dataset import jobs.

      - *(dict) --*

        Provides a summary of the properties of a dataset import job. For a complete listing, call
        the  DescribeDatasetImportJob API.

        - **datasetImportJobArn** *(string) --*

          The Amazon Resource Name (ARN) of the dataset import job.

        - **jobName** *(string) --*

          The name of the dataset import job.

        - **status** *(string) --*

          The status of the dataset import job.

          A dataset import job can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset import job was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset was last updated.

        - **failureReason** *(string) --*

          If a dataset import job fails, the reason behind the failure.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDatasetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetsPaginatePaginationConfigTypeDef(
    _ListDatasetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDatasetsPaginate` `PaginationConfig`

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


_ListDatasetsPaginateResponsedatasetsTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetsTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetType": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListDatasetsPaginateResponsedatasetsTypeDef(
    _ListDatasetsPaginateResponsedatasetsTypeDef
):
    """
    Type definition for `ListDatasetsPaginateResponse` `datasets`

    Provides a summary of the properties of a dataset. For a complete listing, call the
    DescribeDataset API.

    - **name** *(string) --*

      The name of the dataset.

    - **datasetArn** *(string) --*

      The Amazon Resource Name (ARN) of the dataset.

    - **datasetType** *(string) --*

      The dataset type. One of the following values:

      * Interactions

      * Items

      * Users

      * Event-Interactions

    - **status** *(string) --*

      The status of the dataset.

      A dataset can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the dataset was last updated.
    """


_ListDatasetsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetsPaginateResponseTypeDef",
    {"datasets": List[ListDatasetsPaginateResponsedatasetsTypeDef], "NextToken": str},
    total=False,
)


class ListDatasetsPaginateResponseTypeDef(_ListDatasetsPaginateResponseTypeDef):
    """
    Type definition for `ListDatasetsPaginate` `Response`

    - **datasets** *(list) --*

      An array of ``Dataset`` objects. Each object provides metadata information.

      - *(dict) --*

        Provides a summary of the properties of a dataset. For a complete listing, call the
        DescribeDataset API.

        - **name** *(string) --*

          The name of the dataset.

        - **datasetArn** *(string) --*

          The Amazon Resource Name (ARN) of the dataset.

        - **datasetType** *(string) --*

          The dataset type. One of the following values:

          * Interactions

          * Items

          * Users

          * Event-Interactions

        - **status** *(string) --*

          The status of the dataset.

          A dataset can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the dataset was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListEventTrackersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEventTrackersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEventTrackersPaginatePaginationConfigTypeDef(
    _ListEventTrackersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEventTrackersPaginate` `PaginationConfig`

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


_ListEventTrackersPaginateResponseeventTrackersTypeDef = TypedDict(
    "_ListEventTrackersPaginateResponseeventTrackersTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListEventTrackersPaginateResponseeventTrackersTypeDef(
    _ListEventTrackersPaginateResponseeventTrackersTypeDef
):
    """
    Type definition for `ListEventTrackersPaginateResponse` `eventTrackers`

    Provides a summary of the properties of an event tracker. For a complete listing, call the
    DescribeEventTracker API.

    - **name** *(string) --*

      The name of the event tracker.

    - **eventTrackerArn** *(string) --*

      The Amazon Resource Name (ARN) of the event tracker.

    - **status** *(string) --*

      The status of the event tracker.

      An event tracker can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the event tracker was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the event tracker was last updated.
    """


_ListEventTrackersPaginateResponseTypeDef = TypedDict(
    "_ListEventTrackersPaginateResponseTypeDef",
    {
        "eventTrackers": List[ListEventTrackersPaginateResponseeventTrackersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListEventTrackersPaginateResponseTypeDef(
    _ListEventTrackersPaginateResponseTypeDef
):
    """
    Type definition for `ListEventTrackersPaginate` `Response`

    - **eventTrackers** *(list) --*

      A list of event trackers.

      - *(dict) --*

        Provides a summary of the properties of an event tracker. For a complete listing, call the
        DescribeEventTracker API.

        - **name** *(string) --*

          The name of the event tracker.

        - **eventTrackerArn** *(string) --*

          The Amazon Resource Name (ARN) of the event tracker.

        - **status** *(string) --*

          The status of the event tracker.

          An event tracker can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the event tracker was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the event tracker was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRecipesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRecipesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRecipesPaginatePaginationConfigTypeDef(
    _ListRecipesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRecipesPaginate` `PaginationConfig`

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


_ListRecipesPaginateResponserecipesTypeDef = TypedDict(
    "_ListRecipesPaginateResponserecipesTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListRecipesPaginateResponserecipesTypeDef(
    _ListRecipesPaginateResponserecipesTypeDef
):
    """
    Type definition for `ListRecipesPaginateResponse` `recipes`

    Provides a summary of the properties of a recipe. For a complete listing, call the
    DescribeRecipe API.

    - **name** *(string) --*

      The name of the recipe.

    - **recipeArn** *(string) --*

      The Amazon Resource Name (ARN) of the recipe.

    - **status** *(string) --*

      The status of the recipe.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the recipe was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the recipe was last updated.
    """


_ListRecipesPaginateResponseTypeDef = TypedDict(
    "_ListRecipesPaginateResponseTypeDef",
    {"recipes": List[ListRecipesPaginateResponserecipesTypeDef], "NextToken": str},
    total=False,
)


class ListRecipesPaginateResponseTypeDef(_ListRecipesPaginateResponseTypeDef):
    """
    Type definition for `ListRecipesPaginate` `Response`

    - **recipes** *(list) --*

      The list of available recipes.

      - *(dict) --*

        Provides a summary of the properties of a recipe. For a complete listing, call the
        DescribeRecipe API.

        - **name** *(string) --*

          The name of the recipe.

        - **recipeArn** *(string) --*

          The Amazon Resource Name (ARN) of the recipe.

        - **status** *(string) --*

          The status of the recipe.

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the recipe was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the recipe was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSchemasPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSchemasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSchemasPaginatePaginationConfigTypeDef(
    _ListSchemasPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSchemasPaginate` `PaginationConfig`

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


_ListSchemasPaginateResponseschemasTypeDef = TypedDict(
    "_ListSchemasPaginateResponseschemasTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListSchemasPaginateResponseschemasTypeDef(
    _ListSchemasPaginateResponseschemasTypeDef
):
    """
    Type definition for `ListSchemasPaginateResponse` `schemas`

    Provides a summary of the properties of a dataset schema. For a complete listing, call the
    DescribeSchema API.

    - **name** *(string) --*

      The name of the schema.

    - **schemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema.

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the schema was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the schema was last updated.
    """


_ListSchemasPaginateResponseTypeDef = TypedDict(
    "_ListSchemasPaginateResponseTypeDef",
    {"schemas": List[ListSchemasPaginateResponseschemasTypeDef], "NextToken": str},
    total=False,
)


class ListSchemasPaginateResponseTypeDef(_ListSchemasPaginateResponseTypeDef):
    """
    Type definition for `ListSchemasPaginate` `Response`

    - **schemas** *(list) --*

      A list of schemas.

      - *(dict) --*

        Provides a summary of the properties of a dataset schema. For a complete listing, call the
        DescribeSchema API.

        - **name** *(string) --*

          The name of the schema.

        - **schemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema.

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the schema was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the schema was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSolutionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSolutionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSolutionVersionsPaginatePaginationConfigTypeDef(
    _ListSolutionVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSolutionVersionsPaginate` `PaginationConfig`

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


_ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef = TypedDict(
    "_ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef(
    _ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef
):
    """
    Type definition for `ListSolutionVersionsPaginateResponse` `solutionVersions`

    Provides a summary of the properties of a solution version. For a complete listing, call
    the  DescribeSolutionVersion API.

    - **solutionVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the solution version.

    - **status** *(string) --*

      The status of the solution version.

      A solution version can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that this version of a solution was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution version was last updated.

    - **failureReason** *(string) --*

      If a solution version fails, the reason behind the failure.
    """


_ListSolutionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListSolutionVersionsPaginateResponseTypeDef",
    {
        "solutionVersions": List[
            ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSolutionVersionsPaginateResponseTypeDef(
    _ListSolutionVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListSolutionVersionsPaginate` `Response`

    - **solutionVersions** *(list) --*

      A list of solution versions describing the version properties.

      - *(dict) --*

        Provides a summary of the properties of a solution version. For a complete listing, call
        the  DescribeSolutionVersion API.

        - **solutionVersionArn** *(string) --*

          The Amazon Resource Name (ARN) of the solution version.

        - **status** *(string) --*

          The status of the solution version.

          A solution version can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that this version of a solution was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the solution version was last updated.

        - **failureReason** *(string) --*

          If a solution version fails, the reason behind the failure.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSolutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSolutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSolutionsPaginatePaginationConfigTypeDef(
    _ListSolutionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSolutionsPaginate` `PaginationConfig`

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


_ListSolutionsPaginateResponsesolutionsTypeDef = TypedDict(
    "_ListSolutionsPaginateResponsesolutionsTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListSolutionsPaginateResponsesolutionsTypeDef(
    _ListSolutionsPaginateResponsesolutionsTypeDef
):
    """
    Type definition for `ListSolutionsPaginateResponse` `solutions`

    Provides a summary of the properties of a solution. For a complete listing, call the
    DescribeSolution API.

    - **name** *(string) --*

      The name of the solution.

    - **solutionArn** *(string) --*

      The Amazon Resource Name (ARN) of the solution.

    - **status** *(string) --*

      The status of the solution.

      A solution can be in one of the following states:

      * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

      * DELETE PENDING > DELETE IN_PROGRESS

    - **creationDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution was created.

    - **lastUpdatedDateTime** *(datetime) --*

      The date and time (in Unix time) that the solution was last updated.
    """


_ListSolutionsPaginateResponseTypeDef = TypedDict(
    "_ListSolutionsPaginateResponseTypeDef",
    {
        "solutions": List[ListSolutionsPaginateResponsesolutionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListSolutionsPaginateResponseTypeDef(_ListSolutionsPaginateResponseTypeDef):
    """
    Type definition for `ListSolutionsPaginate` `Response`

    - **solutions** *(list) --*

      A list of the current solutions.

      - *(dict) --*

        Provides a summary of the properties of a solution. For a complete listing, call the
        DescribeSolution API.

        - **name** *(string) --*

          The name of the solution.

        - **solutionArn** *(string) --*

          The Amazon Resource Name (ARN) of the solution.

        - **status** *(string) --*

          The status of the solution.

          A solution can be in one of the following states:

          * CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

          * DELETE PENDING > DELETE IN_PROGRESS

        - **creationDateTime** *(datetime) --*

          The date and time (in Unix time) that the solution was created.

        - **lastUpdatedDateTime** *(datetime) --*

          The date and time (in Unix time) that the solution was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
