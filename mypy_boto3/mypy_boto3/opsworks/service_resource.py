from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from boto3.resources.base import ServiceResource
from boto3.resources.collection import ResourceCollection


class ServiceResource(base.ServiceResource):
    stacks: 'stacks'

    def Layer(
        self,
        id: Optional[str] = None,
    ) -> 'Layer':
        pass


    def Stack(
        self,
        id: Optional[str] = None,
    ) -> 'Stack':
        pass


    def StackSummary(
        self,
        stack_id: Optional[str] = None,
    ) -> 'StackSummary':
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
    ) -> 'Stack':
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class Layer(base.ServiceResource):
    arn: str
    stack_id: str
    layer_id: str
    type: str
    name: str
    shortname: str
    attributes: Dict
    cloud_watch_logs_configuration: Dict
    custom_instance_profile_arn: str
    custom_json: str
    custom_security_group_ids: List
    default_security_group_names: List
    packages: List
    volume_configurations: List
    enable_auto_healing: bool
    auto_assign_elastic_ips: bool
    auto_assign_public_ips: bool
    default_recipes: Dict
    custom_recipes: Dict
    created_at: str
    install_updates_on_boot: bool
    use_ebs_optimized_instances: bool
    lifecycle_event_configuration: Dict
    id: str

    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class Stack(base.ServiceResource):
    stack_id: str
    name: str
    arn: str
    region: str
    vpc_id: str
    attributes: Dict
    service_role_arn: str
    default_instance_profile_arn: str
    default_os: str
    hostname_theme: str
    default_availability_zone: str
    default_subnet_id: str
    custom_json: str
    configuration_manager: Dict
    chef_configuration: Dict
    use_custom_cookbooks: bool
    use_opsworks_security_groups: bool
    custom_cookbooks_source: Dict
    default_ssh_key_name: str
    created_at: str
    default_root_device_type: str
    agent_version: str
    id: str
    layers: 'layers'

    def create_layer(
        self,
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
    ) -> 'Layer':
        pass


    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class StackSummary(base.ServiceResource):
    name: str
    arn: str
    layers_count: int
    apps_count: int
    instances_count: Dict
    stack_id: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class stacks(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Stack']:
        pass


    @classmethod
    def filter(
        cls,
        StackIds: Optional[List] = None,
    ) -> List['Stack']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Stack']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Stack']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass

