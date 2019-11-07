from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_certificate_transfer(
        self,
        certificateId: str,
        setAsActive: Optional[bool] = None,
    ):
        pass


    def add_thing_to_billing_group(
        self,
        billingGroupName: Optional[str] = None,
        billingGroupArn: Optional[str] = None,
        thingName: Optional[str] = None,
        thingArn: Optional[str] = None,
    ) -> Dict:
        pass


    def add_thing_to_thing_group(
        self,
        thingGroupName: Optional[str] = None,
        thingGroupArn: Optional[str] = None,
        thingName: Optional[str] = None,
        thingArn: Optional[str] = None,
        overrideDynamicGroups: Optional[bool] = None,
    ) -> Dict:
        pass


    def associate_targets_with_job(
        self,
        targets: List,
        jobId: str,
        comment: Optional[str] = None,
    ) -> Dict:
        pass


    def attach_policy(
        self,
        policyName: str,
        target: str,
    ):
        pass


    def attach_principal_policy(
        self,
        policyName: str,
        principal: str,
    ):
        pass


    def attach_security_profile(
        self,
        securityProfileName: str,
        securityProfileTargetArn: str,
    ) -> Dict:
        pass


    def attach_thing_principal(
        self,
        thingName: str,
        principal: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_audit_mitigation_actions_task(
        self,
        taskId: str,
    ) -> Dict:
        pass


    def cancel_audit_task(
        self,
        taskId: str,
    ) -> Dict:
        pass


    def cancel_certificate_transfer(
        self,
        certificateId: str,
    ):
        pass


    def cancel_job(
        self,
        jobId: str,
        reasonCode: Optional[str] = None,
        comment: Optional[str] = None,
        force: Optional[bool] = None,
    ) -> Dict:
        pass


    def cancel_job_execution(
        self,
        jobId: str,
        thingName: str,
        force: Optional[bool] = None,
        expectedVersion: Optional[int] = None,
        statusDetails: Optional[Dict] = None,
    ):
        pass


    def clear_default_authorizer(
        self,
    ) -> Dict:
        pass


    def create_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str,
        tokenKeyName: str,
        tokenSigningPublicKeys: Dict,
        status: Optional[str] = None,
    ) -> Dict:
        pass


    def create_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_certificate_from_csr(
        self,
        certificateSigningRequest: str,
        setAsActive: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_dynamic_thing_group(
        self,
        thingGroupName: str,
        queryString: str,
        thingGroupProperties: Optional[Dict] = None,
        indexName: Optional[str] = None,
        queryVersion: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_job(
        self,
        jobId: str,
        targets: List,
        documentSource: Optional[str] = None,
        document: Optional[str] = None,
        description: Optional[str] = None,
        presignedUrlConfig: Optional[Dict] = None,
        targetSelection: Optional[str] = None,
        jobExecutionsRolloutConfig: Optional[Dict] = None,
        abortConfig: Optional[Dict] = None,
        timeoutConfig: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_keys_and_certificate(
        self,
        setAsActive: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_mitigation_action(
        self,
        actionName: str,
        roleArn: str,
        actionParams: Dict,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_ota_update(
        self,
        otaUpdateId: str,
        targets: List,
        files: List,
        roleArn: str,
        description: Optional[str] = None,
        targetSelection: Optional[str] = None,
        awsJobExecutionsRolloutConfig: Optional[Dict] = None,
        additionalParameters: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_policy(
        self,
        policyName: str,
        policyDocument: str,
    ) -> Dict:
        pass


    def create_policy_version(
        self,
        policyName: str,
        policyDocument: str,
        setAsDefault: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_role_alias(
        self,
        roleAlias: str,
        roleArn: str,
        credentialDurationSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def create_scheduled_audit(
        self,
        frequency: str,
        targetCheckNames: List,
        scheduledAuditName: str,
        dayOfMonth: Optional[str] = None,
        dayOfWeek: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: Optional[str] = None,
        behaviors: Optional[List] = None,
        alertTargets: Optional[Dict] = None,
        additionalMetricsToRetain: Optional[List] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_stream(
        self,
        streamId: str,
        files: List,
        roleArn: str,
        description: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_thing(
        self,
        thingName: str,
        thingTypeName: Optional[str] = None,
        attributePayload: Optional[Dict] = None,
        billingGroupName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_thing_group(
        self,
        thingGroupName: str,
        parentGroupName: Optional[str] = None,
        thingGroupProperties: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_thing_type(
        self,
        thingTypeName: str,
        thingTypeProperties: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_topic_rule(
        self,
        ruleName: str,
        topicRulePayload: Dict,
        tags: Optional[str] = None,
    ):
        pass


    def delete_account_audit_configuration(
        self,
        deleteScheduledAudits: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_authorizer(
        self,
        authorizerName: str,
    ) -> Dict:
        pass


    def delete_billing_group(
        self,
        billingGroupName: str,
        expectedVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def delete_ca_certificate(
        self,
        certificateId: str,
    ) -> Dict:
        pass


    def delete_certificate(
        self,
        certificateId: str,
        forceDelete: Optional[bool] = None,
    ):
        pass


    def delete_dynamic_thing_group(
        self,
        thingGroupName: str,
        expectedVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def delete_job(
        self,
        jobId: str,
        force: Optional[bool] = None,
    ):
        pass


    def delete_job_execution(
        self,
        jobId: str,
        thingName: str,
        executionNumber: int,
        force: Optional[bool] = None,
    ):
        pass


    def delete_mitigation_action(
        self,
        actionName: str,
    ) -> Dict:
        pass


    def delete_ota_update(
        self,
        otaUpdateId: str,
        deleteStream: Optional[bool] = None,
        forceDeleteAWSJob: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_policy(
        self,
        policyName: str,
    ):
        pass


    def delete_policy_version(
        self,
        policyName: str,
        policyVersionId: str,
    ):
        pass


    def delete_registration_code(
        self,
    ) -> Dict:
        pass


    def delete_role_alias(
        self,
        roleAlias: str,
    ) -> Dict:
        pass


    def delete_scheduled_audit(
        self,
        scheduledAuditName: str,
    ) -> Dict:
        pass


    def delete_security_profile(
        self,
        securityProfileName: str,
        expectedVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def delete_stream(
        self,
        streamId: str,
    ) -> Dict:
        pass


    def delete_thing(
        self,
        thingName: str,
        expectedVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def delete_thing_group(
        self,
        thingGroupName: str,
        expectedVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def delete_thing_type(
        self,
        thingTypeName: str,
    ) -> Dict:
        pass


    def delete_topic_rule(
        self,
        ruleName: str,
    ):
        pass


    def delete_v2_logging_level(
        self,
        targetType: str,
        targetName: str,
    ):
        pass


    def deprecate_thing_type(
        self,
        thingTypeName: str,
        undoDeprecate: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_account_audit_configuration(
        self,
    ) -> Dict:
        pass


    def describe_audit_finding(
        self,
        findingId: str,
    ) -> Dict:
        pass


    def describe_audit_mitigation_actions_task(
        self,
        taskId: str,
    ) -> Dict:
        pass


    def describe_audit_task(
        self,
        taskId: str,
    ) -> Dict:
        pass


    def describe_authorizer(
        self,
        authorizerName: str,
    ) -> Dict:
        pass


    def describe_billing_group(
        self,
        billingGroupName: str,
    ) -> Dict:
        pass


    def describe_ca_certificate(
        self,
        certificateId: str,
    ) -> Dict:
        pass


    def describe_certificate(
        self,
        certificateId: str,
    ) -> Dict:
        pass


    def describe_default_authorizer(
        self,
    ) -> Dict:
        pass


    def describe_endpoint(
        self,
        endpointType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_event_configurations(
        self,
    ) -> Dict:
        pass


    def describe_index(
        self,
        indexName: str,
    ) -> Dict:
        pass


    def describe_job(
        self,
        jobId: str,
    ) -> Dict:
        pass


    def describe_job_execution(
        self,
        jobId: str,
        thingName: str,
        executionNumber: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_mitigation_action(
        self,
        actionName: str,
    ) -> Dict:
        pass


    def describe_role_alias(
        self,
        roleAlias: str,
    ) -> Dict:
        pass


    def describe_scheduled_audit(
        self,
        scheduledAuditName: str,
    ) -> Dict:
        pass


    def describe_security_profile(
        self,
        securityProfileName: str,
    ) -> Dict:
        pass


    def describe_stream(
        self,
        streamId: str,
    ) -> Dict:
        pass


    def describe_thing(
        self,
        thingName: str,
    ) -> Dict:
        pass


    def describe_thing_group(
        self,
        thingGroupName: str,
    ) -> Dict:
        pass


    def describe_thing_registration_task(
        self,
        taskId: str,
    ) -> Dict:
        pass


    def describe_thing_type(
        self,
        thingTypeName: str,
    ) -> Dict:
        pass


    def detach_policy(
        self,
        policyName: str,
        target: str,
    ):
        pass


    def detach_principal_policy(
        self,
        policyName: str,
        principal: str,
    ):
        pass


    def detach_security_profile(
        self,
        securityProfileName: str,
        securityProfileTargetArn: str,
    ) -> Dict:
        pass


    def detach_thing_principal(
        self,
        thingName: str,
        principal: str,
    ) -> Dict:
        pass


    def disable_topic_rule(
        self,
        ruleName: str,
    ):
        pass


    def enable_topic_rule(
        self,
        ruleName: str,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_effective_policies(
        self,
        principal: Optional[str] = None,
        cognitoIdentityPoolId: Optional[str] = None,
        thingName: Optional[str] = None,
    ) -> Dict:
        pass


    def get_indexing_configuration(
        self,
    ) -> Dict:
        pass


    def get_job_document(
        self,
        jobId: str,
    ) -> Dict:
        pass


    def get_logging_options(
        self,
    ) -> Dict:
        pass


    def get_ota_update(
        self,
        otaUpdateId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_policy(
        self,
        policyName: str,
    ) -> Dict:
        pass


    def get_policy_version(
        self,
        policyName: str,
        policyVersionId: str,
    ) -> Dict:
        pass


    def get_registration_code(
        self,
    ) -> Dict:
        pass


    def get_statistics(
        self,
        queryString: str,
        indexName: Optional[str] = None,
        aggregationField: Optional[str] = None,
        queryVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def get_topic_rule(
        self,
        ruleName: str,
    ) -> Dict:
        pass


    def get_v2_logging_options(
        self,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_active_violations(
        self,
        thingName: Optional[str] = None,
        securityProfileName: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_attached_policies(
        self,
        target: str,
        recursive: Optional[bool] = None,
        marker: Optional[str] = None,
        pageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def list_audit_findings(
        self,
        taskId: Optional[str] = None,
        checkName: Optional[str] = None,
        resourceIdentifier: Optional[Dict] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def list_audit_mitigation_actions_executions(
        self,
        taskId: str,
        findingId: str,
        actionStatus: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_audit_mitigation_actions_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        auditTaskId: Optional[str] = None,
        findingId: Optional[str] = None,
        taskStatus: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_audit_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: Optional[str] = None,
        taskStatus: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_authorizers(
        self,
        pageSize: Optional[int] = None,
        marker: Optional[str] = None,
        ascendingOrder: Optional[bool] = None,
        status: Optional[str] = None,
    ) -> Dict:
        pass


    def list_billing_groups(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        namePrefixFilter: Optional[str] = None,
    ) -> Dict:
        pass


    def list_ca_certificates(
        self,
        pageSize: Optional[int] = None,
        marker: Optional[str] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_certificates(
        self,
        pageSize: Optional[int] = None,
        marker: Optional[str] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_certificates_by_ca(
        self,
        caCertificateId: str,
        pageSize: Optional[int] = None,
        marker: Optional[str] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_indices(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_job_executions_for_job(
        self,
        jobId: str,
        status: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_job_executions_for_thing(
        self,
        thingName: str,
        status: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_jobs(
        self,
        status: Optional[str] = None,
        targetSelection: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
        thingGroupName: Optional[str] = None,
        thingGroupId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_mitigation_actions(
        self,
        actionType: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_ota_updates(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
        otaUpdateStatus: Optional[str] = None,
    ) -> Dict:
        pass


    def list_outgoing_certificates(
        self,
        pageSize: Optional[int] = None,
        marker: Optional[str] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_policies(
        self,
        marker: Optional[str] = None,
        pageSize: Optional[int] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_policy_principals(
        self,
        policyName: str,
        marker: Optional[str] = None,
        pageSize: Optional[int] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_policy_versions(
        self,
        policyName: str,
    ) -> Dict:
        pass


    def list_principal_policies(
        self,
        principal: str,
        marker: Optional[str] = None,
        pageSize: Optional[int] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_principal_things(
        self,
        principal: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_role_aliases(
        self,
        pageSize: Optional[int] = None,
        marker: Optional[str] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_scheduled_audits(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_security_profiles(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_security_profiles_for_target(
        self,
        securityProfileTargetArn: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        recursive: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_streams(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
        ascendingOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_targets_for_policy(
        self,
        policyName: str,
        marker: Optional[str] = None,
        pageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def list_targets_for_security_profile(
        self,
        securityProfileName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_thing_groups(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        parentGroup: Optional[str] = None,
        namePrefixFilter: Optional[str] = None,
        recursive: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_thing_groups_for_thing(
        self,
        thingName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_thing_principals(
        self,
        thingName: str,
    ) -> Dict:
        pass


    def list_thing_registration_task_reports(
        self,
        taskId: str,
        reportType: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_thing_registration_tasks(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        status: Optional[str] = None,
    ) -> Dict:
        pass


    def list_thing_types(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        thingTypeName: Optional[str] = None,
    ) -> Dict:
        pass


    def list_things(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        attributeName: Optional[str] = None,
        attributeValue: Optional[str] = None,
        thingTypeName: Optional[str] = None,
    ) -> Dict:
        pass


    def list_things_in_billing_group(
        self,
        billingGroupName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_things_in_thing_group(
        self,
        thingGroupName: str,
        recursive: Optional[bool] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_topic_rules(
        self,
        topic: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
        ruleDisabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_v2_logging_levels(
        self,
        targetType: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_violation_events(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: Optional[str] = None,
        securityProfileName: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def register_ca_certificate(
        self,
        caCertificate: str,
        verificationCertificate: str,
        setAsActive: Optional[bool] = None,
        allowAutoRegistration: Optional[bool] = None,
        registrationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def register_certificate(
        self,
        certificatePem: str,
        caCertificatePem: Optional[str] = None,
        setAsActive: Optional[bool] = None,
        status: Optional[str] = None,
    ) -> Dict:
        pass


    def register_thing(
        self,
        templateBody: str,
        parameters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def reject_certificate_transfer(
        self,
        certificateId: str,
        rejectReason: Optional[str] = None,
    ):
        pass


    def remove_thing_from_billing_group(
        self,
        billingGroupName: Optional[str] = None,
        billingGroupArn: Optional[str] = None,
        thingName: Optional[str] = None,
        thingArn: Optional[str] = None,
    ) -> Dict:
        pass


    def remove_thing_from_thing_group(
        self,
        thingGroupName: Optional[str] = None,
        thingGroupArn: Optional[str] = None,
        thingName: Optional[str] = None,
        thingArn: Optional[str] = None,
    ) -> Dict:
        pass


    def replace_topic_rule(
        self,
        ruleName: str,
        topicRulePayload: Dict,
    ):
        pass


    def search_index(
        self,
        queryString: str,
        indexName: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        queryVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def set_default_authorizer(
        self,
        authorizerName: str,
    ) -> Dict:
        pass


    def set_default_policy_version(
        self,
        policyName: str,
        policyVersionId: str,
    ):
        pass


    def set_logging_options(
        self,
        loggingOptionsPayload: Dict,
    ):
        pass


    def set_v2_logging_level(
        self,
        logTarget: Dict,
        logLevel: str,
    ):
        pass


    def set_v2_logging_options(
        self,
        roleArn: Optional[str] = None,
        defaultLogLevel: Optional[str] = None,
        disableAllLogs: Optional[bool] = None,
    ):
        pass


    def start_audit_mitigation_actions_task(
        self,
        taskId: str,
        target: Dict,
        auditCheckToActionsMapping: Dict,
        clientRequestToken: str,
    ) -> Dict:
        pass


    def start_on_demand_audit_task(
        self,
        targetCheckNames: List,
    ) -> Dict:
        pass


    def start_thing_registration_task(
        self,
        templateBody: str,
        inputFileBucket: str,
        inputFileKey: str,
        roleArn: str,
    ) -> Dict:
        pass


    def stop_thing_registration_task(
        self,
        taskId: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ) -> Dict:
        pass


    def test_authorization(
        self,
        authInfos: List,
        principal: Optional[str] = None,
        cognitoIdentityPoolId: Optional[str] = None,
        clientId: Optional[str] = None,
        policyNamesToAdd: Optional[List] = None,
        policyNamesToSkip: Optional[List] = None,
    ) -> Dict:
        pass


    def test_invoke_authorizer(
        self,
        authorizerName: str,
        token: str,
        tokenSignature: str,
    ) -> Dict:
        pass


    def transfer_certificate(
        self,
        certificateId: str,
        targetAwsAccount: str,
        transferMessage: Optional[str] = None,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_account_audit_configuration(
        self,
        roleArn: Optional[str] = None,
        auditNotificationTargetConfigurations: Optional[Dict] = None,
        auditCheckConfigurations: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: Optional[str] = None,
        tokenKeyName: Optional[str] = None,
        tokenSigningPublicKeys: Optional[Dict] = None,
        status: Optional[str] = None,
    ) -> Dict:
        pass


    def update_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: Dict,
        expectedVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def update_ca_certificate(
        self,
        certificateId: str,
        newStatus: Optional[str] = None,
        newAutoRegistrationStatus: Optional[str] = None,
        registrationConfig: Optional[Dict] = None,
        removeAutoRegistration: Optional[bool] = None,
    ):
        pass


    def update_certificate(
        self,
        certificateId: str,
        newStatus: str,
    ):
        pass


    def update_dynamic_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: Dict,
        expectedVersion: Optional[int] = None,
        indexName: Optional[str] = None,
        queryString: Optional[str] = None,
        queryVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def update_event_configurations(
        self,
        eventConfigurations: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_indexing_configuration(
        self,
        thingIndexingConfiguration: Optional[Dict] = None,
        thingGroupIndexingConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_job(
        self,
        jobId: str,
        description: Optional[str] = None,
        presignedUrlConfig: Optional[Dict] = None,
        jobExecutionsRolloutConfig: Optional[Dict] = None,
        abortConfig: Optional[Dict] = None,
        timeoutConfig: Optional[Dict] = None,
    ):
        pass


    def update_mitigation_action(
        self,
        actionName: str,
        roleArn: Optional[str] = None,
        actionParams: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_role_alias(
        self,
        roleAlias: str,
        roleArn: Optional[str] = None,
        credentialDurationSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def update_scheduled_audit(
        self,
        scheduledAuditName: str,
        frequency: Optional[str] = None,
        dayOfMonth: Optional[str] = None,
        dayOfWeek: Optional[str] = None,
        targetCheckNames: Optional[List] = None,
    ) -> Dict:
        pass


    def update_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: Optional[str] = None,
        behaviors: Optional[List] = None,
        alertTargets: Optional[Dict] = None,
        additionalMetricsToRetain: Optional[List] = None,
        deleteBehaviors: Optional[bool] = None,
        deleteAlertTargets: Optional[bool] = None,
        deleteAdditionalMetricsToRetain: Optional[bool] = None,
        expectedVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def update_stream(
        self,
        streamId: str,
        description: Optional[str] = None,
        files: Optional[List] = None,
        roleArn: Optional[str] = None,
    ) -> Dict:
        pass


    def update_thing(
        self,
        thingName: str,
        thingTypeName: Optional[str] = None,
        attributePayload: Optional[Dict] = None,
        expectedVersion: Optional[int] = None,
        removeThingType: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: Dict,
        expectedVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def update_thing_groups_for_thing(
        self,
        thingName: Optional[str] = None,
        thingGroupsToAdd: Optional[List] = None,
        thingGroupsToRemove: Optional[List] = None,
        overrideDynamicGroups: Optional[bool] = None,
    ) -> Dict:
        pass


    def validate_security_profile_behaviors(
        self,
        behaviors: List,
    ) -> Dict:
        pass

