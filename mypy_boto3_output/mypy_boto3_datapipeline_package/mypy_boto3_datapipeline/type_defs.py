"Main interface for datapipeline type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientActivatePipelineparameterValuesTypeDef",
    "ClientAddTagstagsTypeDef",
    "ClientCreatePipelineResponseTypeDef",
    "ClientCreatePipelinetagsTypeDef",
    "ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef",
    "ClientDescribeObjectsResponsepipelineObjectsTypeDef",
    "ClientDescribeObjectsResponseTypeDef",
    "ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef",
    "ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef",
    "ClientDescribePipelinesResponsepipelineDescriptionListTypeDef",
    "ClientDescribePipelinesResponseTypeDef",
    "ClientEvaluateExpressionResponseTypeDef",
    "ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef",
    "ClientGetPipelineDefinitionResponseparameterObjectsTypeDef",
    "ClientGetPipelineDefinitionResponseparameterValuesTypeDef",
    "ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef",
    "ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef",
    "ClientGetPipelineDefinitionResponseTypeDef",
    "ClientListPipelinesResponsepipelineIdListTypeDef",
    "ClientListPipelinesResponseTypeDef",
    "ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef",
    "ClientPollForTaskResponsetaskObjectobjectsTypeDef",
    "ClientPollForTaskResponsetaskObjectTypeDef",
    "ClientPollForTaskResponseTypeDef",
    "ClientPollForTaskinstanceIdentityTypeDef",
    "ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef",
    "ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef",
    "ClientPutPipelineDefinitionResponseTypeDef",
    "ClientPutPipelineDefinitionparameterObjectsattributesTypeDef",
    "ClientPutPipelineDefinitionparameterObjectsTypeDef",
    "ClientPutPipelineDefinitionparameterValuesTypeDef",
    "ClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef",
    "ClientPutPipelineDefinitionpipelineObjectsTypeDef",
    "ClientQueryObjectsResponseTypeDef",
    "ClientQueryObjectsqueryselectorsoperatorTypeDef",
    "ClientQueryObjectsqueryselectorsTypeDef",
    "ClientQueryObjectsqueryTypeDef",
    "ClientReportTaskProgressResponseTypeDef",
    "ClientReportTaskProgressfieldsTypeDef",
    "ClientReportTaskRunnerHeartbeatResponseTypeDef",
    "ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef",
    "ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef",
    "ClientValidatePipelineDefinitionResponseTypeDef",
    "ClientValidatePipelineDefinitionparameterObjectsattributesTypeDef",
    "ClientValidatePipelineDefinitionparameterObjectsTypeDef",
    "ClientValidatePipelineDefinitionparameterValuesTypeDef",
    "ClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef",
    "ClientValidatePipelineDefinitionpipelineObjectsTypeDef",
    "DescribeObjectsPaginatePaginationConfigTypeDef",
    "DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef",
    "DescribeObjectsPaginateResponsepipelineObjectsTypeDef",
    "DescribeObjectsPaginateResponseTypeDef",
    "ListPipelinesPaginatePaginationConfigTypeDef",
    "ListPipelinesPaginateResponsepipelineIdListTypeDef",
    "ListPipelinesPaginateResponseTypeDef",
    "QueryObjectsPaginatePaginationConfigTypeDef",
    "QueryObjectsPaginateResponseTypeDef",
    "QueryObjectsPaginatequeryselectorsoperatorTypeDef",
    "QueryObjectsPaginatequeryselectorsTypeDef",
    "QueryObjectsPaginatequeryTypeDef",
)


_ClientActivatePipelineparameterValuesTypeDef = TypedDict(
    "_ClientActivatePipelineparameterValuesTypeDef", {"id": str, "stringValue": str}
)


class ClientActivatePipelineparameterValuesTypeDef(
    _ClientActivatePipelineparameterValuesTypeDef
):
    """
    Type definition for `ClientActivatePipeline` `parameterValues`

    A value or list of parameter values.

    - **id** *(string) --* **[REQUIRED]**

      The ID of the parameter value.

    - **stringValue** *(string) --* **[REQUIRED]**

      The field value, expressed as a String.
    """


_ClientAddTagstagsTypeDef = TypedDict(
    "_ClientAddTagstagsTypeDef", {"key": str, "value": str}
)


class ClientAddTagstagsTypeDef(_ClientAddTagstagsTypeDef):
    """
    Type definition for `ClientAddTags` `tags`

    Tags are key/value pairs defined by a user and associated with a pipeline to control access.
    AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see
    `Controlling User Access to Pipelines
    <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
    the *AWS Data Pipeline Developer Guide* .

    - **key** *(string) --* **[REQUIRED]**

      The key name of a tag defined by a user. For more information, see `Controlling User Access
      to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
      the *AWS Data Pipeline Developer Guide* .

    - **value** *(string) --* **[REQUIRED]**

      The optional value portion of a tag defined by a user. For more information, see `Controlling
      User Access to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
      the *AWS Data Pipeline Developer Guide* .
    """


_ClientCreatePipelineResponseTypeDef = TypedDict(
    "_ClientCreatePipelineResponseTypeDef", {"pipelineId": str}, total=False
)


class ClientCreatePipelineResponseTypeDef(_ClientCreatePipelineResponseTypeDef):
    """
    Type definition for `ClientCreatePipeline` `Response`

    Contains the output of CreatePipeline.

    - **pipelineId** *(string) --*

      The ID that AWS Data Pipeline assigns the newly created pipeline. For example,
      ``df-06372391ZG65EXAMPLE`` .
    """


_ClientCreatePipelinetagsTypeDef = TypedDict(
    "_ClientCreatePipelinetagsTypeDef", {"key": str, "value": str}
)


class ClientCreatePipelinetagsTypeDef(_ClientCreatePipelinetagsTypeDef):
    """
    Type definition for `ClientCreatePipeline` `tags`

    Tags are key/value pairs defined by a user and associated with a pipeline to control access.
    AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see
    `Controlling User Access to Pipelines
    <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
    the *AWS Data Pipeline Developer Guide* .

    - **key** *(string) --* **[REQUIRED]**

      The key name of a tag defined by a user. For more information, see `Controlling User Access
      to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
      the *AWS Data Pipeline Developer Guide* .

    - **value** *(string) --* **[REQUIRED]**

      The optional value portion of a tag defined by a user. For more information, see `Controlling
      User Access to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
      the *AWS Data Pipeline Developer Guide* .
    """


_ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "_ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef(
    _ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef
):
    """
    Type definition for `ClientDescribeObjectsResponsepipelineObjects` `fields`

    A key-value pair that describes a property of a pipeline object. The value is specified
    as either a string value (``StringValue`` ) or a reference to another object
    (``RefValue`` ) but not as both.

    - **key** *(string) --*

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.

    - **refValue** *(string) --*

      The field value, expressed as the identifier of another object.
    """


