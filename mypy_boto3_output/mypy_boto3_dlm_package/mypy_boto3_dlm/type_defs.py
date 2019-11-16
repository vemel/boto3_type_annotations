"Main interface for dlm type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsTypeDef",
    "ClientCreateLifecyclePolicyResponseTypeDef",
    "ClientGetLifecyclePoliciesResponsePoliciesTypeDef",
    "ClientGetLifecyclePoliciesResponseTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyTypeDef",
    "ClientGetLifecyclePolicyResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsTypeDef",
)


_ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef
):
    """
    Type definition for `ClientCreateLifecyclePolicyPolicyDetails` `Parameters`

    A set of optional parameters that can be provided by the policy.

    - **ExcludeBootVolume** *(boolean) --*

      When executing an EBS Snapshot Management – Instance policy, execute all CreateSnapshots
      calls with the ``excludeBootVolume`` set to the supplied field. Defaults to false. Only valid
      for EBS Snapshot Management – Instance policies.
    """


_RequiredClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "_RequiredClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str},
)
_OptionalClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "_OptionalClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Times": List[str]},
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef(
    _RequiredClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
    _OptionalClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
):
    """
    Type definition for `ClientCreateLifecyclePolicyPolicyDetailsSchedules` `CreateRule`

    The create rule.

    - **Interval** *(integer) --* **[REQUIRED]**

      The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

    - **IntervalUnit** *(string) --* **[REQUIRED]**

      The interval unit.

    - **Times** *(list) --*

      The time, in UTC, to start the operation. The supported format is hh:mm.

      The operation occurs within a one-hour window following the specified time.

      - *(string) --*
    """


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int},
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef
):
    """
    Type definition for `ClientCreateLifecyclePolicyPolicyDetailsSchedules` `RetainRule`

    The retain rule.

    - **Count** *(integer) --* **[REQUIRED]**

      The number of snapshots to keep for each volume, up to a maximum of 1000.
    """


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef
):
    """
    Type definition for `ClientCreateLifecyclePolicyPolicyDetailsSchedules` `TagsToAdd`

    Specifies a tag for a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The tag value.
    """


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef
):
    """
    Type definition for `ClientCreateLifecyclePolicyPolicyDetailsSchedules` `VariableTags`

    Specifies a tag for a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The tag value.
    """


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[
            ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef
        ],
        "VariableTags": List[
            ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef
        ],
        "CreateRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
    },
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef
):
    """
    Type definition for `ClientCreateLifecyclePolicyPolicyDetails` `Schedules`

    Specifies a schedule.

    - **Name** *(string) --*

      The name of the schedule.

    - **CopyTags** *(boolean) --*

      Copy all user-defined tags on a source volume to snapshots of the volume created by this
      policy.

    - **TagsToAdd** *(list) --*

      The tags to apply to policy-created resources. These user-defined tags are in addition to
      the AWS-added lifecycle tags.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --* **[REQUIRED]**

          The tag key.

        - **Value** *(string) --* **[REQUIRED]**

          The tag value.

    - **VariableTags** *(list) --*

      A collection of key/value pairs with values determined dynamically when the policy is
      executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two
      following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only valid
      for EBS Snapshot Management – Instance policies.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --* **[REQUIRED]**

          The tag key.

        - **Value** *(string) --* **[REQUIRED]**

          The tag value.

    - **CreateRule** *(dict) --*

      The create rule.

      - **Interval** *(integer) --* **[REQUIRED]**

        The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

      - **IntervalUnit** *(string) --* **[REQUIRED]**

        The interval unit.

      - **Times** *(list) --*

        The time, in UTC, to start the operation. The supported format is hh:mm.

        The operation occurs within a one-hour window following the specified time.

        - *(string) --*

    - **RetainRule** *(dict) --*

      The retain rule.

      - **Count** *(integer) --* **[REQUIRED]**

        The number of snapshots to keep for each volume, up to a maximum of 1000.
    """


_ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
)


class ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef
):
    """
    Type definition for `ClientCreateLifecyclePolicyPolicyDetails` `TargetTags`

    Specifies a tag for a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The tag value.
    """


_ClientCreateLifecyclePolicyPolicyDetailsTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[str],
        "TargetTags": List[ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef],
        "Schedules": List[ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef],
        "Parameters": ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsTypeDef
):
    """
    Type definition for `ClientCreateLifecyclePolicy` `PolicyDetails`

    The configuration details of the lifecycle policy.

    - **PolicyType** *(string) --*

      This field determines the valid target resource types and actions a policy can manage. This
      field defaults to EBS_SNAPSHOT_MANAGEMENT if not present.

    - **ResourceTypes** *(list) --*

      The resource type.

      - *(string) --*

    - **TargetTags** *(list) --*

      The single tag that identifies targeted resources for this policy.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --* **[REQUIRED]**

          The tag key.

        - **Value** *(string) --* **[REQUIRED]**

          The tag value.

    - **Schedules** *(list) --*

      The schedule of policy-defined actions.

      - *(dict) --*

        Specifies a schedule.

        - **Name** *(string) --*

          The name of the schedule.

        - **CopyTags** *(boolean) --*

          Copy all user-defined tags on a source volume to snapshots of the volume created by this
          policy.

        - **TagsToAdd** *(list) --*

          The tags to apply to policy-created resources. These user-defined tags are in addition to
          the AWS-added lifecycle tags.

          - *(dict) --*

            Specifies a tag for a resource.

            - **Key** *(string) --* **[REQUIRED]**

              The tag key.

            - **Value** *(string) --* **[REQUIRED]**

              The tag value.

        - **VariableTags** *(list) --*

          A collection of key/value pairs with values determined dynamically when the policy is
          executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two
          following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only valid
          for EBS Snapshot Management – Instance policies.

          - *(dict) --*

            Specifies a tag for a resource.

            - **Key** *(string) --* **[REQUIRED]**

              The tag key.

            - **Value** *(string) --* **[REQUIRED]**

              The tag value.

        - **CreateRule** *(dict) --*

          The create rule.

          - **Interval** *(integer) --* **[REQUIRED]**

            The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

          - **IntervalUnit** *(string) --* **[REQUIRED]**

            The interval unit.

          - **Times** *(list) --*

            The time, in UTC, to start the operation. The supported format is hh:mm.

            The operation occurs within a one-hour window following the specified time.

            - *(string) --*

        - **RetainRule** *(dict) --*

          The retain rule.

          - **Count** *(integer) --* **[REQUIRED]**

            The number of snapshots to keep for each volume, up to a maximum of 1000.

    - **Parameters** *(dict) --*

      A set of optional parameters that can be provided by the policy.

      - **ExcludeBootVolume** *(boolean) --*

        When executing an EBS Snapshot Management – Instance policy, execute all CreateSnapshots
        calls with the ``excludeBootVolume`` set to the supplied field. Defaults to false. Only valid
        for EBS Snapshot Management – Instance policies.
    """


_ClientCreateLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyResponseTypeDef", {"PolicyId": str}, total=False
)


class ClientCreateLifecyclePolicyResponseTypeDef(
    _ClientCreateLifecyclePolicyResponseTypeDef
):
    """
    Type definition for `ClientCreateLifecyclePolicy` `Response`

    - **PolicyId** *(string) --*

      The identifier of the lifecycle policy.
    """


_ClientGetLifecyclePoliciesResponsePoliciesTypeDef = TypedDict(
    "_ClientGetLifecyclePoliciesResponsePoliciesTypeDef",
    {"PolicyId": str, "Description": str, "State": str, "Tags": Dict[str, str]},
    total=False,
)


