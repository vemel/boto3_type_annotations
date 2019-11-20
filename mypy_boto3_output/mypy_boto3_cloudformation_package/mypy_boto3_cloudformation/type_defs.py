"Main interface for cloudformation type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ChangeSetCreateCompleteWaitWaiterConfigTypeDef",
    "ClientCreateChangeSetParametersTypeDef",
    "ClientCreateChangeSetResourcesToImportTypeDef",
    "ClientCreateChangeSetResponseTypeDef",
    "ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    "ClientCreateChangeSetRollbackConfigurationTypeDef",
    "ClientCreateChangeSetTagsTypeDef",
    "ClientCreateStackInstancesOperationPreferencesTypeDef",
    "ClientCreateStackInstancesParameterOverridesTypeDef",
    "ClientCreateStackInstancesResponseTypeDef",
    "ClientCreateStackParametersTypeDef",
    "ClientCreateStackResponseTypeDef",
    "ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    "ClientCreateStackRollbackConfigurationTypeDef",
    "ClientCreateStackSetParametersTypeDef",
    "ClientCreateStackSetResponseTypeDef",
    "ClientCreateStackSetTagsTypeDef",
    "ClientCreateStackTagsTypeDef",
    "ClientDeleteStackInstancesOperationPreferencesTypeDef",
    "ClientDeleteStackInstancesResponseTypeDef",
    "ClientDescribeAccountLimitsResponseAccountLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeTypeDef",
    "ClientDescribeChangeSetResponseChangesTypeDef",
    "ClientDescribeChangeSetResponseParametersTypeDef",
    "ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef",
    "ClientDescribeChangeSetResponseRollbackConfigurationTypeDef",
    "ClientDescribeChangeSetResponseTagsTypeDef",
    "ClientDescribeChangeSetResponseTypeDef",
    "ClientDescribeStackDriftDetectionStatusResponseTypeDef",
    "ClientDescribeStackEventsResponseStackEventsTypeDef",
    "ClientDescribeStackEventsResponseTypeDef",
    "ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef",
    "ClientDescribeStackInstanceResponseStackInstanceTypeDef",
    "ClientDescribeStackInstanceResponseTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef",
    "ClientDescribeStackResourceDriftsResponseTypeDef",
    "ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef",
    "ClientDescribeStackResourceResponseStackResourceDetailTypeDef",
    "ClientDescribeStackResourceResponseTypeDef",
    "ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef",
    "ClientDescribeStackResourcesResponseStackResourcesTypeDef",
    "ClientDescribeStackResourcesResponseTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationTypeDef",
    "ClientDescribeStackSetOperationResponseTypeDef",
    "ClientDescribeStacksResponseStacksDriftInformationTypeDef",
    "ClientDescribeStacksResponseStacksOutputsTypeDef",
    "ClientDescribeStacksResponseStacksParametersTypeDef",
    "ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    "ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef",
    "ClientDescribeStacksResponseStacksTagsTypeDef",
    "ClientDescribeStacksResponseStacksTypeDef",
    "ClientDescribeStacksResponseTypeDef",
    "ClientDescribeTypeRegistrationResponseTypeDef",
    "ClientDescribeTypeResponseLoggingConfigTypeDef",
    "ClientDescribeTypeResponseTypeDef",
    "ClientDetectStackDriftResponseTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef",
    "ClientDetectStackResourceDriftResponseTypeDef",
    "ClientDetectStackSetDriftOperationPreferencesTypeDef",
    "ClientDetectStackSetDriftResponseTypeDef",
    "ClientEstimateTemplateCostParametersTypeDef",
    "ClientEstimateTemplateCostResponseTypeDef",
    "ClientGetStackPolicyResponseTypeDef",
    "ClientGetTemplateResponseTypeDef",
    "ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef",
    "ClientGetTemplateSummaryResponseParametersTypeDef",
    "ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef",
    "ClientGetTemplateSummaryResponseTypeDef",
    "ClientListChangeSetsResponseSummariesTypeDef",
    "ClientListChangeSetsResponseTypeDef",
    "ClientListExportsResponseExportsTypeDef",
    "ClientListExportsResponseTypeDef",
    "ClientListImportsResponseTypeDef",
    "ClientListStackInstancesResponseSummariesTypeDef",
    "ClientListStackInstancesResponseTypeDef",
    "ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef",
    "ClientListStackResourcesResponseStackResourceSummariesTypeDef",
    "ClientListStackResourcesResponseTypeDef",
    "ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef",
    "ClientListStackSetOperationResultsResponseSummariesTypeDef",
    "ClientListStackSetOperationResultsResponseTypeDef",
    "ClientListStackSetOperationsResponseSummariesTypeDef",
    "ClientListStackSetOperationsResponseTypeDef",
    "ClientListStackSetsResponseSummariesTypeDef",
    "ClientListStackSetsResponseTypeDef",
    "ClientListStacksResponseStackSummariesDriftInformationTypeDef",
    "ClientListStacksResponseStackSummariesTypeDef",
    "ClientListStacksResponseTypeDef",
    "ClientListTypeRegistrationsResponseTypeDef",
    "ClientListTypeVersionsResponseTypeVersionSummariesTypeDef",
    "ClientListTypeVersionsResponseTypeDef",
    "ClientListTypesResponseTypeSummariesTypeDef",
    "ClientListTypesResponseTypeDef",
    "ClientRegisterTypeLoggingConfigTypeDef",
    "ClientRegisterTypeResponseTypeDef",
    "ClientUpdateStackInstancesOperationPreferencesTypeDef",
    "ClientUpdateStackInstancesParameterOverridesTypeDef",
    "ClientUpdateStackInstancesResponseTypeDef",
    "ClientUpdateStackParametersTypeDef",
    "ClientUpdateStackResponseTypeDef",
    "ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef",
    "ClientUpdateStackRollbackConfigurationTypeDef",
    "ClientUpdateStackSetOperationPreferencesTypeDef",
    "ClientUpdateStackSetParametersTypeDef",
    "ClientUpdateStackSetResponseTypeDef",
    "ClientUpdateStackSetTagsTypeDef",
    "ClientUpdateStackTagsTypeDef",
    "ClientUpdateTerminationProtectionResponseTypeDef",
    "ClientValidateTemplateResponseParametersTypeDef",
    "ClientValidateTemplateResponseTypeDef",
    "DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    "DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef",
    "DescribeAccountLimitsPaginateResponseTypeDef",
    "DescribeChangeSetPaginatePaginationConfigTypeDef",
    "DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef",
    "DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef",
    "DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef",
    "DescribeChangeSetPaginateResponseChangesTypeDef",
    "DescribeChangeSetPaginateResponseParametersTypeDef",
    "DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef",
    "DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef",
    "DescribeChangeSetPaginateResponseTagsTypeDef",
    "DescribeChangeSetPaginateResponseTypeDef",
    "DescribeStackEventsPaginatePaginationConfigTypeDef",
    "DescribeStackEventsPaginateResponseStackEventsTypeDef",
    "DescribeStackEventsPaginateResponseTypeDef",
    "DescribeStacksPaginatePaginationConfigTypeDef",
    "DescribeStacksPaginateResponseStacksDriftInformationTypeDef",
    "DescribeStacksPaginateResponseStacksOutputsTypeDef",
    "DescribeStacksPaginateResponseStacksParametersTypeDef",
    "DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    "DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef",
    "DescribeStacksPaginateResponseStacksTagsTypeDef",
    "DescribeStacksPaginateResponseStacksTypeDef",
    "DescribeStacksPaginateResponseTypeDef",
    "ListChangeSetsPaginatePaginationConfigTypeDef",
    "ListChangeSetsPaginateResponseSummariesTypeDef",
    "ListChangeSetsPaginateResponseTypeDef",
    "ListExportsPaginatePaginationConfigTypeDef",
    "ListExportsPaginateResponseExportsTypeDef",
    "ListExportsPaginateResponseTypeDef",
    "ListImportsPaginatePaginationConfigTypeDef",
    "ListImportsPaginateResponseTypeDef",
    "ListStackInstancesPaginatePaginationConfigTypeDef",
    "ListStackInstancesPaginateResponseSummariesTypeDef",
    "ListStackInstancesPaginateResponseTypeDef",
    "ListStackResourcesPaginatePaginationConfigTypeDef",
    "ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef",
    "ListStackResourcesPaginateResponseStackResourceSummariesTypeDef",
    "ListStackResourcesPaginateResponseTypeDef",
    "ListStackSetOperationResultsPaginatePaginationConfigTypeDef",
    "ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef",
    "ListStackSetOperationResultsPaginateResponseSummariesTypeDef",
    "ListStackSetOperationResultsPaginateResponseTypeDef",
    "ListStackSetOperationsPaginatePaginationConfigTypeDef",
    "ListStackSetOperationsPaginateResponseSummariesTypeDef",
    "ListStackSetOperationsPaginateResponseTypeDef",
    "ListStackSetsPaginatePaginationConfigTypeDef",
    "ListStackSetsPaginateResponseSummariesTypeDef",
    "ListStackSetsPaginateResponseTypeDef",
    "ListStacksPaginatePaginationConfigTypeDef",
    "ListStacksPaginateResponseStackSummariesDriftInformationTypeDef",
    "ListStacksPaginateResponseStackSummariesTypeDef",
    "ListStacksPaginateResponseTypeDef",
    "ServiceResourceCreateStackParametersTypeDef",
    "ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    "ServiceResourceCreateStackRollbackConfigurationTypeDef",
    "ServiceResourceCreateStackTagsTypeDef",
    "StackCreateCompleteWaitWaiterConfigTypeDef",
    "StackDeleteCompleteWaitWaiterConfigTypeDef",
    "StackExistsWaitWaiterConfigTypeDef",
    "StackImportCompleteWaitWaiterConfigTypeDef",
    "StackUpdateCompleteWaitWaiterConfigTypeDef",
    "StackUpdateParametersTypeDef",
    "StackUpdateResponseTypeDef",
    "StackUpdateRollbackConfigurationRollbackTriggersTypeDef",
    "StackUpdateRollbackConfigurationTypeDef",
    "StackUpdateTagsTypeDef",
    "TypeRegistrationCompleteWaitWaiterConfigTypeDef",
)


_ChangeSetCreateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_ChangeSetCreateCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ChangeSetCreateCompleteWaitWaiterConfigTypeDef(
    _ChangeSetCreateCompleteWaitWaiterConfigTypeDef
):
    """
    Type definition for `ChangeSetCreateCompleteWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 120
    """


