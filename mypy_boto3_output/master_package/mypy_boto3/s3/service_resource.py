try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_s3.service_resource import *
except ImportError:
    raise ImportError("Install boto3-stubs[s3] to use s3 ServiceResource annotations")