_ClientDescribeObjectsResponsepipelineObjectsTypeDef = TypedDict(
    "_ClientDescribeObjectsResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)


class ClientDescribeObjectsResponsepipelineObjectsTypeDef(
    _ClientDescribeObjectsResponsepipelineObjectsTypeDef
):
    """
    Type definition for `ClientDescribeObjectsResponse` `pipelineObjects`

    Contains information about a pipeline object. This can be a logical, physical, or physical
    attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

    - **id** *(string) --*

      The ID of the object.

    - **name** *(string) --*

      The name of the object.

    - **fields** *(list) --*

      Key-value pairs that define the properties of the object.

      - *(dict) --*

        A key-value pair that describes a property of a pipeline object. The value is specified
        as either a string value (``StringValue`` ) or a reference to another object
        (``RefValue`` ) but not as both.

        - **key** *(string) --*

          The field identifier.

        - **stringValue** *(string) --*

          The field value, expressed as a String.

        - **refValue** *(string) --*

          The field value, expressed as the identifier of another object.
    """


_ClientDescribeObjectsResponseTypeDef = TypedDict(
    "_ClientDescribeObjectsResponseTypeDef",
    {
        "pipelineObjects": List[ClientDescribeObjectsResponsepipelineObjectsTypeDef],
        "marker": str,
        "hasMoreResults": bool,
    },
    total=False,
)


class ClientDescribeObjectsResponseTypeDef(_ClientDescribeObjectsResponseTypeDef):
    """
    Type definition for `ClientDescribeObjects` `Response`

    Contains the output of DescribeObjects.

    - **pipelineObjects** *(list) --*

      An array of object definitions.

      - *(dict) --*

        Contains information about a pipeline object. This can be a logical, physical, or physical
        attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

        - **id** *(string) --*

          The ID of the object.

        - **name** *(string) --*

          The name of the object.

        - **fields** *(list) --*

          Key-value pairs that define the properties of the object.

          - *(dict) --*

            A key-value pair that describes a property of a pipeline object. The value is specified
            as either a string value (``StringValue`` ) or a reference to another object
            (``RefValue`` ) but not as both.

            - **key** *(string) --*

              The field identifier.

            - **stringValue** *(string) --*

              The field value, expressed as a String.

            - **refValue** *(string) --*

              The field value, expressed as the identifier of another object.

    - **marker** *(string) --*

      The starting point for the next page of results. To view the next page of results, call
      ``DescribeObjects`` again with this marker value. If the value is null, there are no more
      results.

    - **hasMoreResults** *(boolean) --*

      Indicates whether there are more results to return.
    """


_ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef = TypedDict(
    "_ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef(
    _ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef
):
    """
    Type definition for `ClientDescribePipelinesResponsepipelineDescriptionList` `fields`

    A key-value pair that describes a property of a pipeline object. The value is specified
    as either a string value (``StringValue`` ) or a reference to another object
    (``RefValue`` ) but not as both.

    - **key** *(string) --*

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.

    - **refValue** *(string) --*

      The field value, expressed as the identifier of another object.
    """


_ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef = TypedDict(
    "_ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef(
    _ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef
):
    """
    Type definition for `ClientDescribePipelinesResponsepipelineDescriptionList` `tags`

    Tags are key/value pairs defined by a user and associated with a pipeline to control
    access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more
    information, see `Controlling User Access to Pipelines
    <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
    in the *AWS Data Pipeline Developer Guide* .

    - **key** *(string) --*

      The key name of a tag defined by a user. For more information, see `Controlling User
      Access to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
      in the *AWS Data Pipeline Developer Guide* .

    - **value** *(string) --*

      The optional value portion of a tag defined by a user. For more information, see
      `Controlling User Access to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
      in the *AWS Data Pipeline Developer Guide* .
    """


_ClientDescribePipelinesResponsepipelineDescriptionListTypeDef = TypedDict(
    "_ClientDescribePipelinesResponsepipelineDescriptionListTypeDef",
    {
        "pipelineId": str,
        "name": str,
        "fields": List[
            ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef
        ],
        "description": str,
        "tags": List[ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef],
    },
    total=False,
)


class ClientDescribePipelinesResponsepipelineDescriptionListTypeDef(
    _ClientDescribePipelinesResponsepipelineDescriptionListTypeDef
):
    """
    Type definition for `ClientDescribePipelinesResponse` `pipelineDescriptionList`

    Contains pipeline metadata.

    - **pipelineId** *(string) --*

      The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the
      form ``df-297EG78HU43EEXAMPLE`` .

    - **name** *(string) --*

      The name of the pipeline.

    - **fields** *(list) --*

      A list of read-only fields that contain metadata about the pipeline: @userId, @accountId,
      and @pipelineState.

      - *(dict) --*

        A key-value pair that describes a property of a pipeline object. The value is specified
        as either a string value (``StringValue`` ) or a reference to another object
        (``RefValue`` ) but not as both.

        - **key** *(string) --*

          The field identifier.

        - **stringValue** *(string) --*

          The field value, expressed as a String.

        - **refValue** *(string) --*

          The field value, expressed as the identifier of another object.

    - **description** *(string) --*

      Description of the pipeline.

    - **tags** *(list) --*

      A list of tags to associated with a pipeline. Tags let you control access to pipelines.
      For more information, see `Controlling User Access to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
      in the *AWS Data Pipeline Developer Guide* .

      - *(dict) --*

        Tags are key/value pairs defined by a user and associated with a pipeline to control
        access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more
        information, see `Controlling User Access to Pipelines
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
        in the *AWS Data Pipeline Developer Guide* .

        - **key** *(string) --*

          The key name of a tag defined by a user. For more information, see `Controlling User
          Access to Pipelines
          <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
          in the *AWS Data Pipeline Developer Guide* .

        - **value** *(string) --*

          The optional value portion of a tag defined by a user. For more information, see
          `Controlling User Access to Pipelines
          <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
          in the *AWS Data Pipeline Developer Guide* .
    """


_ClientDescribePipelinesResponseTypeDef = TypedDict(
    "_ClientDescribePipelinesResponseTypeDef",
    {
        "pipelineDescriptionList": List[
            ClientDescribePipelinesResponsepipelineDescriptionListTypeDef
        ]
    },
    total=False,
)


class ClientDescribePipelinesResponseTypeDef(_ClientDescribePipelinesResponseTypeDef):
    """
    Type definition for `ClientDescribePipelines` `Response`

    Contains the output of DescribePipelines.

    - **pipelineDescriptionList** *(list) --*

      An array of descriptions for the specified pipelines.

      - *(dict) --*

        Contains pipeline metadata.

        - **pipelineId** *(string) --*

          The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the
          form ``df-297EG78HU43EEXAMPLE`` .

        - **name** *(string) --*

          The name of the pipeline.

        - **fields** *(list) --*

          A list of read-only fields that contain metadata about the pipeline: @userId, @accountId,
          and @pipelineState.

          - *(dict) --*

            A key-value pair that describes a property of a pipeline object. The value is specified
            as either a string value (``StringValue`` ) or a reference to another object
            (``RefValue`` ) but not as both.

            - **key** *(string) --*

              The field identifier.

            - **stringValue** *(string) --*

              The field value, expressed as a String.

            - **refValue** *(string) --*

              The field value, expressed as the identifier of another object.

        - **description** *(string) --*

          Description of the pipeline.

        - **tags** *(list) --*

          A list of tags to associated with a pipeline. Tags let you control access to pipelines.
          For more information, see `Controlling User Access to Pipelines
          <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
          in the *AWS Data Pipeline Developer Guide* .

          - *(dict) --*

            Tags are key/value pairs defined by a user and associated with a pipeline to control
            access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more
            information, see `Controlling User Access to Pipelines
            <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
            in the *AWS Data Pipeline Developer Guide* .

            - **key** *(string) --*

              The key name of a tag defined by a user. For more information, see `Controlling User
              Access to Pipelines
              <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
              in the *AWS Data Pipeline Developer Guide* .

            - **value** *(string) --*

              The optional value portion of a tag defined by a user. For more information, see
              `Controlling User Access to Pipelines
              <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__
              in the *AWS Data Pipeline Developer Guide* .
    """


_ClientEvaluateExpressionResponseTypeDef = TypedDict(
    "_ClientEvaluateExpressionResponseTypeDef",
    {"evaluatedExpression": str},
    total=False,
)


class ClientEvaluateExpressionResponseTypeDef(_ClientEvaluateExpressionResponseTypeDef):
    """
    Type definition for `ClientEvaluateExpression` `Response`

    Contains the output of EvaluateExpression.

    - **evaluatedExpression** *(string) --*

      The evaluated expression.
    """


_ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
    total=False,
)


class ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef(
    _ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef
):
    """
    Type definition for `ClientGetPipelineDefinitionResponseparameterObjects` `attributes`

    The attributes allowed or specified with a parameter object.

    - **key** *(string) --*

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.
    """


_ClientGetPipelineDefinitionResponseparameterObjectsTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponseparameterObjectsTypeDef",
    {
        "id": str,
        "attributes": List[
            ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef
        ],
    },
    total=False,
)


class ClientGetPipelineDefinitionResponseparameterObjectsTypeDef(
    _ClientGetPipelineDefinitionResponseparameterObjectsTypeDef
):
    """
    Type definition for `ClientGetPipelineDefinitionResponse` `parameterObjects`

    Contains information about a parameter object.

    - **id** *(string) --*

      The ID of the parameter object.

    - **attributes** *(list) --*

      The attributes of the parameter object.

      - *(dict) --*

        The attributes allowed or specified with a parameter object.

        - **key** *(string) --*

          The field identifier.

        - **stringValue** *(string) --*

          The field value, expressed as a String.
    """


_ClientGetPipelineDefinitionResponseparameterValuesTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponseparameterValuesTypeDef",
    {"id": str, "stringValue": str},
    total=False,
)


class ClientGetPipelineDefinitionResponseparameterValuesTypeDef(
    _ClientGetPipelineDefinitionResponseparameterValuesTypeDef
):
    """
    Type definition for `ClientGetPipelineDefinitionResponse` `parameterValues`

    A value or list of parameter values.

    - **id** *(string) --*

      The ID of the parameter value.

    - **stringValue** *(string) --*

      The field value, expressed as a String.
    """


_ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef(
    _ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef
):
    """
    Type definition for `ClientGetPipelineDefinitionResponsepipelineObjects` `fields`

    A key-value pair that describes a property of a pipeline object. The value is specified
    as either a string value (``StringValue`` ) or a reference to another object
    (``RefValue`` ) but not as both.

    - **key** *(string) --*

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.

    - **refValue** *(string) --*

      The field value, expressed as the identifier of another object.
    """


_ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)


class ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef(
    _ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef
):
    """
    Type definition for `ClientGetPipelineDefinitionResponse` `pipelineObjects`

    Contains information about a pipeline object. This can be a logical, physical, or physical
    attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

    - **id** *(string) --*

      The ID of the object.

    - **name** *(string) --*

      The name of the object.

    - **fields** *(list) --*

      Key-value pairs that define the properties of the object.

      - *(dict) --*

        A key-value pair that describes a property of a pipeline object. The value is specified
        as either a string value (``StringValue`` ) or a reference to another object
        (``RefValue`` ) but not as both.

        - **key** *(string) --*

          The field identifier.

        - **stringValue** *(string) --*

          The field value, expressed as a String.

        - **refValue** *(string) --*

          The field value, expressed as the identifier of another object.
    """


_ClientGetPipelineDefinitionResponseTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponseTypeDef",
    {
        "pipelineObjects": List[
            ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef
        ],
        "parameterObjects": List[
            ClientGetPipelineDefinitionResponseparameterObjectsTypeDef
        ],
        "parameterValues": List[
            ClientGetPipelineDefinitionResponseparameterValuesTypeDef
        ],
    },
    total=False,
)


class ClientGetPipelineDefinitionResponseTypeDef(
    _ClientGetPipelineDefinitionResponseTypeDef
):
    """
    Type definition for `ClientGetPipelineDefinition` `Response`

    Contains the output of GetPipelineDefinition.

    - **pipelineObjects** *(list) --*

      The objects defined in the pipeline.

      - *(dict) --*

        Contains information about a pipeline object. This can be a logical, physical, or physical
        attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

        - **id** *(string) --*

          The ID of the object.

        - **name** *(string) --*

          The name of the object.

        - **fields** *(list) --*

          Key-value pairs that define the properties of the object.

          - *(dict) --*

            A key-value pair that describes a property of a pipeline object. The value is specified
            as either a string value (``StringValue`` ) or a reference to another object
            (``RefValue`` ) but not as both.

            - **key** *(string) --*

              The field identifier.

            - **stringValue** *(string) --*

              The field value, expressed as a String.

            - **refValue** *(string) --*

              The field value, expressed as the identifier of another object.

    - **parameterObjects** *(list) --*

      The parameter objects used in the pipeline definition.

      - *(dict) --*

        Contains information about a parameter object.

        - **id** *(string) --*

          The ID of the parameter object.

        - **attributes** *(list) --*

          The attributes of the parameter object.

          - *(dict) --*

            The attributes allowed or specified with a parameter object.

            - **key** *(string) --*

              The field identifier.

            - **stringValue** *(string) --*

              The field value, expressed as a String.

    - **parameterValues** *(list) --*

      The parameter values used in the pipeline definition.

      - *(dict) --*

        A value or list of parameter values.

        - **id** *(string) --*

          The ID of the parameter value.

        - **stringValue** *(string) --*

          The field value, expressed as a String.
    """


_ClientListPipelinesResponsepipelineIdListTypeDef = TypedDict(
    "_ClientListPipelinesResponsepipelineIdListTypeDef",
    {"id": str, "name": str},
    total=False,
)


class ClientListPipelinesResponsepipelineIdListTypeDef(
    _ClientListPipelinesResponsepipelineIdListTypeDef
):
    """
    Type definition for `ClientListPipelinesResponse` `pipelineIdList`

    Contains the name and identifier of a pipeline.

    - **id** *(string) --*

      The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the
      form ``df-297EG78HU43EEXAMPLE`` .

    - **name** *(string) --*

      The name of the pipeline.
    """


_ClientListPipelinesResponseTypeDef = TypedDict(
    "_ClientListPipelinesResponseTypeDef",
    {
        "pipelineIdList": List[ClientListPipelinesResponsepipelineIdListTypeDef],
        "marker": str,
        "hasMoreResults": bool,
    },
    total=False,
)


class ClientListPipelinesResponseTypeDef(_ClientListPipelinesResponseTypeDef):
    """
    Type definition for `ClientListPipelines` `Response`

    Contains the output of ListPipelines.

    - **pipelineIdList** *(list) --*

      The pipeline identifiers. If you require additional information about the pipelines, you can
      use these identifiers to call  DescribePipelines and  GetPipelineDefinition .

      - *(dict) --*

        Contains the name and identifier of a pipeline.

        - **id** *(string) --*

          The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the
          form ``df-297EG78HU43EEXAMPLE`` .

        - **name** *(string) --*

          The name of the pipeline.

    - **marker** *(string) --*

      The starting point for the next page of results. To view the next page of results, call
      ``ListPipelinesOutput`` again with this marker value. If the value is null, there are no more
      results.

    - **hasMoreResults** *(boolean) --*

      Indicates whether there are more results that can be obtained by a subsequent call.
    """


_ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef = TypedDict(
    "_ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef(
    _ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef
):
    """
    Type definition for `ClientPollForTaskResponsetaskObjectobjects` `fields`

    A key-value pair that describes a property of a pipeline object. The value is
    specified as either a string value (``StringValue`` ) or a reference to another
    object (``RefValue`` ) but not as both.

    - **key** *(string) --*

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.

    - **refValue** *(string) --*

      The field value, expressed as the identifier of another object.
    """


