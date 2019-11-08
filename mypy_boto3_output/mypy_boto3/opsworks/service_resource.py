from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3.opsworks.service_resource as opsworks_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    stacks: opsworks_service_resource_scope.stacks

    # pylint: disable=arguments-differ
    def Layer(self, id: str = None) -> opsworks_service_resource_scope.Layer:
        pass

    # pylint: disable=arguments-differ
    def Stack(self, id: str = None) -> opsworks_service_resource_scope.Stack:
        pass

    # pylint: disable=arguments-differ
    def StackSummary(
        self, stack_id: str = None
    ) -> opsworks_service_resource_scope.StackSummary:
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
    ) -> opsworks_service_resource_scope.Stack:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Layer(Boto3ServiceResource):
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

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class Stack(Boto3ServiceResource):
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
    layers: opsworks_service_resource_scope.layers

    # pylint: disable=arguments-differ
    def create_layer(
        self,
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
    ) -> opsworks_service_resource_scope.Layer:
        pass

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class StackSummary(Boto3ServiceResource):
    name: str
    arn: str
    layers_count: int
    apps_count: int
    instances_count: Dict
    stack_id: str

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class stacks(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[opsworks_service_resource_scope.Stack]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, StackIds: List[Any] = None
    ) -> List[opsworks_service_resource_scope.Stack]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[opsworks_service_resource_scope.Stack]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[opsworks_service_resource_scope.Stack]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class layers(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[opsworks_service_resource_scope.Layer]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, LayerIds: List[Any] = None
    ) -> List[opsworks_service_resource_scope.Layer]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[opsworks_service_resource_scope.Layer]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[opsworks_service_resource_scope.Layer]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
