"Main interface for ses service"

from mypy_boto3_ses.client import Client
from mypy_boto3_ses.helpers import (
    boto3_client,
    get_identity_exists_waiter,
    get_list_configuration_sets_paginator,
    get_list_custom_verification_email_templates_paginator,
    get_list_identities_paginator,
    get_list_receipt_rule_sets_paginator,
    get_list_templates_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_configuration_sets_paginator",
    "get_list_custom_verification_email_templates_paginator",
    "get_list_identities_paginator",
    "get_list_receipt_rule_sets_paginator",
    "get_list_templates_paginator",
    "get_identity_exists_waiter",
)
