# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.managedblockchain.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Managedblockchain](index.md#managedblockchain) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_member](#clientcreate_member)
        - [Client().create_network](#clientcreate_network)
        - [Client().create_node](#clientcreate_node)
        - [Client().create_proposal](#clientcreate_proposal)
        - [Client().delete_member](#clientdelete_member)
        - [Client().delete_node](#clientdelete_node)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_member](#clientget_member)
        - [Client().get_network](#clientget_network)
        - [Client().get_node](#clientget_node)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_proposal](#clientget_proposal)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_invitations](#clientlist_invitations)
        - [Client().list_members](#clientlist_members)
        - [Client().list_networks](#clientlist_networks)
        - [Client().list_nodes](#clientlist_nodes)
        - [Client().list_proposal_votes](#clientlist_proposal_votes)
        - [Client().list_proposals](#clientlist_proposals)
        - [Client().reject_invitation](#clientreject_invitation)
        - [Client().vote_on_proposal](#clientvote_on_proposal)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_member

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L18)

```python
def create_member(
    ClientRequestToken: str,
    InvitationId: str,
    NetworkId: str,
    MemberConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_network

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L28)

```python
def create_network(
    ClientRequestToken: str,
    Name: str,
    Framework: str,
    FrameworkVersion: str,
    VotingPolicy: Dict[str, Any],
    MemberConfiguration: Dict[str, Any],
    Description: str = None,
    FrameworkConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L42)

```python
def create_node(
    ClientRequestToken: str,
    NetworkId: str,
    MemberId: str,
    NodeConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_proposal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L52)

```python
def create_proposal(
    ClientRequestToken: str,
    NetworkId: str,
    MemberId: str,
    Actions: Dict[str, Any],
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().delete_member

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L63)

```python
def delete_member(NetworkId: str, MemberId: str) -> Dict[str, Any]:
```

### Client().delete_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L67)

```python
def delete_node(NetworkId: str, MemberId: str, NodeId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L71)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_member

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L81)

```python
def get_member(NetworkId: str, MemberId: str) -> Dict[str, Any]:
```

### Client().get_network

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L85)

```python
def get_network(NetworkId: str) -> Dict[str, Any]:
```

### Client().get_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L89)

```python
def get_node(NetworkId: str, MemberId: str, NodeId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L93)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_proposal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L97)

```python
def get_proposal(NetworkId: str, ProposalId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L101)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_invitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L105)

```python
def list_invitations(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L111)

```python
def list_members(
    NetworkId: str,
    Name: str = None,
    Status: str = None,
    IsOwned: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_networks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L123)

```python
def list_networks(
    Name: str = None,
    Framework: str = None,
    Status: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_nodes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L134)

```python
def list_nodes(
    NetworkId: str,
    MemberId: str,
    Status: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_proposal_votes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L145)

```python
def list_proposal_votes(
    NetworkId: str,
    ProposalId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_proposals

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L155)

```python
def list_proposals(
    NetworkId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().reject_invitation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L161)

```python
def reject_invitation(InvitationId: str) -> Dict[str, Any]:
```

### Client().vote_on_proposal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/managedblockchain/client.py#L165)

```python
def vote_on_proposal(
    NetworkId: str,
    ProposalId: str,
    VoterMemberId: str,
    Vote: str,
) -> Dict[str, Any]:
```
