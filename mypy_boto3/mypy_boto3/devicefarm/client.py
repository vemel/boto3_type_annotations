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


    def create_device_pool(
        self,
        projectArn: str,
        name: str,
        rules: List,
        description: Optional[str] = None,
        maxDevices: Optional[int] = None,
    ) -> Dict:
        pass


    def create_instance_profile(
        self,
        name: str,
        description: Optional[str] = None,
        packageCleanup: Optional[bool] = None,
        excludeAppPackagesFromCleanup: Optional[List] = None,
        rebootAfterUse: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_network_profile(
        self,
        projectArn: str,
        name: str,
        description: Optional[str] = None,
        type: Optional[str] = None,
        uplinkBandwidthBits: Optional[int] = None,
        downlinkBandwidthBits: Optional[int] = None,
        uplinkDelayMs: Optional[int] = None,
        downlinkDelayMs: Optional[int] = None,
        uplinkJitterMs: Optional[int] = None,
        downlinkJitterMs: Optional[int] = None,
        uplinkLossPercent: Optional[int] = None,
        downlinkLossPercent: Optional[int] = None,
    ) -> Dict:
        pass


    def create_project(
        self,
        name: str,
        defaultJobTimeoutMinutes: Optional[int] = None,
    ) -> Dict:
        pass


    def create_remote_access_session(
        self,
        projectArn: str,
        deviceArn: str,
        instanceArn: Optional[str] = None,
        sshPublicKey: Optional[str] = None,
        remoteDebugEnabled: Optional[bool] = None,
        remoteRecordEnabled: Optional[bool] = None,
        remoteRecordAppArn: Optional[str] = None,
        name: Optional[str] = None,
        clientId: Optional[str] = None,
        configuration: Optional[Dict] = None,
        interactionMode: Optional[str] = None,
        skipAppResign: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_upload(
        self,
        projectArn: str,
        name: str,
        type: str,
        contentType: Optional[str] = None,
    ) -> Dict:
        pass


    def create_vpce_configuration(
        self,
        vpceConfigurationName: str,
        vpceServiceName: str,
        serviceDnsName: str,
        vpceConfigurationDescription: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_device_pool(
        self,
        arn: str,
    ) -> Dict:
        pass


    def delete_instance_profile(
        self,
        arn: str,
    ) -> Dict:
        pass


    def delete_network_profile(
        self,
        arn: str,
    ) -> Dict:
        pass


    def delete_project(
        self,
        arn: str,
    ) -> Dict:
        pass


    def delete_remote_access_session(
        self,
        arn: str,
    ) -> Dict:
        pass


    def delete_run(
        self,
        arn: str,
    ) -> Dict:
        pass


    def delete_upload(
        self,
        arn: str,
    ) -> Dict:
        pass


    def delete_vpce_configuration(
        self,
        arn: str,
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


    def get_account_settings(
        self,
    ) -> Dict:
        pass


    def get_device(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_device_instance(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_device_pool(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_device_pool_compatibility(
        self,
        devicePoolArn: str,
        appArn: Optional[str] = None,
        testType: Optional[str] = None,
        test: Optional[Dict] = None,
        configuration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_instance_profile(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_job(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_network_profile(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_offering_status(
        self,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_project(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_remote_access_session(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_run(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_suite(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_test(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_upload(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_vpce_configuration(
        self,
        arn: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def install_to_remote_access_session(
        self,
        remoteAccessSessionArn: str,
        appArn: str,
    ) -> Dict:
        pass


    def list_artifacts(
        self,
        arn: str,
        type: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_device_instances(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_device_pools(
        self,
        arn: str,
        type: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_devices(
        self,
        arn: Optional[str] = None,
        nextToken: Optional[str] = None,
        filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_instance_profiles(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_jobs(
        self,
        arn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_network_profiles(
        self,
        arn: str,
        type: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_offering_promotions(
        self,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_offering_transactions(
        self,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_offerings(
        self,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_projects(
        self,
        arn: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_remote_access_sessions(
        self,
        arn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_runs(
        self,
        arn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_samples(
        self,
        arn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_suites(
        self,
        arn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceARN: str,
    ) -> Dict:
        pass


    def list_tests(
        self,
        arn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_unique_problems(
        self,
        arn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_uploads(
        self,
        arn: str,
        type: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_vpce_configurations(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def purchase_offering(
        self,
        offeringId: Optional[str] = None,
        quantity: Optional[int] = None,
        offeringPromotionId: Optional[str] = None,
    ) -> Dict:
        pass


    def renew_offering(
        self,
        offeringId: Optional[str] = None,
        quantity: Optional[int] = None,
    ) -> Dict:
        pass


    def schedule_run(
        self,
        projectArn: str,
        test: Dict,
        appArn: Optional[str] = None,
        devicePoolArn: Optional[str] = None,
        deviceSelectionConfiguration: Optional[Dict] = None,
        name: Optional[str] = None,
        configuration: Optional[Dict] = None,
        executionConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def stop_job(
        self,
        arn: str,
    ) -> Dict:
        pass


    def stop_remote_access_session(
        self,
        arn: str,
    ) -> Dict:
        pass


    def stop_run(
        self,
        arn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceARN: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceARN: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_device_instance(
        self,
        arn: str,
        profileArn: Optional[str] = None,
        labels: Optional[List] = None,
    ) -> Dict:
        pass


    def update_device_pool(
        self,
        arn: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        rules: Optional[List] = None,
        maxDevices: Optional[int] = None,
        clearMaxDevices: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_instance_profile(
        self,
        arn: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        packageCleanup: Optional[bool] = None,
        excludeAppPackagesFromCleanup: Optional[List] = None,
        rebootAfterUse: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_network_profile(
        self,
        arn: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        type: Optional[str] = None,
        uplinkBandwidthBits: Optional[int] = None,
        downlinkBandwidthBits: Optional[int] = None,
        uplinkDelayMs: Optional[int] = None,
        downlinkDelayMs: Optional[int] = None,
        uplinkJitterMs: Optional[int] = None,
        downlinkJitterMs: Optional[int] = None,
        uplinkLossPercent: Optional[int] = None,
        downlinkLossPercent: Optional[int] = None,
    ) -> Dict:
        pass


    def update_project(
        self,
        arn: str,
        name: Optional[str] = None,
        defaultJobTimeoutMinutes: Optional[int] = None,
    ) -> Dict:
        pass


    def update_upload(
        self,
        arn: str,
        name: Optional[str] = None,
        contentType: Optional[str] = None,
        editContent: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_vpce_configuration(
        self,
        arn: str,
        vpceConfigurationName: Optional[str] = None,
        vpceServiceName: Optional[str] = None,
        serviceDnsName: Optional[str] = None,
        vpceConfigurationDescription: Optional[str] = None,
    ) -> Dict:
        pass

