try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_cloudfront.waiter import *
except ImportError:
    raise ImportError(
        "Install boto3-stubs[cloudfront] to use cloudfront Waiter annotations"
    )