_ClientPollForTaskResponsetaskObjectobjectsTypeDef = TypedDict(
    "_ClientPollForTaskResponsetaskObjectobjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef],
    },
    total=False,
)


class ClientPollForTaskResponsetaskObjectobjectsTypeDef(
    _ClientPollForTaskResponsetaskObjectobjectsTypeDef
):
    """
    Type definition for `ClientPollForTaskResponsetaskObject` `objects`

    Contains information about a pipeline object. This can be a logical, physical, or
    physical attempt pipeline object. The complete set of components of a pipeline defines
    the pipeline.

    - **id** *(string) --*

      The ID of the object.

    - **name** *(string) --*

      The name of the object.

    - **fields** *(list) --*

      Key-value pairs that define the properties of the object.

      - *(dict) --*

        A key-value pair that describes a property of a pipeline object. The value is
        specified as either a string value (``StringValue`` ) or a reference to another
        object (``RefValue`` ) but not as both.

        - **key** *(string) --*

          The field identifier.

        - **stringValue** *(string) --*

          The field value, expressed as a String.

        - **refValue** *(string) --*

          The field value, expressed as the identifier of another object.
    """


_ClientPollForTaskResponsetaskObjectTypeDef = TypedDict(
    "_ClientPollForTaskResponsetaskObjectTypeDef",
    {
        "taskId": str,
        "pipelineId": str,
        "attemptId": str,
        "objects": Dict[str, ClientPollForTaskResponsetaskObjectobjectsTypeDef],
    },
    total=False,
)


class ClientPollForTaskResponsetaskObjectTypeDef(
    _ClientPollForTaskResponsetaskObjectTypeDef
):
    """
    Type definition for `ClientPollForTaskResponse` `taskObject`

    The information needed to complete the task that is being assigned to the task runner. One of
    the fields returned in this object is ``taskId`` , which contains an identifier for the task
    being assigned. The calling task runner uses ``taskId`` in subsequent calls to
    ReportTaskProgress and  SetTaskStatus .

    - **taskId** *(string) --*

      An internal identifier for the task. This ID is passed to the  SetTaskStatus and
      ReportTaskProgress actions.

    - **pipelineId** *(string) --*

      The ID of the pipeline that provided the task.

    - **attemptId** *(string) --*

      The ID of the pipeline task attempt object. AWS Data Pipeline uses this value to track how
      many times a task is attempted.

    - **objects** *(dict) --*

      Connection information for the location where the task runner will publish the output of
      the task.

      - *(string) --*

        - *(dict) --*

          Contains information about a pipeline object. This can be a logical, physical, or
          physical attempt pipeline object. The complete set of components of a pipeline defines
          the pipeline.

          - **id** *(string) --*

            The ID of the object.

          - **name** *(string) --*

            The name of the object.

          - **fields** *(list) --*

            Key-value pairs that define the properties of the object.

            - *(dict) --*

              A key-value pair that describes a property of a pipeline object. The value is
              specified as either a string value (``StringValue`` ) or a reference to another
              object (``RefValue`` ) but not as both.

              - **key** *(string) --*

                The field identifier.

              - **stringValue** *(string) --*

                The field value, expressed as a String.

              - **refValue** *(string) --*

                The field value, expressed as the identifier of another object.
    """


_ClientPollForTaskResponseTypeDef = TypedDict(
    "_ClientPollForTaskResponseTypeDef",
    {"taskObject": ClientPollForTaskResponsetaskObjectTypeDef},
    total=False,
)


class ClientPollForTaskResponseTypeDef(_ClientPollForTaskResponseTypeDef):
    """
    Type definition for `ClientPollForTask` `Response`

    Contains the output of PollForTask.

    - **taskObject** *(dict) --*

      The information needed to complete the task that is being assigned to the task runner. One of
      the fields returned in this object is ``taskId`` , which contains an identifier for the task
      being assigned. The calling task runner uses ``taskId`` in subsequent calls to
      ReportTaskProgress and  SetTaskStatus .

      - **taskId** *(string) --*

        An internal identifier for the task. This ID is passed to the  SetTaskStatus and
        ReportTaskProgress actions.

      - **pipelineId** *(string) --*

        The ID of the pipeline that provided the task.

      - **attemptId** *(string) --*

        The ID of the pipeline task attempt object. AWS Data Pipeline uses this value to track how
        many times a task is attempted.

      - **objects** *(dict) --*

        Connection information for the location where the task runner will publish the output of
        the task.

        - *(string) --*

          - *(dict) --*

            Contains information about a pipeline object. This can be a logical, physical, or
            physical attempt pipeline object. The complete set of components of a pipeline defines
            the pipeline.

            - **id** *(string) --*

              The ID of the object.

            - **name** *(string) --*

              The name of the object.

            - **fields** *(list) --*

              Key-value pairs that define the properties of the object.

              - *(dict) --*

                A key-value pair that describes a property of a pipeline object. The value is
                specified as either a string value (``StringValue`` ) or a reference to another
                object (``RefValue`` ) but not as both.

                - **key** *(string) --*

                  The field identifier.

                - **stringValue** *(string) --*

                  The field value, expressed as a String.

                - **refValue** *(string) --*

                  The field value, expressed as the identifier of another object.
    """


_ClientPollForTaskinstanceIdentityTypeDef = TypedDict(
    "_ClientPollForTaskinstanceIdentityTypeDef",
    {"document": str, "signature": str},
    total=False,
)


class ClientPollForTaskinstanceIdentityTypeDef(
    _ClientPollForTaskinstanceIdentityTypeDef
):
    """
    Type definition for `ClientPollForTask` `instanceIdentity`

    Identity information for the EC2 instance that is hosting the task runner. You can get this value
    from the instance using ``http://169.254.169.254/latest/meta-data/instance-id`` . For more
    information, see `Instance Metadata
    <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html>`__ in the
    *Amazon Elastic Compute Cloud User Guide.* Passing in this value proves that your task runner is
    running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied
    to your pipeline.

    - **document** *(string) --*

      A description of an EC2 instance that is generated when the instance is launched and exposed to
      the instance via the instance metadata service in the form of a JSON representation of an
      object.

    - **signature** *(string) --*

      A signature which can be used to verify the accuracy and authenticity of the information
      provided in the instance identity document.
    """


_ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef",
    {"id": str, "errors": List[str]},
    total=False,
)


class ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef(
    _ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef
):
    """
    Type definition for `ClientPutPipelineDefinitionResponse` `validationErrors`

    Defines a validation error. Validation errors prevent pipeline activation. The set of
    validation errors that can be returned are defined by AWS Data Pipeline.

    - **id** *(string) --*

      The identifier of the object that contains the validation error.

    - **errors** *(list) --*

      A description of the validation error.

      - *(string) --*
    """


_ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef",
    {"id": str, "warnings": List[str]},
    total=False,
)


class ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef(
    _ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef
):
    """
    Type definition for `ClientPutPipelineDefinitionResponse` `validationWarnings`

    Defines a validation warning. Validation warnings do not prevent pipeline activation. The
    set of validation warnings that can be returned are defined by AWS Data Pipeline.

    - **id** *(string) --*

      The identifier of the object that contains the validation warning.

    - **warnings** *(list) --*

      A description of the validation warning.

      - *(string) --*
    """


_ClientPutPipelineDefinitionResponseTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionResponseTypeDef",
    {
        "validationErrors": List[
            ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef
        ],
        "validationWarnings": List[
            ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef
        ],
        "errored": bool,
    },
    total=False,
)


