"Main interface for backup type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef",
    "ClientCreateBackupPlanBackupPlanRulesTypeDef",
    "ClientCreateBackupPlanBackupPlanTypeDef",
    "ClientCreateBackupPlanResponseTypeDef",
    "ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef",
    "ClientCreateBackupSelectionBackupSelectionTypeDef",
    "ClientCreateBackupSelectionResponseTypeDef",
    "ClientCreateBackupVaultResponseTypeDef",
    "ClientDeleteBackupPlanResponseTypeDef",
    "ClientDescribeBackupJobResponseCreatedByTypeDef",
    "ClientDescribeBackupJobResponseTypeDef",
    "ClientDescribeBackupVaultResponseTypeDef",
    "ClientDescribeProtectedResourceResponseTypeDef",
    "ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef",
    "ClientDescribeRecoveryPointResponseCreatedByTypeDef",
    "ClientDescribeRecoveryPointResponseLifecycleTypeDef",
    "ClientDescribeRecoveryPointResponseTypeDef",
    "ClientDescribeRestoreJobResponseTypeDef",
    "ClientExportBackupPlanTemplateResponseTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef",
    "ClientGetBackupPlanFromJsonResponseTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef",
    "ClientGetBackupPlanFromTemplateResponseTypeDef",
    "ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef",
    "ClientGetBackupPlanResponseBackupPlanRulesTypeDef",
    "ClientGetBackupPlanResponseBackupPlanTypeDef",
    "ClientGetBackupPlanResponseTypeDef",
    "ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef",
    "ClientGetBackupSelectionResponseBackupSelectionTypeDef",
    "ClientGetBackupSelectionResponseTypeDef",
    "ClientGetBackupVaultAccessPolicyResponseTypeDef",
    "ClientGetBackupVaultNotificationsResponseTypeDef",
    "ClientGetRecoveryPointRestoreMetadataResponseTypeDef",
    "ClientGetSupportedResourceTypesResponseTypeDef",
    "ClientListBackupJobsResponseBackupJobsCreatedByTypeDef",
    "ClientListBackupJobsResponseBackupJobsTypeDef",
    "ClientListBackupJobsResponseTypeDef",
    "ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef",
    "ClientListBackupPlanTemplatesResponseTypeDef",
    "ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef",
    "ClientListBackupPlanVersionsResponseTypeDef",
    "ClientListBackupPlansResponseBackupPlansListTypeDef",
    "ClientListBackupPlansResponseTypeDef",
    "ClientListBackupSelectionsResponseBackupSelectionsListTypeDef",
    "ClientListBackupSelectionsResponseTypeDef",
    "ClientListBackupVaultsResponseBackupVaultListTypeDef",
    "ClientListBackupVaultsResponseTypeDef",
    "ClientListProtectedResourcesResponseResultsTypeDef",
    "ClientListProtectedResourcesResponseTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseTypeDef",
    "ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef",
    "ClientListRecoveryPointsByResourceResponseTypeDef",
    "ClientListRestoreJobsResponseRestoreJobsTypeDef",
    "ClientListRestoreJobsResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientStartBackupJobLifecycleTypeDef",
    "ClientStartBackupJobResponseTypeDef",
    "ClientStartRestoreJobResponseTypeDef",
    "ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef",
    "ClientUpdateBackupPlanBackupPlanRulesTypeDef",
    "ClientUpdateBackupPlanBackupPlanTypeDef",
    "ClientUpdateBackupPlanResponseTypeDef",
    "ClientUpdateRecoveryPointLifecycleLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseTypeDef",
)


_ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef = TypedDict(
    "_ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef(
    _ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef
):
    """
    Type definition for `ClientCreateBackupPlanBackupPlanRules` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and when it
    expires. AWS Backup will transition and expire backups automatically according to the
    lifecycle that you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
    days. Therefore, the “expire after days” setting must be 90 days greater than the
    “transition to cold after days”. The “transition to cold after days” setting cannot be
    changed after a backup has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold
      storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be
      greater than ``MoveToColdStorageAfterDays`` .
    """


_RequiredClientCreateBackupPlanBackupPlanRulesTypeDef = TypedDict(
    "_RequiredClientCreateBackupPlanBackupPlanRulesTypeDef",
    {"RuleName": str, "TargetBackupVaultName": str},
)
_OptionalClientCreateBackupPlanBackupPlanRulesTypeDef = TypedDict(
    "_OptionalClientCreateBackupPlanBackupPlanRulesTypeDef",
    {
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
    },
    total=False,
)


