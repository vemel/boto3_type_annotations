try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_sagemaker.waiter import *
except ImportError:
    raise ImportError(
        "Install boto3-stubs[sagemaker] to use sagemaker Waiter annotations"
    )
