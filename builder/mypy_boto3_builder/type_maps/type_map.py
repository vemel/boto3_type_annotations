"""
String to type annotation map that find type annotation by argument name and type.
"""
from datetime import datetime
from typing import Callable, IO, List, Dict, Union

from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_class import TypeClass


TYPE_MAP: Dict[str, FakeAnnotation] = {
    "bytes": TypeClass(bytes),
    "blob": TypeClass(bytes),
    "boolean": TypeClass(bool),
    "function": TypeSubscript(Callable, [TypeConstant(...), TypeAnnotation.Any()]),
    "botocore or boto3 Client": ExternalImport(
        source=ImportString("botocore", "client"), name="BaseClient"
    ),
    "datetime": TypeClass(datetime),
    "timestamp": TypeClass(datetime),
    "dict": TypeSubscript(Dict, [TypeClass(str), TypeAnnotation.Any()]),
    "structure": TypeSubscript(Dict, [TypeClass(str), TypeAnnotation.Any()]),
    "map": TypeSubscript(Dict, [TypeClass(str), TypeAnnotation.Any()]),
    "float": TypeClass(float),
    "double": TypeClass(float),
    "int": TypeClass(int),
    "integer": TypeClass(int),
    "long": TypeClass(int),
    "a file-like object": TypeSubscript(IO, [TypeAnnotation.Any()]),
    "seekable file-like object": TypeSubscript(
        IO, [TypeAnnotation.Any()]
    ),
    "list": TypeSubscript(List, [TypeAnnotation.Any()]),
    "L{botocore.paginate.Paginator}": ExternalImport(
        source=ImportString("botocore", "paginate"), name="Paginator"
    ),
    ":py:class:`ResourceCollection`": ExternalImport(
        source=ImportString("boto3", "resources", "collection"), name="ResourceCollection"
    ),
    "JSON serializable": TypeClass(str),
    "string": TypeClass(str),
    "str": TypeClass(str),
    "boto3.s3.transfer.TransferConfig": ExternalImport(
        source=ImportString("boto3", "s3", "transfer"), name="TransferConfig"
    ),
    "botocore.waiter.Waiter": ExternalImport(source=ImportString("botocore", "waiter"), name="Waiter"),
    "bytes or seekable file-like object": TypeSubscript(
        Union, [TypeClass(bytes), TypeAnnotation(IO)]
    ),
    "str or dict": TypeSubscript(
        Union, [TypeClass(str), TypeAnnotation(Dict)]
    ),
    "list(string)": TypeSubscript(List, [TypeClass(str)]),
    "list of str": TypeSubscript(List, [TypeClass(str)]),
    "None": TypeConstant(None),
    ":py:class:`ec2.NetworkAcl`": InternalImport("NetworkAcl", ServiceName.ec2),
    ":py:class:`EC2.NetworkAcl`": InternalImport("NetworkAcl", ServiceName.ec2),
    "list(:py:class:`ec2.InternetGateway`)": TypeSubscript(
        List, [InternalImport("InternetGateway", ServiceName.ec2)]
    ),
    ":py:class:`iam.UserPolicy`": InternalImport("UserPolicy", ServiceName.iam),
    ":py:class:`IAM.UserPolicy`": InternalImport("UserPolicy", ServiceName.iam),
    "list(:py:class:`iam.VirtualMfaDevice`)": TypeSubscript(
        List, [InternalImport("VirtualMfaDevice", ServiceName.iam)]
    ),
    "list(:py:class:`ec2.Image`)": TypeSubscript(
        List, [InternalImport("Image", ServiceName.ec2)]
    ),
    "list(:py:class:`cloudwatch.Alarm`)": TypeSubscript(
        List, [InternalImport("Alarm", ServiceName.cloudwatch)]
    ),
    "list(:py:class:`opsworks.Layer`)": TypeSubscript(
        List, [InternalImport("Layer", ServiceName.opsworks)]
    ),
    ":py:class:`iam.GroupPolicy`": InternalImport("GroupPolicy", ServiceName.iam),
    ":py:class:`IAM.GroupPolicy`": InternalImport("GroupPolicy", ServiceName.iam),
    "list(:py:class:`iam.SigningCertificate`)": TypeSubscript(
        List, [InternalImport("SigningCertificate", ServiceName.iam)]
    ),
    "list(:py:class:`ec2.Volume`)": TypeSubscript(
        List, [InternalImport("Volume", ServiceName.ec2)]
    ),
    "list(:py:class:`ec2.VpcPeeringConnection`)": TypeSubscript(
        List, [InternalImport("VpcPeeringConnection", ServiceName.ec2)]
    ),
    ":py:class:`ec2.Subnet`": InternalImport("Subnet", ServiceName.ec2),
    ":py:class:`EC2.Subnet`": InternalImport("Subnet", ServiceName.ec2),
    "list(:py:class:`iam.ServerCertificate`)": TypeSubscript(
        List, [InternalImport("ServerCertificate", ServiceName.iam)]
    ),
    "list(:py:class:`ec2.VpcAddress`)": TypeSubscript(
        List, [InternalImport("VpcAddress", ServiceName.ec2)]
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
    "list(:py:class:`ec2.Subnet`)": TypeSubscript(
        List, [InternalImport("Subnet", ServiceName.ec2)]
    ),
    ":py:class:`opsworks.Layer`": InternalImport("Layer", ServiceName.opsworks),
    ":py:class:`OpsWorks.Layer`": InternalImport("Layer", ServiceName.opsworks),
    "list(:py:class:`iam.MfaDevice`)": TypeSubscript(
        List, [InternalImport("MfaDevice", ServiceName.iam)]
    ),
    "list(:py:class:`glacier.Job`)": TypeSubscript(
        List, [InternalImport("Job", ServiceName.glacier)]
    ),
    "list(:py:class:`iam.RolePolicy`)": TypeSubscript(
        List, [InternalImport("RolePolicy", ServiceName.iam)]
    ),
    "list(:py:class:`iam.InstanceProfile`)": TypeSubscript(
        List, [InternalImport("InstanceProfile", ServiceName.iam)]
    ),
    "list(:py:class:`ec2.Instance`)": TypeSubscript(
        List, [InternalImport("Instance", ServiceName.ec2)]
    ),
    ":py:class:`glacier.Vault`": InternalImport("Vault", ServiceName.glacier),
    ":py:class:`Glacier.Vault`": InternalImport("Vault", ServiceName.glacier),
    ":py:class:`ec2.SecurityGroup`": InternalImport("SecurityGroup", ServiceName.ec2),
    ":py:class:`EC2.SecurityGroup`": InternalImport("SecurityGroup", ServiceName.ec2),
    ":py:class:`ec2.RouteTable`": InternalImport("RouteTable", ServiceName.ec2),
    ":py:class:`EC2.RouteTable`": InternalImport("RouteTable", ServiceName.ec2),
    "list(:py:class:`dynamodb.Table`)": TypeSubscript(
        List, [InternalImport("Table", ServiceName.dynamodb)]
    ),
    "list(:py:class:`ec2.Snapshot`)": TypeSubscript(
        List, [InternalImport("Snapshot", ServiceName.ec2)]
    ),
    "list(:py:class:`sqs.Message`)": TypeSubscript(
        List, [InternalImport("Message", ServiceName.sqs)]
    ),
    "list(:py:class:`iam.Role`)": TypeSubscript(
        List, [InternalImport("Role", ServiceName.iam)]
    ),
    ":py:class:`glacier.Job`": InternalImport("Job", ServiceName.glacier),
    ":py:class:`Glacier.Job`": InternalImport("Job", ServiceName.glacier),
    "list(:py:class:`cloudwatch.Metric`)": TypeSubscript(
        List, [InternalImport("Metric", ServiceName.cloudwatch)]
    ),
    "list(:py:class:`iam.Policy`)": TypeSubscript(
        List, [InternalImport("Policy", ServiceName.iam)]
    ),
    "list(:py:class:`ec2.ClassicAddress`)": TypeSubscript(
        List, [InternalImport("ClassicAddress", ServiceName.ec2)]
    ),
    "list(:py:class:`iam.User`)": TypeSubscript(
        List, [InternalImport("User", ServiceName.iam)]
    ),
    "list(:py:class:`iam.GroupPolicy`)": TypeSubscript(
        List, [InternalImport("GroupPolicy", ServiceName.iam)]
    ),
    "list(:py:class:`iam.PolicyVersion`)": TypeSubscript(
        List, [InternalImport("PolicyVersion", ServiceName.iam)]
    ),
    "list(:py:class:`sns.Topic`)": TypeSubscript(
        List, [InternalImport("Topic", ServiceName.sns)]
    ),
    ":py:class:`iam.LoginProfile`": InternalImport("LoginProfile", ServiceName.iam),
    ":py:class:`IAM.LoginProfile`": InternalImport("LoginProfile", ServiceName.iam),
    "list(:py:class:`iam.UserPolicy`)": TypeSubscript(
        List, [InternalImport("UserPolicy", ServiceName.iam)]
    ),
    "list(:py:class:`cloudformation.Event`)": TypeSubscript(
        List, [InternalImport("Event", ServiceName.cloudformation)]
    ),
    ":py:class:`cloudformation.Event`": InternalImport(
        "Event", ServiceName.cloudformation
    ),
    ":py:class:`CloudFormation.Event`": InternalImport(
        "Event", ServiceName.cloudformation
    ),
    "list(:py:class:`s3.MultipartUpload`)": TypeSubscript(
        List, [InternalImport("MultipartUpload", ServiceName.s3)]
    ),
    "list(:py:class:`glacier.MultipartUpload`)": TypeSubscript(
        List, [InternalImport("MultipartUpload", ServiceName.glacier)]
    ),
    "list(:py:class:`sns.Subscription`)": TypeSubscript(
        List, [InternalImport("Subscription", ServiceName.sns)]
    ),
    ":py:class:`iam.PolicyVersion`": InternalImport("PolicyVersion", ServiceName.iam),
    ":py:class:`IAM.PolicyVersion`": InternalImport("PolicyVersion", ServiceName.iam),
    "list(:py:class:`~boto3.resources.base.ServiceResource`)": TypeSubscript(
        List,
        [
            ExternalImport(
                ImportString("boto3", "resources", "base"),
                name="ServiceResource",
                alias="Boto3ServiceResource",
            )
        ],
    ),
    "list(:py:class:`ec2.NetworkInterface`)": TypeSubscript(
        List, [InternalImport("NetworkInterface", ServiceName.ec2)]
    ),
    "list(:py:class:`s3.ObjectVersion`)": TypeSubscript(
        List, [InternalImport("ObjectVersion", ServiceName.s3)]
    ),
    "list(:py:class:`ec2.SecurityGroup`)": TypeSubscript(
        List, [InternalImport("SecurityGroup", ServiceName.ec2)]
    ),
    "list(:py:class:`sqs.Queue`)": TypeSubscript(
        List, [InternalImport("Queue", ServiceName.sqs)]
    ),
    "list(:py:class:`ec2.PlacementGroup`)": TypeSubscript(
        List, [InternalImport("PlacementGroup", ServiceName.ec2)]
    ),
    "list(:py:class:`ec2.Vpc`)": TypeSubscript(
        List, [InternalImport("Vpc", ServiceName.ec2)]
    ),
    "list(:py:class:`ec2.RouteTable`)": TypeSubscript(
        List, [InternalImport("RouteTable", ServiceName.ec2)]
    ),
    "list(:py:class:`glacier.Vault`)": TypeSubscript(
        List, [InternalImport("Vault", ServiceName.glacier)]
    ),
    "list(:py:class:`iam.Group`)": TypeSubscript(
        List, [InternalImport("Group", ServiceName.iam)]
    ),
    ":py:class:`iam.Group`": TypeSubscript(
        List, [InternalImport("Group", ServiceName.iam)]
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
    "list(:py:class:`cloudformation.Stack`)": TypeSubscript(
        List, [InternalImport("Stack", ServiceName.cloudformation)]
    ),
    "list(:py:class:`opsworks.Stack`)": TypeSubscript(
        List, [InternalImport("Stack", ServiceName.opsworks)]
    ),
    ":py:class:`iam.MfaDevice`": InternalImport("MfaDevice", ServiceName.iam),
    ":py:class:`IAM.MfaDevice`": InternalImport("MfaDevice", ServiceName.iam),
    "list(:py:class:`s3.Bucket`)": TypeSubscript(
        List, [InternalImport("Bucket", ServiceName.s3)]
    ),
    "list(:py:class:`sns.PlatformEndpoint`)": TypeSubscript(
        List, [InternalImport("PlatformEndpoint", ServiceName.sns)]
    ),
    ":py:class:`ec2.Snapshot`": InternalImport("Snapshot", ServiceName.ec2),
    ":py:class:`EC2.Snapshot`": InternalImport("Snapshot", ServiceName.ec2),
    "list(:py:class:`ec2.DhcpOptions`)": TypeSubscript(
        List, [InternalImport("DhcpOptions", ServiceName.ec2)]
    ),
    "list(:py:class:`ec2.NetworkAcl`)": TypeSubscript(
        List, [InternalImport("NetworkAcl", ServiceName.ec2)]
    ),
    "list(:py:class:`ec2.KeyPairInfo`)": TypeSubscript(
        List, [InternalImport("KeyPairInfo", ServiceName.ec2)]
    ),
    "list(:py:class:`cloudformation.StackResourceSummary`)": TypeSubscript(
        List,
        [InternalImport("StackResourceSummary", ServiceName.cloudformation)],
    ),
    ":py:class:`dynamodb.Table`": InternalImport("Table", ServiceName.dynamodb),
    ":py:class:`DynamoDB.Table`": InternalImport("Table", ServiceName.dynamodb),
    ":py:class:`iam.AccessKeyPair`": InternalImport("AccessKeyPair", ServiceName.iam),
    ":py:class:`IAM.AccessKeyPair`": InternalImport("AccessKeyPair", ServiceName.iam),
    "list(:py:class:`iam.SamlProvider`)": TypeSubscript(
        List, [InternalImport("SamlProvider", ServiceName.iam)]
    ),
    ":py:class:`glacier.Archive`": InternalImport("Archive", ServiceName.glacier),
    ":py:class:`Glacier.Archive`": InternalImport("Archive", ServiceName.glacier),
    ":py:class:`ec2.NetworkInterface`": InternalImport(
        "NetworkInterface", ServiceName.ec2
    ),
    ":py:class:`EC2.NetworkInterface`": InternalImport(
        "NetworkInterface", ServiceName.ec2
    ),
    "list(:py:class:`iam.AccessKey`)": TypeSubscript(
        List, [InternalImport("AccessKey", ServiceName.iam)]
    ),
    ":py:class:`sns.Subscription`": InternalImport("Subscription", ServiceName.sns),
    ":py:class:`SNS.Subscription`": InternalImport("Subscription", ServiceName.sns),
    "list(:py:class:`s3.MultipartUploadPart`)": TypeSubscript(
        List, [InternalImport("MultipartUploadPart", ServiceName.s3)]
    ),
    ":py:class:`iam.ServerCertificate`": InternalImport(
        "ServerCertificate", ServiceName.iam
    ),
    ":py:class:`IAM.ServerCertificate`": InternalImport(
        "ServerCertificate", ServiceName.iam
    ),
    "list(:py:class:`ec2.Tag`)": TypeSubscript(
        List, [InternalImport("Tag", ServiceName.ec2)]
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
    "list(:py:class:`sns.PlatformApplication`)": TypeSubscript(
        List, [InternalImport("PlatformApplication", ServiceName.sns)]
    ),
    "list(:py:class:`s3.ObjectSummary`)": TypeSubscript(
        List, [InternalImport("ObjectSummary", ServiceName.s3)]
    ),
    "botocore.waiter.SingleWaiterConfig": ExternalImport(
        source=ImportString("botocore", "waiter"), name="SingleWaiterConfig"
    ),
    "callable": TypeSubscript(
        Callable, [TypeConstant(...), TypeAnnotation.Any()]
    ),
}