class ClientCreateBackupPlanBackupPlanRulesTypeDef(
    _RequiredClientCreateBackupPlanBackupPlanRulesTypeDef,
    _OptionalClientCreateBackupPlanBackupPlanRulesTypeDef,
):
    """
    Type definition for `ClientCreateBackupPlanBackupPlan` `Rules`

    Specifies a scheduled task used to back up a selection of resources.

    - **RuleName** *(string) --* **[REQUIRED]**

      >An optional display name for a backup rule.

    - **TargetBackupVaultName** *(string) --* **[REQUIRED]**

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the AWS Region where they are
      created. They consist of lowercase letters, numbers, and hyphens.

    - **ScheduleExpression** *(string) --*

      A CRON expression specifying when AWS Backup initiates a backup job.

    - **StartWindowMinutes** *(integer) --*

      The amount of time in minutes before beginning a backup.

    - **CompletionWindowMinutes** *(integer) --*

      The amount of time AWS Backup attempts a backup before canceling the job and returning an
      error.

    - **Lifecycle** *(dict) --*

      The lifecycle defines when a protected resource is transitioned to cold storage and when it
      expires. AWS Backup will transition and expire backups automatically according to the
      lifecycle that you define.

      Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
      days. Therefore, the “expire after days” setting must be 90 days greater than the
      “transition to cold after days”. The “transition to cold after days” setting cannot be
      changed after a backup has been transitioned to cold.

      - **MoveToColdStorageAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is moved to cold
        storage.

      - **DeleteAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is deleted. Must be
        greater than ``MoveToColdStorageAfterDays`` .

    - **RecoveryPointTags** *(dict) --*

      To help organize your resources, you can assign your own metadata to the resources that you
      create. Each tag is a key-value pair.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateBackupPlanBackupPlanTypeDef = TypedDict(
    "_ClientCreateBackupPlanBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[ClientCreateBackupPlanBackupPlanRulesTypeDef],
    },
)


class ClientCreateBackupPlanBackupPlanTypeDef(_ClientCreateBackupPlanBackupPlanTypeDef):
    """
    Type definition for `ClientCreateBackupPlan` `BackupPlan`

    Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
    ``Rules`` .

    - **BackupPlanName** *(string) --* **[REQUIRED]**

      The display name of a backup plan.

    - **Rules** *(list) --* **[REQUIRED]**

      An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to
      back up a selection of resources.

      - *(dict) --*

        Specifies a scheduled task used to back up a selection of resources.

        - **RuleName** *(string) --* **[REQUIRED]**

          >An optional display name for a backup rule.

        - **TargetBackupVaultName** *(string) --* **[REQUIRED]**

          The name of a logical container where backups are stored. Backup vaults are identified by
          names that are unique to the account used to create them and the AWS Region where they are
          created. They consist of lowercase letters, numbers, and hyphens.

        - **ScheduleExpression** *(string) --*

          A CRON expression specifying when AWS Backup initiates a backup job.

        - **StartWindowMinutes** *(integer) --*

          The amount of time in minutes before beginning a backup.

        - **CompletionWindowMinutes** *(integer) --*

          The amount of time AWS Backup attempts a backup before canceling the job and returning an
          error.

        - **Lifecycle** *(dict) --*

          The lifecycle defines when a protected resource is transitioned to cold storage and when it
          expires. AWS Backup will transition and expire backups automatically according to the
          lifecycle that you define.

          Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
          days. Therefore, the “expire after days” setting must be 90 days greater than the
          “transition to cold after days”. The “transition to cold after days” setting cannot be
          changed after a backup has been transitioned to cold.

          - **MoveToColdStorageAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is moved to cold
            storage.

          - **DeleteAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is deleted. Must be
            greater than ``MoveToColdStorageAfterDays`` .

        - **RecoveryPointTags** *(dict) --*

          To help organize your resources, you can assign your own metadata to the resources that you
          create. Each tag is a key-value pair.

          - *(string) --*

            - *(string) --*
    """


_ClientCreateBackupPlanResponseTypeDef = TypedDict(
    "_ClientCreateBackupPlanResponseTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
    },
    total=False,
)


class ClientCreateBackupPlanResponseTypeDef(_ClientCreateBackupPlanResponseTypeDef):
    """
    Type definition for `ClientCreateBackupPlan` `Response`

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **CreationDate** *(datetime) --*

      The date and time that a backup plan is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **VersionId** *(string) --*

      Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1024 bytes long.
      They cannot be edited.
    """


_ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef = TypedDict(
    "_ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef",
    {"ConditionType": str, "ConditionKey": str, "ConditionValue": str},
)


class ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef(
    _ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef
):
    """
    Type definition for `ClientCreateBackupSelectionBackupSelection` `ListOfTags`

    Contains an array of triplets made up of a condition type (such as ``StringEquals`` ), a key,
    and a value. Conditions are used to filter resources in a selection that is assigned to a
    backup plan.

    - **ConditionType** *(string) --* **[REQUIRED]**

      An operation, such as ``StringEquals`` , that is applied to a key-value pair used to filter
      resources in a selection.

    - **ConditionKey** *(string) --* **[REQUIRED]**

      The key in a key-value pair. For example, in ``"ec2:ResourceTag/Department": "accounting"``
      , ``"ec2:ResourceTag/Department"`` is the key.

    - **ConditionValue** *(string) --* **[REQUIRED]**

      The value in a key-value pair. For example, in ``"ec2:ResourceTag/Department":
      "accounting"`` , ``"accounting"`` is the value.
    """


_RequiredClientCreateBackupSelectionBackupSelectionTypeDef = TypedDict(
    "_RequiredClientCreateBackupSelectionBackupSelectionTypeDef",
    {"SelectionName": str, "IamRoleArn": str},
)
_OptionalClientCreateBackupSelectionBackupSelectionTypeDef = TypedDict(
    "_OptionalClientCreateBackupSelectionBackupSelectionTypeDef",
    {
        "Resources": List[str],
        "ListOfTags": List[ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef],
    },
    total=False,
)


class ClientCreateBackupSelectionBackupSelectionTypeDef(
    _RequiredClientCreateBackupSelectionBackupSelectionTypeDef,
    _OptionalClientCreateBackupSelectionBackupSelectionTypeDef,
):
    """
    Type definition for `ClientCreateBackupSelection` `BackupSelection`

    Specifies the body of a request to assign a set of resources to a backup plan.

    It includes an array of resources, an optional array of patterns to exclude resources, an
    optional role to provide access to the AWS service the resource belongs to, and an optional array
    of tags used to identify a set of resources.

    - **SelectionName** *(string) --* **[REQUIRED]**

      The display name of a resource selection document.

    - **IamRoleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that AWS Backup uses to authenticate when restoring the target
      resource; for example, ``arn:aws:iam::123456789012:role/S3Access`` .

    - **Resources** *(list) --*

      An array of strings that either contain Amazon Resource Names (ARNs) or match patterns such as
      "``arn:aws:ec2:us-east-1:123456789012:volume/*`` " of resources to assign to a backup plan.

      - *(string) --*

    - **ListOfTags** *(list) --*

      An array of conditions used to specify a set of resources to assign to a backup plan; for
      example, ``"StringEquals": {"ec2:ResourceTag/Department": "accounting"`` .

      - *(dict) --*

        Contains an array of triplets made up of a condition type (such as ``StringEquals`` ), a key,
        and a value. Conditions are used to filter resources in a selection that is assigned to a
        backup plan.

        - **ConditionType** *(string) --* **[REQUIRED]**

          An operation, such as ``StringEquals`` , that is applied to a key-value pair used to filter
          resources in a selection.

        - **ConditionKey** *(string) --* **[REQUIRED]**

          The key in a key-value pair. For example, in ``"ec2:ResourceTag/Department": "accounting"``
          , ``"ec2:ResourceTag/Department"`` is the key.

        - **ConditionValue** *(string) --* **[REQUIRED]**

          The value in a key-value pair. For example, in ``"ec2:ResourceTag/Department":
          "accounting"`` , ``"accounting"`` is the value.
    """


_ClientCreateBackupSelectionResponseTypeDef = TypedDict(
    "_ClientCreateBackupSelectionResponseTypeDef",
    {"SelectionId": str, "BackupPlanId": str, "CreationDate": datetime},
    total=False,
)


class ClientCreateBackupSelectionResponseTypeDef(
    _ClientCreateBackupSelectionResponseTypeDef
):
    """
    Type definition for `ClientCreateBackupSelection` `Response`

    - **SelectionId** *(string) --*

      Uniquely identifies the body of a request to assign a set of resources to a backup plan.

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **CreationDate** *(datetime) --*

      The date and time a backup selection is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
    """


_ClientCreateBackupVaultResponseTypeDef = TypedDict(
    "_ClientCreateBackupVaultResponseTypeDef",
    {"BackupVaultName": str, "BackupVaultArn": str, "CreationDate": datetime},
    total=False,
)


class ClientCreateBackupVaultResponseTypeDef(_ClientCreateBackupVaultResponseTypeDef):
    """
    Type definition for `ClientCreateBackupVault` `Response`

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the Region where they are
      created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **CreationDate** *(datetime) --*

      The date and time a backup vault is created, in Unix format and Coordinated Universal Time
      (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
    """


_ClientDeleteBackupPlanResponseTypeDef = TypedDict(
    "_ClientDeleteBackupPlanResponseTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "DeletionDate": datetime,
        "VersionId": str,
    },
    total=False,
)


class ClientDeleteBackupPlanResponseTypeDef(_ClientDeleteBackupPlanResponseTypeDef):
    """
    Type definition for `ClientDeleteBackupPlan` `Response`

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **DeletionDate** *(datetime) --*

      The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time
      (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **VersionId** *(string) --*

      Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long.
      Version Ids cannot be edited.
    """


_ClientDescribeBackupJobResponseCreatedByTypeDef = TypedDict(
    "_ClientDescribeBackupJobResponseCreatedByTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
    },
    total=False,
)


class ClientDescribeBackupJobResponseCreatedByTypeDef(
    _ClientDescribeBackupJobResponseCreatedByTypeDef
):
    """
    Type definition for `ClientDescribeBackupJobResponse` `CreatedBy`

    Contains identifying information about the creation of a backup job, including the
    ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of the
    backup plan that is used to create it.

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **BackupPlanVersion** *(string) --*

      Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most
      1,024 bytes long. They cannot be edited.

    - **BackupRuleId** *(string) --*

      Uniquely identifies a rule used to schedule the backup of a selection of resources.
    """


_ClientDescribeBackupJobResponseTypeDef = TypedDict(
    "_ClientDescribeBackupJobResponseTypeDef",
    {
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": str,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": ClientDescribeBackupJobResponseCreatedByTypeDef,
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
    },
    total=False,
)


class ClientDescribeBackupJobResponseTypeDef(_ClientDescribeBackupJobResponseTypeDef):
    """
    Type definition for `ClientDescribeBackupJob` `Response`

    - **BackupJobId** *(string) --*

      Uniquely identifies a request to AWS Backup to back up a resource.

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the AWS Region where they are
      created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **RecoveryPointArn** *(string) --*

      An ARN that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **ResourceArn** *(string) --*

      An ARN that uniquely identifies a saved resource. The format of the ARN depends on the
      resource type.

    - **CreationDate** *(datetime) --*

      The date and time that a backup job is created, in Unix format and Coordinated Universal Time
      (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CompletionDate** *(datetime) --*

      The date and time that a job to create a backup job is completed, in Unix format and
      Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds.
      For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **State** *(string) --*

      The current state of a resource recovery point.

    - **StatusMessage** *(string) --*

      A detailed message explaining the status of the job to back up a resource.

    - **PercentDone** *(string) --*

      Contains an estimated percentage that is complete of a job at the time the job status was
      queried.

    - **BackupSizeInBytes** *(integer) --*

      The size, in bytes, of a backup.

    - **IamRoleArn** *(string) --*

      Specifies the IAM role ARN used to create the target recovery point; for example,
      ``arn:aws:iam::123456789012:role/S3Access`` .

    - **CreatedBy** *(dict) --*

      Contains identifying information about the creation of a backup job, including the
      ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of the
      backup plan that is used to create it.

      - **BackupPlanId** *(string) --*

        Uniquely identifies a backup plan.

      - **BackupPlanArn** *(string) --*

        An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
        ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

      - **BackupPlanVersion** *(string) --*

        Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most
        1,024 bytes long. They cannot be edited.

      - **BackupRuleId** *(string) --*

        Uniquely identifies a rule used to schedule the backup of a selection of resources.

    - **ResourceType** *(string) --*

      The type of AWS resource to be backed-up; for example, an Amazon Elastic Block Store (Amazon
      EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

    - **BytesTransferred** *(integer) --*

      The size in bytes transferred to a backup vault at the time that the job status was queried.

    - **ExpectedCompletionDate** *(datetime) --*

      The date and time that a job to back up resources is expected to be completed, in Unix format
      and Coordinated Universal Time (UTC). The value of ``ExpectedCompletionDate`` is accurate to
      milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
      12:11:30.087 AM.

    - **StartBy** *(datetime) --*

      Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job must
      be started before it is canceled. The value is calculated by adding the start window to the
      scheduled time. So if the scheduled time were 6:00 PM and the start window is 2 hours, the
      ``StartBy`` time would be 8:00 PM on the date specified. The value of ``StartBy`` is accurate
      to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
      12:11:30.087 AM.
    """


_ClientDescribeBackupVaultResponseTypeDef = TypedDict(
    "_ClientDescribeBackupVaultResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)


class ClientDescribeBackupVaultResponseTypeDef(
    _ClientDescribeBackupVaultResponseTypeDef
):
    """
    Type definition for `ClientDescribeBackupVault` `Response`

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the Region where they are
      created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **EncryptionKeyArn** *(string) --*

      The server-side encryption key that is used to protect your backups; for example,
      ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

    - **CreationDate** *(datetime) --*

      The date and time that a backup vault is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and allows failed requests to be retried without
      the risk of executing the operation twice.

    - **NumberOfRecoveryPoints** *(integer) --*

      The number of recovery points that are stored in a backup vault.
    """


_ClientDescribeProtectedResourceResponseTypeDef = TypedDict(
    "_ClientDescribeProtectedResourceResponseTypeDef",
    {"ResourceArn": str, "ResourceType": str, "LastBackupTime": datetime},
    total=False,
)


class ClientDescribeProtectedResourceResponseTypeDef(
    _ClientDescribeProtectedResourceResponseTypeDef
):
    """
    Type definition for `ClientDescribeProtectedResource` `Response`

    - **ResourceArn** *(string) --*

      An ARN that uniquely identifies a resource. The format of the ARN depends on the resource
      type.

    - **ResourceType** *(string) --*

      The type of AWS resource saved as a recovery point; for example, an EBS volume or an Amazon
      RDS database.

    - **LastBackupTime** *(datetime) --*

      The date and time that a resource was last backed up, in Unix format and Coordinated
      Universal Time (UTC). The value of ``LastBackupTime`` is accurate to milliseconds. For
      example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
    """


_ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef = TypedDict(
    "_ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)


class ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef(
    _ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef
):
    """
    Type definition for `ClientDescribeRecoveryPointResponse` `CalculatedLifecycle`

    A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt``
    timestamps.

    - **MoveToColdStorageAt** *(datetime) --*

      A timestamp that specifies when to transition a recovery point to cold storage.

    - **DeleteAt** *(datetime) --*

      A timestamp that specifies when to delete a recovery point.
    """


_ClientDescribeRecoveryPointResponseCreatedByTypeDef = TypedDict(
    "_ClientDescribeRecoveryPointResponseCreatedByTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
    },
    total=False,
)


class ClientDescribeRecoveryPointResponseCreatedByTypeDef(
    _ClientDescribeRecoveryPointResponseCreatedByTypeDef
):
    """
    Type definition for `ClientDescribeRecoveryPointResponse` `CreatedBy`

    Contains identifying information about the creation of a recovery point, including the
    ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of the
    backup plan used to create it.

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **BackupPlanVersion** *(string) --*

      Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most
      1,024 bytes long. They cannot be edited.

    - **BackupRuleId** *(string) --*

      Uniquely identifies a rule used to schedule the backup of a selection of resources.
    """


_ClientDescribeRecoveryPointResponseLifecycleTypeDef = TypedDict(
    "_ClientDescribeRecoveryPointResponseLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientDescribeRecoveryPointResponseLifecycleTypeDef(
    _ClientDescribeRecoveryPointResponseLifecycleTypeDef
):
    """
    Type definition for `ClientDescribeRecoveryPointResponse` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and when it
    expires. AWS Backup transitions and expires backups automatically according to the lifecycle
    that you define.

    Backups that are transitioned to cold storage must be stored in cold storage for a minimum of
    90 days. Therefore, the “expire after days” setting must be 90 days greater than the
    “transition to cold after days” setting. The “transition to cold after days” setting cannot
    be changed after a backup has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be
      greater than ``MoveToColdStorageAfterDays`` .
    """


_ClientDescribeRecoveryPointResponseTypeDef = TypedDict(
    "_ClientDescribeRecoveryPointResponseTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": ClientDescribeRecoveryPointResponseCreatedByTypeDef,
        "IamRoleArn": str,
        "Status": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef,
        "Lifecycle": ClientDescribeRecoveryPointResponseLifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": str,
        "LastRestoreTime": datetime,
    },
    total=False,
)


class ClientDescribeRecoveryPointResponseTypeDef(
    _ClientDescribeRecoveryPointResponseTypeDef
):
    """
    Type definition for `ClientDescribeRecoveryPoint` `Response`

    - **RecoveryPointArn** *(string) --*

      An ARN that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the Region where they are
      created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An ARN that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **ResourceArn** *(string) --*

      An ARN that uniquely identifies a saved resource. The format of the ARN depends on the
      resource type.

    - **ResourceType** *(string) --*

      The type of AWS resource to save as a recovery point; for example, an Amazon Elastic Block
      Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

    - **CreatedBy** *(dict) --*

      Contains identifying information about the creation of a recovery point, including the
      ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of the
      backup plan used to create it.

      - **BackupPlanId** *(string) --*

        Uniquely identifies a backup plan.

      - **BackupPlanArn** *(string) --*

        An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
        ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

      - **BackupPlanVersion** *(string) --*

        Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most
        1,024 bytes long. They cannot be edited.

      - **BackupRuleId** *(string) --*

        Uniquely identifies a rule used to schedule the backup of a selection of resources.

    - **IamRoleArn** *(string) --*

      Specifies the IAM role ARN used to create the target recovery point; for example,
      ``arn:aws:iam::123456789012:role/S3Access`` .

    - **Status** *(string) --*

      A status code specifying the state of the recovery point.

      .. note::

        A partial status indicates that the recovery point was not successfully re-created and must
        be retried.

    - **CreationDate** *(datetime) --*

      The date and time that a recovery point is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CompletionDate** *(datetime) --*

      The date and time that a job to create a recovery point is completed, in Unix format and
      Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to
      milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
      12:11:30.087 AM.

    - **BackupSizeInBytes** *(integer) --*

      The size, in bytes, of a backup.

    - **CalculatedLifecycle** *(dict) --*

      A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt``
      timestamps.

      - **MoveToColdStorageAt** *(datetime) --*

        A timestamp that specifies when to transition a recovery point to cold storage.

      - **DeleteAt** *(datetime) --*

        A timestamp that specifies when to delete a recovery point.

    - **Lifecycle** *(dict) --*

      The lifecycle defines when a protected resource is transitioned to cold storage and when it
      expires. AWS Backup transitions and expires backups automatically according to the lifecycle
      that you define.

      Backups that are transitioned to cold storage must be stored in cold storage for a minimum of
      90 days. Therefore, the “expire after days” setting must be 90 days greater than the
      “transition to cold after days” setting. The “transition to cold after days” setting cannot
      be changed after a backup has been transitioned to cold.

      - **MoveToColdStorageAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is moved to cold storage.

      - **DeleteAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is deleted. Must be
        greater than ``MoveToColdStorageAfterDays`` .

    - **EncryptionKeyArn** *(string) --*

      The server-side encryption key used to protect your backups; for example,
      ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

    - **IsEncrypted** *(boolean) --*

      A Boolean value that is returned as ``TRUE`` if the specified recovery point is encrypted, or
      ``FALSE`` if the recovery point is not encrypted.

    - **StorageClass** *(string) --*

      Specifies the storage class of the recovery point. Valid values are ``WARM`` or ``COLD`` .

    - **LastRestoreTime** *(datetime) --*

      The date and time that a recovery point was last restored, in Unix format and Coordinated
      Universal Time (UTC). The value of ``LastRestoreTime`` is accurate to milliseconds. For
      example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
    """


_ClientDescribeRestoreJobResponseTypeDef = TypedDict(
    "_ClientDescribeRestoreJobResponseTypeDef",
    {
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": str,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
    },
    total=False,
)


class ClientDescribeRestoreJobResponseTypeDef(_ClientDescribeRestoreJobResponseTypeDef):
    """
    Type definition for `ClientDescribeRestoreJob` `Response`

    - **RestoreJobId** *(string) --*

      Uniquely identifies the job that restores a recovery point.

    - **RecoveryPointArn** *(string) --*

      An ARN that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **CreationDate** *(datetime) --*

      The date and time that a restore job is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CompletionDate** *(datetime) --*

      The date and time that a job to restore a recovery point is completed, in Unix format and
      Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to
      milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
      12:11:30.087 AM.

    - **Status** *(string) --*

      Status code specifying the state of the job that is initiated by AWS Backup to restore a
      recovery point.

    - **StatusMessage** *(string) --*

      A detailed message explaining the status of a job to restore a recovery point.

    - **PercentDone** *(string) --*

      Contains an estimated percentage that is complete of a job at the time the job status was
      queried.

    - **BackupSizeInBytes** *(integer) --*

      The size, in bytes, of the restored resource.

    - **IamRoleArn** *(string) --*

      Specifies the IAM role ARN used to create the target recovery point; for example,
      ``arn:aws:iam::123456789012:role/S3Access`` .

    - **ExpectedCompletionTimeMinutes** *(integer) --*

      The amount of time in minutes that a job restoring a recovery point is expected to take.

    - **CreatedResourceArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a resource whose recovery point is
      being restored. The format of the ARN depends on the resource type of the backed-up resource.
    """


_ClientExportBackupPlanTemplateResponseTypeDef = TypedDict(
    "_ClientExportBackupPlanTemplateResponseTypeDef",
    {"BackupPlanTemplateJson": str},
    total=False,
)


class ClientExportBackupPlanTemplateResponseTypeDef(
    _ClientExportBackupPlanTemplateResponseTypeDef
):
    """
    Type definition for `ClientExportBackupPlanTemplate` `Response`

    - **BackupPlanTemplateJson** *(string) --*

      The body of a backup plan template in JSON format.

      .. note::

        This is a signed JSON document that cannot be modified before being passed to
        ``GetBackupPlanFromJSON.``
    """


_ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef = TypedDict(
    "_ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef(
    _ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef
):
    """
    Type definition for `ClientGetBackupPlanFromJsonResponseBackupPlanRules` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and
    when it expires. AWS Backup transitions and expires backups automatically according to
    the lifecycle that you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
    days. Therefore, the “expire after days” setting must be 90 days greater than the
    “transition to cold after days” setting. The “transition to cold after days” setting
    cannot be changed after a backup has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold
      storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be
      greater than ``MoveToColdStorageAfterDays`` .
    """


_ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef = TypedDict(
    "_ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
    },
    total=False,
)


class ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef(
    _ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef
):
    """
    Type definition for `ClientGetBackupPlanFromJsonResponseBackupPlan` `Rules`

    Specifies a scheduled task used to back up a selection of resources.

    - **RuleName** *(string) --*

      An optional display name for a backup rule.

    - **TargetBackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified
      by names that are unique to the account used to create them and the AWS Region where
      they are created. They consist of lowercase letters, numbers, and hyphens.

    - **ScheduleExpression** *(string) --*

      A CRON expression specifying when AWS Backup initiates a backup job.

    - **StartWindowMinutes** *(integer) --*

      An optional value that specifies a period of time in minutes after a backup is
      scheduled before a job is canceled if it doesn't start successfully.

    - **CompletionWindowMinutes** *(integer) --*

      A value in minutes after a backup job is successfully started before it must be
      completed or it is canceled by AWS Backup. This value is optional.

    - **Lifecycle** *(dict) --*

      The lifecycle defines when a protected resource is transitioned to cold storage and
      when it expires. AWS Backup transitions and expires backups automatically according to
      the lifecycle that you define.

      Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
      days. Therefore, the “expire after days” setting must be 90 days greater than the
      “transition to cold after days” setting. The “transition to cold after days” setting
      cannot be changed after a backup has been transitioned to cold.

      - **MoveToColdStorageAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is moved to cold
        storage.

      - **DeleteAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is deleted. Must be
        greater than ``MoveToColdStorageAfterDays`` .

    - **RecoveryPointTags** *(dict) --*

      An array of key-value pair strings that are assigned to resources that are associated
      with this rule when restored from backup.

      - *(string) --*

        - *(string) --*

    - **RuleId** *(string) --*

      Uniquely identifies a rule that is used to schedule the backup of a selection of
      resources.
    """


_ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef = TypedDict(
    "_ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef],
    },
    total=False,
)


class ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef(
    _ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef
):
    """
    Type definition for `ClientGetBackupPlanFromJsonResponse` `BackupPlan`

    Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
    ``Rules`` .

    - **BackupPlanName** *(string) --*

      The display name of a backup plan.

    - **Rules** *(list) --*

      An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used
      to back up a selection of resources.

      - *(dict) --*

        Specifies a scheduled task used to back up a selection of resources.

        - **RuleName** *(string) --*

          An optional display name for a backup rule.

        - **TargetBackupVaultName** *(string) --*

          The name of a logical container where backups are stored. Backup vaults are identified
          by names that are unique to the account used to create them and the AWS Region where
          they are created. They consist of lowercase letters, numbers, and hyphens.

        - **ScheduleExpression** *(string) --*

          A CRON expression specifying when AWS Backup initiates a backup job.

        - **StartWindowMinutes** *(integer) --*

          An optional value that specifies a period of time in minutes after a backup is
          scheduled before a job is canceled if it doesn't start successfully.

        - **CompletionWindowMinutes** *(integer) --*

          A value in minutes after a backup job is successfully started before it must be
          completed or it is canceled by AWS Backup. This value is optional.

        - **Lifecycle** *(dict) --*

          The lifecycle defines when a protected resource is transitioned to cold storage and
          when it expires. AWS Backup transitions and expires backups automatically according to
          the lifecycle that you define.

          Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
          days. Therefore, the “expire after days” setting must be 90 days greater than the
          “transition to cold after days” setting. The “transition to cold after days” setting
          cannot be changed after a backup has been transitioned to cold.

          - **MoveToColdStorageAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is moved to cold
            storage.

          - **DeleteAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is deleted. Must be
            greater than ``MoveToColdStorageAfterDays`` .

        - **RecoveryPointTags** *(dict) --*

          An array of key-value pair strings that are assigned to resources that are associated
          with this rule when restored from backup.

          - *(string) --*

            - *(string) --*

        - **RuleId** *(string) --*

          Uniquely identifies a rule that is used to schedule the backup of a selection of
          resources.
    """


_ClientGetBackupPlanFromJsonResponseTypeDef = TypedDict(
    "_ClientGetBackupPlanFromJsonResponseTypeDef",
    {"BackupPlan": ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef},
    total=False,
)


class ClientGetBackupPlanFromJsonResponseTypeDef(
    _ClientGetBackupPlanFromJsonResponseTypeDef
):
    """
    Type definition for `ClientGetBackupPlanFromJson` `Response`

    - **BackupPlan** *(dict) --*

      Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
      ``Rules`` .

      - **BackupPlanName** *(string) --*

        The display name of a backup plan.

      - **Rules** *(list) --*

        An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used
        to back up a selection of resources.

        - *(dict) --*

          Specifies a scheduled task used to back up a selection of resources.

          - **RuleName** *(string) --*

            An optional display name for a backup rule.

          - **TargetBackupVaultName** *(string) --*

            The name of a logical container where backups are stored. Backup vaults are identified
            by names that are unique to the account used to create them and the AWS Region where
            they are created. They consist of lowercase letters, numbers, and hyphens.

          - **ScheduleExpression** *(string) --*

            A CRON expression specifying when AWS Backup initiates a backup job.

          - **StartWindowMinutes** *(integer) --*

            An optional value that specifies a period of time in minutes after a backup is
            scheduled before a job is canceled if it doesn't start successfully.

          - **CompletionWindowMinutes** *(integer) --*

            A value in minutes after a backup job is successfully started before it must be
            completed or it is canceled by AWS Backup. This value is optional.

          - **Lifecycle** *(dict) --*

            The lifecycle defines when a protected resource is transitioned to cold storage and
            when it expires. AWS Backup transitions and expires backups automatically according to
            the lifecycle that you define.

            Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
            days. Therefore, the “expire after days” setting must be 90 days greater than the
            “transition to cold after days” setting. The “transition to cold after days” setting
            cannot be changed after a backup has been transitioned to cold.

            - **MoveToColdStorageAfterDays** *(integer) --*

              Specifies the number of days after creation that a recovery point is moved to cold
              storage.

            - **DeleteAfterDays** *(integer) --*

              Specifies the number of days after creation that a recovery point is deleted. Must be
              greater than ``MoveToColdStorageAfterDays`` .

          - **RecoveryPointTags** *(dict) --*

            An array of key-value pair strings that are assigned to resources that are associated
            with this rule when restored from backup.

            - *(string) --*

              - *(string) --*

          - **RuleId** *(string) --*

            Uniquely identifies a rule that is used to schedule the backup of a selection of
            resources.
    """


_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef = TypedDict(
    "_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef(
    _ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef
):
    """
    Type definition for `ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRules` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and
    when it expires. AWS Backup transitions and expires backups automatically according to
    the lifecycle that you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
    days. Therefore, the “expire after days” setting must be 90 days greater than the
    “transition to cold after days” setting. The “transition to cold after days” setting
    cannot be changed after a backup has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold
      storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be
      greater than ``MoveToColdStorageAfterDays`` .
    """


_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef = TypedDict(
    "_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
    },
    total=False,
)


class ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef(
    _ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef
):
    """
    Type definition for `ClientGetBackupPlanFromTemplateResponseBackupPlanDocument` `Rules`

    Specifies a scheduled task used to back up a selection of resources.

    - **RuleName** *(string) --*

      An optional display name for a backup rule.

    - **TargetBackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified
      by names that are unique to the account used to create them and the AWS Region where
      they are created. They consist of lowercase letters, numbers, and hyphens.

    - **ScheduleExpression** *(string) --*

      A CRON expression specifying when AWS Backup initiates a backup job.

    - **StartWindowMinutes** *(integer) --*

      An optional value that specifies a period of time in minutes after a backup is
      scheduled before a job is canceled if it doesn't start successfully.

    - **CompletionWindowMinutes** *(integer) --*

      A value in minutes after a backup job is successfully started before it must be
      completed or it is canceled by AWS Backup. This value is optional.

    - **Lifecycle** *(dict) --*

      The lifecycle defines when a protected resource is transitioned to cold storage and
      when it expires. AWS Backup transitions and expires backups automatically according to
      the lifecycle that you define.

      Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
      days. Therefore, the “expire after days” setting must be 90 days greater than the
      “transition to cold after days” setting. The “transition to cold after days” setting
      cannot be changed after a backup has been transitioned to cold.

      - **MoveToColdStorageAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is moved to cold
        storage.

      - **DeleteAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is deleted. Must be
        greater than ``MoveToColdStorageAfterDays`` .

    - **RecoveryPointTags** *(dict) --*

      An array of key-value pair strings that are assigned to resources that are associated
      with this rule when restored from backup.

      - *(string) --*

        - *(string) --*

    - **RuleId** *(string) --*

      Uniquely identifies a rule that is used to schedule the backup of a selection of
      resources.
    """


_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef = TypedDict(
    "_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[
            ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef
        ],
    },
    total=False,
)


class ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef(
    _ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef
):
    """
    Type definition for `ClientGetBackupPlanFromTemplateResponse` `BackupPlanDocument`

    Returns the body of a backup plan based on the target template, including the name, rules,
    and backup vault of the plan.

    - **BackupPlanName** *(string) --*

      The display name of a backup plan.

    - **Rules** *(list) --*

      An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used
      to back up a selection of resources.

      - *(dict) --*

        Specifies a scheduled task used to back up a selection of resources.

        - **RuleName** *(string) --*

          An optional display name for a backup rule.

        - **TargetBackupVaultName** *(string) --*

          The name of a logical container where backups are stored. Backup vaults are identified
          by names that are unique to the account used to create them and the AWS Region where
          they are created. They consist of lowercase letters, numbers, and hyphens.

        - **ScheduleExpression** *(string) --*

          A CRON expression specifying when AWS Backup initiates a backup job.

        - **StartWindowMinutes** *(integer) --*

          An optional value that specifies a period of time in minutes after a backup is
          scheduled before a job is canceled if it doesn't start successfully.

        - **CompletionWindowMinutes** *(integer) --*

          A value in minutes after a backup job is successfully started before it must be
          completed or it is canceled by AWS Backup. This value is optional.

        - **Lifecycle** *(dict) --*

          The lifecycle defines when a protected resource is transitioned to cold storage and
          when it expires. AWS Backup transitions and expires backups automatically according to
          the lifecycle that you define.

          Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
          days. Therefore, the “expire after days” setting must be 90 days greater than the
          “transition to cold after days” setting. The “transition to cold after days” setting
          cannot be changed after a backup has been transitioned to cold.

          - **MoveToColdStorageAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is moved to cold
            storage.

          - **DeleteAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is deleted. Must be
            greater than ``MoveToColdStorageAfterDays`` .

        - **RecoveryPointTags** *(dict) --*

          An array of key-value pair strings that are assigned to resources that are associated
          with this rule when restored from backup.

          - *(string) --*

            - *(string) --*

        - **RuleId** *(string) --*

          Uniquely identifies a rule that is used to schedule the backup of a selection of
          resources.
    """


_ClientGetBackupPlanFromTemplateResponseTypeDef = TypedDict(
    "_ClientGetBackupPlanFromTemplateResponseTypeDef",
    {
        "BackupPlanDocument": ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef
    },
    total=False,
)


class ClientGetBackupPlanFromTemplateResponseTypeDef(
    _ClientGetBackupPlanFromTemplateResponseTypeDef
):
    """
    Type definition for `ClientGetBackupPlanFromTemplate` `Response`

    - **BackupPlanDocument** *(dict) --*

      Returns the body of a backup plan based on the target template, including the name, rules,
      and backup vault of the plan.

      - **BackupPlanName** *(string) --*

        The display name of a backup plan.

      - **Rules** *(list) --*

        An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used
        to back up a selection of resources.

        - *(dict) --*

          Specifies a scheduled task used to back up a selection of resources.

          - **RuleName** *(string) --*

            An optional display name for a backup rule.

          - **TargetBackupVaultName** *(string) --*

            The name of a logical container where backups are stored. Backup vaults are identified
            by names that are unique to the account used to create them and the AWS Region where
            they are created. They consist of lowercase letters, numbers, and hyphens.

          - **ScheduleExpression** *(string) --*

            A CRON expression specifying when AWS Backup initiates a backup job.

          - **StartWindowMinutes** *(integer) --*

            An optional value that specifies a period of time in minutes after a backup is
            scheduled before a job is canceled if it doesn't start successfully.

          - **CompletionWindowMinutes** *(integer) --*

            A value in minutes after a backup job is successfully started before it must be
            completed or it is canceled by AWS Backup. This value is optional.

          - **Lifecycle** *(dict) --*

            The lifecycle defines when a protected resource is transitioned to cold storage and
            when it expires. AWS Backup transitions and expires backups automatically according to
            the lifecycle that you define.

            Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
            days. Therefore, the “expire after days” setting must be 90 days greater than the
            “transition to cold after days” setting. The “transition to cold after days” setting
            cannot be changed after a backup has been transitioned to cold.

            - **MoveToColdStorageAfterDays** *(integer) --*

              Specifies the number of days after creation that a recovery point is moved to cold
              storage.

            - **DeleteAfterDays** *(integer) --*

              Specifies the number of days after creation that a recovery point is deleted. Must be
              greater than ``MoveToColdStorageAfterDays`` .

          - **RecoveryPointTags** *(dict) --*

            An array of key-value pair strings that are assigned to resources that are associated
            with this rule when restored from backup.

            - *(string) --*

              - *(string) --*

          - **RuleId** *(string) --*

            Uniquely identifies a rule that is used to schedule the backup of a selection of
            resources.
    """


_ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef = TypedDict(
    "_ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef(
    _ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef
):
    """
    Type definition for `ClientGetBackupPlanResponseBackupPlanRules` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and
    when it expires. AWS Backup transitions and expires backups automatically according to
    the lifecycle that you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
    days. Therefore, the “expire after days” setting must be 90 days greater than the
    “transition to cold after days” setting. The “transition to cold after days” setting
    cannot be changed after a backup has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold
      storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be
      greater than ``MoveToColdStorageAfterDays`` .
    """


_ClientGetBackupPlanResponseBackupPlanRulesTypeDef = TypedDict(
    "_ClientGetBackupPlanResponseBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
    },
    total=False,
)


class ClientGetBackupPlanResponseBackupPlanRulesTypeDef(
    _ClientGetBackupPlanResponseBackupPlanRulesTypeDef
):
    """
    Type definition for `ClientGetBackupPlanResponseBackupPlan` `Rules`

    Specifies a scheduled task used to back up a selection of resources.

    - **RuleName** *(string) --*

      An optional display name for a backup rule.

    - **TargetBackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified
      by names that are unique to the account used to create them and the AWS Region where
      they are created. They consist of lowercase letters, numbers, and hyphens.

    - **ScheduleExpression** *(string) --*

      A CRON expression specifying when AWS Backup initiates a backup job.

    - **StartWindowMinutes** *(integer) --*

      An optional value that specifies a period of time in minutes after a backup is
      scheduled before a job is canceled if it doesn't start successfully.

    - **CompletionWindowMinutes** *(integer) --*

      A value in minutes after a backup job is successfully started before it must be
      completed or it is canceled by AWS Backup. This value is optional.

    - **Lifecycle** *(dict) --*

      The lifecycle defines when a protected resource is transitioned to cold storage and
      when it expires. AWS Backup transitions and expires backups automatically according to
      the lifecycle that you define.

      Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
      days. Therefore, the “expire after days” setting must be 90 days greater than the
      “transition to cold after days” setting. The “transition to cold after days” setting
      cannot be changed after a backup has been transitioned to cold.

      - **MoveToColdStorageAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is moved to cold
        storage.

      - **DeleteAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is deleted. Must be
        greater than ``MoveToColdStorageAfterDays`` .

    - **RecoveryPointTags** *(dict) --*

      An array of key-value pair strings that are assigned to resources that are associated
      with this rule when restored from backup.

      - *(string) --*

        - *(string) --*

    - **RuleId** *(string) --*

      Uniquely identifies a rule that is used to schedule the backup of a selection of
      resources.
    """


_ClientGetBackupPlanResponseBackupPlanTypeDef = TypedDict(
    "_ClientGetBackupPlanResponseBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[ClientGetBackupPlanResponseBackupPlanRulesTypeDef],
    },
    total=False,
)


class ClientGetBackupPlanResponseBackupPlanTypeDef(
    _ClientGetBackupPlanResponseBackupPlanTypeDef
):
    """
    Type definition for `ClientGetBackupPlanResponse` `BackupPlan`

    Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
    ``Rules`` .

    - **BackupPlanName** *(string) --*

      The display name of a backup plan.

    - **Rules** *(list) --*

      An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used
      to back up a selection of resources.

      - *(dict) --*

        Specifies a scheduled task used to back up a selection of resources.

        - **RuleName** *(string) --*

          An optional display name for a backup rule.

        - **TargetBackupVaultName** *(string) --*

          The name of a logical container where backups are stored. Backup vaults are identified
          by names that are unique to the account used to create them and the AWS Region where
          they are created. They consist of lowercase letters, numbers, and hyphens.

        - **ScheduleExpression** *(string) --*

          A CRON expression specifying when AWS Backup initiates a backup job.

        - **StartWindowMinutes** *(integer) --*

          An optional value that specifies a period of time in minutes after a backup is
          scheduled before a job is canceled if it doesn't start successfully.

        - **CompletionWindowMinutes** *(integer) --*

          A value in minutes after a backup job is successfully started before it must be
          completed or it is canceled by AWS Backup. This value is optional.

        - **Lifecycle** *(dict) --*

          The lifecycle defines when a protected resource is transitioned to cold storage and
          when it expires. AWS Backup transitions and expires backups automatically according to
          the lifecycle that you define.

          Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
          days. Therefore, the “expire after days” setting must be 90 days greater than the
          “transition to cold after days” setting. The “transition to cold after days” setting
          cannot be changed after a backup has been transitioned to cold.

          - **MoveToColdStorageAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is moved to cold
            storage.

          - **DeleteAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is deleted. Must be
            greater than ``MoveToColdStorageAfterDays`` .

        - **RecoveryPointTags** *(dict) --*

          An array of key-value pair strings that are assigned to resources that are associated
          with this rule when restored from backup.

          - *(string) --*

            - *(string) --*

        - **RuleId** *(string) --*

          Uniquely identifies a rule that is used to schedule the backup of a selection of
          resources.
    """


_ClientGetBackupPlanResponseTypeDef = TypedDict(
    "_ClientGetBackupPlanResponseTypeDef",
    {
        "BackupPlan": ClientGetBackupPlanResponseBackupPlanTypeDef,
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "VersionId": str,
        "CreatorRequestId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "LastExecutionDate": datetime,
    },
    total=False,
)


class ClientGetBackupPlanResponseTypeDef(_ClientGetBackupPlanResponseTypeDef):
    """
    Type definition for `ClientGetBackupPlan` `Response`

    - **BackupPlan** *(dict) --*

      Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
      ``Rules`` .

      - **BackupPlanName** *(string) --*

        The display name of a backup plan.

      - **Rules** *(list) --*

        An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used
        to back up a selection of resources.

        - *(dict) --*

          Specifies a scheduled task used to back up a selection of resources.

          - **RuleName** *(string) --*

            An optional display name for a backup rule.

          - **TargetBackupVaultName** *(string) --*

            The name of a logical container where backups are stored. Backup vaults are identified
            by names that are unique to the account used to create them and the AWS Region where
            they are created. They consist of lowercase letters, numbers, and hyphens.

          - **ScheduleExpression** *(string) --*

            A CRON expression specifying when AWS Backup initiates a backup job.

          - **StartWindowMinutes** *(integer) --*

            An optional value that specifies a period of time in minutes after a backup is
            scheduled before a job is canceled if it doesn't start successfully.

          - **CompletionWindowMinutes** *(integer) --*

            A value in minutes after a backup job is successfully started before it must be
            completed or it is canceled by AWS Backup. This value is optional.

          - **Lifecycle** *(dict) --*

            The lifecycle defines when a protected resource is transitioned to cold storage and
            when it expires. AWS Backup transitions and expires backups automatically according to
            the lifecycle that you define.

            Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
            days. Therefore, the “expire after days” setting must be 90 days greater than the
            “transition to cold after days” setting. The “transition to cold after days” setting
            cannot be changed after a backup has been transitioned to cold.

            - **MoveToColdStorageAfterDays** *(integer) --*

              Specifies the number of days after creation that a recovery point is moved to cold
              storage.

            - **DeleteAfterDays** *(integer) --*

              Specifies the number of days after creation that a recovery point is deleted. Must be
              greater than ``MoveToColdStorageAfterDays`` .

          - **RecoveryPointTags** *(dict) --*

            An array of key-value pair strings that are assigned to resources that are associated
            with this rule when restored from backup.

            - *(string) --*

              - *(string) --*

          - **RuleId** *(string) --*

            Uniquely identifies a rule that is used to schedule the backup of a selection of
            resources.

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **VersionId** *(string) --*

      Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long.
      Version IDs cannot be edited.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and allows failed requests to be retried without
      the risk of executing the operation twice.

    - **CreationDate** *(datetime) --*

      The date and time that a backup plan is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **DeletionDate** *(datetime) --*

      The date and time that a backup plan is deleted, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **LastExecutionDate** *(datetime) --*

      The last time a job to back up resources was executed with this backup plan. A date and time,
      in Unix format and Coordinated Universal Time (UTC). The value of ``LastExecutionDate`` is
      accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January
      26, 2018 12:11:30.087 AM.
    """


_ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef = TypedDict(
    "_ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef",
    {"ConditionType": str, "ConditionKey": str, "ConditionValue": str},
    total=False,
)


class ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef(
    _ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef
):
    """
    Type definition for `ClientGetBackupSelectionResponseBackupSelection` `ListOfTags`

    Contains an array of triplets made up of a condition type (such as ``StringEquals`` ), a
    key, and a value. Conditions are used to filter resources in a selection that is assigned
    to a backup plan.

    - **ConditionType** *(string) --*

      An operation, such as ``StringEquals`` , that is applied to a key-value pair used to
      filter resources in a selection.

    - **ConditionKey** *(string) --*

      The key in a key-value pair. For example, in ``"ec2:ResourceTag/Department":
      "accounting"`` , ``"ec2:ResourceTag/Department"`` is the key.

    - **ConditionValue** *(string) --*

      The value in a key-value pair. For example, in ``"ec2:ResourceTag/Department":
      "accounting"`` , ``"accounting"`` is the value.
    """


_ClientGetBackupSelectionResponseBackupSelectionTypeDef = TypedDict(
    "_ClientGetBackupSelectionResponseBackupSelectionTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
        "Resources": List[str],
        "ListOfTags": List[
            ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetBackupSelectionResponseBackupSelectionTypeDef(
    _ClientGetBackupSelectionResponseBackupSelectionTypeDef
):
    """
    Type definition for `ClientGetBackupSelectionResponse` `BackupSelection`

    Specifies the body of a request to assign a set of resources to a backup plan.

    It includes an array of resources, an optional array of patterns to exclude resources, an
    optional role to provide access to the AWS service that the resource belongs to, and an
    optional array of tags used to identify a set of resources.

    - **SelectionName** *(string) --*

      The display name of a resource selection document.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that AWS Backup uses to authenticate when restoring the target
      resource; for example, ``arn:aws:iam::123456789012:role/S3Access`` .

    - **Resources** *(list) --*

      An array of strings that either contain Amazon Resource Names (ARNs) or match patterns such
      as "``arn:aws:ec2:us-east-1:123456789012:volume/*`` " of resources to assign to a backup
      plan.

      - *(string) --*

    - **ListOfTags** *(list) --*

      An array of conditions used to specify a set of resources to assign to a backup plan; for
      example, ``"StringEquals": {"ec2:ResourceTag/Department": "accounting"`` .

      - *(dict) --*

        Contains an array of triplets made up of a condition type (such as ``StringEquals`` ), a
        key, and a value. Conditions are used to filter resources in a selection that is assigned
        to a backup plan.

        - **ConditionType** *(string) --*

          An operation, such as ``StringEquals`` , that is applied to a key-value pair used to
          filter resources in a selection.

        - **ConditionKey** *(string) --*

          The key in a key-value pair. For example, in ``"ec2:ResourceTag/Department":
          "accounting"`` , ``"ec2:ResourceTag/Department"`` is the key.

        - **ConditionValue** *(string) --*

          The value in a key-value pair. For example, in ``"ec2:ResourceTag/Department":
          "accounting"`` , ``"accounting"`` is the value.
    """


_ClientGetBackupSelectionResponseTypeDef = TypedDict(
    "_ClientGetBackupSelectionResponseTypeDef",
    {
        "BackupSelection": ClientGetBackupSelectionResponseBackupSelectionTypeDef,
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class ClientGetBackupSelectionResponseTypeDef(_ClientGetBackupSelectionResponseTypeDef):
    """
    Type definition for `ClientGetBackupSelection` `Response`

    - **BackupSelection** *(dict) --*

      Specifies the body of a request to assign a set of resources to a backup plan.

      It includes an array of resources, an optional array of patterns to exclude resources, an
      optional role to provide access to the AWS service that the resource belongs to, and an
      optional array of tags used to identify a set of resources.

      - **SelectionName** *(string) --*

        The display name of a resource selection document.

      - **IamRoleArn** *(string) --*

        The ARN of the IAM role that AWS Backup uses to authenticate when restoring the target
        resource; for example, ``arn:aws:iam::123456789012:role/S3Access`` .

      - **Resources** *(list) --*

        An array of strings that either contain Amazon Resource Names (ARNs) or match patterns such
        as "``arn:aws:ec2:us-east-1:123456789012:volume/*`` " of resources to assign to a backup
        plan.

        - *(string) --*

      - **ListOfTags** *(list) --*

        An array of conditions used to specify a set of resources to assign to a backup plan; for
        example, ``"StringEquals": {"ec2:ResourceTag/Department": "accounting"`` .

        - *(dict) --*

          Contains an array of triplets made up of a condition type (such as ``StringEquals`` ), a
          key, and a value. Conditions are used to filter resources in a selection that is assigned
          to a backup plan.

          - **ConditionType** *(string) --*

            An operation, such as ``StringEquals`` , that is applied to a key-value pair used to
            filter resources in a selection.

          - **ConditionKey** *(string) --*

            The key in a key-value pair. For example, in ``"ec2:ResourceTag/Department":
            "accounting"`` , ``"ec2:ResourceTag/Department"`` is the key.

          - **ConditionValue** *(string) --*

            The value in a key-value pair. For example, in ``"ec2:ResourceTag/Department":
            "accounting"`` , ``"accounting"`` is the value.

    - **SelectionId** *(string) --*

      Uniquely identifies the body of a request to assign a set of resources to a backup plan.

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **CreationDate** *(datetime) --*

      The date and time a backup selection is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and allows failed requests to be retried without
      the risk of executing the operation twice.
    """


_ClientGetBackupVaultAccessPolicyResponseTypeDef = TypedDict(
    "_ClientGetBackupVaultAccessPolicyResponseTypeDef",
    {"BackupVaultName": str, "BackupVaultArn": str, "Policy": str},
    total=False,
)


class ClientGetBackupVaultAccessPolicyResponseTypeDef(
    _ClientGetBackupVaultAccessPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetBackupVaultAccessPolicy` `Response`

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the Region where they are
      created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **Policy** *(string) --*

      The backup vault access policy document in JSON format.
    """


_ClientGetBackupVaultNotificationsResponseTypeDef = TypedDict(
    "_ClientGetBackupVaultNotificationsResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[str],
    },
    total=False,
)


class ClientGetBackupVaultNotificationsResponseTypeDef(
    _ClientGetBackupVaultNotificationsResponseTypeDef
):
    """
    Type definition for `ClientGetBackupVaultNotifications` `Response`

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the Region where they are
      created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **SNSTopicArn** *(string) --*

      An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS) topic; for
      example, ``arn:aws:sns:us-west-2:111122223333:MyTopic`` .

    - **BackupVaultEvents** *(list) --*

      An array of events that indicate the status of jobs to back up resources to the backup vault.

      - *(string) --*
    """


_ClientGetRecoveryPointRestoreMetadataResponseTypeDef = TypedDict(
    "_ClientGetRecoveryPointRestoreMetadataResponseTypeDef",
    {"BackupVaultArn": str, "RecoveryPointArn": str, "RestoreMetadata": Dict[str, str]},
    total=False,
)


class ClientGetRecoveryPointRestoreMetadataResponseTypeDef(
    _ClientGetRecoveryPointRestoreMetadataResponseTypeDef
):
    """
    Type definition for `ClientGetRecoveryPointRestoreMetadata` `Response`

    - **BackupVaultArn** *(string) --*

      An ARN that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **RecoveryPointArn** *(string) --*

      An ARN that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **RestoreMetadata** *(dict) --*

      A set of metadata key-value pairs that lists the metadata key-value pairs that are required
      to restore the recovery point.

      - *(string) --*

        - *(string) --*
    """


_ClientGetSupportedResourceTypesResponseTypeDef = TypedDict(
    "_ClientGetSupportedResourceTypesResponseTypeDef",
    {"ResourceTypes": List[str]},
    total=False,
)


class ClientGetSupportedResourceTypesResponseTypeDef(
    _ClientGetSupportedResourceTypesResponseTypeDef
):
    """
    Type definition for `ClientGetSupportedResourceTypes` `Response`

    - **ResourceTypes** *(list) --*

      Contains a string with the supported AWS resource types:

      * ``EBS`` for Amazon Elastic Block Store

      * ``SGW`` for AWS Storage Gateway

      * ``RDS`` for Amazon Relational Database Service

      * ``DDB`` for Amazon DynamoDB

      * ``EFS`` for Amazon Elastic File System

      - *(string) --*
    """


_ClientListBackupJobsResponseBackupJobsCreatedByTypeDef = TypedDict(
    "_ClientListBackupJobsResponseBackupJobsCreatedByTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
    },
    total=False,
)


class ClientListBackupJobsResponseBackupJobsCreatedByTypeDef(
    _ClientListBackupJobsResponseBackupJobsCreatedByTypeDef
):
    """
    Type definition for `ClientListBackupJobsResponseBackupJobs` `CreatedBy`

    Contains identifying information about the creation of a backup job, including the
    ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of
    the backup plan used to create it.

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **BackupPlanVersion** *(string) --*

      Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at
      most 1,024 bytes long. They cannot be edited.

    - **BackupRuleId** *(string) --*

      Uniquely identifies a rule used to schedule the backup of a selection of resources.
    """


_ClientListBackupJobsResponseBackupJobsTypeDef = TypedDict(
    "_ClientListBackupJobsResponseBackupJobsTypeDef",
    {
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": str,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": ClientListBackupJobsResponseBackupJobsCreatedByTypeDef,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "ResourceType": str,
        "BytesTransferred": int,
    },
    total=False,
)


class ClientListBackupJobsResponseBackupJobsTypeDef(
    _ClientListBackupJobsResponseBackupJobsTypeDef
):
    """
    Type definition for `ClientListBackupJobsResponse` `BackupJobs`

    Contains detailed information about a backup job.

    - **BackupJobId** *(string) --*

      Uniquely identifies a request to AWS Backup to back up a resource.

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the AWS Region where they
      are created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **RecoveryPointArn** *(string) --*

      An ARN that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **ResourceArn** *(string) --*

      An ARN that uniquely identifies a resource. The format of the ARN depends on the resource
      type.

    - **CreationDate** *(datetime) --*

      The date and time a backup job is created, in Unix format and Coordinated Universal Time
      (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CompletionDate** *(datetime) --*

      The date and time a job to create a backup job is completed, in Unix format and
      Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to
      milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
      12:11:30.087 AM.

    - **State** *(string) --*

      The current state of a resource recovery point.

    - **StatusMessage** *(string) --*

      A detailed message explaining the status of the job to back up a resource.

    - **PercentDone** *(string) --*

      Contains an estimated percentage complete of a job at the time the job status was queried.

    - **BackupSizeInBytes** *(integer) --*

      The size, in bytes, of a backup.

    - **IamRoleArn** *(string) --*

      Specifies the IAM role ARN used to create the target recovery point; for example,
      ``arn:aws:iam::123456789012:role/S3Access`` .

    - **CreatedBy** *(dict) --*

      Contains identifying information about the creation of a backup job, including the
      ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of
      the backup plan used to create it.

      - **BackupPlanId** *(string) --*

        Uniquely identifies a backup plan.

      - **BackupPlanArn** *(string) --*

        An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
        ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

      - **BackupPlanVersion** *(string) --*

        Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at
        most 1,024 bytes long. They cannot be edited.

      - **BackupRuleId** *(string) --*

        Uniquely identifies a rule used to schedule the backup of a selection of resources.

    - **ExpectedCompletionDate** *(datetime) --*

      The date and time a job to back up resources is expected to be completed, in Unix format
      and Coordinated Universal Time (UTC). The value of ``ExpectedCompletionDate`` is accurate
      to milliseconds. For example, the value 1516925490.087 represents Friday, January 26,
      2018 12:11:30.087 AM.

    - **StartBy** *(datetime) --*

      Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job
      must be started before it is canceled. The value is calculated by adding the start window
      to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2
      hours, the ``StartBy`` time would be 8:00 PM on the date specified. The value of
      ``StartBy`` is accurate to milliseconds. For example, the value 1516925490.087 represents
      Friday, January 26, 2018 12:11:30.087 AM.

    - **ResourceType** *(string) --*

      The type of AWS resource to be backed-up; for example, an Amazon Elastic Block Store
      (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

    - **BytesTransferred** *(integer) --*

      The size in bytes transferred to a backup vault at the time that the job status was
      queried.
    """


_ClientListBackupJobsResponseTypeDef = TypedDict(
    "_ClientListBackupJobsResponseTypeDef",
    {
        "BackupJobs": List[ClientListBackupJobsResponseBackupJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListBackupJobsResponseTypeDef(_ClientListBackupJobsResponseTypeDef):
    """
    Type definition for `ClientListBackupJobs` `Response`

    - **BackupJobs** *(list) --*

      An array of structures containing metadata about your backup jobs returned in JSON format.

      - *(dict) --*

        Contains detailed information about a backup job.

        - **BackupJobId** *(string) --*

          Uniquely identifies a request to AWS Backup to back up a resource.

        - **BackupVaultName** *(string) --*

          The name of a logical container where backups are stored. Backup vaults are identified by
          names that are unique to the account used to create them and the AWS Region where they
          are created. They consist of lowercase letters, numbers, and hyphens.

        - **BackupVaultArn** *(string) --*

          An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
          ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

        - **RecoveryPointArn** *(string) --*

          An ARN that uniquely identifies a recovery point; for example,
          ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
          .

        - **ResourceArn** *(string) --*

          An ARN that uniquely identifies a resource. The format of the ARN depends on the resource
          type.

        - **CreationDate** *(datetime) --*

          The date and time a backup job is created, in Unix format and Coordinated Universal Time
          (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
          1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **CompletionDate** *(datetime) --*

          The date and time a job to create a backup job is completed, in Unix format and
          Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to
          milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
          12:11:30.087 AM.

        - **State** *(string) --*

          The current state of a resource recovery point.

        - **StatusMessage** *(string) --*

          A detailed message explaining the status of the job to back up a resource.

        - **PercentDone** *(string) --*

          Contains an estimated percentage complete of a job at the time the job status was queried.

        - **BackupSizeInBytes** *(integer) --*

          The size, in bytes, of a backup.

        - **IamRoleArn** *(string) --*

          Specifies the IAM role ARN used to create the target recovery point; for example,
          ``arn:aws:iam::123456789012:role/S3Access`` .

        - **CreatedBy** *(dict) --*

          Contains identifying information about the creation of a backup job, including the
          ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of
          the backup plan used to create it.

          - **BackupPlanId** *(string) --*

            Uniquely identifies a backup plan.

          - **BackupPlanArn** *(string) --*

            An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
            ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

          - **BackupPlanVersion** *(string) --*

            Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at
            most 1,024 bytes long. They cannot be edited.

          - **BackupRuleId** *(string) --*

            Uniquely identifies a rule used to schedule the backup of a selection of resources.

        - **ExpectedCompletionDate** *(datetime) --*

          The date and time a job to back up resources is expected to be completed, in Unix format
          and Coordinated Universal Time (UTC). The value of ``ExpectedCompletionDate`` is accurate
          to milliseconds. For example, the value 1516925490.087 represents Friday, January 26,
          2018 12:11:30.087 AM.

        - **StartBy** *(datetime) --*

          Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job
          must be started before it is canceled. The value is calculated by adding the start window
          to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2
          hours, the ``StartBy`` time would be 8:00 PM on the date specified. The value of
          ``StartBy`` is accurate to milliseconds. For example, the value 1516925490.087 represents
          Friday, January 26, 2018 12:11:30.087 AM.

        - **ResourceType** *(string) --*

          The type of AWS resource to be backed-up; for example, an Amazon Elastic Block Store
          (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

        - **BytesTransferred** *(integer) --*

          The size in bytes transferred to a backup vault at the time that the job status was
          queried.

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.
    """


_ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef = TypedDict(
    "_ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef",
    {"BackupPlanTemplateId": str, "BackupPlanTemplateName": str},
    total=False,
)


class ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef(
    _ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef
):
    """
    Type definition for `ClientListBackupPlanTemplatesResponse` `BackupPlanTemplatesList`

    An object specifying metadata associated with a backup plan template.

    - **BackupPlanTemplateId** *(string) --*

      Uniquely identifies a stored backup plan template.

    - **BackupPlanTemplateName** *(string) --*

      The optional display name of a backup plan template.
    """


_ClientListBackupPlanTemplatesResponseTypeDef = TypedDict(
    "_ClientListBackupPlanTemplatesResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlanTemplatesList": List[
            ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef
        ],
    },
    total=False,
)


class ClientListBackupPlanTemplatesResponseTypeDef(
    _ClientListBackupPlanTemplatesResponseTypeDef
):
    """
    Type definition for `ClientListBackupPlanTemplates` `Response`

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.

    - **BackupPlanTemplatesList** *(list) --*

      An array of template list items containing metadata about your saved templates.

      - *(dict) --*

        An object specifying metadata associated with a backup plan template.

        - **BackupPlanTemplateId** *(string) --*

          Uniquely identifies a stored backup plan template.

        - **BackupPlanTemplateName** *(string) --*

          The optional display name of a backup plan template.
    """


_ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef = TypedDict(
    "_ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
    },
    total=False,
)


class ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef(
    _ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef
):
    """
    Type definition for `ClientListBackupPlanVersionsResponse` `BackupPlanVersionsList`

    Contains metadata about a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **CreationDate** *(datetime) --*

      The date and time a resource backup plan is created, in Unix format and Coordinated
      Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For
      example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **DeletionDate** *(datetime) --*

      The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time
      (UTC). The value of ``DeletionDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **VersionId** *(string) --*

      Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
      long. Version IDs cannot be edited.

    - **BackupPlanName** *(string) --*

      The display name of a saved backup plan.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and allows failed requests to be retried
      without the risk of executing the operation twice.

    - **LastExecutionDate** *(datetime) --*

      The last time a job to back up resources was executed with this rule. A date and time, in
      Unix format and Coordinated Universal Time (UTC). The value of ``LastExecutionDate`` is
      accurate to milliseconds. For example, the value 1516925490.087 represents Friday,
      January 26, 2018 12:11:30.087 AM.
    """


_ClientListBackupPlanVersionsResponseTypeDef = TypedDict(
    "_ClientListBackupPlanVersionsResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlanVersionsList": List[
            ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef
        ],
    },
    total=False,
)


class ClientListBackupPlanVersionsResponseTypeDef(
    _ClientListBackupPlanVersionsResponseTypeDef
):
    """
    Type definition for `ClientListBackupPlanVersions` `Response`

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.

    - **BackupPlanVersionsList** *(list) --*

      An array of version list items containing metadata about your backup plans.

      - *(dict) --*

        Contains metadata about a backup plan.

        - **BackupPlanArn** *(string) --*

          An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
          ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

        - **BackupPlanId** *(string) --*

          Uniquely identifies a backup plan.

        - **CreationDate** *(datetime) --*

          The date and time a resource backup plan is created, in Unix format and Coordinated
          Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For
          example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **DeletionDate** *(datetime) --*

          The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time
          (UTC). The value of ``DeletionDate`` is accurate to milliseconds. For example, the value
          1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **VersionId** *(string) --*

          Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
          long. Version IDs cannot be edited.

        - **BackupPlanName** *(string) --*

          The display name of a saved backup plan.

        - **CreatorRequestId** *(string) --*

          A unique string that identifies the request and allows failed requests to be retried
          without the risk of executing the operation twice.

        - **LastExecutionDate** *(datetime) --*

          The last time a job to back up resources was executed with this rule. A date and time, in
          Unix format and Coordinated Universal Time (UTC). The value of ``LastExecutionDate`` is
          accurate to milliseconds. For example, the value 1516925490.087 represents Friday,
          January 26, 2018 12:11:30.087 AM.
    """


_ClientListBackupPlansResponseBackupPlansListTypeDef = TypedDict(
    "_ClientListBackupPlansResponseBackupPlansListTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
    },
    total=False,
)


class ClientListBackupPlansResponseBackupPlansListTypeDef(
    _ClientListBackupPlansResponseBackupPlansListTypeDef
):
    """
    Type definition for `ClientListBackupPlansResponse` `BackupPlansList`

    Contains metadata about a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **CreationDate** *(datetime) --*

      The date and time a resource backup plan is created, in Unix format and Coordinated
      Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For
      example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **DeletionDate** *(datetime) --*

      The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time
      (UTC). The value of ``DeletionDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **VersionId** *(string) --*

      Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
      long. Version IDs cannot be edited.

    - **BackupPlanName** *(string) --*

      The display name of a saved backup plan.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and allows failed requests to be retried
      without the risk of executing the operation twice.

    - **LastExecutionDate** *(datetime) --*

      The last time a job to back up resources was executed with this rule. A date and time, in
      Unix format and Coordinated Universal Time (UTC). The value of ``LastExecutionDate`` is
      accurate to milliseconds. For example, the value 1516925490.087 represents Friday,
      January 26, 2018 12:11:30.087 AM.
    """


_ClientListBackupPlansResponseTypeDef = TypedDict(
    "_ClientListBackupPlansResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlansList": List[ClientListBackupPlansResponseBackupPlansListTypeDef],
    },
    total=False,
)


class ClientListBackupPlansResponseTypeDef(_ClientListBackupPlansResponseTypeDef):
    """
    Type definition for `ClientListBackupPlans` `Response`

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.

    - **BackupPlansList** *(list) --*

      An array of backup plan list items containing metadata about your saved backup plans.

      - *(dict) --*

        Contains metadata about a backup plan.

        - **BackupPlanArn** *(string) --*

          An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
          ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

        - **BackupPlanId** *(string) --*

          Uniquely identifies a backup plan.

        - **CreationDate** *(datetime) --*

          The date and time a resource backup plan is created, in Unix format and Coordinated
          Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For
          example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **DeletionDate** *(datetime) --*

          The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time
          (UTC). The value of ``DeletionDate`` is accurate to milliseconds. For example, the value
          1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **VersionId** *(string) --*

          Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
          long. Version IDs cannot be edited.

        - **BackupPlanName** *(string) --*

          The display name of a saved backup plan.

        - **CreatorRequestId** *(string) --*

          A unique string that identifies the request and allows failed requests to be retried
          without the risk of executing the operation twice.

        - **LastExecutionDate** *(datetime) --*

          The last time a job to back up resources was executed with this rule. A date and time, in
          Unix format and Coordinated Universal Time (UTC). The value of ``LastExecutionDate`` is
          accurate to milliseconds. For example, the value 1516925490.087 represents Friday,
          January 26, 2018 12:11:30.087 AM.
    """


_ClientListBackupSelectionsResponseBackupSelectionsListTypeDef = TypedDict(
    "_ClientListBackupSelectionsResponseBackupSelectionsListTypeDef",
    {
        "SelectionId": str,
        "SelectionName": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "IamRoleArn": str,
    },
    total=False,
)


class ClientListBackupSelectionsResponseBackupSelectionsListTypeDef(
    _ClientListBackupSelectionsResponseBackupSelectionsListTypeDef
):
    """
    Type definition for `ClientListBackupSelectionsResponse` `BackupSelectionsList`

    Contains metadata about a ``BackupSelection`` object.

    - **SelectionId** *(string) --*

      Uniquely identifies a request to assign a set of resources to a backup plan.

    - **SelectionName** *(string) --*

      The display name of a resource selection document.

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **CreationDate** *(datetime) --*

      The date and time a backup plan is created, in Unix format and Coordinated Universal Time
      (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and allows failed requests to be retried
      without the risk of executing the operation twice.

    - **IamRoleArn** *(string) --*

      Specifies the IAM role Amazon Resource Name (ARN) to create the target recovery point;
      for example, ``arn:aws:iam::123456789012:role/S3Access`` .
    """


_ClientListBackupSelectionsResponseTypeDef = TypedDict(
    "_ClientListBackupSelectionsResponseTypeDef",
    {
        "NextToken": str,
        "BackupSelectionsList": List[
            ClientListBackupSelectionsResponseBackupSelectionsListTypeDef
        ],
    },
    total=False,
)


class ClientListBackupSelectionsResponseTypeDef(
    _ClientListBackupSelectionsResponseTypeDef
):
    """
    Type definition for `ClientListBackupSelections` `Response`

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.

    - **BackupSelectionsList** *(list) --*

      An array of backup selection list items containing metadata about each resource in the list.

      - *(dict) --*

        Contains metadata about a ``BackupSelection`` object.

        - **SelectionId** *(string) --*

          Uniquely identifies a request to assign a set of resources to a backup plan.

        - **SelectionName** *(string) --*

          The display name of a resource selection document.

        - **BackupPlanId** *(string) --*

          Uniquely identifies a backup plan.

        - **CreationDate** *(datetime) --*

          The date and time a backup plan is created, in Unix format and Coordinated Universal Time
          (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
          1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **CreatorRequestId** *(string) --*

          A unique string that identifies the request and allows failed requests to be retried
          without the risk of executing the operation twice.

        - **IamRoleArn** *(string) --*

          Specifies the IAM role Amazon Resource Name (ARN) to create the target recovery point;
          for example, ``arn:aws:iam::123456789012:role/S3Access`` .
    """


_ClientListBackupVaultsResponseBackupVaultListTypeDef = TypedDict(
    "_ClientListBackupVaultsResponseBackupVaultListTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)


class ClientListBackupVaultsResponseBackupVaultListTypeDef(
    _ClientListBackupVaultsResponseBackupVaultListTypeDef
):
    """
    Type definition for `ClientListBackupVaultsResponse` `BackupVaultList`

    Contains metadata about a backup vault.

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the AWS Region where they
      are created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **CreationDate** *(datetime) --*

      The date and time a resource backup is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the
      value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **EncryptionKeyArn** *(string) --*

      The server-side encryption key that is used to protect your backups; for example,
      ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and allows failed requests to be retried
      without the risk of executing the operation twice.

    - **NumberOfRecoveryPoints** *(integer) --*

      The number of recovery points that are stored in a backup vault.
    """


_ClientListBackupVaultsResponseTypeDef = TypedDict(
    "_ClientListBackupVaultsResponseTypeDef",
    {
        "BackupVaultList": List[ClientListBackupVaultsResponseBackupVaultListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListBackupVaultsResponseTypeDef(_ClientListBackupVaultsResponseTypeDef):
    """
    Type definition for `ClientListBackupVaults` `Response`

    - **BackupVaultList** *(list) --*

      An array of backup vault list members containing vault metadata, including Amazon Resource
      Name (ARN), display name, creation date, number of saved recovery points, and encryption
      information if the resources saved in the backup vault are encrypted.

      - *(dict) --*

        Contains metadata about a backup vault.

        - **BackupVaultName** *(string) --*

          The name of a logical container where backups are stored. Backup vaults are identified by
          names that are unique to the account used to create them and the AWS Region where they
          are created. They consist of lowercase letters, numbers, and hyphens.

        - **BackupVaultArn** *(string) --*

          An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
          ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

        - **CreationDate** *(datetime) --*

          The date and time a resource backup is created, in Unix format and Coordinated Universal
          Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the
          value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **EncryptionKeyArn** *(string) --*

          The server-side encryption key that is used to protect your backups; for example,
          ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

        - **CreatorRequestId** *(string) --*

          A unique string that identifies the request and allows failed requests to be retried
          without the risk of executing the operation twice.

        - **NumberOfRecoveryPoints** *(integer) --*

          The number of recovery points that are stored in a backup vault.

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.
    """


_ClientListProtectedResourcesResponseResultsTypeDef = TypedDict(
    "_ClientListProtectedResourcesResponseResultsTypeDef",
    {"ResourceArn": str, "ResourceType": str, "LastBackupTime": datetime},
    total=False,
)


class ClientListProtectedResourcesResponseResultsTypeDef(
    _ClientListProtectedResourcesResponseResultsTypeDef
):
    """
    Type definition for `ClientListProtectedResourcesResponse` `Results`

    A structure that contains information about a backed-up resource.

    - **ResourceArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
      depends on the resource type.

    - **ResourceType** *(string) --*

      The type of AWS resource; for example, an Amazon Elastic Block Store (Amazon EBS) volume
      or an Amazon Relational Database Service (Amazon RDS) database.

    - **LastBackupTime** *(datetime) --*

      The date and time a resource was last backed up, in Unix format and Coordinated Universal
      Time (UTC). The value of ``LastBackupTime`` is accurate to milliseconds. For example, the
      value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
    """


_ClientListProtectedResourcesResponseTypeDef = TypedDict(
    "_ClientListProtectedResourcesResponseTypeDef",
    {
        "Results": List[ClientListProtectedResourcesResponseResultsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListProtectedResourcesResponseTypeDef(
    _ClientListProtectedResourcesResponseTypeDef
):
    """
    Type definition for `ClientListProtectedResources` `Response`

    - **Results** *(list) --*

      An array of resources successfully backed up by AWS Backup including the time the resource
      was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.

      - *(dict) --*

        A structure that contains information about a backed-up resource.

        - **ResourceArn** *(string) --*

          An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
          depends on the resource type.

        - **ResourceType** *(string) --*

          The type of AWS resource; for example, an Amazon Elastic Block Store (Amazon EBS) volume
          or an Amazon Relational Database Service (Amazon RDS) database.

        - **LastBackupTime** *(datetime) --*

          The date and time a resource was last backed up, in Unix format and Coordinated Universal
          Time (UTC). The value of ``LastBackupTime`` is accurate to milliseconds. For example, the
          value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.
    """


_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef
):
    """
    Type definition for `ClientListRecoveryPointsByBackupVaultResponseRecoveryPoints` `CalculatedLifecycle`

    A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt``
    timestamps.

    - **MoveToColdStorageAt** *(datetime) --*

      A timestamp that specifies when to transition a recovery point to cold storage.

    - **DeleteAt** *(datetime) --*

      A timestamp that specifies when to delete a recovery point.
    """


_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
    },
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef
):
    """
    Type definition for `ClientListRecoveryPointsByBackupVaultResponseRecoveryPoints` `CreatedBy`

    Contains identifying information about the creation of a recovery point, including the
    ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of
    the backup plan that is used to create it.

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **BackupPlanVersion** *(string) --*

      Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at
      most 1,024 bytes long. They cannot be edited.

    - **BackupRuleId** *(string) --*

      Uniquely identifies a rule used to schedule the backup of a selection of resources.
    """


_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef
):
    """
    Type definition for `ClientListRecoveryPointsByBackupVaultResponseRecoveryPoints` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and when
    it expires. AWS Backup transitions and expires backups automatically according to the
    lifecycle that you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
    days. Therefore, the “expire after days” setting must be 90 days greater than the
    “transition to cold after days” setting. The “transition to cold after days” setting
    cannot be changed after a backup has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold
      storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be
      greater than ``MoveToColdStorageAfterDays`` .
    """


_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef,
        "IamRoleArn": str,
        "Status": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef,
        "Lifecycle": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": datetime,
    },
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef
):
    """
    Type definition for `ClientListRecoveryPointsByBackupVaultResponse` `RecoveryPoints`

    Contains detailed information about the recovery points stored in a backup vault.

    - **RecoveryPointArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the AWS Region where they
      are created. They consist of lowercase letters, numbers, and hyphens.

    - **BackupVaultArn** *(string) --*

      An ARN that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **ResourceArn** *(string) --*

      An ARN that uniquely identifies a resource. The format of the ARN depends on the resource
      type.

    - **ResourceType** *(string) --*

      The type of AWS resource saved as a recovery point; for example, an Amazon Elastic Block
      Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

    - **CreatedBy** *(dict) --*

      Contains identifying information about the creation of a recovery point, including the
      ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of
      the backup plan that is used to create it.

      - **BackupPlanId** *(string) --*

        Uniquely identifies a backup plan.

      - **BackupPlanArn** *(string) --*

        An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
        ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

      - **BackupPlanVersion** *(string) --*

        Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at
        most 1,024 bytes long. They cannot be edited.

      - **BackupRuleId** *(string) --*

        Uniquely identifies a rule used to schedule the backup of a selection of resources.

    - **IamRoleArn** *(string) --*

      Specifies the IAM role ARN used to create the target recovery point; for example,
      ``arn:aws:iam::123456789012:role/S3Access`` .

    - **Status** *(string) --*

      A status code specifying the state of the recovery point.

    - **CreationDate** *(datetime) --*

      The date and time a recovery point is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the
      value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CompletionDate** *(datetime) --*

      The date and time a job to restore a recovery point is completed, in Unix format and
      Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to
      milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
      12:11:30.087 AM.

    - **BackupSizeInBytes** *(integer) --*

      The size, in bytes, of a backup.

    - **CalculatedLifecycle** *(dict) --*

      A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt``
      timestamps.

      - **MoveToColdStorageAt** *(datetime) --*

        A timestamp that specifies when to transition a recovery point to cold storage.

      - **DeleteAt** *(datetime) --*

        A timestamp that specifies when to delete a recovery point.

    - **Lifecycle** *(dict) --*

      The lifecycle defines when a protected resource is transitioned to cold storage and when
      it expires. AWS Backup transitions and expires backups automatically according to the
      lifecycle that you define.

      Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
      days. Therefore, the “expire after days” setting must be 90 days greater than the
      “transition to cold after days” setting. The “transition to cold after days” setting
      cannot be changed after a backup has been transitioned to cold.

      - **MoveToColdStorageAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is moved to cold
        storage.

      - **DeleteAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is deleted. Must be
        greater than ``MoveToColdStorageAfterDays`` .

    - **EncryptionKeyArn** *(string) --*

      The server-side encryption key that is used to protect your backups; for example,
      ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

    - **IsEncrypted** *(boolean) --*

      A Boolean value that is returned as ``TRUE`` if the specified recovery point is
      encrypted, or ``FALSE`` if the recovery point is not encrypted.

    - **LastRestoreTime** *(datetime) --*

      The date and time a recovery point was last restored, in Unix format and Coordinated
      Universal Time (UTC). The value of ``LastRestoreTime`` is accurate to milliseconds. For
      example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
    """


_ClientListRecoveryPointsByBackupVaultResponseTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List[
            ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef
        ],
    },
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseTypeDef
):
    """
    Type definition for `ClientListRecoveryPointsByBackupVault` `Response`

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.

    - **RecoveryPoints** *(list) --*

      An array of objects that contain detailed information about recovery points saved in a backup
      vault.

      - *(dict) --*

        Contains detailed information about the recovery points stored in a backup vault.

        - **RecoveryPointArn** *(string) --*

          An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
          ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
          .

        - **BackupVaultName** *(string) --*

          The name of a logical container where backups are stored. Backup vaults are identified by
          names that are unique to the account used to create them and the AWS Region where they
          are created. They consist of lowercase letters, numbers, and hyphens.

        - **BackupVaultArn** *(string) --*

          An ARN that uniquely identifies a backup vault; for example,
          ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

        - **ResourceArn** *(string) --*

          An ARN that uniquely identifies a resource. The format of the ARN depends on the resource
          type.

        - **ResourceType** *(string) --*

          The type of AWS resource saved as a recovery point; for example, an Amazon Elastic Block
          Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

        - **CreatedBy** *(dict) --*

          Contains identifying information about the creation of a recovery point, including the
          ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of
          the backup plan that is used to create it.

          - **BackupPlanId** *(string) --*

            Uniquely identifies a backup plan.

          - **BackupPlanArn** *(string) --*

            An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
            ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

          - **BackupPlanVersion** *(string) --*

            Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at
            most 1,024 bytes long. They cannot be edited.

          - **BackupRuleId** *(string) --*

            Uniquely identifies a rule used to schedule the backup of a selection of resources.

        - **IamRoleArn** *(string) --*

          Specifies the IAM role ARN used to create the target recovery point; for example,
          ``arn:aws:iam::123456789012:role/S3Access`` .

        - **Status** *(string) --*

          A status code specifying the state of the recovery point.

        - **CreationDate** *(datetime) --*

          The date and time a recovery point is created, in Unix format and Coordinated Universal
          Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the
          value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **CompletionDate** *(datetime) --*

          The date and time a job to restore a recovery point is completed, in Unix format and
          Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to
          milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
          12:11:30.087 AM.

        - **BackupSizeInBytes** *(integer) --*

          The size, in bytes, of a backup.

        - **CalculatedLifecycle** *(dict) --*

          A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt``
          timestamps.

          - **MoveToColdStorageAt** *(datetime) --*

            A timestamp that specifies when to transition a recovery point to cold storage.

          - **DeleteAt** *(datetime) --*

            A timestamp that specifies when to delete a recovery point.

        - **Lifecycle** *(dict) --*

          The lifecycle defines when a protected resource is transitioned to cold storage and when
          it expires. AWS Backup transitions and expires backups automatically according to the
          lifecycle that you define.

          Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
          days. Therefore, the “expire after days” setting must be 90 days greater than the
          “transition to cold after days” setting. The “transition to cold after days” setting
          cannot be changed after a backup has been transitioned to cold.

          - **MoveToColdStorageAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is moved to cold
            storage.

          - **DeleteAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is deleted. Must be
            greater than ``MoveToColdStorageAfterDays`` .

        - **EncryptionKeyArn** *(string) --*

          The server-side encryption key that is used to protect your backups; for example,
          ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

        - **IsEncrypted** *(boolean) --*

          A Boolean value that is returned as ``TRUE`` if the specified recovery point is
          encrypted, or ``FALSE`` if the recovery point is not encrypted.

        - **LastRestoreTime** *(datetime) --*

          The date and time a recovery point was last restored, in Unix format and Coordinated
          Universal Time (UTC). The value of ``LastRestoreTime`` is accurate to milliseconds. For
          example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
    """


_ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef = TypedDict(
    "_ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef",
    {
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "Status": str,
        "EncryptionKeyArn": str,
        "BackupSizeBytes": int,
        "BackupVaultName": str,
    },
    total=False,
)


class ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef(
    _ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef
):
    """
    Type definition for `ClientListRecoveryPointsByResourceResponse` `RecoveryPoints`

    Contains detailed information about a saved recovery point.

    - **RecoveryPointArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **CreationDate** *(datetime) --*

      The date and time a recovery point is created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the
      value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **Status** *(string) --*

      A status code specifying the state of the recovery point.

    - **EncryptionKeyArn** *(string) --*

      The server-side encryption key that is used to protect your backups; for example,
      ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

    - **BackupSizeBytes** *(integer) --*

      The size, in bytes, of a backup.

    - **BackupVaultName** *(string) --*

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the AWS Region where they
      are created. They consist of lowercase letters, numbers, and hyphens.
    """


_ClientListRecoveryPointsByResourceResponseTypeDef = TypedDict(
    "_ClientListRecoveryPointsByResourceResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List[
            ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef
        ],
    },
    total=False,
)