class ClientGetLifecyclePoliciesResponsePoliciesTypeDef(
    _ClientGetLifecyclePoliciesResponsePoliciesTypeDef
):
    """
    Type definition for `ClientGetLifecyclePoliciesResponse` `Policies`

    Summary information about a lifecycle policy.

    - **PolicyId** *(string) --*

      The identifier of the lifecycle policy.

    - **Description** *(string) --*

      The description of the lifecycle policy.

    - **State** *(string) --*

      The activation state of the lifecycle policy.

    - **Tags** *(dict) --*

      The tags.

      - *(string) --*

        - *(string) --*
    """


_ClientGetLifecyclePoliciesResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePoliciesResponseTypeDef",
    {"Policies": List[ClientGetLifecyclePoliciesResponsePoliciesTypeDef]},
    total=False,
)


class ClientGetLifecyclePoliciesResponseTypeDef(
    _ClientGetLifecyclePoliciesResponseTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicies` `Response`

    - **Policies** *(list) --*

      Summary information about the lifecycle policies.

      - *(dict) --*

        Summary information about a lifecycle policy.

        - **PolicyId** *(string) --*

          The identifier of the lifecycle policy.

        - **Description** *(string) --*

          The description of the lifecycle policy.

        - **State** *(string) --*

          The activation state of the lifecycle policy.

        - **Tags** *(dict) --*

          The tags.

          - *(string) --*

            - *(string) --*
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponsePolicyPolicyDetails` `Parameters`

    A set of optional parameters that can be provided by the policy.

    - **ExcludeBootVolume** *(boolean) --*

      When executing an EBS Snapshot Management – Instance policy, execute all
      CreateSnapshots calls with the ``excludeBootVolume`` set to the supplied field.
      Defaults to false. Only valid for EBS Snapshot Management – Instance policies.
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str, "Times": List[str]},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedules` `CreateRule`

    The create rule.

    - **Interval** *(integer) --*

      The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

    - **IntervalUnit** *(string) --*

      The interval unit.

    - **Times** *(list) --*

      The time, in UTC, to start the operation. The supported format is hh:mm.

      The operation occurs within a one-hour window following the specified time.

      - *(string) --*
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedules` `RetainRule`

    The retain rule.

    - **Count** *(integer) --*

      The number of snapshots to keep for each volume, up to a maximum of 1000.
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedules` `TagsToAdd`

    Specifies a tag for a resource.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The tag value.
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedules` `VariableTags`

    Specifies a tag for a resource.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The tag value.
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef
        ],
        "VariableTags": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef
        ],
        "CreateRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
    },
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponsePolicyPolicyDetails` `Schedules`

    Specifies a schedule.

    - **Name** *(string) --*

      The name of the schedule.

    - **CopyTags** *(boolean) --*

      Copy all user-defined tags on a source volume to snapshots of the volume created by
      this policy.

    - **TagsToAdd** *(list) --*

      The tags to apply to policy-created resources. These user-defined tags are in
      addition to the AWS-added lifecycle tags.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The tag value.

    - **VariableTags** *(list) --*

      A collection of key/value pairs with values determined dynamically when the policy is
      executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two
      following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only
      valid for EBS Snapshot Management – Instance policies.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The tag value.

    - **CreateRule** *(dict) --*

      The create rule.

      - **Interval** *(integer) --*

        The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

      - **IntervalUnit** *(string) --*

        The interval unit.

      - **Times** *(list) --*

        The time, in UTC, to start the operation. The supported format is hh:mm.

        The operation occurs within a one-hour window following the specified time.

        - *(string) --*

    - **RetainRule** *(dict) --*

      The retain rule.

      - **Count** *(integer) --*

        The number of snapshots to keep for each volume, up to a maximum of 1000.
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponsePolicyPolicyDetails` `TargetTags`

    Specifies a tag for a resource.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The tag value.
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[str],
        "TargetTags": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef
        ],
        "Schedules": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef
        ],
        "Parameters": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponsePolicy` `PolicyDetails`

    The configuration of the lifecycle policy

    - **PolicyType** *(string) --*

      This field determines the valid target resource types and actions a policy can manage.
      This field defaults to EBS_SNAPSHOT_MANAGEMENT if not present.

    - **ResourceTypes** *(list) --*

      The resource type.

      - *(string) --*

    - **TargetTags** *(list) --*

      The single tag that identifies targeted resources for this policy.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The tag value.

    - **Schedules** *(list) --*

      The schedule of policy-defined actions.

      - *(dict) --*

        Specifies a schedule.

        - **Name** *(string) --*

          The name of the schedule.

        - **CopyTags** *(boolean) --*

          Copy all user-defined tags on a source volume to snapshots of the volume created by
          this policy.

        - **TagsToAdd** *(list) --*

          The tags to apply to policy-created resources. These user-defined tags are in
          addition to the AWS-added lifecycle tags.

          - *(dict) --*

            Specifies a tag for a resource.

            - **Key** *(string) --*

              The tag key.

            - **Value** *(string) --*

              The tag value.

        - **VariableTags** *(list) --*

          A collection of key/value pairs with values determined dynamically when the policy is
          executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two
          following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only
          valid for EBS Snapshot Management – Instance policies.

          - *(dict) --*

            Specifies a tag for a resource.

            - **Key** *(string) --*

              The tag key.

            - **Value** *(string) --*

              The tag value.

        - **CreateRule** *(dict) --*

          The create rule.

          - **Interval** *(integer) --*

            The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

          - **IntervalUnit** *(string) --*

            The interval unit.

          - **Times** *(list) --*

            The time, in UTC, to start the operation. The supported format is hh:mm.

            The operation occurs within a one-hour window following the specified time.

            - *(string) --*

        - **RetainRule** *(dict) --*

          The retain rule.

          - **Count** *(integer) --*

            The number of snapshots to keep for each volume, up to a maximum of 1000.

    - **Parameters** *(dict) --*

      A set of optional parameters that can be provided by the policy.

      - **ExcludeBootVolume** *(boolean) --*

        When executing an EBS Snapshot Management – Instance policy, execute all
        CreateSnapshots calls with the ``excludeBootVolume`` set to the supplied field.
        Defaults to false. Only valid for EBS Snapshot Management – Instance policies.
    """


_ClientGetLifecyclePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": str,
        "StatusMessage": str,
        "ExecutionRoleArn": str,
        "DateCreated": datetime,
        "DateModified": datetime,
        "PolicyDetails": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef,
        "Tags": Dict[str, str],
        "PolicyArn": str,
    },
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyResponse` `Policy`

    Detailed information about the lifecycle policy.

    - **PolicyId** *(string) --*

      The identifier of the lifecycle policy.

    - **Description** *(string) --*

      The description of the lifecycle policy.

    - **State** *(string) --*

      The activation state of the lifecycle policy.

    - **StatusMessage** *(string) --*

      The description of the status.

    - **ExecutionRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the
      lifecycle policy.

    - **DateCreated** *(datetime) --*

      The local date and time when the lifecycle policy was created.

    - **DateModified** *(datetime) --*

      The local date and time when the lifecycle policy was last modified.

    - **PolicyDetails** *(dict) --*

      The configuration of the lifecycle policy

      - **PolicyType** *(string) --*

        This field determines the valid target resource types and actions a policy can manage.
        This field defaults to EBS_SNAPSHOT_MANAGEMENT if not present.

      - **ResourceTypes** *(list) --*

        The resource type.

        - *(string) --*

      - **TargetTags** *(list) --*

        The single tag that identifies targeted resources for this policy.

        - *(dict) --*

          Specifies a tag for a resource.

          - **Key** *(string) --*

            The tag key.

          - **Value** *(string) --*

            The tag value.

      - **Schedules** *(list) --*

        The schedule of policy-defined actions.

        - *(dict) --*

          Specifies a schedule.

          - **Name** *(string) --*

            The name of the schedule.

          - **CopyTags** *(boolean) --*

            Copy all user-defined tags on a source volume to snapshots of the volume created by
            this policy.

          - **TagsToAdd** *(list) --*

            The tags to apply to policy-created resources. These user-defined tags are in
            addition to the AWS-added lifecycle tags.

            - *(dict) --*

              Specifies a tag for a resource.

              - **Key** *(string) --*

                The tag key.

              - **Value** *(string) --*

                The tag value.

          - **VariableTags** *(list) --*

            A collection of key/value pairs with values determined dynamically when the policy is
            executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two
            following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only
            valid for EBS Snapshot Management – Instance policies.

            - *(dict) --*

              Specifies a tag for a resource.

              - **Key** *(string) --*

                The tag key.

              - **Value** *(string) --*

                The tag value.

          - **CreateRule** *(dict) --*

            The create rule.

            - **Interval** *(integer) --*

              The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

            - **IntervalUnit** *(string) --*

              The interval unit.

            - **Times** *(list) --*

              The time, in UTC, to start the operation. The supported format is hh:mm.

              The operation occurs within a one-hour window following the specified time.

              - *(string) --*

          - **RetainRule** *(dict) --*

            The retain rule.

            - **Count** *(integer) --*

              The number of snapshots to keep for each volume, up to a maximum of 1000.

      - **Parameters** *(dict) --*

        A set of optional parameters that can be provided by the policy.

        - **ExcludeBootVolume** *(boolean) --*

          When executing an EBS Snapshot Management – Instance policy, execute all
          CreateSnapshots calls with the ``excludeBootVolume`` set to the supplied field.
          Defaults to false. Only valid for EBS Snapshot Management – Instance policies.

    - **Tags** *(dict) --*

      The tags.

      - *(string) --*

        - *(string) --*

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN) of the policy.
    """


_ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponseTypeDef",
    {"Policy": ClientGetLifecyclePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientGetLifecyclePolicyResponseTypeDef(_ClientGetLifecyclePolicyResponseTypeDef):
    """
    Type definition for `ClientGetLifecyclePolicy` `Response`

    - **Policy** *(dict) --*

      Detailed information about the lifecycle policy.

      - **PolicyId** *(string) --*

        The identifier of the lifecycle policy.

      - **Description** *(string) --*

        The description of the lifecycle policy.

      - **State** *(string) --*

        The activation state of the lifecycle policy.

      - **StatusMessage** *(string) --*

        The description of the status.

      - **ExecutionRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the
        lifecycle policy.

      - **DateCreated** *(datetime) --*

        The local date and time when the lifecycle policy was created.

      - **DateModified** *(datetime) --*

        The local date and time when the lifecycle policy was last modified.

      - **PolicyDetails** *(dict) --*

        The configuration of the lifecycle policy

        - **PolicyType** *(string) --*

          This field determines the valid target resource types and actions a policy can manage.
          This field defaults to EBS_SNAPSHOT_MANAGEMENT if not present.

        - **ResourceTypes** *(list) --*

          The resource type.

          - *(string) --*

        - **TargetTags** *(list) --*

          The single tag that identifies targeted resources for this policy.

          - *(dict) --*

            Specifies a tag for a resource.

            - **Key** *(string) --*

              The tag key.

            - **Value** *(string) --*

              The tag value.

        - **Schedules** *(list) --*

          The schedule of policy-defined actions.

          - *(dict) --*

            Specifies a schedule.

            - **Name** *(string) --*

              The name of the schedule.

            - **CopyTags** *(boolean) --*

              Copy all user-defined tags on a source volume to snapshots of the volume created by
              this policy.

            - **TagsToAdd** *(list) --*

              The tags to apply to policy-created resources. These user-defined tags are in
              addition to the AWS-added lifecycle tags.

              - *(dict) --*

                Specifies a tag for a resource.

                - **Key** *(string) --*

                  The tag key.

                - **Value** *(string) --*

                  The tag value.

            - **VariableTags** *(list) --*

              A collection of key/value pairs with values determined dynamically when the policy is
              executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two
              following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only
              valid for EBS Snapshot Management – Instance policies.

              - *(dict) --*

                Specifies a tag for a resource.

                - **Key** *(string) --*

                  The tag key.

                - **Value** *(string) --*

                  The tag value.

            - **CreateRule** *(dict) --*

              The create rule.

              - **Interval** *(integer) --*

                The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

              - **IntervalUnit** *(string) --*

                The interval unit.

              - **Times** *(list) --*

                The time, in UTC, to start the operation. The supported format is hh:mm.

                The operation occurs within a one-hour window following the specified time.

                - *(string) --*

            - **RetainRule** *(dict) --*

              The retain rule.

              - **Count** *(integer) --*

                The number of snapshots to keep for each volume, up to a maximum of 1000.

        - **Parameters** *(dict) --*

          A set of optional parameters that can be provided by the policy.

          - **ExcludeBootVolume** *(boolean) --*

            When executing an EBS Snapshot Management – Instance policy, execute all
            CreateSnapshots calls with the ``excludeBootVolume`` set to the supplied field.
            Defaults to false. Only valid for EBS Snapshot Management – Instance policies.

      - **Tags** *(dict) --*

        The tags.

        - *(string) --*

          - *(string) --*

      - **PolicyArn** *(string) --*

        The Amazon Resource Name (ARN) of the policy.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(dict) --*

      Information about the tags.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef
):
    """
    Type definition for `ClientUpdateLifecyclePolicyPolicyDetails` `Parameters`

    A set of optional parameters that can be provided by the policy.

    - **ExcludeBootVolume** *(boolean) --*

      When executing an EBS Snapshot Management – Instance policy, execute all CreateSnapshots
      calls with the ``excludeBootVolume`` set to the supplied field. Defaults to false. Only valid
      for EBS Snapshot Management – Instance policies.
    """


_RequiredClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "_RequiredClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str},
)
_OptionalClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "_OptionalClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Times": List[str]},
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef(
    _RequiredClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
    _OptionalClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
):
    """
    Type definition for `ClientUpdateLifecyclePolicyPolicyDetailsSchedules` `CreateRule`

    The create rule.

    - **Interval** *(integer) --* **[REQUIRED]**

      The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

    - **IntervalUnit** *(string) --* **[REQUIRED]**

      The interval unit.

    - **Times** *(list) --*

      The time, in UTC, to start the operation. The supported format is hh:mm.

      The operation occurs within a one-hour window following the specified time.

      - *(string) --*
    """


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int},
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef
):
    """
    Type definition for `ClientUpdateLifecyclePolicyPolicyDetailsSchedules` `RetainRule`

    The retain rule.

    - **Count** *(integer) --* **[REQUIRED]**

      The number of snapshots to keep for each volume, up to a maximum of 1000.
    """


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef
):
    """
    Type definition for `ClientUpdateLifecyclePolicyPolicyDetailsSchedules` `TagsToAdd`

    Specifies a tag for a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The tag value.
    """


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef
):
    """
    Type definition for `ClientUpdateLifecyclePolicyPolicyDetailsSchedules` `VariableTags`

    Specifies a tag for a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The tag value.
    """


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[
            ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef
        ],
        "VariableTags": List[
            ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef
        ],
        "CreateRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
    },
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef
):
    """
    Type definition for `ClientUpdateLifecyclePolicyPolicyDetails` `Schedules`

    Specifies a schedule.

    - **Name** *(string) --*

      The name of the schedule.

    - **CopyTags** *(boolean) --*

      Copy all user-defined tags on a source volume to snapshots of the volume created by this
      policy.

    - **TagsToAdd** *(list) --*

      The tags to apply to policy-created resources. These user-defined tags are in addition to
      the AWS-added lifecycle tags.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --* **[REQUIRED]**

          The tag key.

        - **Value** *(string) --* **[REQUIRED]**

          The tag value.

    - **VariableTags** *(list) --*

      A collection of key/value pairs with values determined dynamically when the policy is
      executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two
      following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only valid
      for EBS Snapshot Management – Instance policies.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --* **[REQUIRED]**

          The tag key.

        - **Value** *(string) --* **[REQUIRED]**

          The tag value.

    - **CreateRule** *(dict) --*

      The create rule.

      - **Interval** *(integer) --* **[REQUIRED]**

        The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

      - **IntervalUnit** *(string) --* **[REQUIRED]**

        The interval unit.

      - **Times** *(list) --*

        The time, in UTC, to start the operation. The supported format is hh:mm.

        The operation occurs within a one-hour window following the specified time.

        - *(string) --*

    - **RetainRule** *(dict) --*

      The retain rule.

      - **Count** *(integer) --* **[REQUIRED]**

        The number of snapshots to keep for each volume, up to a maximum of 1000.
    """


_ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
)


class ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef
):
    """
    Type definition for `ClientUpdateLifecyclePolicyPolicyDetails` `TargetTags`

    Specifies a tag for a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The tag value.
    """


_ClientUpdateLifecyclePolicyPolicyDetailsTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[str],
        "TargetTags": List[ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef],
        "Schedules": List[ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef],
        "Parameters": ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsTypeDef
):
    """
    Type definition for `ClientUpdateLifecyclePolicy` `PolicyDetails`

    The configuration of the lifecycle policy. You cannot update the policy type or the resource type.

    - **PolicyType** *(string) --*

      This field determines the valid target resource types and actions a policy can manage. This
      field defaults to EBS_SNAPSHOT_MANAGEMENT if not present.

    - **ResourceTypes** *(list) --*

      The resource type.

      - *(string) --*

    - **TargetTags** *(list) --*

      The single tag that identifies targeted resources for this policy.

      - *(dict) --*

        Specifies a tag for a resource.

        - **Key** *(string) --* **[REQUIRED]**

          The tag key.

        - **Value** *(string) --* **[REQUIRED]**

          The tag value.

    - **Schedules** *(list) --*

      The schedule of policy-defined actions.

      - *(dict) --*

        Specifies a schedule.

        - **Name** *(string) --*

          The name of the schedule.

        - **CopyTags** *(boolean) --*

          Copy all user-defined tags on a source volume to snapshots of the volume created by this
          policy.

        - **TagsToAdd** *(list) --*

          The tags to apply to policy-created resources. These user-defined tags are in addition to
          the AWS-added lifecycle tags.

          - *(dict) --*

            Specifies a tag for a resource.

            - **Key** *(string) --* **[REQUIRED]**

              The tag key.

            - **Value** *(string) --* **[REQUIRED]**

              The tag value.

        - **VariableTags** *(list) --*

          A collection of key/value pairs with values determined dynamically when the policy is
          executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two
          following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only valid
          for EBS Snapshot Management – Instance policies.

          - *(dict) --*

            Specifies a tag for a resource.

            - **Key** *(string) --* **[REQUIRED]**

              The tag key.

            - **Value** *(string) --* **[REQUIRED]**

              The tag value.

        - **CreateRule** *(dict) --*

          The create rule.

          - **Interval** *(integer) --* **[REQUIRED]**

            The interval between snapshots. The supported values are 2, 3, 4, 6, 8, 12, and 24.

          - **IntervalUnit** *(string) --* **[REQUIRED]**

            The interval unit.

          - **Times** *(list) --*

            The time, in UTC, to start the operation. The supported format is hh:mm.

            The operation occurs within a one-hour window following the specified time.

            - *(string) --*

        - **RetainRule** *(dict) --*

          The retain rule.

          - **Count** *(integer) --* **[REQUIRED]**

            The number of snapshots to keep for each volume, up to a maximum of 1000.

    - **Parameters** *(dict) --*

      A set of optional parameters that can be provided by the policy.

      - **ExcludeBootVolume** *(boolean) --*

        When executing an EBS Snapshot Management – Instance policy, execute all CreateSnapshots
        calls with the ``excludeBootVolume`` set to the supplied field. Defaults to false. Only valid
        for EBS Snapshot Management – Instance policies.
    """
