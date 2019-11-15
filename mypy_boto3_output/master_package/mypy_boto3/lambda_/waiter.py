try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_lambda.waiter import *
except ImportError:
    raise ImportError("Install boto3-stubs[lambda] to use lambda Waiter annotations")
