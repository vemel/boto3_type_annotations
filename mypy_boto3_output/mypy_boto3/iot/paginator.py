from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListActiveViolations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAttachedPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        target: str,
        recursive: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAuditFindings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: Dict[str, Any] = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAuditTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: str = None,
        taskStatus: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAuthorizers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ascendingOrder: bool = None,
        status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListBillingGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, namePrefixFilter: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListCACertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListCertificatesByCA(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        caCertificateId: str,
        ascendingOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListIndices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListJobExecutionsForJob(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, jobId: str, status: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListJobExecutionsForThing(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        thingName: str,
        status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        status: str = None,
        targetSelection: str = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListOTAUpdates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, otaUpdateStatus: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListOutgoingCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPolicyPrincipals(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        policyName: str,
        ascendingOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPrincipalPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        principal: str,
        ascendingOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPrincipalThings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, principal: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRoleAliases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListScheduledAudits(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSecurityProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSecurityProfilesForTarget(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        securityProfileTargetArn: str,
        recursive: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListStreams(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, resourceArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTargetsForPolicy(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, policyName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTargetsForSecurityProfile(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, securityProfileName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListThingGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListThingGroupsForThing(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, thingName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListThingRegistrationTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, status: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListThingTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, thingTypeName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListThings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListThingsInBillingGroup(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, billingGroupName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListThingsInThingGroup(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        thingGroupName: str,
        recursive: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTopicRules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        topic: str = None,
        ruleDisabled: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListV2LoggingLevels(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, targetType: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListViolationEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