class ClientPutPipelineDefinitionResponseTypeDef(
    _ClientPutPipelineDefinitionResponseTypeDef
):
    """
    Type definition for `ClientPutPipelineDefinition` `Response`

    Contains the output of PutPipelineDefinition.

    - **validationErrors** *(list) --*

      The validation errors that are associated with the objects defined in ``pipelineObjects`` .

      - *(dict) --*

        Defines a validation error. Validation errors prevent pipeline activation. The set of
        validation errors that can be returned are defined by AWS Data Pipeline.

        - **id** *(string) --*

          The identifier of the object that contains the validation error.

        - **errors** *(list) --*

          A description of the validation error.

          - *(string) --*

    - **validationWarnings** *(list) --*

      The validation warnings that are associated with the objects defined in ``pipelineObjects`` .

      - *(dict) --*

        Defines a validation warning. Validation warnings do not prevent pipeline activation. The
        set of validation warnings that can be returned are defined by AWS Data Pipeline.

        - **id** *(string) --*

          The identifier of the object that contains the validation warning.

        - **warnings** *(list) --*

          A description of the validation warning.

          - *(string) --*

    - **errored** *(boolean) --*

      Indicates whether there were validation errors, and the pipeline definition is stored but
      cannot be activated until you correct the pipeline and call ``PutPipelineDefinition`` to
      commit the corrected pipeline.
    """


_ClientPutPipelineDefinitionparameterObjectsattributesTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionparameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
)


class ClientPutPipelineDefinitionparameterObjectsattributesTypeDef(
    _ClientPutPipelineDefinitionparameterObjectsattributesTypeDef
):
    """
    Type definition for `ClientPutPipelineDefinitionparameterObjects` `attributes`

    The attributes allowed or specified with a parameter object.

    - **key** *(string) --* **[REQUIRED]**

      The field identifier.

    - **stringValue** *(string) --* **[REQUIRED]**

      The field value, expressed as a String.
    """


_ClientPutPipelineDefinitionparameterObjectsTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionparameterObjectsTypeDef",
    {
        "id": str,
        "attributes": List[
            ClientPutPipelineDefinitionparameterObjectsattributesTypeDef
        ],
    },
)


class ClientPutPipelineDefinitionparameterObjectsTypeDef(
    _ClientPutPipelineDefinitionparameterObjectsTypeDef
):
    """
    Type definition for `ClientPutPipelineDefinition` `parameterObjects`

    Contains information about a parameter object.

    - **id** *(string) --* **[REQUIRED]**

      The ID of the parameter object.

    - **attributes** *(list) --* **[REQUIRED]**

      The attributes of the parameter object.

      - *(dict) --*

        The attributes allowed or specified with a parameter object.

        - **key** *(string) --* **[REQUIRED]**

          The field identifier.

        - **stringValue** *(string) --* **[REQUIRED]**

          The field value, expressed as a String.
    """


_ClientPutPipelineDefinitionparameterValuesTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionparameterValuesTypeDef",
    {"id": str, "stringValue": str},
)


class ClientPutPipelineDefinitionparameterValuesTypeDef(
    _ClientPutPipelineDefinitionparameterValuesTypeDef
):
    """
    Type definition for `ClientPutPipelineDefinition` `parameterValues`

    A value or list of parameter values.

    - **id** *(string) --* **[REQUIRED]**

      The ID of the parameter value.

    - **stringValue** *(string) --* **[REQUIRED]**

      The field value, expressed as a String.
    """


_RequiredClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef = TypedDict(
    "_RequiredClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef", {"key": str}
)
_OptionalClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef = TypedDict(
    "_OptionalClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef",
    {"stringValue": str, "refValue": str},
    total=False,
)


class ClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef(
    _RequiredClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef,
    _OptionalClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef,
):
    """
    Type definition for `ClientPutPipelineDefinitionpipelineObjects` `fields`

    A key-value pair that describes a property of a pipeline object. The value is specified as
    either a string value (``StringValue`` ) or a reference to another object (``RefValue`` )
    but not as both.

    - **key** *(string) --* **[REQUIRED]**

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.

    - **refValue** *(string) --*

      The field value, expressed as the identifier of another object.
    """


_ClientPutPipelineDefinitionpipelineObjectsTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionpipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientPutPipelineDefinitionpipelineObjectsfieldsTypeDef],
    },
)


class ClientPutPipelineDefinitionpipelineObjectsTypeDef(
    _ClientPutPipelineDefinitionpipelineObjectsTypeDef
):
    """
    Type definition for `ClientPutPipelineDefinition` `pipelineObjects`

    Contains information about a pipeline object. This can be a logical, physical, or physical
    attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

    - **id** *(string) --* **[REQUIRED]**

      The ID of the object.

    - **name** *(string) --* **[REQUIRED]**

      The name of the object.

    - **fields** *(list) --* **[REQUIRED]**

      Key-value pairs that define the properties of the object.

      - *(dict) --*

        A key-value pair that describes a property of a pipeline object. The value is specified as
        either a string value (``StringValue`` ) or a reference to another object (``RefValue`` )
        but not as both.

        - **key** *(string) --* **[REQUIRED]**

          The field identifier.

        - **stringValue** *(string) --*

          The field value, expressed as a String.

        - **refValue** *(string) --*

          The field value, expressed as the identifier of another object.
    """


_ClientQueryObjectsResponseTypeDef = TypedDict(
    "_ClientQueryObjectsResponseTypeDef",
    {"ids": List[str], "marker": str, "hasMoreResults": bool},
    total=False,
)


class ClientQueryObjectsResponseTypeDef(_ClientQueryObjectsResponseTypeDef):
    """
    Type definition for `ClientQueryObjects` `Response`

    Contains the output of QueryObjects.

    - **ids** *(list) --*

      The identifiers that match the query selectors.

      - *(string) --*

    - **marker** *(string) --*

      The starting point for the next page of results. To view the next page of results, call
      ``QueryObjects`` again with this marker value. If the value is null, there are no more
      results.

    - **hasMoreResults** *(boolean) --*

      Indicates whether there are more results that can be obtained by a subsequent call.
    """


_ClientQueryObjectsqueryselectorsoperatorTypeDef = TypedDict(
    "_ClientQueryObjectsqueryselectorsoperatorTypeDef",
    {"type": str, "values": List[str]},
    total=False,
)


class ClientQueryObjectsqueryselectorsoperatorTypeDef(
    _ClientQueryObjectsqueryselectorsoperatorTypeDef
):
    """
    Type definition for `ClientQueryObjectsqueryselectors` `operator`

    Contains a logical operation for comparing the value of a field with a specified value.

    - **type** *(string) --*

      The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ),
      less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ).
      Equal reference (``REF_EQ`` ) can be used only with reference fields. The other
      comparison types can be used only with String fields. The comparison types you can use
      apply only to certain object fields, as detailed below.

      The comparison operators EQ and REF_EQ act on the following fields:

      * name

      * @sphere

      * parent

      * @componentParent

      * @instanceParent

      * @status

      * @scheduledStartTime

      * @scheduledEndTime

      * @actualStartTime

      * @actualEndTime

      The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields:

      * @scheduledStartTime

      * @scheduledEndTime

      * @actualStartTime

      * @actualEndTime

      Note that fields beginning with the at sign (@) are read-only and set by the web service.
      When you name fields, you should choose names containing only alpha-numeric values, as
      symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a
      pipeline should prefix their name with the string "my".

    - **values** *(list) --*

      The value that the actual field value will be compared with.

      - *(string) --*
    """


_ClientQueryObjectsqueryselectorsTypeDef = TypedDict(
    "_ClientQueryObjectsqueryselectorsTypeDef",
    {"fieldName": str, "operator": ClientQueryObjectsqueryselectorsoperatorTypeDef},
    total=False,
)


