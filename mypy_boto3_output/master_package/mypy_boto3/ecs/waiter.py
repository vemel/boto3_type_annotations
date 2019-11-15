try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_ecs.waiter import *
except ImportError:
    raise ImportError("Install boto3-stubs[ecs] to use ecs Waiter annotations")
