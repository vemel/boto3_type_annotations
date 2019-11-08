from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def clone_receipt_rule_set(
        self, RuleSetName: str, OriginalRuleSetName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_configuration_set(
        self, ConfigurationSet: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestination: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_configuration_set_tracking_options(
        self, ConfigurationSetName: str, TrackingOptions: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_receipt_filter(self, Filter: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_receipt_rule(
        self, RuleSetName: str, Rule: Dict[str, Any], After: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_template(self, Template: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_configuration_set_tracking_options(
        self, ConfigurationSetName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_custom_verification_email_template(self, TemplateName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_identity(self, Identity: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_identity_policy(self, Identity: str, PolicyName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_receipt_filter(self, FilterName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_receipt_rule(self, RuleSetName: str, RuleName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_template(self, TemplateName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_verified_email_address(self, EmailAddress: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_active_receipt_rule_set(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_configuration_set(
        self,
        ConfigurationSetName: str,
        ConfigurationSetAttributeNames: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_receipt_rule(self, RuleSetName: str, RuleName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_account_sending_enabled(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_custom_verification_email_template(
        self, TemplateName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_identity_dkim_attributes(self, Identities: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_identity_mail_from_domain_attributes(
        self, Identities: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_identity_notification_attributes(
        self, Identities: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_identity_policies(
        self, Identity: str, PolicyNames: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_identity_verification_attributes(
        self, Identities: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_send_quota(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_send_statistics(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_template(self, TemplateName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_configuration_sets(
        self, NextToken: str = None, MaxItems: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_custom_verification_email_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_identities(
        self, IdentityType: str = None, NextToken: str = None, MaxItems: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_identity_policies(self, Identity: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_receipt_filters(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_receipt_rule_sets(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_templates(
        self, NextToken: str = None, MaxItems: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_verified_email_addresses(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_configuration_set_delivery_options(
        self, ConfigurationSetName: str, DeliveryOptions: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_identity_policy(
        self, Identity: str, PolicyName: str, Policy: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reorder_receipt_rule_set(
        self, RuleSetName: str, RuleNames: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_bounce(
        self,
        OriginalMessageId: str,
        BounceSender: str,
        BouncedRecipientInfoList: List[Any],
        Explanation: str = None,
        MessageDsn: Dict[str, Any] = None,
        BounceSenderArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_bulk_templated_email(
        self,
        Source: str,
        Template: str,
        Destinations: List[Any],
        SourceArn: str = None,
        ReplyToAddresses: List[Any] = None,
        ReturnPath: str = None,
        ReturnPathArn: str = None,
        ConfigurationSetName: str = None,
        DefaultTags: List[Any] = None,
        TemplateArn: str = None,
        DefaultTemplateData: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_custom_verification_email(
        self, EmailAddress: str, TemplateName: str, ConfigurationSetName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_email(
        self,
        Source: str,
        Destination: Dict[str, Any],
        Message: Dict[str, Any],
        ReplyToAddresses: List[Any] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[Any] = None,
        ConfigurationSetName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_raw_email(
        self,
        RawMessage: Dict[str, Any],
        Source: str = None,
        Destinations: List[Any] = None,
        FromArn: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[Any] = None,
        ConfigurationSetName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_templated_email(
        self,
        Source: str,
        Destination: Dict[str, Any],
        Template: str,
        TemplateData: str,
        ReplyToAddresses: List[Any] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[Any] = None,
        ConfigurationSetName: str = None,
        TemplateArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_active_receipt_rule_set(self, RuleSetName: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_identity_dkim_enabled(
        self, Identity: str, DkimEnabled: bool
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_identity_feedback_forwarding_enabled(
        self, Identity: str, ForwardingEnabled: bool
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_identity_headers_in_notifications_enabled(
        self, Identity: str, NotificationType: str, Enabled: bool
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_identity_mail_from_domain(
        self, Identity: str, MailFromDomain: str = None, BehaviorOnMXFailure: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_identity_notification_topic(
        self, Identity: str, NotificationType: str, SnsTopic: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_receipt_rule_position(
        self, RuleSetName: str, RuleName: str, After: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def test_render_template(
        self, TemplateName: str, TemplateData: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_account_sending_enabled(self, Enabled: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestination: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_configuration_set_reputation_metrics_enabled(
        self, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_configuration_set_sending_enabled(
        self, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_configuration_set_tracking_options(
        self, ConfigurationSetName: str, TrackingOptions: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str = None,
        TemplateSubject: str = None,
        TemplateContent: str = None,
        SuccessRedirectionURL: str = None,
        FailureRedirectionURL: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_receipt_rule(
        self, RuleSetName: str, Rule: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_template(self, Template: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def verify_domain_dkim(self, Domain: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def verify_domain_identity(self, Domain: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def verify_email_address(self, EmailAddress: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def verify_email_identity(self, EmailAddress: str) -> Dict[str, Any]:
        pass
