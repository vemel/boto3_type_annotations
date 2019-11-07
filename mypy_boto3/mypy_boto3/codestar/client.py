from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_team_member(
        self,
        projectId: str,
        userArn: str,
        projectRole: str,
        clientRequestToken: Optional[str] = None,
        remoteAccessAllowed: Optional[bool] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_project(
        self,
        name: str,
        id: str,
        description: Optional[str] = None,
        clientRequestToken: Optional[str] = None,
        sourceCode: Optional[List] = None,
        toolchain: Optional[Dict] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_user_profile(
        self,
        userArn: str,
        displayName: str,
        emailAddress: str,
        sshPublicKey: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_project(
        self,
        id: str,
        clientRequestToken: Optional[str] = None,
        deleteStack: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_user_profile(
        self,
        userArn: str,
    ) -> Dict:
        pass


    def describe_project(
        self,
        id: str,
    ) -> Dict:
        pass


    def describe_user_profile(
        self,
        userArn: str,
    ) -> Dict:
        pass


    def disassociate_team_member(
        self,
        projectId: str,
        userArn: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
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


    def list_projects(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_resources(
        self,
        projectId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_project(
        self,
        id: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_team_members(
        self,
        projectId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_user_profiles(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def tag_project(
        self,
        id: str,
        tags: Dict,
    ) -> Dict:
        pass


    def untag_project(
        self,
        id: str,
        tags: List,
    ) -> Dict:
        pass


    def update_project(
        self,
        id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_team_member(
        self,
        projectId: str,
        userArn: str,
        projectRole: Optional[str] = None,
        remoteAccessAllowed: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_user_profile(
        self,
        userArn: str,
        displayName: Optional[str] = None,
        emailAddress: Optional[str] = None,
        sshPublicKey: Optional[str] = None,
    ) -> Dict:
        pass

