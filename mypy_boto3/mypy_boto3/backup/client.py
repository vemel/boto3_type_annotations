from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_backup_plan(
        self,
        BackupPlan: Dict,
        BackupPlanTags: Optional[Dict] = None,
        CreatorRequestId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_backup_selection(
        self,
        BackupPlanId: str,
        BackupSelection: Dict,
        CreatorRequestId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_backup_vault(
        self,
        BackupVaultName: str,
        BackupVaultTags: Optional[Dict] = None,
        EncryptionKeyArn: Optional[str] = None,
        CreatorRequestId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_backup_plan(
        self,
        BackupPlanId: str,
    ) -> Dict:
        pass


    def delete_backup_selection(
        self,
        BackupPlanId: str,
        SelectionId: str,
    ):
        pass


    def delete_backup_vault(
        self,
        BackupVaultName: str,
    ):
        pass


    def delete_backup_vault_access_policy(
        self,
        BackupVaultName: str,
    ):
        pass


    def delete_backup_vault_notifications(
        self,
        BackupVaultName: str,
    ):
        pass


    def delete_recovery_point(
        self,
        BackupVaultName: str,
        RecoveryPointArn: str,
    ):
        pass


    def describe_backup_job(
        self,
        BackupJobId: str,
    ) -> Dict:
        pass


    def describe_backup_vault(
        self,
        BackupVaultName: str,
    ) -> Dict:
        pass


    def describe_protected_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def describe_recovery_point(
        self,
        BackupVaultName: str,
        RecoveryPointArn: str,
    ) -> Dict:
        pass


    def describe_restore_job(
        self,
        RestoreJobId: str,
    ) -> Dict:
        pass


    def export_backup_plan_template(
        self,
        BackupPlanId: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_backup_plan(
        self,
        BackupPlanId: str,
        VersionId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_backup_plan_from_json(
        self,
        BackupPlanTemplateJson: str,
    ) -> Dict:
        pass


    def get_backup_plan_from_template(
        self,
        BackupPlanTemplateId: str,
    ) -> Dict:
        pass


    def get_backup_selection(
        self,
        BackupPlanId: str,
        SelectionId: str,
    ) -> Dict:
        pass


    def get_backup_vault_access_policy(
        self,
        BackupVaultName: str,
    ) -> Dict:
        pass


    def get_backup_vault_notifications(
        self,
        BackupVaultName: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_recovery_point_restore_metadata(
        self,
        BackupVaultName: str,
        RecoveryPointArn: str,
    ) -> Dict:
        pass


    def get_supported_resource_types(
        self,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_backup_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        ByResourceArn: Optional[str] = None,
        ByState: Optional[str] = None,
        ByBackupVaultName: Optional[str] = None,
        ByCreatedBefore: Optional[datetime] = None,
        ByCreatedAfter: Optional[datetime] = None,
        ByResourceType: Optional[str] = None,
    ) -> Dict:
        pass


    def list_backup_plan_templates(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_backup_plan_versions(
        self,
        BackupPlanId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_backup_plans(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        IncludeDeleted: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_backup_selections(
        self,
        BackupPlanId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_backup_vaults(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_protected_resources(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_recovery_points_by_backup_vault(
        self,
        BackupVaultName: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        ByResourceArn: Optional[str] = None,
        ByResourceType: Optional[str] = None,
        ByBackupPlanId: Optional[str] = None,
        ByCreatedBefore: Optional[datetime] = None,
        ByCreatedAfter: Optional[datetime] = None,
    ) -> Dict:
        pass


    def list_recovery_points_by_resource(
        self,
        ResourceArn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_restore_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        ResourceArn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def put_backup_vault_access_policy(
        self,
        BackupVaultName: str,
        Policy: Optional[str] = None,
    ):
        pass


    def put_backup_vault_notifications(
        self,
        BackupVaultName: str,
        SNSTopicArn: str,
        BackupVaultEvents: List,
    ):
        pass


    def start_backup_job(
        self,
        BackupVaultName: str,
        ResourceArn: str,
        IamRoleArn: str,
        IdempotencyToken: Optional[str] = None,
        StartWindowMinutes: Optional[int] = None,
        CompleteWindowMinutes: Optional[int] = None,
        Lifecycle: Optional[Dict] = None,
        RecoveryPointTags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_restore_job(
        self,
        RecoveryPointArn: str,
        Metadata: Dict,
        IamRoleArn: str,
        IdempotencyToken: Optional[str] = None,
        ResourceType: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_backup_job(
        self,
        BackupJobId: str,
    ):
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ):
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeyList: List,
    ):
        pass


    def update_backup_plan(
        self,
        BackupPlanId: str,
        BackupPlan: Dict,
    ) -> Dict:
        pass


    def update_recovery_point_lifecycle(
        self,
        BackupVaultName: str,
        RecoveryPointArn: str,
        Lifecycle: Optional[Dict] = None,
    ) -> Dict:
        pass