class ClientListRecoveryPointsByResourceResponseTypeDef(
    _ClientListRecoveryPointsByResourceResponseTypeDef
):
    """
    Type definition for `ClientListRecoveryPointsByResource` `Response`

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.

    - **RecoveryPoints** *(list) --*

      An array of objects that contain detailed information about recovery points of the specified
      resource type.

      - *(dict) --*

        Contains detailed information about a saved recovery point.

        - **RecoveryPointArn** *(string) --*

          An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
          ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
          .

        - **CreationDate** *(datetime) --*

          The date and time a recovery point is created, in Unix format and Coordinated Universal
          Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the
          value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **Status** *(string) --*

          A status code specifying the state of the recovery point.

        - **EncryptionKeyArn** *(string) --*

          The server-side encryption key that is used to protect your backups; for example,
          ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

        - **BackupSizeBytes** *(integer) --*

          The size, in bytes, of a backup.

        - **BackupVaultName** *(string) --*

          The name of a logical container where backups are stored. Backup vaults are identified by
          names that are unique to the account used to create them and the AWS Region where they
          are created. They consist of lowercase letters, numbers, and hyphens.
    """


_ClientListRestoreJobsResponseRestoreJobsTypeDef = TypedDict(
    "_ClientListRestoreJobsResponseRestoreJobsTypeDef",
    {
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": str,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
    },
    total=False,
)


