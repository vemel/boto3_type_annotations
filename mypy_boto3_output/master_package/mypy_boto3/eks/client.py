try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_eks.client import *
except ImportError:
    raise ImportError("Install boto3-stubs[eks] to use eks Client annotations")