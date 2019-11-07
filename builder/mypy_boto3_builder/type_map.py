from datetime import datetime
from typing import Callable, IO, List, Dict, Union, Any

from boto3.resources.collection import ResourceCollection
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter

from mypy_boto3_builder.structures import (
    TypeAnnotation,
    InternalImport,
    AnnotationWrapper,
)
from mypy_boto3_builder.service_name import ServiceName

TYPE_MAP: Dict[str, TypeAnnotation] = {
    "bytes": bytes,
    "blob": bytes,
    "boolean": bool,
    "function": Callable[..., Any],
    "botocore or boto3 Client": BaseClient,
    "datetime": datetime,
    "timestamp": datetime,
    "dict": Dict[str, Any],
    "structure": Dict[str, Any],
    "map": Dict[str, Any],
    "float": float,
    "double": float,
    "int": int,
    "integer": int,
    "long": int,
    "a file-like object": IO[Any],
    "seekable file-like object": IO[Any],
    "list": List[Any],
    "L{botocore.paginate.Paginator}": Paginator,
    ":py:class:`ResourceCollection`": ResourceCollection,
    "JSON serializable": str,
    "string": str,
    "str": str,
    "boto3.s3.transfer.TransferConfig": TransferConfig,
    "botocore.waiter.Waiter": Waiter,
    "bytes or seekable file-like object": Union[bytes, IO],
    "str or dict": Union[str, Dict],
    "list(string)": List[str],
    "list of str": List[str],
    "None": type(None),
    ":py:class:`ec2.NetworkAcl`": InternalImport("NetworkAcl", ServiceName.ec2),
    ":py:class:`EC2.NetworkAcl`": InternalImport("NetworkAcl", ServiceName.ec2),
    "list(:py:class:`ec2.InternetGateway`)": AnnotationWrapper(
        parent=List, children=(InternalImport("InternetGateway", ServiceName.ec2),),
    ),
    ":py:class:`iam.UserPolicy`": InternalImport("UserPolicy", ServiceName.iam),
    ":py:class:`IAM.UserPolicy`": InternalImport("UserPolicy", ServiceName.iam),
    "list(:py:class:`iam.VirtualMfaDevice`)": AnnotationWrapper(
        parent=List, children=(InternalImport("VirtualMfaDevice", ServiceName.iam),),
    ),
    "list(:py:class:`ec2.Image`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Image", ServiceName.ec2),),
    ),
    "list(:py:class:`cloudwatch.Alarm`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Alarm", ServiceName.cloudwatch),),
    ),
    "list(:py:class:`opsworks.Layer`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Layer", ServiceName.opsworks),),
    ),
    ":py:class:`iam.GroupPolicy`": InternalImport("GroupPolicy", ServiceName.iam),
    ":py:class:`IAM.GroupPolicy`": InternalImport("GroupPolicy", ServiceName.iam),
    "list(:py:class:`iam.SigningCertificate`)": AnnotationWrapper(
        parent=List, children=(InternalImport("SigningCertificate", ServiceName.iam),),
    ),
    "list(:py:class:`ec2.Volume`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Volume", ServiceName.ec2),),
    ),
    "list(:py:class:`ec2.VpcPeeringConnection`)": AnnotationWrapper(
        parent=List,
        children=(InternalImport("VpcPeeringConnection", ServiceName.ec2),),
    ),
    ":py:class:`ec2.Subnet`": InternalImport("Subnet", ServiceName.ec2),
    ":py:class:`EC2.Subnet`": InternalImport("Subnet", ServiceName.ec2),
    "list(:py:class:`iam.ServerCertificate`)": AnnotationWrapper(
        parent=List, children=(InternalImport("ServerCertificate", ServiceName.iam),),
    ),
    "list(:py:class:`ec2.VpcAddress`)": AnnotationWrapper(
        parent=List, children=(InternalImport("VpcAddress", ServiceName.ec2),),
    ),
    ":py:class:`sns.PlatformEndpoint`": InternalImport(
        "PlatformEndpoint", ServiceName.sns
    ),
    ":py:class:`SNS.PlatformEndpoint`": InternalImport(
        "PlatformEndpoint", ServiceName.sns
    ),
    ":py:class:`s3.MultipartUpload`": InternalImport("MultipartUpload", ServiceName.s3),
    ":py:class:`glacier.MultipartUpload`": InternalImport(
        "MultipartUpload", ServiceName.glacier
    ),
    ":py:class:`Glacier.MultipartUpload`": InternalImport(
        "MultipartUpload", ServiceName.glacier
    ),
    ":py:class:`S3.MultipartUpload`": InternalImport("MultipartUpload", ServiceName.s3),
    "list(:py:class:`ec2.Subnet`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Subnet", ServiceName.ec2),),
    ),
    ":py:class:`opsworks.Layer`": InternalImport("Layer", ServiceName.opsworks),
    ":py:class:`OpsWorks.Layer`": InternalImport("Layer", ServiceName.opsworks),
    "list(:py:class:`iam.MfaDevice`)": AnnotationWrapper(
        parent=List, children=(InternalImport("MfaDevice", ServiceName.iam),),
    ),
    "list(:py:class:`glacier.Job`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Job", ServiceName.glacier),),
    ),
    "list(:py:class:`iam.RolePolicy`)": AnnotationWrapper(
        parent=List, children=(InternalImport("RolePolicy", ServiceName.iam),),
    ),
    "list(:py:class:`iam.InstanceProfile`)": AnnotationWrapper(
        parent=List, children=(InternalImport("InstanceProfile", ServiceName.iam),),
    ),
    "list(:py:class:`ec2.Instance`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Instance", ServiceName.ec2),),
    ),
    ":py:class:`glacier.Vault`": InternalImport("Vault", ServiceName.glacier),
    ":py:class:`Glacier.Vault`": InternalImport("Vault", ServiceName.glacier),
    ":py:class:`ec2.SecurityGroup`": InternalImport("SecurityGroup", ServiceName.ec2),
    ":py:class:`EC2.SecurityGroup`": InternalImport("SecurityGroup", ServiceName.ec2),
    ":py:class:`ec2.RouteTable`": InternalImport("RouteTable", ServiceName.ec2),
    ":py:class:`EC2.RouteTable`": InternalImport("RouteTable", ServiceName.ec2),
    "list(:py:class:`dynamodb.Table`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Table", ServiceName.dynamodb),),
    ),
    "list(:py:class:`ec2.Snapshot`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Snapshot", ServiceName.ec2),),
    ),
    "list(:py:class:`sqs.Message`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Message", ServiceName.sqs),),
    ),
    "list(:py:class:`iam.Role`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Role", ServiceName.iam),),
    ),
    ":py:class:`glacier.Job`": InternalImport("Job", ServiceName.glacier),
    ":py:class:`Glacier.Job`": InternalImport("Job", ServiceName.glacier),
    "list(:py:class:`cloudwatch.Metric`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Metric", ServiceName.cloudwatch),),
    ),
    "list(:py:class:`iam.Policy`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Policy", ServiceName.iam),),
    ),
    "list(:py:class:`ec2.ClassicAddress`)": AnnotationWrapper(
        parent=List, children=(InternalImport("ClassicAddress", ServiceName.ec2),),
    ),
    "list(:py:class:`iam.User`)": AnnotationWrapper(
        parent=List, children=(InternalImport("User", ServiceName.iam),),
    ),
    "list(:py:class:`iam.GroupPolicy`)": AnnotationWrapper(
        parent=List, children=(InternalImport("GroupPolicy", ServiceName.iam),),
    ),
    "list(:py:class:`iam.PolicyVersion`)": AnnotationWrapper(
        parent=List, children=(InternalImport("PolicyVersion", ServiceName.iam),),
    ),
    "list(:py:class:`sns.Topic`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Topic", ServiceName.sns),),
    ),
    ":py:class:`iam.LoginProfile`": InternalImport("LoginProfile", ServiceName.iam),
    ":py:class:`IAM.LoginProfile`": InternalImport("LoginProfile", ServiceName.iam),
    "list(:py:class:`iam.UserPolicy`)": AnnotationWrapper(
        parent=List, children=(InternalImport("UserPolicy", ServiceName.iam),),
    ),
    "list(:py:class:`cloudformation.Event`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Event", ServiceName.cloudformation),),
    ),
    ":py:class:`cloudformation.Event`": InternalImport(
        "Event", ServiceName.cloudformation
    ),
    ":py:class:`CloudFormation.Event`": InternalImport(
        "Event", ServiceName.cloudformation
    ),
    "list(:py:class:`s3.MultipartUpload`)": AnnotationWrapper(
        parent=List, children=(InternalImport("MultipartUpload", ServiceName.s3),),
    ),
    "list(:py:class:`glacier.MultipartUpload`)": AnnotationWrapper(
        parent=List, children=(InternalImport("MultipartUpload", ServiceName.glacier),),
    ),
    "list(:py:class:`sns.Subscription`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Subscription", ServiceName.sns),),
    ),
    ":py:class:`iam.PolicyVersion`": InternalImport("PolicyVersion", ServiceName.iam),
    ":py:class:`IAM.PolicyVersion`": InternalImport("PolicyVersion", ServiceName.iam),
    "list(:py:class:`~boto3.resources.base.ServiceResource`)": List[
        Boto3ServiceResource
    ],
    "list(:py:class:`ec2.NetworkInterface`)": AnnotationWrapper(
        parent=List, children=(InternalImport("NetworkInterface", ServiceName.ec2),),
    ),
    "list(:py:class:`s3.ObjectVersion`)": AnnotationWrapper(
        parent=List, children=(InternalImport("ObjectVersion", ServiceName.s3),),
    ),
    "list(:py:class:`ec2.SecurityGroup`)": AnnotationWrapper(
        parent=List, children=(InternalImport("SecurityGroup", ServiceName.ec2),),
    ),
    "list(:py:class:`sqs.Queue`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Queue", ServiceName.sqs),),
    ),
    "list(:py:class:`ec2.PlacementGroup`)": AnnotationWrapper(
        parent=List, children=(InternalImport("PlacementGroup", ServiceName.ec2),),
    ),
    "list(:py:class:`ec2.Vpc`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Vpc", ServiceName.ec2),),
    ),
    "list(:py:class:`ec2.RouteTable`)": AnnotationWrapper(
        parent=List, children=(InternalImport("RouteTable", ServiceName.ec2),),
    ),
    "list(:py:class:`glacier.Vault`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Vault", ServiceName.glacier),),
    ),
    "list(:py:class:`iam.Group`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Group", ServiceName.iam),),
    ),
    ":py:class:`iam.Group`": AnnotationWrapper(
        parent=List, children=(InternalImport("Group", ServiceName.iam),),
    ),
    ":py:class:`ec2.Image`": InternalImport("Image", ServiceName.ec2),
    ":py:class:`EC2.Image`": InternalImport("Image", ServiceName.ec2),
    ":py:class:`ec2.Route`": InternalImport("Route", ServiceName.ec2),
    ":py:class:`EC2.Route`": InternalImport("Route", ServiceName.ec2),
    ":py:class:`ec2.VpcPeeringConnection`": InternalImport(
        "VpcPeeringConnection", ServiceName.ec2
    ),
    ":py:class:`EC2.VpcPeeringConnection`": InternalImport(
        "VpcPeeringConnection", ServiceName.ec2
    ),
    "list(:py:class:`cloudformation.Stack`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Stack", ServiceName.cloudformation),),
    ),
    "list(:py:class:`opsworks.Stack`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Stack", ServiceName.opsworks),),
    ),
    ":py:class:`iam.MfaDevice`": InternalImport("MfaDevice", ServiceName.iam),
    ":py:class:`IAM.MfaDevice`": InternalImport("MfaDevice", ServiceName.iam),
    "list(:py:class:`s3.Bucket`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Bucket", ServiceName.s3),),
    ),
    "list(:py:class:`sns.PlatformEndpoint`)": AnnotationWrapper(
        parent=List, children=(InternalImport("PlatformEndpoint", ServiceName.sns),),
    ),
    ":py:class:`ec2.Snapshot`": InternalImport("Snapshot", ServiceName.ec2),
    ":py:class:`EC2.Snapshot`": InternalImport("Snapshot", ServiceName.ec2),
    "list(:py:class:`ec2.DhcpOptions`)": AnnotationWrapper(
        parent=List, children=(InternalImport("DhcpOptions", ServiceName.ec2),),
    ),
    "list(:py:class:`ec2.NetworkAcl`)": AnnotationWrapper(
        parent=List, children=(InternalImport("NetworkAcl", ServiceName.ec2),),
    ),
    "list(:py:class:`ec2.KeyPairInfo`)": AnnotationWrapper(
        parent=List, children=(InternalImport("KeyPairInfo", ServiceName.ec2),),
    ),
    "list(:py:class:`cloudformation.StackResourceSummary`)": AnnotationWrapper(
        parent=List,
        children=(InternalImport("StackResourceSummary", ServiceName.cloudformation),),
    ),
    ":py:class:`dynamodb.Table`": InternalImport("Table", ServiceName.dynamodb),
    ":py:class:`DynamoDB.Table`": InternalImport("Table", ServiceName.dynamodb),
    ":py:class:`iam.AccessKeyPair`": InternalImport("AccessKeyPair", ServiceName.iam),
    ":py:class:`IAM.AccessKeyPair`": InternalImport("AccessKeyPair", ServiceName.iam),
    "list(:py:class:`iam.SamlProvider`)": AnnotationWrapper(
        parent=List, children=(InternalImport("SamlProvider", ServiceName.iam),),
    ),
    ":py:class:`glacier.Archive`": InternalImport("Archive", ServiceName.glacier),
    ":py:class:`Glacier.Archive`": InternalImport("Archive", ServiceName.glacier),
    ":py:class:`ec2.NetworkInterface`": InternalImport(
        "NetworkInterface", ServiceName.ec2
    ),
    ":py:class:`EC2.NetworkInterface`": InternalImport(
        "NetworkInterface", ServiceName.ec2
    ),
    "list(:py:class:`iam.AccessKey`)": AnnotationWrapper(
        parent=List, children=(InternalImport("AccessKey", ServiceName.iam),),
    ),
    ":py:class:`sns.Subscription`": InternalImport("Subscription", ServiceName.sns),
    ":py:class:`SNS.Subscription`": InternalImport("Subscription", ServiceName.sns),
    "list(:py:class:`s3.MultipartUploadPart`)": AnnotationWrapper(
        parent=List, children=(InternalImport("MultipartUploadPart", ServiceName.s3),),
    ),
    ":py:class:`iam.ServerCertificate`": InternalImport(
        "ServerCertificate", ServiceName.iam
    ),
    ":py:class:`IAM.ServerCertificate`": InternalImport(
        "ServerCertificate", ServiceName.iam
    ),
    "list(:py:class:`ec2.Tag`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Tag", ServiceName.ec2),),
    ),
    ":py:class:`cloudwatch.Alarm`": InternalImport("Alarm", ServiceName.cloudwatch),
    ":py:class:`CloudWatch.Alarm`": InternalImport("Alarm", ServiceName.cloudwatch),
    ":py:class:`EC2.PlacementGroup`": InternalImport("PlacementGroup", ServiceName.ec2),
    ":py:class:`ec2.PlacementGroup`": InternalImport("PlacementGroup", ServiceName.ec2),
    ":py:class:`EC2.Vpc`": InternalImport("Vpc", ServiceName.ec2),
    ":py:class:`ec2.Vpc`": InternalImport("Vpc", ServiceName.ec2),
    ":py:class:`S3.BucketVersioning`": InternalImport(
        "BucketVersioning", ServiceName.s3
    ),
    ":py:class:`IAM.User`": InternalImport("User", ServiceName.iam),
    ":py:class:`iam.User`": InternalImport("User", ServiceName.iam),
    ":py:class:`sns.Topic`": InternalImport("Topic", ServiceName.sns),
    ":py:class:`SNS.Topic`": InternalImport("Topic", ServiceName.sns),
    ":py:class:`iam.Policy`": InternalImport("Policy", ServiceName.iam),
    ":py:class:`IAM.Policy`": InternalImport("Policy", ServiceName.iam),
    ":py:class:`S3.BucketCors`": InternalImport("BucketCors", ServiceName.s3),
    ":py:class:`OpsWorks.Stack`": InternalImport("Stack", ServiceName.opsworks),
    ":py:class:`CloudFormation.Stack`": InternalImport(
        "Stack", ServiceName.cloudformation
    ),
    ":py:class:`opsworks.Stack`": InternalImport("Stack", ServiceName.opsworks),
    ":py:class:`cloudformation.Stack`": InternalImport(
        "Stack", ServiceName.cloudformation
    ),
    ":py:class:`IAM.SigningCertificate`": InternalImport(
        "SigningCertificate", ServiceName.iam
    ),
    ":py:class:`iam.SigningCertificate`": InternalImport(
        "SigningCertificate", ServiceName.iam
    ),
    ":py:class:`S3.ObjectVersion`": InternalImport("ObjectVersion", ServiceName.s3),
    ":py:class:`S3.BucketPolicy`": InternalImport("BucketPolicy", ServiceName.s3),
    ":py:class:`EC2.RouteTableAssociation`": InternalImport(
        "RouteTableAssociation", ServiceName.ec2
    ),
    ":py:class:`ec2.RouteTableAssociation`": InternalImport(
        "RouteTableAssociation", ServiceName.ec2
    ),
    ":py:class:`IAM.RolePolicy`": InternalImport("RolePolicy", ServiceName.iam),
    ":py:class:`IAM.CurrentUser`": InternalImport("CurrentUser", ServiceName.iam),
    ":py:class:`EC2.InternetGateway`": InternalImport(
        "InternetGateway", ServiceName.ec2
    ),
    ":py:class:`ec2.InternetGateway`": InternalImport(
        "InternetGateway", ServiceName.ec2
    ),
    ":py:class:`sns.PlatformApplication`": InternalImport(
        "PlatformApplication", ServiceName.sns
    ),
    ":py:class:`SNS.PlatformApplication`": InternalImport(
        "PlatformApplication", ServiceName.sns
    ),
    ":py:class:`CloudWatch.Metric`": InternalImport("Metric", ServiceName.cloudwatch),
    ":py:class:`IAM.Group`": InternalImport("Group", ServiceName.iam),
    ":py:class:`OpsWorks.StackSummary`": InternalImport(
        "StackSummary", ServiceName.opsworks
    ),
    ":py:class:`IAM.AssumeRolePolicy`": InternalImport(
        "AssumeRolePolicy", ServiceName.iam
    ),
    ":py:class:`S3.Object`": InternalImport("Object", ServiceName.s3),
    ":py:class:`s3.Object`": InternalImport("Object", ServiceName.s3),
    ":py:class:`CloudFormation.StackResourceSummary`": InternalImport(
        "StackResourceSummary", ServiceName.cloudformation
    ),
    ":py:class:`S3.BucketWebsite`": InternalImport("BucketWebsite", ServiceName.s3),
    ":py:class:`SQS.Queue`": InternalImport("Queue", ServiceName.sqs),
    ":py:class:`sqs.Queue`": InternalImport("Queue", ServiceName.sqs),
    ":py:class:`S3.MultipartUploadPart`": InternalImport(
        "MultipartUploadPart", ServiceName.s3
    ),
    ":py:class:`ec2.KeyPairInfo`": InternalImport("KeyPairInfo", ServiceName.ec2),
    ":py:class:`EC2.KeyPairInfo`": InternalImport("KeyPairInfo", ServiceName.ec2),
    ":py:class:`iam.InstanceProfile`": InternalImport(
        "InstanceProfile", ServiceName.iam
    ),
    ":py:class:`IAM.InstanceProfile`": InternalImport(
        "InstanceProfile", ServiceName.iam
    ),
    ":py:class:`IAM.AccessKey`": InternalImport("AccessKey", ServiceName.iam),
    ":py:class:`IAM.SamlProvider`": InternalImport("SamlProvider", ServiceName.iam),
    ":py:class:`iam.SamlProvider`": InternalImport("SamlProvider", ServiceName.iam),
    ":py:class:`EC2.Tag`": InternalImport("Tag", ServiceName.ec2),
    ":py:class:`S3.BucketLifecycleConfiguration`": InternalImport(
        "BucketLifecycleConfiguration", ServiceName.s3
    ),
    ":py:class:`iam.AccountPasswordPolicy`": InternalImport(
        "AccountPasswordPolicy", ServiceName.iam
    ),
    ":py:class:`IAM.AccountPasswordPolicy`": InternalImport(
        "AccountPasswordPolicy", ServiceName.iam
    ),
    ":py:class:`S3.BucketNotification`": InternalImport(
        "BucketNotification", ServiceName.s3
    ),
    ":py:class:`CloudFormation.StackResource`": InternalImport(
        "StackResource", ServiceName.cloudformation
    ),
    ":py:class:`EC2.Instance`": InternalImport("Instance", ServiceName.ec2),
    ":py:class:`S3.BucketTagging`": InternalImport("BucketTagging", ServiceName.s3),
    ":py:class:`IAM.AccountSummary`": InternalImport("AccountSummary", ServiceName.iam),
    ":py:class:`EC2.Volume`": InternalImport("Volume", ServiceName.ec2),
    ":py:class:`ec2.Volume`": InternalImport("Volume", ServiceName.ec2),
    ":py:class:`SQS.Message`": InternalImport("Message", ServiceName.sqs),
    ":py:class:`ec2.KeyPair`": InternalImport("KeyPair", ServiceName.ec2),
    ":py:class:`S3.BucketAcl`": InternalImport("BucketAcl", ServiceName.s3),
    ":py:class:`S3.BucketRequestPayment`": InternalImport(
        "BucketRequestPayment", ServiceName.s3
    ),
    ":py:class:`IAM.Role`": InternalImport("Role", ServiceName.iam),
    ":py:class:`iam.Role`": InternalImport("Role", ServiceName.iam),
    ":py:class:`IAM.VirtualMfaDevice`": InternalImport(
        "VirtualMfaDevice", ServiceName.iam
    ),
    ":py:class:`iam.VirtualMfaDevice`": InternalImport(
        "VirtualMfaDevice", ServiceName.iam
    ),
    ":py:class:`Glacier.Account`": InternalImport("Account", ServiceName.glacier),
    ":py:class:`S3.BucketLifecycle`": InternalImport("BucketLifecycle", ServiceName.s3),
    ":py:class:`EC2.DhcpOptions`": InternalImport("DhcpOptions", ServiceName.ec2),
    ":py:class:`ec2.DhcpOptions`": InternalImport("DhcpOptions", ServiceName.ec2),
    ":py:class:`S3.BucketLogging`": InternalImport("BucketLogging", ServiceName.s3),
    ":py:class:`Glacier.Notification`": InternalImport(
        "Notification", ServiceName.glacier
    ),
    ":py:class:`EC2.ClassicAddress`": InternalImport("ClassicAddress", ServiceName.ec2),
    ":py:class:`s3.Bucket`": InternalImport("Bucket", ServiceName.s3),
    ":py:class:`S3.Bucket`": InternalImport("Bucket", ServiceName.s3),
    ":py:class:`EC2.VpcAddress`": InternalImport("VpcAddress", ServiceName.ec2),
    ":py:class:`S3.ObjectSummary`": InternalImport("ObjectSummary", ServiceName.s3),
    ":py:class:`EC2.NetworkInterfaceAssociation`": InternalImport(
        "NetworkInterfaceAssociation", ServiceName.ec2
    ),
    ":py:class:`S3.ObjectAcl`": InternalImport("ObjectAcl", ServiceName.s3),
    "list(:py:class:`sns.PlatformApplication`)": AnnotationWrapper(
        parent=List, children=(InternalImport("PlatformApplication", ServiceName.sns),),
    ),
    "list(:py:class:`s3.ObjectSummary`)": AnnotationWrapper(
        parent=List, children=(InternalImport("ObjectSummary", ServiceName.s3),),
    ),
}