class ClientListRestoreJobsResponseRestoreJobsTypeDef(
    _ClientListRestoreJobsResponseRestoreJobsTypeDef
):
    """
    Type definition for `ClientListRestoreJobsResponse` `RestoreJobs`

    Contains metadata about a restore job.

    - **RestoreJobId** *(string) --*

      Uniquely identifies the job that restores a recovery point.

    - **RecoveryPointArn** *(string) --*

      An ARN that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **CreationDate** *(datetime) --*

      The date and time a restore job is created, in Unix format and Coordinated Universal Time
      (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CompletionDate** *(datetime) --*

      The date and time a job to restore a recovery point is completed, in Unix format and
      Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to
      milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
      12:11:30.087 AM.

    - **Status** *(string) --*

      A status code specifying the state of the job initiated by AWS Backup to restore a
      recovery point.

    - **StatusMessage** *(string) --*

      A detailed message explaining the status of the job to restore a recovery point.

    - **PercentDone** *(string) --*

      Contains an estimated percentage complete of a job at the time the job status was queried.

    - **BackupSizeInBytes** *(integer) --*

      The size, in bytes, of the restored resource.

    - **IamRoleArn** *(string) --*

      Specifies the IAM role ARN used to create the target recovery point; for example,
      ``arn:aws:iam::123456789012:role/S3Access`` .

    - **ExpectedCompletionTimeMinutes** *(integer) --*

      The amount of time in minutes that a job restoring a recovery point is expected to take.

    - **CreatedResourceArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
      depends on the resource type.
    """


