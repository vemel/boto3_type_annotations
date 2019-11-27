# pylint: disable=unused-argument,multiple-statements,super-init-not-called
from typing import Dict, Any, Iterable, List
from mypy_boto3.type_defs import TypedDict

class Tag(TypedDict):
    Key: str
    Value: str

def inject_create_tags(
    event_name: str, class_attributes: Dict[str, Any], **kwargs: Any
) -> None: ...
def create_tags(self: Any, **kwargs: Iterable[Any]) -> List[Tag]: ...
