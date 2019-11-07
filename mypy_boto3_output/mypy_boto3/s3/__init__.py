"Main interface for s3 service"

from mypy_boto3.s3.client import Client
from mypy_boto3.s3.service_resource import Object
from mypy_boto3.s3.service_resource import ObjectSummary
from mypy_boto3.s3.service_resource import BucketAcl
from mypy_boto3.s3.service_resource import BucketLifecycleConfiguration
from mypy_boto3.s3.service_resource import BucketLogging
from mypy_boto3.s3.service_resource import multipart_uploads
from mypy_boto3.s3.service_resource import MultipartUploadPart
from mypy_boto3.s3.service_resource import Bucket
from mypy_boto3.s3.service_resource import BucketCors
from mypy_boto3.s3.service_resource import BucketNotification
from mypy_boto3.s3.service_resource import MultipartUpload
from mypy_boto3.s3.service_resource import objects
from mypy_boto3.s3.service_resource import BucketVersioning
from mypy_boto3.s3.service_resource import BucketTagging
from mypy_boto3.s3.service_resource import buckets
from mypy_boto3.s3.service_resource import ObjectVersion
from mypy_boto3.s3.service_resource import parts
from mypy_boto3.s3.service_resource import BucketRequestPayment
from mypy_boto3.s3.service_resource import ServiceResource
from mypy_boto3.s3.service_resource import BucketLifecycle
from mypy_boto3.s3.service_resource import BucketWebsite
from mypy_boto3.s3.service_resource import BucketPolicy
from mypy_boto3.s3.service_resource import object_versions
from mypy_boto3.s3.service_resource import ObjectAcl

__all__ = (
    "Client",
    "Object",
    "ObjectSummary",
    "BucketAcl",
    "BucketLifecycleConfiguration",
    "BucketLogging",
    "multipart_uploads",
    "MultipartUploadPart",
    "Bucket",
    "BucketCors",
    "BucketNotification",
    "MultipartUpload",
    "objects",
    "BucketVersioning",
    "BucketTagging",
    "buckets",
    "ObjectVersion",
    "parts",
    "BucketRequestPayment",
    "ServiceResource",
    "BucketLifecycle",
    "BucketWebsite",
    "BucketPolicy",
    "object_versions",
    "ObjectAcl",
)
