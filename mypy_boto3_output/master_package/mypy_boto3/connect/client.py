try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_connect.client import *
except ImportError:
    raise ImportError("Install boto3-stubs[connect] to use connect Client annotations")