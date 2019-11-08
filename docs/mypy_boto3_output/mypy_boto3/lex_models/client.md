# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.lex_models.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Lex Models](index.md#lex-models) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_bot_version](#clientcreate_bot_version)
        - [Client().create_intent_version](#clientcreate_intent_version)
        - [Client().create_slot_type_version](#clientcreate_slot_type_version)
        - [Client().delete_bot](#clientdelete_bot)
        - [Client().delete_bot_alias](#clientdelete_bot_alias)
        - [Client().delete_bot_channel_association](#clientdelete_bot_channel_association)
        - [Client().delete_bot_version](#clientdelete_bot_version)
        - [Client().delete_intent](#clientdelete_intent)
        - [Client().delete_intent_version](#clientdelete_intent_version)
        - [Client().delete_slot_type](#clientdelete_slot_type)
        - [Client().delete_slot_type_version](#clientdelete_slot_type_version)
        - [Client().delete_utterances](#clientdelete_utterances)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_bot](#clientget_bot)
        - [Client().get_bot_alias](#clientget_bot_alias)
        - [Client().get_bot_aliases](#clientget_bot_aliases)
        - [Client().get_bot_channel_association](#clientget_bot_channel_association)
        - [Client().get_bot_channel_associations](#clientget_bot_channel_associations)
        - [Client().get_bot_versions](#clientget_bot_versions)
        - [Client().get_bots](#clientget_bots)
        - [Client().get_builtin_intent](#clientget_builtin_intent)
        - [Client().get_builtin_intents](#clientget_builtin_intents)
        - [Client().get_builtin_slot_types](#clientget_builtin_slot_types)
        - [Client().get_export](#clientget_export)
        - [Client().get_import](#clientget_import)
        - [Client().get_intent](#clientget_intent)
        - [Client().get_intent_versions](#clientget_intent_versions)
        - [Client().get_intents](#clientget_intents)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_slot_type](#clientget_slot_type)
        - [Client().get_slot_type_versions](#clientget_slot_type_versions)
        - [Client().get_slot_types](#clientget_slot_types)
        - [Client().get_utterances_view](#clientget_utterances_view)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().put_bot](#clientput_bot)
        - [Client().put_bot_alias](#clientput_bot_alias)
        - [Client().put_intent](#clientput_intent)
        - [Client().put_slot_type](#clientput_slot_type)
        - [Client().start_import](#clientstart_import)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_bot_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L19)

```python
def create_bot_version(name: str, checksum: str = None) -> Dict[str, Any]:
```

### Client().create_intent_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L23)

```python
def create_intent_version(name: str, checksum: str = None) -> Dict[str, Any]:
```

### Client().create_slot_type_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L27)

```python
def create_slot_type_version(
    name: str,
    checksum: str = None,
) -> Dict[str, Any]:
```

### Client().delete_bot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L33)

```python
def delete_bot(name: str) -> None:
```

### Client().delete_bot_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L37)

```python
def delete_bot_alias(name: str, botName: str) -> None:
```

### Client().delete_bot_channel_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L41)

```python
def delete_bot_channel_association(
    name: str,
    botName: str,
    botAlias: str,
) -> None:
```

### Client().delete_bot_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L47)

```python
def delete_bot_version(name: str, version: str) -> None:
```

### Client().delete_intent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L51)

```python
def delete_intent(name: str) -> None:
```

### Client().delete_intent_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L55)

```python
def delete_intent_version(name: str, version: str) -> None:
```

### Client().delete_slot_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L59)

```python
def delete_slot_type(name: str) -> None:
```

### Client().delete_slot_type_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L63)

```python
def delete_slot_type_version(name: str, version: str) -> None:
```

### Client().delete_utterances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L67)

```python
def delete_utterances(botName: str, userId: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L71)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_bot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L81)

```python
def get_bot(name: str, versionOrAlias: str) -> Dict[str, Any]:
```

### Client().get_bot_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L85)

```python
def get_bot_alias(name: str, botName: str) -> Dict[str, Any]:
```

### Client().get_bot_aliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L89)

```python
def get_bot_aliases(
    botName: str,
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None,
) -> Dict[str, Any]:
```

### Client().get_bot_channel_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L99)

```python
def get_bot_channel_association(
    name: str,
    botName: str,
    botAlias: str,
) -> Dict[str, Any]:
```

### Client().get_bot_channel_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L105)

```python
def get_bot_channel_associations(
    botName: str,
    botAlias: str,
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None,
) -> Dict[str, Any]:
```

### Client().get_bot_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L116)

```python
def get_bot_versions(
    name: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_bots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L122)

```python
def get_bots(
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None,
) -> Dict[str, Any]:
```

### Client().get_builtin_intent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L128)

```python
def get_builtin_intent(signature: str) -> Dict[str, Any]:
```

### Client().get_builtin_intents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L132)

```python
def get_builtin_intents(
    locale: str = None,
    signatureContains: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_builtin_slot_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L142)

```python
def get_builtin_slot_types(
    locale: str = None,
    signatureContains: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_export

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L152)

```python
def get_export(
    name: str,
    version: str,
    resourceType: str,
    exportType: str,
) -> Dict[str, Any]:
```

### Client().get_import

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L158)

```python
def get_import(importId: str) -> Dict[str, Any]:
```

### Client().get_intent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L162)

```python
def get_intent(name: str, version: str) -> Dict[str, Any]:
```

### Client().get_intent_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L166)

```python
def get_intent_versions(
    name: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_intents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L172)

```python
def get_intents(
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L178)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_slot_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L182)

```python
def get_slot_type(name: str, version: str) -> Dict[str, Any]:
```

### Client().get_slot_type_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L186)

```python
def get_slot_type_versions(
    name: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_slot_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L192)

```python
def get_slot_types(
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None,
) -> Dict[str, Any]:
```

### Client().get_utterances_view

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L198)

```python
def get_utterances_view(
    botName: str,
    botVersions: List[Any],
    statusType: str,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L204)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().put_bot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L208)

```python
def put_bot(
    name: str,
    locale: str,
    childDirected: bool,
    description: str = None,
    intents: List[Any] = None,
    clarificationPrompt: Dict[str, Any] = None,
    abortStatement: Dict[str, Any] = None,
    idleSessionTTLInSeconds: int = None,
    voiceId: str = None,
    checksum: str = None,
    processBehavior: str = None,
    createVersion: bool = None,
) -> Dict[str, Any]:
```

### Client().put_bot_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L226)

```python
def put_bot_alias(
    name: str,
    botVersion: str,
    botName: str,
    description: str = None,
    checksum: str = None,
) -> Dict[str, Any]:
```

### Client().put_intent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L237)

```python
def put_intent(
    name: str,
    description: str = None,
    slots: List[Any] = None,
    sampleUtterances: List[Any] = None,
    confirmationPrompt: Dict[str, Any] = None,
    rejectionStatement: Dict[str, Any] = None,
    followUpPrompt: Dict[str, Any] = None,
    conclusionStatement: Dict[str, Any] = None,
    dialogCodeHook: Dict[str, Any] = None,
    fulfillmentActivity: Dict[str, Any] = None,
    parentIntentSignature: str = None,
    checksum: str = None,
    createVersion: bool = None,
) -> Dict[str, Any]:
```

### Client().put_slot_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L256)

```python
def put_slot_type(
    name: str,
    description: str = None,
    enumerationValues: List[Any] = None,
    checksum: str = None,
    valueSelectionStrategy: str = None,
    createVersion: bool = None,
) -> Dict[str, Any]:
```

### Client().start_import

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/client.py#L268)

```python
def start_import(
    payload: bytes,
    resourceType: str,
    mergeStrategy: str,
) -> Dict[str, Any]:
```