_ClientCreateChangeSetParametersTypeDef = TypedDict(
    "_ClientCreateChangeSetParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientCreateChangeSetParametersTypeDef(_ClientCreateChangeSetParametersTypeDef):
    """
    Type definition for `ClientCreateChangeSet` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientCreateChangeSetResourcesToImportTypeDef = TypedDict(
    "_ClientCreateChangeSetResourcesToImportTypeDef",
    {
        "ResourceType": str,
        "LogicalResourceId": str,
        "ResourceIdentifier": Dict[str, str],
    },
)


class ClientCreateChangeSetResourcesToImportTypeDef(
    _ClientCreateChangeSetResourcesToImportTypeDef
):
    """
    Type definition for `ClientCreateChangeSet` `ResourcesToImport`

    Describes the target resource of an import operation.

    - **ResourceType** *(string) --* **[REQUIRED]**

      The type of resource to import into your stack, such as ``AWS::S3::Bucket`` .

    - **LogicalResourceId** *(string) --* **[REQUIRED]**

      The logical ID of the target resource as specified in the template.

    - **ResourceIdentifier** *(dict) --* **[REQUIRED]**

      A key-value pair that identifies the target resource. The key is an identifier property (for
      example, ``BucketName`` for ``AWS::S3::Bucket`` resources) and the value is the actual
      property value (for example, ``MyS3Bucket`` ).

      - *(string) --*

        - *(string) --*
    """


_ClientCreateChangeSetResponseTypeDef = TypedDict(
    "_ClientCreateChangeSetResponseTypeDef", {"Id": str, "StackId": str}, total=False
)


class ClientCreateChangeSetResponseTypeDef(_ClientCreateChangeSetResponseTypeDef):
    """
    Type definition for `ClientCreateChangeSet` `Response`

    The output for the  CreateChangeSet action.

    - **Id** *(string) --*

      The Amazon Resource Name (ARN) of the change set.

    - **StackId** *(string) --*

      The unique ID of the stack.
    """


_ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
)


class ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef(
    _ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `ClientCreateChangeSetRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
    of the alarms you specify goes to ALARM state during the stack operation or within the
    specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

    - **Arn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

    - **Type** *(string) --* **[REQUIRED]**

      The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_ClientCreateChangeSetRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateChangeSetRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientCreateChangeSetRollbackConfigurationTypeDef(
    _ClientCreateChangeSetRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientCreateChangeSet` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you do
      specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
        of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

        - **Arn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - **Type** *(string) --* **[REQUIRED]**

          The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the rollback
      triggers after the stack creation or update operation deploys all necessary resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
      still waits the specified period of time before cleaning up old resources after update
      operations. You can use this monitoring period to perform any manual stack validation desired,
      and manually cancel the stack creation or update (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
      triggers during stack creation and update operations. Then, for update operations, it begins
      disposing of old resources immediately once the operation completes.
    """


_ClientCreateChangeSetTagsTypeDef = TypedDict(
    "_ClientCreateChangeSetTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateChangeSetTagsTypeDef(_ClientCreateChangeSetTagsTypeDef):
    """
    Type definition for `ClientCreateChangeSet` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --* **[REQUIRED]**

       *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
       for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

       *Required* . A string containing the value for this tag. You can specify a maximum of 256
       characters for a tag value.
    """


_ClientCreateStackInstancesOperationPreferencesTypeDef = TypedDict(
    "_ClientCreateStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientCreateStackInstancesOperationPreferencesTypeDef(
    _ClientCreateStackInstancesOperationPreferencesTypeDef
):
    """
    Type definition for `ClientCreateStackInstances` `OperationPreferences`

    Preferences for how AWS CloudFormation performs this stack set operation.

    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.

      - *(string) --*

    - **FailureToleranceCount** *(integer) --*

      The number of accounts, per region, for which this operation can fail before AWS CloudFormation
      stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation
      doesn't attempt the operation in any subsequent regions.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` (but not both).

    - **FailureTolerancePercentage** *(integer) --*

      The percentage of accounts, per region, for which this stack operation can fail before AWS
      CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS
      CloudFormation doesn't attempt the operation in any subsequent regions.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds *down* to the next whole number.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` , but not both.

    - **MaxConcurrentCount** *(integer) --*

      The maximum number of accounts in which to perform this operation at one time. This is
      dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more
      than the ``FailureToleranceCount`` .

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.

    - **MaxConcurrentPercentage** *(integer) --*

      The maximum percentage of accounts in which to perform this operation at one time.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds down to the next whole number. This is true except in cases where rounding down would
      result is zero. In this case, CloudFormation sets the number as one instead.

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.
    """


_ClientCreateStackInstancesParameterOverridesTypeDef = TypedDict(
    "_ClientCreateStackInstancesParameterOverridesTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientCreateStackInstancesParameterOverridesTypeDef(
    _ClientCreateStackInstancesParameterOverridesTypeDef
):
    """
    Type definition for `ClientCreateStackInstances` `ParameterOverrides`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientCreateStackInstancesResponseTypeDef = TypedDict(
    "_ClientCreateStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)


class ClientCreateStackInstancesResponseTypeDef(
    _ClientCreateStackInstancesResponseTypeDef
):
    """
    Type definition for `ClientCreateStackInstances` `Response`

    - **OperationId** *(string) --*

      The unique identifier for this stack set operation.
    """


_ClientCreateStackParametersTypeDef = TypedDict(
    "_ClientCreateStackParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientCreateStackParametersTypeDef(_ClientCreateStackParametersTypeDef):
    """
    Type definition for `ClientCreateStack` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientCreateStackResponseTypeDef = TypedDict(
    "_ClientCreateStackResponseTypeDef", {"StackId": str}, total=False
)


class ClientCreateStackResponseTypeDef(_ClientCreateStackResponseTypeDef):
    """
    Type definition for `ClientCreateStack` `Response`

    The output for a  CreateStack action.

    - **StackId** *(string) --*

      Unique identifier of the stack.
    """


_ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
)


class ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef(
    _ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `ClientCreateStackRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
    of the alarms you specify goes to ALARM state during the stack operation or within the
    specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

    - **Arn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

    - **Type** *(string) --* **[REQUIRED]**

      The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_ClientCreateStackRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientCreateStackRollbackConfigurationTypeDef(
    _ClientCreateStackRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientCreateStack` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you do
      specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
        of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

        - **Arn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - **Type** *(string) --* **[REQUIRED]**

          The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the rollback
      triggers after the stack creation or update operation deploys all necessary resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
      still waits the specified period of time before cleaning up old resources after update
      operations. You can use this monitoring period to perform any manual stack validation desired,
      and manually cancel the stack creation or update (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
      triggers during stack creation and update operations. Then, for update operations, it begins
      disposing of old resources immediately once the operation completes.
    """


_ClientCreateStackSetParametersTypeDef = TypedDict(
    "_ClientCreateStackSetParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientCreateStackSetParametersTypeDef(_ClientCreateStackSetParametersTypeDef):
    """
    Type definition for `ClientCreateStackSet` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientCreateStackSetResponseTypeDef = TypedDict(
    "_ClientCreateStackSetResponseTypeDef", {"StackSetId": str}, total=False
)


class ClientCreateStackSetResponseTypeDef(_ClientCreateStackSetResponseTypeDef):
    """
    Type definition for `ClientCreateStackSet` `Response`

    - **StackSetId** *(string) --*

      The ID of the stack set that you're creating.
    """


_ClientCreateStackSetTagsTypeDef = TypedDict(
    "_ClientCreateStackSetTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateStackSetTagsTypeDef(_ClientCreateStackSetTagsTypeDef):
    """
    Type definition for `ClientCreateStackSet` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --* **[REQUIRED]**

       *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
       for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

       *Required* . A string containing the value for this tag. You can specify a maximum of 256
       characters for a tag value.
    """


_ClientCreateStackTagsTypeDef = TypedDict(
    "_ClientCreateStackTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateStackTagsTypeDef(_ClientCreateStackTagsTypeDef):
    """
    Type definition for `ClientCreateStack` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --* **[REQUIRED]**

       *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
       for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

       *Required* . A string containing the value for this tag. You can specify a maximum of 256
       characters for a tag value.
    """


_ClientDeleteStackInstancesOperationPreferencesTypeDef = TypedDict(
    "_ClientDeleteStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientDeleteStackInstancesOperationPreferencesTypeDef(
    _ClientDeleteStackInstancesOperationPreferencesTypeDef
):
    """
    Type definition for `ClientDeleteStackInstances` `OperationPreferences`

    Preferences for how AWS CloudFormation performs this stack set operation.

    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.

      - *(string) --*

    - **FailureToleranceCount** *(integer) --*

      The number of accounts, per region, for which this operation can fail before AWS CloudFormation
      stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation
      doesn't attempt the operation in any subsequent regions.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` (but not both).

    - **FailureTolerancePercentage** *(integer) --*

      The percentage of accounts, per region, for which this stack operation can fail before AWS
      CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS
      CloudFormation doesn't attempt the operation in any subsequent regions.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds *down* to the next whole number.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` , but not both.

    - **MaxConcurrentCount** *(integer) --*

      The maximum number of accounts in which to perform this operation at one time. This is
      dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more
      than the ``FailureToleranceCount`` .

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.

    - **MaxConcurrentPercentage** *(integer) --*

      The maximum percentage of accounts in which to perform this operation at one time.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds down to the next whole number. This is true except in cases where rounding down would
      result is zero. In this case, CloudFormation sets the number as one instead.

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.
    """


_ClientDeleteStackInstancesResponseTypeDef = TypedDict(
    "_ClientDeleteStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDeleteStackInstancesResponseTypeDef(
    _ClientDeleteStackInstancesResponseTypeDef
):
    """
    Type definition for `ClientDeleteStackInstances` `Response`

    - **OperationId** *(string) --*

      The unique identifier for this stack set operation.
    """


_ClientDescribeAccountLimitsResponseAccountLimitsTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseAccountLimitsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)


class ClientDescribeAccountLimitsResponseAccountLimitsTypeDef(
    _ClientDescribeAccountLimitsResponseAccountLimitsTypeDef
):
    """
    Type definition for `ClientDescribeAccountLimitsResponse` `AccountLimits`

    The AccountLimit data type.

    CloudFormation has the following limits per account:

    * Number of concurrent resources

    * Number of stacks

    * Number of stack outputs

    For more information about these account limits, and other CloudFormation limits, see `AWS
    CloudFormation Limits
    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
    in the *AWS CloudFormation User Guide* .

    - **Name** *(string) --*

      The name of the account limit.

      Values: ``ConcurrentResourcesLimit`` | ``StackLimit`` | ``StackOutputsLimit``

    - **Value** *(integer) --*

      The value that is associated with the account limit name.
    """


_ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseTypeDef",
    {
        "AccountLimits": List[ClientDescribeAccountLimitsResponseAccountLimitsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAccountLimitsResponseTypeDef(
    _ClientDescribeAccountLimitsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccountLimits` `Response`

    The output for the  DescribeAccountLimits action.

    - **AccountLimits** *(list) --*

      An account limit structure that contain a list of AWS CloudFormation account limits and their
      values.

      - *(dict) --*

        The AccountLimit data type.

        CloudFormation has the following limits per account:

        * Number of concurrent resources

        * Number of stacks

        * Number of stack outputs

        For more information about these account limits, and other CloudFormation limits, see `AWS
        CloudFormation Limits
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
        in the *AWS CloudFormation User Guide* .

        - **Name** *(string) --*

          The name of the account limit.

          Values: ``ConcurrentResourcesLimit`` | ``StackLimit`` | ``StackOutputsLimit``

        - **Value** *(integer) --*

          The value that is associated with the account limit name.

    - **NextToken** *(string) --*

      If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no
      additional page exists, this value is null.
    """


_ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef",
    {"Attribute": str, "Name": str, "RequiresRecreation": str},
    total=False,
)


class ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef(
    _ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef
):
    """
    Type definition for `ClientDescribeChangeSetResponseChangesResourceChangeDetails` `Target`

    A ``ResourceTargetDefinition`` structure that describes the field that AWS
    CloudFormation will change and whether the resource will be recreated.

    - **Attribute** *(string) --*

      Indicates which resource attribute is triggering this update, such as a change in
      the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

    - **Name** *(string) --*

      If the ``Attribute`` value is ``Properties`` , the name of the property. For all
      other attributes, the value is null.

    - **RequiresRecreation** *(string) --*

      If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
      property causes the resource to be recreated. The value can be ``Never`` ,
      ``Always`` , or ``Conditionally`` . To determine the conditions for a
      ``Conditionally`` recreation, see the update behavior for that `property
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
      in the AWS CloudFormation User Guide.
    """


_ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef",
    {
        "Target": ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef,
        "Evaluation": str,
        "ChangeSource": str,
        "CausingEntity": str,
    },
    total=False,
)


class ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef(
    _ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef
):
    """
    Type definition for `ClientDescribeChangeSetResponseChangesResourceChange` `Details`

    For a resource with ``Modify`` as the action, the ``ResourceChange`` structure
    describes the changes AWS CloudFormation will make to that resource.

    - **Target** *(dict) --*

      A ``ResourceTargetDefinition`` structure that describes the field that AWS
      CloudFormation will change and whether the resource will be recreated.

      - **Attribute** *(string) --*

        Indicates which resource attribute is triggering this update, such as a change in
        the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

      - **Name** *(string) --*

        If the ``Attribute`` value is ``Properties`` , the name of the property. For all
        other attributes, the value is null.

      - **RequiresRecreation** *(string) --*

        If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
        property causes the resource to be recreated. The value can be ``Never`` ,
        ``Always`` , or ``Conditionally`` . To determine the conditions for a
        ``Conditionally`` recreation, see the update behavior for that `property
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
        in the AWS CloudFormation User Guide.

    - **Evaluation** *(string) --*

      Indicates whether AWS CloudFormation can determine the target value, and whether
      the target value will change before you execute a change set.

      For ``Static`` evaluations, AWS CloudFormation can determine that the target value
      will change, and its value. For example, if you directly modify the
      ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this
      property value will change, and its value, so this is a ``Static`` evaluation.

      For ``Dynamic`` evaluations, cannot determine the target value because it depends
      on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt``
      intrinsic function, when the stack is updated. For example, if your template
      includes a reference to a resource that is conditionally recreated, the value of
      the reference (the physical ID of the resource) might change, depending on if the
      resource is recreated. If the resource is recreated, it will have a new physical
      ID, so all references to that resource will also be updated.

    - **ChangeSource** *(string) --*

      The group to which the ``CausingEntity`` value belongs. There are five entity
      groups:

      * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to
      resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` .

      * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template
      parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` .

      * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get
      resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource",
      "PublicDnsName" ] }`` .

      * ``DirectModification`` entities are changes that are made directly to the
      template.

      * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which
      are also known as nested stacks. If you made no changes to the
      ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the
      ``ChangeSource`` to ``Automatic`` because the nested stack's template might have
      changed. Changes to a nested stack's template aren't visible to AWS CloudFormation
      until you run an update on the parent stack.

    - **CausingEntity** *(string) --*

      The identity of the entity that triggered this change. This entity is a member of
      the group that is specified by the ``ChangeSource`` field. For example, if you
      modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the
      name of the parameter (``KeyPairName`` ).

      If the ``ChangeSource`` value is ``DirectModification`` , no value is given for
      ``CausingEntity`` .
    """


_ClientDescribeChangeSetResponseChangesResourceChangeTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseChangesResourceChangeTypeDef",
    {
        "Action": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": str,
        "Scope": List[str],
        "Details": List[
            ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeChangeSetResponseChangesResourceChangeTypeDef(
    _ClientDescribeChangeSetResponseChangesResourceChangeTypeDef
):
    """
    Type definition for `ClientDescribeChangeSetResponseChanges` `ResourceChange`

    A ``ResourceChange`` structure that describes the resource and action that AWS
    CloudFormation will perform.

    - **Action** *(string) --*

      The action that AWS CloudFormation takes on the resource, such as ``Add`` (adds a new
      resource), ``Modify`` (changes a resource), or ``Remove`` (deletes a resource).

    - **LogicalResourceId** *(string) --*

      The resource's logical ID, which is defined in the stack's template.

    - **PhysicalResourceId** *(string) --*

      The resource's physical ID (resource name). Resources that you are adding don't have
      physical IDs because they haven't been created.

    - **ResourceType** *(string) --*

      The type of AWS CloudFormation resource, such as ``AWS::S3::Bucket`` .

    - **Replacement** *(string) --*

      For the ``Modify`` action, indicates whether AWS CloudFormation will replace the
      resource by creating a new one and deleting the old one. This value depends on the
      value of the ``RequiresRecreation`` property in the ``ResourceTargetDefinition``
      structure. For example, if the ``RequiresRecreation`` field is ``Always`` and the
      ``Evaluation`` field is ``Static`` , ``Replacement`` is ``True`` . If the
      ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Dynamic``
      , ``Replacement`` is ``Conditionally`` .

      If you have multiple changes with different ``RequiresRecreation`` values, the
      ``Replacement`` value depends on the change with the most impact. A
      ``RequiresRecreation`` value of ``Always`` has the most impact, followed by
      ``Conditionally`` , and then ``Never`` .

    - **Scope** *(list) --*

      For the ``Modify`` action, indicates which resource attribute is triggering this
      update, such as a change in the resource attribute's ``Metadata`` , ``Properties`` , or
      ``Tags`` .

      - *(string) --*

    - **Details** *(list) --*

      For the ``Modify`` action, a list of ``ResourceChangeDetail`` structures that describes
      the changes that AWS CloudFormation will make to the resource.

      - *(dict) --*

        For a resource with ``Modify`` as the action, the ``ResourceChange`` structure
        describes the changes AWS CloudFormation will make to that resource.

        - **Target** *(dict) --*

          A ``ResourceTargetDefinition`` structure that describes the field that AWS
          CloudFormation will change and whether the resource will be recreated.

          - **Attribute** *(string) --*

            Indicates which resource attribute is triggering this update, such as a change in
            the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

          - **Name** *(string) --*

            If the ``Attribute`` value is ``Properties`` , the name of the property. For all
            other attributes, the value is null.

          - **RequiresRecreation** *(string) --*

            If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
            property causes the resource to be recreated. The value can be ``Never`` ,
            ``Always`` , or ``Conditionally`` . To determine the conditions for a
            ``Conditionally`` recreation, see the update behavior for that `property
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
            in the AWS CloudFormation User Guide.

        - **Evaluation** *(string) --*

          Indicates whether AWS CloudFormation can determine the target value, and whether
          the target value will change before you execute a change set.

          For ``Static`` evaluations, AWS CloudFormation can determine that the target value
          will change, and its value. For example, if you directly modify the
          ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this
          property value will change, and its value, so this is a ``Static`` evaluation.

          For ``Dynamic`` evaluations, cannot determine the target value because it depends
          on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt``
          intrinsic function, when the stack is updated. For example, if your template
          includes a reference to a resource that is conditionally recreated, the value of
          the reference (the physical ID of the resource) might change, depending on if the
          resource is recreated. If the resource is recreated, it will have a new physical
          ID, so all references to that resource will also be updated.

        - **ChangeSource** *(string) --*

          The group to which the ``CausingEntity`` value belongs. There are five entity
          groups:

          * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to
          resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` .

          * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template
          parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` .

          * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get
          resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource",
          "PublicDnsName" ] }`` .

          * ``DirectModification`` entities are changes that are made directly to the
          template.

          * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which
          are also known as nested stacks. If you made no changes to the
          ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the
          ``ChangeSource`` to ``Automatic`` because the nested stack's template might have
          changed. Changes to a nested stack's template aren't visible to AWS CloudFormation
          until you run an update on the parent stack.

        - **CausingEntity** *(string) --*

          The identity of the entity that triggered this change. This entity is a member of
          the group that is specified by the ``ChangeSource`` field. For example, if you
          modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the
          name of the parameter (``KeyPairName`` ).

          If the ``ChangeSource`` value is ``DirectModification`` , no value is given for
          ``CausingEntity`` .
    """


_ClientDescribeChangeSetResponseChangesTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseChangesTypeDef",
    {
        "Type": str,
        "ResourceChange": ClientDescribeChangeSetResponseChangesResourceChangeTypeDef,
    },
    total=False,
)


class ClientDescribeChangeSetResponseChangesTypeDef(
    _ClientDescribeChangeSetResponseChangesTypeDef
):
    """
    Type definition for `ClientDescribeChangeSetResponse` `Changes`

    The ``Change`` structure describes the changes AWS CloudFormation will perform if you
    execute the change set.

    - **Type** *(string) --*

      The type of entity that AWS CloudFormation changes. Currently, the only entity type is
      ``Resource`` .

    - **ResourceChange** *(dict) --*

      A ``ResourceChange`` structure that describes the resource and action that AWS
      CloudFormation will perform.

      - **Action** *(string) --*

        The action that AWS CloudFormation takes on the resource, such as ``Add`` (adds a new
        resource), ``Modify`` (changes a resource), or ``Remove`` (deletes a resource).

      - **LogicalResourceId** *(string) --*

        The resource's logical ID, which is defined in the stack's template.

      - **PhysicalResourceId** *(string) --*

        The resource's physical ID (resource name). Resources that you are adding don't have
        physical IDs because they haven't been created.

      - **ResourceType** *(string) --*

        The type of AWS CloudFormation resource, such as ``AWS::S3::Bucket`` .

      - **Replacement** *(string) --*

        For the ``Modify`` action, indicates whether AWS CloudFormation will replace the
        resource by creating a new one and deleting the old one. This value depends on the
        value of the ``RequiresRecreation`` property in the ``ResourceTargetDefinition``
        structure. For example, if the ``RequiresRecreation`` field is ``Always`` and the
        ``Evaluation`` field is ``Static`` , ``Replacement`` is ``True`` . If the
        ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Dynamic``
        , ``Replacement`` is ``Conditionally`` .

        If you have multiple changes with different ``RequiresRecreation`` values, the
        ``Replacement`` value depends on the change with the most impact. A
        ``RequiresRecreation`` value of ``Always`` has the most impact, followed by
        ``Conditionally`` , and then ``Never`` .

      - **Scope** *(list) --*

        For the ``Modify`` action, indicates which resource attribute is triggering this
        update, such as a change in the resource attribute's ``Metadata`` , ``Properties`` , or
        ``Tags`` .

        - *(string) --*

      - **Details** *(list) --*

        For the ``Modify`` action, a list of ``ResourceChangeDetail`` structures that describes
        the changes that AWS CloudFormation will make to the resource.

        - *(dict) --*

          For a resource with ``Modify`` as the action, the ``ResourceChange`` structure
          describes the changes AWS CloudFormation will make to that resource.

          - **Target** *(dict) --*

            A ``ResourceTargetDefinition`` structure that describes the field that AWS
            CloudFormation will change and whether the resource will be recreated.

            - **Attribute** *(string) --*

              Indicates which resource attribute is triggering this update, such as a change in
              the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

            - **Name** *(string) --*

              If the ``Attribute`` value is ``Properties`` , the name of the property. For all
              other attributes, the value is null.

            - **RequiresRecreation** *(string) --*

              If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
              property causes the resource to be recreated. The value can be ``Never`` ,
              ``Always`` , or ``Conditionally`` . To determine the conditions for a
              ``Conditionally`` recreation, see the update behavior for that `property
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
              in the AWS CloudFormation User Guide.

          - **Evaluation** *(string) --*

            Indicates whether AWS CloudFormation can determine the target value, and whether
            the target value will change before you execute a change set.

            For ``Static`` evaluations, AWS CloudFormation can determine that the target value
            will change, and its value. For example, if you directly modify the
            ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this
            property value will change, and its value, so this is a ``Static`` evaluation.

            For ``Dynamic`` evaluations, cannot determine the target value because it depends
            on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt``
            intrinsic function, when the stack is updated. For example, if your template
            includes a reference to a resource that is conditionally recreated, the value of
            the reference (the physical ID of the resource) might change, depending on if the
            resource is recreated. If the resource is recreated, it will have a new physical
            ID, so all references to that resource will also be updated.

          - **ChangeSource** *(string) --*

            The group to which the ``CausingEntity`` value belongs. There are five entity
            groups:

            * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to
            resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` .

            * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template
            parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` .

            * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get
            resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource",
            "PublicDnsName" ] }`` .

            * ``DirectModification`` entities are changes that are made directly to the
            template.

            * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which
            are also known as nested stacks. If you made no changes to the
            ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the
            ``ChangeSource`` to ``Automatic`` because the nested stack's template might have
            changed. Changes to a nested stack's template aren't visible to AWS CloudFormation
            until you run an update on the parent stack.

          - **CausingEntity** *(string) --*

            The identity of the entity that triggered this change. This entity is a member of
            the group that is specified by the ``ChangeSource`` field. For example, if you
            modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the
            name of the parameter (``KeyPairName`` ).

            If the ``ChangeSource`` value is ``DirectModification`` , no value is given for
            ``CausingEntity`` .
    """


_ClientDescribeChangeSetResponseParametersTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientDescribeChangeSetResponseParametersTypeDef(
    _ClientDescribeChangeSetResponseParametersTypeDef
):
    """
    Type definition for `ClientDescribeChangeSetResponse` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a
      particular parameter, AWS CloudFormation uses the default value that is specified in your
      template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a
      given parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef(
    _ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `ClientDescribeChangeSetResponseRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
    any of the alarms you specify goes to ALARM state during the stack operation or within
    the specified monitoring period afterwards, CloudFormation rolls back the entire stack
    operation.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

    - **Type** *(string) --*

      The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_ClientDescribeChangeSetResponseRollbackConfigurationTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientDescribeChangeSetResponseRollbackConfigurationTypeDef(
    _ClientDescribeChangeSetResponseRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeChangeSetResponse` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and
      applies them to any subsequent update operations for the stack, unless you specify
      otherwise. If you do specify rollback triggers for this parameter, those triggers replace
      any list of triggers previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't specify
      this parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating
      the stack or during a previous stack update). Any triggers that you don't include in the
      updated list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
        any of the alarms you specify goes to ALARM state during the stack operation or within
        the specified monitoring period afterwards, CloudFormation rolls back the entire stack
        operation.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - **Type** *(string) --*

          The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the rollback
      triggers after the stack creation or update operation deploys all necessary resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
      still waits the specified period of time before cleaning up old resources after update
      operations. You can use this monitoring period to perform any manual stack validation
      desired, and manually cancel the stack creation or update (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
      triggers during stack creation and update operations. Then, for update operations, it
      begins disposing of old resources immediately once the operation completes.
    """


_ClientDescribeChangeSetResponseTagsTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeChangeSetResponseTagsTypeDef(
    _ClientDescribeChangeSetResponseTagsTypeDef
):
    """
    Type definition for `ClientDescribeChangeSetResponse` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --*

       *Required* . A string used to identify this tag. You can specify a maximum of 128
       characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
       prefix: ``aws:`` .

    - **Value** *(string) --*

       *Required* . A string containing the value for this tag. You can specify a maximum of
       256 characters for a tag value.
    """


_ClientDescribeChangeSetResponseTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[ClientDescribeChangeSetResponseParametersTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": str,
        "Status": str,
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": ClientDescribeChangeSetResponseRollbackConfigurationTypeDef,
        "Capabilities": List[str],
        "Tags": List[ClientDescribeChangeSetResponseTagsTypeDef],
        "Changes": List[ClientDescribeChangeSetResponseChangesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeChangeSetResponseTypeDef(_ClientDescribeChangeSetResponseTypeDef):
    """
    Type definition for `ClientDescribeChangeSet` `Response`

    The output for the  DescribeChangeSet action.

    - **ChangeSetName** *(string) --*

      The name of the change set.

    - **ChangeSetId** *(string) --*

      The ARN of the change set.

    - **StackId** *(string) --*

      The ARN of the stack that is associated with the change set.

    - **StackName** *(string) --*

      The name of the stack that is associated with the change set.

    - **Description** *(string) --*

      Information about the change set.

    - **Parameters** *(list) --*

      A list of ``Parameter`` structures that describes the input parameters and their values used
      to create the change set. For more information, see the `Parameter
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html>`__
      data type.

      - *(dict) --*

        The Parameter data type.

        - **ParameterKey** *(string) --*

          The key associated with the parameter. If you don't specify a key and value for a
          particular parameter, AWS CloudFormation uses the default value that is specified in your
          template.

        - **ParameterValue** *(string) --*

          The input value associated with the parameter.

        - **UsePreviousValue** *(boolean) --*

          During a stack update, use the existing parameter value that the stack is using for a
          given parameter key. If you specify ``true`` , do not specify a parameter value.

        - **ResolvedValue** *(string) --*

          Read-only. The value that corresponds to a Systems Manager parameter key. This field is
          returned only for ` ``SSM`` parameter types
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
          in the template.

    - **CreationTime** *(datetime) --*

      The start time when the change set was created, in UTC.

    - **ExecutionStatus** *(string) --*

      If the change set execution status is ``AVAILABLE`` , you can execute the change set. If you
      can’t execute the change set, the status indicates why. For example, a change set might be in
      an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or in an
      ``OBSOLETE`` state because the stack was already updated.

    - **Status** *(string) --*

      The current status of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` ,
      or ``FAILED`` .

    - **StatusReason** *(string) --*

      A description of the change set's status. For example, if your attempt to create a change set
      failed, AWS CloudFormation shows the error message.

    - **NotificationARNs** *(list) --*

      The ARNs of the Amazon Simple Notification Service (Amazon SNS) topics that will be
      associated with the stack if you execute the change set.

      - *(string) --*

    - **RollbackConfiguration** *(dict) --*

      The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
      operations, and for the specified monitoring period afterwards.

      - **RollbackTriggers** *(list) --*

        The triggers to monitor during stack creation or update actions.

        By default, AWS CloudFormation saves the rollback triggers specified for a stack and
        applies them to any subsequent update operations for the stack, unless you specify
        otherwise. If you do specify rollback triggers for this parameter, those triggers replace
        any list of triggers previously specified for the stack. This means:

        * To use the rollback triggers previously specified for this stack, if any, don't specify
        this parameter.

        * To specify new or updated rollback triggers, you must specify *all* the triggers that you
        want used for this stack, even triggers you've specifed before (for example, when creating
        the stack or during a previous stack update). Any triggers that you don't include in the
        updated list of triggers are no longer applied to the stack.

        * To remove all currently specified triggers, specify an empty list for this parameter.

        If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - *(dict) --*

          A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
          any of the alarms you specify goes to ALARM state during the stack operation or within
          the specified monitoring period afterwards, CloudFormation rolls back the entire stack
          operation.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the rollback trigger.

            If a specified trigger is missing, the entire stack operation fails and is rolled back.

          - **Type** *(string) --*

            The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
            is the only supported resource type.

      - **MonitoringTimeInMinutes** *(integer) --*

        The amount of time, in minutes, during which CloudFormation should monitor all the rollback
        triggers after the stack creation or update operation deploys all necessary resources.

        The default is 0 minutes.

        If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
        still waits the specified period of time before cleaning up old resources after update
        operations. You can use this monitoring period to perform any manual stack validation
        desired, and manually cancel the stack creation or update (using `CancelUpdateStack
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
        , for example) as necessary.

        If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
        triggers during stack creation and update operations. Then, for update operations, it
        begins disposing of old resources immediately once the operation completes.

    - **Capabilities** *(list) --*

      If you execute the change set, the list of capabilities that were explicitly acknowledged
      when the change set was created.

      - *(string) --*

    - **Tags** *(list) --*

      If you execute the change set, the tags that will be associated with the stack.

      - *(dict) --*

        The Tag type enables you to specify a key-value pair that can be used to store information
        about an AWS CloudFormation stack.

        - **Key** *(string) --*

           *Required* . A string used to identify this tag. You can specify a maximum of 128
           characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
           prefix: ``aws:`` .

        - **Value** *(string) --*

           *Required* . A string containing the value for this tag. You can specify a maximum of
           256 characters for a tag value.

    - **Changes** *(list) --*

      A list of ``Change`` structures that describes the resources AWS CloudFormation changes if
      you execute the change set.

      - *(dict) --*

        The ``Change`` structure describes the changes AWS CloudFormation will perform if you
        execute the change set.

        - **Type** *(string) --*

          The type of entity that AWS CloudFormation changes. Currently, the only entity type is
          ``Resource`` .

        - **ResourceChange** *(dict) --*

          A ``ResourceChange`` structure that describes the resource and action that AWS
          CloudFormation will perform.

          - **Action** *(string) --*

            The action that AWS CloudFormation takes on the resource, such as ``Add`` (adds a new
            resource), ``Modify`` (changes a resource), or ``Remove`` (deletes a resource).

          - **LogicalResourceId** *(string) --*

            The resource's logical ID, which is defined in the stack's template.

          - **PhysicalResourceId** *(string) --*

            The resource's physical ID (resource name). Resources that you are adding don't have
            physical IDs because they haven't been created.

          - **ResourceType** *(string) --*

            The type of AWS CloudFormation resource, such as ``AWS::S3::Bucket`` .

          - **Replacement** *(string) --*

            For the ``Modify`` action, indicates whether AWS CloudFormation will replace the
            resource by creating a new one and deleting the old one. This value depends on the
            value of the ``RequiresRecreation`` property in the ``ResourceTargetDefinition``
            structure. For example, if the ``RequiresRecreation`` field is ``Always`` and the
            ``Evaluation`` field is ``Static`` , ``Replacement`` is ``True`` . If the
            ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Dynamic``
            , ``Replacement`` is ``Conditionally`` .

            If you have multiple changes with different ``RequiresRecreation`` values, the
            ``Replacement`` value depends on the change with the most impact. A
            ``RequiresRecreation`` value of ``Always`` has the most impact, followed by
            ``Conditionally`` , and then ``Never`` .

          - **Scope** *(list) --*

            For the ``Modify`` action, indicates which resource attribute is triggering this
            update, such as a change in the resource attribute's ``Metadata`` , ``Properties`` , or
            ``Tags`` .

            - *(string) --*

          - **Details** *(list) --*

            For the ``Modify`` action, a list of ``ResourceChangeDetail`` structures that describes
            the changes that AWS CloudFormation will make to the resource.

            - *(dict) --*

              For a resource with ``Modify`` as the action, the ``ResourceChange`` structure
              describes the changes AWS CloudFormation will make to that resource.

              - **Target** *(dict) --*

                A ``ResourceTargetDefinition`` structure that describes the field that AWS
                CloudFormation will change and whether the resource will be recreated.

                - **Attribute** *(string) --*

                  Indicates which resource attribute is triggering this update, such as a change in
                  the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

                - **Name** *(string) --*

                  If the ``Attribute`` value is ``Properties`` , the name of the property. For all
                  other attributes, the value is null.

                - **RequiresRecreation** *(string) --*

                  If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
                  property causes the resource to be recreated. The value can be ``Never`` ,
                  ``Always`` , or ``Conditionally`` . To determine the conditions for a
                  ``Conditionally`` recreation, see the update behavior for that `property
                  <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
                  in the AWS CloudFormation User Guide.

              - **Evaluation** *(string) --*

                Indicates whether AWS CloudFormation can determine the target value, and whether
                the target value will change before you execute a change set.

                For ``Static`` evaluations, AWS CloudFormation can determine that the target value
                will change, and its value. For example, if you directly modify the
                ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this
                property value will change, and its value, so this is a ``Static`` evaluation.

                For ``Dynamic`` evaluations, cannot determine the target value because it depends
                on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt``
                intrinsic function, when the stack is updated. For example, if your template
                includes a reference to a resource that is conditionally recreated, the value of
                the reference (the physical ID of the resource) might change, depending on if the
                resource is recreated. If the resource is recreated, it will have a new physical
                ID, so all references to that resource will also be updated.

              - **ChangeSource** *(string) --*

                The group to which the ``CausingEntity`` value belongs. There are five entity
                groups:

                * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to
                resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` .

                * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template
                parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` .

                * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get
                resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource",
                "PublicDnsName" ] }`` .

                * ``DirectModification`` entities are changes that are made directly to the
                template.

                * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which
                are also known as nested stacks. If you made no changes to the
                ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the
                ``ChangeSource`` to ``Automatic`` because the nested stack's template might have
                changed. Changes to a nested stack's template aren't visible to AWS CloudFormation
                until you run an update on the parent stack.

              - **CausingEntity** *(string) --*

                The identity of the entity that triggered this change. This entity is a member of
                the group that is specified by the ``ChangeSource`` field. For example, if you
                modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the
                name of the parameter (``KeyPairName`` ).

                If the ``ChangeSource`` value is ``DirectModification`` , no value is given for
                ``CausingEntity`` .

    - **NextToken** *(string) --*

      If the output exceeds 1 MB, a string that identifies the next page of changes. If there is no
      additional page, this value is null.
    """


_ClientDescribeStackDriftDetectionStatusResponseTypeDef = TypedDict(
    "_ClientDescribeStackDriftDetectionStatusResponseTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "StackDriftStatus": str,
        "DetectionStatus": str,
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "Timestamp": datetime,
    },
    total=False,
)


class ClientDescribeStackDriftDetectionStatusResponseTypeDef(
    _ClientDescribeStackDriftDetectionStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackDriftDetectionStatus` `Response`

    - **StackId** *(string) --*

      The ID of the stack.

    - **StackDriftDetectionId** *(string) --*

      The ID of the drift detection results of this operation.

      AWS CloudFormation generates new results, with a new drift detection ID, each time this
      operation is run. However, the number of reports AWS CloudFormation retains for any given
      stack, and for how long, may vary.

    - **StackDriftStatus** *(string) --*

      Status of the stack's actual configuration compared to its expected configuration.

      * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
      considered to have drifted if one or more of its resources have drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its expected
      template configuration.

      * ``IN_SYNC`` : The stack's actual configuration matches its expected template configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **DetectionStatus** *(string) --*

      The status of the stack drift detection operation.

      * ``DETECTION_COMPLETE`` : The stack drift detection operation has successfully completed for
      all resources in the stack that support drift detection. (Resources that do not currently
      support stack detection remain unchecked.) If you specified logical resource IDs for AWS
      CloudFormation to use as a filter for the stack drift detection operation, only the resources
      with those logical IDs are checked for drift.

      * ``DETECTION_FAILED`` : The stack drift detection operation has failed for at least one
      resource in the stack. Results will be available for resources on which AWS CloudFormation
      successfully completed drift detection.

      * ``DETECTION_IN_PROGRESS`` : The stack drift detection operation is currently in progress.

    - **DetectionStatusReason** *(string) --*

      The reason the stack drift detection operation has its current status.

    - **DriftedStackResourceCount** *(integer) --*

      Total number of stack resources that have drifted. This is NULL until the drift detection
      operation reaches a status of ``DETECTION_COMPLETE`` . This value will be 0 for stacks whose
      drift status is ``IN_SYNC`` .

    - **Timestamp** *(datetime) --*

      Time at which the stack drift detection operation was initiated.
    """


_ClientDescribeStackEventsResponseStackEventsTypeDef = TypedDict(
    "_ClientDescribeStackEventsResponseStackEventsTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": str,
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class ClientDescribeStackEventsResponseStackEventsTypeDef(
    _ClientDescribeStackEventsResponseStackEventsTypeDef
):
    """
    Type definition for `ClientDescribeStackEventsResponse` `StackEvents`

    The StackEvent data type.

    - **StackId** *(string) --*

      The unique ID name of the instance of the stack.

    - **EventId** *(string) --*

      The unique ID of this event.

    - **StackName** *(string) --*

      The name associated with a stack.

    - **LogicalResourceId** *(string) --*

      The logical name of the resource specified in the template.

    - **PhysicalResourceId** *(string) --*

      The name or unique identifier associated with the physical instance of the resource.

    - **ResourceType** *(string) --*

      Type of resource. (For more information, go to `AWS Resource Types Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
      in the AWS CloudFormation User Guide.)

    - **Timestamp** *(datetime) --*

      Time the status was updated.

    - **ResourceStatus** *(string) --*

      Current status of the resource.

    - **ResourceStatusReason** *(string) --*

      Success/failure message associated with the resource.

    - **ResourceProperties** *(string) --*

      BLOB of the properties used to create the resource.

    - **ClientRequestToken** *(string) --*

      The token passed to the operation that generated this event.

      All events triggered by a given stack operation are assigned the same client request
      token, which you can use to track operations. For example, if you execute a
      ``CreateStack`` operation with the token ``token1`` , then all the ``StackEvents``
      generated by that operation will have ``ClientRequestToken`` set as ``token1`` .

      In the console, stack operations display the client request token on the Events tab.
      Stack operations that are initiated from the console use the token format
      *Console-StackOperation-ID* , which helps you easily identify the stack operation . For
      example, if you create a stack using the console, each stack event would be assigned the
      same token in the following format:
      ``Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`` .
    """


_ClientDescribeStackEventsResponseTypeDef = TypedDict(
    "_ClientDescribeStackEventsResponseTypeDef",
    {
        "StackEvents": List[ClientDescribeStackEventsResponseStackEventsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeStackEventsResponseTypeDef(
    _ClientDescribeStackEventsResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackEvents` `Response`

    The output for a  DescribeStackEvents action.

    - **StackEvents** *(list) --*

      A list of ``StackEvents`` structures.

      - *(dict) --*

        The StackEvent data type.

        - **StackId** *(string) --*

          The unique ID name of the instance of the stack.

        - **EventId** *(string) --*

          The unique ID of this event.

        - **StackName** *(string) --*

          The name associated with a stack.

        - **LogicalResourceId** *(string) --*

          The logical name of the resource specified in the template.

        - **PhysicalResourceId** *(string) --*

          The name or unique identifier associated with the physical instance of the resource.

        - **ResourceType** *(string) --*

          Type of resource. (For more information, go to `AWS Resource Types Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
          in the AWS CloudFormation User Guide.)

        - **Timestamp** *(datetime) --*

          Time the status was updated.

        - **ResourceStatus** *(string) --*

          Current status of the resource.

        - **ResourceStatusReason** *(string) --*

          Success/failure message associated with the resource.

        - **ResourceProperties** *(string) --*

          BLOB of the properties used to create the resource.

        - **ClientRequestToken** *(string) --*

          The token passed to the operation that generated this event.

          All events triggered by a given stack operation are assigned the same client request
          token, which you can use to track operations. For example, if you execute a
          ``CreateStack`` operation with the token ``token1`` , then all the ``StackEvents``
          generated by that operation will have ``ClientRequestToken`` set as ``token1`` .

          In the console, stack operations display the client request token on the Events tab.
          Stack operations that are initiated from the console use the token format
          *Console-StackOperation-ID* , which helps you easily identify the stack operation . For
          example, if you create a stack using the console, each stack event would be assigned the
          same token in the following format:
          ``Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`` .

    - **NextToken** *(string) --*

      If the output exceeds 1 MB in size, a string that identifies the next page of events. If no
      additional page exists, this value is null.
    """


_ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef = TypedDict(
    "_ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef(
    _ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef
):
    """
    Type definition for `ClientDescribeStackInstanceResponseStackInstance` `ParameterOverrides`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a
      particular parameter, AWS CloudFormation uses the default value that is specified in
      your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a
      given parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientDescribeStackInstanceResponseStackInstanceTypeDef = TypedDict(
    "_ClientDescribeStackInstanceResponseStackInstanceTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "ParameterOverrides": List[
            ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef
        ],
        "Status": str,
        "StatusReason": str,
        "DriftStatus": str,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeStackInstanceResponseStackInstanceTypeDef(
    _ClientDescribeStackInstanceResponseStackInstanceTypeDef
):
    """
    Type definition for `ClientDescribeStackInstanceResponse` `StackInstance`

    The stack instance that matches the specified request parameters.

    - **StackSetId** *(string) --*

      The name or unique ID of the stack set that the stack instance is associated with.

    - **Region** *(string) --*

      The name of the AWS region that the stack instance is associated with.

    - **Account** *(string) --*

      The name of the AWS account that the stack instance is associated with.

    - **StackId** *(string) --*

      The ID of the stack instance.

    - **ParameterOverrides** *(list) --*

      A list of parameters from the stack set template whose values have been overridden in this
      stack instance.

      - *(dict) --*

        The Parameter data type.

        - **ParameterKey** *(string) --*

          The key associated with the parameter. If you don't specify a key and value for a
          particular parameter, AWS CloudFormation uses the default value that is specified in
          your template.

        - **ParameterValue** *(string) --*

          The input value associated with the parameter.

        - **UsePreviousValue** *(boolean) --*

          During a stack update, use the existing parameter value that the stack is using for a
          given parameter key. If you specify ``true`` , do not specify a parameter value.

        - **ResolvedValue** *(string) --*

          Read-only. The value that corresponds to a Systems Manager parameter key. This field is
          returned only for ` ``SSM`` parameter types
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
          in the template.

    - **Status** *(string) --*

      The status of the stack instance, in terms of its synchronization with its associated stack
      set.

      * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in an
      unstable state. Stacks in this state are excluded from further ``UpdateStackSet``
      operations. You might need to perform a ``DeleteStackInstances`` operation, with
      ``RetainStacks`` set to ``true`` , to delete the stack instance, and then delete the stack
      manually.

      * ``OUTDATED`` : The stack isn't currently up to date with the stack set because:

        * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet`` operation.

        * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that failed
        or was stopped before the stack was created or updated.

      * ``CURRENT`` : The stack is currently up to date with the stack set.

    - **StatusReason** *(string) --*

      The explanation for the specific status code that is assigned to this stack instance.

    - **DriftStatus** *(string) --*

      Status of the stack instance's actual configuration compared to the expected template and
      parameter configuration of the stack set to which it belongs.

      * ``DRIFTED`` : The stack differs from the expected template and parameter configuration of
      the stack set to which it belongs. A stack instance is considered to have drifted if one or
      more of the resources in the associated stack have drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack instance differs from
      its expected stack set configuration.

      * ``IN_SYNC`` : The stack instance's actual configuration matches its expected stack set
      configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastDriftCheckTimestamp** *(datetime) --*

      Most recent time when CloudFormation performed a drift detection operation on the stack
      instance. This value will be ``NULL`` for any stack instance on which drift detection has
      not yet been performed.
    """


_ClientDescribeStackInstanceResponseTypeDef = TypedDict(
    "_ClientDescribeStackInstanceResponseTypeDef",
    {"StackInstance": ClientDescribeStackInstanceResponseStackInstanceTypeDef},
    total=False,
)


class ClientDescribeStackInstanceResponseTypeDef(
    _ClientDescribeStackInstanceResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackInstance` `Response`

    - **StackInstance** *(dict) --*

      The stack instance that matches the specified request parameters.

      - **StackSetId** *(string) --*

        The name or unique ID of the stack set that the stack instance is associated with.

      - **Region** *(string) --*

        The name of the AWS region that the stack instance is associated with.

      - **Account** *(string) --*

        The name of the AWS account that the stack instance is associated with.

      - **StackId** *(string) --*

        The ID of the stack instance.

      - **ParameterOverrides** *(list) --*

        A list of parameters from the stack set template whose values have been overridden in this
        stack instance.

        - *(dict) --*

          The Parameter data type.

          - **ParameterKey** *(string) --*

            The key associated with the parameter. If you don't specify a key and value for a
            particular parameter, AWS CloudFormation uses the default value that is specified in
            your template.

          - **ParameterValue** *(string) --*

            The input value associated with the parameter.

          - **UsePreviousValue** *(boolean) --*

            During a stack update, use the existing parameter value that the stack is using for a
            given parameter key. If you specify ``true`` , do not specify a parameter value.

          - **ResolvedValue** *(string) --*

            Read-only. The value that corresponds to a Systems Manager parameter key. This field is
            returned only for ` ``SSM`` parameter types
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
            in the template.

      - **Status** *(string) --*

        The status of the stack instance, in terms of its synchronization with its associated stack
        set.

        * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in an
        unstable state. Stacks in this state are excluded from further ``UpdateStackSet``
        operations. You might need to perform a ``DeleteStackInstances`` operation, with
        ``RetainStacks`` set to ``true`` , to delete the stack instance, and then delete the stack
        manually.

        * ``OUTDATED`` : The stack isn't currently up to date with the stack set because:

          * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet`` operation.

          * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that failed
          or was stopped before the stack was created or updated.

        * ``CURRENT`` : The stack is currently up to date with the stack set.

      - **StatusReason** *(string) --*

        The explanation for the specific status code that is assigned to this stack instance.

      - **DriftStatus** *(string) --*

        Status of the stack instance's actual configuration compared to the expected template and
        parameter configuration of the stack set to which it belongs.

        * ``DRIFTED`` : The stack differs from the expected template and parameter configuration of
        the stack set to which it belongs. A stack instance is considered to have drifted if one or
        more of the resources in the associated stack have drifted.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack instance differs from
        its expected stack set configuration.

        * ``IN_SYNC`` : The stack instance's actual configuration matches its expected stack set
        configuration.

        * ``UNKNOWN`` : This value is reserved for future use.

      - **LastDriftCheckTimestamp** *(datetime) --*

        Most recent time when CloudFormation performed a drift detection operation on the stack
        instance. This value will be ``NULL`` for any stack instance on which drift detection has
        not yet been performed.
    """


_ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef = TypedDict(
    "_ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef(
    _ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef
):
    """
    Type definition for `ClientDescribeStackResourceDriftsResponseStackResourceDrifts` `PhysicalResourceIdContext`

    Context information that enables AWS CloudFormation to uniquely identify a resource.
    AWS CloudFormation uses context key-value pairs in cases where a resource's logical and
    physical IDs are not enough to uniquely identify that resource. Each context key-value
    pair specifies a resource that contains the targeted resource.

    - **Key** *(string) --*

      The resource context key.

    - **Value** *(string) --*

      The resource context value.
    """


_ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef = TypedDict(
    "_ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": str,
    },
    total=False,
)


class ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef(
    _ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef
):
    """
    Type definition for `ClientDescribeStackResourceDriftsResponseStackResourceDrifts` `PropertyDifferences`

    Information about a resource property whose actual value differs from its expected
    value, as defined in the stack template and any values specified as template
    parameters. These will be present only for resources whose ``StackResourceDriftStatus``
    is ``MODIFIED`` . For more information, see `Detecting Unregulated Configuration
    Changes to Stacks and Resources
    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **PropertyPath** *(string) --*

      The fully-qualified path to the resource property.

    - **ExpectedValue** *(string) --*

      The expected property value of the resource property, as defined in the stack
      template and any values specified as template parameters.

    - **ActualValue** *(string) --*

      The actual property value of the resource property.

    - **DifferenceType** *(string) --*

      The type of property difference.

      * ``ADD`` : A value has been added to a resource property that is an array or list
      data type.

      * ``REMOVE`` : The property has been removed from the current resource configuration.

      * ``NOT_EQUAL`` : The current property value differs from its expected value (as
      defined in the stack template and any values specified as template parameters).
    """


_ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef = TypedDict(
    "_ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef
        ],
        "ResourceType": str,
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef
        ],
        "StackResourceDriftStatus": str,
        "Timestamp": datetime,
    },
    total=False,
)


class ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef(
    _ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef
):
    """
    Type definition for `ClientDescribeStackResourceDriftsResponse` `StackResourceDrifts`

    Contains the drift information for a resource that has been checked for drift. This
    includes actual and expected property values for resources in which AWS CloudFormation has
    detected drift. Only resource properties explicitly defined in the stack template are
    checked for drift. For more information, see `Detecting Unregulated Configuration Changes
    to Stacks and Resources
    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    Resources that do not currently support drift detection cannot be checked. For a list of
    resources that support drift detection, see `Resources that Support Drift Detection
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
    .

    Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift
    to detect drift on all resources in a given stack that support drift detection.

    - **StackId** *(string) --*

      The ID of the stack.

    - **LogicalResourceId** *(string) --*

      The logical name of the resource specified in the template.

    - **PhysicalResourceId** *(string) --*

      The name or unique identifier that corresponds to a physical instance ID of a resource
      supported by AWS CloudFormation.

    - **PhysicalResourceIdContext** *(list) --*

      Context information that enables AWS CloudFormation to uniquely identify a resource. AWS
      CloudFormation uses context key-value pairs in cases where a resource's logical and
      physical IDs are not enough to uniquely identify that resource. Each context key-value
      pair specifies a unique resource that contains the targeted resource.

      - *(dict) --*

        Context information that enables AWS CloudFormation to uniquely identify a resource.
        AWS CloudFormation uses context key-value pairs in cases where a resource's logical and
        physical IDs are not enough to uniquely identify that resource. Each context key-value
        pair specifies a resource that contains the targeted resource.

        - **Key** *(string) --*

          The resource context key.

        - **Value** *(string) --*

          The resource context value.

    - **ResourceType** *(string) --*

      The type of the resource.

    - **ExpectedProperties** *(string) --*

      A JSON structure containing the expected property values of the stack resource, as
      defined in the stack template and any values specified as template parameters.

      For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not
      be present.

    - **ActualProperties** *(string) --*

      A JSON structure containing the actual property values of the stack resource.

      For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not
      be present.

    - **PropertyDifferences** *(list) --*

      A collection of the resource properties whose actual values differ from their expected
      values. These will be present only for resources whose ``StackResourceDriftStatus`` is
      ``MODIFIED`` .

      - *(dict) --*

        Information about a resource property whose actual value differs from its expected
        value, as defined in the stack template and any values specified as template
        parameters. These will be present only for resources whose ``StackResourceDriftStatus``
        is ``MODIFIED`` . For more information, see `Detecting Unregulated Configuration
        Changes to Stacks and Resources
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
        .

        - **PropertyPath** *(string) --*

          The fully-qualified path to the resource property.

        - **ExpectedValue** *(string) --*

          The expected property value of the resource property, as defined in the stack
          template and any values specified as template parameters.

        - **ActualValue** *(string) --*

          The actual property value of the resource property.

        - **DifferenceType** *(string) --*

          The type of property difference.

          * ``ADD`` : A value has been added to a resource property that is an array or list
          data type.

          * ``REMOVE`` : The property has been removed from the current resource configuration.

          * ``NOT_EQUAL`` : The current property value differs from its expected value (as
          defined in the stack template and any values specified as template parameters).

    - **StackResourceDriftStatus** *(string) --*

      Status of the resource's actual configuration compared to its expected configuration

      * ``DELETED`` : The resource differs from its expected template configuration because the
      resource has been deleted.

      * ``MODIFIED`` : One or more resource properties differ from their expected values (as
      defined in the stack template and any values specified as template parameters).

      * ``IN_SYNC`` : The resources's actual configuration matches its expected template
      configuration.

      * ``NOT_CHECKED`` : AWS CloudFormation does not currently return this value.

    - **Timestamp** *(datetime) --*

      Time at which AWS CloudFormation performed drift detection on the stack resource.
    """


_ClientDescribeStackResourceDriftsResponseTypeDef = TypedDict(
    "_ClientDescribeStackResourceDriftsResponseTypeDef",
    {
        "StackResourceDrifts": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeStackResourceDriftsResponseTypeDef(
    _ClientDescribeStackResourceDriftsResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackResourceDrifts` `Response`

    - **StackResourceDrifts** *(list) --*

      Drift information for the resources that have been checked for drift in the specified stack.
      This includes actual and expected configuration values for resources where AWS CloudFormation
      detects drift.

      For a given stack, there will be one ``StackResourceDrift`` for each stack resource that has
      been checked for drift. Resources that have not yet been checked for drift are not included.
      Resources that do not currently support drift detection are not checked, and so not included.
      For a list of resources that support drift detection, see `Resources that Support Drift
      Detection
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
      .

      - *(dict) --*

        Contains the drift information for a resource that has been checked for drift. This
        includes actual and expected property values for resources in which AWS CloudFormation has
        detected drift. Only resource properties explicitly defined in the stack template are
        checked for drift. For more information, see `Detecting Unregulated Configuration Changes
        to Stacks and Resources
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
        .

        Resources that do not currently support drift detection cannot be checked. For a list of
        resources that support drift detection, see `Resources that Support Drift Detection
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
        .

        Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift
        to detect drift on all resources in a given stack that support drift detection.

        - **StackId** *(string) --*

          The ID of the stack.

        - **LogicalResourceId** *(string) --*

          The logical name of the resource specified in the template.

        - **PhysicalResourceId** *(string) --*

          The name or unique identifier that corresponds to a physical instance ID of a resource
          supported by AWS CloudFormation.

        - **PhysicalResourceIdContext** *(list) --*

          Context information that enables AWS CloudFormation to uniquely identify a resource. AWS
          CloudFormation uses context key-value pairs in cases where a resource's logical and
          physical IDs are not enough to uniquely identify that resource. Each context key-value
          pair specifies a unique resource that contains the targeted resource.

          - *(dict) --*

            Context information that enables AWS CloudFormation to uniquely identify a resource.
            AWS CloudFormation uses context key-value pairs in cases where a resource's logical and
            physical IDs are not enough to uniquely identify that resource. Each context key-value
            pair specifies a resource that contains the targeted resource.

            - **Key** *(string) --*

              The resource context key.

            - **Value** *(string) --*

              The resource context value.

        - **ResourceType** *(string) --*

          The type of the resource.

        - **ExpectedProperties** *(string) --*

          A JSON structure containing the expected property values of the stack resource, as
          defined in the stack template and any values specified as template parameters.

          For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not
          be present.

        - **ActualProperties** *(string) --*

          A JSON structure containing the actual property values of the stack resource.

          For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not
          be present.

        - **PropertyDifferences** *(list) --*

          A collection of the resource properties whose actual values differ from their expected
          values. These will be present only for resources whose ``StackResourceDriftStatus`` is
          ``MODIFIED`` .

          - *(dict) --*

            Information about a resource property whose actual value differs from its expected
            value, as defined in the stack template and any values specified as template
            parameters. These will be present only for resources whose ``StackResourceDriftStatus``
            is ``MODIFIED`` . For more information, see `Detecting Unregulated Configuration
            Changes to Stacks and Resources
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
            .

            - **PropertyPath** *(string) --*

              The fully-qualified path to the resource property.

            - **ExpectedValue** *(string) --*

              The expected property value of the resource property, as defined in the stack
              template and any values specified as template parameters.

            - **ActualValue** *(string) --*

              The actual property value of the resource property.

            - **DifferenceType** *(string) --*

              The type of property difference.

              * ``ADD`` : A value has been added to a resource property that is an array or list
              data type.

              * ``REMOVE`` : The property has been removed from the current resource configuration.

              * ``NOT_EQUAL`` : The current property value differs from its expected value (as
              defined in the stack template and any values specified as template parameters).

        - **StackResourceDriftStatus** *(string) --*

          Status of the resource's actual configuration compared to its expected configuration

          * ``DELETED`` : The resource differs from its expected template configuration because the
          resource has been deleted.

          * ``MODIFIED`` : One or more resource properties differ from their expected values (as
          defined in the stack template and any values specified as template parameters).

          * ``IN_SYNC`` : The resources's actual configuration matches its expected template
          configuration.

          * ``NOT_CHECKED`` : AWS CloudFormation does not currently return this value.

        - **Timestamp** *(datetime) --*

          Time at which AWS CloudFormation performed drift detection on the stack resource.

    - **NextToken** *(string) --*

      If the request doesn't return all of the remaining results, ``NextToken`` is set to a token.
      To retrieve the next set of results, call ``DescribeStackResourceDrifts`` again and assign
      that token to the request object's ``NextToken`` parameter. If the request returns all
      results, ``NextToken`` is set to ``null`` .
    """


_ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef = TypedDict(
    "_ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef",
    {"StackResourceDriftStatus": str, "LastCheckTimestamp": datetime},
    total=False,
)


class ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef(
    _ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef
):
    """
    Type definition for `ClientDescribeStackResourceResponseStackResourceDetail` `DriftInformation`

    Information about whether the resource's actual configuration differs, or has *drifted* ,
    from its expected configuration, as defined in the stack template and any values specified
    as template parameters. For more information, see `Detecting Unregulated Configuration
    Changes to Stacks and Resources
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **StackResourceDriftStatus** *(string) --*

      Status of the resource's actual configuration compared to its expected configuration

      * ``DELETED`` : The resource differs from its expected configuration in that it has been
      deleted.

      * ``MODIFIED`` : The resource differs from its expected configuration.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
      expected configuration. Any resources that do not currently support drift detection have
      a status of ``NOT_CHECKED`` . For more information, see `Resources that Support Drift
      Detection
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
      .

      * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

    - **LastCheckTimestamp** *(datetime) --*

      When AWS CloudFormation last checked if the resource had drifted from its expected
      configuration.
    """


_ClientDescribeStackResourceResponseStackResourceDetailTypeDef = TypedDict(
    "_ClientDescribeStackResourceResponseStackResourceDetailTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": str,
        "ResourceStatusReason": str,
        "Description": str,
        "Metadata": str,
        "DriftInformation": ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef,
    },
    total=False,
)


class ClientDescribeStackResourceResponseStackResourceDetailTypeDef(
    _ClientDescribeStackResourceResponseStackResourceDetailTypeDef
):
    """
    Type definition for `ClientDescribeStackResourceResponse` `StackResourceDetail`

    A ``StackResourceDetail`` structure containing the description of the specified resource in
    the specified stack.

    - **StackName** *(string) --*

      The name associated with the stack.

    - **StackId** *(string) --*

      Unique identifier of the stack.

    - **LogicalResourceId** *(string) --*

      The logical name of the resource specified in the template.

    - **PhysicalResourceId** *(string) --*

      The name or unique identifier that corresponds to a physical instance ID of a resource
      supported by AWS CloudFormation.

    - **ResourceType** *(string) --*

      Type of resource. ((For more information, go to `AWS Resource Types Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
      in the AWS CloudFormation User Guide.)

    - **LastUpdatedTimestamp** *(datetime) --*

      Time the status was updated.

    - **ResourceStatus** *(string) --*

      Current status of the resource.

    - **ResourceStatusReason** *(string) --*

      Success/failure message associated with the resource.

    - **Description** *(string) --*

      User defined description associated with the resource.

    - **Metadata** *(string) --*

      The content of the ``Metadata`` attribute declared for the resource. For more information,
      see `Metadata Attribute
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-metadata.html>`__
      in the AWS CloudFormation User Guide.

    - **DriftInformation** *(dict) --*

      Information about whether the resource's actual configuration differs, or has *drifted* ,
      from its expected configuration, as defined in the stack template and any values specified
      as template parameters. For more information, see `Detecting Unregulated Configuration
      Changes to Stacks and Resources
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .

      - **StackResourceDriftStatus** *(string) --*

        Status of the resource's actual configuration compared to its expected configuration

        * ``DELETED`` : The resource differs from its expected configuration in that it has been
        deleted.

        * ``MODIFIED`` : The resource differs from its expected configuration.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
        expected configuration. Any resources that do not currently support drift detection have
        a status of ``NOT_CHECKED`` . For more information, see `Resources that Support Drift
        Detection
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
        .

        * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

      - **LastCheckTimestamp** *(datetime) --*

        When AWS CloudFormation last checked if the resource had drifted from its expected
        configuration.
    """


_ClientDescribeStackResourceResponseTypeDef = TypedDict(
    "_ClientDescribeStackResourceResponseTypeDef",
    {
        "StackResourceDetail": ClientDescribeStackResourceResponseStackResourceDetailTypeDef
    },
    total=False,
)


class ClientDescribeStackResourceResponseTypeDef(
    _ClientDescribeStackResourceResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackResource` `Response`

    The output for a  DescribeStackResource action.

    - **StackResourceDetail** *(dict) --*

      A ``StackResourceDetail`` structure containing the description of the specified resource in
      the specified stack.

      - **StackName** *(string) --*

        The name associated with the stack.

      - **StackId** *(string) --*

        Unique identifier of the stack.

      - **LogicalResourceId** *(string) --*

        The logical name of the resource specified in the template.

      - **PhysicalResourceId** *(string) --*

        The name or unique identifier that corresponds to a physical instance ID of a resource
        supported by AWS CloudFormation.

      - **ResourceType** *(string) --*

        Type of resource. ((For more information, go to `AWS Resource Types Reference
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
        in the AWS CloudFormation User Guide.)

      - **LastUpdatedTimestamp** *(datetime) --*

        Time the status was updated.

      - **ResourceStatus** *(string) --*

        Current status of the resource.

      - **ResourceStatusReason** *(string) --*

        Success/failure message associated with the resource.

      - **Description** *(string) --*

        User defined description associated with the resource.

      - **Metadata** *(string) --*

        The content of the ``Metadata`` attribute declared for the resource. For more information,
        see `Metadata Attribute
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-metadata.html>`__
        in the AWS CloudFormation User Guide.

      - **DriftInformation** *(dict) --*

        Information about whether the resource's actual configuration differs, or has *drifted* ,
        from its expected configuration, as defined in the stack template and any values specified
        as template parameters. For more information, see `Detecting Unregulated Configuration
        Changes to Stacks and Resources
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
        .

        - **StackResourceDriftStatus** *(string) --*

          Status of the resource's actual configuration compared to its expected configuration

          * ``DELETED`` : The resource differs from its expected configuration in that it has been
          deleted.

          * ``MODIFIED`` : The resource differs from its expected configuration.

          * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
          expected configuration. Any resources that do not currently support drift detection have
          a status of ``NOT_CHECKED`` . For more information, see `Resources that Support Drift
          Detection
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
          .

          * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

        - **LastCheckTimestamp** *(datetime) --*

          When AWS CloudFormation last checked if the resource had drifted from its expected
          configuration.
    """


_ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef = TypedDict(
    "_ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef",
    {"StackResourceDriftStatus": str, "LastCheckTimestamp": datetime},
    total=False,
)


class ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef(
    _ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef
):
    """
    Type definition for `ClientDescribeStackResourcesResponseStackResources` `DriftInformation`

    Information about whether the resource's actual configuration differs, or has *drifted* ,
    from its expected configuration, as defined in the stack template and any values
    specified as template parameters. For more information, see `Detecting Unregulated
    Configuration Changes to Stacks and Resources
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **StackResourceDriftStatus** *(string) --*

      Status of the resource's actual configuration compared to its expected configuration

      * ``DELETED`` : The resource differs from its expected configuration in that it has
      been deleted.

      * ``MODIFIED`` : The resource differs from its expected configuration.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
      expected configuration. Any resources that do not currently support drift detection
      have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
      Drift Detection
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
      .

      * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

    - **LastCheckTimestamp** *(datetime) --*

      When AWS CloudFormation last checked if the resource had drifted from its expected
      configuration.
    """


_ClientDescribeStackResourcesResponseStackResourcesTypeDef = TypedDict(
    "_ClientDescribeStackResourcesResponseStackResourcesTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": str,
        "ResourceStatusReason": str,
        "Description": str,
        "DriftInformation": ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef,
    },
    total=False,
)


class ClientDescribeStackResourcesResponseStackResourcesTypeDef(
    _ClientDescribeStackResourcesResponseStackResourcesTypeDef
):
    """
    Type definition for `ClientDescribeStackResourcesResponse` `StackResources`

    The StackResource data type.

    - **StackName** *(string) --*

      The name associated with the stack.

    - **StackId** *(string) --*

      Unique identifier of the stack.

    - **LogicalResourceId** *(string) --*

      The logical name of the resource specified in the template.

    - **PhysicalResourceId** *(string) --*

      The name or unique identifier that corresponds to a physical instance ID of a resource
      supported by AWS CloudFormation.

    - **ResourceType** *(string) --*

      Type of resource. (For more information, go to `AWS Resource Types Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
      in the AWS CloudFormation User Guide.)

    - **Timestamp** *(datetime) --*

      Time the status was updated.

    - **ResourceStatus** *(string) --*

      Current status of the resource.

    - **ResourceStatusReason** *(string) --*

      Success/failure message associated with the resource.

    - **Description** *(string) --*

      User defined description associated with the resource.

    - **DriftInformation** *(dict) --*

      Information about whether the resource's actual configuration differs, or has *drifted* ,
      from its expected configuration, as defined in the stack template and any values
      specified as template parameters. For more information, see `Detecting Unregulated
      Configuration Changes to Stacks and Resources
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .

      - **StackResourceDriftStatus** *(string) --*

        Status of the resource's actual configuration compared to its expected configuration

        * ``DELETED`` : The resource differs from its expected configuration in that it has
        been deleted.

        * ``MODIFIED`` : The resource differs from its expected configuration.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
        expected configuration. Any resources that do not currently support drift detection
        have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
        Drift Detection
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
        .

        * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

      - **LastCheckTimestamp** *(datetime) --*

        When AWS CloudFormation last checked if the resource had drifted from its expected
        configuration.
    """


_ClientDescribeStackResourcesResponseTypeDef = TypedDict(
    "_ClientDescribeStackResourcesResponseTypeDef",
    {"StackResources": List[ClientDescribeStackResourcesResponseStackResourcesTypeDef]},
    total=False,
)


class ClientDescribeStackResourcesResponseTypeDef(
    _ClientDescribeStackResourcesResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackResources` `Response`

    The output for a  DescribeStackResources action.

    - **StackResources** *(list) --*

      A list of ``StackResource`` structures.

      - *(dict) --*

        The StackResource data type.

        - **StackName** *(string) --*

          The name associated with the stack.

        - **StackId** *(string) --*

          Unique identifier of the stack.

        - **LogicalResourceId** *(string) --*

          The logical name of the resource specified in the template.

        - **PhysicalResourceId** *(string) --*

          The name or unique identifier that corresponds to a physical instance ID of a resource
          supported by AWS CloudFormation.

        - **ResourceType** *(string) --*

          Type of resource. (For more information, go to `AWS Resource Types Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
          in the AWS CloudFormation User Guide.)

        - **Timestamp** *(datetime) --*

          Time the status was updated.

        - **ResourceStatus** *(string) --*

          Current status of the resource.

        - **ResourceStatusReason** *(string) --*

          Success/failure message associated with the resource.

        - **Description** *(string) --*

          User defined description associated with the resource.

        - **DriftInformation** *(dict) --*

          Information about whether the resource's actual configuration differs, or has *drifted* ,
          from its expected configuration, as defined in the stack template and any values
          specified as template parameters. For more information, see `Detecting Unregulated
          Configuration Changes to Stacks and Resources
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .

          - **StackResourceDriftStatus** *(string) --*

            Status of the resource's actual configuration compared to its expected configuration

            * ``DELETED`` : The resource differs from its expected configuration in that it has
            been deleted.

            * ``MODIFIED`` : The resource differs from its expected configuration.

            * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
            expected configuration. Any resources that do not currently support drift detection
            have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
            Drift Detection
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
            .

            * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

          - **LastCheckTimestamp** *(datetime) --*

            When AWS CloudFormation last checked if the resource had drifted from its expected
            configuration.
    """


_ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef = TypedDict(
    "_ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef(
    _ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef
):
    """
    Type definition for `ClientDescribeStackSetOperationResponseStackSetOperation` `OperationPreferences`

    The preferences for how AWS CloudFormation performs this stack set operation.

    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.

      - *(string) --*

    - **FailureToleranceCount** *(integer) --*

      The number of accounts, per region, for which this operation can fail before AWS
      CloudFormation stops the operation in that region. If the operation is stopped in a
      region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` (but not both).

    - **FailureTolerancePercentage** *(integer) --*

      The percentage of accounts, per region, for which this stack operation can fail before
      AWS CloudFormation stops the operation in that region. If the operation is stopped in a
      region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.

      When calculating the number of accounts based on the specified percentage, AWS
      CloudFormation rounds *down* to the next whole number.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` , but not both.

    - **MaxConcurrentCount** *(integer) --*

      The maximum number of accounts in which to perform this operation at one time. This is
      dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most
      one more than the ``FailureToleranceCount`` .

      Note that this setting lets you specify the *maximum* for operations. For large
      deployments, under certain circumstances the actual number of accounts acted upon
      concurrently may be lower due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or
      ``MaxConcurrentPercentage`` , but not both.

    - **MaxConcurrentPercentage** *(integer) --*

      The maximum percentage of accounts in which to perform this operation at one time.

      When calculating the number of accounts based on the specified percentage, AWS
      CloudFormation rounds down to the next whole number. This is true except in cases where
      rounding down would result is zero. In this case, CloudFormation sets the number as one
      instead.

      Note that this setting lets you specify the *maximum* for operations. For large
      deployments, under certain circumstances the actual number of accounts acted upon
      concurrently may be lower due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or
      ``MaxConcurrentPercentage`` , but not both.
    """


_ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef = TypedDict(
    "_ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": str,
        "DriftDetectionStatus": str,
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)


class ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef(
    _ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef
):
    """
    Type definition for `ClientDescribeStackSetOperationResponseStackSetOperation` `StackSetDriftDetectionDetails`

    Detailed information about the drift status of the stack set. This includes information
    about drift operations currently being performed on the stack set.

    this information will only be present for stack set operations whose ``Action`` type is
    ``DETECT_DRIFT`` .

    For more information, see `Detecting Unmanaged Changes in Stack Sets
    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html>`__ in
    the AWS CloudFormation User Guide.

    - **DriftStatus** *(string) --*

      Status of the stack set's actual configuration compared to its expected template and
      parameter configuration. A stack set is considered to have drifted if one or more of its
      stack instances have drifted from their expected template and parameter configuration.

      * ``DRIFTED`` : One or more of the stack instances belonging to the stack set stack
      differs from the expected template and parameter configuration. A stack instance is
      considered to have drifted if one or more of the resources in the associated stack have
      drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked the stack set for drift.

      * ``IN_SYNC`` : All of the stack instances belonging to the stack set stack match from
      the expected template and parameter configuration.

    - **DriftDetectionStatus** *(string) --*

      The status of the stack set drift detection operation.

      * ``COMPLETED`` : The drift detection operation completed without failing on any stack
      instances.

      * ``FAILED`` : The drift detection operation exceeded the specified failure tolerance.

      * ``PARTIAL_SUCCESS`` : The drift detection operation completed without exceeding the
      failure tolerance for the operation.

      * ``IN_PROGRESS`` : The drift detection operation is currently being performed.

      * ``STOPPED`` : The user has cancelled the drift detection operation.

    - **LastDriftCheckTimestamp** *(datetime) --*

      Most recent time when CloudFormation performed a drift detection operation on the stack
      set. This value will be ``NULL`` for any stack set on which drift detection has not yet
      been performed.

    - **TotalStackInstancesCount** *(integer) --*

      The total number of stack instances belonging to this stack set.

      The total number of stack instances is equal to the total of:

      * Stack instances that match the stack set configuration.

      * Stack instances that have drifted from the stack set configuration.

      * Stack instances where the drift detection operation has failed.

      * Stack instances currently being checked for drift.

    - **DriftedStackInstancesCount** *(integer) --*

      The number of stack instances that have drifted from the expected template and parameter
      configuration of the stack set. A stack instance is considered to have drifted if one or
      more of the resources in the associated stack do not match their expected configuration.

    - **InSyncStackInstancesCount** *(integer) --*

      The number of stack instances which match the expected template and parameter
      configuration of the stack set.

    - **InProgressStackInstancesCount** *(integer) --*

      The number of stack instances that are currently being checked for drift.

    - **FailedStackInstancesCount** *(integer) --*

      The number of stack instances for which the drift detection operation failed.
    """


_ClientDescribeStackSetOperationResponseStackSetOperationTypeDef = TypedDict(
    "_ClientDescribeStackSetOperationResponseStackSetOperationTypeDef",
    {
        "OperationId": str,
        "StackSetId": str,
        "Action": str,
        "Status": str,
        "OperationPreferences": ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef,
        "RetainStacks": bool,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
        "StackSetDriftDetectionDetails": ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef,
    },
    total=False,
)


class ClientDescribeStackSetOperationResponseStackSetOperationTypeDef(
    _ClientDescribeStackSetOperationResponseStackSetOperationTypeDef
):
    """
    Type definition for `ClientDescribeStackSetOperationResponse` `StackSetOperation`

    The specified stack set operation.

    - **OperationId** *(string) --*

      The unique ID of a stack set operation.

    - **StackSetId** *(string) --*

      The ID of the stack set.

    - **Action** *(string) --*

      The type of stack set operation: ``CREATE`` , ``UPDATE`` , or ``DELETE`` . Create and
      delete operations affect only the specified stack set instances that are associated with
      the specified stack set. Update operations affect both the stack set itself, as well as
      *all* associated stack set instances.

    - **Status** *(string) --*

      The status of the operation.

      * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure
      tolerance value that you've set for an operation is applied for each region during stack
      create and update operations. If the number of failed stacks within a region exceeds the
      failure tolerance, the status of the operation in the region is set to ``FAILED`` . This in
      turn sets the status of the operation as a whole to ``FAILED`` , and AWS CloudFormation
      cancels the operation in any remaining regions.

      * ``RUNNING`` : The operation is currently being performed.

      * ``STOPPED`` : The user has cancelled the operation.

      * ``STOPPING`` : The operation is in the process of stopping, at user request.

      * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks
      without exceeding the failure tolerance for the operation.

    - **OperationPreferences** *(dict) --*

      The preferences for how AWS CloudFormation performs this stack set operation.

      - **RegionOrder** *(list) --*

        The order of the regions in where you want to perform the stack operation.

        - *(string) --*

      - **FailureToleranceCount** *(integer) --*

        The number of accounts, per region, for which this operation can fail before AWS
        CloudFormation stops the operation in that region. If the operation is stopped in a
        region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.

        Conditional: You must specify either ``FailureToleranceCount`` or
        ``FailureTolerancePercentage`` (but not both).

      - **FailureTolerancePercentage** *(integer) --*

        The percentage of accounts, per region, for which this stack operation can fail before
        AWS CloudFormation stops the operation in that region. If the operation is stopped in a
        region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.

        When calculating the number of accounts based on the specified percentage, AWS
        CloudFormation rounds *down* to the next whole number.

        Conditional: You must specify either ``FailureToleranceCount`` or
        ``FailureTolerancePercentage`` , but not both.

      - **MaxConcurrentCount** *(integer) --*

        The maximum number of accounts in which to perform this operation at one time. This is
        dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most
        one more than the ``FailureToleranceCount`` .

        Note that this setting lets you specify the *maximum* for operations. For large
        deployments, under certain circumstances the actual number of accounts acted upon
        concurrently may be lower due to service throttling.

        Conditional: You must specify either ``MaxConcurrentCount`` or
        ``MaxConcurrentPercentage`` , but not both.

      - **MaxConcurrentPercentage** *(integer) --*

        The maximum percentage of accounts in which to perform this operation at one time.

        When calculating the number of accounts based on the specified percentage, AWS
        CloudFormation rounds down to the next whole number. This is true except in cases where
        rounding down would result is zero. In this case, CloudFormation sets the number as one
        instead.

        Note that this setting lets you specify the *maximum* for operations. For large
        deployments, under certain circumstances the actual number of accounts acted upon
        concurrently may be lower due to service throttling.

        Conditional: You must specify either ``MaxConcurrentCount`` or
        ``MaxConcurrentPercentage`` , but not both.

    - **RetainStacks** *(boolean) --*

      For stack set operations of action type ``DELETE`` , specifies whether to remove the stack
      instances from the specified stack set, but doesn't delete the stacks. You can't
      reassociate a retained stack, or add an existing, saved stack to a new stack set.

    - **AdministrationRoleARN** *(string) --*

      The Amazon Resource Number (ARN) of the IAM role used to perform this stack set operation.

      Use customized administrator roles to control which users or groups can manage specific
      stack sets within the same administrator account. For more information, see `Define
      Permissions for Multiple Administrators
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`__
      in the *AWS CloudFormation User Guide* .

    - **ExecutionRoleName** *(string) --*

      The name of the IAM execution role used to create or update the stack set.

      Use customized execution roles to control which stack resources users and groups can
      include in their stack sets.

    - **CreationTimestamp** *(datetime) --*

      The time at which the operation was initiated. Note that the creation times for the stack
      set operation might differ from the creation time of the individual stacks themselves. This
      is because AWS CloudFormation needs to perform preparatory work for the operation, such as
      dispatching the work to the requested regions, before actually creating the first stacks.

    - **EndTimestamp** *(datetime) --*

      The time at which the stack set operation ended, across all accounts and regions specified.
      Note that this doesn't necessarily mean that the stack set operation was successful, or
      even attempted, in each account or region.

    - **StackSetDriftDetectionDetails** *(dict) --*

      Detailed information about the drift status of the stack set. This includes information
      about drift operations currently being performed on the stack set.

      this information will only be present for stack set operations whose ``Action`` type is
      ``DETECT_DRIFT`` .

      For more information, see `Detecting Unmanaged Changes in Stack Sets
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html>`__ in
      the AWS CloudFormation User Guide.

      - **DriftStatus** *(string) --*

        Status of the stack set's actual configuration compared to its expected template and
        parameter configuration. A stack set is considered to have drifted if one or more of its
        stack instances have drifted from their expected template and parameter configuration.

        * ``DRIFTED`` : One or more of the stack instances belonging to the stack set stack
        differs from the expected template and parameter configuration. A stack instance is
        considered to have drifted if one or more of the resources in the associated stack have
        drifted.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked the stack set for drift.

        * ``IN_SYNC`` : All of the stack instances belonging to the stack set stack match from
        the expected template and parameter configuration.

      - **DriftDetectionStatus** *(string) --*

        The status of the stack set drift detection operation.

        * ``COMPLETED`` : The drift detection operation completed without failing on any stack
        instances.

        * ``FAILED`` : The drift detection operation exceeded the specified failure tolerance.

        * ``PARTIAL_SUCCESS`` : The drift detection operation completed without exceeding the
        failure tolerance for the operation.

        * ``IN_PROGRESS`` : The drift detection operation is currently being performed.

        * ``STOPPED`` : The user has cancelled the drift detection operation.

      - **LastDriftCheckTimestamp** *(datetime) --*

        Most recent time when CloudFormation performed a drift detection operation on the stack
        set. This value will be ``NULL`` for any stack set on which drift detection has not yet
        been performed.

      - **TotalStackInstancesCount** *(integer) --*

        The total number of stack instances belonging to this stack set.

        The total number of stack instances is equal to the total of:

        * Stack instances that match the stack set configuration.

        * Stack instances that have drifted from the stack set configuration.

        * Stack instances where the drift detection operation has failed.

        * Stack instances currently being checked for drift.

      - **DriftedStackInstancesCount** *(integer) --*

        The number of stack instances that have drifted from the expected template and parameter
        configuration of the stack set. A stack instance is considered to have drifted if one or
        more of the resources in the associated stack do not match their expected configuration.

      - **InSyncStackInstancesCount** *(integer) --*

        The number of stack instances which match the expected template and parameter
        configuration of the stack set.

      - **InProgressStackInstancesCount** *(integer) --*

        The number of stack instances that are currently being checked for drift.

      - **FailedStackInstancesCount** *(integer) --*

        The number of stack instances for which the drift detection operation failed.
    """


_ClientDescribeStackSetOperationResponseTypeDef = TypedDict(
    "_ClientDescribeStackSetOperationResponseTypeDef",
    {
        "StackSetOperation": ClientDescribeStackSetOperationResponseStackSetOperationTypeDef
    },
    total=False,
)


class ClientDescribeStackSetOperationResponseTypeDef(
    _ClientDescribeStackSetOperationResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackSetOperation` `Response`

    - **StackSetOperation** *(dict) --*

      The specified stack set operation.

      - **OperationId** *(string) --*

        The unique ID of a stack set operation.

      - **StackSetId** *(string) --*

        The ID of the stack set.

      - **Action** *(string) --*

        The type of stack set operation: ``CREATE`` , ``UPDATE`` , or ``DELETE`` . Create and
        delete operations affect only the specified stack set instances that are associated with
        the specified stack set. Update operations affect both the stack set itself, as well as
        *all* associated stack set instances.

      - **Status** *(string) --*

        The status of the operation.

        * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure
        tolerance value that you've set for an operation is applied for each region during stack
        create and update operations. If the number of failed stacks within a region exceeds the
        failure tolerance, the status of the operation in the region is set to ``FAILED`` . This in
        turn sets the status of the operation as a whole to ``FAILED`` , and AWS CloudFormation
        cancels the operation in any remaining regions.

        * ``RUNNING`` : The operation is currently being performed.

        * ``STOPPED`` : The user has cancelled the operation.

        * ``STOPPING`` : The operation is in the process of stopping, at user request.

        * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks
        without exceeding the failure tolerance for the operation.

      - **OperationPreferences** *(dict) --*

        The preferences for how AWS CloudFormation performs this stack set operation.

        - **RegionOrder** *(list) --*

          The order of the regions in where you want to perform the stack operation.

          - *(string) --*

        - **FailureToleranceCount** *(integer) --*

          The number of accounts, per region, for which this operation can fail before AWS
          CloudFormation stops the operation in that region. If the operation is stopped in a
          region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.

          Conditional: You must specify either ``FailureToleranceCount`` or
          ``FailureTolerancePercentage`` (but not both).

        - **FailureTolerancePercentage** *(integer) --*

          The percentage of accounts, per region, for which this stack operation can fail before
          AWS CloudFormation stops the operation in that region. If the operation is stopped in a
          region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.

          When calculating the number of accounts based on the specified percentage, AWS
          CloudFormation rounds *down* to the next whole number.

          Conditional: You must specify either ``FailureToleranceCount`` or
          ``FailureTolerancePercentage`` , but not both.

        - **MaxConcurrentCount** *(integer) --*

          The maximum number of accounts in which to perform this operation at one time. This is
          dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most
          one more than the ``FailureToleranceCount`` .

          Note that this setting lets you specify the *maximum* for operations. For large
          deployments, under certain circumstances the actual number of accounts acted upon
          concurrently may be lower due to service throttling.

          Conditional: You must specify either ``MaxConcurrentCount`` or
          ``MaxConcurrentPercentage`` , but not both.

        - **MaxConcurrentPercentage** *(integer) --*

          The maximum percentage of accounts in which to perform this operation at one time.

          When calculating the number of accounts based on the specified percentage, AWS
          CloudFormation rounds down to the next whole number. This is true except in cases where
          rounding down would result is zero. In this case, CloudFormation sets the number as one
          instead.

          Note that this setting lets you specify the *maximum* for operations. For large
          deployments, under certain circumstances the actual number of accounts acted upon
          concurrently may be lower due to service throttling.

          Conditional: You must specify either ``MaxConcurrentCount`` or
          ``MaxConcurrentPercentage`` , but not both.

      - **RetainStacks** *(boolean) --*

        For stack set operations of action type ``DELETE`` , specifies whether to remove the stack
        instances from the specified stack set, but doesn't delete the stacks. You can't
        reassociate a retained stack, or add an existing, saved stack to a new stack set.

      - **AdministrationRoleARN** *(string) --*

        The Amazon Resource Number (ARN) of the IAM role used to perform this stack set operation.

        Use customized administrator roles to control which users or groups can manage specific
        stack sets within the same administrator account. For more information, see `Define
        Permissions for Multiple Administrators
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`__
        in the *AWS CloudFormation User Guide* .

      - **ExecutionRoleName** *(string) --*

        The name of the IAM execution role used to create or update the stack set.

        Use customized execution roles to control which stack resources users and groups can
        include in their stack sets.

      - **CreationTimestamp** *(datetime) --*

        The time at which the operation was initiated. Note that the creation times for the stack
        set operation might differ from the creation time of the individual stacks themselves. This
        is because AWS CloudFormation needs to perform preparatory work for the operation, such as
        dispatching the work to the requested regions, before actually creating the first stacks.

      - **EndTimestamp** *(datetime) --*

        The time at which the stack set operation ended, across all accounts and regions specified.
        Note that this doesn't necessarily mean that the stack set operation was successful, or
        even attempted, in each account or region.

      - **StackSetDriftDetectionDetails** *(dict) --*

        Detailed information about the drift status of the stack set. This includes information
        about drift operations currently being performed on the stack set.

        this information will only be present for stack set operations whose ``Action`` type is
        ``DETECT_DRIFT`` .

        For more information, see `Detecting Unmanaged Changes in Stack Sets
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html>`__ in
        the AWS CloudFormation User Guide.

        - **DriftStatus** *(string) --*

          Status of the stack set's actual configuration compared to its expected template and
          parameter configuration. A stack set is considered to have drifted if one or more of its
          stack instances have drifted from their expected template and parameter configuration.

          * ``DRIFTED`` : One or more of the stack instances belonging to the stack set stack
          differs from the expected template and parameter configuration. A stack instance is
          considered to have drifted if one or more of the resources in the associated stack have
          drifted.

          * ``NOT_CHECKED`` : AWS CloudFormation has not checked the stack set for drift.

          * ``IN_SYNC`` : All of the stack instances belonging to the stack set stack match from
          the expected template and parameter configuration.

        - **DriftDetectionStatus** *(string) --*

          The status of the stack set drift detection operation.

          * ``COMPLETED`` : The drift detection operation completed without failing on any stack
          instances.

          * ``FAILED`` : The drift detection operation exceeded the specified failure tolerance.

          * ``PARTIAL_SUCCESS`` : The drift detection operation completed without exceeding the
          failure tolerance for the operation.

          * ``IN_PROGRESS`` : The drift detection operation is currently being performed.

          * ``STOPPED`` : The user has cancelled the drift detection operation.

        - **LastDriftCheckTimestamp** *(datetime) --*

          Most recent time when CloudFormation performed a drift detection operation on the stack
          set. This value will be ``NULL`` for any stack set on which drift detection has not yet
          been performed.

        - **TotalStackInstancesCount** *(integer) --*

          The total number of stack instances belonging to this stack set.

          The total number of stack instances is equal to the total of:

          * Stack instances that match the stack set configuration.

          * Stack instances that have drifted from the stack set configuration.

          * Stack instances where the drift detection operation has failed.

          * Stack instances currently being checked for drift.

        - **DriftedStackInstancesCount** *(integer) --*

          The number of stack instances that have drifted from the expected template and parameter
          configuration of the stack set. A stack instance is considered to have drifted if one or
          more of the resources in the associated stack do not match their expected configuration.

        - **InSyncStackInstancesCount** *(integer) --*

          The number of stack instances which match the expected template and parameter
          configuration of the stack set.

        - **InProgressStackInstancesCount** *(integer) --*

          The number of stack instances that are currently being checked for drift.

        - **FailedStackInstancesCount** *(integer) --*

          The number of stack instances for which the drift detection operation failed.
    """


_ClientDescribeStacksResponseStacksDriftInformationTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksDriftInformationTypeDef",
    {"StackDriftStatus": str, "LastCheckTimestamp": datetime},
    total=False,
)


class ClientDescribeStacksResponseStacksDriftInformationTypeDef(
    _ClientDescribeStacksResponseStacksDriftInformationTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `DriftInformation`

    Information on whether a stack's actual configuration differs, or has *drifted* , from
    it's expected configuration, as defined in the stack template and any values specified as
    template parameters. For more information, see `Detecting Unregulated Configuration
    Changes to Stacks and Resources
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **StackDriftStatus** *(string) --*

      Status of the stack's actual configuration compared to its expected template
      configuration.

      * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
      considered to have drifted if one or more of its resources have drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
      expected template configuration.

      * ``IN_SYNC`` : The stack's actual configuration matches its expected template
      configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastCheckTimestamp** *(datetime) --*

      Most recent time when a drift detection operation was initiated on the stack, or any of
      its individual resources that support drift detection.
    """


_ClientDescribeStacksResponseStacksOutputsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)


class ClientDescribeStacksResponseStacksOutputsTypeDef(
    _ClientDescribeStacksResponseStacksOutputsTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `Outputs`

    The Output data type.

    - **OutputKey** *(string) --*

      The key associated with the output.

    - **OutputValue** *(string) --*

      The value associated with the output.

    - **Description** *(string) --*

      User defined description associated with the output.

    - **ExportName** *(string) --*

      The name of the export associated with the output.
    """


_ClientDescribeStacksResponseStacksParametersTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksParametersTypeDef(
    _ClientDescribeStacksResponseStacksParametersTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a
      particular parameter, AWS CloudFormation uses the default value that is specified in
      your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a
      given parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field
      is returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef(
    _ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacksRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of
    stacks. If any of the alarms you specify goes to ALARM state during the stack
    operation or within the specified monitoring period afterwards, CloudFormation rolls
    back the entire stack operation.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled
      back.

    - **Type** *(string) --*

      The resource type of the rollback trigger. Currently,
      `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef(
    _ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and
    updating operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and
      applies them to any subsequent update operations for the stack, unless you specify
      otherwise. If you do specify rollback triggers for this parameter, those triggers
      replace any list of triggers previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't
      specify this parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that
      you want used for this stack, even triggers you've specifed before (for example, when
      creating the stack or during a previous stack update). Any triggers that you don't
      include in the updated list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of
        stacks. If any of the alarms you specify goes to ALARM state during the stack
        operation or within the specified monitoring period afterwards, CloudFormation rolls
        back the entire stack operation.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled
          back.

        - **Type** *(string) --*

          The resource type of the rollback trigger. Currently,
          `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the
      rollback triggers after the stack creation or update operation deploys all necessary
      resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers,
      CloudFormation still waits the specified period of time before cleaning up old
      resources after update operations. You can use this monitoring period to perform any
      manual stack validation desired, and manually cancel the stack creation or update
      (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified
      rollback triggers during stack creation and update operations. Then, for update
      operations, it begins disposing of old resources immediately once the operation
      completes.
    """


_ClientDescribeStacksResponseStacksTagsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeStacksResponseStacksTagsTypeDef(
    _ClientDescribeStacksResponseStacksTagsTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store
    information about an AWS CloudFormation stack.

    - **Key** *(string) --*

       *Required* . A string used to identify this tag. You can specify a maximum of 128
       characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
       prefix: ``aws:`` .

    - **Value** *(string) --*

       *Required* . A string containing the value for this tag. You can specify a maximum
       of 256 characters for a tag value.
    """


_ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List[ClientDescribeStacksResponseStacksParametersTypeDef],
        "CreationTime": datetime,
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef,
        "StackStatus": str,
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[str],
        "Outputs": List[ClientDescribeStacksResponseStacksOutputsTypeDef],
        "RoleARN": str,
        "Tags": List[ClientDescribeStacksResponseStacksTagsTypeDef],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ClientDescribeStacksResponseStacksDriftInformationTypeDef,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksTypeDef(
    _ClientDescribeStacksResponseStacksTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponse` `Stacks`

    The Stack data type.

    - **StackId** *(string) --*

      Unique identifier of the stack.

    - **StackName** *(string) --*

      The name associated with the stack.

    - **ChangeSetId** *(string) --*

      The unique ID of the change set.

    - **Description** *(string) --*

      A user-defined description associated with the stack.

    - **Parameters** *(list) --*

      A list of ``Parameter`` structures.

      - *(dict) --*

        The Parameter data type.

        - **ParameterKey** *(string) --*

          The key associated with the parameter. If you don't specify a key and value for a
          particular parameter, AWS CloudFormation uses the default value that is specified in
          your template.

        - **ParameterValue** *(string) --*

          The input value associated with the parameter.

        - **UsePreviousValue** *(boolean) --*

          During a stack update, use the existing parameter value that the stack is using for a
          given parameter key. If you specify ``true`` , do not specify a parameter value.

        - **ResolvedValue** *(string) --*

          Read-only. The value that corresponds to a Systems Manager parameter key. This field
          is returned only for ` ``SSM`` parameter types
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
          in the template.

    - **CreationTime** *(datetime) --*

      The time at which the stack was created.

    - **DeletionTime** *(datetime) --*

      The time the stack was deleted.

    - **LastUpdatedTime** *(datetime) --*

      The time the stack was last updated. This field will only be returned if the stack has
      been updated at least once.

    - **RollbackConfiguration** *(dict) --*

      The rollback triggers for AWS CloudFormation to monitor during stack creation and
      updating operations, and for the specified monitoring period afterwards.

      - **RollbackTriggers** *(list) --*

        The triggers to monitor during stack creation or update actions.

        By default, AWS CloudFormation saves the rollback triggers specified for a stack and
        applies them to any subsequent update operations for the stack, unless you specify
        otherwise. If you do specify rollback triggers for this parameter, those triggers
        replace any list of triggers previously specified for the stack. This means:

        * To use the rollback triggers previously specified for this stack, if any, don't
        specify this parameter.

        * To specify new or updated rollback triggers, you must specify *all* the triggers that
        you want used for this stack, even triggers you've specifed before (for example, when
        creating the stack or during a previous stack update). Any triggers that you don't
        include in the updated list of triggers are no longer applied to the stack.

        * To remove all currently specified triggers, specify an empty list for this parameter.

        If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - *(dict) --*

          A rollback trigger AWS CloudFormation monitors during creation and updating of
          stacks. If any of the alarms you specify goes to ALARM state during the stack
          operation or within the specified monitoring period afterwards, CloudFormation rolls
          back the entire stack operation.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the rollback trigger.

            If a specified trigger is missing, the entire stack operation fails and is rolled
            back.

          - **Type** *(string) --*

            The resource type of the rollback trigger. Currently,
            `AWS\\:\\:CloudWatch\\:\\:Alarm
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
            is the only supported resource type.

      - **MonitoringTimeInMinutes** *(integer) --*

        The amount of time, in minutes, during which CloudFormation should monitor all the
        rollback triggers after the stack creation or update operation deploys all necessary
        resources.

        The default is 0 minutes.

        If you specify a monitoring period but do not specify any rollback triggers,
        CloudFormation still waits the specified period of time before cleaning up old
        resources after update operations. You can use this monitoring period to perform any
        manual stack validation desired, and manually cancel the stack creation or update
        (using `CancelUpdateStack
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
        , for example) as necessary.

        If you specify 0 for this parameter, CloudFormation still monitors the specified
        rollback triggers during stack creation and update operations. Then, for update
        operations, it begins disposing of old resources immediately once the operation
        completes.

    - **StackStatus** *(string) --*

      Current status of the stack.

    - **StackStatusReason** *(string) --*

      Success/failure message associated with the stack status.

    - **DisableRollback** *(boolean) --*

      Boolean to enable or disable rollback on stack creation failures:

      * ``true`` : disable rollback

      * ``false`` : enable rollback

    - **NotificationARNs** *(list) --*

      SNS topic ARNs to which stack related events are published.

      - *(string) --*

    - **TimeoutInMinutes** *(integer) --*

      The amount of time within which stack creation should complete.

    - **Capabilities** *(list) --*

      The capabilities allowed in the stack.

      - *(string) --*

    - **Outputs** *(list) --*

      A list of output structures.

      - *(dict) --*

        The Output data type.

        - **OutputKey** *(string) --*

          The key associated with the output.

        - **OutputValue** *(string) --*

          The value associated with the output.

        - **Description** *(string) --*

          User defined description associated with the output.

        - **ExportName** *(string) --*

          The name of the export associated with the output.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that
      is associated with the stack. During a stack operation, AWS CloudFormation uses this
      role's credentials to make calls on your behalf.

    - **Tags** *(list) --*

      A list of ``Tag`` s that specify information about the stack.

      - *(dict) --*

        The Tag type enables you to specify a key-value pair that can be used to store
        information about an AWS CloudFormation stack.

        - **Key** *(string) --*

           *Required* . A string used to identify this tag. You can specify a maximum of 128
           characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
           prefix: ``aws:`` .

        - **Value** *(string) --*

           *Required* . A string containing the value for this tag. You can specify a maximum
           of 256 characters for a tag value.

    - **EnableTerminationProtection** *(boolean) --*

      Whether termination protection is enabled for the stack.

      For `nested stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      , termination protection is set on the root stack and cannot be changed directly on the
      nested stack. For more information, see `Protecting a Stack From Being Deleted
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **ParentId** *(string) --*

      For nested stacks--stacks created as resources for another stack--the stack ID of the
      direct parent of this stack. For the first level of nested stacks, the root stack is also
      the parent stack.

      For more information, see `Working with Nested Stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **RootId** *(string) --*

      For nested stacks--stacks created as resources for another stack--the stack ID of the
      top-level stack to which the nested stack ultimately belongs.

      For more information, see `Working with Nested Stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **DriftInformation** *(dict) --*

      Information on whether a stack's actual configuration differs, or has *drifted* , from
      it's expected configuration, as defined in the stack template and any values specified as
      template parameters. For more information, see `Detecting Unregulated Configuration
      Changes to Stacks and Resources
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .

      - **StackDriftStatus** *(string) --*

        Status of the stack's actual configuration compared to its expected template
        configuration.

        * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
        considered to have drifted if one or more of its resources have drifted.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
        expected template configuration.

        * ``IN_SYNC`` : The stack's actual configuration matches its expected template
        configuration.

        * ``UNKNOWN`` : This value is reserved for future use.

      - **LastCheckTimestamp** *(datetime) --*

        Most recent time when a drift detection operation was initiated on the stack, or any of
        its individual resources that support drift detection.
    """


_ClientDescribeStacksResponseTypeDef = TypedDict(
    "_ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeStacksResponseTypeDef(_ClientDescribeStacksResponseTypeDef):
    """
    Type definition for `ClientDescribeStacks` `Response`

    The output for a  DescribeStacks action.

    - **Stacks** *(list) --*

      A list of stack structures.

      - *(dict) --*

        The Stack data type.

        - **StackId** *(string) --*

          Unique identifier of the stack.

        - **StackName** *(string) --*

          The name associated with the stack.

        - **ChangeSetId** *(string) --*

          The unique ID of the change set.

        - **Description** *(string) --*

          A user-defined description associated with the stack.

        - **Parameters** *(list) --*

          A list of ``Parameter`` structures.

          - *(dict) --*

            The Parameter data type.

            - **ParameterKey** *(string) --*

              The key associated with the parameter. If you don't specify a key and value for a
              particular parameter, AWS CloudFormation uses the default value that is specified in
              your template.

            - **ParameterValue** *(string) --*

              The input value associated with the parameter.

            - **UsePreviousValue** *(boolean) --*

              During a stack update, use the existing parameter value that the stack is using for a
              given parameter key. If you specify ``true`` , do not specify a parameter value.

            - **ResolvedValue** *(string) --*

              Read-only. The value that corresponds to a Systems Manager parameter key. This field
              is returned only for ` ``SSM`` parameter types
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
              in the template.

        - **CreationTime** *(datetime) --*

          The time at which the stack was created.

        - **DeletionTime** *(datetime) --*

          The time the stack was deleted.

        - **LastUpdatedTime** *(datetime) --*

          The time the stack was last updated. This field will only be returned if the stack has
          been updated at least once.

        - **RollbackConfiguration** *(dict) --*

          The rollback triggers for AWS CloudFormation to monitor during stack creation and
          updating operations, and for the specified monitoring period afterwards.

          - **RollbackTriggers** *(list) --*

            The triggers to monitor during stack creation or update actions.

            By default, AWS CloudFormation saves the rollback triggers specified for a stack and
            applies them to any subsequent update operations for the stack, unless you specify
            otherwise. If you do specify rollback triggers for this parameter, those triggers
            replace any list of triggers previously specified for the stack. This means:

            * To use the rollback triggers previously specified for this stack, if any, don't
            specify this parameter.

            * To specify new or updated rollback triggers, you must specify *all* the triggers that
            you want used for this stack, even triggers you've specifed before (for example, when
            creating the stack or during a previous stack update). Any triggers that you don't
            include in the updated list of triggers are no longer applied to the stack.

            * To remove all currently specified triggers, specify an empty list for this parameter.

            If a specified trigger is missing, the entire stack operation fails and is rolled back.

            - *(dict) --*

              A rollback trigger AWS CloudFormation monitors during creation and updating of
              stacks. If any of the alarms you specify goes to ALARM state during the stack
              operation or within the specified monitoring period afterwards, CloudFormation rolls
              back the entire stack operation.

              - **Arn** *(string) --*

                The Amazon Resource Name (ARN) of the rollback trigger.

                If a specified trigger is missing, the entire stack operation fails and is rolled
                back.

              - **Type** *(string) --*

                The resource type of the rollback trigger. Currently,
                `AWS\\:\\:CloudWatch\\:\\:Alarm
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
                is the only supported resource type.

          - **MonitoringTimeInMinutes** *(integer) --*

            The amount of time, in minutes, during which CloudFormation should monitor all the
            rollback triggers after the stack creation or update operation deploys all necessary
            resources.

            The default is 0 minutes.

            If you specify a monitoring period but do not specify any rollback triggers,
            CloudFormation still waits the specified period of time before cleaning up old
            resources after update operations. You can use this monitoring period to perform any
            manual stack validation desired, and manually cancel the stack creation or update
            (using `CancelUpdateStack
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
            , for example) as necessary.

            If you specify 0 for this parameter, CloudFormation still monitors the specified
            rollback triggers during stack creation and update operations. Then, for update
            operations, it begins disposing of old resources immediately once the operation
            completes.

        - **StackStatus** *(string) --*

          Current status of the stack.

        - **StackStatusReason** *(string) --*

          Success/failure message associated with the stack status.

        - **DisableRollback** *(boolean) --*

          Boolean to enable or disable rollback on stack creation failures:

          * ``true`` : disable rollback

          * ``false`` : enable rollback

        - **NotificationARNs** *(list) --*

          SNS topic ARNs to which stack related events are published.

          - *(string) --*

        - **TimeoutInMinutes** *(integer) --*

          The amount of time within which stack creation should complete.

        - **Capabilities** *(list) --*

          The capabilities allowed in the stack.

          - *(string) --*

        - **Outputs** *(list) --*

          A list of output structures.

          - *(dict) --*

            The Output data type.

            - **OutputKey** *(string) --*

              The key associated with the output.

            - **OutputValue** *(string) --*

              The value associated with the output.

            - **Description** *(string) --*

              User defined description associated with the output.

            - **ExportName** *(string) --*

              The name of the export associated with the output.

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that
          is associated with the stack. During a stack operation, AWS CloudFormation uses this
          role's credentials to make calls on your behalf.

        - **Tags** *(list) --*

          A list of ``Tag`` s that specify information about the stack.

          - *(dict) --*

            The Tag type enables you to specify a key-value pair that can be used to store
            information about an AWS CloudFormation stack.

            - **Key** *(string) --*

               *Required* . A string used to identify this tag. You can specify a maximum of 128
               characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
               prefix: ``aws:`` .

            - **Value** *(string) --*

               *Required* . A string containing the value for this tag. You can specify a maximum
               of 256 characters for a tag value.

        - **EnableTerminationProtection** *(boolean) --*

          Whether termination protection is enabled for the stack.

          For `nested stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          , termination protection is set on the root stack and cannot be changed directly on the
          nested stack. For more information, see `Protecting a Stack From Being Deleted
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **ParentId** *(string) --*

          For nested stacks--stacks created as resources for another stack--the stack ID of the
          direct parent of this stack. For the first level of nested stacks, the root stack is also
          the parent stack.

          For more information, see `Working with Nested Stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **RootId** *(string) --*

          For nested stacks--stacks created as resources for another stack--the stack ID of the
          top-level stack to which the nested stack ultimately belongs.

          For more information, see `Working with Nested Stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **DriftInformation** *(dict) --*

          Information on whether a stack's actual configuration differs, or has *drifted* , from
          it's expected configuration, as defined in the stack template and any values specified as
          template parameters. For more information, see `Detecting Unregulated Configuration
          Changes to Stacks and Resources
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .

          - **StackDriftStatus** *(string) --*

            Status of the stack's actual configuration compared to its expected template
            configuration.

            * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
            considered to have drifted if one or more of its resources have drifted.

            * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
            expected template configuration.

            * ``IN_SYNC`` : The stack's actual configuration matches its expected template
            configuration.

            * ``UNKNOWN`` : This value is reserved for future use.

          - **LastCheckTimestamp** *(datetime) --*

            Most recent time when a drift detection operation was initiated on the stack, or any of
            its individual resources that support drift detection.

    - **NextToken** *(string) --*

      If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no
      additional page exists, this value is null.
    """


_ClientDescribeTypeRegistrationResponseTypeDef = TypedDict(
    "_ClientDescribeTypeRegistrationResponseTypeDef",
    {"ProgressStatus": str, "Description": str, "TypeArn": str, "TypeVersionArn": str},
    total=False,
)


class ClientDescribeTypeRegistrationResponseTypeDef(
    _ClientDescribeTypeRegistrationResponseTypeDef
):
    """
    Type definition for `ClientDescribeTypeRegistration` `Response`

    - **ProgressStatus** *(string) --*

      The current status of the type registration request.

    - **Description** *(string) --*

      The description of the type registration request.

    - **TypeArn** *(string) --*

      The Amazon Resource Name (ARN) of the type being registered.

      For registration requests with a ``ProgressStatus`` of other than ``COMPLETE`` , this will be
      ``null`` .

    - **TypeVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of this specific version of the type being registered.

      For registration requests with a ``ProgressStatus`` of other than ``COMPLETE`` , this will be
      ``null`` .
    """


_ClientDescribeTypeResponseLoggingConfigTypeDef = TypedDict(
    "_ClientDescribeTypeResponseLoggingConfigTypeDef",
    {"LogRoleArn": str, "LogGroupName": str},
    total=False,
)


class ClientDescribeTypeResponseLoggingConfigTypeDef(
    _ClientDescribeTypeResponseLoggingConfigTypeDef
):
    """
    Type definition for `ClientDescribeTypeResponse` `LoggingConfig`

    Contains logging configuration information for a type.

    - **LogRoleArn** *(string) --*

      The ARN of the role that CloudFormation should assume when sending log entries to
      CloudWatch logs.

    - **LogGroupName** *(string) --*

      The Amazon CloudWatch log group to which CloudFormation sends error logging information
      when invoking the type's handlers.
    """


_ClientDescribeTypeResponseTypeDef = TypedDict(
    "_ClientDescribeTypeResponseTypeDef",
    {
        "Arn": str,
        "Type": str,
        "TypeName": str,
        "DefaultVersionId": str,
        "Description": str,
        "Schema": str,
        "ProvisioningType": str,
        "DeprecatedStatus": str,
        "LoggingConfig": ClientDescribeTypeResponseLoggingConfigTypeDef,
        "ExecutionRoleArn": str,
        "Visibility": str,
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
    },
    total=False,
)


class ClientDescribeTypeResponseTypeDef(_ClientDescribeTypeResponseTypeDef):
    """
    Type definition for `ClientDescribeType` `Response`

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the type.

    - **Type** *(string) --*

      The kind of type.

      Currently the only valid value is ``RESOURCE`` .

    - **TypeName** *(string) --*

      The name of the registered type.

    - **DefaultVersionId** *(string) --*

      The ID of the default version of the type. The default version is used when the type version
      is not specified.

      To set the default version of a type, use ``  SetTypeDefaultVersion `` .

    - **Description** *(string) --*

      The description of the registered type.

    - **Schema** *(string) --*

      The schema that defines the type.

      For more information on type schemas, see `Resource Provider Schema
      <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html>`__
      in the *CloudFormation CLI User Guide* .

    - **ProvisioningType** *(string) --*

      The provisioning behavior of the type. AWS CloudFormation determines the provisioning type
      during registration, based on the types of handlers in the schema handler package submitted.

      Valid values include:

      * ``FULLY_MUTABLE`` : The type includes an update handler to process updates to the type
      during stack update operations.

      * ``IMMUTABLE`` : The type does not include an update handler, so the type cannot be updated
      and must instead be replaced during stack update operations.

      * ``NON_PROVISIONABLE`` : The type does not include all of the following handlers, and
      therefore cannot actually be provisioned.

        * create

        * read

        * delete

    - **DeprecatedStatus** *(string) --*

      The deprecation status of the type.

      Valid values include:

      * ``LIVE`` : The type is registered and can be used in CloudFormation operations, dependent
      on its provisioning behavior and visibility scope.

      * ``DEPRECATED`` : The type has been deregistered and can no longer be used in CloudFormation
      operations.

    - **LoggingConfig** *(dict) --*

      Contains logging configuration information for a type.

      - **LogRoleArn** *(string) --*

        The ARN of the role that CloudFormation should assume when sending log entries to
        CloudWatch logs.

      - **LogGroupName** *(string) --*

        The Amazon CloudWatch log group to which CloudFormation sends error logging information
        when invoking the type's handlers.

    - **ExecutionRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM execution role used to register the type. If your
      resource type calls AWS APIs in any of its handlers, you must create an * `IAM execution role
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`__ * that includes the
      necessary permissions to call those AWS APIs, and provision that execution role in your
      account. CloudFormation then assumes that execution role to provide your resource type with
      the appropriate credentials.

    - **Visibility** *(string) --*

      The scope at which the type is visible and usable in CloudFormation operations.

      Valid values include:

      * ``PRIVATE`` : The type is only visible and usable within the account in which it is
      registered. Currently, AWS CloudFormation marks any types you register as ``PRIVATE`` .

      * ``PUBLIC`` : The type is publically visible and usable within any Amazon account.

    - **SourceUrl** *(string) --*

      The URL of the source code for the type.

    - **DocumentationUrl** *(string) --*

      The URL of a page providing detailed documentation for this type.

    - **LastUpdated** *(datetime) --*

      When the specified type version was registered.

    - **TimeCreated** *(datetime) --*

      When the specified type version was registered.
    """


_ClientDetectStackDriftResponseTypeDef = TypedDict(
    "_ClientDetectStackDriftResponseTypeDef",
    {"StackDriftDetectionId": str},
    total=False,
)


class ClientDetectStackDriftResponseTypeDef(_ClientDetectStackDriftResponseTypeDef):
    """
    Type definition for `ClientDetectStackDrift` `Response`

    - **StackDriftDetectionId** *(string) --*

      The ID of the drift detection results of this operation.

      AWS CloudFormation generates new results, with a new drift detection ID, each time this
      operation is run. However, the number of drift results AWS CloudFormation retains for any
      given stack, and for how long, may vary.
    """


_ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef = TypedDict(
    "_ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef(
    _ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef
):
    """
    Type definition for `ClientDetectStackResourceDriftResponseStackResourceDrift` `PhysicalResourceIdContext`

    Context information that enables AWS CloudFormation to uniquely identify a resource. AWS
    CloudFormation uses context key-value pairs in cases where a resource's logical and
    physical IDs are not enough to uniquely identify that resource. Each context key-value
    pair specifies a resource that contains the targeted resource.

    - **Key** *(string) --*

      The resource context key.

    - **Value** *(string) --*

      The resource context value.
    """


_ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef = TypedDict(
    "_ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": str,
    },
    total=False,
)


class ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef(
    _ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef
):
    """
    Type definition for `ClientDetectStackResourceDriftResponseStackResourceDrift` `PropertyDifferences`

    Information about a resource property whose actual value differs from its expected value,
    as defined in the stack template and any values specified as template parameters. These
    will be present only for resources whose ``StackResourceDriftStatus`` is ``MODIFIED`` .
    For more information, see `Detecting Unregulated Configuration Changes to Stacks and
    Resources
    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **PropertyPath** *(string) --*

      The fully-qualified path to the resource property.

    - **ExpectedValue** *(string) --*

      The expected property value of the resource property, as defined in the stack template
      and any values specified as template parameters.

    - **ActualValue** *(string) --*

      The actual property value of the resource property.

    - **DifferenceType** *(string) --*

      The type of property difference.

      * ``ADD`` : A value has been added to a resource property that is an array or list data
      type.

      * ``REMOVE`` : The property has been removed from the current resource configuration.

      * ``NOT_EQUAL`` : The current property value differs from its expected value (as
      defined in the stack template and any values specified as template parameters).
    """


_ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef = TypedDict(
    "_ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List[
            ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef
        ],
        "ResourceType": str,
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List[
            ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef
        ],
        "StackResourceDriftStatus": str,
        "Timestamp": datetime,
    },
    total=False,
)


class ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef(
    _ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef
):
    """
    Type definition for `ClientDetectStackResourceDriftResponse` `StackResourceDrift`

    Information about whether the resource's actual configuration has drifted from its expected
    template configuration, including actual and expected property values and any differences
    detected.

    - **StackId** *(string) --*

      The ID of the stack.

    - **LogicalResourceId** *(string) --*

      The logical name of the resource specified in the template.

    - **PhysicalResourceId** *(string) --*

      The name or unique identifier that corresponds to a physical instance ID of a resource
      supported by AWS CloudFormation.

    - **PhysicalResourceIdContext** *(list) --*

      Context information that enables AWS CloudFormation to uniquely identify a resource. AWS
      CloudFormation uses context key-value pairs in cases where a resource's logical and
      physical IDs are not enough to uniquely identify that resource. Each context key-value pair
      specifies a unique resource that contains the targeted resource.

      - *(dict) --*

        Context information that enables AWS CloudFormation to uniquely identify a resource. AWS
        CloudFormation uses context key-value pairs in cases where a resource's logical and
        physical IDs are not enough to uniquely identify that resource. Each context key-value
        pair specifies a resource that contains the targeted resource.

        - **Key** *(string) --*

          The resource context key.

        - **Value** *(string) --*

          The resource context value.

    - **ResourceType** *(string) --*

      The type of the resource.

    - **ExpectedProperties** *(string) --*

      A JSON structure containing the expected property values of the stack resource, as defined
      in the stack template and any values specified as template parameters.

      For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not
      be present.

    - **ActualProperties** *(string) --*

      A JSON structure containing the actual property values of the stack resource.

      For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not
      be present.

    - **PropertyDifferences** *(list) --*

      A collection of the resource properties whose actual values differ from their expected
      values. These will be present only for resources whose ``StackResourceDriftStatus`` is
      ``MODIFIED`` .

      - *(dict) --*

        Information about a resource property whose actual value differs from its expected value,
        as defined in the stack template and any values specified as template parameters. These
        will be present only for resources whose ``StackResourceDriftStatus`` is ``MODIFIED`` .
        For more information, see `Detecting Unregulated Configuration Changes to Stacks and
        Resources
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
        .

        - **PropertyPath** *(string) --*

          The fully-qualified path to the resource property.

        - **ExpectedValue** *(string) --*

          The expected property value of the resource property, as defined in the stack template
          and any values specified as template parameters.

        - **ActualValue** *(string) --*

          The actual property value of the resource property.

        - **DifferenceType** *(string) --*

          The type of property difference.

          * ``ADD`` : A value has been added to a resource property that is an array or list data
          type.

          * ``REMOVE`` : The property has been removed from the current resource configuration.

          * ``NOT_EQUAL`` : The current property value differs from its expected value (as
          defined in the stack template and any values specified as template parameters).

    - **StackResourceDriftStatus** *(string) --*

      Status of the resource's actual configuration compared to its expected configuration

      * ``DELETED`` : The resource differs from its expected template configuration because the
      resource has been deleted.

      * ``MODIFIED`` : One or more resource properties differ from their expected values (as
      defined in the stack template and any values specified as template parameters).

      * ``IN_SYNC`` : The resources's actual configuration matches its expected template
      configuration.

      * ``NOT_CHECKED`` : AWS CloudFormation does not currently return this value.

    - **Timestamp** *(datetime) --*

      Time at which AWS CloudFormation performed drift detection on the stack resource.
    """


_ClientDetectStackResourceDriftResponseTypeDef = TypedDict(
    "_ClientDetectStackResourceDriftResponseTypeDef",
    {
        "StackResourceDrift": ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef
    },
    total=False,
)


class ClientDetectStackResourceDriftResponseTypeDef(
    _ClientDetectStackResourceDriftResponseTypeDef
):
    """
    Type definition for `ClientDetectStackResourceDrift` `Response`

    - **StackResourceDrift** *(dict) --*

      Information about whether the resource's actual configuration has drifted from its expected
      template configuration, including actual and expected property values and any differences
      detected.

      - **StackId** *(string) --*

        The ID of the stack.

      - **LogicalResourceId** *(string) --*

        The logical name of the resource specified in the template.

      - **PhysicalResourceId** *(string) --*

        The name or unique identifier that corresponds to a physical instance ID of a resource
        supported by AWS CloudFormation.

      - **PhysicalResourceIdContext** *(list) --*

        Context information that enables AWS CloudFormation to uniquely identify a resource. AWS
        CloudFormation uses context key-value pairs in cases where a resource's logical and
        physical IDs are not enough to uniquely identify that resource. Each context key-value pair
        specifies a unique resource that contains the targeted resource.

        - *(dict) --*

          Context information that enables AWS CloudFormation to uniquely identify a resource. AWS
          CloudFormation uses context key-value pairs in cases where a resource's logical and
          physical IDs are not enough to uniquely identify that resource. Each context key-value
          pair specifies a resource that contains the targeted resource.

          - **Key** *(string) --*

            The resource context key.

          - **Value** *(string) --*

            The resource context value.

      - **ResourceType** *(string) --*

        The type of the resource.

      - **ExpectedProperties** *(string) --*

        A JSON structure containing the expected property values of the stack resource, as defined
        in the stack template and any values specified as template parameters.

        For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not
        be present.

      - **ActualProperties** *(string) --*

        A JSON structure containing the actual property values of the stack resource.

        For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not
        be present.

      - **PropertyDifferences** *(list) --*

        A collection of the resource properties whose actual values differ from their expected
        values. These will be present only for resources whose ``StackResourceDriftStatus`` is
        ``MODIFIED`` .

        - *(dict) --*

          Information about a resource property whose actual value differs from its expected value,
          as defined in the stack template and any values specified as template parameters. These
          will be present only for resources whose ``StackResourceDriftStatus`` is ``MODIFIED`` .
          For more information, see `Detecting Unregulated Configuration Changes to Stacks and
          Resources
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .

          - **PropertyPath** *(string) --*

            The fully-qualified path to the resource property.

          - **ExpectedValue** *(string) --*

            The expected property value of the resource property, as defined in the stack template
            and any values specified as template parameters.

          - **ActualValue** *(string) --*

            The actual property value of the resource property.

          - **DifferenceType** *(string) --*

            The type of property difference.

            * ``ADD`` : A value has been added to a resource property that is an array or list data
            type.

            * ``REMOVE`` : The property has been removed from the current resource configuration.

            * ``NOT_EQUAL`` : The current property value differs from its expected value (as
            defined in the stack template and any values specified as template parameters).

      - **StackResourceDriftStatus** *(string) --*

        Status of the resource's actual configuration compared to its expected configuration

        * ``DELETED`` : The resource differs from its expected template configuration because the
        resource has been deleted.

        * ``MODIFIED`` : One or more resource properties differ from their expected values (as
        defined in the stack template and any values specified as template parameters).

        * ``IN_SYNC`` : The resources's actual configuration matches its expected template
        configuration.

        * ``NOT_CHECKED`` : AWS CloudFormation does not currently return this value.

      - **Timestamp** *(datetime) --*

        Time at which AWS CloudFormation performed drift detection on the stack resource.
    """


_ClientDetectStackSetDriftOperationPreferencesTypeDef = TypedDict(
    "_ClientDetectStackSetDriftOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientDetectStackSetDriftOperationPreferencesTypeDef(
    _ClientDetectStackSetDriftOperationPreferencesTypeDef
):
    """
    Type definition for `ClientDetectStackSetDrift` `OperationPreferences`

    The user-specified preferences for how AWS CloudFormation performs a stack set operation.

    For more information on maximum concurrent accounts and failure tolerance, see `Stack set
    operation options
    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options>`__
    .

    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.

      - *(string) --*

    - **FailureToleranceCount** *(integer) --*

      The number of accounts, per region, for which this operation can fail before AWS CloudFormation
      stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation
      doesn't attempt the operation in any subsequent regions.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` (but not both).

    - **FailureTolerancePercentage** *(integer) --*

      The percentage of accounts, per region, for which this stack operation can fail before AWS
      CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS
      CloudFormation doesn't attempt the operation in any subsequent regions.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds *down* to the next whole number.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` , but not both.

    - **MaxConcurrentCount** *(integer) --*

      The maximum number of accounts in which to perform this operation at one time. This is
      dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more
      than the ``FailureToleranceCount`` .

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.

    - **MaxConcurrentPercentage** *(integer) --*

      The maximum percentage of accounts in which to perform this operation at one time.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds down to the next whole number. This is true except in cases where rounding down would
      result is zero. In this case, CloudFormation sets the number as one instead.

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.
    """


_ClientDetectStackSetDriftResponseTypeDef = TypedDict(
    "_ClientDetectStackSetDriftResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDetectStackSetDriftResponseTypeDef(
    _ClientDetectStackSetDriftResponseTypeDef
):
    """
    Type definition for `ClientDetectStackSetDrift` `Response`

    - **OperationId** *(string) --*

      The ID of the drift detection stack set operation.

      you can use this operation id with ``  DescribeStackSetOperation `` to monitor the progress
      of the drift detection operation.
    """


_ClientEstimateTemplateCostParametersTypeDef = TypedDict(
    "_ClientEstimateTemplateCostParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientEstimateTemplateCostParametersTypeDef(
    _ClientEstimateTemplateCostParametersTypeDef
):
    """
    Type definition for `ClientEstimateTemplateCost` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientEstimateTemplateCostResponseTypeDef = TypedDict(
    "_ClientEstimateTemplateCostResponseTypeDef", {"Url": str}, total=False
)


class ClientEstimateTemplateCostResponseTypeDef(
    _ClientEstimateTemplateCostResponseTypeDef
):
    """
    Type definition for `ClientEstimateTemplateCost` `Response`

    The output for a  EstimateTemplateCost action.

    - **Url** *(string) --*

      An AWS Simple Monthly Calculator URL with a query string that describes the resources
      required to run the template.
    """


_ClientGetStackPolicyResponseTypeDef = TypedDict(
    "_ClientGetStackPolicyResponseTypeDef", {"StackPolicyBody": str}, total=False
)


class ClientGetStackPolicyResponseTypeDef(_ClientGetStackPolicyResponseTypeDef):
    """
    Type definition for `ClientGetStackPolicy` `Response`

    The output for the  GetStackPolicy action.

    - **StackPolicyBody** *(string) --*

      Structure containing the stack policy body. (For more information, go to `Prevent Updates to
      Stack Resources
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html>`__
      in the AWS CloudFormation User Guide.)
    """


_ClientGetTemplateResponseTypeDef = TypedDict(
    "_ClientGetTemplateResponseTypeDef", {"StagesAvailable": List[str]}, total=False
)


class ClientGetTemplateResponseTypeDef(_ClientGetTemplateResponseTypeDef):
    """
    Type definition for `ClientGetTemplate` `Response`

    The output for  GetTemplate action.

    - **TemplateBody** (*dict*) --

      Structure containing the template body. (For more information, go to `Template Anatomy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in
      the AWS CloudFormation User Guide.)

      AWS CloudFormation returns the same template that was used when the stack was created.

    - **StagesAvailable** *(list) --*

      The stage of the template that you can retrieve. For stacks, the ``Original`` and
      ``Processed`` templates are always available. For change sets, the ``Original`` template is
      always available. After AWS CloudFormation finishes creating the change set, the
      ``Processed`` template becomes available.

      - *(string) --*
    """


_ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef = TypedDict(
    "_ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef",
    {"AllowedValues": List[str]},
    total=False,
)


class ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef(
    _ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef
):
    """
    Type definition for `ClientGetTemplateSummaryResponseParameters` `ParameterConstraints`

    The criteria that AWS CloudFormation uses to validate parameter values.

    - **AllowedValues** *(list) --*

      A list of values that are permitted for a parameter.

      - *(string) --*
    """


_ClientGetTemplateSummaryResponseParametersTypeDef = TypedDict(
    "_ClientGetTemplateSummaryResponseParametersTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "NoEcho": bool,
        "Description": str,
        "ParameterConstraints": ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef,
    },
    total=False,
)


class ClientGetTemplateSummaryResponseParametersTypeDef(
    _ClientGetTemplateSummaryResponseParametersTypeDef
):
    """
    Type definition for `ClientGetTemplateSummaryResponse` `Parameters`

    The ParameterDeclaration data type.

    - **ParameterKey** *(string) --*

      The name that is associated with the parameter.

    - **DefaultValue** *(string) --*

      The default value of the parameter.

    - **ParameterType** *(string) --*

      The type of parameter.

    - **NoEcho** *(boolean) --*

      Flag that indicates whether the parameter value is shown as plain text in logs and in the
      AWS Management Console.

    - **Description** *(string) --*

      The description that is associate with the parameter.

    - **ParameterConstraints** *(dict) --*

      The criteria that AWS CloudFormation uses to validate parameter values.

      - **AllowedValues** *(list) --*

        A list of values that are permitted for a parameter.

        - *(string) --*
    """


_ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef = TypedDict(
    "_ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef",
    {
        "ResourceType": str,
        "LogicalResourceIds": List[str],
        "ResourceIdentifiers": List[str],
    },
    total=False,
)


class ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef(
    _ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef
):
    """
    Type definition for `ClientGetTemplateSummaryResponse` `ResourceIdentifierSummaries`

    Describes the target resources of a specific type in your import template (for example, all
    ``AWS::S3::Bucket`` resources) and the properties you can provide during the import to
    identify resources of that type.

    - **ResourceType** *(string) --*

      The template resource type of the target resources, such as ``AWS::S3::Bucket`` .

    - **LogicalResourceIds** *(list) --*

      The logical IDs of the target resources of the specified ``ResourceType`` , as defined in
      the import template.

      - *(string) --*

    - **ResourceIdentifiers** *(list) --*

      The resource properties you can provide during the import to identify your target
      resources. For example, ``BucketName`` is a possible identifier property for
      ``AWS::S3::Bucket`` resources.

      - *(string) --*
    """


_ClientGetTemplateSummaryResponseTypeDef = TypedDict(
    "_ClientGetTemplateSummaryResponseTypeDef",
    {
        "Parameters": List[ClientGetTemplateSummaryResponseParametersTypeDef],
        "Description": str,
        "Capabilities": List[str],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List[
            ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef
        ],
    },
    total=False,
)


class ClientGetTemplateSummaryResponseTypeDef(_ClientGetTemplateSummaryResponseTypeDef):
    """
    Type definition for `ClientGetTemplateSummary` `Response`

    The output for the  GetTemplateSummary action.

    - **Parameters** *(list) --*

      A list of parameter declarations that describe various properties for each parameter.

      - *(dict) --*

        The ParameterDeclaration data type.

        - **ParameterKey** *(string) --*

          The name that is associated with the parameter.

        - **DefaultValue** *(string) --*

          The default value of the parameter.

        - **ParameterType** *(string) --*

          The type of parameter.

        - **NoEcho** *(boolean) --*

          Flag that indicates whether the parameter value is shown as plain text in logs and in the
          AWS Management Console.

        - **Description** *(string) --*

          The description that is associate with the parameter.

        - **ParameterConstraints** *(dict) --*

          The criteria that AWS CloudFormation uses to validate parameter values.

          - **AllowedValues** *(list) --*

            A list of values that are permitted for a parameter.

            - *(string) --*

    - **Description** *(string) --*

      The value that is defined in the ``Description`` property of the template.

    - **Capabilities** *(list) --*

      The capabilities found within the template. If your template contains IAM resources, you must
      specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM value for this parameter when you use the
      CreateStack or  UpdateStack actions with your template; otherwise, those actions return an
      InsufficientCapabilities error.

      For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__
      .

      - *(string) --*

    - **CapabilitiesReason** *(string) --*

      The list of resources that generated the values in the ``Capabilities`` response element.

    - **ResourceTypes** *(list) --*

      A list of all the template resource types that are defined in the template, such as
      ``AWS::EC2::Instance`` , ``AWS::Dynamo::Table`` , and ``Custom::MyCustomInstance`` .

      - *(string) --*

    - **Version** *(string) --*

      The AWS template format version, which identifies the capabilities of the template.

    - **Metadata** *(string) --*

      The value that is defined for the ``Metadata`` property of the template.

    - **DeclaredTransforms** *(list) --*

      A list of the transforms that are declared in the template.

      - *(string) --*

    - **ResourceIdentifierSummaries** *(list) --*

      A list of resource identifier summaries that describe the target resources of an import
      operation and the properties you can provide during the import to identify the target
      resources. For example, ``BucketName`` is a possible identifier property for an
      ``AWS::S3::Bucket`` resource.

      - *(dict) --*

        Describes the target resources of a specific type in your import template (for example, all
        ``AWS::S3::Bucket`` resources) and the properties you can provide during the import to
        identify resources of that type.

        - **ResourceType** *(string) --*

          The template resource type of the target resources, such as ``AWS::S3::Bucket`` .

        - **LogicalResourceIds** *(list) --*

          The logical IDs of the target resources of the specified ``ResourceType`` , as defined in
          the import template.

          - *(string) --*

        - **ResourceIdentifiers** *(list) --*

          The resource properties you can provide during the import to identify your target
          resources. For example, ``BucketName`` is a possible identifier property for
          ``AWS::S3::Bucket`` resources.

          - *(string) --*
    """


_ClientListChangeSetsResponseSummariesTypeDef = TypedDict(
    "_ClientListChangeSetsResponseSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": str,
        "Status": str,
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListChangeSetsResponseSummariesTypeDef(
    _ClientListChangeSetsResponseSummariesTypeDef
):
    """
    Type definition for `ClientListChangeSetsResponse` `Summaries`

    The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with
    which it's associated.

    - **StackId** *(string) --*

      The ID of the stack with which the change set is associated.

    - **StackName** *(string) --*

      The name of the stack with which the change set is associated.

    - **ChangeSetId** *(string) --*

      The ID of the change set.

    - **ChangeSetName** *(string) --*

      The name of the change set.

    - **ExecutionStatus** *(string) --*

      If the change set execution status is ``AVAILABLE`` , you can execute the change set. If
      you can’t execute the change set, the status indicates why. For example, a change set
      might be in an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or
      in an ``OBSOLETE`` state because the stack was already updated.

    - **Status** *(string) --*

      The state of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` , or
      ``FAILED`` .

    - **StatusReason** *(string) --*

      A description of the change set's status. For example, if your change set is in the
      ``FAILED`` state, AWS CloudFormation shows the error message.

    - **CreationTime** *(datetime) --*

      The start time when the change set was created, in UTC.

    - **Description** *(string) --*

      Descriptive information about the change set.
    """


_ClientListChangeSetsResponseTypeDef = TypedDict(
    "_ClientListChangeSetsResponseTypeDef",
    {"Summaries": List[ClientListChangeSetsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListChangeSetsResponseTypeDef(_ClientListChangeSetsResponseTypeDef):
    """
    Type definition for `ClientListChangeSets` `Response`

    The output for the  ListChangeSets action.

    - **Summaries** *(list) --*

      A list of ``ChangeSetSummary`` structures that provides the ID and status of each change set
      for the specified stack.

      - *(dict) --*

        The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with
        which it's associated.

        - **StackId** *(string) --*

          The ID of the stack with which the change set is associated.

        - **StackName** *(string) --*

          The name of the stack with which the change set is associated.

        - **ChangeSetId** *(string) --*

          The ID of the change set.

        - **ChangeSetName** *(string) --*

          The name of the change set.

        - **ExecutionStatus** *(string) --*

          If the change set execution status is ``AVAILABLE`` , you can execute the change set. If
          you can’t execute the change set, the status indicates why. For example, a change set
          might be in an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or
          in an ``OBSOLETE`` state because the stack was already updated.

        - **Status** *(string) --*

          The state of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` , or
          ``FAILED`` .

        - **StatusReason** *(string) --*

          A description of the change set's status. For example, if your change set is in the
          ``FAILED`` state, AWS CloudFormation shows the error message.

        - **CreationTime** *(datetime) --*

          The start time when the change set was created, in UTC.

        - **Description** *(string) --*

          Descriptive information about the change set.

    - **NextToken** *(string) --*

      If the output exceeds 1 MB, a string that identifies the next page of change sets. If there
      is no additional page, this value is null.
    """


_ClientListExportsResponseExportsTypeDef = TypedDict(
    "_ClientListExportsResponseExportsTypeDef",
    {"ExportingStackId": str, "Name": str, "Value": str},
    total=False,
)


class ClientListExportsResponseExportsTypeDef(_ClientListExportsResponseExportsTypeDef):
    """
    Type definition for `ClientListExportsResponse` `Exports`

    The ``Export`` structure describes the exported output values for a stack.

    - **ExportingStackId** *(string) --*

      The stack that contains the exported output name and value.

    - **Name** *(string) --*

      The name of exported output value. Use this name and the ``Fn::ImportValue`` function to
      import the associated value into other stacks. The name is defined in the ``Export``
      field in the associated stack's ``Outputs`` section.

    - **Value** *(string) --*

      The value of the exported output, such as a resource physical ID. This value is defined
      in the ``Export`` field in the associated stack's ``Outputs`` section.
    """


_ClientListExportsResponseTypeDef = TypedDict(
    "_ClientListExportsResponseTypeDef",
    {"Exports": List[ClientListExportsResponseExportsTypeDef], "NextToken": str},
    total=False,
)


class ClientListExportsResponseTypeDef(_ClientListExportsResponseTypeDef):
    """
    Type definition for `ClientListExports` `Response`

    - **Exports** *(list) --*

      The output for the  ListExports action.

      - *(dict) --*

        The ``Export`` structure describes the exported output values for a stack.

        - **ExportingStackId** *(string) --*

          The stack that contains the exported output name and value.

        - **Name** *(string) --*

          The name of exported output value. Use this name and the ``Fn::ImportValue`` function to
          import the associated value into other stacks. The name is defined in the ``Export``
          field in the associated stack's ``Outputs`` section.

        - **Value** *(string) --*

          The value of the exported output, such as a resource physical ID. This value is defined
          in the ``Export`` field in the associated stack's ``Outputs`` section.

    - **NextToken** *(string) --*

      If the output exceeds 100 exported output values, a string that identifies the next page of
      exports. If there is no additional page, this value is null.
    """


_ClientListImportsResponseTypeDef = TypedDict(
    "_ClientListImportsResponseTypeDef",
    {"Imports": List[str], "NextToken": str},
    total=False,
)


class ClientListImportsResponseTypeDef(_ClientListImportsResponseTypeDef):
    """
    Type definition for `ClientListImports` `Response`

    - **Imports** *(list) --*

      A list of stack names that are importing the specified exported output value.

      - *(string) --*

    - **NextToken** *(string) --*

      A string that identifies the next page of exports. If there is no additional page, this value
      is null.
    """


_ClientListStackInstancesResponseSummariesTypeDef = TypedDict(
    "_ClientListStackInstancesResponseSummariesTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": str,
        "StatusReason": str,
        "DriftStatus": str,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ClientListStackInstancesResponseSummariesTypeDef(
    _ClientListStackInstancesResponseSummariesTypeDef
):
    """
    Type definition for `ClientListStackInstancesResponse` `Summaries`

    The structure that contains summary information about a stack instance.

    - **StackSetId** *(string) --*

      The name or unique ID of the stack set that the stack instance is associated with.

    - **Region** *(string) --*

      The name of the AWS region that the stack instance is associated with.

    - **Account** *(string) --*

      The name of the AWS account that the stack instance is associated with.

    - **StackId** *(string) --*

      The ID of the stack instance.

    - **Status** *(string) --*

      The status of the stack instance, in terms of its synchronization with its associated
      stack set.

      * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in
      an unstable state. Stacks in this state are excluded from further ``UpdateStackSet``
      operations. You might need to perform a ``DeleteStackInstances`` operation, with
      ``RetainStacks`` set to ``true`` , to delete the stack instance, and then delete the
      stack manually.

      * ``OUTDATED`` : The stack isn't currently up to date with the stack set because:

        * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet``
        operation.

        * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that
        failed or was stopped before the stack was created or updated.

      * ``CURRENT`` : The stack is currently up to date with the stack set.

    - **StatusReason** *(string) --*

      The explanation for the specific status code assigned to this stack instance.

    - **DriftStatus** *(string) --*

      Status of the stack instance's actual configuration compared to the expected template and
      parameter configuration of the stack set to which it belongs.

      * ``DRIFTED`` : The stack differs from the expected template and parameter configuration
      of the stack set to which it belongs. A stack instance is considered to have drifted if
      one or more of the resources in the associated stack have drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack instance differs from
      its expected stack set configuration.

      * ``IN_SYNC`` : The stack instance's actual configuration matches its expected stack set
      configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastDriftCheckTimestamp** *(datetime) --*

      Most recent time when CloudFormation performed a drift detection operation on the stack
      instance. This value will be ``NULL`` for any stack instance on which drift detection has
      not yet been performed.
    """


_ClientListStackInstancesResponseTypeDef = TypedDict(
    "_ClientListStackInstancesResponseTypeDef",
    {
        "Summaries": List[ClientListStackInstancesResponseSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListStackInstancesResponseTypeDef(_ClientListStackInstancesResponseTypeDef):
    """
    Type definition for `ClientListStackInstances` `Response`

    - **Summaries** *(list) --*

      A list of ``StackInstanceSummary`` structures that contain information about the specified
      stack instances.

      - *(dict) --*

        The structure that contains summary information about a stack instance.

        - **StackSetId** *(string) --*

          The name or unique ID of the stack set that the stack instance is associated with.

        - **Region** *(string) --*

          The name of the AWS region that the stack instance is associated with.

        - **Account** *(string) --*

          The name of the AWS account that the stack instance is associated with.

        - **StackId** *(string) --*

          The ID of the stack instance.

        - **Status** *(string) --*

          The status of the stack instance, in terms of its synchronization with its associated
          stack set.

          * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in
          an unstable state. Stacks in this state are excluded from further ``UpdateStackSet``
          operations. You might need to perform a ``DeleteStackInstances`` operation, with
          ``RetainStacks`` set to ``true`` , to delete the stack instance, and then delete the
          stack manually.

          * ``OUTDATED`` : The stack isn't currently up to date with the stack set because:

            * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet``
            operation.

            * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that
            failed or was stopped before the stack was created or updated.

          * ``CURRENT`` : The stack is currently up to date with the stack set.

        - **StatusReason** *(string) --*

          The explanation for the specific status code assigned to this stack instance.

        - **DriftStatus** *(string) --*

          Status of the stack instance's actual configuration compared to the expected template and
          parameter configuration of the stack set to which it belongs.

          * ``DRIFTED`` : The stack differs from the expected template and parameter configuration
          of the stack set to which it belongs. A stack instance is considered to have drifted if
          one or more of the resources in the associated stack have drifted.

          * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack instance differs from
          its expected stack set configuration.

          * ``IN_SYNC`` : The stack instance's actual configuration matches its expected stack set
          configuration.

          * ``UNKNOWN`` : This value is reserved for future use.

        - **LastDriftCheckTimestamp** *(datetime) --*

          Most recent time when CloudFormation performed a drift detection operation on the stack
          instance. This value will be ``NULL`` for any stack instance on which drift detection has
          not yet been performed.

    - **NextToken** *(string) --*

      If the request doesn't return all of the remaining results, ``NextToken`` is set to a token.
      To retrieve the next set of results, call ``ListStackInstances`` again and assign that token
      to the request object's ``NextToken`` parameter. If the request returns all results,
      ``NextToken`` is set to ``null`` .
    """


_ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef = TypedDict(
    "_ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef",
    {"StackResourceDriftStatus": str, "LastCheckTimestamp": datetime},
    total=False,
)


class ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef(
    _ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef
):
    """
    Type definition for `ClientListStackResourcesResponseStackResourceSummaries` `DriftInformation`

    Information about whether the resource's actual configuration differs, or has *drifted* ,
    from its expected configuration, as defined in the stack template and any values
    specified as template parameters. For more information, see `Detecting Unregulated
    Configuration Changes to Stacks and Resources
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **StackResourceDriftStatus** *(string) --*

      Status of the resource's actual configuration compared to its expected configuration

      * ``DELETED`` : The resource differs from its expected configuration in that it has
      been deleted.

      * ``MODIFIED`` : The resource differs from its expected configuration.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
      expected configuration. Any resources that do not currently support drift detection
      have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
      Drift Detection
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
      . If you performed an  ContinueUpdateRollback operation on a stack, any resources
      included in ``ResourcesToSkip`` will also have a status of ``NOT_CHECKED`` . For more
      information on skipping resources during rollback operations, see `Continue Rolling
      Back an Update
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`__
      in the AWS CloudFormation User Guide.

      * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

    - **LastCheckTimestamp** *(datetime) --*

      When AWS CloudFormation last checked if the resource had drifted from its expected
      configuration.
    """


_ClientListStackResourcesResponseStackResourceSummariesTypeDef = TypedDict(
    "_ClientListStackResourcesResponseStackResourceSummariesTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": str,
        "ResourceStatusReason": str,
        "DriftInformation": ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef,
    },
    total=False,
)


class ClientListStackResourcesResponseStackResourceSummariesTypeDef(
    _ClientListStackResourcesResponseStackResourceSummariesTypeDef
):
    """
    Type definition for `ClientListStackResourcesResponse` `StackResourceSummaries`

    Contains high-level information about the specified stack resource.

    - **LogicalResourceId** *(string) --*

      The logical name of the resource specified in the template.

    - **PhysicalResourceId** *(string) --*

      The name or unique identifier that corresponds to a physical instance ID of the resource.

    - **ResourceType** *(string) --*

      Type of resource. (For more information, go to `AWS Resource Types Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
      in the AWS CloudFormation User Guide.)

    - **LastUpdatedTimestamp** *(datetime) --*

      Time the status was updated.

    - **ResourceStatus** *(string) --*

      Current status of the resource.

    - **ResourceStatusReason** *(string) --*

      Success/failure message associated with the resource.

    - **DriftInformation** *(dict) --*

      Information about whether the resource's actual configuration differs, or has *drifted* ,
      from its expected configuration, as defined in the stack template and any values
      specified as template parameters. For more information, see `Detecting Unregulated
      Configuration Changes to Stacks and Resources
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .

      - **StackResourceDriftStatus** *(string) --*

        Status of the resource's actual configuration compared to its expected configuration

        * ``DELETED`` : The resource differs from its expected configuration in that it has
        been deleted.

        * ``MODIFIED`` : The resource differs from its expected configuration.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
        expected configuration. Any resources that do not currently support drift detection
        have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
        Drift Detection
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
        . If you performed an  ContinueUpdateRollback operation on a stack, any resources
        included in ``ResourcesToSkip`` will also have a status of ``NOT_CHECKED`` . For more
        information on skipping resources during rollback operations, see `Continue Rolling
        Back an Update
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`__
        in the AWS CloudFormation User Guide.

        * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

      - **LastCheckTimestamp** *(datetime) --*

        When AWS CloudFormation last checked if the resource had drifted from its expected
        configuration.
    """


_ClientListStackResourcesResponseTypeDef = TypedDict(
    "_ClientListStackResourcesResponseTypeDef",
    {
        "StackResourceSummaries": List[
            ClientListStackResourcesResponseStackResourceSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListStackResourcesResponseTypeDef(_ClientListStackResourcesResponseTypeDef):
    """
    Type definition for `ClientListStackResources` `Response`

    The output for a  ListStackResources action.

    - **StackResourceSummaries** *(list) --*

      A list of ``StackResourceSummary`` structures.

      - *(dict) --*

        Contains high-level information about the specified stack resource.

        - **LogicalResourceId** *(string) --*

          The logical name of the resource specified in the template.

        - **PhysicalResourceId** *(string) --*

          The name or unique identifier that corresponds to a physical instance ID of the resource.

        - **ResourceType** *(string) --*

          Type of resource. (For more information, go to `AWS Resource Types Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
          in the AWS CloudFormation User Guide.)

        - **LastUpdatedTimestamp** *(datetime) --*

          Time the status was updated.

        - **ResourceStatus** *(string) --*

          Current status of the resource.

        - **ResourceStatusReason** *(string) --*

          Success/failure message associated with the resource.

        - **DriftInformation** *(dict) --*

          Information about whether the resource's actual configuration differs, or has *drifted* ,
          from its expected configuration, as defined in the stack template and any values
          specified as template parameters. For more information, see `Detecting Unregulated
          Configuration Changes to Stacks and Resources
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .

          - **StackResourceDriftStatus** *(string) --*

            Status of the resource's actual configuration compared to its expected configuration

            * ``DELETED`` : The resource differs from its expected configuration in that it has
            been deleted.

            * ``MODIFIED`` : The resource differs from its expected configuration.

            * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
            expected configuration. Any resources that do not currently support drift detection
            have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
            Drift Detection
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
            . If you performed an  ContinueUpdateRollback operation on a stack, any resources
            included in ``ResourcesToSkip`` will also have a status of ``NOT_CHECKED`` . For more
            information on skipping resources during rollback operations, see `Continue Rolling
            Back an Update
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`__
            in the AWS CloudFormation User Guide.

            * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

          - **LastCheckTimestamp** *(datetime) --*

            When AWS CloudFormation last checked if the resource had drifted from its expected
            configuration.

    - **NextToken** *(string) --*

      If the output exceeds 1 MB, a string that identifies the next page of stack resources. If no
      additional page exists, this value is null.
    """


_ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef = TypedDict(
    "_ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef",
    {"Status": str, "StatusReason": str},
    total=False,
)


class ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef(
    _ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef
):
    """
    Type definition for `ClientListStackSetOperationResultsResponseSummaries` `AccountGateResult`

    The results of the account gate function AWS CloudFormation invokes, if present, before
    proceeding with stack set operations in an account

    - **Status** *(string) --*

      The status of the account gate function.

      * ``SUCCEEDED`` : The account gate function has determined that the account and region
      passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds
      with the stack operation in that account and region.

      * ``FAILED`` : The account gate function has determined that the account and region
      does not meet the requirements for a stack set operation to occur. AWS CloudFormation
      cancels the stack set operation in that account and region, and sets the stack set
      operation result status for that account and region to ``FAILED`` .

      * ``SKIPPED`` : AWS CloudFormation has skipped calling the account gate function for
      this account and region, for one of the following reasons:

        * An account gate function has not been specified for the account and region. AWS
        CloudFormation proceeds with the stack set operation in this account and region.

        * The ``AWSCloudFormationStackSetExecutionRole`` of the stack set adminstration
        account lacks permissions to invoke the function. AWS CloudFormation proceeds with
        the stack set operation in this account and region.

        * Either no action is necessary, or no action is possible, on the stack. AWS
        CloudFormation skips the stack set operation in this account and region.

    - **StatusReason** *(string) --*

      The reason for the account gate status assigned to this account and region for the
      stack set operation.
    """


_ClientListStackSetOperationResultsResponseSummariesTypeDef = TypedDict(
    "_ClientListStackSetOperationResultsResponseSummariesTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": str,
        "StatusReason": str,
        "AccountGateResult": ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef,
    },
    total=False,
)


class ClientListStackSetOperationResultsResponseSummariesTypeDef(
    _ClientListStackSetOperationResultsResponseSummariesTypeDef
):
    """
    Type definition for `ClientListStackSetOperationResultsResponse` `Summaries`

    The structure that contains information about a specified operation's results for a given
    account in a given region.

    - **Account** *(string) --*

      The name of the AWS account for this operation result.

    - **Region** *(string) --*

      The name of the AWS region for this operation result.

    - **Status** *(string) --*

      The result status of the stack set operation for the given account in the given region.

      * ``CANCELLED`` : The operation in the specified account and region has been cancelled.
      This is either because a user has stopped the stack set operation, or because the failure
      tolerance of the stack set operation has been exceeded.

      * ``FAILED`` : The operation in the specified account and region failed.  If the stack
      set operation fails in enough accounts within a region, the failure tolerance for the
      stack set operation as a whole might be exceeded.

      * ``RUNNING`` : The operation in the specified account and region is currently in
      progress.

      * ``PENDING`` : The operation in the specified account and region has yet to start.

      * ``SUCCEEDED`` : The operation in the specified account and region completed
      successfully.

    - **StatusReason** *(string) --*

      The reason for the assigned result status.

    - **AccountGateResult** *(dict) --*

      The results of the account gate function AWS CloudFormation invokes, if present, before
      proceeding with stack set operations in an account

      - **Status** *(string) --*

        The status of the account gate function.

        * ``SUCCEEDED`` : The account gate function has determined that the account and region
        passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds
        with the stack operation in that account and region.

        * ``FAILED`` : The account gate function has determined that the account and region
        does not meet the requirements for a stack set operation to occur. AWS CloudFormation
        cancels the stack set operation in that account and region, and sets the stack set
        operation result status for that account and region to ``FAILED`` .

        * ``SKIPPED`` : AWS CloudFormation has skipped calling the account gate function for
        this account and region, for one of the following reasons:

          * An account gate function has not been specified for the account and region. AWS
          CloudFormation proceeds with the stack set operation in this account and region.

          * The ``AWSCloudFormationStackSetExecutionRole`` of the stack set adminstration
          account lacks permissions to invoke the function. AWS CloudFormation proceeds with
          the stack set operation in this account and region.

          * Either no action is necessary, or no action is possible, on the stack. AWS
          CloudFormation skips the stack set operation in this account and region.

      - **StatusReason** *(string) --*

        The reason for the account gate status assigned to this account and region for the
        stack set operation.
    """


_ClientListStackSetOperationResultsResponseTypeDef = TypedDict(
    "_ClientListStackSetOperationResultsResponseTypeDef",
    {
        "Summaries": List[ClientListStackSetOperationResultsResponseSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListStackSetOperationResultsResponseTypeDef(
    _ClientListStackSetOperationResultsResponseTypeDef
):
    """
    Type definition for `ClientListStackSetOperationResults` `Response`

    - **Summaries** *(list) --*

      A list of ``StackSetOperationResultSummary`` structures that contain information about the
      specified operation results, for accounts and regions that are included in the operation.

      - *(dict) --*

        The structure that contains information about a specified operation's results for a given
        account in a given region.

        - **Account** *(string) --*

          The name of the AWS account for this operation result.

        - **Region** *(string) --*

          The name of the AWS region for this operation result.

        - **Status** *(string) --*

          The result status of the stack set operation for the given account in the given region.

          * ``CANCELLED`` : The operation in the specified account and region has been cancelled.
          This is either because a user has stopped the stack set operation, or because the failure
          tolerance of the stack set operation has been exceeded.

          * ``FAILED`` : The operation in the specified account and region failed.  If the stack
          set operation fails in enough accounts within a region, the failure tolerance for the
          stack set operation as a whole might be exceeded.

          * ``RUNNING`` : The operation in the specified account and region is currently in
          progress.

          * ``PENDING`` : The operation in the specified account and region has yet to start.

          * ``SUCCEEDED`` : The operation in the specified account and region completed
          successfully.

        - **StatusReason** *(string) --*

          The reason for the assigned result status.

        - **AccountGateResult** *(dict) --*

          The results of the account gate function AWS CloudFormation invokes, if present, before
          proceeding with stack set operations in an account

          - **Status** *(string) --*

            The status of the account gate function.

            * ``SUCCEEDED`` : The account gate function has determined that the account and region
            passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds
            with the stack operation in that account and region.

            * ``FAILED`` : The account gate function has determined that the account and region
            does not meet the requirements for a stack set operation to occur. AWS CloudFormation
            cancels the stack set operation in that account and region, and sets the stack set
            operation result status for that account and region to ``FAILED`` .

            * ``SKIPPED`` : AWS CloudFormation has skipped calling the account gate function for
            this account and region, for one of the following reasons:

              * An account gate function has not been specified for the account and region. AWS
              CloudFormation proceeds with the stack set operation in this account and region.

              * The ``AWSCloudFormationStackSetExecutionRole`` of the stack set adminstration
              account lacks permissions to invoke the function. AWS CloudFormation proceeds with
              the stack set operation in this account and region.

              * Either no action is necessary, or no action is possible, on the stack. AWS
              CloudFormation skips the stack set operation in this account and region.

          - **StatusReason** *(string) --*

            The reason for the account gate status assigned to this account and region for the
            stack set operation.

    - **NextToken** *(string) --*

      If the request doesn't return all results, ``NextToken`` is set to a token. To retrieve the
      next set of results, call ``ListOperationResults`` again and assign that token to the request
      object's ``NextToken`` parameter. If there are no remaining results, ``NextToken`` is set to
      ``null`` .
    """


_ClientListStackSetOperationsResponseSummariesTypeDef = TypedDict(
    "_ClientListStackSetOperationsResponseSummariesTypeDef",
    {
        "OperationId": str,
        "Action": str,
        "Status": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)


class ClientListStackSetOperationsResponseSummariesTypeDef(
    _ClientListStackSetOperationsResponseSummariesTypeDef
):
    """
    Type definition for `ClientListStackSetOperationsResponse` `Summaries`

    The structures that contain summary information about the specified operation.

    - **OperationId** *(string) --*

      The unique ID of the stack set operation.

    - **Action** *(string) --*

      The type of operation: ``CREATE`` , ``UPDATE`` , or ``DELETE`` . Create and delete
      operations affect only the specified stack instances that are associated with the
      specified stack set. Update operations affect both the stack set itself as well as *all*
      associated stack set instances.

    - **Status** *(string) --*

      The overall status of the operation.

      * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure
      tolerance value that you've set for an operation is applied for each region during stack
      create and update operations. If the number of failed stacks within a region exceeds the
      failure tolerance, the status of the operation in the region is set to ``FAILED`` . This
      in turn sets the status of the operation as a whole to ``FAILED`` , and AWS
      CloudFormation cancels the operation in any remaining regions.

      * ``RUNNING`` : The operation is currently being performed.

      * ``STOPPED`` : The user has cancelled the operation.

      * ``STOPPING`` : The operation is in the process of stopping, at user request.

      * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks
      without exceeding the failure tolerance for the operation.

    - **CreationTimestamp** *(datetime) --*

      The time at which the operation was initiated. Note that the creation times for the stack
      set operation might differ from the creation time of the individual stacks themselves.
      This is because AWS CloudFormation needs to perform preparatory work for the operation,
      such as dispatching the work to the requested regions, before actually creating the first
      stacks.

    - **EndTimestamp** *(datetime) --*

      The time at which the stack set operation ended, across all accounts and regions
      specified. Note that this doesn't necessarily mean that the stack set operation was
      successful, or even attempted, in each account or region.
    """


_ClientListStackSetOperationsResponseTypeDef = TypedDict(
    "_ClientListStackSetOperationsResponseTypeDef",
    {
        "Summaries": List[ClientListStackSetOperationsResponseSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListStackSetOperationsResponseTypeDef(
    _ClientListStackSetOperationsResponseTypeDef
):
    """
    Type definition for `ClientListStackSetOperations` `Response`

    - **Summaries** *(list) --*

      A list of ``StackSetOperationSummary`` structures that contain summary information about
      operations for the specified stack set.

      - *(dict) --*

        The structures that contain summary information about the specified operation.

        - **OperationId** *(string) --*

          The unique ID of the stack set operation.

        - **Action** *(string) --*

          The type of operation: ``CREATE`` , ``UPDATE`` , or ``DELETE`` . Create and delete
          operations affect only the specified stack instances that are associated with the
          specified stack set. Update operations affect both the stack set itself as well as *all*
          associated stack set instances.

        - **Status** *(string) --*

          The overall status of the operation.

          * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure
          tolerance value that you've set for an operation is applied for each region during stack
          create and update operations. If the number of failed stacks within a region exceeds the
          failure tolerance, the status of the operation in the region is set to ``FAILED`` . This
          in turn sets the status of the operation as a whole to ``FAILED`` , and AWS
          CloudFormation cancels the operation in any remaining regions.

          * ``RUNNING`` : The operation is currently being performed.

          * ``STOPPED`` : The user has cancelled the operation.

          * ``STOPPING`` : The operation is in the process of stopping, at user request.

          * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks
          without exceeding the failure tolerance for the operation.

        - **CreationTimestamp** *(datetime) --*

          The time at which the operation was initiated. Note that the creation times for the stack
          set operation might differ from the creation time of the individual stacks themselves.
          This is because AWS CloudFormation needs to perform preparatory work for the operation,
          such as dispatching the work to the requested regions, before actually creating the first
          stacks.

        - **EndTimestamp** *(datetime) --*

          The time at which the stack set operation ended, across all accounts and regions
          specified. Note that this doesn't necessarily mean that the stack set operation was
          successful, or even attempted, in each account or region.

    - **NextToken** *(string) --*

      If the request doesn't return all results, ``NextToken`` is set to a token. To retrieve the
      next set of results, call ``ListOperationResults`` again and assign that token to the request
      object's ``NextToken`` parameter. If there are no remaining results, ``NextToken`` is set to
      ``null`` .
    """


_ClientListStackSetsResponseSummariesTypeDef = TypedDict(
    "_ClientListStackSetsResponseSummariesTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": str,
        "DriftStatus": str,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ClientListStackSetsResponseSummariesTypeDef(
    _ClientListStackSetsResponseSummariesTypeDef
):
    """
    Type definition for `ClientListStackSetsResponse` `Summaries`

    The structures that contain summary information about the specified stack set.

    - **StackSetName** *(string) --*

      The name of the stack set.

    - **StackSetId** *(string) --*

      The ID of the stack set.

    - **Description** *(string) --*

      A description of the stack set that you specify when the stack set is created or updated.

    - **Status** *(string) --*

      The status of the stack set.

    - **DriftStatus** *(string) --*

      Status of the stack set's actual configuration compared to its expected template and
      parameter configuration. A stack set is considered to have drifted if one or more of its
      stack instances have drifted from their expected template and parameter configuration.

      * ``DRIFTED`` : One or more of the stack instances belonging to the stack set stack
      differs from the expected template and parameter configuration. A stack instance is
      considered to have drifted if one or more of the resources in the associated stack have
      drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked the stack set for drift.

      * ``IN_SYNC`` : All of the stack instances belonging to the stack set stack match from
      the expected template and parameter configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastDriftCheckTimestamp** *(datetime) --*

      Most recent time when CloudFormation performed a drift detection operation on the stack
      set. This value will be ``NULL`` for any stack set on which drift detection has not yet
      been performed.
    """


_ClientListStackSetsResponseTypeDef = TypedDict(
    "_ClientListStackSetsResponseTypeDef",
    {"Summaries": List[ClientListStackSetsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListStackSetsResponseTypeDef(_ClientListStackSetsResponseTypeDef):
    """
    Type definition for `ClientListStackSets` `Response`

    - **Summaries** *(list) --*

      A list of ``StackSetSummary`` structures that contain information about the user's stack sets.

      - *(dict) --*

        The structures that contain summary information about the specified stack set.

        - **StackSetName** *(string) --*

          The name of the stack set.

        - **StackSetId** *(string) --*

          The ID of the stack set.

        - **Description** *(string) --*

          A description of the stack set that you specify when the stack set is created or updated.

        - **Status** *(string) --*

          The status of the stack set.

        - **DriftStatus** *(string) --*

          Status of the stack set's actual configuration compared to its expected template and
          parameter configuration. A stack set is considered to have drifted if one or more of its
          stack instances have drifted from their expected template and parameter configuration.

          * ``DRIFTED`` : One or more of the stack instances belonging to the stack set stack
          differs from the expected template and parameter configuration. A stack instance is
          considered to have drifted if one or more of the resources in the associated stack have
          drifted.

          * ``NOT_CHECKED`` : AWS CloudFormation has not checked the stack set for drift.

          * ``IN_SYNC`` : All of the stack instances belonging to the stack set stack match from
          the expected template and parameter configuration.

          * ``UNKNOWN`` : This value is reserved for future use.

        - **LastDriftCheckTimestamp** *(datetime) --*

          Most recent time when CloudFormation performed a drift detection operation on the stack
          set. This value will be ``NULL`` for any stack set on which drift detection has not yet
          been performed.

    - **NextToken** *(string) --*

      If the request doesn't return all of the remaining results, ``NextToken`` is set to a token.
      To retrieve the next set of results, call ``ListStackInstances`` again and assign that token
      to the request object's ``NextToken`` parameter. If the request returns all results,
      ``NextToken`` is set to ``null`` .
    """


_ClientListStacksResponseStackSummariesDriftInformationTypeDef = TypedDict(
    "_ClientListStacksResponseStackSummariesDriftInformationTypeDef",
    {"StackDriftStatus": str, "LastCheckTimestamp": datetime},
    total=False,
)


class ClientListStacksResponseStackSummariesDriftInformationTypeDef(
    _ClientListStacksResponseStackSummariesDriftInformationTypeDef
):
    """
    Type definition for `ClientListStacksResponseStackSummaries` `DriftInformation`

    Summarizes information on whether a stack's actual configuration differs, or has
    *drifted* , from it's expected configuration, as defined in the stack template and any
    values specified as template parameters. For more information, see `Detecting Unregulated
    Configuration Changes to Stacks and Resources
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **StackDriftStatus** *(string) --*

      Status of the stack's actual configuration compared to its expected template
      configuration.

      * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
      considered to have drifted if one or more of its resources have drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
      expected template configuration.

      * ``IN_SYNC`` : The stack's actual configuration matches its expected template
      configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastCheckTimestamp** *(datetime) --*

      Most recent time when a drift detection operation was initiated on the stack, or any of
      its individual resources that support drift detection.
    """


_ClientListStacksResponseStackSummariesTypeDef = TypedDict(
    "_ClientListStacksResponseStackSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "TemplateDescription": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatus": str,
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ClientListStacksResponseStackSummariesDriftInformationTypeDef,
    },
    total=False,
)


class ClientListStacksResponseStackSummariesTypeDef(
    _ClientListStacksResponseStackSummariesTypeDef
):
    """
    Type definition for `ClientListStacksResponse` `StackSummaries`

    The StackSummary Data Type

    - **StackId** *(string) --*

      Unique stack identifier.

    - **StackName** *(string) --*

      The name associated with the stack.

    - **TemplateDescription** *(string) --*

      The template description of the template used to create the stack.

    - **CreationTime** *(datetime) --*

      The time the stack was created.

    - **LastUpdatedTime** *(datetime) --*

      The time the stack was last updated. This field will only be returned if the stack has
      been updated at least once.

    - **DeletionTime** *(datetime) --*

      The time the stack was deleted.

    - **StackStatus** *(string) --*

      The current status of the stack.

    - **StackStatusReason** *(string) --*

      Success/Failure message associated with the stack status.

    - **ParentId** *(string) --*

      For nested stacks--stacks created as resources for another stack--the stack ID of the
      direct parent of this stack. For the first level of nested stacks, the root stack is also
      the parent stack.

      For more information, see `Working with Nested Stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **RootId** *(string) --*

      For nested stacks--stacks created as resources for another stack--the stack ID of the
      top-level stack to which the nested stack ultimately belongs.

      For more information, see `Working with Nested Stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **DriftInformation** *(dict) --*

      Summarizes information on whether a stack's actual configuration differs, or has
      *drifted* , from it's expected configuration, as defined in the stack template and any
      values specified as template parameters. For more information, see `Detecting Unregulated
      Configuration Changes to Stacks and Resources
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .

      - **StackDriftStatus** *(string) --*

        Status of the stack's actual configuration compared to its expected template
        configuration.

        * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
        considered to have drifted if one or more of its resources have drifted.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
        expected template configuration.

        * ``IN_SYNC`` : The stack's actual configuration matches its expected template
        configuration.

        * ``UNKNOWN`` : This value is reserved for future use.

      - **LastCheckTimestamp** *(datetime) --*

        Most recent time when a drift detection operation was initiated on the stack, or any of
        its individual resources that support drift detection.
    """


_ClientListStacksResponseTypeDef = TypedDict(
    "_ClientListStacksResponseTypeDef",
    {
        "StackSummaries": List[ClientListStacksResponseStackSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListStacksResponseTypeDef(_ClientListStacksResponseTypeDef):
    """
    Type definition for `ClientListStacks` `Response`

    The output for  ListStacks action.

    - **StackSummaries** *(list) --*

      A list of ``StackSummary`` structures containing information about the specified stacks.

      - *(dict) --*

        The StackSummary Data Type

        - **StackId** *(string) --*

          Unique stack identifier.

        - **StackName** *(string) --*

          The name associated with the stack.

        - **TemplateDescription** *(string) --*

          The template description of the template used to create the stack.

        - **CreationTime** *(datetime) --*

          The time the stack was created.

        - **LastUpdatedTime** *(datetime) --*

          The time the stack was last updated. This field will only be returned if the stack has
          been updated at least once.

        - **DeletionTime** *(datetime) --*

          The time the stack was deleted.

        - **StackStatus** *(string) --*

          The current status of the stack.

        - **StackStatusReason** *(string) --*

          Success/Failure message associated with the stack status.

        - **ParentId** *(string) --*

          For nested stacks--stacks created as resources for another stack--the stack ID of the
          direct parent of this stack. For the first level of nested stacks, the root stack is also
          the parent stack.

          For more information, see `Working with Nested Stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **RootId** *(string) --*

          For nested stacks--stacks created as resources for another stack--the stack ID of the
          top-level stack to which the nested stack ultimately belongs.

          For more information, see `Working with Nested Stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **DriftInformation** *(dict) --*

          Summarizes information on whether a stack's actual configuration differs, or has
          *drifted* , from it's expected configuration, as defined in the stack template and any
          values specified as template parameters. For more information, see `Detecting Unregulated
          Configuration Changes to Stacks and Resources
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .

          - **StackDriftStatus** *(string) --*

            Status of the stack's actual configuration compared to its expected template
            configuration.

            * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
            considered to have drifted if one or more of its resources have drifted.

            * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
            expected template configuration.

            * ``IN_SYNC`` : The stack's actual configuration matches its expected template
            configuration.

            * ``UNKNOWN`` : This value is reserved for future use.

          - **LastCheckTimestamp** *(datetime) --*

            Most recent time when a drift detection operation was initiated on the stack, or any of
            its individual resources that support drift detection.

    - **NextToken** *(string) --*

      If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no
      additional page exists, this value is null.
    """


_ClientListTypeRegistrationsResponseTypeDef = TypedDict(
    "_ClientListTypeRegistrationsResponseTypeDef",
    {"RegistrationTokenList": List[str], "NextToken": str},
    total=False,
)


class ClientListTypeRegistrationsResponseTypeDef(
    _ClientListTypeRegistrationsResponseTypeDef
):
    """
    Type definition for `ClientListTypeRegistrations` `Response`

    - **RegistrationTokenList** *(list) --*

      A list of type registration tokens.

      Use ``  DescribeTypeRegistration `` to return detailed information about a type registration
      request.

      - *(string) --*

    - **NextToken** *(string) --*

      If the request doesn't return all of the remaining results, ``NextToken`` is set to a token.
      To retrieve the next set of results, call this action again and assign that token to the
      request object's ``NextToken`` parameter. If the request returns all results, ``NextToken``
      is set to ``null`` .
    """


_ClientListTypeVersionsResponseTypeVersionSummariesTypeDef = TypedDict(
    "_ClientListTypeVersionsResponseTypeVersionSummariesTypeDef",
    {
        "Type": str,
        "TypeName": str,
        "VersionId": str,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListTypeVersionsResponseTypeVersionSummariesTypeDef(
    _ClientListTypeVersionsResponseTypeVersionSummariesTypeDef
):
    """
    Type definition for `ClientListTypeVersionsResponse` `TypeVersionSummaries`

    Contains summary information about a specific version of a CloudFormation type.

    - **Type** *(string) --*

      The kind of type.

    - **TypeName** *(string) --*

      The name of the type.

    - **VersionId** *(string) --*

      The ID of a specific version of the type. The version ID is the value at the end of the
      Amazon Resource Name (ARN) assigned to the type version when it is registered.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the type version.

    - **TimeCreated** *(datetime) --*

      When the version was registered.

    - **Description** *(string) --*

      The description of the type version.
    """


_ClientListTypeVersionsResponseTypeDef = TypedDict(
    "_ClientListTypeVersionsResponseTypeDef",
    {
        "TypeVersionSummaries": List[
            ClientListTypeVersionsResponseTypeVersionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListTypeVersionsResponseTypeDef(_ClientListTypeVersionsResponseTypeDef):
    """
    Type definition for `ClientListTypeVersions` `Response`

    - **TypeVersionSummaries** *(list) --*

      A list of ``TypeVersionSummary`` structures that contain information about the specified
      type's versions.

      - *(dict) --*

        Contains summary information about a specific version of a CloudFormation type.

        - **Type** *(string) --*

          The kind of type.

        - **TypeName** *(string) --*

          The name of the type.

        - **VersionId** *(string) --*

          The ID of a specific version of the type. The version ID is the value at the end of the
          Amazon Resource Name (ARN) assigned to the type version when it is registered.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the type version.

        - **TimeCreated** *(datetime) --*

          When the version was registered.

        - **Description** *(string) --*

          The description of the type version.

    - **NextToken** *(string) --*

      If the request doesn't return all of the remaining results, ``NextToken`` is set to a token.
      To retrieve the next set of results, call this action again and assign that token to the
      request object's ``NextToken`` parameter. If the request returns all results, ``NextToken``
      is set to ``null`` .
    """


_ClientListTypesResponseTypeSummariesTypeDef = TypedDict(
    "_ClientListTypesResponseTypeSummariesTypeDef",
    {
        "Type": str,
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListTypesResponseTypeSummariesTypeDef(
    _ClientListTypesResponseTypeSummariesTypeDef
):
    """
    Type definition for `ClientListTypesResponse` `TypeSummaries`

    Contains summary information about the specified CloudFormation type.

    - **Type** *(string) --*

      The kind of type.

    - **TypeName** *(string) --*

      The name of the type.

    - **DefaultVersionId** *(string) --*

      The ID of the default version of the type. The default version is used when the type
      version is not specified.

      To set the default version of a type, use ``  SetTypeDefaultVersion `` .

    - **TypeArn** *(string) --*

      The Amazon Resource Name (ARN) of the type.

    - **LastUpdated** *(datetime) --*

      When the current default version of the type was registered.

    - **Description** *(string) --*

      The description of the type.
    """


_ClientListTypesResponseTypeDef = TypedDict(
    "_ClientListTypesResponseTypeDef",
    {
        "TypeSummaries": List[ClientListTypesResponseTypeSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTypesResponseTypeDef(_ClientListTypesResponseTypeDef):
    """
    Type definition for `ClientListTypes` `Response`

    - **TypeSummaries** *(list) --*

      A list of ``TypeSummary`` structures that contain information about the specified types.

      - *(dict) --*

        Contains summary information about the specified CloudFormation type.

        - **Type** *(string) --*

          The kind of type.

        - **TypeName** *(string) --*

          The name of the type.

        - **DefaultVersionId** *(string) --*

          The ID of the default version of the type. The default version is used when the type
          version is not specified.

          To set the default version of a type, use ``  SetTypeDefaultVersion `` .

        - **TypeArn** *(string) --*

          The Amazon Resource Name (ARN) of the type.

        - **LastUpdated** *(datetime) --*

          When the current default version of the type was registered.

        - **Description** *(string) --*

          The description of the type.

    - **NextToken** *(string) --*

      If the request doesn't return all of the remaining results, ``NextToken`` is set to a token.
      To retrieve the next set of results, call this action again and assign that token to the
      request object's ``NextToken`` parameter. If the request returns all results, ``NextToken``
      is set to ``null`` .
    """


_ClientRegisterTypeLoggingConfigTypeDef = TypedDict(
    "_ClientRegisterTypeLoggingConfigTypeDef", {"LogRoleArn": str, "LogGroupName": str}
)


class ClientRegisterTypeLoggingConfigTypeDef(_ClientRegisterTypeLoggingConfigTypeDef):
    """
    Type definition for `ClientRegisterType` `LoggingConfig`

    Specifies logging configuration information for a type.

    - **LogRoleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch
      logs.

    - **LogGroupName** *(string) --* **[REQUIRED]**

      The Amazon CloudWatch log group to which CloudFormation sends error logging information when
      invoking the type's handlers.
    """


_ClientRegisterTypeResponseTypeDef = TypedDict(
    "_ClientRegisterTypeResponseTypeDef", {"RegistrationToken": str}, total=False
)


class ClientRegisterTypeResponseTypeDef(_ClientRegisterTypeResponseTypeDef):
    """
    Type definition for `ClientRegisterType` `Response`

    - **RegistrationToken** *(string) --*

      The identifier for this registration request.

      Use this registration token when calling ``  DescribeTypeRegistration `` , which returns
      information about the status and IDs of the type registration.
    """


_ClientUpdateStackInstancesOperationPreferencesTypeDef = TypedDict(
    "_ClientUpdateStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientUpdateStackInstancesOperationPreferencesTypeDef(
    _ClientUpdateStackInstancesOperationPreferencesTypeDef
):
    """
    Type definition for `ClientUpdateStackInstances` `OperationPreferences`

    Preferences for how AWS CloudFormation performs this stack set operation.

    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.

      - *(string) --*

    - **FailureToleranceCount** *(integer) --*

      The number of accounts, per region, for which this operation can fail before AWS CloudFormation
      stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation
      doesn't attempt the operation in any subsequent regions.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` (but not both).

    - **FailureTolerancePercentage** *(integer) --*

      The percentage of accounts, per region, for which this stack operation can fail before AWS
      CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS
      CloudFormation doesn't attempt the operation in any subsequent regions.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds *down* to the next whole number.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` , but not both.

    - **MaxConcurrentCount** *(integer) --*

      The maximum number of accounts in which to perform this operation at one time. This is
      dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more
      than the ``FailureToleranceCount`` .

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.

    - **MaxConcurrentPercentage** *(integer) --*

      The maximum percentage of accounts in which to perform this operation at one time.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds down to the next whole number. This is true except in cases where rounding down would
      result is zero. In this case, CloudFormation sets the number as one instead.

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.
    """


_ClientUpdateStackInstancesParameterOverridesTypeDef = TypedDict(
    "_ClientUpdateStackInstancesParameterOverridesTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientUpdateStackInstancesParameterOverridesTypeDef(
    _ClientUpdateStackInstancesParameterOverridesTypeDef
):
    """
    Type definition for `ClientUpdateStackInstances` `ParameterOverrides`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientUpdateStackInstancesResponseTypeDef = TypedDict(
    "_ClientUpdateStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateStackInstancesResponseTypeDef(
    _ClientUpdateStackInstancesResponseTypeDef
):
    """
    Type definition for `ClientUpdateStackInstances` `Response`

    - **OperationId** *(string) --*

      The unique identifier for this stack set operation.
    """


_ClientUpdateStackParametersTypeDef = TypedDict(
    "_ClientUpdateStackParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientUpdateStackParametersTypeDef(_ClientUpdateStackParametersTypeDef):
    """
    Type definition for `ClientUpdateStack` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientUpdateStackResponseTypeDef = TypedDict(
    "_ClientUpdateStackResponseTypeDef", {"StackId": str}, total=False
)


class ClientUpdateStackResponseTypeDef(_ClientUpdateStackResponseTypeDef):
    """
    Type definition for `ClientUpdateStack` `Response`

    The output for an  UpdateStack action.

    - **StackId** *(string) --*

      Unique identifier of the stack.
    """


_ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
)


class ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef(
    _ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `ClientUpdateStackRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
    of the alarms you specify goes to ALARM state during the stack operation or within the
    specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

    - **Arn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

    - **Type** *(string) --* **[REQUIRED]**

      The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_ClientUpdateStackRollbackConfigurationTypeDef = TypedDict(
    "_ClientUpdateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientUpdateStackRollbackConfigurationTypeDef(
    _ClientUpdateStackRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateStack` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you do
      specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
        of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

        - **Arn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - **Type** *(string) --* **[REQUIRED]**

          The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the rollback
      triggers after the stack creation or update operation deploys all necessary resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
      still waits the specified period of time before cleaning up old resources after update
      operations. You can use this monitoring period to perform any manual stack validation desired,
      and manually cancel the stack creation or update (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
      triggers during stack creation and update operations. Then, for update operations, it begins
      disposing of old resources immediately once the operation completes.
    """


_ClientUpdateStackSetOperationPreferencesTypeDef = TypedDict(
    "_ClientUpdateStackSetOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientUpdateStackSetOperationPreferencesTypeDef(
    _ClientUpdateStackSetOperationPreferencesTypeDef
):
    """
    Type definition for `ClientUpdateStackSet` `OperationPreferences`

    Preferences for how AWS CloudFormation performs this stack set operation.

    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.

      - *(string) --*

    - **FailureToleranceCount** *(integer) --*

      The number of accounts, per region, for which this operation can fail before AWS CloudFormation
      stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation
      doesn't attempt the operation in any subsequent regions.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` (but not both).

    - **FailureTolerancePercentage** *(integer) --*

      The percentage of accounts, per region, for which this stack operation can fail before AWS
      CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS
      CloudFormation doesn't attempt the operation in any subsequent regions.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds *down* to the next whole number.

      Conditional: You must specify either ``FailureToleranceCount`` or
      ``FailureTolerancePercentage`` , but not both.

    - **MaxConcurrentCount** *(integer) --*

      The maximum number of accounts in which to perform this operation at one time. This is
      dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more
      than the ``FailureToleranceCount`` .

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.

    - **MaxConcurrentPercentage** *(integer) --*

      The maximum percentage of accounts in which to perform this operation at one time.

      When calculating the number of accounts based on the specified percentage, AWS CloudFormation
      rounds down to the next whole number. This is true except in cases where rounding down would
      result is zero. In this case, CloudFormation sets the number as one instead.

      Note that this setting lets you specify the *maximum* for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` ,
      but not both.
    """


_ClientUpdateStackSetParametersTypeDef = TypedDict(
    "_ClientUpdateStackSetParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ClientUpdateStackSetParametersTypeDef(_ClientUpdateStackSetParametersTypeDef):
    """
    Type definition for `ClientUpdateStackSet` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ClientUpdateStackSetResponseTypeDef = TypedDict(
    "_ClientUpdateStackSetResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateStackSetResponseTypeDef(_ClientUpdateStackSetResponseTypeDef):
    """
    Type definition for `ClientUpdateStackSet` `Response`

    - **OperationId** *(string) --*

      The unique ID for this stack set operation.
    """


_ClientUpdateStackSetTagsTypeDef = TypedDict(
    "_ClientUpdateStackSetTagsTypeDef", {"Key": str, "Value": str}
)


class ClientUpdateStackSetTagsTypeDef(_ClientUpdateStackSetTagsTypeDef):
    """
    Type definition for `ClientUpdateStackSet` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --* **[REQUIRED]**

       *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
       for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

       *Required* . A string containing the value for this tag. You can specify a maximum of 256
       characters for a tag value.
    """


_ClientUpdateStackTagsTypeDef = TypedDict(
    "_ClientUpdateStackTagsTypeDef", {"Key": str, "Value": str}
)


class ClientUpdateStackTagsTypeDef(_ClientUpdateStackTagsTypeDef):
    """
    Type definition for `ClientUpdateStack` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --* **[REQUIRED]**

       *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
       for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

       *Required* . A string containing the value for this tag. You can specify a maximum of 256
       characters for a tag value.
    """


_ClientUpdateTerminationProtectionResponseTypeDef = TypedDict(
    "_ClientUpdateTerminationProtectionResponseTypeDef", {"StackId": str}, total=False
)


class ClientUpdateTerminationProtectionResponseTypeDef(
    _ClientUpdateTerminationProtectionResponseTypeDef
):
    """
    Type definition for `ClientUpdateTerminationProtection` `Response`

    - **StackId** *(string) --*

      The unique ID of the stack.
    """


_ClientValidateTemplateResponseParametersTypeDef = TypedDict(
    "_ClientValidateTemplateResponseParametersTypeDef",
    {"ParameterKey": str, "DefaultValue": str, "NoEcho": bool, "Description": str},
    total=False,
)


class ClientValidateTemplateResponseParametersTypeDef(
    _ClientValidateTemplateResponseParametersTypeDef
):
    """
    Type definition for `ClientValidateTemplateResponse` `Parameters`

    The TemplateParameter data type.

    - **ParameterKey** *(string) --*

      The name associated with the parameter.

    - **DefaultValue** *(string) --*

      The default value associated with the parameter.

    - **NoEcho** *(boolean) --*

      Flag indicating whether the parameter should be displayed as plain text in logs and UIs.

    - **Description** *(string) --*

      User defined description associated with the parameter.
    """


_ClientValidateTemplateResponseTypeDef = TypedDict(
    "_ClientValidateTemplateResponseTypeDef",
    {
        "Parameters": List[ClientValidateTemplateResponseParametersTypeDef],
        "Description": str,
        "Capabilities": List[str],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
    },
    total=False,
)


class ClientValidateTemplateResponseTypeDef(_ClientValidateTemplateResponseTypeDef):
    """
    Type definition for `ClientValidateTemplate` `Response`

    The output for  ValidateTemplate action.

    - **Parameters** *(list) --*

      A list of ``TemplateParameter`` structures.

      - *(dict) --*

        The TemplateParameter data type.

        - **ParameterKey** *(string) --*

          The name associated with the parameter.

        - **DefaultValue** *(string) --*

          The default value associated with the parameter.

        - **NoEcho** *(boolean) --*

          Flag indicating whether the parameter should be displayed as plain text in logs and UIs.

        - **Description** *(string) --*

          User defined description associated with the parameter.

    - **Description** *(string) --*

      The description found within the template.

    - **Capabilities** *(list) --*

      The capabilities found within the template. If your template contains IAM resources, you must
      specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM value for this parameter when you use the
      CreateStack or  UpdateStack actions with your template; otherwise, those actions return an
      InsufficientCapabilities error.

      For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__
      .

      - *(string) --*

    - **CapabilitiesReason** *(string) --*

      The list of resources that generated the values in the ``Capabilities`` response element.

    - **DeclaredTransforms** *(list) --*

      A list of the transforms that are declared in the template.

      - *(string) --*
    """


_DescribeAccountLimitsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeAccountLimitsPaginatePaginationConfigTypeDef(
    _DescribeAccountLimitsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAccountLimitsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)


class DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef(
    _DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef
):
    """
    Type definition for `DescribeAccountLimitsPaginateResponse` `AccountLimits`

    The AccountLimit data type.

    CloudFormation has the following limits per account:

    * Number of concurrent resources

    * Number of stacks

    * Number of stack outputs

    For more information about these account limits, and other CloudFormation limits, see `AWS
    CloudFormation Limits
    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
    in the *AWS CloudFormation User Guide* .

    - **Name** *(string) --*

      The name of the account limit.

      Values: ``ConcurrentResourcesLimit`` | ``StackLimit`` | ``StackOutputsLimit``

    - **Value** *(integer) --*

      The value that is associated with the account limit name.
    """


_DescribeAccountLimitsPaginateResponseTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginateResponseTypeDef",
    {"AccountLimits": List[DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef]},
    total=False,
)


class DescribeAccountLimitsPaginateResponseTypeDef(
    _DescribeAccountLimitsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAccountLimitsPaginate` `Response`

    The output for the  DescribeAccountLimits action.

    - **AccountLimits** *(list) --*

      An account limit structure that contain a list of AWS CloudFormation account limits and their
      values.

      - *(dict) --*

        The AccountLimit data type.

        CloudFormation has the following limits per account:

        * Number of concurrent resources

        * Number of stacks

        * Number of stack outputs

        For more information about these account limits, and other CloudFormation limits, see `AWS
        CloudFormation Limits
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
        in the *AWS CloudFormation User Guide* .

        - **Name** *(string) --*

          The name of the account limit.

          Values: ``ConcurrentResourcesLimit`` | ``StackLimit`` | ``StackOutputsLimit``

        - **Value** *(integer) --*

          The value that is associated with the account limit name.
    """


_DescribeChangeSetPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeChangeSetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeChangeSetPaginatePaginationConfigTypeDef(
    _DescribeChangeSetPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef",
    {"Attribute": str, "Name": str, "RequiresRecreation": str},
    total=False,
)


class DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef(
    _DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginateResponseChangesResourceChangeDetails` `Target`

    A ``ResourceTargetDefinition`` structure that describes the field that AWS
    CloudFormation will change and whether the resource will be recreated.

    - **Attribute** *(string) --*

      Indicates which resource attribute is triggering this update, such as a change in
      the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

    - **Name** *(string) --*

      If the ``Attribute`` value is ``Properties`` , the name of the property. For all
      other attributes, the value is null.

    - **RequiresRecreation** *(string) --*

      If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
      property causes the resource to be recreated. The value can be ``Never`` ,
      ``Always`` , or ``Conditionally`` . To determine the conditions for a
      ``Conditionally`` recreation, see the update behavior for that `property
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
      in the AWS CloudFormation User Guide.
    """


_DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef",
    {
        "Target": DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef,
        "Evaluation": str,
        "ChangeSource": str,
        "CausingEntity": str,
    },
    total=False,
)


class DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef(
    _DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginateResponseChangesResourceChange` `Details`

    For a resource with ``Modify`` as the action, the ``ResourceChange`` structure
    describes the changes AWS CloudFormation will make to that resource.

    - **Target** *(dict) --*

      A ``ResourceTargetDefinition`` structure that describes the field that AWS
      CloudFormation will change and whether the resource will be recreated.

      - **Attribute** *(string) --*

        Indicates which resource attribute is triggering this update, such as a change in
        the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

      - **Name** *(string) --*

        If the ``Attribute`` value is ``Properties`` , the name of the property. For all
        other attributes, the value is null.

      - **RequiresRecreation** *(string) --*

        If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
        property causes the resource to be recreated. The value can be ``Never`` ,
        ``Always`` , or ``Conditionally`` . To determine the conditions for a
        ``Conditionally`` recreation, see the update behavior for that `property
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
        in the AWS CloudFormation User Guide.

    - **Evaluation** *(string) --*

      Indicates whether AWS CloudFormation can determine the target value, and whether
      the target value will change before you execute a change set.

      For ``Static`` evaluations, AWS CloudFormation can determine that the target value
      will change, and its value. For example, if you directly modify the
      ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this
      property value will change, and its value, so this is a ``Static`` evaluation.

      For ``Dynamic`` evaluations, cannot determine the target value because it depends
      on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt``
      intrinsic function, when the stack is updated. For example, if your template
      includes a reference to a resource that is conditionally recreated, the value of
      the reference (the physical ID of the resource) might change, depending on if the
      resource is recreated. If the resource is recreated, it will have a new physical
      ID, so all references to that resource will also be updated.

    - **ChangeSource** *(string) --*

      The group to which the ``CausingEntity`` value belongs. There are five entity
      groups:

      * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to
      resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` .

      * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template
      parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` .

      * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get
      resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource",
      "PublicDnsName" ] }`` .

      * ``DirectModification`` entities are changes that are made directly to the
      template.

      * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which
      are also known as nested stacks. If you made no changes to the
      ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the
      ``ChangeSource`` to ``Automatic`` because the nested stack's template might have
      changed. Changes to a nested stack's template aren't visible to AWS CloudFormation
      until you run an update on the parent stack.

    - **CausingEntity** *(string) --*

      The identity of the entity that triggered this change. This entity is a member of
      the group that is specified by the ``ChangeSource`` field. For example, if you
      modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the
      name of the parameter (``KeyPairName`` ).

      If the ``ChangeSource`` value is ``DirectModification`` , no value is given for
      ``CausingEntity`` .
    """


_DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef",
    {
        "Action": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": str,
        "Scope": List[str],
        "Details": List[
            DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef
        ],
    },
    total=False,
)


class DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef(
    _DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginateResponseChanges` `ResourceChange`

    A ``ResourceChange`` structure that describes the resource and action that AWS
    CloudFormation will perform.

    - **Action** *(string) --*

      The action that AWS CloudFormation takes on the resource, such as ``Add`` (adds a new
      resource), ``Modify`` (changes a resource), or ``Remove`` (deletes a resource).

    - **LogicalResourceId** *(string) --*

      The resource's logical ID, which is defined in the stack's template.

    - **PhysicalResourceId** *(string) --*

      The resource's physical ID (resource name). Resources that you are adding don't have
      physical IDs because they haven't been created.

    - **ResourceType** *(string) --*

      The type of AWS CloudFormation resource, such as ``AWS::S3::Bucket`` .

    - **Replacement** *(string) --*

      For the ``Modify`` action, indicates whether AWS CloudFormation will replace the
      resource by creating a new one and deleting the old one. This value depends on the
      value of the ``RequiresRecreation`` property in the ``ResourceTargetDefinition``
      structure. For example, if the ``RequiresRecreation`` field is ``Always`` and the
      ``Evaluation`` field is ``Static`` , ``Replacement`` is ``True`` . If the
      ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Dynamic``
      , ``Replacement`` is ``Conditionally`` .

      If you have multiple changes with different ``RequiresRecreation`` values, the
      ``Replacement`` value depends on the change with the most impact. A
      ``RequiresRecreation`` value of ``Always`` has the most impact, followed by
      ``Conditionally`` , and then ``Never`` .

    - **Scope** *(list) --*

      For the ``Modify`` action, indicates which resource attribute is triggering this
      update, such as a change in the resource attribute's ``Metadata`` , ``Properties`` , or
      ``Tags`` .

      - *(string) --*

    - **Details** *(list) --*

      For the ``Modify`` action, a list of ``ResourceChangeDetail`` structures that describes
      the changes that AWS CloudFormation will make to the resource.

      - *(dict) --*

        For a resource with ``Modify`` as the action, the ``ResourceChange`` structure
        describes the changes AWS CloudFormation will make to that resource.

        - **Target** *(dict) --*

          A ``ResourceTargetDefinition`` structure that describes the field that AWS
          CloudFormation will change and whether the resource will be recreated.

          - **Attribute** *(string) --*

            Indicates which resource attribute is triggering this update, such as a change in
            the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

          - **Name** *(string) --*

            If the ``Attribute`` value is ``Properties`` , the name of the property. For all
            other attributes, the value is null.

          - **RequiresRecreation** *(string) --*

            If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
            property causes the resource to be recreated. The value can be ``Never`` ,
            ``Always`` , or ``Conditionally`` . To determine the conditions for a
            ``Conditionally`` recreation, see the update behavior for that `property
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
            in the AWS CloudFormation User Guide.

        - **Evaluation** *(string) --*

          Indicates whether AWS CloudFormation can determine the target value, and whether
          the target value will change before you execute a change set.

          For ``Static`` evaluations, AWS CloudFormation can determine that the target value
          will change, and its value. For example, if you directly modify the
          ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this
          property value will change, and its value, so this is a ``Static`` evaluation.

          For ``Dynamic`` evaluations, cannot determine the target value because it depends
          on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt``
          intrinsic function, when the stack is updated. For example, if your template
          includes a reference to a resource that is conditionally recreated, the value of
          the reference (the physical ID of the resource) might change, depending on if the
          resource is recreated. If the resource is recreated, it will have a new physical
          ID, so all references to that resource will also be updated.

        - **ChangeSource** *(string) --*

          The group to which the ``CausingEntity`` value belongs. There are five entity
          groups:

          * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to
          resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` .

          * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template
          parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` .

          * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get
          resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource",
          "PublicDnsName" ] }`` .

          * ``DirectModification`` entities are changes that are made directly to the
          template.

          * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which
          are also known as nested stacks. If you made no changes to the
          ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the
          ``ChangeSource`` to ``Automatic`` because the nested stack's template might have
          changed. Changes to a nested stack's template aren't visible to AWS CloudFormation
          until you run an update on the parent stack.

        - **CausingEntity** *(string) --*

          The identity of the entity that triggered this change. This entity is a member of
          the group that is specified by the ``ChangeSource`` field. For example, if you
          modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the
          name of the parameter (``KeyPairName`` ).

          If the ``ChangeSource`` value is ``DirectModification`` , no value is given for
          ``CausingEntity`` .
    """


_DescribeChangeSetPaginateResponseChangesTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseChangesTypeDef",
    {
        "Type": str,
        "ResourceChange": DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef,
    },
    total=False,
)


class DescribeChangeSetPaginateResponseChangesTypeDef(
    _DescribeChangeSetPaginateResponseChangesTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginateResponse` `Changes`

    The ``Change`` structure describes the changes AWS CloudFormation will perform if you
    execute the change set.

    - **Type** *(string) --*

      The type of entity that AWS CloudFormation changes. Currently, the only entity type is
      ``Resource`` .

    - **ResourceChange** *(dict) --*

      A ``ResourceChange`` structure that describes the resource and action that AWS
      CloudFormation will perform.

      - **Action** *(string) --*

        The action that AWS CloudFormation takes on the resource, such as ``Add`` (adds a new
        resource), ``Modify`` (changes a resource), or ``Remove`` (deletes a resource).

      - **LogicalResourceId** *(string) --*

        The resource's logical ID, which is defined in the stack's template.

      - **PhysicalResourceId** *(string) --*

        The resource's physical ID (resource name). Resources that you are adding don't have
        physical IDs because they haven't been created.

      - **ResourceType** *(string) --*

        The type of AWS CloudFormation resource, such as ``AWS::S3::Bucket`` .

      - **Replacement** *(string) --*

        For the ``Modify`` action, indicates whether AWS CloudFormation will replace the
        resource by creating a new one and deleting the old one. This value depends on the
        value of the ``RequiresRecreation`` property in the ``ResourceTargetDefinition``
        structure. For example, if the ``RequiresRecreation`` field is ``Always`` and the
        ``Evaluation`` field is ``Static`` , ``Replacement`` is ``True`` . If the
        ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Dynamic``
        , ``Replacement`` is ``Conditionally`` .

        If you have multiple changes with different ``RequiresRecreation`` values, the
        ``Replacement`` value depends on the change with the most impact. A
        ``RequiresRecreation`` value of ``Always`` has the most impact, followed by
        ``Conditionally`` , and then ``Never`` .

      - **Scope** *(list) --*

        For the ``Modify`` action, indicates which resource attribute is triggering this
        update, such as a change in the resource attribute's ``Metadata`` , ``Properties`` , or
        ``Tags`` .

        - *(string) --*

      - **Details** *(list) --*

        For the ``Modify`` action, a list of ``ResourceChangeDetail`` structures that describes
        the changes that AWS CloudFormation will make to the resource.

        - *(dict) --*

          For a resource with ``Modify`` as the action, the ``ResourceChange`` structure
          describes the changes AWS CloudFormation will make to that resource.

          - **Target** *(dict) --*

            A ``ResourceTargetDefinition`` structure that describes the field that AWS
            CloudFormation will change and whether the resource will be recreated.

            - **Attribute** *(string) --*

              Indicates which resource attribute is triggering this update, such as a change in
              the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

            - **Name** *(string) --*

              If the ``Attribute`` value is ``Properties`` , the name of the property. For all
              other attributes, the value is null.

            - **RequiresRecreation** *(string) --*

              If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
              property causes the resource to be recreated. The value can be ``Never`` ,
              ``Always`` , or ``Conditionally`` . To determine the conditions for a
              ``Conditionally`` recreation, see the update behavior for that `property
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
              in the AWS CloudFormation User Guide.

          - **Evaluation** *(string) --*

            Indicates whether AWS CloudFormation can determine the target value, and whether
            the target value will change before you execute a change set.

            For ``Static`` evaluations, AWS CloudFormation can determine that the target value
            will change, and its value. For example, if you directly modify the
            ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this
            property value will change, and its value, so this is a ``Static`` evaluation.

            For ``Dynamic`` evaluations, cannot determine the target value because it depends
            on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt``
            intrinsic function, when the stack is updated. For example, if your template
            includes a reference to a resource that is conditionally recreated, the value of
            the reference (the physical ID of the resource) might change, depending on if the
            resource is recreated. If the resource is recreated, it will have a new physical
            ID, so all references to that resource will also be updated.

          - **ChangeSource** *(string) --*

            The group to which the ``CausingEntity`` value belongs. There are five entity
            groups:

            * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to
            resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` .

            * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template
            parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` .

            * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get
            resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource",
            "PublicDnsName" ] }`` .

            * ``DirectModification`` entities are changes that are made directly to the
            template.

            * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which
            are also known as nested stacks. If you made no changes to the
            ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the
            ``ChangeSource`` to ``Automatic`` because the nested stack's template might have
            changed. Changes to a nested stack's template aren't visible to AWS CloudFormation
            until you run an update on the parent stack.

          - **CausingEntity** *(string) --*

            The identity of the entity that triggered this change. This entity is a member of
            the group that is specified by the ``ChangeSource`` field. For example, if you
            modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the
            name of the parameter (``KeyPairName`` ).

            If the ``ChangeSource`` value is ``DirectModification`` , no value is given for
            ``CausingEntity`` .
    """


_DescribeChangeSetPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class DescribeChangeSetPaginateResponseParametersTypeDef(
    _DescribeChangeSetPaginateResponseParametersTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginateResponse` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a
      particular parameter, AWS CloudFormation uses the default value that is specified in your
      template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a
      given parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef(
    _DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginateResponseRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
    any of the alarms you specify goes to ALARM state during the stack operation or within
    the specified monitoring period afterwards, CloudFormation rolls back the entire stack
    operation.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

    - **Type** *(string) --*

      The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef(
    _DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginateResponse` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and
      applies them to any subsequent update operations for the stack, unless you specify
      otherwise. If you do specify rollback triggers for this parameter, those triggers replace
      any list of triggers previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't specify
      this parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating
      the stack or during a previous stack update). Any triggers that you don't include in the
      updated list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
        any of the alarms you specify goes to ALARM state during the stack operation or within
        the specified monitoring period afterwards, CloudFormation rolls back the entire stack
        operation.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - **Type** *(string) --*

          The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the rollback
      triggers after the stack creation or update operation deploys all necessary resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
      still waits the specified period of time before cleaning up old resources after update
      operations. You can use this monitoring period to perform any manual stack validation
      desired, and manually cancel the stack creation or update (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
      triggers during stack creation and update operations. Then, for update operations, it
      begins disposing of old resources immediately once the operation completes.
    """


_DescribeChangeSetPaginateResponseTagsTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeChangeSetPaginateResponseTagsTypeDef(
    _DescribeChangeSetPaginateResponseTagsTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginateResponse` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --*

       *Required* . A string used to identify this tag. You can specify a maximum of 128
       characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
       prefix: ``aws:`` .

    - **Value** *(string) --*

       *Required* . A string containing the value for this tag. You can specify a maximum of
       256 characters for a tag value.
    """


_DescribeChangeSetPaginateResponseTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[DescribeChangeSetPaginateResponseParametersTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": str,
        "Status": str,
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef,
        "Capabilities": List[str],
        "Tags": List[DescribeChangeSetPaginateResponseTagsTypeDef],
        "Changes": List[DescribeChangeSetPaginateResponseChangesTypeDef],
    },
    total=False,
)


class DescribeChangeSetPaginateResponseTypeDef(
    _DescribeChangeSetPaginateResponseTypeDef
):
    """
    Type definition for `DescribeChangeSetPaginate` `Response`

    The output for the  DescribeChangeSet action.

    - **ChangeSetName** *(string) --*

      The name of the change set.

    - **ChangeSetId** *(string) --*

      The ARN of the change set.

    - **StackId** *(string) --*

      The ARN of the stack that is associated with the change set.

    - **StackName** *(string) --*

      The name of the stack that is associated with the change set.

    - **Description** *(string) --*

      Information about the change set.

    - **Parameters** *(list) --*

      A list of ``Parameter`` structures that describes the input parameters and their values used
      to create the change set. For more information, see the `Parameter
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html>`__
      data type.

      - *(dict) --*

        The Parameter data type.

        - **ParameterKey** *(string) --*

          The key associated with the parameter. If you don't specify a key and value for a
          particular parameter, AWS CloudFormation uses the default value that is specified in your
          template.

        - **ParameterValue** *(string) --*

          The input value associated with the parameter.

        - **UsePreviousValue** *(boolean) --*

          During a stack update, use the existing parameter value that the stack is using for a
          given parameter key. If you specify ``true`` , do not specify a parameter value.

        - **ResolvedValue** *(string) --*

          Read-only. The value that corresponds to a Systems Manager parameter key. This field is
          returned only for ` ``SSM`` parameter types
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
          in the template.

    - **CreationTime** *(datetime) --*

      The start time when the change set was created, in UTC.

    - **ExecutionStatus** *(string) --*

      If the change set execution status is ``AVAILABLE`` , you can execute the change set. If you
      can’t execute the change set, the status indicates why. For example, a change set might be in
      an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or in an
      ``OBSOLETE`` state because the stack was already updated.

    - **Status** *(string) --*

      The current status of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` ,
      or ``FAILED`` .

    - **StatusReason** *(string) --*

      A description of the change set's status. For example, if your attempt to create a change set
      failed, AWS CloudFormation shows the error message.

    - **NotificationARNs** *(list) --*

      The ARNs of the Amazon Simple Notification Service (Amazon SNS) topics that will be
      associated with the stack if you execute the change set.

      - *(string) --*

    - **RollbackConfiguration** *(dict) --*

      The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
      operations, and for the specified monitoring period afterwards.

      - **RollbackTriggers** *(list) --*

        The triggers to monitor during stack creation or update actions.

        By default, AWS CloudFormation saves the rollback triggers specified for a stack and
        applies them to any subsequent update operations for the stack, unless you specify
        otherwise. If you do specify rollback triggers for this parameter, those triggers replace
        any list of triggers previously specified for the stack. This means:

        * To use the rollback triggers previously specified for this stack, if any, don't specify
        this parameter.

        * To specify new or updated rollback triggers, you must specify *all* the triggers that you
        want used for this stack, even triggers you've specifed before (for example, when creating
        the stack or during a previous stack update). Any triggers that you don't include in the
        updated list of triggers are no longer applied to the stack.

        * To remove all currently specified triggers, specify an empty list for this parameter.

        If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - *(dict) --*

          A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
          any of the alarms you specify goes to ALARM state during the stack operation or within
          the specified monitoring period afterwards, CloudFormation rolls back the entire stack
          operation.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the rollback trigger.

            If a specified trigger is missing, the entire stack operation fails and is rolled back.

          - **Type** *(string) --*

            The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
            is the only supported resource type.

      - **MonitoringTimeInMinutes** *(integer) --*

        The amount of time, in minutes, during which CloudFormation should monitor all the rollback
        triggers after the stack creation or update operation deploys all necessary resources.

        The default is 0 minutes.

        If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
        still waits the specified period of time before cleaning up old resources after update
        operations. You can use this monitoring period to perform any manual stack validation
        desired, and manually cancel the stack creation or update (using `CancelUpdateStack
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
        , for example) as necessary.

        If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
        triggers during stack creation and update operations. Then, for update operations, it
        begins disposing of old resources immediately once the operation completes.

    - **Capabilities** *(list) --*

      If you execute the change set, the list of capabilities that were explicitly acknowledged
      when the change set was created.

      - *(string) --*

    - **Tags** *(list) --*

      If you execute the change set, the tags that will be associated with the stack.

      - *(dict) --*

        The Tag type enables you to specify a key-value pair that can be used to store information
        about an AWS CloudFormation stack.

        - **Key** *(string) --*

           *Required* . A string used to identify this tag. You can specify a maximum of 128
           characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
           prefix: ``aws:`` .

        - **Value** *(string) --*

           *Required* . A string containing the value for this tag. You can specify a maximum of
           256 characters for a tag value.

    - **Changes** *(list) --*

      A list of ``Change`` structures that describes the resources AWS CloudFormation changes if
      you execute the change set.

      - *(dict) --*

        The ``Change`` structure describes the changes AWS CloudFormation will perform if you
        execute the change set.

        - **Type** *(string) --*

          The type of entity that AWS CloudFormation changes. Currently, the only entity type is
          ``Resource`` .

        - **ResourceChange** *(dict) --*

          A ``ResourceChange`` structure that describes the resource and action that AWS
          CloudFormation will perform.

          - **Action** *(string) --*

            The action that AWS CloudFormation takes on the resource, such as ``Add`` (adds a new
            resource), ``Modify`` (changes a resource), or ``Remove`` (deletes a resource).

          - **LogicalResourceId** *(string) --*

            The resource's logical ID, which is defined in the stack's template.

          - **PhysicalResourceId** *(string) --*

            The resource's physical ID (resource name). Resources that you are adding don't have
            physical IDs because they haven't been created.

          - **ResourceType** *(string) --*

            The type of AWS CloudFormation resource, such as ``AWS::S3::Bucket`` .

          - **Replacement** *(string) --*

            For the ``Modify`` action, indicates whether AWS CloudFormation will replace the
            resource by creating a new one and deleting the old one. This value depends on the
            value of the ``RequiresRecreation`` property in the ``ResourceTargetDefinition``
            structure. For example, if the ``RequiresRecreation`` field is ``Always`` and the
            ``Evaluation`` field is ``Static`` , ``Replacement`` is ``True`` . If the
            ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Dynamic``
            , ``Replacement`` is ``Conditionally`` .

            If you have multiple changes with different ``RequiresRecreation`` values, the
            ``Replacement`` value depends on the change with the most impact. A
            ``RequiresRecreation`` value of ``Always`` has the most impact, followed by
            ``Conditionally`` , and then ``Never`` .

          - **Scope** *(list) --*

            For the ``Modify`` action, indicates which resource attribute is triggering this
            update, such as a change in the resource attribute's ``Metadata`` , ``Properties`` , or
            ``Tags`` .

            - *(string) --*

          - **Details** *(list) --*

            For the ``Modify`` action, a list of ``ResourceChangeDetail`` structures that describes
            the changes that AWS CloudFormation will make to the resource.

            - *(dict) --*

              For a resource with ``Modify`` as the action, the ``ResourceChange`` structure
              describes the changes AWS CloudFormation will make to that resource.

              - **Target** *(dict) --*

                A ``ResourceTargetDefinition`` structure that describes the field that AWS
                CloudFormation will change and whether the resource will be recreated.

                - **Attribute** *(string) --*

                  Indicates which resource attribute is triggering this update, such as a change in
                  the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .

                - **Name** *(string) --*

                  If the ``Attribute`` value is ``Properties`` , the name of the property. For all
                  other attributes, the value is null.

                - **RequiresRecreation** *(string) --*

                  If the ``Attribute`` value is ``Properties`` , indicates whether a change to this
                  property causes the resource to be recreated. The value can be ``Never`` ,
                  ``Always`` , or ``Conditionally`` . To determine the conditions for a
                  ``Conditionally`` recreation, see the update behavior for that `property
                  <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
                  in the AWS CloudFormation User Guide.

              - **Evaluation** *(string) --*

                Indicates whether AWS CloudFormation can determine the target value, and whether
                the target value will change before you execute a change set.

                For ``Static`` evaluations, AWS CloudFormation can determine that the target value
                will change, and its value. For example, if you directly modify the
                ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this
                property value will change, and its value, so this is a ``Static`` evaluation.

                For ``Dynamic`` evaluations, cannot determine the target value because it depends
                on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt``
                intrinsic function, when the stack is updated. For example, if your template
                includes a reference to a resource that is conditionally recreated, the value of
                the reference (the physical ID of the resource) might change, depending on if the
                resource is recreated. If the resource is recreated, it will have a new physical
                ID, so all references to that resource will also be updated.

              - **ChangeSource** *(string) --*

                The group to which the ``CausingEntity`` value belongs. There are five entity
                groups:

                * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to
                resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` .

                * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template
                parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` .

                * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get
                resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource",
                "PublicDnsName" ] }`` .

                * ``DirectModification`` entities are changes that are made directly to the
                template.

                * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which
                are also known as nested stacks. If you made no changes to the
                ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the
                ``ChangeSource`` to ``Automatic`` because the nested stack's template might have
                changed. Changes to a nested stack's template aren't visible to AWS CloudFormation
                until you run an update on the parent stack.

              - **CausingEntity** *(string) --*

                The identity of the entity that triggered this change. This entity is a member of
                the group that is specified by the ``ChangeSource`` field. For example, if you
                modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the
                name of the parameter (``KeyPairName`` ).

                If the ``ChangeSource`` value is ``DirectModification`` , no value is given for
                ``CausingEntity`` .
    """


_DescribeStackEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeStackEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeStackEventsPaginatePaginationConfigTypeDef(
    _DescribeStackEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeStackEventsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeStackEventsPaginateResponseStackEventsTypeDef = TypedDict(
    "_DescribeStackEventsPaginateResponseStackEventsTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": str,
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class DescribeStackEventsPaginateResponseStackEventsTypeDef(
    _DescribeStackEventsPaginateResponseStackEventsTypeDef
):
    """
    Type definition for `DescribeStackEventsPaginateResponse` `StackEvents`

    The StackEvent data type.

    - **StackId** *(string) --*

      The unique ID name of the instance of the stack.

    - **EventId** *(string) --*

      The unique ID of this event.

    - **StackName** *(string) --*

      The name associated with a stack.

    - **LogicalResourceId** *(string) --*

      The logical name of the resource specified in the template.

    - **PhysicalResourceId** *(string) --*

      The name or unique identifier associated with the physical instance of the resource.

    - **ResourceType** *(string) --*

      Type of resource. (For more information, go to `AWS Resource Types Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
      in the AWS CloudFormation User Guide.)

    - **Timestamp** *(datetime) --*

      Time the status was updated.

    - **ResourceStatus** *(string) --*

      Current status of the resource.

    - **ResourceStatusReason** *(string) --*

      Success/failure message associated with the resource.

    - **ResourceProperties** *(string) --*

      BLOB of the properties used to create the resource.

    - **ClientRequestToken** *(string) --*

      The token passed to the operation that generated this event.

      All events triggered by a given stack operation are assigned the same client request
      token, which you can use to track operations. For example, if you execute a
      ``CreateStack`` operation with the token ``token1`` , then all the ``StackEvents``
      generated by that operation will have ``ClientRequestToken`` set as ``token1`` .

      In the console, stack operations display the client request token on the Events tab.
      Stack operations that are initiated from the console use the token format
      *Console-StackOperation-ID* , which helps you easily identify the stack operation . For
      example, if you create a stack using the console, each stack event would be assigned the
      same token in the following format:
      ``Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`` .
    """


_DescribeStackEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeStackEventsPaginateResponseTypeDef",
    {"StackEvents": List[DescribeStackEventsPaginateResponseStackEventsTypeDef]},
    total=False,
)


class DescribeStackEventsPaginateResponseTypeDef(
    _DescribeStackEventsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeStackEventsPaginate` `Response`

    The output for a  DescribeStackEvents action.

    - **StackEvents** *(list) --*

      A list of ``StackEvents`` structures.

      - *(dict) --*

        The StackEvent data type.

        - **StackId** *(string) --*

          The unique ID name of the instance of the stack.

        - **EventId** *(string) --*

          The unique ID of this event.

        - **StackName** *(string) --*

          The name associated with a stack.

        - **LogicalResourceId** *(string) --*

          The logical name of the resource specified in the template.

        - **PhysicalResourceId** *(string) --*

          The name or unique identifier associated with the physical instance of the resource.

        - **ResourceType** *(string) --*

          Type of resource. (For more information, go to `AWS Resource Types Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
          in the AWS CloudFormation User Guide.)

        - **Timestamp** *(datetime) --*

          Time the status was updated.

        - **ResourceStatus** *(string) --*

          Current status of the resource.

        - **ResourceStatusReason** *(string) --*

          Success/failure message associated with the resource.

        - **ResourceProperties** *(string) --*

          BLOB of the properties used to create the resource.

        - **ClientRequestToken** *(string) --*

          The token passed to the operation that generated this event.

          All events triggered by a given stack operation are assigned the same client request
          token, which you can use to track operations. For example, if you execute a
          ``CreateStack`` operation with the token ``token1`` , then all the ``StackEvents``
          generated by that operation will have ``ClientRequestToken`` set as ``token1`` .

          In the console, stack operations display the client request token on the Events tab.
          Stack operations that are initiated from the console use the token format
          *Console-StackOperation-ID* , which helps you easily identify the stack operation . For
          example, if you create a stack using the console, each stack event would be assigned the
          same token in the following format:
          ``Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`` .
    """


_DescribeStacksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeStacksPaginatePaginationConfigTypeDef(
    _DescribeStacksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeStacksPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeStacksPaginateResponseStacksDriftInformationTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksDriftInformationTypeDef",
    {"StackDriftStatus": str, "LastCheckTimestamp": datetime},
    total=False,
)


class DescribeStacksPaginateResponseStacksDriftInformationTypeDef(
    _DescribeStacksPaginateResponseStacksDriftInformationTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `DriftInformation`

    Information on whether a stack's actual configuration differs, or has *drifted* , from
    it's expected configuration, as defined in the stack template and any values specified as
    template parameters. For more information, see `Detecting Unregulated Configuration
    Changes to Stacks and Resources
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **StackDriftStatus** *(string) --*

      Status of the stack's actual configuration compared to its expected template
      configuration.

      * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
      considered to have drifted if one or more of its resources have drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
      expected template configuration.

      * ``IN_SYNC`` : The stack's actual configuration matches its expected template
      configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastCheckTimestamp** *(datetime) --*

      Most recent time when a drift detection operation was initiated on the stack, or any of
      its individual resources that support drift detection.
    """


_DescribeStacksPaginateResponseStacksOutputsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksOutputsTypeDef(
    _DescribeStacksPaginateResponseStacksOutputsTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `Outputs`

    The Output data type.

    - **OutputKey** *(string) --*

      The key associated with the output.

    - **OutputValue** *(string) --*

      The value associated with the output.

    - **Description** *(string) --*

      User defined description associated with the output.

    - **ExportName** *(string) --*

      The name of the export associated with the output.
    """


_DescribeStacksPaginateResponseStacksParametersTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksParametersTypeDef(
    _DescribeStacksPaginateResponseStacksParametersTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a
      particular parameter, AWS CloudFormation uses the default value that is specified in
      your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a
      given parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field
      is returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef(
    _DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacksRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of
    stacks. If any of the alarms you specify goes to ALARM state during the stack
    operation or within the specified monitoring period afterwards, CloudFormation rolls
    back the entire stack operation.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled
      back.

    - **Type** *(string) --*

      The resource type of the rollback trigger. Currently,
      `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef(
    _DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and
    updating operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and
      applies them to any subsequent update operations for the stack, unless you specify
      otherwise. If you do specify rollback triggers for this parameter, those triggers
      replace any list of triggers previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't
      specify this parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that
      you want used for this stack, even triggers you've specifed before (for example, when
      creating the stack or during a previous stack update). Any triggers that you don't
      include in the updated list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of
        stacks. If any of the alarms you specify goes to ALARM state during the stack
        operation or within the specified monitoring period afterwards, CloudFormation rolls
        back the entire stack operation.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled
          back.

        - **Type** *(string) --*

          The resource type of the rollback trigger. Currently,
          `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the
      rollback triggers after the stack creation or update operation deploys all necessary
      resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers,
      CloudFormation still waits the specified period of time before cleaning up old
      resources after update operations. You can use this monitoring period to perform any
      manual stack validation desired, and manually cancel the stack creation or update
      (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified
      rollback triggers during stack creation and update operations. Then, for update
      operations, it begins disposing of old resources immediately once the operation
      completes.
    """


_DescribeStacksPaginateResponseStacksTagsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksTagsTypeDef(
    _DescribeStacksPaginateResponseStacksTagsTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store
    information about an AWS CloudFormation stack.

    - **Key** *(string) --*

       *Required* . A string used to identify this tag. You can specify a maximum of 128
       characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
       prefix: ``aws:`` .

    - **Value** *(string) --*

       *Required* . A string containing the value for this tag. You can specify a maximum
       of 256 characters for a tag value.
    """


_DescribeStacksPaginateResponseStacksTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List[DescribeStacksPaginateResponseStacksParametersTypeDef],
        "CreationTime": datetime,
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef,
        "StackStatus": str,
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[str],
        "Outputs": List[DescribeStacksPaginateResponseStacksOutputsTypeDef],
        "RoleARN": str,
        "Tags": List[DescribeStacksPaginateResponseStacksTagsTypeDef],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": DescribeStacksPaginateResponseStacksDriftInformationTypeDef,
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksTypeDef(
    _DescribeStacksPaginateResponseStacksTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponse` `Stacks`

    The Stack data type.

    - **StackId** *(string) --*

      Unique identifier of the stack.

    - **StackName** *(string) --*

      The name associated with the stack.

    - **ChangeSetId** *(string) --*

      The unique ID of the change set.

    - **Description** *(string) --*

      A user-defined description associated with the stack.

    - **Parameters** *(list) --*

      A list of ``Parameter`` structures.

      - *(dict) --*

        The Parameter data type.

        - **ParameterKey** *(string) --*

          The key associated with the parameter. If you don't specify a key and value for a
          particular parameter, AWS CloudFormation uses the default value that is specified in
          your template.

        - **ParameterValue** *(string) --*

          The input value associated with the parameter.

        - **UsePreviousValue** *(boolean) --*

          During a stack update, use the existing parameter value that the stack is using for a
          given parameter key. If you specify ``true`` , do not specify a parameter value.

        - **ResolvedValue** *(string) --*

          Read-only. The value that corresponds to a Systems Manager parameter key. This field
          is returned only for ` ``SSM`` parameter types
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
          in the template.

    - **CreationTime** *(datetime) --*

      The time at which the stack was created.

    - **DeletionTime** *(datetime) --*

      The time the stack was deleted.

    - **LastUpdatedTime** *(datetime) --*

      The time the stack was last updated. This field will only be returned if the stack has
      been updated at least once.

    - **RollbackConfiguration** *(dict) --*

      The rollback triggers for AWS CloudFormation to monitor during stack creation and
      updating operations, and for the specified monitoring period afterwards.

      - **RollbackTriggers** *(list) --*

        The triggers to monitor during stack creation or update actions.

        By default, AWS CloudFormation saves the rollback triggers specified for a stack and
        applies them to any subsequent update operations for the stack, unless you specify
        otherwise. If you do specify rollback triggers for this parameter, those triggers
        replace any list of triggers previously specified for the stack. This means:

        * To use the rollback triggers previously specified for this stack, if any, don't
        specify this parameter.

        * To specify new or updated rollback triggers, you must specify *all* the triggers that
        you want used for this stack, even triggers you've specifed before (for example, when
        creating the stack or during a previous stack update). Any triggers that you don't
        include in the updated list of triggers are no longer applied to the stack.

        * To remove all currently specified triggers, specify an empty list for this parameter.

        If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - *(dict) --*

          A rollback trigger AWS CloudFormation monitors during creation and updating of
          stacks. If any of the alarms you specify goes to ALARM state during the stack
          operation or within the specified monitoring period afterwards, CloudFormation rolls
          back the entire stack operation.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the rollback trigger.

            If a specified trigger is missing, the entire stack operation fails and is rolled
            back.

          - **Type** *(string) --*

            The resource type of the rollback trigger. Currently,
            `AWS\\:\\:CloudWatch\\:\\:Alarm
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
            is the only supported resource type.

      - **MonitoringTimeInMinutes** *(integer) --*

        The amount of time, in minutes, during which CloudFormation should monitor all the
        rollback triggers after the stack creation or update operation deploys all necessary
        resources.

        The default is 0 minutes.

        If you specify a monitoring period but do not specify any rollback triggers,
        CloudFormation still waits the specified period of time before cleaning up old
        resources after update operations. You can use this monitoring period to perform any
        manual stack validation desired, and manually cancel the stack creation or update
        (using `CancelUpdateStack
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
        , for example) as necessary.

        If you specify 0 for this parameter, CloudFormation still monitors the specified
        rollback triggers during stack creation and update operations. Then, for update
        operations, it begins disposing of old resources immediately once the operation
        completes.

    - **StackStatus** *(string) --*

      Current status of the stack.

    - **StackStatusReason** *(string) --*

      Success/failure message associated with the stack status.

    - **DisableRollback** *(boolean) --*

      Boolean to enable or disable rollback on stack creation failures:

      * ``true`` : disable rollback

      * ``false`` : enable rollback

    - **NotificationARNs** *(list) --*

      SNS topic ARNs to which stack related events are published.

      - *(string) --*

    - **TimeoutInMinutes** *(integer) --*

      The amount of time within which stack creation should complete.

    - **Capabilities** *(list) --*

      The capabilities allowed in the stack.

      - *(string) --*

    - **Outputs** *(list) --*

      A list of output structures.

      - *(dict) --*

        The Output data type.

        - **OutputKey** *(string) --*

          The key associated with the output.

        - **OutputValue** *(string) --*

          The value associated with the output.

        - **Description** *(string) --*

          User defined description associated with the output.

        - **ExportName** *(string) --*

          The name of the export associated with the output.

    - **RoleARN** *(string) --*

      The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that
      is associated with the stack. During a stack operation, AWS CloudFormation uses this
      role's credentials to make calls on your behalf.

    - **Tags** *(list) --*

      A list of ``Tag`` s that specify information about the stack.

      - *(dict) --*

        The Tag type enables you to specify a key-value pair that can be used to store
        information about an AWS CloudFormation stack.

        - **Key** *(string) --*

           *Required* . A string used to identify this tag. You can specify a maximum of 128
           characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
           prefix: ``aws:`` .

        - **Value** *(string) --*

           *Required* . A string containing the value for this tag. You can specify a maximum
           of 256 characters for a tag value.

    - **EnableTerminationProtection** *(boolean) --*

      Whether termination protection is enabled for the stack.

      For `nested stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      , termination protection is set on the root stack and cannot be changed directly on the
      nested stack. For more information, see `Protecting a Stack From Being Deleted
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **ParentId** *(string) --*

      For nested stacks--stacks created as resources for another stack--the stack ID of the
      direct parent of this stack. For the first level of nested stacks, the root stack is also
      the parent stack.

      For more information, see `Working with Nested Stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **RootId** *(string) --*

      For nested stacks--stacks created as resources for another stack--the stack ID of the
      top-level stack to which the nested stack ultimately belongs.

      For more information, see `Working with Nested Stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **DriftInformation** *(dict) --*

      Information on whether a stack's actual configuration differs, or has *drifted* , from
      it's expected configuration, as defined in the stack template and any values specified as
      template parameters. For more information, see `Detecting Unregulated Configuration
      Changes to Stacks and Resources
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .

      - **StackDriftStatus** *(string) --*

        Status of the stack's actual configuration compared to its expected template
        configuration.

        * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
        considered to have drifted if one or more of its resources have drifted.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
        expected template configuration.

        * ``IN_SYNC`` : The stack's actual configuration matches its expected template
        configuration.

        * ``UNKNOWN`` : This value is reserved for future use.

      - **LastCheckTimestamp** *(datetime) --*

        Most recent time when a drift detection operation was initiated on the stack, or any of
        its individual resources that support drift detection.
    """


_DescribeStacksPaginateResponseTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseTypeDef",
    {"Stacks": List[DescribeStacksPaginateResponseStacksTypeDef]},
    total=False,
)


class DescribeStacksPaginateResponseTypeDef(_DescribeStacksPaginateResponseTypeDef):
    """
    Type definition for `DescribeStacksPaginate` `Response`

    The output for a  DescribeStacks action.

    - **Stacks** *(list) --*

      A list of stack structures.

      - *(dict) --*

        The Stack data type.

        - **StackId** *(string) --*

          Unique identifier of the stack.

        - **StackName** *(string) --*

          The name associated with the stack.

        - **ChangeSetId** *(string) --*

          The unique ID of the change set.

        - **Description** *(string) --*

          A user-defined description associated with the stack.

        - **Parameters** *(list) --*

          A list of ``Parameter`` structures.

          - *(dict) --*

            The Parameter data type.

            - **ParameterKey** *(string) --*

              The key associated with the parameter. If you don't specify a key and value for a
              particular parameter, AWS CloudFormation uses the default value that is specified in
              your template.

            - **ParameterValue** *(string) --*

              The input value associated with the parameter.

            - **UsePreviousValue** *(boolean) --*

              During a stack update, use the existing parameter value that the stack is using for a
              given parameter key. If you specify ``true`` , do not specify a parameter value.

            - **ResolvedValue** *(string) --*

              Read-only. The value that corresponds to a Systems Manager parameter key. This field
              is returned only for ` ``SSM`` parameter types
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
              in the template.

        - **CreationTime** *(datetime) --*

          The time at which the stack was created.

        - **DeletionTime** *(datetime) --*

          The time the stack was deleted.

        - **LastUpdatedTime** *(datetime) --*

          The time the stack was last updated. This field will only be returned if the stack has
          been updated at least once.

        - **RollbackConfiguration** *(dict) --*

          The rollback triggers for AWS CloudFormation to monitor during stack creation and
          updating operations, and for the specified monitoring period afterwards.

          - **RollbackTriggers** *(list) --*

            The triggers to monitor during stack creation or update actions.

            By default, AWS CloudFormation saves the rollback triggers specified for a stack and
            applies them to any subsequent update operations for the stack, unless you specify
            otherwise. If you do specify rollback triggers for this parameter, those triggers
            replace any list of triggers previously specified for the stack. This means:

            * To use the rollback triggers previously specified for this stack, if any, don't
            specify this parameter.

            * To specify new or updated rollback triggers, you must specify *all* the triggers that
            you want used for this stack, even triggers you've specifed before (for example, when
            creating the stack or during a previous stack update). Any triggers that you don't
            include in the updated list of triggers are no longer applied to the stack.

            * To remove all currently specified triggers, specify an empty list for this parameter.

            If a specified trigger is missing, the entire stack operation fails and is rolled back.

            - *(dict) --*

              A rollback trigger AWS CloudFormation monitors during creation and updating of
              stacks. If any of the alarms you specify goes to ALARM state during the stack
              operation or within the specified monitoring period afterwards, CloudFormation rolls
              back the entire stack operation.

              - **Arn** *(string) --*

                The Amazon Resource Name (ARN) of the rollback trigger.

                If a specified trigger is missing, the entire stack operation fails and is rolled
                back.

              - **Type** *(string) --*

                The resource type of the rollback trigger. Currently,
                `AWS\\:\\:CloudWatch\\:\\:Alarm
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
                is the only supported resource type.

          - **MonitoringTimeInMinutes** *(integer) --*

            The amount of time, in minutes, during which CloudFormation should monitor all the
            rollback triggers after the stack creation or update operation deploys all necessary
            resources.

            The default is 0 minutes.

            If you specify a monitoring period but do not specify any rollback triggers,
            CloudFormation still waits the specified period of time before cleaning up old
            resources after update operations. You can use this monitoring period to perform any
            manual stack validation desired, and manually cancel the stack creation or update
            (using `CancelUpdateStack
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
            , for example) as necessary.

            If you specify 0 for this parameter, CloudFormation still monitors the specified
            rollback triggers during stack creation and update operations. Then, for update
            operations, it begins disposing of old resources immediately once the operation
            completes.

        - **StackStatus** *(string) --*

          Current status of the stack.

        - **StackStatusReason** *(string) --*

          Success/failure message associated with the stack status.

        - **DisableRollback** *(boolean) --*

          Boolean to enable or disable rollback on stack creation failures:

          * ``true`` : disable rollback

          * ``false`` : enable rollback

        - **NotificationARNs** *(list) --*

          SNS topic ARNs to which stack related events are published.

          - *(string) --*

        - **TimeoutInMinutes** *(integer) --*

          The amount of time within which stack creation should complete.

        - **Capabilities** *(list) --*

          The capabilities allowed in the stack.

          - *(string) --*

        - **Outputs** *(list) --*

          A list of output structures.

          - *(dict) --*

            The Output data type.

            - **OutputKey** *(string) --*

              The key associated with the output.

            - **OutputValue** *(string) --*

              The value associated with the output.

            - **Description** *(string) --*

              User defined description associated with the output.

            - **ExportName** *(string) --*

              The name of the export associated with the output.

        - **RoleARN** *(string) --*

          The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that
          is associated with the stack. During a stack operation, AWS CloudFormation uses this
          role's credentials to make calls on your behalf.

        - **Tags** *(list) --*

          A list of ``Tag`` s that specify information about the stack.

          - *(dict) --*

            The Tag type enables you to specify a key-value pair that can be used to store
            information about an AWS CloudFormation stack.

            - **Key** *(string) --*

               *Required* . A string used to identify this tag. You can specify a maximum of 128
               characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved
               prefix: ``aws:`` .

            - **Value** *(string) --*

               *Required* . A string containing the value for this tag. You can specify a maximum
               of 256 characters for a tag value.

        - **EnableTerminationProtection** *(boolean) --*

          Whether termination protection is enabled for the stack.

          For `nested stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          , termination protection is set on the root stack and cannot be changed directly on the
          nested stack. For more information, see `Protecting a Stack From Being Deleted
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **ParentId** *(string) --*

          For nested stacks--stacks created as resources for another stack--the stack ID of the
          direct parent of this stack. For the first level of nested stacks, the root stack is also
          the parent stack.

          For more information, see `Working with Nested Stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **RootId** *(string) --*

          For nested stacks--stacks created as resources for another stack--the stack ID of the
          top-level stack to which the nested stack ultimately belongs.

          For more information, see `Working with Nested Stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **DriftInformation** *(dict) --*

          Information on whether a stack's actual configuration differs, or has *drifted* , from
          it's expected configuration, as defined in the stack template and any values specified as
          template parameters. For more information, see `Detecting Unregulated Configuration
          Changes to Stacks and Resources
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .

          - **StackDriftStatus** *(string) --*

            Status of the stack's actual configuration compared to its expected template
            configuration.

            * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
            considered to have drifted if one or more of its resources have drifted.

            * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
            expected template configuration.

            * ``IN_SYNC`` : The stack's actual configuration matches its expected template
            configuration.

            * ``UNKNOWN`` : This value is reserved for future use.

          - **LastCheckTimestamp** *(datetime) --*

            Most recent time when a drift detection operation was initiated on the stack, or any of
            its individual resources that support drift detection.
    """


_ListChangeSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListChangeSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListChangeSetsPaginatePaginationConfigTypeDef(
    _ListChangeSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListChangeSetsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListChangeSetsPaginateResponseSummariesTypeDef = TypedDict(
    "_ListChangeSetsPaginateResponseSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": str,
        "Status": str,
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)


class ListChangeSetsPaginateResponseSummariesTypeDef(
    _ListChangeSetsPaginateResponseSummariesTypeDef
):
    """
    Type definition for `ListChangeSetsPaginateResponse` `Summaries`

    The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with
    which it's associated.

    - **StackId** *(string) --*

      The ID of the stack with which the change set is associated.

    - **StackName** *(string) --*

      The name of the stack with which the change set is associated.

    - **ChangeSetId** *(string) --*

      The ID of the change set.

    - **ChangeSetName** *(string) --*

      The name of the change set.

    - **ExecutionStatus** *(string) --*

      If the change set execution status is ``AVAILABLE`` , you can execute the change set. If
      you can’t execute the change set, the status indicates why. For example, a change set
      might be in an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or
      in an ``OBSOLETE`` state because the stack was already updated.

    - **Status** *(string) --*

      The state of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` , or
      ``FAILED`` .

    - **StatusReason** *(string) --*

      A description of the change set's status. For example, if your change set is in the
      ``FAILED`` state, AWS CloudFormation shows the error message.

    - **CreationTime** *(datetime) --*

      The start time when the change set was created, in UTC.

    - **Description** *(string) --*

      Descriptive information about the change set.
    """


_ListChangeSetsPaginateResponseTypeDef = TypedDict(
    "_ListChangeSetsPaginateResponseTypeDef",
    {"Summaries": List[ListChangeSetsPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListChangeSetsPaginateResponseTypeDef(_ListChangeSetsPaginateResponseTypeDef):
    """
    Type definition for `ListChangeSetsPaginate` `Response`

    The output for the  ListChangeSets action.

    - **Summaries** *(list) --*

      A list of ``ChangeSetSummary`` structures that provides the ID and status of each change set
      for the specified stack.

      - *(dict) --*

        The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with
        which it's associated.

        - **StackId** *(string) --*

          The ID of the stack with which the change set is associated.

        - **StackName** *(string) --*

          The name of the stack with which the change set is associated.

        - **ChangeSetId** *(string) --*

          The ID of the change set.

        - **ChangeSetName** *(string) --*

          The name of the change set.

        - **ExecutionStatus** *(string) --*

          If the change set execution status is ``AVAILABLE`` , you can execute the change set. If
          you can’t execute the change set, the status indicates why. For example, a change set
          might be in an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or
          in an ``OBSOLETE`` state because the stack was already updated.

        - **Status** *(string) --*

          The state of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` , or
          ``FAILED`` .

        - **StatusReason** *(string) --*

          A description of the change set's status. For example, if your change set is in the
          ``FAILED`` state, AWS CloudFormation shows the error message.

        - **CreationTime** *(datetime) --*

          The start time when the change set was created, in UTC.

        - **Description** *(string) --*

          Descriptive information about the change set.
    """


_ListExportsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListExportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListExportsPaginatePaginationConfigTypeDef(
    _ListExportsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListExportsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListExportsPaginateResponseExportsTypeDef = TypedDict(
    "_ListExportsPaginateResponseExportsTypeDef",
    {"ExportingStackId": str, "Name": str, "Value": str},
    total=False,
)


class ListExportsPaginateResponseExportsTypeDef(
    _ListExportsPaginateResponseExportsTypeDef
):
    """
    Type definition for `ListExportsPaginateResponse` `Exports`

    The ``Export`` structure describes the exported output values for a stack.

    - **ExportingStackId** *(string) --*

      The stack that contains the exported output name and value.

    - **Name** *(string) --*

      The name of exported output value. Use this name and the ``Fn::ImportValue`` function to
      import the associated value into other stacks. The name is defined in the ``Export``
      field in the associated stack's ``Outputs`` section.

    - **Value** *(string) --*

      The value of the exported output, such as a resource physical ID. This value is defined
      in the ``Export`` field in the associated stack's ``Outputs`` section.
    """


_ListExportsPaginateResponseTypeDef = TypedDict(
    "_ListExportsPaginateResponseTypeDef",
    {"Exports": List[ListExportsPaginateResponseExportsTypeDef]},
    total=False,
)


class ListExportsPaginateResponseTypeDef(_ListExportsPaginateResponseTypeDef):
    """
    Type definition for `ListExportsPaginate` `Response`

    - **Exports** *(list) --*

      The output for the  ListExports action.

      - *(dict) --*

        The ``Export`` structure describes the exported output values for a stack.

        - **ExportingStackId** *(string) --*

          The stack that contains the exported output name and value.

        - **Name** *(string) --*

          The name of exported output value. Use this name and the ``Fn::ImportValue`` function to
          import the associated value into other stacks. The name is defined in the ``Export``
          field in the associated stack's ``Outputs`` section.

        - **Value** *(string) --*

          The value of the exported output, such as a resource physical ID. This value is defined
          in the ``Export`` field in the associated stack's ``Outputs`` section.
    """


_ListImportsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListImportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListImportsPaginatePaginationConfigTypeDef(
    _ListImportsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListImportsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListImportsPaginateResponseTypeDef = TypedDict(
    "_ListImportsPaginateResponseTypeDef", {"Imports": List[str]}, total=False
)


class ListImportsPaginateResponseTypeDef(_ListImportsPaginateResponseTypeDef):
    """
    Type definition for `ListImportsPaginate` `Response`

    - **Imports** *(list) --*

      A list of stack names that are importing the specified exported output value.

      - *(string) --*
    """


_ListStackInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStackInstancesPaginatePaginationConfigTypeDef(
    _ListStackInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStackInstancesPaginate` `PaginationConfig`

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


_ListStackInstancesPaginateResponseSummariesTypeDef = TypedDict(
    "_ListStackInstancesPaginateResponseSummariesTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": str,
        "StatusReason": str,
        "DriftStatus": str,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ListStackInstancesPaginateResponseSummariesTypeDef(
    _ListStackInstancesPaginateResponseSummariesTypeDef
):
    """
    Type definition for `ListStackInstancesPaginateResponse` `Summaries`

    The structure that contains summary information about a stack instance.

    - **StackSetId** *(string) --*

      The name or unique ID of the stack set that the stack instance is associated with.

    - **Region** *(string) --*

      The name of the AWS region that the stack instance is associated with.

    - **Account** *(string) --*

      The name of the AWS account that the stack instance is associated with.

    - **StackId** *(string) --*

      The ID of the stack instance.

    - **Status** *(string) --*

      The status of the stack instance, in terms of its synchronization with its associated
      stack set.

      * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in
      an unstable state. Stacks in this state are excluded from further ``UpdateStackSet``
      operations. You might need to perform a ``DeleteStackInstances`` operation, with
      ``RetainStacks`` set to ``true`` , to delete the stack instance, and then delete the
      stack manually.

      * ``OUTDATED`` : The stack isn't currently up to date with the stack set because:

        * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet``
        operation.

        * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that
        failed or was stopped before the stack was created or updated.

      * ``CURRENT`` : The stack is currently up to date with the stack set.

    - **StatusReason** *(string) --*

      The explanation for the specific status code assigned to this stack instance.

    - **DriftStatus** *(string) --*

      Status of the stack instance's actual configuration compared to the expected template and
      parameter configuration of the stack set to which it belongs.

      * ``DRIFTED`` : The stack differs from the expected template and parameter configuration
      of the stack set to which it belongs. A stack instance is considered to have drifted if
      one or more of the resources in the associated stack have drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack instance differs from
      its expected stack set configuration.

      * ``IN_SYNC`` : The stack instance's actual configuration matches its expected stack set
      configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastDriftCheckTimestamp** *(datetime) --*

      Most recent time when CloudFormation performed a drift detection operation on the stack
      instance. This value will be ``NULL`` for any stack instance on which drift detection has
      not yet been performed.
    """


_ListStackInstancesPaginateResponseTypeDef = TypedDict(
    "_ListStackInstancesPaginateResponseTypeDef",
    {"Summaries": List[ListStackInstancesPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListStackInstancesPaginateResponseTypeDef(
    _ListStackInstancesPaginateResponseTypeDef
):
    """
    Type definition for `ListStackInstancesPaginate` `Response`

    - **Summaries** *(list) --*

      A list of ``StackInstanceSummary`` structures that contain information about the specified
      stack instances.

      - *(dict) --*

        The structure that contains summary information about a stack instance.

        - **StackSetId** *(string) --*

          The name or unique ID of the stack set that the stack instance is associated with.

        - **Region** *(string) --*

          The name of the AWS region that the stack instance is associated with.

        - **Account** *(string) --*

          The name of the AWS account that the stack instance is associated with.

        - **StackId** *(string) --*

          The ID of the stack instance.

        - **Status** *(string) --*

          The status of the stack instance, in terms of its synchronization with its associated
          stack set.

          * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in
          an unstable state. Stacks in this state are excluded from further ``UpdateStackSet``
          operations. You might need to perform a ``DeleteStackInstances`` operation, with
          ``RetainStacks`` set to ``true`` , to delete the stack instance, and then delete the
          stack manually.

          * ``OUTDATED`` : The stack isn't currently up to date with the stack set because:

            * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet``
            operation.

            * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that
            failed or was stopped before the stack was created or updated.

          * ``CURRENT`` : The stack is currently up to date with the stack set.

        - **StatusReason** *(string) --*

          The explanation for the specific status code assigned to this stack instance.

        - **DriftStatus** *(string) --*

          Status of the stack instance's actual configuration compared to the expected template and
          parameter configuration of the stack set to which it belongs.

          * ``DRIFTED`` : The stack differs from the expected template and parameter configuration
          of the stack set to which it belongs. A stack instance is considered to have drifted if
          one or more of the resources in the associated stack have drifted.

          * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack instance differs from
          its expected stack set configuration.

          * ``IN_SYNC`` : The stack instance's actual configuration matches its expected stack set
          configuration.

          * ``UNKNOWN`` : This value is reserved for future use.

        - **LastDriftCheckTimestamp** *(datetime) --*

          Most recent time when CloudFormation performed a drift detection operation on the stack
          instance. This value will be ``NULL`` for any stack instance on which drift detection has
          not yet been performed.
    """


_ListStackResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListStackResourcesPaginatePaginationConfigTypeDef(
    _ListStackResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStackResourcesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef = TypedDict(
    "_ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef",
    {"StackResourceDriftStatus": str, "LastCheckTimestamp": datetime},
    total=False,
)


class ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef(
    _ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef
):
    """
    Type definition for `ListStackResourcesPaginateResponseStackResourceSummaries` `DriftInformation`

    Information about whether the resource's actual configuration differs, or has *drifted* ,
    from its expected configuration, as defined in the stack template and any values
    specified as template parameters. For more information, see `Detecting Unregulated
    Configuration Changes to Stacks and Resources
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **StackResourceDriftStatus** *(string) --*

      Status of the resource's actual configuration compared to its expected configuration

      * ``DELETED`` : The resource differs from its expected configuration in that it has
      been deleted.

      * ``MODIFIED`` : The resource differs from its expected configuration.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
      expected configuration. Any resources that do not currently support drift detection
      have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
      Drift Detection
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
      . If you performed an  ContinueUpdateRollback operation on a stack, any resources
      included in ``ResourcesToSkip`` will also have a status of ``NOT_CHECKED`` . For more
      information on skipping resources during rollback operations, see `Continue Rolling
      Back an Update
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`__
      in the AWS CloudFormation User Guide.

      * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

    - **LastCheckTimestamp** *(datetime) --*

      When AWS CloudFormation last checked if the resource had drifted from its expected
      configuration.
    """


_ListStackResourcesPaginateResponseStackResourceSummariesTypeDef = TypedDict(
    "_ListStackResourcesPaginateResponseStackResourceSummariesTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": str,
        "ResourceStatusReason": str,
        "DriftInformation": ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef,
    },
    total=False,
)


class ListStackResourcesPaginateResponseStackResourceSummariesTypeDef(
    _ListStackResourcesPaginateResponseStackResourceSummariesTypeDef
):
    """
    Type definition for `ListStackResourcesPaginateResponse` `StackResourceSummaries`

    Contains high-level information about the specified stack resource.

    - **LogicalResourceId** *(string) --*

      The logical name of the resource specified in the template.

    - **PhysicalResourceId** *(string) --*

      The name or unique identifier that corresponds to a physical instance ID of the resource.

    - **ResourceType** *(string) --*

      Type of resource. (For more information, go to `AWS Resource Types Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
      in the AWS CloudFormation User Guide.)

    - **LastUpdatedTimestamp** *(datetime) --*

      Time the status was updated.

    - **ResourceStatus** *(string) --*

      Current status of the resource.

    - **ResourceStatusReason** *(string) --*

      Success/failure message associated with the resource.

    - **DriftInformation** *(dict) --*

      Information about whether the resource's actual configuration differs, or has *drifted* ,
      from its expected configuration, as defined in the stack template and any values
      specified as template parameters. For more information, see `Detecting Unregulated
      Configuration Changes to Stacks and Resources
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .

      - **StackResourceDriftStatus** *(string) --*

        Status of the resource's actual configuration compared to its expected configuration

        * ``DELETED`` : The resource differs from its expected configuration in that it has
        been deleted.

        * ``MODIFIED`` : The resource differs from its expected configuration.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
        expected configuration. Any resources that do not currently support drift detection
        have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
        Drift Detection
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
        . If you performed an  ContinueUpdateRollback operation on a stack, any resources
        included in ``ResourcesToSkip`` will also have a status of ``NOT_CHECKED`` . For more
        information on skipping resources during rollback operations, see `Continue Rolling
        Back an Update
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`__
        in the AWS CloudFormation User Guide.

        * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

      - **LastCheckTimestamp** *(datetime) --*

        When AWS CloudFormation last checked if the resource had drifted from its expected
        configuration.
    """


_ListStackResourcesPaginateResponseTypeDef = TypedDict(
    "_ListStackResourcesPaginateResponseTypeDef",
    {
        "StackResourceSummaries": List[
            ListStackResourcesPaginateResponseStackResourceSummariesTypeDef
        ]
    },
    total=False,
)


class ListStackResourcesPaginateResponseTypeDef(
    _ListStackResourcesPaginateResponseTypeDef
):
    """
    Type definition for `ListStackResourcesPaginate` `Response`

    The output for a  ListStackResources action.

    - **StackResourceSummaries** *(list) --*

      A list of ``StackResourceSummary`` structures.

      - *(dict) --*

        Contains high-level information about the specified stack resource.

        - **LogicalResourceId** *(string) --*

          The logical name of the resource specified in the template.

        - **PhysicalResourceId** *(string) --*

          The name or unique identifier that corresponds to a physical instance ID of the resource.

        - **ResourceType** *(string) --*

          Type of resource. (For more information, go to `AWS Resource Types Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__
          in the AWS CloudFormation User Guide.)

        - **LastUpdatedTimestamp** *(datetime) --*

          Time the status was updated.

        - **ResourceStatus** *(string) --*

          Current status of the resource.

        - **ResourceStatusReason** *(string) --*

          Success/failure message associated with the resource.

        - **DriftInformation** *(dict) --*

          Information about whether the resource's actual configuration differs, or has *drifted* ,
          from its expected configuration, as defined in the stack template and any values
          specified as template parameters. For more information, see `Detecting Unregulated
          Configuration Changes to Stacks and Resources
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .

          - **StackResourceDriftStatus** *(string) --*

            Status of the resource's actual configuration compared to its expected configuration

            * ``DELETED`` : The resource differs from its expected configuration in that it has
            been deleted.

            * ``MODIFIED`` : The resource differs from its expected configuration.

            * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its
            expected configuration. Any resources that do not currently support drift detection
            have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support
            Drift Detection
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
            . If you performed an  ContinueUpdateRollback operation on a stack, any resources
            included in ``ResourcesToSkip`` will also have a status of ``NOT_CHECKED`` . For more
            information on skipping resources during rollback operations, see `Continue Rolling
            Back an Update
            <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`__
            in the AWS CloudFormation User Guide.

            * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration.

          - **LastCheckTimestamp** *(datetime) --*

            When AWS CloudFormation last checked if the resource had drifted from its expected
            configuration.
    """


_ListStackSetOperationResultsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackSetOperationResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStackSetOperationResultsPaginatePaginationConfigTypeDef(
    _ListStackSetOperationResultsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStackSetOperationResultsPaginate` `PaginationConfig`

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


_ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef = TypedDict(
    "_ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef",
    {"Status": str, "StatusReason": str},
    total=False,
)


class ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef(
    _ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef
):
    """
    Type definition for `ListStackSetOperationResultsPaginateResponseSummaries` `AccountGateResult`

    The results of the account gate function AWS CloudFormation invokes, if present, before
    proceeding with stack set operations in an account

    - **Status** *(string) --*

      The status of the account gate function.

      * ``SUCCEEDED`` : The account gate function has determined that the account and region
      passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds
      with the stack operation in that account and region.

      * ``FAILED`` : The account gate function has determined that the account and region
      does not meet the requirements for a stack set operation to occur. AWS CloudFormation
      cancels the stack set operation in that account and region, and sets the stack set
      operation result status for that account and region to ``FAILED`` .

      * ``SKIPPED`` : AWS CloudFormation has skipped calling the account gate function for
      this account and region, for one of the following reasons:

        * An account gate function has not been specified for the account and region. AWS
        CloudFormation proceeds with the stack set operation in this account and region.

        * The ``AWSCloudFormationStackSetExecutionRole`` of the stack set adminstration
        account lacks permissions to invoke the function. AWS CloudFormation proceeds with
        the stack set operation in this account and region.

        * Either no action is necessary, or no action is possible, on the stack. AWS
        CloudFormation skips the stack set operation in this account and region.

    - **StatusReason** *(string) --*

      The reason for the account gate status assigned to this account and region for the
      stack set operation.
    """


_ListStackSetOperationResultsPaginateResponseSummariesTypeDef = TypedDict(
    "_ListStackSetOperationResultsPaginateResponseSummariesTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": str,
        "StatusReason": str,
        "AccountGateResult": ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef,
    },
    total=False,
)


class ListStackSetOperationResultsPaginateResponseSummariesTypeDef(
    _ListStackSetOperationResultsPaginateResponseSummariesTypeDef
):
    """
    Type definition for `ListStackSetOperationResultsPaginateResponse` `Summaries`

    The structure that contains information about a specified operation's results for a given
    account in a given region.

    - **Account** *(string) --*

      The name of the AWS account for this operation result.

    - **Region** *(string) --*

      The name of the AWS region for this operation result.

    - **Status** *(string) --*

      The result status of the stack set operation for the given account in the given region.

      * ``CANCELLED`` : The operation in the specified account and region has been cancelled.
      This is either because a user has stopped the stack set operation, or because the failure
      tolerance of the stack set operation has been exceeded.

      * ``FAILED`` : The operation in the specified account and region failed.  If the stack
      set operation fails in enough accounts within a region, the failure tolerance for the
      stack set operation as a whole might be exceeded.

      * ``RUNNING`` : The operation in the specified account and region is currently in
      progress.

      * ``PENDING`` : The operation in the specified account and region has yet to start.

      * ``SUCCEEDED`` : The operation in the specified account and region completed
      successfully.

    - **StatusReason** *(string) --*

      The reason for the assigned result status.

    - **AccountGateResult** *(dict) --*

      The results of the account gate function AWS CloudFormation invokes, if present, before
      proceeding with stack set operations in an account

      - **Status** *(string) --*

        The status of the account gate function.

        * ``SUCCEEDED`` : The account gate function has determined that the account and region
        passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds
        with the stack operation in that account and region.

        * ``FAILED`` : The account gate function has determined that the account and region
        does not meet the requirements for a stack set operation to occur. AWS CloudFormation
        cancels the stack set operation in that account and region, and sets the stack set
        operation result status for that account and region to ``FAILED`` .

        * ``SKIPPED`` : AWS CloudFormation has skipped calling the account gate function for
        this account and region, for one of the following reasons:

          * An account gate function has not been specified for the account and region. AWS
          CloudFormation proceeds with the stack set operation in this account and region.

          * The ``AWSCloudFormationStackSetExecutionRole`` of the stack set adminstration
          account lacks permissions to invoke the function. AWS CloudFormation proceeds with
          the stack set operation in this account and region.

          * Either no action is necessary, or no action is possible, on the stack. AWS
          CloudFormation skips the stack set operation in this account and region.

      - **StatusReason** *(string) --*

        The reason for the account gate status assigned to this account and region for the
        stack set operation.
    """


_ListStackSetOperationResultsPaginateResponseTypeDef = TypedDict(
    "_ListStackSetOperationResultsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetOperationResultsPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListStackSetOperationResultsPaginateResponseTypeDef(
    _ListStackSetOperationResultsPaginateResponseTypeDef
):
    """
    Type definition for `ListStackSetOperationResultsPaginate` `Response`

    - **Summaries** *(list) --*

      A list of ``StackSetOperationResultSummary`` structures that contain information about the
      specified operation results, for accounts and regions that are included in the operation.

      - *(dict) --*

        The structure that contains information about a specified operation's results for a given
        account in a given region.

        - **Account** *(string) --*

          The name of the AWS account for this operation result.

        - **Region** *(string) --*

          The name of the AWS region for this operation result.

        - **Status** *(string) --*

          The result status of the stack set operation for the given account in the given region.

          * ``CANCELLED`` : The operation in the specified account and region has been cancelled.
          This is either because a user has stopped the stack set operation, or because the failure
          tolerance of the stack set operation has been exceeded.

          * ``FAILED`` : The operation in the specified account and region failed.  If the stack
          set operation fails in enough accounts within a region, the failure tolerance for the
          stack set operation as a whole might be exceeded.

          * ``RUNNING`` : The operation in the specified account and region is currently in
          progress.

          * ``PENDING`` : The operation in the specified account and region has yet to start.

          * ``SUCCEEDED`` : The operation in the specified account and region completed
          successfully.

        - **StatusReason** *(string) --*

          The reason for the assigned result status.

        - **AccountGateResult** *(dict) --*

          The results of the account gate function AWS CloudFormation invokes, if present, before
          proceeding with stack set operations in an account

          - **Status** *(string) --*

            The status of the account gate function.

            * ``SUCCEEDED`` : The account gate function has determined that the account and region
            passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds
            with the stack operation in that account and region.

            * ``FAILED`` : The account gate function has determined that the account and region
            does not meet the requirements for a stack set operation to occur. AWS CloudFormation
            cancels the stack set operation in that account and region, and sets the stack set
            operation result status for that account and region to ``FAILED`` .

            * ``SKIPPED`` : AWS CloudFormation has skipped calling the account gate function for
            this account and region, for one of the following reasons:

              * An account gate function has not been specified for the account and region. AWS
              CloudFormation proceeds with the stack set operation in this account and region.

              * The ``AWSCloudFormationStackSetExecutionRole`` of the stack set adminstration
              account lacks permissions to invoke the function. AWS CloudFormation proceeds with
              the stack set operation in this account and region.

              * Either no action is necessary, or no action is possible, on the stack. AWS
              CloudFormation skips the stack set operation in this account and region.

          - **StatusReason** *(string) --*

            The reason for the account gate status assigned to this account and region for the
            stack set operation.
    """


_ListStackSetOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackSetOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStackSetOperationsPaginatePaginationConfigTypeDef(
    _ListStackSetOperationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStackSetOperationsPaginate` `PaginationConfig`

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


_ListStackSetOperationsPaginateResponseSummariesTypeDef = TypedDict(
    "_ListStackSetOperationsPaginateResponseSummariesTypeDef",
    {
        "OperationId": str,
        "Action": str,
        "Status": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)


class ListStackSetOperationsPaginateResponseSummariesTypeDef(
    _ListStackSetOperationsPaginateResponseSummariesTypeDef
):
    """
    Type definition for `ListStackSetOperationsPaginateResponse` `Summaries`

    The structures that contain summary information about the specified operation.

    - **OperationId** *(string) --*

      The unique ID of the stack set operation.

    - **Action** *(string) --*

      The type of operation: ``CREATE`` , ``UPDATE`` , or ``DELETE`` . Create and delete
      operations affect only the specified stack instances that are associated with the
      specified stack set. Update operations affect both the stack set itself as well as *all*
      associated stack set instances.

    - **Status** *(string) --*

      The overall status of the operation.

      * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure
      tolerance value that you've set for an operation is applied for each region during stack
      create and update operations. If the number of failed stacks within a region exceeds the
      failure tolerance, the status of the operation in the region is set to ``FAILED`` . This
      in turn sets the status of the operation as a whole to ``FAILED`` , and AWS
      CloudFormation cancels the operation in any remaining regions.

      * ``RUNNING`` : The operation is currently being performed.

      * ``STOPPED`` : The user has cancelled the operation.

      * ``STOPPING`` : The operation is in the process of stopping, at user request.

      * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks
      without exceeding the failure tolerance for the operation.

    - **CreationTimestamp** *(datetime) --*

      The time at which the operation was initiated. Note that the creation times for the stack
      set operation might differ from the creation time of the individual stacks themselves.
      This is because AWS CloudFormation needs to perform preparatory work for the operation,
      such as dispatching the work to the requested regions, before actually creating the first
      stacks.

    - **EndTimestamp** *(datetime) --*

      The time at which the stack set operation ended, across all accounts and regions
      specified. Note that this doesn't necessarily mean that the stack set operation was
      successful, or even attempted, in each account or region.
    """


_ListStackSetOperationsPaginateResponseTypeDef = TypedDict(
    "_ListStackSetOperationsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetOperationsPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListStackSetOperationsPaginateResponseTypeDef(
    _ListStackSetOperationsPaginateResponseTypeDef
):
    """
    Type definition for `ListStackSetOperationsPaginate` `Response`

    - **Summaries** *(list) --*

      A list of ``StackSetOperationSummary`` structures that contain summary information about
      operations for the specified stack set.

      - *(dict) --*

        The structures that contain summary information about the specified operation.

        - **OperationId** *(string) --*

          The unique ID of the stack set operation.

        - **Action** *(string) --*

          The type of operation: ``CREATE`` , ``UPDATE`` , or ``DELETE`` . Create and delete
          operations affect only the specified stack instances that are associated with the
          specified stack set. Update operations affect both the stack set itself as well as *all*
          associated stack set instances.

        - **Status** *(string) --*

          The overall status of the operation.

          * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure
          tolerance value that you've set for an operation is applied for each region during stack
          create and update operations. If the number of failed stacks within a region exceeds the
          failure tolerance, the status of the operation in the region is set to ``FAILED`` . This
          in turn sets the status of the operation as a whole to ``FAILED`` , and AWS
          CloudFormation cancels the operation in any remaining regions.

          * ``RUNNING`` : The operation is currently being performed.

          * ``STOPPED`` : The user has cancelled the operation.

          * ``STOPPING`` : The operation is in the process of stopping, at user request.

          * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks
          without exceeding the failure tolerance for the operation.

        - **CreationTimestamp** *(datetime) --*

          The time at which the operation was initiated. Note that the creation times for the stack
          set operation might differ from the creation time of the individual stacks themselves.
          This is because AWS CloudFormation needs to perform preparatory work for the operation,
          such as dispatching the work to the requested regions, before actually creating the first
          stacks.

        - **EndTimestamp** *(datetime) --*

          The time at which the stack set operation ended, across all accounts and regions
          specified. Note that this doesn't necessarily mean that the stack set operation was
          successful, or even attempted, in each account or region.
    """


_ListStackSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStackSetsPaginatePaginationConfigTypeDef(
    _ListStackSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStackSetsPaginate` `PaginationConfig`

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


_ListStackSetsPaginateResponseSummariesTypeDef = TypedDict(
    "_ListStackSetsPaginateResponseSummariesTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": str,
        "DriftStatus": str,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ListStackSetsPaginateResponseSummariesTypeDef(
    _ListStackSetsPaginateResponseSummariesTypeDef
):
    """
    Type definition for `ListStackSetsPaginateResponse` `Summaries`

    The structures that contain summary information about the specified stack set.

    - **StackSetName** *(string) --*

      The name of the stack set.

    - **StackSetId** *(string) --*

      The ID of the stack set.

    - **Description** *(string) --*

      A description of the stack set that you specify when the stack set is created or updated.

    - **Status** *(string) --*

      The status of the stack set.

    - **DriftStatus** *(string) --*

      Status of the stack set's actual configuration compared to its expected template and
      parameter configuration. A stack set is considered to have drifted if one or more of its
      stack instances have drifted from their expected template and parameter configuration.

      * ``DRIFTED`` : One or more of the stack instances belonging to the stack set stack
      differs from the expected template and parameter configuration. A stack instance is
      considered to have drifted if one or more of the resources in the associated stack have
      drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked the stack set for drift.

      * ``IN_SYNC`` : All of the stack instances belonging to the stack set stack match from
      the expected template and parameter configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastDriftCheckTimestamp** *(datetime) --*

      Most recent time when CloudFormation performed a drift detection operation on the stack
      set. This value will be ``NULL`` for any stack set on which drift detection has not yet
      been performed.
    """


_ListStackSetsPaginateResponseTypeDef = TypedDict(
    "_ListStackSetsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetsPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListStackSetsPaginateResponseTypeDef(_ListStackSetsPaginateResponseTypeDef):
    """
    Type definition for `ListStackSetsPaginate` `Response`

    - **Summaries** *(list) --*

      A list of ``StackSetSummary`` structures that contain information about the user's stack sets.

      - *(dict) --*

        The structures that contain summary information about the specified stack set.

        - **StackSetName** *(string) --*

          The name of the stack set.

        - **StackSetId** *(string) --*

          The ID of the stack set.

        - **Description** *(string) --*

          A description of the stack set that you specify when the stack set is created or updated.

        - **Status** *(string) --*

          The status of the stack set.

        - **DriftStatus** *(string) --*

          Status of the stack set's actual configuration compared to its expected template and
          parameter configuration. A stack set is considered to have drifted if one or more of its
          stack instances have drifted from their expected template and parameter configuration.

          * ``DRIFTED`` : One or more of the stack instances belonging to the stack set stack
          differs from the expected template and parameter configuration. A stack instance is
          considered to have drifted if one or more of the resources in the associated stack have
          drifted.

          * ``NOT_CHECKED`` : AWS CloudFormation has not checked the stack set for drift.

          * ``IN_SYNC`` : All of the stack instances belonging to the stack set stack match from
          the expected template and parameter configuration.

          * ``UNKNOWN`` : This value is reserved for future use.

        - **LastDriftCheckTimestamp** *(datetime) --*

          Most recent time when CloudFormation performed a drift detection operation on the stack
          set. This value will be ``NULL`` for any stack set on which drift detection has not yet
          been performed.
    """


_ListStacksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListStacksPaginatePaginationConfigTypeDef(
    _ListStacksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStacksPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListStacksPaginateResponseStackSummariesDriftInformationTypeDef = TypedDict(
    "_ListStacksPaginateResponseStackSummariesDriftInformationTypeDef",
    {"StackDriftStatus": str, "LastCheckTimestamp": datetime},
    total=False,
)


class ListStacksPaginateResponseStackSummariesDriftInformationTypeDef(
    _ListStacksPaginateResponseStackSummariesDriftInformationTypeDef
):
    """
    Type definition for `ListStacksPaginateResponseStackSummaries` `DriftInformation`

    Summarizes information on whether a stack's actual configuration differs, or has
    *drifted* , from it's expected configuration, as defined in the stack template and any
    values specified as template parameters. For more information, see `Detecting Unregulated
    Configuration Changes to Stacks and Resources
    <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
    .

    - **StackDriftStatus** *(string) --*

      Status of the stack's actual configuration compared to its expected template
      configuration.

      * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
      considered to have drifted if one or more of its resources have drifted.

      * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
      expected template configuration.

      * ``IN_SYNC`` : The stack's actual configuration matches its expected template
      configuration.

      * ``UNKNOWN`` : This value is reserved for future use.

    - **LastCheckTimestamp** *(datetime) --*

      Most recent time when a drift detection operation was initiated on the stack, or any of
      its individual resources that support drift detection.
    """


_ListStacksPaginateResponseStackSummariesTypeDef = TypedDict(
    "_ListStacksPaginateResponseStackSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "TemplateDescription": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatus": str,
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ListStacksPaginateResponseStackSummariesDriftInformationTypeDef,
    },
    total=False,
)


class ListStacksPaginateResponseStackSummariesTypeDef(
    _ListStacksPaginateResponseStackSummariesTypeDef
):
    """
    Type definition for `ListStacksPaginateResponse` `StackSummaries`

    The StackSummary Data Type

    - **StackId** *(string) --*

      Unique stack identifier.

    - **StackName** *(string) --*

      The name associated with the stack.

    - **TemplateDescription** *(string) --*

      The template description of the template used to create the stack.

    - **CreationTime** *(datetime) --*

      The time the stack was created.

    - **LastUpdatedTime** *(datetime) --*

      The time the stack was last updated. This field will only be returned if the stack has
      been updated at least once.

    - **DeletionTime** *(datetime) --*

      The time the stack was deleted.

    - **StackStatus** *(string) --*

      The current status of the stack.

    - **StackStatusReason** *(string) --*

      Success/Failure message associated with the stack status.

    - **ParentId** *(string) --*

      For nested stacks--stacks created as resources for another stack--the stack ID of the
      direct parent of this stack. For the first level of nested stacks, the root stack is also
      the parent stack.

      For more information, see `Working with Nested Stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **RootId** *(string) --*

      For nested stacks--stacks created as resources for another stack--the stack ID of the
      top-level stack to which the nested stack ultimately belongs.

      For more information, see `Working with Nested Stacks
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
      in the *AWS CloudFormation User Guide* .

    - **DriftInformation** *(dict) --*

      Summarizes information on whether a stack's actual configuration differs, or has
      *drifted* , from it's expected configuration, as defined in the stack template and any
      values specified as template parameters. For more information, see `Detecting Unregulated
      Configuration Changes to Stacks and Resources
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .

      - **StackDriftStatus** *(string) --*

        Status of the stack's actual configuration compared to its expected template
        configuration.

        * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
        considered to have drifted if one or more of its resources have drifted.

        * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
        expected template configuration.

        * ``IN_SYNC`` : The stack's actual configuration matches its expected template
        configuration.

        * ``UNKNOWN`` : This value is reserved for future use.

      - **LastCheckTimestamp** *(datetime) --*

        Most recent time when a drift detection operation was initiated on the stack, or any of
        its individual resources that support drift detection.
    """


_ListStacksPaginateResponseTypeDef = TypedDict(
    "_ListStacksPaginateResponseTypeDef",
    {"StackSummaries": List[ListStacksPaginateResponseStackSummariesTypeDef]},
    total=False,
)


class ListStacksPaginateResponseTypeDef(_ListStacksPaginateResponseTypeDef):
    """
    Type definition for `ListStacksPaginate` `Response`

    The output for  ListStacks action.

    - **StackSummaries** *(list) --*

      A list of ``StackSummary`` structures containing information about the specified stacks.

      - *(dict) --*

        The StackSummary Data Type

        - **StackId** *(string) --*

          Unique stack identifier.

        - **StackName** *(string) --*

          The name associated with the stack.

        - **TemplateDescription** *(string) --*

          The template description of the template used to create the stack.

        - **CreationTime** *(datetime) --*

          The time the stack was created.

        - **LastUpdatedTime** *(datetime) --*

          The time the stack was last updated. This field will only be returned if the stack has
          been updated at least once.

        - **DeletionTime** *(datetime) --*

          The time the stack was deleted.

        - **StackStatus** *(string) --*

          The current status of the stack.

        - **StackStatusReason** *(string) --*

          Success/Failure message associated with the stack status.

        - **ParentId** *(string) --*

          For nested stacks--stacks created as resources for another stack--the stack ID of the
          direct parent of this stack. For the first level of nested stacks, the root stack is also
          the parent stack.

          For more information, see `Working with Nested Stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **RootId** *(string) --*

          For nested stacks--stacks created as resources for another stack--the stack ID of the
          top-level stack to which the nested stack ultimately belongs.

          For more information, see `Working with Nested Stacks
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__
          in the *AWS CloudFormation User Guide* .

        - **DriftInformation** *(dict) --*

          Summarizes information on whether a stack's actual configuration differs, or has
          *drifted* , from it's expected configuration, as defined in the stack template and any
          values specified as template parameters. For more information, see `Detecting Unregulated
          Configuration Changes to Stacks and Resources
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .

          - **StackDriftStatus** *(string) --*

            Status of the stack's actual configuration compared to its expected template
            configuration.

            * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is
            considered to have drifted if one or more of its resources have drifted.

            * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its
            expected template configuration.

            * ``IN_SYNC`` : The stack's actual configuration matches its expected template
            configuration.

            * ``UNKNOWN`` : This value is reserved for future use.

          - **LastCheckTimestamp** *(datetime) --*

            Most recent time when a drift detection operation was initiated on the stack, or any of
            its individual resources that support drift detection.
    """


_ServiceResourceCreateStackParametersTypeDef = TypedDict(
    "_ServiceResourceCreateStackParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class ServiceResourceCreateStackParametersTypeDef(
    _ServiceResourceCreateStackParametersTypeDef
):
    """
    Type definition for `ServiceResourceCreateStack` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
)


class ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef(
    _ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `ServiceResourceCreateStackRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
    of the alarms you specify goes to ALARM state during the stack operation or within the
    specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

    - **Arn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

    - **Type** *(string) --* **[REQUIRED]**

      The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_ServiceResourceCreateStackRollbackConfigurationTypeDef = TypedDict(
    "_ServiceResourceCreateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ServiceResourceCreateStackRollbackConfigurationTypeDef(
    _ServiceResourceCreateStackRollbackConfigurationTypeDef
):
    """
    Type definition for `ServiceResourceCreateStack` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you do
      specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
        of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

        - **Arn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - **Type** *(string) --* **[REQUIRED]**

          The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the rollback
      triggers after the stack creation or update operation deploys all necessary resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
      still waits the specified period of time before cleaning up old resources after update
      operations. You can use this monitoring period to perform any manual stack validation desired,
      and manually cancel the stack creation or update (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
      triggers during stack creation and update operations. Then, for update operations, it begins
      disposing of old resources immediately once the operation completes.
    """


_ServiceResourceCreateStackTagsTypeDef = TypedDict(
    "_ServiceResourceCreateStackTagsTypeDef", {"Key": str, "Value": str}
)


class ServiceResourceCreateStackTagsTypeDef(_ServiceResourceCreateStackTagsTypeDef):
    """
    Type definition for `ServiceResourceCreateStack` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --* **[REQUIRED]**

       *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
       for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

       *Required* . A string containing the value for this tag. You can specify a maximum of 256
       characters for a tag value.
    """


_StackCreateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StackCreateCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StackCreateCompleteWaitWaiterConfigTypeDef(
    _StackCreateCompleteWaitWaiterConfigTypeDef
):
    """
    Type definition for `StackCreateCompleteWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 120
    """


_StackDeleteCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StackDeleteCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StackDeleteCompleteWaitWaiterConfigTypeDef(
    _StackDeleteCompleteWaitWaiterConfigTypeDef
):
    """
    Type definition for `StackDeleteCompleteWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 120
    """


_StackExistsWaitWaiterConfigTypeDef = TypedDict(
    "_StackExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StackExistsWaitWaiterConfigTypeDef(_StackExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `StackExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 20
    """


_StackImportCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StackImportCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StackImportCompleteWaitWaiterConfigTypeDef(
    _StackImportCompleteWaitWaiterConfigTypeDef
):
    """
    Type definition for `StackImportCompleteWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 120
    """


_StackUpdateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StackUpdateCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StackUpdateCompleteWaitWaiterConfigTypeDef(
    _StackUpdateCompleteWaitWaiterConfigTypeDef
):
    """
    Type definition for `StackUpdateCompleteWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 120
    """


_StackUpdateParametersTypeDef = TypedDict(
    "_StackUpdateParametersTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)


class StackUpdateParametersTypeDef(_StackUpdateParametersTypeDef):
    """
    Type definition for `StackUpdate` `Parameters`

    The Parameter data type.

    - **ParameterKey** *(string) --*

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **ParameterValue** *(string) --*

      The input value associated with the parameter.

    - **UsePreviousValue** *(boolean) --*

      During a stack update, use the existing parameter value that the stack is using for a given
      parameter key. If you specify ``true`` , do not specify a parameter value.

    - **ResolvedValue** *(string) --*

      Read-only. The value that corresponds to a Systems Manager parameter key. This field is
      returned only for ` ``SSM`` parameter types
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__
      in the template.
    """


_StackUpdateResponseTypeDef = TypedDict(
    "_StackUpdateResponseTypeDef", {"StackId": str}, total=False
)


class StackUpdateResponseTypeDef(_StackUpdateResponseTypeDef):
    """
    Type definition for `StackUpdate` `Response`

    The output for an  UpdateStack action.

    - **StackId** *(string) --*

      Unique identifier of the stack.
    """


_StackUpdateRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_StackUpdateRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
)


class StackUpdateRollbackConfigurationRollbackTriggersTypeDef(
    _StackUpdateRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `StackUpdateRollbackConfiguration` `RollbackTriggers`

    A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
    of the alarms you specify goes to ALARM state during the stack operation or within the
    specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

    - **Arn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the rollback trigger.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

    - **Type** *(string) --* **[REQUIRED]**

      The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
      is the only supported resource type.
    """


_StackUpdateRollbackConfigurationTypeDef = TypedDict(
    "_StackUpdateRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            StackUpdateRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class StackUpdateRollbackConfigurationTypeDef(_StackUpdateRollbackConfigurationTypeDef):
    """
    Type definition for `StackUpdate` `RollbackConfiguration`

    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.

    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.

      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you do
      specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:

      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.

      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.

      * To remove all currently specified triggers, specify an empty list for this parameter.

      If a specified trigger is missing, the entire stack operation fails and is rolled back.

      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
        of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

        - **Arn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.

          If a specified trigger is missing, the entire stack operation fails and is rolled back.

        - **Type** *(string) --* **[REQUIRED]**

          The resource type of the rollback trigger. Currently, `AWS\\:\\:CloudWatch\\:\\:Alarm
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__
          is the only supported resource type.

    - **MonitoringTimeInMinutes** *(integer) --*

      The amount of time, in minutes, during which CloudFormation should monitor all the rollback
      triggers after the stack creation or update operation deploys all necessary resources.

      The default is 0 minutes.

      If you specify a monitoring period but do not specify any rollback triggers, CloudFormation
      still waits the specified period of time before cleaning up old resources after update
      operations. You can use this monitoring period to perform any manual stack validation desired,
      and manually cancel the stack creation or update (using `CancelUpdateStack
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__
      , for example) as necessary.

      If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
      triggers during stack creation and update operations. Then, for update operations, it begins
      disposing of old resources immediately once the operation completes.
    """


_StackUpdateTagsTypeDef = TypedDict(
    "_StackUpdateTagsTypeDef", {"Key": str, "Value": str}
)


class StackUpdateTagsTypeDef(_StackUpdateTagsTypeDef):
    """
    Type definition for `StackUpdate` `Tags`

    The Tag type enables you to specify a key-value pair that can be used to store information
    about an AWS CloudFormation stack.

    - **Key** *(string) --* **[REQUIRED]**

       *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
       for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

       *Required* . A string containing the value for this tag. You can specify a maximum of 256
       characters for a tag value.
    """


_TypeRegistrationCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_TypeRegistrationCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class TypeRegistrationCompleteWaitWaiterConfigTypeDef(
    _TypeRegistrationCompleteWaitWaiterConfigTypeDef
):
    """
    Type definition for `TypeRegistrationCompleteWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 120
    """