_ClientListRestoreJobsResponseTypeDef = TypedDict(
    "_ClientListRestoreJobsResponseTypeDef",
    {
        "RestoreJobs": List[ClientListRestoreJobsResponseRestoreJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListRestoreJobsResponseTypeDef(_ClientListRestoreJobsResponseTypeDef):
    """
    Type definition for `ClientListRestoreJobs` `Response`

    - **RestoreJobs** *(list) --*

      An array of objects that contain detailed information about jobs to restore saved resources.

      - *(dict) --*

        Contains metadata about a restore job.

        - **RestoreJobId** *(string) --*

          Uniquely identifies the job that restores a recovery point.

        - **RecoveryPointArn** *(string) --*

          An ARN that uniquely identifies a recovery point; for example,
          ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
          .

        - **CreationDate** *(datetime) --*

          The date and time a restore job is created, in Unix format and Coordinated Universal Time
          (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
          1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

        - **CompletionDate** *(datetime) --*

          The date and time a job to restore a recovery point is completed, in Unix format and
          Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to
          milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
          12:11:30.087 AM.

        - **Status** *(string) --*

          A status code specifying the state of the job initiated by AWS Backup to restore a
          recovery point.

        - **StatusMessage** *(string) --*

          A detailed message explaining the status of the job to restore a recovery point.

        - **PercentDone** *(string) --*

          Contains an estimated percentage complete of a job at the time the job status was queried.

        - **BackupSizeInBytes** *(integer) --*

          The size, in bytes, of the restored resource.

        - **IamRoleArn** *(string) --*

          Specifies the IAM role ARN used to create the target recovery point; for example,
          ``arn:aws:iam::123456789012:role/S3Access`` .

        - **ExpectedCompletionTimeMinutes** *(integer) --*

          The amount of time in minutes that a job restoring a recovery point is expected to take.

        - **CreatedResourceArn** *(string) --*

          An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
          depends on the resource type.

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"NextToken": str, "Tags": Dict[str, str]},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    - **NextToken** *(string) --*

      The next item following a partial list of returned items. For example, if a request is made
      to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
      your list starting at the location pointed to by the next token.

    - **Tags** *(dict) --*

      To help organize your resources, you can assign your own metadata to the resources you
      create. Each tag is a key-value pair.

      - *(string) --*

        - *(string) --*
    """


_ClientStartBackupJobLifecycleTypeDef = TypedDict(
    "_ClientStartBackupJobLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientStartBackupJobLifecycleTypeDef(_ClientStartBackupJobLifecycleTypeDef):
    """
    Type definition for `ClientStartBackupJob` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and when it
    expires. AWS Backup will transition and expire backups automatically according to the lifecycle
    that you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.
    Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold
    after days” setting. The “transition to cold after days” setting cannot be changed after a backup
    has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be greater
      than ``MoveToColdStorageAfterDays`` .
    """


_ClientStartBackupJobResponseTypeDef = TypedDict(
    "_ClientStartBackupJobResponseTypeDef",
    {"BackupJobId": str, "RecoveryPointArn": str, "CreationDate": datetime},
    total=False,
)


class ClientStartBackupJobResponseTypeDef(_ClientStartBackupJobResponseTypeDef):
    """
    Type definition for `ClientStartBackupJob` `Response`

    - **BackupJobId** *(string) --*

      Uniquely identifies a request to AWS Backup to back up a resource.

    - **RecoveryPointArn** *(string) --*

      An ARN that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **CreationDate** *(datetime) --*

      The date and time that a backup job is started, in Unix format and Coordinated Universal Time
      (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
    """


_ClientStartRestoreJobResponseTypeDef = TypedDict(
    "_ClientStartRestoreJobResponseTypeDef", {"RestoreJobId": str}, total=False
)


class ClientStartRestoreJobResponseTypeDef(_ClientStartRestoreJobResponseTypeDef):
    """
    Type definition for `ClientStartRestoreJob` `Response`

    - **RestoreJobId** *(string) --*

      Uniquely identifies the job that restores a recovery point.
    """


_ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef = TypedDict(
    "_ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef(
    _ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef
):
    """
    Type definition for `ClientUpdateBackupPlanBackupPlanRules` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and when it
    expires. AWS Backup will transition and expire backups automatically according to the
    lifecycle that you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
    days. Therefore, the “expire after days” setting must be 90 days greater than the
    “transition to cold after days”. The “transition to cold after days” setting cannot be
    changed after a backup has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold
      storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be
      greater than ``MoveToColdStorageAfterDays`` .
    """


_RequiredClientUpdateBackupPlanBackupPlanRulesTypeDef = TypedDict(
    "_RequiredClientUpdateBackupPlanBackupPlanRulesTypeDef",
    {"RuleName": str, "TargetBackupVaultName": str},
)
_OptionalClientUpdateBackupPlanBackupPlanRulesTypeDef = TypedDict(
    "_OptionalClientUpdateBackupPlanBackupPlanRulesTypeDef",
    {
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateBackupPlanBackupPlanRulesTypeDef(
    _RequiredClientUpdateBackupPlanBackupPlanRulesTypeDef,
    _OptionalClientUpdateBackupPlanBackupPlanRulesTypeDef,
):
    """
    Type definition for `ClientUpdateBackupPlanBackupPlan` `Rules`

    Specifies a scheduled task used to back up a selection of resources.

    - **RuleName** *(string) --* **[REQUIRED]**

      >An optional display name for a backup rule.

    - **TargetBackupVaultName** *(string) --* **[REQUIRED]**

      The name of a logical container where backups are stored. Backup vaults are identified by
      names that are unique to the account used to create them and the AWS Region where they are
      created. They consist of lowercase letters, numbers, and hyphens.

    - **ScheduleExpression** *(string) --*

      A CRON expression specifying when AWS Backup initiates a backup job.

    - **StartWindowMinutes** *(integer) --*

      The amount of time in minutes before beginning a backup.

    - **CompletionWindowMinutes** *(integer) --*

      The amount of time AWS Backup attempts a backup before canceling the job and returning an
      error.

    - **Lifecycle** *(dict) --*

      The lifecycle defines when a protected resource is transitioned to cold storage and when it
      expires. AWS Backup will transition and expire backups automatically according to the
      lifecycle that you define.

      Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
      days. Therefore, the “expire after days” setting must be 90 days greater than the
      “transition to cold after days”. The “transition to cold after days” setting cannot be
      changed after a backup has been transitioned to cold.

      - **MoveToColdStorageAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is moved to cold
        storage.

      - **DeleteAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is deleted. Must be
        greater than ``MoveToColdStorageAfterDays`` .

    - **RecoveryPointTags** *(dict) --*

      To help organize your resources, you can assign your own metadata to the resources that you
      create. Each tag is a key-value pair.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateBackupPlanBackupPlanTypeDef = TypedDict(
    "_ClientUpdateBackupPlanBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[ClientUpdateBackupPlanBackupPlanRulesTypeDef],
    },
)


class ClientUpdateBackupPlanBackupPlanTypeDef(_ClientUpdateBackupPlanBackupPlanTypeDef):
    """
    Type definition for `ClientUpdateBackupPlan` `BackupPlan`

    Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
    ``Rules`` .

    - **BackupPlanName** *(string) --* **[REQUIRED]**

      The display name of a backup plan.

    - **Rules** *(list) --* **[REQUIRED]**

      An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to
      back up a selection of resources.

      - *(dict) --*

        Specifies a scheduled task used to back up a selection of resources.

        - **RuleName** *(string) --* **[REQUIRED]**

          >An optional display name for a backup rule.

        - **TargetBackupVaultName** *(string) --* **[REQUIRED]**

          The name of a logical container where backups are stored. Backup vaults are identified by
          names that are unique to the account used to create them and the AWS Region where they are
          created. They consist of lowercase letters, numbers, and hyphens.

        - **ScheduleExpression** *(string) --*

          A CRON expression specifying when AWS Backup initiates a backup job.

        - **StartWindowMinutes** *(integer) --*

          The amount of time in minutes before beginning a backup.

        - **CompletionWindowMinutes** *(integer) --*

          The amount of time AWS Backup attempts a backup before canceling the job and returning an
          error.

        - **Lifecycle** *(dict) --*

          The lifecycle defines when a protected resource is transitioned to cold storage and when it
          expires. AWS Backup will transition and expire backups automatically according to the
          lifecycle that you define.

          Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
          days. Therefore, the “expire after days” setting must be 90 days greater than the
          “transition to cold after days”. The “transition to cold after days” setting cannot be
          changed after a backup has been transitioned to cold.

          - **MoveToColdStorageAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is moved to cold
            storage.

          - **DeleteAfterDays** *(integer) --*

            Specifies the number of days after creation that a recovery point is deleted. Must be
            greater than ``MoveToColdStorageAfterDays`` .

        - **RecoveryPointTags** *(dict) --*

          To help organize your resources, you can assign your own metadata to the resources that you
          create. Each tag is a key-value pair.

          - *(string) --*

            - *(string) --*
    """


_ClientUpdateBackupPlanResponseTypeDef = TypedDict(
    "_ClientUpdateBackupPlanResponseTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
    },
    total=False,
)


class ClientUpdateBackupPlanResponseTypeDef(_ClientUpdateBackupPlanResponseTypeDef):
    """
    Type definition for `ClientUpdateBackupPlan` `Response`

    - **BackupPlanId** *(string) --*

      Uniquely identifies a backup plan.

    - **BackupPlanArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
      ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

    - **CreationDate** *(datetime) --*

      The date and time a backup plan is updated, in Unix format and Coordinated Universal Time
      (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value
      1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

    - **VersionId** *(string) --*

      Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long.
      Version Ids cannot be edited.
    """


_ClientUpdateRecoveryPointLifecycleLifecycleTypeDef = TypedDict(
    "_ClientUpdateRecoveryPointLifecycleLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientUpdateRecoveryPointLifecycleLifecycleTypeDef(
    _ClientUpdateRecoveryPointLifecycleLifecycleTypeDef
):
    """
    Type definition for `ClientUpdateRecoveryPointLifecycle` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and when it
    expires. AWS Backup transitions and expires backups automatically according to the lifecycle that
    you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.
    Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold
    after days” setting. The “transition to cold after days” setting cannot be changed after a backup
    has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be greater
      than ``MoveToColdStorageAfterDays`` .
    """


_ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef = TypedDict(
    "_ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)


class ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef(
    _ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef
):
    """
    Type definition for `ClientUpdateRecoveryPointLifecycleResponse` `CalculatedLifecycle`

    A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt``
    timestamps.

    - **MoveToColdStorageAt** *(datetime) --*

      A timestamp that specifies when to transition a recovery point to cold storage.

    - **DeleteAt** *(datetime) --*

      A timestamp that specifies when to delete a recovery point.
    """


_ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef = TypedDict(
    "_ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef(
    _ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef
):
    """
    Type definition for `ClientUpdateRecoveryPointLifecycleResponse` `Lifecycle`

    The lifecycle defines when a protected resource is transitioned to cold storage and when it
    expires. AWS Backup transitions and expires backups automatically according to the lifecycle
    that you define.

    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.
    Therefore, the “expire after days” setting must be 90 days greater than the “transition to
    cold after days” setting. The “transition to cold after days” setting cannot be changed after
    a backup has been transitioned to cold.

    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold storage.

    - **DeleteAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is deleted. Must be
      greater than ``MoveToColdStorageAfterDays`` .
    """


_ClientUpdateRecoveryPointLifecycleResponseTypeDef = TypedDict(
    "_ClientUpdateRecoveryPointLifecycleResponseTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef,
        "CalculatedLifecycle": ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef,
    },
    total=False,
)


class ClientUpdateRecoveryPointLifecycleResponseTypeDef(
    _ClientUpdateRecoveryPointLifecycleResponseTypeDef
):
    """
    Type definition for `ClientUpdateRecoveryPointLifecycle` `Response`

    - **BackupVaultArn** *(string) --*

      An ARN that uniquely identifies a backup vault; for example,
      ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .

    - **RecoveryPointArn** *(string) --*

      An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
      ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
      .

    - **Lifecycle** *(dict) --*

      The lifecycle defines when a protected resource is transitioned to cold storage and when it
      expires. AWS Backup transitions and expires backups automatically according to the lifecycle
      that you define.

      Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.
      Therefore, the “expire after days” setting must be 90 days greater than the “transition to
      cold after days” setting. The “transition to cold after days” setting cannot be changed after
      a backup has been transitioned to cold.

      - **MoveToColdStorageAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is moved to cold storage.

      - **DeleteAfterDays** *(integer) --*

        Specifies the number of days after creation that a recovery point is deleted. Must be
        greater than ``MoveToColdStorageAfterDays`` .

    - **CalculatedLifecycle** *(dict) --*

      A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt``
      timestamps.

      - **MoveToColdStorageAt** *(datetime) --*

        A timestamp that specifies when to transition a recovery point to cold storage.

      - **DeleteAt** *(datetime) --*

        A timestamp that specifies when to delete a recovery point.
    """
