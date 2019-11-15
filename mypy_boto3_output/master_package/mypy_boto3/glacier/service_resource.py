try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_glacier.service_resource import *
except ImportError:
    raise ImportError(
        "Install boto3-stubs[glacier] to use glacier ServiceResource annotations"
    )
