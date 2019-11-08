"Main interface for ec2 service"

from mypy_boto3.ec2.client import Client
from mypy_boto3.ec2.service_resource import ClassicAddress
from mypy_boto3.ec2.service_resource import DhcpOptions
from mypy_boto3.ec2.service_resource import Image
from mypy_boto3.ec2.service_resource import Instance
from mypy_boto3.ec2.service_resource import InternetGateway
from mypy_boto3.ec2.service_resource import KeyPair
from mypy_boto3.ec2.service_resource import KeyPairInfo
from mypy_boto3.ec2.service_resource import NetworkAcl
from mypy_boto3.ec2.service_resource import NetworkInterface
from mypy_boto3.ec2.service_resource import NetworkInterfaceAssociation
from mypy_boto3.ec2.service_resource import PlacementGroup
from mypy_boto3.ec2.service_resource import Route
from mypy_boto3.ec2.service_resource import RouteTable
from mypy_boto3.ec2.service_resource import RouteTableAssociation
from mypy_boto3.ec2.service_resource import SecurityGroup
from mypy_boto3.ec2.service_resource import ServiceResource
from mypy_boto3.ec2.service_resource import Snapshot
from mypy_boto3.ec2.service_resource import Subnet
from mypy_boto3.ec2.service_resource import Tag
from mypy_boto3.ec2.service_resource import Volume
from mypy_boto3.ec2.service_resource import Vpc
from mypy_boto3.ec2.service_resource import VpcAddress
from mypy_boto3.ec2.service_resource import VpcPeeringConnection
from mypy_boto3.ec2.service_resource import accepted_vpc_peering_connections
from mypy_boto3.ec2.service_resource import classic_addresses
from mypy_boto3.ec2.service_resource import dhcp_options_sets
from mypy_boto3.ec2.service_resource import images
from mypy_boto3.ec2.service_resource import instances
from mypy_boto3.ec2.service_resource import internet_gateways
from mypy_boto3.ec2.service_resource import key_pairs
from mypy_boto3.ec2.service_resource import network_acls
from mypy_boto3.ec2.service_resource import network_interfaces
from mypy_boto3.ec2.service_resource import placement_groups
from mypy_boto3.ec2.service_resource import requested_vpc_peering_connections
from mypy_boto3.ec2.service_resource import route_tables
from mypy_boto3.ec2.service_resource import security_groups
from mypy_boto3.ec2.service_resource import snapshots
from mypy_boto3.ec2.service_resource import subnets
from mypy_boto3.ec2.service_resource import volumes
from mypy_boto3.ec2.service_resource import vpc_addresses
from mypy_boto3.ec2.service_resource import vpc_peering_connections
from mypy_boto3.ec2.service_resource import vpcs

__all__ = (
    "Client",
    "ClassicAddress",
    "DhcpOptions",
    "Image",
    "Instance",
    "InternetGateway",
    "KeyPair",
    "KeyPairInfo",
    "NetworkAcl",
    "NetworkInterface",
    "NetworkInterfaceAssociation",
    "PlacementGroup",
    "Route",
    "RouteTable",
    "RouteTableAssociation",
    "SecurityGroup",
    "ServiceResource",
    "Snapshot",
    "Subnet",
    "Tag",
    "Volume",
    "Vpc",
    "VpcAddress",
    "VpcPeeringConnection",
    "accepted_vpc_peering_connections",
    "classic_addresses",
    "dhcp_options_sets",
    "images",
    "instances",
    "internet_gateways",
    "key_pairs",
    "network_acls",
    "network_interfaces",
    "placement_groups",
    "requested_vpc_peering_connections",
    "route_tables",
    "security_groups",
    "snapshots",
    "subnets",
    "volumes",
    "vpc_addresses",
    "vpc_peering_connections",
    "vpcs",
)
