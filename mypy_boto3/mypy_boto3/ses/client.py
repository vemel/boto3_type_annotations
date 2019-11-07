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


    def clone_receipt_rule_set(
        self,
        RuleSetName: str,
        OriginalRuleSetName: str,
    ) -> Dict:
        pass


    def create_configuration_set(
        self,
        ConfigurationSet: Dict,
    ) -> Dict:
        pass


    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: Dict,
    ) -> Dict:
        pass


    def create_configuration_set_tracking_options(
        self,
        ConfigurationSetName: str,
        TrackingOptions: Dict,
    ) -> Dict:
        pass


    def create_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ):
        pass


    def create_receipt_filter(
        self,
        Filter: Dict,
    ) -> Dict:
        pass


    def create_receipt_rule(
        self,
        RuleSetName: str,
        Rule: Dict,
        After: Optional[str] = None,
    ) -> Dict:
        pass


    def create_receipt_rule_set(
        self,
        RuleSetName: str,
    ) -> Dict:
        pass


    def create_template(
        self,
        Template: Dict,
    ) -> Dict:
        pass


    def delete_configuration_set(
        self,
        ConfigurationSetName: str,
    ) -> Dict:
        pass


    def delete_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
    ) -> Dict:
        pass


    def delete_configuration_set_tracking_options(
        self,
        ConfigurationSetName: str,
    ) -> Dict:
        pass


    def delete_custom_verification_email_template(
        self,
        TemplateName: str,
    ):
        pass


    def delete_identity(
        self,
        Identity: str,
    ) -> Dict:
        pass


    def delete_identity_policy(
        self,
        Identity: str,
        PolicyName: str,
    ) -> Dict:
        pass


    def delete_receipt_filter(
        self,
        FilterName: str,
    ) -> Dict:
        pass


    def delete_receipt_rule(
        self,
        RuleSetName: str,
        RuleName: str,
    ) -> Dict:
        pass


    def delete_receipt_rule_set(
        self,
        RuleSetName: str,
    ) -> Dict:
        pass


    def delete_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def delete_verified_email_address(
        self,
        EmailAddress: str,
    ):
        pass


    def describe_active_receipt_rule_set(
        self,
    ) -> Dict:
        pass


    def describe_configuration_set(
        self,
        ConfigurationSetName: str,
        ConfigurationSetAttributeNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_receipt_rule(
        self,
        RuleSetName: str,
        RuleName: str,
    ) -> Dict:
        pass


    def describe_receipt_rule_set(
        self,
        RuleSetName: str,
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


    def get_account_sending_enabled(
        self,
    ) -> Dict:
        pass


    def get_custom_verification_email_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def get_identity_dkim_attributes(
        self,
        Identities: List,
    ) -> Dict:
        pass


    def get_identity_mail_from_domain_attributes(
        self,
        Identities: List,
    ) -> Dict:
        pass


    def get_identity_notification_attributes(
        self,
        Identities: List,
    ) -> Dict:
        pass


    def get_identity_policies(
        self,
        Identity: str,
        PolicyNames: List,
    ) -> Dict:
        pass


    def get_identity_verification_attributes(
        self,
        Identities: List,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_send_quota(
        self,
    ) -> Dict:
        pass


    def get_send_statistics(
        self,
    ) -> Dict:
        pass


    def get_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_configuration_sets(
        self,
        NextToken: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_custom_verification_email_templates(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_identities(
        self,
        IdentityType: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_identity_policies(
        self,
        Identity: str,
    ) -> Dict:
        pass


    def list_receipt_filters(
        self,
    ) -> Dict:
        pass


    def list_receipt_rule_sets(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_templates(
        self,
        NextToken: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_verified_email_addresses(
        self,
    ) -> Dict:
        pass


    def put_configuration_set_delivery_options(
        self,
        ConfigurationSetName: str,
        DeliveryOptions: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_identity_policy(
        self,
        Identity: str,
        PolicyName: str,
        Policy: str,
    ) -> Dict:
        pass


    def reorder_receipt_rule_set(
        self,
        RuleSetName: str,
        RuleNames: List,
    ) -> Dict:
        pass


    def send_bounce(
        self,
        OriginalMessageId: str,
        BounceSender: str,
        BouncedRecipientInfoList: List,
        Explanation: Optional[str] = None,
        MessageDsn: Optional[Dict] = None,
        BounceSenderArn: Optional[str] = None,
    ) -> Dict:
        pass


    def send_bulk_templated_email(
        self,
        Source: str,
        Template: str,
        Destinations: List,
        SourceArn: Optional[str] = None,
        ReplyToAddresses: Optional[List] = None,
        ReturnPath: Optional[str] = None,
        ReturnPathArn: Optional[str] = None,
        ConfigurationSetName: Optional[str] = None,
        DefaultTags: Optional[List] = None,
        TemplateArn: Optional[str] = None,
        DefaultTemplateData: Optional[str] = None,
    ) -> Dict:
        pass


    def send_custom_verification_email(
        self,
        EmailAddress: str,
        TemplateName: str,
        ConfigurationSetName: Optional[str] = None,
    ) -> Dict:
        pass


    def send_email(
        self,
        Source: str,
        Destination: Dict,
        Message: Dict,
        ReplyToAddresses: Optional[List] = None,
        ReturnPath: Optional[str] = None,
        SourceArn: Optional[str] = None,
        ReturnPathArn: Optional[str] = None,
        Tags: Optional[List] = None,
        ConfigurationSetName: Optional[str] = None,
    ) -> Dict:
        pass


    def send_raw_email(
        self,
        RawMessage: Dict,
        Source: Optional[str] = None,
        Destinations: Optional[List] = None,
        FromArn: Optional[str] = None,
        SourceArn: Optional[str] = None,
        ReturnPathArn: Optional[str] = None,
        Tags: Optional[List] = None,
        ConfigurationSetName: Optional[str] = None,
    ) -> Dict:
        pass


    def send_templated_email(
        self,
        Source: str,
        Destination: Dict,
        Template: str,
        TemplateData: str,
        ReplyToAddresses: Optional[List] = None,
        ReturnPath: Optional[str] = None,
        SourceArn: Optional[str] = None,
        ReturnPathArn: Optional[str] = None,
        Tags: Optional[List] = None,
        ConfigurationSetName: Optional[str] = None,
        TemplateArn: Optional[str] = None,
    ) -> Dict:
        pass


    def set_active_receipt_rule_set(
        self,
        RuleSetName: Optional[str] = None,
    ) -> Dict:
        pass


    def set_identity_dkim_enabled(
        self,
        Identity: str,
        DkimEnabled: bool,
    ) -> Dict:
        pass


    def set_identity_feedback_forwarding_enabled(
        self,
        Identity: str,
        ForwardingEnabled: bool,
    ) -> Dict:
        pass


    def set_identity_headers_in_notifications_enabled(
        self,
        Identity: str,
        NotificationType: str,
        Enabled: bool,
    ) -> Dict:
        pass


    def set_identity_mail_from_domain(
        self,
        Identity: str,
        MailFromDomain: Optional[str] = None,
        BehaviorOnMXFailure: Optional[str] = None,
    ) -> Dict:
        pass


    def set_identity_notification_topic(
        self,
        Identity: str,
        NotificationType: str,
        SnsTopic: Optional[str] = None,
    ) -> Dict:
        pass


    def set_receipt_rule_position(
        self,
        RuleSetName: str,
        RuleName: str,
        After: Optional[str] = None,
    ) -> Dict:
        pass


    def test_render_template(
        self,
        TemplateName: str,
        TemplateData: str,
    ) -> Dict:
        pass


    def update_account_sending_enabled(
        self,
        Enabled: Optional[bool] = None,
    ):
        pass


    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: Dict,
    ) -> Dict:
        pass


    def update_configuration_set_reputation_metrics_enabled(
        self,
        ConfigurationSetName: str,
        Enabled: bool,
    ):
        pass


    def update_configuration_set_sending_enabled(
        self,
        ConfigurationSetName: str,
        Enabled: bool,
    ):
        pass


    def update_configuration_set_tracking_options(
        self,
        ConfigurationSetName: str,
        TrackingOptions: Dict,
    ) -> Dict:
        pass


    def update_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: Optional[str] = None,
        TemplateSubject: Optional[str] = None,
        TemplateContent: Optional[str] = None,
        SuccessRedirectionURL: Optional[str] = None,
        FailureRedirectionURL: Optional[str] = None,
    ):
        pass


    def update_receipt_rule(
        self,
        RuleSetName: str,
        Rule: Dict,
    ) -> Dict:
        pass


    def update_template(
        self,
        Template: Dict,
    ) -> Dict:
        pass


    def verify_domain_dkim(
        self,
        Domain: str,
    ) -> Dict:
        pass


    def verify_domain_identity(
        self,
        Domain: str,
    ) -> Dict:
        pass


    def verify_email_address(
        self,
        EmailAddress: str,
    ):
        pass


    def verify_email_identity(
        self,
        EmailAddress: str,
    ) -> Dict:
        pass

