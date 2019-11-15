try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_glacier.waiter import *
except ImportError:
    raise ImportError("Install boto3-stubs[glacier] to use glacier Waiter annotations")
