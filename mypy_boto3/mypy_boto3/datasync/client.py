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


    def cancel_task_execution(
        self,
        TaskExecutionArn: str,
    ) -> Dict:
        pass


    def create_agent(
        self,
        ActivationKey: str,
        AgentName: Optional[str] = None,
        Tags: Optional[List] = None,
        VpcEndpointId: Optional[str] = None,
        SubnetArns: Optional[List] = None,
        SecurityGroupArns: Optional[List] = None,
    ) -> Dict:
        pass


    def create_location_efs(
        self,
        EfsFilesystemArn: str,
        Ec2Config: Dict,
        Subdirectory: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_location_nfs(
        self,
        Subdirectory: str,
        ServerHostname: str,
        OnPremConfig: Dict,
        MountOptions: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_location_s3(
        self,
        S3BucketArn: str,
        S3Config: Dict,
        Subdirectory: Optional[str] = None,
        S3StorageClass: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_location_smb(
        self,
        Subdirectory: str,
        ServerHostname: str,
        User: str,
        Password: str,
        AgentArns: List,
        Domain: Optional[str] = None,
        MountOptions: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_task(
        self,
        SourceLocationArn: str,
        DestinationLocationArn: str,
        CloudWatchLogGroupArn: Optional[str] = None,
        Name: Optional[str] = None,
        Options: Optional[Dict] = None,
        Excludes: Optional[List] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_agent(
        self,
        AgentArn: str,
    ) -> Dict:
        pass


    def delete_location(
        self,
        LocationArn: str,
    ) -> Dict:
        pass


    def delete_task(
        self,
        TaskArn: str,
    ) -> Dict:
        pass


    def describe_agent(
        self,
        AgentArn: str,
    ) -> Dict:
        pass


    def describe_location_efs(
        self,
        LocationArn: str,
    ) -> Dict:
        pass


    def describe_location_nfs(
        self,
        LocationArn: str,
    ) -> Dict:
        pass


    def describe_location_s3(
        self,
        LocationArn: str,
    ) -> Dict:
        pass


    def describe_location_smb(
        self,
        LocationArn: str,
    ) -> Dict:
        pass


    def describe_task(
        self,
        TaskArn: str,
    ) -> Dict:
        pass


    def describe_task_execution(
        self,
        TaskExecutionArn: str,
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


    def list_agents(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_locations(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_task_executions(
        self,
        TaskArn: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tasks(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def start_task_execution(
        self,
        TaskArn: str,
        OverrideOptions: Optional[Dict] = None,
        Includes: Optional[List] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        Keys: List,
    ) -> Dict:
        pass


    def update_agent(
        self,
        AgentArn: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_task(
        self,
        TaskArn: str,
        Options: Optional[Dict] = None,
        Excludes: Optional[List] = None,
        Name: Optional[str] = None,
        CloudWatchLogGroupArn: Optional[str] = None,
    ) -> Dict:
        pass