class ClientQueryObjectsqueryselectorsTypeDef(_ClientQueryObjectsqueryselectorsTypeDef):
    """
    Type definition for `ClientQueryObjectsquery` `selectors`

    A comparision that is used to determine whether a query should return this object.

    - **fieldName** *(string) --*

      The name of the field that the operator will be applied to. The field name is the "key"
      portion of the field definition in the pipeline definition syntax that is used by the AWS
      Data Pipeline API. If the field is not set on the object, the condition fails.

    - **operator** *(dict) --*

      Contains a logical operation for comparing the value of a field with a specified value.

      - **type** *(string) --*

        The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ),
        less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ).
        Equal reference (``REF_EQ`` ) can be used only with reference fields. The other
        comparison types can be used only with String fields. The comparison types you can use
        apply only to certain object fields, as detailed below.

        The comparison operators EQ and REF_EQ act on the following fields:

        * name

        * @sphere

        * parent

        * @componentParent

        * @instanceParent

        * @status

        * @scheduledStartTime

        * @scheduledEndTime

        * @actualStartTime

        * @actualEndTime

        The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields:

        * @scheduledStartTime

        * @scheduledEndTime

        * @actualStartTime

        * @actualEndTime

        Note that fields beginning with the at sign (@) are read-only and set by the web service.
        When you name fields, you should choose names containing only alpha-numeric values, as
        symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a
        pipeline should prefix their name with the string "my".

      - **values** *(list) --*

        The value that the actual field value will be compared with.

        - *(string) --*
    """


_ClientQueryObjectsqueryTypeDef = TypedDict(
    "_ClientQueryObjectsqueryTypeDef",
    {"selectors": List[ClientQueryObjectsqueryselectorsTypeDef]},
    total=False,
)


class ClientQueryObjectsqueryTypeDef(_ClientQueryObjectsqueryTypeDef):
    """
    Type definition for `ClientQueryObjects` `query`

    The query that defines the objects to be returned. The ``Query`` object can contain a maximum of
    ten selectors. The conditions in the query are limited to top-level String fields in the object.
    These filters can be applied to components, instances, and attempts.

    - **selectors** *(list) --*

      List of selectors that define the query. An object must satisfy all of the selectors to match
      the query.

      - *(dict) --*

        A comparision that is used to determine whether a query should return this object.

        - **fieldName** *(string) --*

          The name of the field that the operator will be applied to. The field name is the "key"
          portion of the field definition in the pipeline definition syntax that is used by the AWS
          Data Pipeline API. If the field is not set on the object, the condition fails.

        - **operator** *(dict) --*

          Contains a logical operation for comparing the value of a field with a specified value.

          - **type** *(string) --*

            The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ),
            less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ).
            Equal reference (``REF_EQ`` ) can be used only with reference fields. The other
            comparison types can be used only with String fields. The comparison types you can use
            apply only to certain object fields, as detailed below.

            The comparison operators EQ and REF_EQ act on the following fields:

            * name

            * @sphere

            * parent

            * @componentParent

            * @instanceParent

            * @status

            * @scheduledStartTime

            * @scheduledEndTime

            * @actualStartTime

            * @actualEndTime

            The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields:

            * @scheduledStartTime

            * @scheduledEndTime

            * @actualStartTime

            * @actualEndTime

            Note that fields beginning with the at sign (@) are read-only and set by the web service.
            When you name fields, you should choose names containing only alpha-numeric values, as
            symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a
            pipeline should prefix their name with the string "my".

          - **values** *(list) --*

            The value that the actual field value will be compared with.

            - *(string) --*
    """


_ClientReportTaskProgressResponseTypeDef = TypedDict(
    "_ClientReportTaskProgressResponseTypeDef", {"canceled": bool}, total=False
)


class ClientReportTaskProgressResponseTypeDef(_ClientReportTaskProgressResponseTypeDef):
    """
    Type definition for `ClientReportTaskProgress` `Response`

    Contains the output of ReportTaskProgress.

    - **canceled** *(boolean) --*

      If true, the calling task runner should cancel processing of the task. The task runner does
      not need to call  SetTaskStatus for canceled tasks.
    """


_RequiredClientReportTaskProgressfieldsTypeDef = TypedDict(
    "_RequiredClientReportTaskProgressfieldsTypeDef", {"key": str}
)
_OptionalClientReportTaskProgressfieldsTypeDef = TypedDict(
    "_OptionalClientReportTaskProgressfieldsTypeDef",
    {"stringValue": str, "refValue": str},
    total=False,
)


class ClientReportTaskProgressfieldsTypeDef(
    _RequiredClientReportTaskProgressfieldsTypeDef,
    _OptionalClientReportTaskProgressfieldsTypeDef,
):
    """
    Type definition for `ClientReportTaskProgress` `fields`

    A key-value pair that describes a property of a pipeline object. The value is specified as
    either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but
    not as both.

    - **key** *(string) --* **[REQUIRED]**

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.

    - **refValue** *(string) --*

      The field value, expressed as the identifier of another object.
    """


_ClientReportTaskRunnerHeartbeatResponseTypeDef = TypedDict(
    "_ClientReportTaskRunnerHeartbeatResponseTypeDef", {"terminate": bool}, total=False
)


class ClientReportTaskRunnerHeartbeatResponseTypeDef(
    _ClientReportTaskRunnerHeartbeatResponseTypeDef
):
    """
    Type definition for `ClientReportTaskRunnerHeartbeat` `Response`

    Contains the output of ReportTaskRunnerHeartbeat.

    - **terminate** *(boolean) --*

      Indicates whether the calling task runner should terminate.
    """


_ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef",
    {"id": str, "errors": List[str]},
    total=False,
)


class ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef(
    _ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef
):
    """
    Type definition for `ClientValidatePipelineDefinitionResponse` `validationErrors`

    Defines a validation error. Validation errors prevent pipeline activation. The set of
    validation errors that can be returned are defined by AWS Data Pipeline.

    - **id** *(string) --*

      The identifier of the object that contains the validation error.

    - **errors** *(list) --*

      A description of the validation error.

      - *(string) --*
    """


_ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef",
    {"id": str, "warnings": List[str]},
    total=False,
)


class ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef(
    _ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef
):
    """
    Type definition for `ClientValidatePipelineDefinitionResponse` `validationWarnings`

    Defines a validation warning. Validation warnings do not prevent pipeline activation. The
    set of validation warnings that can be returned are defined by AWS Data Pipeline.

    - **id** *(string) --*

      The identifier of the object that contains the validation warning.

    - **warnings** *(list) --*

      A description of the validation warning.

      - *(string) --*
    """


_ClientValidatePipelineDefinitionResponseTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionResponseTypeDef",
    {
        "validationErrors": List[
            ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef
        ],
        "validationWarnings": List[
            ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef
        ],
        "errored": bool,
    },
    total=False,
)


class ClientValidatePipelineDefinitionResponseTypeDef(
    _ClientValidatePipelineDefinitionResponseTypeDef
):
    """
    Type definition for `ClientValidatePipelineDefinition` `Response`

    Contains the output of ValidatePipelineDefinition.

    - **validationErrors** *(list) --*

      Any validation errors that were found.

      - *(dict) --*

        Defines a validation error. Validation errors prevent pipeline activation. The set of
        validation errors that can be returned are defined by AWS Data Pipeline.

        - **id** *(string) --*

          The identifier of the object that contains the validation error.

        - **errors** *(list) --*

          A description of the validation error.

          - *(string) --*

    - **validationWarnings** *(list) --*

      Any validation warnings that were found.

      - *(dict) --*

        Defines a validation warning. Validation warnings do not prevent pipeline activation. The
        set of validation warnings that can be returned are defined by AWS Data Pipeline.

        - **id** *(string) --*

          The identifier of the object that contains the validation warning.

        - **warnings** *(list) --*

          A description of the validation warning.

          - *(string) --*

    - **errored** *(boolean) --*

      Indicates whether there were validation errors.
    """


