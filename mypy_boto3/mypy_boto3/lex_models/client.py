from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_bot_version(
        self,
        name: str,
        checksum: Optional[str] = None,
    ) -> Dict:
        pass


    def create_intent_version(
        self,
        name: str,
        checksum: Optional[str] = None,
    ) -> Dict:
        pass


    def create_slot_type_version(
        self,
        name: str,
        checksum: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_bot(
        self,
        name: str,
    ):
        pass


    def delete_bot_alias(
        self,
        name: str,
        botName: str,
    ):
        pass


    def delete_bot_channel_association(
        self,
        name: str,
        botName: str,
        botAlias: str,
    ):
        pass


    def delete_bot_version(
        self,
        name: str,
        version: str,
    ):
        pass


    def delete_intent(
        self,
        name: str,
    ):
        pass


    def delete_intent_version(
        self,
        name: str,
        version: str,
    ):
        pass


    def delete_slot_type(
        self,
        name: str,
    ):
        pass


    def delete_slot_type_version(
        self,
        name: str,
        version: str,
    ):
        pass


    def delete_utterances(
        self,
        botName: str,
        userId: str,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_bot(
        self,
        name: str,
        versionOrAlias: str,
    ) -> Dict:
        pass


    def get_bot_alias(
        self,
        name: str,
        botName: str,
    ) -> Dict:
        pass


    def get_bot_aliases(
        self,
        botName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        nameContains: Optional[str] = None,
    ) -> Dict:
        pass


    def get_bot_channel_association(
        self,
        name: str,
        botName: str,
        botAlias: str,
    ) -> Dict:
        pass


    def get_bot_channel_associations(
        self,
        botName: str,
        botAlias: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        nameContains: Optional[str] = None,
    ) -> Dict:
        pass


    def get_bot_versions(
        self,
        name: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_bots(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        nameContains: Optional[str] = None,
    ) -> Dict:
        pass


    def get_builtin_intent(
        self,
        signature: str,
    ) -> Dict:
        pass


    def get_builtin_intents(
        self,
        locale: Optional[str] = None,
        signatureContains: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_builtin_slot_types(
        self,
        locale: Optional[str] = None,
        signatureContains: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_export(
        self,
        name: str,
        version: str,
        resourceType: str,
        exportType: str,
    ) -> Dict:
        pass


    def get_import(
        self,
        importId: str,
    ) -> Dict:
        pass


    def get_intent(
        self,
        name: str,
        version: str,
    ) -> Dict:
        pass


    def get_intent_versions(
        self,
        name: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_intents(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        nameContains: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_slot_type(
        self,
        name: str,
        version: str,
    ) -> Dict:
        pass


    def get_slot_type_versions(
        self,
        name: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_slot_types(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        nameContains: Optional[str] = None,
    ) -> Dict:
        pass


    def get_utterances_view(
        self,
        botName: str,
        botVersions: List,
        statusType: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def put_bot(
        self,
        name: str,
        locale: str,
        childDirected: bool,
        description: Optional[str] = None,
        intents: Optional[List] = None,
        clarificationPrompt: Optional[Dict] = None,
        abortStatement: Optional[Dict] = None,
        idleSessionTTLInSeconds: Optional[int] = None,
        voiceId: Optional[str] = None,
        checksum: Optional[str] = None,
        processBehavior: Optional[str] = None,
        createVersion: Optional[bool] = None,
    ) -> Dict:
        pass


    def put_bot_alias(
        self,
        name: str,
        botVersion: str,
        botName: str,
        description: Optional[str] = None,
        checksum: Optional[str] = None,
    ) -> Dict:
        pass


    def put_intent(
        self,
        name: str,
        description: Optional[str] = None,
        slots: Optional[List] = None,
        sampleUtterances: Optional[List] = None,
        confirmationPrompt: Optional[Dict] = None,
        rejectionStatement: Optional[Dict] = None,
        followUpPrompt: Optional[Dict] = None,
        conclusionStatement: Optional[Dict] = None,
        dialogCodeHook: Optional[Dict] = None,
        fulfillmentActivity: Optional[Dict] = None,
        parentIntentSignature: Optional[str] = None,
        checksum: Optional[str] = None,
        createVersion: Optional[bool] = None,
    ) -> Dict:
        pass


    def put_slot_type(
        self,
        name: str,
        description: Optional[str] = None,
        enumerationValues: Optional[List] = None,
        checksum: Optional[str] = None,
        valueSelectionStrategy: Optional[str] = None,
        createVersion: Optional[bool] = None,
    ) -> Dict:
        pass


    def start_import(
        self,
        payload: bytes,
        resourceType: str,
        mergeStrategy: str,
    ) -> Dict:
        pass

