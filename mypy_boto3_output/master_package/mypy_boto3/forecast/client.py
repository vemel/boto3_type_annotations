try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_forecast.client import *
except ImportError:
    raise ImportError(
        "Install boto3-stubs[forecast] to use forecast Client annotations"
    )