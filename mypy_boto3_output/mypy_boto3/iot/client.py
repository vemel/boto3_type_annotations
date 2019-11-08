from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_certificate_transfer(
        self, certificateId: str, setAsActive: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def add_thing_to_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_thing_to_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_targets_with_job(
        self, targets: List[Any], jobId: str, comment: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_policy(self, policyName: str, target: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def attach_principal_policy(self, policyName: str, principal: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def attach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_audit_mitigation_actions_task(self, taskId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def cancel_audit_task(self, taskId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def cancel_certificate_transfer(self, certificateId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_job(
        self,
        jobId: str,
        reasonCode: str = None,
        comment: str = None,
        force: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def cancel_job_execution(
        self,
        jobId: str,
        thingName: str,
        force: bool = None,
        expectedVersion: int = None,
        statusDetails: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def clear_default_authorizer(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str,
        tokenKeyName: str,
        tokenSigningPublicKeys: Dict[str, Any],
        status: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_certificate_from_csr(
        self, certificateSigningRequest: str, setAsActive: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_dynamic_thing_group(
        self,
        thingGroupName: str,
        queryString: str,
        thingGroupProperties: Dict[str, Any] = None,
        indexName: str = None,
        queryVersion: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_job(
        self,
        jobId: str,
        targets: List[Any],
        documentSource: str = None,
        document: str = None,
        description: str = None,
        presignedUrlConfig: Dict[str, Any] = None,
        targetSelection: str = None,
        jobExecutionsRolloutConfig: Dict[str, Any] = None,
        abortConfig: Dict[str, Any] = None,
        timeoutConfig: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_keys_and_certificate(self, setAsActive: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_mitigation_action(
        self,
        actionName: str,
        roleArn: str,
        actionParams: Dict[str, Any],
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_ota_update(
        self,
        otaUpdateId: str,
        targets: List[Any],
        files: List[Any],
        roleArn: str,
        description: str = None,
        targetSelection: str = None,
        awsJobExecutionsRolloutConfig: Dict[str, Any] = None,
        additionalParameters: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_policy(self, policyName: str, policyDocument: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_policy_version(
        self, policyName: str, policyDocument: str, setAsDefault: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_role_alias(
        self, roleAlias: str, roleArn: str, credentialDurationSeconds: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_scheduled_audit(
        self,
        frequency: str,
        targetCheckNames: List[Any],
        scheduledAuditName: str,
        dayOfMonth: str = None,
        dayOfWeek: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List[Any] = None,
        alertTargets: Dict[str, Any] = None,
        additionalMetricsToRetain: List[Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stream(
        self,
        streamId: str,
        files: List[Any],
        roleArn: str,
        description: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: Dict[str, Any] = None,
        billingGroupName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_thing_group(
        self,
        thingGroupName: str,
        parentGroupName: str = None,
        thingGroupProperties: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_thing_type(
        self,
        thingTypeName: str,
        thingTypeProperties: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_topic_rule(
        self, ruleName: str, topicRulePayload: Dict[str, Any], tags: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_account_audit_configuration(
        self, deleteScheduledAudits: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_authorizer(self, authorizerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_billing_group(
        self, billingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_ca_certificate(self, certificateId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_certificate(self, certificateId: str, forceDelete: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_dynamic_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_job(self, jobId: str, force: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_job_execution(
        self, jobId: str, thingName: str, executionNumber: int, force: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_mitigation_action(self, actionName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_ota_update(
        self,
        otaUpdateId: str,
        deleteStream: bool = None,
        forceDeleteAWSJob: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_policy(self, policyName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_policy_version(self, policyName: str, policyVersionId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_registration_code(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_role_alias(self, roleAlias: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_scheduled_audit(self, scheduledAuditName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_security_profile(
        self, securityProfileName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_stream(self, streamId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_thing(
        self, thingName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_thing_type(self, thingTypeName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_topic_rule(self, ruleName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_v2_logging_level(self, targetType: str, targetName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def deprecate_thing_type(
        self, thingTypeName: str, undoDeprecate: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account_audit_configuration(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_audit_finding(self, findingId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_audit_mitigation_actions_task(self, taskId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_audit_task(self, taskId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_authorizer(self, authorizerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_billing_group(self, billingGroupName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_ca_certificate(self, certificateId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_certificate(self, certificateId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_default_authorizer(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_endpoint(self, endpointType: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_event_configurations(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_index(self, indexName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_job(self, jobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_job_execution(
        self, jobId: str, thingName: str, executionNumber: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_mitigation_action(self, actionName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_role_alias(self, roleAlias: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_scheduled_audit(self, scheduledAuditName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_security_profile(self, securityProfileName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stream(self, streamId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_thing(self, thingName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_thing_group(self, thingGroupName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_thing_registration_task(self, taskId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_thing_type(self, thingTypeName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_policy(self, policyName: str, target: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def detach_principal_policy(self, policyName: str, principal: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def detach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_topic_rule(self, ruleName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def enable_topic_rule(self, ruleName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_effective_policies(
        self,
        principal: str = None,
        cognitoIdentityPoolId: str = None,
        thingName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_indexing_configuration(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job_document(self, jobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_logging_options(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ota_update(self, otaUpdateId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_policy(self, policyName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_policy_version(
        self, policyName: str, policyVersionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_registration_code(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_statistics(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_topic_rule(self, ruleName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_v2_logging_options(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_active_violations(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_attached_policies(
        self,
        target: str,
        recursive: bool = None,
        marker: str = None,
        pageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_audit_findings(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: Dict[str, Any] = None,
        maxResults: int = None,
        nextToken: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_audit_mitigation_actions_executions(
        self,
        taskId: str,
        findingId: str,
        actionStatus: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_audit_mitigation_actions_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_audit_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: str = None,
        taskStatus: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_authorizers(
        self,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
        status: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_billing_groups(
        self,
        nextToken: str = None,
        maxResults: int = None,
        namePrefixFilter: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_ca_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_certificates_by_ca(
        self,
        caCertificateId: str,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_indices(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_job_executions_for_job(
        self,
        jobId: str,
        status: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_job_executions_for_thing(
        self,
        thingName: str,
        status: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self,
        status: str = None,
        targetSelection: str = None,
        maxResults: int = None,
        nextToken: str = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_mitigation_actions(
        self, actionType: str = None, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_ota_updates(
        self, maxResults: int = None, nextToken: str = None, otaUpdateStatus: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_outgoing_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_policies(
        self, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_policy_principals(
        self,
        policyName: str,
        marker: str = None,
        pageSize: int = None,
        ascendingOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_policy_versions(self, policyName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_principal_policies(
        self,
        principal: str,
        marker: str = None,
        pageSize: int = None,
        ascendingOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_principal_things(
        self, principal: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_role_aliases(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_scheduled_audits(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_security_profiles(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_security_profiles_for_target(
        self,
        securityProfileTargetArn: str,
        nextToken: str = None,
        maxResults: int = None,
        recursive: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_streams(
        self, maxResults: int = None, nextToken: str = None, ascendingOrder: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_targets_for_policy(
        self, policyName: str, marker: str = None, pageSize: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_targets_for_security_profile(
        self, securityProfileName: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_thing_groups(
        self,
        nextToken: str = None,
        maxResults: int = None,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_thing_groups_for_thing(
        self, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_thing_principals(self, thingName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_thing_registration_task_reports(
        self,
        taskId: str,
        reportType: str,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_thing_registration_tasks(
        self, nextToken: str = None, maxResults: int = None, status: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_thing_types(
        self, nextToken: str = None, maxResults: int = None, thingTypeName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_things(
        self,
        nextToken: str = None,
        maxResults: int = None,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_things_in_billing_group(
        self, billingGroupName: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_things_in_thing_group(
        self,
        thingGroupName: str,
        recursive: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_topic_rules(
        self,
        topic: str = None,
        maxResults: int = None,
        nextToken: str = None,
        ruleDisabled: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_v2_logging_levels(
        self, targetType: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_violation_events(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_ca_certificate(
        self,
        caCertificate: str,
        verificationCertificate: str,
        setAsActive: bool = None,
        allowAutoRegistration: bool = None,
        registrationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_certificate(
        self,
        certificatePem: str,
        caCertificatePem: str = None,
        setAsActive: bool = None,
        status: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_thing(
        self, templateBody: str, parameters: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reject_certificate_transfer(
        self, certificateId: str, rejectReason: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def remove_thing_from_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_thing_from_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def replace_topic_rule(
        self, ruleName: str, topicRulePayload: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def search_index(
        self,
        queryString: str,
        indexName: str = None,
        nextToken: str = None,
        maxResults: int = None,
        queryVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_default_authorizer(self, authorizerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_default_policy_version(self, policyName: str, policyVersionId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_logging_options(self, loggingOptionsPayload: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_v2_logging_level(self, logTarget: Dict[str, Any], logLevel: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_v2_logging_options(
        self,
        roleArn: str = None,
        defaultLogLevel: str = None,
        disableAllLogs: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def start_audit_mitigation_actions_task(
        self,
        taskId: str,
        target: Dict[str, Any],
        auditCheckToActionsMapping: Dict[str, Any],
        clientRequestToken: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_on_demand_audit_task(self, targetCheckNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_thing_registration_task(
        self, templateBody: str, inputFileBucket: str, inputFileKey: str, roleArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_thing_registration_task(self, taskId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def test_authorization(
        self,
        authInfos: List[Any],
        principal: str = None,
        cognitoIdentityPoolId: str = None,
        clientId: str = None,
        policyNamesToAdd: List[Any] = None,
        policyNamesToSkip: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def test_invoke_authorizer(
        self, authorizerName: str, token: str, tokenSignature: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def transfer_certificate(
        self, certificateId: str, targetAwsAccount: str, transferMessage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_account_audit_configuration(
        self,
        roleArn: str = None,
        auditNotificationTargetConfigurations: Dict[str, Any] = None,
        auditCheckConfigurations: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str = None,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, Any] = None,
        status: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: Dict[str, Any],
        expectedVersion: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_ca_certificate(
        self,
        certificateId: str,
        newStatus: str = None,
        newAutoRegistrationStatus: str = None,
        registrationConfig: Dict[str, Any] = None,
        removeAutoRegistration: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_certificate(self, certificateId: str, newStatus: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_dynamic_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: Dict[str, Any],
        expectedVersion: int = None,
        indexName: str = None,
        queryString: str = None,
        queryVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_event_configurations(
        self, eventConfigurations: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_indexing_configuration(
        self,
        thingIndexingConfiguration: Dict[str, Any] = None,
        thingGroupIndexingConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_job(
        self,
        jobId: str,
        description: str = None,
        presignedUrlConfig: Dict[str, Any] = None,
        jobExecutionsRolloutConfig: Dict[str, Any] = None,
        abortConfig: Dict[str, Any] = None,
        timeoutConfig: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_mitigation_action(
        self, actionName: str, roleArn: str = None, actionParams: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_role_alias(
        self, roleAlias: str, roleArn: str = None, credentialDurationSeconds: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_scheduled_audit(
        self,
        scheduledAuditName: str,
        frequency: str = None,
        dayOfMonth: str = None,
        dayOfWeek: str = None,
        targetCheckNames: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List[Any] = None,
        alertTargets: Dict[str, Any] = None,
        additionalMetricsToRetain: List[Any] = None,
        deleteBehaviors: bool = None,
        deleteAlertTargets: bool = None,
        deleteAdditionalMetricsToRetain: bool = None,
        expectedVersion: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_stream(
        self,
        streamId: str,
        description: str = None,
        files: List[Any] = None,
        roleArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: Dict[str, Any] = None,
        expectedVersion: int = None,
        removeThingType: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: Dict[str, Any],
        expectedVersion: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_thing_groups_for_thing(
        self,
        thingName: str = None,
        thingGroupsToAdd: List[Any] = None,
        thingGroupsToRemove: List[Any] = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def validate_security_profile_behaviors(
        self, behaviors: List[Any]
    ) -> Dict[str, Any]:
        pass
