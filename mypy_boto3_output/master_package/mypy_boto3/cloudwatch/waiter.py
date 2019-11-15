try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_cloudwatch.waiter import *
except ImportError:
    raise ImportError(
        "Install boto3-stubs[cloudwatch] to use cloudwatch Waiter annotations"
    )
