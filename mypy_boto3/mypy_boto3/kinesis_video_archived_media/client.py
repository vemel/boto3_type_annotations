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


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_dash_streaming_session_url(
        self,
        StreamName: Optional[str] = None,
        StreamARN: Optional[str] = None,
        PlaybackMode: Optional[str] = None,
        DisplayFragmentTimestamp: Optional[str] = None,
        DisplayFragmentNumber: Optional[str] = None,
        DASHFragmentSelector: Optional[Dict] = None,
        Expires: Optional[int] = None,
        MaxManifestFragmentResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_hls_streaming_session_url(
        self,
        StreamName: Optional[str] = None,
        StreamARN: Optional[str] = None,
        PlaybackMode: Optional[str] = None,
        HLSFragmentSelector: Optional[Dict] = None,
        ContainerFormat: Optional[str] = None,
        DiscontinuityMode: Optional[str] = None,
        DisplayFragmentTimestamp: Optional[str] = None,
        Expires: Optional[int] = None,
        MaxMediaPlaylistFragmentResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_media_for_fragment_list(
        self,
        StreamName: str,
        Fragments: List,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_fragments(
        self,
        StreamName: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        FragmentSelector: Optional[Dict] = None,
    ) -> Dict:
        pass

