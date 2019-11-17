"Main interface for comprehend service"

from mypy_boto3_comprehend.client import Client
from mypy_boto3_comprehend.helpers import (
    boto3_client,
    get_list_document_classification_jobs_paginator,
    get_list_document_classifiers_paginator,
    get_list_dominant_language_detection_jobs_paginator,
    get_list_entities_detection_jobs_paginator,
    get_list_entity_recognizers_paginator,
    get_list_key_phrases_detection_jobs_paginator,
    get_list_sentiment_detection_jobs_paginator,
    get_list_topics_detection_jobs_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_document_classification_jobs_paginator",
    "get_list_document_classifiers_paginator",
    "get_list_dominant_language_detection_jobs_paginator",
    "get_list_entities_detection_jobs_paginator",
    "get_list_entity_recognizers_paginator",
    "get_list_key_phrases_detection_jobs_paginator",
    "get_list_sentiment_detection_jobs_paginator",
    "get_list_topics_detection_jobs_paginator",
)
