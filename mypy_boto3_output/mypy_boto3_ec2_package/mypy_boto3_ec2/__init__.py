"Main interface for ec2 service"

from mypy_boto3_ec2.client import Client
from mypy_boto3_ec2.service_resource import ClassicAddress
from mypy_boto3_ec2.service_resource import DhcpOptions
from mypy_boto3_ec2.service_resource import Image
from mypy_boto3_ec2.service_resource import Instance
from mypy_boto3_ec2.service_resource import InternetGateway
from mypy_boto3_ec2.service_resource import KeyPair
from mypy_boto3_ec2.service_resource import KeyPairInfo
from mypy_boto3_ec2.service_resource import NetworkAcl
from mypy_boto3_ec2.service_resource import NetworkInterface
from mypy_boto3_ec2.service_resource import NetworkInterfaceAssociation
from mypy_boto3_ec2.service_resource import PlacementGroup
from mypy_boto3_ec2.service_resource import Route
from mypy_boto3_ec2.service_resource import RouteTable
from mypy_boto3_ec2.service_resource import RouteTableAssociation
from mypy_boto3_ec2.service_resource import SecurityGroup
from mypy_boto3_ec2.service_resource import ServiceResource
from mypy_boto3_ec2.service_resource import Snapshot
from mypy_boto3_ec2.service_resource import Subnet
from mypy_boto3_ec2.service_resource import Tag
from mypy_boto3_ec2.service_resource import Volume
from mypy_boto3_ec2.service_resource import Vpc
from mypy_boto3_ec2.service_resource import VpcAddress
from mypy_boto3_ec2.service_resource import VpcPeeringConnection


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
)
