try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_discovery.client import *
except ImportError:
    raise ImportError(
        "Install boto3-stubs[discovery] to use discovery Client annotations"
    )