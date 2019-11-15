try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_kinesis.waiter import *
except ImportError:
    raise ImportError("Install boto3-stubs[kinesis] to use kinesis Waiter annotations")
