try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_cloudformation.waiter import *
except ImportError:
    raise ImportError(
        "Install boto3-stubs[cloudformation] to use cloudformation Waiter annotations"
    )
