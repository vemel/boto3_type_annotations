try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_s3.waiter import *
except ImportError:
    raise ImportError("Install boto3-stubs[s3] to use s3 Waiter annotations")
