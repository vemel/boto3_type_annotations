try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_cloudwatch.service_resource import *
except ImportError:
    raise ImportError(
        "Install boto3-stubs[cloudwatch] to use cloudwatch ServiceResource annotations"
    )
