from typing_extensions import TypedDict

class _Tag(TypedDict):
    Key: str

class Tag(_Tag, total=False):
    Value: str
