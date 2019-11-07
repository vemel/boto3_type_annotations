from datetime import datetime
from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListActiveViolations(Paginator):
    def paginate(
        self,
        thingName: Optional[str] = None,
        securityProfileName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAttachedPolicies(Paginator):
    def paginate(
        self,
        target: str,
        recursive: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAuditFindings(Paginator):
    def paginate(
        self,
        taskId: Optional[str] = None,
        checkName: Optional[str] = None,
        resourceIdentifier: Optional[Dict] = None,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAuditTasks(Paginator):
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: Optional[str] = None,
        taskStatus: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAuthorizers(Paginator):
    def paginate(
        self,
        ascendingOrder: Optional[bool] = None,
        status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListBillingGroups(Paginator):
    def paginate(
        self,
        namePrefixFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCACertificates(Paginator):
    def paginate(
        self,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCertificates(Paginator):
    def paginate(
        self,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCertificatesByCA(Paginator):
    def paginate(
        self,
        caCertificateId: str,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListIndices(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobExecutionsForJob(Paginator):
    def paginate(
        self,
        jobId: str,
        status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobExecutionsForThing(Paginator):
    def paginate(
        self,
        thingName: str,
        status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobs(Paginator):
    def paginate(
        self,
        status: Optional[str] = None,
        targetSelection: Optional[str] = None,
        thingGroupName: Optional[str] = None,
        thingGroupId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOTAUpdates(Paginator):
    def paginate(
        self,
        otaUpdateStatus: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOutgoingCertificates(Paginator):
    def paginate(
        self,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPolicies(Paginator):
    def paginate(
        self,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPolicyPrincipals(Paginator):
    def paginate(
        self,
        policyName: str,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPrincipalPolicies(Paginator):
    def paginate(
        self,
        principal: str,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPrincipalThings(Paginator):
    def paginate(
        self,
        principal: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRoleAliases(Paginator):
    def paginate(
        self,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListScheduledAudits(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSecurityProfiles(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSecurityProfilesForTarget(Paginator):
    def paginate(
        self,
        securityProfileTargetArn: str,
        recursive: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStreams(Paginator):
    def paginate(
        self,
        ascendingOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTagsForResource(Paginator):
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTargetsForPolicy(Paginator):
    def paginate(
        self,
        policyName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTargetsForSecurityProfile(Paginator):
    def paginate(
        self,
        securityProfileName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListThingGroups(Paginator):
    def paginate(
        self,
        parentGroup: Optional[str] = None,
        namePrefixFilter: Optional[str] = None,
        recursive: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListThingGroupsForThing(Paginator):
    def paginate(
        self,
        thingName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListThingRegistrationTasks(Paginator):
    def paginate(
        self,
        status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListThingTypes(Paginator):
    def paginate(
        self,
        thingTypeName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListThings(Paginator):
    def paginate(
        self,
        attributeName: Optional[str] = None,
        attributeValue: Optional[str] = None,
        thingTypeName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListThingsInBillingGroup(Paginator):
    def paginate(
        self,
        billingGroupName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListThingsInThingGroup(Paginator):
    def paginate(
        self,
        thingGroupName: str,
        recursive: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTopicRules(Paginator):
    def paginate(
        self,
        topic: Optional[str] = None,
        ruleDisabled: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListV2LoggingLevels(Paginator):
    def paginate(
        self,
        targetType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListViolationEvents(Paginator):
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: Optional[str] = None,
        securityProfileName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

