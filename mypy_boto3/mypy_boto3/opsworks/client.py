from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def assign_instance(
        self,
        InstanceId: str,
        LayerIds: List,
    ):
        pass


    def assign_volume(
        self,
        VolumeId: str,
        InstanceId: Optional[str] = None,
    ):
        pass


    def associate_elastic_ip(
        self,
        ElasticIp: str,
        InstanceId: Optional[str] = None,
    ):
        pass


    def attach_elastic_load_balancer(
        self,
        ElasticLoadBalancerName: str,
        LayerId: str,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def clone_stack(
        self,
        SourceStackId: str,
        ServiceRoleArn: str,
        Name: Optional[str] = None,
        Region: Optional[str] = None,
        VpcId: Optional[str] = None,
        Attributes: Optional[Dict] = None,
        DefaultInstanceProfileArn: Optional[str] = None,
        DefaultOs: Optional[str] = None,
        HostnameTheme: Optional[str] = None,
        DefaultAvailabilityZone: Optional[str] = None,
        DefaultSubnetId: Optional[str] = None,
        CustomJson: Optional[str] = None,
        ConfigurationManager: Optional[Dict] = None,
        ChefConfiguration: Optional[Dict] = None,
        UseCustomCookbooks: Optional[bool] = None,
        UseOpsworksSecurityGroups: Optional[bool] = None,
        CustomCookbooksSource: Optional[Dict] = None,
        DefaultSshKeyName: Optional[str] = None,
        ClonePermissions: Optional[bool] = None,
        CloneAppIds: Optional[List] = None,
        DefaultRootDeviceType: Optional[str] = None,
        AgentVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def create_app(
        self,
        StackId: str,
        Name: str,
        Type: str,
        Shortname: Optional[str] = None,
        Description: Optional[str] = None,
        DataSources: Optional[List] = None,
        AppSource: Optional[Dict] = None,
        Domains: Optional[List] = None,
        EnableSsl: Optional[bool] = None,
        SslConfiguration: Optional[Dict] = None,
        Attributes: Optional[Dict] = None,
        Environment: Optional[List] = None,
    ) -> Dict:
        pass


    def create_deployment(
        self,
        StackId: str,
        Command: Dict,
        AppId: Optional[str] = None,
        InstanceIds: Optional[List] = None,
        LayerIds: Optional[List] = None,
        Comment: Optional[str] = None,
        CustomJson: Optional[str] = None,
    ) -> Dict:
        pass


    def create_instance(
        self,
        StackId: str,
        LayerIds: List,
        InstanceType: str,
        AutoScalingType: Optional[str] = None,
        Hostname: Optional[str] = None,
        Os: Optional[str] = None,
        AmiId: Optional[str] = None,
        SshKeyName: Optional[str] = None,
        AvailabilityZone: Optional[str] = None,
        VirtualizationType: Optional[str] = None,
        SubnetId: Optional[str] = None,
        Architecture: Optional[str] = None,
        RootDeviceType: Optional[str] = None,
        BlockDeviceMappings: Optional[List] = None,
        InstallUpdatesOnBoot: Optional[bool] = None,
        EbsOptimized: Optional[bool] = None,
        AgentVersion: Optional[str] = None,
        Tenancy: Optional[str] = None,
    ) -> Dict:
        pass


    def create_layer(
        self,
        StackId: str,
        Type: str,
        Name: str,
        Shortname: str,
        Attributes: Optional[Dict] = None,
        CloudWatchLogsConfiguration: Optional[Dict] = None,
        CustomInstanceProfileArn: Optional[str] = None,
        CustomJson: Optional[str] = None,
        CustomSecurityGroupIds: Optional[List] = None,
        Packages: Optional[List] = None,
        VolumeConfigurations: Optional[List] = None,
        EnableAutoHealing: Optional[bool] = None,
        AutoAssignElasticIps: Optional[bool] = None,
        AutoAssignPublicIps: Optional[bool] = None,
        CustomRecipes: Optional[Dict] = None,
        InstallUpdatesOnBoot: Optional[bool] = None,
        UseEbsOptimizedInstances: Optional[bool] = None,
        LifecycleEventConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_stack(
        self,
        Name: str,
        Region: str,
        ServiceRoleArn: str,
        DefaultInstanceProfileArn: str,
        VpcId: Optional[str] = None,
        Attributes: Optional[Dict] = None,
        DefaultOs: Optional[str] = None,
        HostnameTheme: Optional[str] = None,
        DefaultAvailabilityZone: Optional[str] = None,
        DefaultSubnetId: Optional[str] = None,
        CustomJson: Optional[str] = None,
        ConfigurationManager: Optional[Dict] = None,
        ChefConfiguration: Optional[Dict] = None,
        UseCustomCookbooks: Optional[bool] = None,
        UseOpsworksSecurityGroups: Optional[bool] = None,
        CustomCookbooksSource: Optional[Dict] = None,
        DefaultSshKeyName: Optional[str] = None,
        DefaultRootDeviceType: Optional[str] = None,
        AgentVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def create_user_profile(
        self,
        IamUserArn: str,
        SshUsername: Optional[str] = None,
        SshPublicKey: Optional[str] = None,
        AllowSelfManagement: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_app(
        self,
        AppId: str,
    ):
        pass


    def delete_instance(
        self,
        InstanceId: str,
        DeleteElasticIp: Optional[bool] = None,
        DeleteVolumes: Optional[bool] = None,
    ):
        pass


    def delete_layer(
        self,
        LayerId: str,
    ):
        pass


    def delete_stack(
        self,
        StackId: str,
    ):
        pass


    def delete_user_profile(
        self,
        IamUserArn: str,
    ):
        pass


    def deregister_ecs_cluster(
        self,
        EcsClusterArn: str,
    ):
        pass


    def deregister_elastic_ip(
        self,
        ElasticIp: str,
    ):
        pass


    def deregister_instance(
        self,
        InstanceId: str,
    ):
        pass


    def deregister_rds_db_instance(
        self,
        RdsDbInstanceArn: str,
    ):
        pass


    def deregister_volume(
        self,
        VolumeId: str,
    ):
        pass


    def describe_agent_versions(
        self,
        StackId: Optional[str] = None,
        ConfigurationManager: Optional[Dict] = None,
    ) -> Dict:
        pass


    def describe_apps(
        self,
        StackId: Optional[str] = None,
        AppIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_commands(
        self,
        DeploymentId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        CommandIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_deployments(
        self,
        StackId: Optional[str] = None,
        AppId: Optional[str] = None,
        DeploymentIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_ecs_clusters(
        self,
        EcsClusterArns: Optional[List] = None,
        StackId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_elastic_ips(
        self,
        InstanceId: Optional[str] = None,
        StackId: Optional[str] = None,
        Ips: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_elastic_load_balancers(
        self,
        StackId: Optional[str] = None,
        LayerIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_instances(
        self,
        StackId: Optional[str] = None,
        LayerId: Optional[str] = None,
        InstanceIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_layers(
        self,
        StackId: Optional[str] = None,
        LayerIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_load_based_auto_scaling(
        self,
        LayerIds: List,
    ) -> Dict:
        pass


    def describe_my_user_profile(
        self,
    ) -> Dict:
        pass


    def describe_operating_systems(
        self,
    ) -> Dict:
        pass


    def describe_permissions(
        self,
        IamUserArn: Optional[str] = None,
        StackId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_raid_arrays(
        self,
        InstanceId: Optional[str] = None,
        StackId: Optional[str] = None,
        RaidArrayIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_rds_db_instances(
        self,
        StackId: str,
        RdsDbInstanceArns: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_service_errors(
        self,
        StackId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        ServiceErrorIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_stack_provisioning_parameters(
        self,
        StackId: str,
    ) -> Dict:
        pass


    def describe_stack_summary(
        self,
        StackId: str,
    ) -> Dict:
        pass


    def describe_stacks(
        self,
        StackIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_time_based_auto_scaling(
        self,
        InstanceIds: List,
    ) -> Dict:
        pass


    def describe_user_profiles(
        self,
        IamUserArns: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_volumes(
        self,
        InstanceId: Optional[str] = None,
        StackId: Optional[str] = None,
        RaidArrayId: Optional[str] = None,
        VolumeIds: Optional[List] = None,
    ) -> Dict:
        pass


    def detach_elastic_load_balancer(
        self,
        ElasticLoadBalancerName: str,
        LayerId: str,
    ):
        pass


    def disassociate_elastic_ip(
        self,
        ElasticIp: str,
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


    def get_hostname_suggestion(
        self,
        LayerId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def grant_access(
        self,
        InstanceId: str,
        ValidForInMinutes: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        ResourceArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def reboot_instance(
        self,
        InstanceId: str,
    ):
        pass


    def register_ecs_cluster(
        self,
        EcsClusterArn: str,
        StackId: str,
    ) -> Dict:
        pass


    def register_elastic_ip(
        self,
        ElasticIp: str,
        StackId: str,
    ) -> Dict:
        pass


    def register_instance(
        self,
        StackId: str,
        Hostname: Optional[str] = None,
        PublicIp: Optional[str] = None,
        PrivateIp: Optional[str] = None,
        RsaPublicKey: Optional[str] = None,
        RsaPublicKeyFingerprint: Optional[str] = None,
        InstanceIdentity: Optional[Dict] = None,
    ) -> Dict:
        pass


    def register_rds_db_instance(
        self,
        StackId: str,
        RdsDbInstanceArn: str,
        DbUser: str,
        DbPassword: str,
    ):
        pass


    def register_volume(
        self,
        StackId: str,
        Ec2VolumeId: Optional[str] = None,
    ) -> Dict:
        pass


    def set_load_based_auto_scaling(
        self,
        LayerId: str,
        Enable: Optional[bool] = None,
        UpScaling: Optional[Dict] = None,
        DownScaling: Optional[Dict] = None,
    ):
        pass


    def set_permission(
        self,
        StackId: str,
        IamUserArn: str,
        AllowSsh: Optional[bool] = None,
        AllowSudo: Optional[bool] = None,
        Level: Optional[str] = None,
    ):
        pass


    def set_time_based_auto_scaling(
        self,
        InstanceId: str,
        AutoScalingSchedule: Optional[Dict] = None,
    ):
        pass


    def start_instance(
        self,
        InstanceId: str,
    ):
        pass


    def start_stack(
        self,
        StackId: str,
    ):
        pass


    def stop_instance(
        self,
        InstanceId: str,
        Force: Optional[bool] = None,
    ):
        pass


    def stop_stack(
        self,
        StackId: str,
    ):
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ):
        pass


    def unassign_instance(
        self,
        InstanceId: str,
    ):
        pass


    def unassign_volume(
        self,
        VolumeId: str,
    ):
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def update_app(
        self,
        AppId: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        DataSources: Optional[List] = None,
        Type: Optional[str] = None,
        AppSource: Optional[Dict] = None,
        Domains: Optional[List] = None,
        EnableSsl: Optional[bool] = None,
        SslConfiguration: Optional[Dict] = None,
        Attributes: Optional[Dict] = None,
        Environment: Optional[List] = None,
    ):
        pass


    def update_elastic_ip(
        self,
        ElasticIp: str,
        Name: Optional[str] = None,
    ):
        pass


    def update_instance(
        self,
        InstanceId: str,
        LayerIds: Optional[List] = None,
        InstanceType: Optional[str] = None,
        AutoScalingType: Optional[str] = None,
        Hostname: Optional[str] = None,
        Os: Optional[str] = None,
        AmiId: Optional[str] = None,
        SshKeyName: Optional[str] = None,
        Architecture: Optional[str] = None,
        InstallUpdatesOnBoot: Optional[bool] = None,
        EbsOptimized: Optional[bool] = None,
        AgentVersion: Optional[str] = None,
    ):
        pass


    def update_layer(
        self,
        LayerId: str,
        Name: Optional[str] = None,
        Shortname: Optional[str] = None,
        Attributes: Optional[Dict] = None,
        CloudWatchLogsConfiguration: Optional[Dict] = None,
        CustomInstanceProfileArn: Optional[str] = None,
        CustomJson: Optional[str] = None,
        CustomSecurityGroupIds: Optional[List] = None,
        Packages: Optional[List] = None,
        VolumeConfigurations: Optional[List] = None,
        EnableAutoHealing: Optional[bool] = None,
        AutoAssignElasticIps: Optional[bool] = None,
        AutoAssignPublicIps: Optional[bool] = None,
        CustomRecipes: Optional[Dict] = None,
        InstallUpdatesOnBoot: Optional[bool] = None,
        UseEbsOptimizedInstances: Optional[bool] = None,
        LifecycleEventConfiguration: Optional[Dict] = None,
    ):
        pass


    def update_my_user_profile(
        self,
        SshPublicKey: Optional[str] = None,
    ):
        pass


    def update_rds_db_instance(
        self,
        RdsDbInstanceArn: str,
        DbUser: Optional[str] = None,
        DbPassword: Optional[str] = None,
    ):
        pass


    def update_stack(
        self,
        StackId: str,
        Name: Optional[str] = None,
        Attributes: Optional[Dict] = None,
        ServiceRoleArn: Optional[str] = None,
        DefaultInstanceProfileArn: Optional[str] = None,
        DefaultOs: Optional[str] = None,
        HostnameTheme: Optional[str] = None,
        DefaultAvailabilityZone: Optional[str] = None,
        DefaultSubnetId: Optional[str] = None,
        CustomJson: Optional[str] = None,
        ConfigurationManager: Optional[Dict] = None,
        ChefConfiguration: Optional[Dict] = None,
        UseCustomCookbooks: Optional[bool] = None,
        CustomCookbooksSource: Optional[Dict] = None,
        DefaultSshKeyName: Optional[str] = None,
        DefaultRootDeviceType: Optional[str] = None,
        UseOpsworksSecurityGroups: Optional[bool] = None,
        AgentVersion: Optional[str] = None,
    ):
        pass


    def update_user_profile(
        self,
        IamUserArn: str,
        SshUsername: Optional[str] = None,
        SshPublicKey: Optional[str] = None,
        AllowSelfManagement: Optional[bool] = None,
    ):
        pass


    def update_volume(
        self,
        VolumeId: str,
        Name: Optional[str] = None,
        MountPoint: Optional[str] = None,
    ):
        pass

