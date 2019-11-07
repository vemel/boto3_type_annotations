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


    def create_api_key(
        self,
        apiId: str,
        description: Optional[str] = None,
        expires: Optional[int] = None,
    ) -> Dict:
        pass


    def create_data_source(
        self,
        apiId: str,
        name: str,
        type: str,
        description: Optional[str] = None,
        serviceRoleArn: Optional[str] = None,
        dynamodbConfig: Optional[Dict] = None,
        lambdaConfig: Optional[Dict] = None,
        elasticsearchConfig: Optional[Dict] = None,
        httpConfig: Optional[Dict] = None,
        relationalDatabaseConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_function(
        self,
        apiId: str,
        name: str,
        dataSourceName: str,
        requestMappingTemplate: str,
        functionVersion: str,
        description: Optional[str] = None,
        responseMappingTemplate: Optional[str] = None,
    ) -> Dict:
        pass


    def create_graphql_api(
        self,
        name: str,
        authenticationType: str,
        logConfig: Optional[Dict] = None,
        userPoolConfig: Optional[Dict] = None,
        openIDConnectConfig: Optional[Dict] = None,
        tags: Optional[Dict] = None,
        additionalAuthenticationProviders: Optional[List] = None,
    ) -> Dict:
        pass


    def create_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
        requestMappingTemplate: str,
        dataSourceName: Optional[str] = None,
        responseMappingTemplate: Optional[str] = None,
        kind: Optional[str] = None,
        pipelineConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_type(
        self,
        apiId: str,
        definition: str,
        format: str,
    ) -> Dict:
        pass


    def delete_api_key(
        self,
        apiId: str,
        id: str,
    ) -> Dict:
        pass


    def delete_data_source(
        self,
        apiId: str,
        name: str,
    ) -> Dict:
        pass


    def delete_function(
        self,
        apiId: str,
        functionId: str,
    ) -> Dict:
        pass


    def delete_graphql_api(
        self,
        apiId: str,
    ) -> Dict:
        pass


    def delete_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
    ) -> Dict:
        pass


    def delete_type(
        self,
        apiId: str,
        typeName: str,
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


    def get_data_source(
        self,
        apiId: str,
        name: str,
    ) -> Dict:
        pass


    def get_function(
        self,
        apiId: str,
        functionId: str,
    ) -> Dict:
        pass


    def get_graphql_api(
        self,
        apiId: str,
    ) -> Dict:
        pass


    def get_introspection_schema(
        self,
        apiId: str,
        format: str,
        includeDirectives: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
    ) -> Dict:
        pass


    def get_schema_creation_status(
        self,
        apiId: str,
    ) -> Dict:
        pass


    def get_type(
        self,
        apiId: str,
        typeName: str,
        format: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_api_keys(
        self,
        apiId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_data_sources(
        self,
        apiId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_functions(
        self,
        apiId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_graphql_apis(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_resolvers(
        self,
        apiId: str,
        typeName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_resolvers_by_function(
        self,
        apiId: str,
        functionId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def list_types(
        self,
        apiId: str,
        format: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def start_schema_creation(
        self,
        apiId: str,
        definition: bytes,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_api_key(
        self,
        apiId: str,
        id: str,
        description: Optional[str] = None,
        expires: Optional[int] = None,
    ) -> Dict:
        pass


    def update_data_source(
        self,
        apiId: str,
        name: str,
        type: str,
        description: Optional[str] = None,
        serviceRoleArn: Optional[str] = None,
        dynamodbConfig: Optional[Dict] = None,
        lambdaConfig: Optional[Dict] = None,
        elasticsearchConfig: Optional[Dict] = None,
        httpConfig: Optional[Dict] = None,
        relationalDatabaseConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_function(
        self,
        apiId: str,
        name: str,
        functionId: str,
        dataSourceName: str,
        requestMappingTemplate: str,
        functionVersion: str,
        description: Optional[str] = None,
        responseMappingTemplate: Optional[str] = None,
    ) -> Dict:
        pass


    def update_graphql_api(
        self,
        apiId: str,
        name: str,
        logConfig: Optional[Dict] = None,
        authenticationType: Optional[str] = None,
        userPoolConfig: Optional[Dict] = None,
        openIDConnectConfig: Optional[Dict] = None,
        additionalAuthenticationProviders: Optional[List] = None,
    ) -> Dict:
        pass


    def update_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
        requestMappingTemplate: str,
        dataSourceName: Optional[str] = None,
        responseMappingTemplate: Optional[str] = None,
        kind: Optional[str] = None,
        pipelineConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_type(
        self,
        apiId: str,
        typeName: str,
        format: str,
        definition: Optional[str] = None,
    ) -> Dict:
        pass

