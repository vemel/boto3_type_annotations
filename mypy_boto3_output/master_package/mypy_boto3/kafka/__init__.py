try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_kafka import *
except ImportError:
    raise ImportError("Install boto3-stubs[kafka] to use kafka annotations")