_ClientValidatePipelineDefinitionparameterObjectsattributesTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionparameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
)


class ClientValidatePipelineDefinitionparameterObjectsattributesTypeDef(
    _ClientValidatePipelineDefinitionparameterObjectsattributesTypeDef
):
    """
    Type definition for `ClientValidatePipelineDefinitionparameterObjects` `attributes`

    The attributes allowed or specified with a parameter object.

    - **key** *(string) --* **[REQUIRED]**

      The field identifier.

    - **stringValue** *(string) --* **[REQUIRED]**

      The field value, expressed as a String.
    """


_ClientValidatePipelineDefinitionparameterObjectsTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionparameterObjectsTypeDef",
    {
        "id": str,
        "attributes": List[
            ClientValidatePipelineDefinitionparameterObjectsattributesTypeDef
        ],
    },
)


class ClientValidatePipelineDefinitionparameterObjectsTypeDef(
    _ClientValidatePipelineDefinitionparameterObjectsTypeDef
):
    """
    Type definition for `ClientValidatePipelineDefinition` `parameterObjects`

    Contains information about a parameter object.

    - **id** *(string) --* **[REQUIRED]**

      The ID of the parameter object.

    - **attributes** *(list) --* **[REQUIRED]**

      The attributes of the parameter object.

      - *(dict) --*

        The attributes allowed or specified with a parameter object.

        - **key** *(string) --* **[REQUIRED]**

          The field identifier.

        - **stringValue** *(string) --* **[REQUIRED]**

          The field value, expressed as a String.
    """


_ClientValidatePipelineDefinitionparameterValuesTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionparameterValuesTypeDef",
    {"id": str, "stringValue": str},
)


class ClientValidatePipelineDefinitionparameterValuesTypeDef(
    _ClientValidatePipelineDefinitionparameterValuesTypeDef
):
    """
    Type definition for `ClientValidatePipelineDefinition` `parameterValues`

    A value or list of parameter values.

    - **id** *(string) --* **[REQUIRED]**

      The ID of the parameter value.

    - **stringValue** *(string) --* **[REQUIRED]**

      The field value, expressed as a String.
    """


_RequiredClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef = TypedDict(
    "_RequiredClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef",
    {"key": str},
)
_OptionalClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef = TypedDict(
    "_OptionalClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef",
    {"stringValue": str, "refValue": str},
    total=False,
)


class ClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef(
    _RequiredClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef,
    _OptionalClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef,
):
    """
    Type definition for `ClientValidatePipelineDefinitionpipelineObjects` `fields`

    A key-value pair that describes a property of a pipeline object. The value is specified as
    either a string value (``StringValue`` ) or a reference to another object (``RefValue`` )
    but not as both.

    - **key** *(string) --* **[REQUIRED]**

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.

    - **refValue** *(string) --*

      The field value, expressed as the identifier of another object.
    """


_ClientValidatePipelineDefinitionpipelineObjectsTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionpipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientValidatePipelineDefinitionpipelineObjectsfieldsTypeDef],
    },
)


class ClientValidatePipelineDefinitionpipelineObjectsTypeDef(
    _ClientValidatePipelineDefinitionpipelineObjectsTypeDef
):
    """
    Type definition for `ClientValidatePipelineDefinition` `pipelineObjects`

    Contains information about a pipeline object. This can be a logical, physical, or physical
    attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

    - **id** *(string) --* **[REQUIRED]**

      The ID of the object.

    - **name** *(string) --* **[REQUIRED]**

      The name of the object.

    - **fields** *(list) --* **[REQUIRED]**

      Key-value pairs that define the properties of the object.

      - *(dict) --*

        A key-value pair that describes a property of a pipeline object. The value is specified as
        either a string value (``StringValue`` ) or a reference to another object (``RefValue`` )
        but not as both.

        - **key** *(string) --* **[REQUIRED]**

          The field identifier.

        - **stringValue** *(string) --*

          The field value, expressed as a String.

        - **refValue** *(string) --*

          The field value, expressed as the identifier of another object.
    """


_DescribeObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeObjectsPaginatePaginationConfigTypeDef(
    _DescribeObjectsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeObjectsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "_DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef(
    _DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef
):
    """
    Type definition for `DescribeObjectsPaginateResponsepipelineObjects` `fields`

    A key-value pair that describes a property of a pipeline object. The value is specified
    as either a string value (``StringValue`` ) or a reference to another object
    (``RefValue`` ) but not as both.

    - **key** *(string) --*

      The field identifier.

    - **stringValue** *(string) --*

      The field value, expressed as a String.

    - **refValue** *(string) --*

      The field value, expressed as the identifier of another object.
    """


