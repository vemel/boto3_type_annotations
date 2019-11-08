from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def assign_instance(self, InstanceId: str, LayerIds: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def assign_volume(self, VolumeId: str, InstanceId: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def associate_elastic_ip(self, ElasticIp: str, InstanceId: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def attach_elastic_load_balancer(
        self, ElasticLoadBalancerName: str, LayerId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def clone_stack(
        self,
        SourceStackId: str,
        ServiceRoleArn: str,
        Name: str = None,
        Region: str = None,
        VpcId: str = None,
        Attributes: Dict[str, Any] = None,
        DefaultInstanceProfileArn: str = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: Dict[str, Any] = None,
        ChefConfiguration: Dict[str, Any] = None,
        UseCustomCookbooks: bool = None,
        UseOpsworksSecurityGroups: bool = None,
        CustomCookbooksSource: Dict[str, Any] = None,
        DefaultSshKeyName: str = None,
        ClonePermissions: bool = None,
        CloneAppIds: List[Any] = None,
        DefaultRootDeviceType: str = None,
        AgentVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_app(
        self,
        StackId: str,
        Name: str,
        Type: str,
        Shortname: str = None,
        Description: str = None,
        DataSources: List[Any] = None,
        AppSource: Dict[str, Any] = None,
        Domains: List[Any] = None,
        EnableSsl: bool = None,
        SslConfiguration: Dict[str, Any] = None,
        Attributes: Dict[str, Any] = None,
        Environment: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_deployment(
        self,
        StackId: str,
        Command: Dict[str, Any],
        AppId: str = None,
        InstanceIds: List[Any] = None,
        LayerIds: List[Any] = None,
        Comment: str = None,
        CustomJson: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_instance(
        self,
        StackId: str,
        LayerIds: List[Any],
        InstanceType: str,
        AutoScalingType: str = None,
        Hostname: str = None,
        Os: str = None,
        AmiId: str = None,
        SshKeyName: str = None,
        AvailabilityZone: str = None,
        VirtualizationType: str = None,
        SubnetId: str = None,
        Architecture: str = None,
        RootDeviceType: str = None,
        BlockDeviceMappings: List[Any] = None,
        InstallUpdatesOnBoot: bool = None,
        EbsOptimized: bool = None,
        AgentVersion: str = None,
        Tenancy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_layer(
        self,
        StackId: str,
        Type: str,
        Name: str,
        Shortname: str,
        Attributes: Dict[str, Any] = None,
        CloudWatchLogsConfiguration: Dict[str, Any] = None,
        CustomInstanceProfileArn: str = None,
        CustomJson: str = None,
        CustomSecurityGroupIds: List[Any] = None,
        Packages: List[Any] = None,
        VolumeConfigurations: List[Any] = None,
        EnableAutoHealing: bool = None,
        AutoAssignElasticIps: bool = None,
        AutoAssignPublicIps: bool = None,
        CustomRecipes: Dict[str, Any] = None,
        InstallUpdatesOnBoot: bool = None,
        UseEbsOptimizedInstances: bool = None,
        LifecycleEventConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stack(
        self,
        Name: str,
        Region: str,
        ServiceRoleArn: str,
        DefaultInstanceProfileArn: str,
        VpcId: str = None,
        Attributes: Dict[str, Any] = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: Dict[str, Any] = None,
        ChefConfiguration: Dict[str, Any] = None,
        UseCustomCookbooks: bool = None,
        UseOpsworksSecurityGroups: bool = None,
        CustomCookbooksSource: Dict[str, Any] = None,
        DefaultSshKeyName: str = None,
        DefaultRootDeviceType: str = None,
        AgentVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_user_profile(
        self,
        IamUserArn: str,
        SshUsername: str = None,
        SshPublicKey: str = None,
        AllowSelfManagement: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_app(self, AppId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_instance(
        self, InstanceId: str, DeleteElasticIp: bool = None, DeleteVolumes: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_layer(self, LayerId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_stack(self, StackId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_user_profile(self, IamUserArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def deregister_ecs_cluster(self, EcsClusterArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def deregister_elastic_ip(self, ElasticIp: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def deregister_instance(self, InstanceId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def deregister_rds_db_instance(self, RdsDbInstanceArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def deregister_volume(self, VolumeId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_agent_versions(
        self, StackId: str = None, ConfigurationManager: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_apps(
        self, StackId: str = None, AppIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_commands(
        self,
        DeploymentId: str = None,
        InstanceId: str = None,
        CommandIds: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_deployments(
        self, StackId: str = None, AppId: str = None, DeploymentIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_ecs_clusters(
        self,
        EcsClusterArns: List[Any] = None,
        StackId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_elastic_ips(
        self, InstanceId: str = None, StackId: str = None, Ips: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_elastic_load_balancers(
        self, StackId: str = None, LayerIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instances(
        self, StackId: str = None, LayerId: str = None, InstanceIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_layers(
        self, StackId: str = None, LayerIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_load_based_auto_scaling(self, LayerIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_my_user_profile(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_operating_systems(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_permissions(
        self, IamUserArn: str = None, StackId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_raid_arrays(
        self,
        InstanceId: str = None,
        StackId: str = None,
        RaidArrayIds: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_rds_db_instances(
        self, StackId: str, RdsDbInstanceArns: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_service_errors(
        self,
        StackId: str = None,
        InstanceId: str = None,
        ServiceErrorIds: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_provisioning_parameters(self, StackId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_summary(self, StackId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stacks(self, StackIds: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_time_based_auto_scaling(
        self, InstanceIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_user_profiles(self, IamUserArns: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_volumes(
        self,
        InstanceId: str = None,
        StackId: str = None,
        RaidArrayId: str = None,
        VolumeIds: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_elastic_load_balancer(
        self, ElasticLoadBalancerName: str, LayerId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def disassociate_elastic_ip(self, ElasticIp: str) -> None:
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
    def get_hostname_suggestion(self, LayerId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def grant_access(
        self, InstanceId: str, ValidForInMinutes: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_instance(self, InstanceId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def register_ecs_cluster(self, EcsClusterArn: str, StackId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_elastic_ip(self, ElasticIp: str, StackId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_instance(
        self,
        StackId: str,
        Hostname: str = None,
        PublicIp: str = None,
        PrivateIp: str = None,
        RsaPublicKey: str = None,
        RsaPublicKeyFingerprint: str = None,
        InstanceIdentity: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_rds_db_instance(
        self, StackId: str, RdsDbInstanceArn: str, DbUser: str, DbPassword: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def register_volume(self, StackId: str, Ec2VolumeId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_load_based_auto_scaling(
        self,
        LayerId: str,
        Enable: bool = None,
        UpScaling: Dict[str, Any] = None,
        DownScaling: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_permission(
        self,
        StackId: str,
        IamUserArn: str,
        AllowSsh: bool = None,
        AllowSudo: bool = None,
        Level: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_time_based_auto_scaling(
        self, InstanceId: str, AutoScalingSchedule: Dict[str, Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def start_instance(self, InstanceId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def start_stack(self, StackId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_instance(self, InstanceId: str, Force: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_stack(self, StackId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def unassign_instance(self, InstanceId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def unassign_volume(self, VolumeId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_app(
        self,
        AppId: str,
        Name: str = None,
        Description: str = None,
        DataSources: List[Any] = None,
        Type: str = None,
        AppSource: Dict[str, Any] = None,
        Domains: List[Any] = None,
        EnableSsl: bool = None,
        SslConfiguration: Dict[str, Any] = None,
        Attributes: Dict[str, Any] = None,
        Environment: List[Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_elastic_ip(self, ElasticIp: str, Name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_instance(
        self,
        InstanceId: str,
        LayerIds: List[Any] = None,
        InstanceType: str = None,
        AutoScalingType: str = None,
        Hostname: str = None,
        Os: str = None,
        AmiId: str = None,
        SshKeyName: str = None,
        Architecture: str = None,
        InstallUpdatesOnBoot: bool = None,
        EbsOptimized: bool = None,
        AgentVersion: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_layer(
        self,
        LayerId: str,
        Name: str = None,
        Shortname: str = None,
        Attributes: Dict[str, Any] = None,
        CloudWatchLogsConfiguration: Dict[str, Any] = None,
        CustomInstanceProfileArn: str = None,
        CustomJson: str = None,
        CustomSecurityGroupIds: List[Any] = None,
        Packages: List[Any] = None,
        VolumeConfigurations: List[Any] = None,
        EnableAutoHealing: bool = None,
        AutoAssignElasticIps: bool = None,
        AutoAssignPublicIps: bool = None,
        CustomRecipes: Dict[str, Any] = None,
        InstallUpdatesOnBoot: bool = None,
        UseEbsOptimizedInstances: bool = None,
        LifecycleEventConfiguration: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_my_user_profile(self, SshPublicKey: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_rds_db_instance(
        self, RdsDbInstanceArn: str, DbUser: str = None, DbPassword: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_stack(
        self,
        StackId: str,
        Name: str = None,
        Attributes: Dict[str, Any] = None,
        ServiceRoleArn: str = None,
        DefaultInstanceProfileArn: str = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: Dict[str, Any] = None,
        ChefConfiguration: Dict[str, Any] = None,
        UseCustomCookbooks: bool = None,
        CustomCookbooksSource: Dict[str, Any] = None,
        DefaultSshKeyName: str = None,
        DefaultRootDeviceType: str = None,
        UseOpsworksSecurityGroups: bool = None,
        AgentVersion: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_user_profile(
        self,
        IamUserArn: str,
        SshUsername: str = None,
        SshPublicKey: str = None,
        AllowSelfManagement: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_volume(
        self, VolumeId: str, Name: str = None, MountPoint: str = None
    ) -> None:
        pass