_DescribeObjectsPaginateResponsepipelineObjectsTypeDef = TypedDict(
    "_DescribeObjectsPaginateResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)


class DescribeObjectsPaginateResponsepipelineObjectsTypeDef(
    _DescribeObjectsPaginateResponsepipelineObjectsTypeDef
):
    """
    Type definition for `DescribeObjectsPaginateResponse` `pipelineObjects`

    Contains information about a pipeline object. This can be a logical, physical, or physical
    attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

    - **id** *(string) --*

      The ID of the object.

    - **name** *(string) --*

      The name of the object.

    - **fields** *(list) --*

      Key-value pairs that define the properties of the object.

      - *(dict) --*

        A key-value pair that describes a property of a pipeline object. The value is specified
        as either a string value (``StringValue`` ) or a reference to another object
        (``RefValue`` ) but not as both.

        - **key** *(string) --*

          The field identifier.

        - **stringValue** *(string) --*

          The field value, expressed as a String.

        - **refValue** *(string) --*

          The field value, expressed as the identifier of another object.
    """


_DescribeObjectsPaginateResponseTypeDef = TypedDict(
    "_DescribeObjectsPaginateResponseTypeDef",
    {
        "pipelineObjects": List[DescribeObjectsPaginateResponsepipelineObjectsTypeDef],
        "hasMoreResults": bool,
        "NextToken": str,
    },
    total=False,
)


class DescribeObjectsPaginateResponseTypeDef(_DescribeObjectsPaginateResponseTypeDef):
    """
    Type definition for `DescribeObjectsPaginate` `Response`

    Contains the output of DescribeObjects.

    - **pipelineObjects** *(list) --*

      An array of object definitions.

      - *(dict) --*

        Contains information about a pipeline object. This can be a logical, physical, or physical
        attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

        - **id** *(string) --*

          The ID of the object.

        - **name** *(string) --*

          The name of the object.

        - **fields** *(list) --*

          Key-value pairs that define the properties of the object.

          - *(dict) --*

            A key-value pair that describes a property of a pipeline object. The value is specified
            as either a string value (``StringValue`` ) or a reference to another object
            (``RefValue`` ) but not as both.

            - **key** *(string) --*

              The field identifier.

            - **stringValue** *(string) --*

              The field value, expressed as a String.

            - **refValue** *(string) --*

              The field value, expressed as the identifier of another object.

    - **hasMoreResults** *(boolean) --*

      Indicates whether there are more results to return.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPipelinesPaginatePaginationConfigTypeDef(
    _ListPipelinesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPipelinesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListPipelinesPaginateResponsepipelineIdListTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsepipelineIdListTypeDef",
    {"id": str, "name": str},
    total=False,
)


class ListPipelinesPaginateResponsepipelineIdListTypeDef(
    _ListPipelinesPaginateResponsepipelineIdListTypeDef
):
    """
    Type definition for `ListPipelinesPaginateResponse` `pipelineIdList`

    Contains the name and identifier of a pipeline.

    - **id** *(string) --*

      The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the
      form ``df-297EG78HU43EEXAMPLE`` .

    - **name** *(string) --*

      The name of the pipeline.
    """


_ListPipelinesPaginateResponseTypeDef = TypedDict(
    "_ListPipelinesPaginateResponseTypeDef",
    {
        "pipelineIdList": List[ListPipelinesPaginateResponsepipelineIdListTypeDef],
        "hasMoreResults": bool,
        "NextToken": str,
    },
    total=False,
)


class ListPipelinesPaginateResponseTypeDef(_ListPipelinesPaginateResponseTypeDef):
    """
    Type definition for `ListPipelinesPaginate` `Response`

    Contains the output of ListPipelines.

    - **pipelineIdList** *(list) --*

      The pipeline identifiers. If you require additional information about the pipelines, you can
      use these identifiers to call  DescribePipelines and  GetPipelineDefinition .

      - *(dict) --*

        Contains the name and identifier of a pipeline.

        - **id** *(string) --*

          The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the
          form ``df-297EG78HU43EEXAMPLE`` .

        - **name** *(string) --*

          The name of the pipeline.

    - **hasMoreResults** *(boolean) --*

      Indicates whether there are more results that can be obtained by a subsequent call.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_QueryObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_QueryObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class QueryObjectsPaginatePaginationConfigTypeDef(
    _QueryObjectsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `QueryObjectsPaginate` `PaginationConfig`

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


_QueryObjectsPaginateResponseTypeDef = TypedDict(
    "_QueryObjectsPaginateResponseTypeDef",
    {"ids": List[str], "hasMoreResults": bool, "NextToken": str},
    total=False,
)


class QueryObjectsPaginateResponseTypeDef(_QueryObjectsPaginateResponseTypeDef):
    """
    Type definition for `QueryObjectsPaginate` `Response`

    Contains the output of QueryObjects.

    - **ids** *(list) --*

      The identifiers that match the query selectors.

      - *(string) --*

    - **hasMoreResults** *(boolean) --*

      Indicates whether there are more results that can be obtained by a subsequent call.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_QueryObjectsPaginatequeryselectorsoperatorTypeDef = TypedDict(
    "_QueryObjectsPaginatequeryselectorsoperatorTypeDef",
    {"type": str, "values": List[str]},
    total=False,
)


class QueryObjectsPaginatequeryselectorsoperatorTypeDef(
    _QueryObjectsPaginatequeryselectorsoperatorTypeDef
):
    """
    Type definition for `QueryObjectsPaginatequeryselectors` `operator`

    Contains a logical operation for comparing the value of a field with a specified value.

    - **type** *(string) --*

      The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ),
      less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ).
      Equal reference (``REF_EQ`` ) can be used only with reference fields. The other
      comparison types can be used only with String fields. The comparison types you can use
      apply only to certain object fields, as detailed below.

      The comparison operators EQ and REF_EQ act on the following fields:

      * name

      * @sphere

      * parent

      * @componentParent

      * @instanceParent

      * @status

      * @scheduledStartTime

      * @scheduledEndTime

      * @actualStartTime

      * @actualEndTime

      The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields:

      * @scheduledStartTime

      * @scheduledEndTime

      * @actualStartTime

      * @actualEndTime

      Note that fields beginning with the at sign (@) are read-only and set by the web service.
      When you name fields, you should choose names containing only alpha-numeric values, as
      symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a
      pipeline should prefix their name with the string "my".

    - **values** *(list) --*

      The value that the actual field value will be compared with.

      - *(string) --*
    """


_QueryObjectsPaginatequeryselectorsTypeDef = TypedDict(
    "_QueryObjectsPaginatequeryselectorsTypeDef",
    {"fieldName": str, "operator": QueryObjectsPaginatequeryselectorsoperatorTypeDef},
    total=False,
)


class QueryObjectsPaginatequeryselectorsTypeDef(
    _QueryObjectsPaginatequeryselectorsTypeDef
):
    """
    Type definition for `QueryObjectsPaginatequery` `selectors`

    A comparision that is used to determine whether a query should return this object.

    - **fieldName** *(string) --*

      The name of the field that the operator will be applied to. The field name is the "key"
      portion of the field definition in the pipeline definition syntax that is used by the AWS
      Data Pipeline API. If the field is not set on the object, the condition fails.

    - **operator** *(dict) --*

      Contains a logical operation for comparing the value of a field with a specified value.

      - **type** *(string) --*

        The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ),
        less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ).
        Equal reference (``REF_EQ`` ) can be used only with reference fields. The other
        comparison types can be used only with String fields. The comparison types you can use
        apply only to certain object fields, as detailed below.

        The comparison operators EQ and REF_EQ act on the following fields:

        * name

        * @sphere

        * parent

        * @componentParent

        * @instanceParent

        * @status

        * @scheduledStartTime

        * @scheduledEndTime

        * @actualStartTime

        * @actualEndTime

        The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields:

        * @scheduledStartTime

        * @scheduledEndTime

        * @actualStartTime

        * @actualEndTime

        Note that fields beginning with the at sign (@) are read-only and set by the web service.
        When you name fields, you should choose names containing only alpha-numeric values, as
        symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a
        pipeline should prefix their name with the string "my".

      - **values** *(list) --*

        The value that the actual field value will be compared with.

        - *(string) --*
    """


_QueryObjectsPaginatequeryTypeDef = TypedDict(
    "_QueryObjectsPaginatequeryTypeDef",
    {"selectors": List[QueryObjectsPaginatequeryselectorsTypeDef]},
    total=False,
)


class QueryObjectsPaginatequeryTypeDef(_QueryObjectsPaginatequeryTypeDef):
    """
    Type definition for `QueryObjectsPaginate` `query`

    The query that defines the objects to be returned. The ``Query`` object can contain a maximum of
    ten selectors. The conditions in the query are limited to top-level String fields in the object.
    These filters can be applied to components, instances, and attempts.

    - **selectors** *(list) --*

      List of selectors that define the query. An object must satisfy all of the selectors to match
      the query.

      - *(dict) --*

        A comparision that is used to determine whether a query should return this object.

        - **fieldName** *(string) --*

          The name of the field that the operator will be applied to. The field name is the "key"
          portion of the field definition in the pipeline definition syntax that is used by the AWS
          Data Pipeline API. If the field is not set on the object, the condition fails.

        - **operator** *(dict) --*

          Contains a logical operation for comparing the value of a field with a specified value.

          - **type** *(string) --*

            The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ),
            less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ).
            Equal reference (``REF_EQ`` ) can be used only with reference fields. The other
            comparison types can be used only with String fields. The comparison types you can use
            apply only to certain object fields, as detailed below.

            The comparison operators EQ and REF_EQ act on the following fields:

            * name

            * @sphere

            * parent

            * @componentParent

            * @instanceParent

            * @status

            * @scheduledStartTime

            * @scheduledEndTime

            * @actualStartTime

            * @actualEndTime

            The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields:

            * @scheduledStartTime

            * @scheduledEndTime

            * @actualStartTime

            * @actualEndTime

            Note that fields beginning with the at sign (@) are read-only and set by the web service.
            When you name fields, you should choose names containing only alpha-numeric values, as
            symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a
            pipeline should prefix their name with the string "my".

          - **values** *(list) --*

            The value that the actual field value will be compared with.

            - *(string) --*
    """
