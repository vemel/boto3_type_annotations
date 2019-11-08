# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ec2.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ec2](index.md#ec2) / Client
    - [Client](#client)
        - [Client().accept_reserved_instances_exchange_quote](#clientaccept_reserved_instances_exchange_quote)
        - [Client().accept_transit_gateway_vpc_attachment](#clientaccept_transit_gateway_vpc_attachment)
        - [Client().accept_vpc_endpoint_connections](#clientaccept_vpc_endpoint_connections)
        - [Client().accept_vpc_peering_connection](#clientaccept_vpc_peering_connection)
        - [Client().advertise_byoip_cidr](#clientadvertise_byoip_cidr)
        - [Client().allocate_address](#clientallocate_address)
        - [Client().allocate_hosts](#clientallocate_hosts)
        - [Client().apply_security_groups_to_client_vpn_target_network](#clientapply_security_groups_to_client_vpn_target_network)
        - [Client().assign_ipv6_addresses](#clientassign_ipv6_addresses)
        - [Client().assign_private_ip_addresses](#clientassign_private_ip_addresses)
        - [Client().associate_address](#clientassociate_address)
        - [Client().associate_client_vpn_target_network](#clientassociate_client_vpn_target_network)
        - [Client().associate_dhcp_options](#clientassociate_dhcp_options)
        - [Client().associate_iam_instance_profile](#clientassociate_iam_instance_profile)
        - [Client().associate_route_table](#clientassociate_route_table)
        - [Client().associate_subnet_cidr_block](#clientassociate_subnet_cidr_block)
        - [Client().associate_transit_gateway_route_table](#clientassociate_transit_gateway_route_table)
        - [Client().associate_vpc_cidr_block](#clientassociate_vpc_cidr_block)
        - [Client().attach_classic_link_vpc](#clientattach_classic_link_vpc)
        - [Client().attach_internet_gateway](#clientattach_internet_gateway)
        - [Client().attach_network_interface](#clientattach_network_interface)
        - [Client().attach_volume](#clientattach_volume)
        - [Client().attach_vpn_gateway](#clientattach_vpn_gateway)
        - [Client().authorize_client_vpn_ingress](#clientauthorize_client_vpn_ingress)
        - [Client().authorize_security_group_egress](#clientauthorize_security_group_egress)
        - [Client().authorize_security_group_ingress](#clientauthorize_security_group_ingress)
        - [Client().bundle_instance](#clientbundle_instance)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_bundle_task](#clientcancel_bundle_task)
        - [Client().cancel_capacity_reservation](#clientcancel_capacity_reservation)
        - [Client().cancel_conversion_task](#clientcancel_conversion_task)
        - [Client().cancel_export_task](#clientcancel_export_task)
        - [Client().cancel_import_task](#clientcancel_import_task)
        - [Client().cancel_reserved_instances_listing](#clientcancel_reserved_instances_listing)
        - [Client().cancel_spot_fleet_requests](#clientcancel_spot_fleet_requests)
        - [Client().cancel_spot_instance_requests](#clientcancel_spot_instance_requests)
        - [Client().confirm_product_instance](#clientconfirm_product_instance)
        - [Client().copy_fpga_image](#clientcopy_fpga_image)
        - [Client().copy_image](#clientcopy_image)
        - [Client().copy_snapshot](#clientcopy_snapshot)
        - [Client().create_capacity_reservation](#clientcreate_capacity_reservation)
        - [Client().create_client_vpn_endpoint](#clientcreate_client_vpn_endpoint)
        - [Client().create_client_vpn_route](#clientcreate_client_vpn_route)
        - [Client().create_customer_gateway](#clientcreate_customer_gateway)
        - [Client().create_default_subnet](#clientcreate_default_subnet)
        - [Client().create_default_vpc](#clientcreate_default_vpc)
        - [Client().create_dhcp_options](#clientcreate_dhcp_options)
        - [Client().create_egress_only_internet_gateway](#clientcreate_egress_only_internet_gateway)
        - [Client().create_fleet](#clientcreate_fleet)
        - [Client().create_flow_logs](#clientcreate_flow_logs)
        - [Client().create_fpga_image](#clientcreate_fpga_image)
        - [Client().create_image](#clientcreate_image)
        - [Client().create_instance_export_task](#clientcreate_instance_export_task)
        - [Client().create_internet_gateway](#clientcreate_internet_gateway)
        - [Client().create_key_pair](#clientcreate_key_pair)
        - [Client().create_launch_template](#clientcreate_launch_template)
        - [Client().create_launch_template_version](#clientcreate_launch_template_version)
        - [Client().create_nat_gateway](#clientcreate_nat_gateway)
        - [Client().create_network_acl](#clientcreate_network_acl)
        - [Client().create_network_acl_entry](#clientcreate_network_acl_entry)
        - [Client().create_network_interface](#clientcreate_network_interface)
        - [Client().create_network_interface_permission](#clientcreate_network_interface_permission)
        - [Client().create_placement_group](#clientcreate_placement_group)
        - [Client().create_reserved_instances_listing](#clientcreate_reserved_instances_listing)
        - [Client().create_route](#clientcreate_route)
        - [Client().create_route_table](#clientcreate_route_table)
        - [Client().create_security_group](#clientcreate_security_group)
        - [Client().create_snapshot](#clientcreate_snapshot)
        - [Client().create_snapshots](#clientcreate_snapshots)
        - [Client().create_spot_datafeed_subscription](#clientcreate_spot_datafeed_subscription)
        - [Client().create_subnet](#clientcreate_subnet)
        - [Client().create_tags](#clientcreate_tags)
        - [Client().create_traffic_mirror_filter](#clientcreate_traffic_mirror_filter)
        - [Client().create_traffic_mirror_filter_rule](#clientcreate_traffic_mirror_filter_rule)
        - [Client().create_traffic_mirror_session](#clientcreate_traffic_mirror_session)
        - [Client().create_traffic_mirror_target](#clientcreate_traffic_mirror_target)
        - [Client().create_transit_gateway](#clientcreate_transit_gateway)
        - [Client().create_transit_gateway_route](#clientcreate_transit_gateway_route)
        - [Client().create_transit_gateway_route_table](#clientcreate_transit_gateway_route_table)
        - [Client().create_transit_gateway_vpc_attachment](#clientcreate_transit_gateway_vpc_attachment)
        - [Client().create_volume](#clientcreate_volume)
        - [Client().create_vpc](#clientcreate_vpc)
        - [Client().create_vpc_endpoint](#clientcreate_vpc_endpoint)
        - [Client().create_vpc_endpoint_connection_notification](#clientcreate_vpc_endpoint_connection_notification)
        - [Client().create_vpc_endpoint_service_configuration](#clientcreate_vpc_endpoint_service_configuration)
        - [Client().create_vpc_peering_connection](#clientcreate_vpc_peering_connection)
        - [Client().create_vpn_connection](#clientcreate_vpn_connection)
        - [Client().create_vpn_connection_route](#clientcreate_vpn_connection_route)
        - [Client().create_vpn_gateway](#clientcreate_vpn_gateway)
        - [Client().delete_client_vpn_endpoint](#clientdelete_client_vpn_endpoint)
        - [Client().delete_client_vpn_route](#clientdelete_client_vpn_route)
        - [Client().delete_customer_gateway](#clientdelete_customer_gateway)
        - [Client().delete_dhcp_options](#clientdelete_dhcp_options)
        - [Client().delete_egress_only_internet_gateway](#clientdelete_egress_only_internet_gateway)
        - [Client().delete_fleets](#clientdelete_fleets)
        - [Client().delete_flow_logs](#clientdelete_flow_logs)
        - [Client().delete_fpga_image](#clientdelete_fpga_image)
        - [Client().delete_internet_gateway](#clientdelete_internet_gateway)
        - [Client().delete_key_pair](#clientdelete_key_pair)
        - [Client().delete_launch_template](#clientdelete_launch_template)
        - [Client().delete_launch_template_versions](#clientdelete_launch_template_versions)
        - [Client().delete_nat_gateway](#clientdelete_nat_gateway)
        - [Client().delete_network_acl](#clientdelete_network_acl)
        - [Client().delete_network_acl_entry](#clientdelete_network_acl_entry)
        - [Client().delete_network_interface](#clientdelete_network_interface)
        - [Client().delete_network_interface_permission](#clientdelete_network_interface_permission)
        - [Client().delete_placement_group](#clientdelete_placement_group)
        - [Client().delete_queued_reserved_instances](#clientdelete_queued_reserved_instances)
        - [Client().delete_route](#clientdelete_route)
        - [Client().delete_route_table](#clientdelete_route_table)
        - [Client().delete_security_group](#clientdelete_security_group)
        - [Client().delete_snapshot](#clientdelete_snapshot)
        - [Client().delete_spot_datafeed_subscription](#clientdelete_spot_datafeed_subscription)
        - [Client().delete_subnet](#clientdelete_subnet)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().delete_traffic_mirror_filter](#clientdelete_traffic_mirror_filter)
        - [Client().delete_traffic_mirror_filter_rule](#clientdelete_traffic_mirror_filter_rule)
        - [Client().delete_traffic_mirror_session](#clientdelete_traffic_mirror_session)
        - [Client().delete_traffic_mirror_target](#clientdelete_traffic_mirror_target)
        - [Client().delete_transit_gateway](#clientdelete_transit_gateway)
        - [Client().delete_transit_gateway_route](#clientdelete_transit_gateway_route)
        - [Client().delete_transit_gateway_route_table](#clientdelete_transit_gateway_route_table)
        - [Client().delete_transit_gateway_vpc_attachment](#clientdelete_transit_gateway_vpc_attachment)
        - [Client().delete_volume](#clientdelete_volume)
        - [Client().delete_vpc](#clientdelete_vpc)
        - [Client().delete_vpc_endpoint_connection_notifications](#clientdelete_vpc_endpoint_connection_notifications)
        - [Client().delete_vpc_endpoint_service_configurations](#clientdelete_vpc_endpoint_service_configurations)
        - [Client().delete_vpc_endpoints](#clientdelete_vpc_endpoints)
        - [Client().delete_vpc_peering_connection](#clientdelete_vpc_peering_connection)
        - [Client().delete_vpn_connection](#clientdelete_vpn_connection)
        - [Client().delete_vpn_connection_route](#clientdelete_vpn_connection_route)
        - [Client().delete_vpn_gateway](#clientdelete_vpn_gateway)
        - [Client().deprovision_byoip_cidr](#clientdeprovision_byoip_cidr)
        - [Client().deregister_image](#clientderegister_image)
        - [Client().describe_account_attributes](#clientdescribe_account_attributes)
        - [Client().describe_addresses](#clientdescribe_addresses)
        - [Client().describe_aggregate_id_format](#clientdescribe_aggregate_id_format)
        - [Client().describe_availability_zones](#clientdescribe_availability_zones)
        - [Client().describe_bundle_tasks](#clientdescribe_bundle_tasks)
        - [Client().describe_byoip_cidrs](#clientdescribe_byoip_cidrs)
        - [Client().describe_capacity_reservations](#clientdescribe_capacity_reservations)
        - [Client().describe_classic_link_instances](#clientdescribe_classic_link_instances)
        - [Client().describe_client_vpn_authorization_rules](#clientdescribe_client_vpn_authorization_rules)
        - [Client().describe_client_vpn_connections](#clientdescribe_client_vpn_connections)
        - [Client().describe_client_vpn_endpoints](#clientdescribe_client_vpn_endpoints)
        - [Client().describe_client_vpn_routes](#clientdescribe_client_vpn_routes)
        - [Client().describe_client_vpn_target_networks](#clientdescribe_client_vpn_target_networks)
        - [Client().describe_conversion_tasks](#clientdescribe_conversion_tasks)
        - [Client().describe_customer_gateways](#clientdescribe_customer_gateways)
        - [Client().describe_dhcp_options](#clientdescribe_dhcp_options)
        - [Client().describe_egress_only_internet_gateways](#clientdescribe_egress_only_internet_gateways)
        - [Client().describe_elastic_gpus](#clientdescribe_elastic_gpus)
        - [Client().describe_export_image_tasks](#clientdescribe_export_image_tasks)
        - [Client().describe_export_tasks](#clientdescribe_export_tasks)
        - [Client().describe_fleet_history](#clientdescribe_fleet_history)
        - [Client().describe_fleet_instances](#clientdescribe_fleet_instances)
        - [Client().describe_fleets](#clientdescribe_fleets)
        - [Client().describe_flow_logs](#clientdescribe_flow_logs)
        - [Client().describe_fpga_image_attribute](#clientdescribe_fpga_image_attribute)
        - [Client().describe_fpga_images](#clientdescribe_fpga_images)
        - [Client().describe_host_reservation_offerings](#clientdescribe_host_reservation_offerings)
        - [Client().describe_host_reservations](#clientdescribe_host_reservations)
        - [Client().describe_hosts](#clientdescribe_hosts)
        - [Client().describe_iam_instance_profile_associations](#clientdescribe_iam_instance_profile_associations)
        - [Client().describe_id_format](#clientdescribe_id_format)
        - [Client().describe_identity_id_format](#clientdescribe_identity_id_format)
        - [Client().describe_image_attribute](#clientdescribe_image_attribute)
        - [Client().describe_images](#clientdescribe_images)
        - [Client().describe_import_image_tasks](#clientdescribe_import_image_tasks)
        - [Client().describe_import_snapshot_tasks](#clientdescribe_import_snapshot_tasks)
        - [Client().describe_instance_attribute](#clientdescribe_instance_attribute)
        - [Client().describe_instance_credit_specifications](#clientdescribe_instance_credit_specifications)
        - [Client().describe_instance_status](#clientdescribe_instance_status)
        - [Client().describe_instances](#clientdescribe_instances)
        - [Client().describe_internet_gateways](#clientdescribe_internet_gateways)
        - [Client().describe_key_pairs](#clientdescribe_key_pairs)
        - [Client().describe_launch_template_versions](#clientdescribe_launch_template_versions)
        - [Client().describe_launch_templates](#clientdescribe_launch_templates)
        - [Client().describe_moving_addresses](#clientdescribe_moving_addresses)
        - [Client().describe_nat_gateways](#clientdescribe_nat_gateways)
        - [Client().describe_network_acls](#clientdescribe_network_acls)
        - [Client().describe_network_interface_attribute](#clientdescribe_network_interface_attribute)
        - [Client().describe_network_interface_permissions](#clientdescribe_network_interface_permissions)
        - [Client().describe_network_interfaces](#clientdescribe_network_interfaces)
        - [Client().describe_placement_groups](#clientdescribe_placement_groups)
        - [Client().describe_prefix_lists](#clientdescribe_prefix_lists)
        - [Client().describe_principal_id_format](#clientdescribe_principal_id_format)
        - [Client().describe_public_ipv4_pools](#clientdescribe_public_ipv4_pools)
        - [Client().describe_regions](#clientdescribe_regions)
        - [Client().describe_reserved_instances](#clientdescribe_reserved_instances)
        - [Client().describe_reserved_instances_listings](#clientdescribe_reserved_instances_listings)
        - [Client().describe_reserved_instances_modifications](#clientdescribe_reserved_instances_modifications)
        - [Client().describe_reserved_instances_offerings](#clientdescribe_reserved_instances_offerings)
        - [Client().describe_route_tables](#clientdescribe_route_tables)
        - [Client().describe_scheduled_instance_availability](#clientdescribe_scheduled_instance_availability)
        - [Client().describe_scheduled_instances](#clientdescribe_scheduled_instances)
        - [Client().describe_security_group_references](#clientdescribe_security_group_references)
        - [Client().describe_security_groups](#clientdescribe_security_groups)
        - [Client().describe_snapshot_attribute](#clientdescribe_snapshot_attribute)
        - [Client().describe_snapshots](#clientdescribe_snapshots)
        - [Client().describe_spot_datafeed_subscription](#clientdescribe_spot_datafeed_subscription)
        - [Client().describe_spot_fleet_instances](#clientdescribe_spot_fleet_instances)
        - [Client().describe_spot_fleet_request_history](#clientdescribe_spot_fleet_request_history)
        - [Client().describe_spot_fleet_requests](#clientdescribe_spot_fleet_requests)
        - [Client().describe_spot_instance_requests](#clientdescribe_spot_instance_requests)
        - [Client().describe_spot_price_history](#clientdescribe_spot_price_history)
        - [Client().describe_stale_security_groups](#clientdescribe_stale_security_groups)
        - [Client().describe_subnets](#clientdescribe_subnets)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().describe_traffic_mirror_filters](#clientdescribe_traffic_mirror_filters)
        - [Client().describe_traffic_mirror_sessions](#clientdescribe_traffic_mirror_sessions)
        - [Client().describe_traffic_mirror_targets](#clientdescribe_traffic_mirror_targets)
        - [Client().describe_transit_gateway_attachments](#clientdescribe_transit_gateway_attachments)
        - [Client().describe_transit_gateway_route_tables](#clientdescribe_transit_gateway_route_tables)
        - [Client().describe_transit_gateway_vpc_attachments](#clientdescribe_transit_gateway_vpc_attachments)
        - [Client().describe_transit_gateways](#clientdescribe_transit_gateways)
        - [Client().describe_volume_attribute](#clientdescribe_volume_attribute)
        - [Client().describe_volume_status](#clientdescribe_volume_status)
        - [Client().describe_volumes](#clientdescribe_volumes)
        - [Client().describe_volumes_modifications](#clientdescribe_volumes_modifications)
        - [Client().describe_vpc_attribute](#clientdescribe_vpc_attribute)
        - [Client().describe_vpc_classic_link](#clientdescribe_vpc_classic_link)
        - [Client().describe_vpc_classic_link_dns_support](#clientdescribe_vpc_classic_link_dns_support)
        - [Client().describe_vpc_endpoint_connection_notifications](#clientdescribe_vpc_endpoint_connection_notifications)
        - [Client().describe_vpc_endpoint_connections](#clientdescribe_vpc_endpoint_connections)
        - [Client().describe_vpc_endpoint_service_configurations](#clientdescribe_vpc_endpoint_service_configurations)
        - [Client().describe_vpc_endpoint_service_permissions](#clientdescribe_vpc_endpoint_service_permissions)
        - [Client().describe_vpc_endpoint_services](#clientdescribe_vpc_endpoint_services)
        - [Client().describe_vpc_endpoints](#clientdescribe_vpc_endpoints)
        - [Client().describe_vpc_peering_connections](#clientdescribe_vpc_peering_connections)
        - [Client().describe_vpcs](#clientdescribe_vpcs)
        - [Client().describe_vpn_connections](#clientdescribe_vpn_connections)
        - [Client().describe_vpn_gateways](#clientdescribe_vpn_gateways)
        - [Client().detach_classic_link_vpc](#clientdetach_classic_link_vpc)
        - [Client().detach_internet_gateway](#clientdetach_internet_gateway)
        - [Client().detach_network_interface](#clientdetach_network_interface)
        - [Client().detach_volume](#clientdetach_volume)
        - [Client().detach_vpn_gateway](#clientdetach_vpn_gateway)
        - [Client().disable_ebs_encryption_by_default](#clientdisable_ebs_encryption_by_default)
        - [Client().disable_transit_gateway_route_table_propagation](#clientdisable_transit_gateway_route_table_propagation)
        - [Client().disable_vgw_route_propagation](#clientdisable_vgw_route_propagation)
        - [Client().disable_vpc_classic_link](#clientdisable_vpc_classic_link)
        - [Client().disable_vpc_classic_link_dns_support](#clientdisable_vpc_classic_link_dns_support)
        - [Client().disassociate_address](#clientdisassociate_address)
        - [Client().disassociate_client_vpn_target_network](#clientdisassociate_client_vpn_target_network)
        - [Client().disassociate_iam_instance_profile](#clientdisassociate_iam_instance_profile)
        - [Client().disassociate_route_table](#clientdisassociate_route_table)
        - [Client().disassociate_subnet_cidr_block](#clientdisassociate_subnet_cidr_block)
        - [Client().disassociate_transit_gateway_route_table](#clientdisassociate_transit_gateway_route_table)
        - [Client().disassociate_vpc_cidr_block](#clientdisassociate_vpc_cidr_block)
        - [Client().enable_ebs_encryption_by_default](#clientenable_ebs_encryption_by_default)
        - [Client().enable_transit_gateway_route_table_propagation](#clientenable_transit_gateway_route_table_propagation)
        - [Client().enable_vgw_route_propagation](#clientenable_vgw_route_propagation)
        - [Client().enable_volume_io](#clientenable_volume_io)
        - [Client().enable_vpc_classic_link](#clientenable_vpc_classic_link)
        - [Client().enable_vpc_classic_link_dns_support](#clientenable_vpc_classic_link_dns_support)
        - [Client().export_client_vpn_client_certificate_revocation_list](#clientexport_client_vpn_client_certificate_revocation_list)
        - [Client().export_client_vpn_client_configuration](#clientexport_client_vpn_client_configuration)
        - [Client().export_image](#clientexport_image)
        - [Client().export_transit_gateway_routes](#clientexport_transit_gateway_routes)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_capacity_reservation_usage](#clientget_capacity_reservation_usage)
        - [Client().get_console_output](#clientget_console_output)
        - [Client().get_console_screenshot](#clientget_console_screenshot)
        - [Client().get_ebs_default_kms_key_id](#clientget_ebs_default_kms_key_id)
        - [Client().get_ebs_encryption_by_default](#clientget_ebs_encryption_by_default)
        - [Client().get_host_reservation_purchase_preview](#clientget_host_reservation_purchase_preview)
        - [Client().get_launch_template_data](#clientget_launch_template_data)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_password_data](#clientget_password_data)
        - [Client().get_reserved_instances_exchange_quote](#clientget_reserved_instances_exchange_quote)
        - [Client().get_transit_gateway_attachment_propagations](#clientget_transit_gateway_attachment_propagations)
        - [Client().get_transit_gateway_route_table_associations](#clientget_transit_gateway_route_table_associations)
        - [Client().get_transit_gateway_route_table_propagations](#clientget_transit_gateway_route_table_propagations)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_client_vpn_client_certificate_revocation_list](#clientimport_client_vpn_client_certificate_revocation_list)
        - [Client().import_image](#clientimport_image)
        - [Client().import_instance](#clientimport_instance)
        - [Client().import_key_pair](#clientimport_key_pair)
        - [Client().import_snapshot](#clientimport_snapshot)
        - [Client().import_volume](#clientimport_volume)
        - [Client().modify_capacity_reservation](#clientmodify_capacity_reservation)
        - [Client().modify_client_vpn_endpoint](#clientmodify_client_vpn_endpoint)
        - [Client().modify_ebs_default_kms_key_id](#clientmodify_ebs_default_kms_key_id)
        - [Client().modify_fleet](#clientmodify_fleet)
        - [Client().modify_fpga_image_attribute](#clientmodify_fpga_image_attribute)
        - [Client().modify_hosts](#clientmodify_hosts)
        - [Client().modify_id_format](#clientmodify_id_format)
        - [Client().modify_identity_id_format](#clientmodify_identity_id_format)
        - [Client().modify_image_attribute](#clientmodify_image_attribute)
        - [Client().modify_instance_attribute](#clientmodify_instance_attribute)
        - [Client().modify_instance_capacity_reservation_attributes](#clientmodify_instance_capacity_reservation_attributes)
        - [Client().modify_instance_credit_specification](#clientmodify_instance_credit_specification)
        - [Client().modify_instance_event_start_time](#clientmodify_instance_event_start_time)
        - [Client().modify_instance_placement](#clientmodify_instance_placement)
        - [Client().modify_launch_template](#clientmodify_launch_template)
        - [Client().modify_network_interface_attribute](#clientmodify_network_interface_attribute)
        - [Client().modify_reserved_instances](#clientmodify_reserved_instances)
        - [Client().modify_snapshot_attribute](#clientmodify_snapshot_attribute)
        - [Client().modify_spot_fleet_request](#clientmodify_spot_fleet_request)
        - [Client().modify_subnet_attribute](#clientmodify_subnet_attribute)
        - [Client().modify_traffic_mirror_filter_network_services](#clientmodify_traffic_mirror_filter_network_services)
        - [Client().modify_traffic_mirror_filter_rule](#clientmodify_traffic_mirror_filter_rule)
        - [Client().modify_traffic_mirror_session](#clientmodify_traffic_mirror_session)
        - [Client().modify_transit_gateway_vpc_attachment](#clientmodify_transit_gateway_vpc_attachment)
        - [Client().modify_volume](#clientmodify_volume)
        - [Client().modify_volume_attribute](#clientmodify_volume_attribute)
        - [Client().modify_vpc_attribute](#clientmodify_vpc_attribute)
        - [Client().modify_vpc_endpoint](#clientmodify_vpc_endpoint)
        - [Client().modify_vpc_endpoint_connection_notification](#clientmodify_vpc_endpoint_connection_notification)
        - [Client().modify_vpc_endpoint_service_configuration](#clientmodify_vpc_endpoint_service_configuration)
        - [Client().modify_vpc_endpoint_service_permissions](#clientmodify_vpc_endpoint_service_permissions)
        - [Client().modify_vpc_peering_connection_options](#clientmodify_vpc_peering_connection_options)
        - [Client().modify_vpc_tenancy](#clientmodify_vpc_tenancy)
        - [Client().modify_vpn_connection](#clientmodify_vpn_connection)
        - [Client().modify_vpn_tunnel_certificate](#clientmodify_vpn_tunnel_certificate)
        - [Client().modify_vpn_tunnel_options](#clientmodify_vpn_tunnel_options)
        - [Client().monitor_instances](#clientmonitor_instances)
        - [Client().move_address_to_vpc](#clientmove_address_to_vpc)
        - [Client().provision_byoip_cidr](#clientprovision_byoip_cidr)
        - [Client().purchase_host_reservation](#clientpurchase_host_reservation)
        - [Client().purchase_reserved_instances_offering](#clientpurchase_reserved_instances_offering)
        - [Client().purchase_scheduled_instances](#clientpurchase_scheduled_instances)
        - [Client().reboot_instances](#clientreboot_instances)
        - [Client().register_image](#clientregister_image)
        - [Client().reject_transit_gateway_vpc_attachment](#clientreject_transit_gateway_vpc_attachment)
        - [Client().reject_vpc_endpoint_connections](#clientreject_vpc_endpoint_connections)
        - [Client().reject_vpc_peering_connection](#clientreject_vpc_peering_connection)
        - [Client().release_address](#clientrelease_address)
        - [Client().release_hosts](#clientrelease_hosts)
        - [Client().replace_iam_instance_profile_association](#clientreplace_iam_instance_profile_association)
        - [Client().replace_network_acl_association](#clientreplace_network_acl_association)
        - [Client().replace_network_acl_entry](#clientreplace_network_acl_entry)
        - [Client().replace_route](#clientreplace_route)
        - [Client().replace_route_table_association](#clientreplace_route_table_association)
        - [Client().replace_transit_gateway_route](#clientreplace_transit_gateway_route)
        - [Client().report_instance_status](#clientreport_instance_status)
        - [Client().request_spot_fleet](#clientrequest_spot_fleet)
        - [Client().request_spot_instances](#clientrequest_spot_instances)
        - [Client().reset_ebs_default_kms_key_id](#clientreset_ebs_default_kms_key_id)
        - [Client().reset_fpga_image_attribute](#clientreset_fpga_image_attribute)
        - [Client().reset_image_attribute](#clientreset_image_attribute)
        - [Client().reset_instance_attribute](#clientreset_instance_attribute)
        - [Client().reset_network_interface_attribute](#clientreset_network_interface_attribute)
        - [Client().reset_snapshot_attribute](#clientreset_snapshot_attribute)
        - [Client().restore_address_to_classic](#clientrestore_address_to_classic)
        - [Client().revoke_client_vpn_ingress](#clientrevoke_client_vpn_ingress)
        - [Client().revoke_security_group_egress](#clientrevoke_security_group_egress)
        - [Client().revoke_security_group_ingress](#clientrevoke_security_group_ingress)
        - [Client().run_instances](#clientrun_instances)
        - [Client().run_scheduled_instances](#clientrun_scheduled_instances)
        - [Client().search_transit_gateway_routes](#clientsearch_transit_gateway_routes)
        - [Client().send_diagnostic_interrupt](#clientsend_diagnostic_interrupt)
        - [Client().start_instances](#clientstart_instances)
        - [Client().stop_instances](#clientstop_instances)
        - [Client().terminate_client_vpn_connections](#clientterminate_client_vpn_connections)
        - [Client().terminate_instances](#clientterminate_instances)
        - [Client().unassign_ipv6_addresses](#clientunassign_ipv6_addresses)
        - [Client().unassign_private_ip_addresses](#clientunassign_private_ip_addresses)
        - [Client().unmonitor_instances](#clientunmonitor_instances)
        - [Client().update_security_group_rule_descriptions_egress](#clientupdate_security_group_rule_descriptions_egress)
        - [Client().update_security_group_rule_descriptions_ingress](#clientupdate_security_group_rule_descriptions_ingress)
        - [Client().withdraw_byoip_cidr](#clientwithdraw_byoip_cidr)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L13)

```python
class Client(BaseClient):
```

### Client().accept_reserved_instances_exchange_quote

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L16)

```python
def accept_reserved_instances_exchange_quote(
    ReservedInstanceIds: List[Any],
    DryRun: bool = None,
    TargetConfigurations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().accept_transit_gateway_vpc_attachment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L25)

```python
def accept_transit_gateway_vpc_attachment(
    TransitGatewayAttachmentId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().accept_vpc_endpoint_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L31)

```python
def accept_vpc_endpoint_connections(
    ServiceId: str,
    VpcEndpointIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().accept_vpc_peering_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L37)

```python
def accept_vpc_peering_connection(
    DryRun: bool = None,
    VpcPeeringConnectionId: str = None,
) -> Dict[str, Any]:
```

### Client().advertise_byoip_cidr

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L43)

```python
def advertise_byoip_cidr(Cidr: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Client().allocate_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L47)

```python
def allocate_address(
    Domain: str = None,
    Address: str = None,
    PublicIpv4Pool: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().allocate_hosts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L57)

```python
def allocate_hosts(
    AvailabilityZone: str,
    InstanceType: str,
    Quantity: int,
    AutoPlacement: str = None,
    ClientToken: str = None,
    TagSpecifications: List[Any] = None,
    HostRecovery: str = None,
) -> Dict[str, Any]:
```

### Client().apply_security_groups_to_client_vpn_target_network

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L70)

```python
def apply_security_groups_to_client_vpn_target_network(
    ClientVpnEndpointId: str,
    VpcId: str,
    SecurityGroupIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().assign_ipv6_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L80)

```python
def assign_ipv6_addresses(
    NetworkInterfaceId: str,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().assign_private_ip_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L89)

```python
def assign_private_ip_addresses(
    NetworkInterfaceId: str,
    AllowReassignment: bool = None,
    PrivateIpAddresses: List[Any] = None,
    SecondaryPrivateIpAddressCount: int = None,
) -> Dict[str, Any]:
```

### Client().associate_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L99)

```python
def associate_address(
    AllocationId: str = None,
    InstanceId: str = None,
    PublicIp: str = None,
    AllowReassociation: bool = None,
    DryRun: bool = None,
    NetworkInterfaceId: str = None,
    PrivateIpAddress: str = None,
) -> Dict[str, Any]:
```

### Client().associate_client_vpn_target_network

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L112)

```python
def associate_client_vpn_target_network(
    ClientVpnEndpointId: str,
    SubnetId: str,
    ClientToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().associate_dhcp_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L122)

```python
def associate_dhcp_options(
    DhcpOptionsId: str,
    VpcId: str,
    DryRun: bool = None,
) -> None:
```

### Client().associate_iam_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L128)

```python
def associate_iam_instance_profile(
    IamInstanceProfile: Dict[str, Any],
    InstanceId: str,
) -> Dict[str, Any]:
```

### Client().associate_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L134)

```python
def associate_route_table(
    RouteTableId: str,
    SubnetId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().associate_subnet_cidr_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L140)

```python
def associate_subnet_cidr_block(
    Ipv6CidrBlock: str,
    SubnetId: str,
) -> Dict[str, Any]:
```

### Client().associate_transit_gateway_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L146)

```python
def associate_transit_gateway_route_table(
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().associate_vpc_cidr_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L155)

```python
def associate_vpc_cidr_block(
    VpcId: str,
    AmazonProvidedIpv6CidrBlock: bool = None,
    CidrBlock: str = None,
) -> Dict[str, Any]:
```

### Client().attach_classic_link_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L164)

```python
def attach_classic_link_vpc(
    Groups: List[Any],
    InstanceId: str,
    VpcId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().attach_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L170)

```python
def attach_internet_gateway(
    InternetGatewayId: str,
    VpcId: str,
    DryRun: bool = None,
) -> None:
```

### Client().attach_network_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L176)

```python
def attach_network_interface(
    DeviceIndex: int,
    InstanceId: str,
    NetworkInterfaceId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().attach_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L186)

```python
def attach_volume(
    Device: str,
    InstanceId: str,
    VolumeId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().attach_vpn_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L192)

```python
def attach_vpn_gateway(
    VpcId: str,
    VpnGatewayId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().authorize_client_vpn_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L198)

```python
def authorize_client_vpn_ingress(
    ClientVpnEndpointId: str,
    TargetNetworkCidr: str,
    AccessGroupId: str = None,
    AuthorizeAllGroups: bool = None,
    Description: str = None,
    ClientToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().authorize_security_group_egress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L211)

```python
def authorize_security_group_egress(
    GroupId: str,
    DryRun: bool = None,
    IpPermissions: List[Any] = None,
    CidrIp: str = None,
    FromPort: int = None,
    IpProtocol: str = None,
    ToPort: int = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
) -> None:
```

### Client().authorize_security_group_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L226)

```python
def authorize_security_group_ingress(
    CidrIp: str = None,
    FromPort: int = None,
    GroupId: str = None,
    GroupName: str = None,
    IpPermissions: List[Any] = None,
    IpProtocol: str = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
    ToPort: int = None,
    DryRun: bool = None,
) -> None:
```

### Client().bundle_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L242)

```python
def bundle_instance(
    InstanceId: str,
    Storage: Dict[str, Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L248)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_bundle_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L252)

```python
def cancel_bundle_task(BundleId: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Client().cancel_capacity_reservation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L256)

```python
def cancel_capacity_reservation(
    CapacityReservationId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().cancel_conversion_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L262)

```python
def cancel_conversion_task(
    ConversionTaskId: str,
    DryRun: bool = None,
    ReasonMessage: str = None,
) -> None:
```

### Client().cancel_export_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L268)

```python
def cancel_export_task(ExportTaskId: str) -> None:
```

### Client().cancel_import_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L272)

```python
def cancel_import_task(
    CancelReason: str = None,
    DryRun: bool = None,
    ImportTaskId: str = None,
) -> Dict[str, Any]:
```

### Client().cancel_reserved_instances_listing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L278)

```python
def cancel_reserved_instances_listing(
    ReservedInstancesListingId: str,
) -> Dict[str, Any]:
```

### Client().cancel_spot_fleet_requests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L284)

```python
def cancel_spot_fleet_requests(
    SpotFleetRequestIds: List[Any],
    TerminateInstances: bool,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().cancel_spot_instance_requests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L293)

```python
def cancel_spot_instance_requests(
    SpotInstanceRequestIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().confirm_product_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L299)

```python
def confirm_product_instance(
    InstanceId: str,
    ProductCode: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().copy_fpga_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L305)

```python
def copy_fpga_image(
    SourceFpgaImageId: str,
    SourceRegion: str,
    DryRun: bool = None,
    Description: str = None,
    Name: str = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().copy_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L317)

```python
def copy_image(
    Name: str,
    SourceImageId: str,
    SourceRegion: str,
    ClientToken: str = None,
    Description: str = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().copy_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L331)

```python
def copy_snapshot(
    SourceRegion: str,
    SourceSnapshotId: str,
    Description: str = None,
    DestinationRegion: str = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    PresignedUrl: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_capacity_reservation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L345)

```python
def create_capacity_reservation(
    InstanceType: str,
    InstancePlatform: str,
    InstanceCount: int,
    ClientToken: str = None,
    AvailabilityZone: str = None,
    AvailabilityZoneId: str = None,
    Tenancy: str = None,
    EbsOptimized: bool = None,
    EphemeralStorage: bool = None,
    EndDate: datetime = None,
    EndDateType: str = None,
    InstanceMatchCriteria: str = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_client_vpn_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L365)

```python
def create_client_vpn_endpoint(
    ClientCidrBlock: str,
    ServerCertificateArn: str,
    AuthenticationOptions: List[Any],
    ConnectionLogOptions: Dict[str, Any],
    DnsServers: List[Any] = None,
    TransportProtocol: str = None,
    Description: str = None,
    SplitTunnel: bool = None,
    DryRun: bool = None,
    ClientToken: str = None,
    TagSpecifications: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_client_vpn_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L382)

```python
def create_client_vpn_route(
    ClientVpnEndpointId: str,
    DestinationCidrBlock: str,
    TargetVpcSubnetId: str,
    Description: str = None,
    ClientToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_customer_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L394)

```python
def create_customer_gateway(
    BgpAsn: int,
    Type: str,
    PublicIp: str = None,
    CertificateArn: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_default_subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L405)

```python
def create_default_subnet(
    AvailabilityZone: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_default_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L411)

```python
def create_default_vpc(DryRun: bool = None) -> Dict[str, Any]:
```

### Client().create_dhcp_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L415)

```python
def create_dhcp_options(
    DhcpConfigurations: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_egress_only_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L421)

```python
def create_egress_only_internet_gateway(
    VpcId: str,
    ClientToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L427)

```python
def create_fleet(
    LaunchTemplateConfigs: List[Any],
    TargetCapacitySpecification: Dict[str, Any],
    DryRun: bool = None,
    ClientToken: str = None,
    SpotOptions: Dict[str, Any] = None,
    OnDemandOptions: Dict[str, Any] = None,
    ExcessCapacityTerminationPolicy: str = None,
    TerminateInstancesWithExpiration: bool = None,
    Type: str = None,
    ValidFrom: datetime = None,
    ValidUntil: datetime = None,
    ReplaceUnhealthyInstances: bool = None,
    TagSpecifications: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_flow_logs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L446)

```python
def create_flow_logs(
    ResourceIds: List[Any],
    ResourceType: str,
    TrafficType: str,
    DryRun: bool = None,
    ClientToken: str = None,
    DeliverLogsPermissionArn: str = None,
    LogGroupName: str = None,
    LogDestinationType: str = None,
    LogDestination: str = None,
    LogFormat: str = None,
) -> Dict[str, Any]:
```

### Client().create_fpga_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L462)

```python
def create_fpga_image(
    InputStorageLocation: Dict[str, Any],
    DryRun: bool = None,
    LogsStorageLocation: Dict[str, Any] = None,
    Description: str = None,
    Name: str = None,
    ClientToken: str = None,
    TagSpecifications: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L475)

```python
def create_image(
    InstanceId: str,
    Name: str,
    BlockDeviceMappings: List[Any] = None,
    Description: str = None,
    DryRun: bool = None,
    NoReboot: bool = None,
) -> Dict[str, Any]:
```

### Client().create_instance_export_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L487)

```python
def create_instance_export_task(
    InstanceId: str,
    Description: str = None,
    ExportToS3Task: Dict[str, Any] = None,
    TargetEnvironment: str = None,
) -> Dict[str, Any]:
```

### Client().create_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L497)

```python
def create_internet_gateway(DryRun: bool = None) -> Dict[str, Any]:
```

### Client().create_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L501)

```python
def create_key_pair(KeyName: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Client().create_launch_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L505)

```python
def create_launch_template(
    LaunchTemplateName: str,
    LaunchTemplateData: Dict[str, Any],
    DryRun: bool = None,
    ClientToken: str = None,
    VersionDescription: str = None,
    TagSpecifications: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_launch_template_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L517)

```python
def create_launch_template_version(
    LaunchTemplateData: Dict[str, Any],
    DryRun: bool = None,
    ClientToken: str = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None,
    SourceVersion: str = None,
    VersionDescription: str = None,
) -> Dict[str, Any]:
```

### Client().create_nat_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L530)

```python
def create_nat_gateway(
    AllocationId: str,
    SubnetId: str,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_network_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L536)

```python
def create_network_acl(VpcId: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Client().create_network_acl_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L540)

```python
def create_network_acl_entry(
    Egress: bool,
    NetworkAclId: str,
    Protocol: str,
    RuleAction: str,
    RuleNumber: int,
    CidrBlock: str = None,
    DryRun: bool = None,
    IcmpTypeCode: Dict[str, Any] = None,
    Ipv6CidrBlock: str = None,
    PortRange: Dict[str, Any] = None,
) -> None:
```

### Client().create_network_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L556)

```python
def create_network_interface(
    SubnetId: str,
    Description: str = None,
    DryRun: bool = None,
    Groups: List[Any] = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List[Any] = None,
    PrivateIpAddress: str = None,
    PrivateIpAddresses: List[Any] = None,
    SecondaryPrivateIpAddressCount: int = None,
    InterfaceType: str = None,
) -> Dict[str, Any]:
```

### Client().create_network_interface_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L572)

```python
def create_network_interface_permission(
    NetworkInterfaceId: str,
    Permission: str,
    AwsAccountId: str = None,
    AwsService: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_placement_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L583)

```python
def create_placement_group(
    DryRun: bool = None,
    GroupName: str = None,
    Strategy: str = None,
    PartitionCount: int = None,
) -> None:
```

### Client().create_reserved_instances_listing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L593)

```python
def create_reserved_instances_listing(
    ClientToken: str,
    InstanceCount: int,
    PriceSchedules: List[Any],
    ReservedInstancesId: str,
) -> Dict[str, Any]:
```

### Client().create_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L603)

```python
def create_route(
    RouteTableId: str,
    DestinationCidrBlock: str = None,
    DestinationIpv6CidrBlock: str = None,
    DryRun: bool = None,
    EgressOnlyInternetGatewayId: str = None,
    GatewayId: str = None,
    InstanceId: str = None,
    NatGatewayId: str = None,
    TransitGatewayId: str = None,
    NetworkInterfaceId: str = None,
    VpcPeeringConnectionId: str = None,
) -> Dict[str, Any]:
```

### Client().create_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L620)

```python
def create_route_table(VpcId: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Client().create_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L624)

```python
def create_security_group(
    Description: str,
    GroupName: str,
    VpcId: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L630)

```python
def create_snapshot(
    VolumeId: str,
    Description: str = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L640)

```python
def create_snapshots(
    InstanceSpecification: Dict[str, Any],
    Description: str = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
    CopyTagsFromSource: str = None,
) -> Dict[str, Any]:
```

### Client().create_spot_datafeed_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L651)

```python
def create_spot_datafeed_subscription(
    Bucket: str,
    DryRun: bool = None,
    Prefix: str = None,
) -> Dict[str, Any]:
```

### Client().create_subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L657)

```python
def create_subnet(
    CidrBlock: str,
    VpcId: str,
    AvailabilityZone: str = None,
    AvailabilityZoneId: str = None,
    Ipv6CidrBlock: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L669)

```python
def create_tags(
    Resources: List[Any],
    Tags: List[Any],
    DryRun: bool = None,
) -> None:
```

### Client().create_traffic_mirror_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L675)

```python
def create_traffic_mirror_filter(
    Description: str = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_traffic_mirror_filter_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L685)

```python
def create_traffic_mirror_filter_rule(
    TrafficMirrorFilterId: str,
    TrafficDirection: str,
    RuleNumber: int,
    RuleAction: str,
    DestinationCidrBlock: str,
    SourceCidrBlock: str,
    DestinationPortRange: Dict[str, Any] = None,
    SourcePortRange: Dict[str, Any] = None,
    Protocol: int = None,
    Description: str = None,
    DryRun: bool = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_traffic_mirror_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L703)

```python
def create_traffic_mirror_session(
    NetworkInterfaceId: str,
    TrafficMirrorTargetId: str,
    TrafficMirrorFilterId: str,
    SessionNumber: int,
    PacketLength: int = None,
    VirtualNetworkId: int = None,
    Description: str = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_traffic_mirror_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L719)

```python
def create_traffic_mirror_target(
    NetworkInterfaceId: str = None,
    NetworkLoadBalancerArn: str = None,
    Description: str = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_transit_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L731)

```python
def create_transit_gateway(
    Description: str = None,
    Options: Dict[str, Any] = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_transit_gateway_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L741)

```python
def create_transit_gateway_route(
    DestinationCidrBlock: str,
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str = None,
    Blackhole: bool = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_transit_gateway_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L752)

```python
def create_transit_gateway_route_table(
    TransitGatewayId: str,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_transit_gateway_vpc_attachment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L761)

```python
def create_transit_gateway_vpc_attachment(
    TransitGatewayId: str,
    VpcId: str,
    SubnetIds: List[Any],
    Options: Dict[str, Any] = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().create_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L773)

```python
def create_volume(
    AvailabilityZone: str,
    Encrypted: bool = None,
    Iops: int = None,
    KmsKeyId: str = None,
    Size: int = None,
    SnapshotId: str = None,
    VolumeType: str = None,
    DryRun: bool = None,
    TagSpecifications: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L788)

```python
def create_vpc(
    CidrBlock: str,
    AmazonProvidedIpv6CidrBlock: bool = None,
    DryRun: bool = None,
    InstanceTenancy: str = None,
) -> Dict[str, Any]:
```

### Client().create_vpc_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L798)

```python
def create_vpc_endpoint(
    VpcId: str,
    ServiceName: str,
    DryRun: bool = None,
    VpcEndpointType: str = None,
    PolicyDocument: str = None,
    RouteTableIds: List[Any] = None,
    SubnetIds: List[Any] = None,
    SecurityGroupIds: List[Any] = None,
    ClientToken: str = None,
    PrivateDnsEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().create_vpc_endpoint_connection_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L814)

```python
def create_vpc_endpoint_connection_notification(
    ConnectionNotificationArn: str,
    ConnectionEvents: List[Any],
    DryRun: bool = None,
    ServiceId: str = None,
    VpcEndpointId: str = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_vpc_endpoint_service_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L826)

```python
def create_vpc_endpoint_service_configuration(
    NetworkLoadBalancerArns: List[Any],
    DryRun: bool = None,
    AcceptanceRequired: bool = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_vpc_peering_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L836)

```python
def create_vpc_peering_connection(
    DryRun: bool = None,
    PeerOwnerId: str = None,
    PeerVpcId: str = None,
    VpcId: str = None,
    PeerRegion: str = None,
) -> Dict[str, Any]:
```

### Client().create_vpn_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L847)

```python
def create_vpn_connection(
    CustomerGatewayId: str,
    Type: str,
    VpnGatewayId: str = None,
    TransitGatewayId: str = None,
    DryRun: bool = None,
    Options: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_vpn_connection_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L859)

```python
def create_vpn_connection_route(
    DestinationCidrBlock: str,
    VpnConnectionId: str,
) -> None:
```

### Client().create_vpn_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L865)

```python
def create_vpn_gateway(
    Type: str,
    AvailabilityZone: str = None,
    AmazonSideAsn: int = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_client_vpn_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L875)

```python
def delete_client_vpn_endpoint(
    ClientVpnEndpointId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_client_vpn_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L881)

```python
def delete_client_vpn_route(
    ClientVpnEndpointId: str,
    DestinationCidrBlock: str,
    TargetVpcSubnetId: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_customer_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L891)

```python
def delete_customer_gateway(
    CustomerGatewayId: str,
    DryRun: bool = None,
) -> None:
```

### Client().delete_dhcp_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L897)

```python
def delete_dhcp_options(DhcpOptionsId: str, DryRun: bool = None) -> None:
```

### Client().delete_egress_only_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L901)

```python
def delete_egress_only_internet_gateway(
    EgressOnlyInternetGatewayId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_fleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L907)

```python
def delete_fleets(
    FleetIds: List[Any],
    TerminateInstances: bool,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_flow_logs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L913)

```python
def delete_flow_logs(
    FlowLogIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_fpga_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L919)

```python
def delete_fpga_image(
    FpgaImageId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L925)

```python
def delete_internet_gateway(
    InternetGatewayId: str,
    DryRun: bool = None,
) -> None:
```

### Client().delete_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L931)

```python
def delete_key_pair(KeyName: str, DryRun: bool = None) -> None:
```

### Client().delete_launch_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L935)

```python
def delete_launch_template(
    DryRun: bool = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None,
) -> Dict[str, Any]:
```

### Client().delete_launch_template_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L944)

```python
def delete_launch_template_versions(
    Versions: List[Any],
    DryRun: bool = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None,
) -> Dict[str, Any]:
```

### Client().delete_nat_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L954)

```python
def delete_nat_gateway(NatGatewayId: str) -> Dict[str, Any]:
```

### Client().delete_network_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L958)

```python
def delete_network_acl(NetworkAclId: str, DryRun: bool = None) -> None:
```

### Client().delete_network_acl_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L962)

```python
def delete_network_acl_entry(
    Egress: bool,
    NetworkAclId: str,
    RuleNumber: int,
    DryRun: bool = None,
) -> None:
```

### Client().delete_network_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L968)

```python
def delete_network_interface(
    NetworkInterfaceId: str,
    DryRun: bool = None,
) -> None:
```

### Client().delete_network_interface_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L974)

```python
def delete_network_interface_permission(
    NetworkInterfacePermissionId: str,
    Force: bool = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_placement_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L980)

```python
def delete_placement_group(GroupName: str, DryRun: bool = None) -> None:
```

### Client().delete_queued_reserved_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L984)

```python
def delete_queued_reserved_instances(
    ReservedInstancesIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L990)

```python
def delete_route(
    RouteTableId: str,
    DestinationCidrBlock: str = None,
    DestinationIpv6CidrBlock: str = None,
    DryRun: bool = None,
) -> None:
```

### Client().delete_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1000)

```python
def delete_route_table(RouteTableId: str, DryRun: bool = None) -> None:
```

### Client().delete_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1004)

```python
def delete_security_group(
    GroupId: str = None,
    GroupName: str = None,
    DryRun: bool = None,
) -> None:
```

### Client().delete_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1010)

```python
def delete_snapshot(SnapshotId: str, DryRun: bool = None) -> None:
```

### Client().delete_spot_datafeed_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1014)

```python
def delete_spot_datafeed_subscription(DryRun: bool = None) -> None:
```

### Client().delete_subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1018)

```python
def delete_subnet(SubnetId: str, DryRun: bool = None) -> None:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1022)

```python
def delete_tags(
    Resources: List[Any],
    DryRun: bool = None,
    Tags: List[Any] = None,
) -> None:
```

### Client().delete_traffic_mirror_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1028)

```python
def delete_traffic_mirror_filter(
    TrafficMirrorFilterId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_traffic_mirror_filter_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1034)

```python
def delete_traffic_mirror_filter_rule(
    TrafficMirrorFilterRuleId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_traffic_mirror_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1040)

```python
def delete_traffic_mirror_session(
    TrafficMirrorSessionId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_traffic_mirror_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1046)

```python
def delete_traffic_mirror_target(
    TrafficMirrorTargetId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_transit_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1052)

```python
def delete_transit_gateway(
    TransitGatewayId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_transit_gateway_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1058)

```python
def delete_transit_gateway_route(
    TransitGatewayRouteTableId: str,
    DestinationCidrBlock: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_transit_gateway_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1067)

```python
def delete_transit_gateway_route_table(
    TransitGatewayRouteTableId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_transit_gateway_vpc_attachment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1073)

```python
def delete_transit_gateway_vpc_attachment(
    TransitGatewayAttachmentId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1079)

```python
def delete_volume(VolumeId: str, DryRun: bool = None) -> None:
```

### Client().delete_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1083)

```python
def delete_vpc(VpcId: str, DryRun: bool = None) -> None:
```

### Client().delete_vpc_endpoint_connection_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1087)

```python
def delete_vpc_endpoint_connection_notifications(
    ConnectionNotificationIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_vpc_endpoint_service_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1093)

```python
def delete_vpc_endpoint_service_configurations(
    ServiceIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_vpc_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1099)

```python
def delete_vpc_endpoints(
    VpcEndpointIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_vpc_peering_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1105)

```python
def delete_vpc_peering_connection(
    VpcPeeringConnectionId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_vpn_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1111)

```python
def delete_vpn_connection(VpnConnectionId: str, DryRun: bool = None) -> None:
```

### Client().delete_vpn_connection_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1115)

```python
def delete_vpn_connection_route(
    DestinationCidrBlock: str,
    VpnConnectionId: str,
) -> None:
```

### Client().delete_vpn_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1121)

```python
def delete_vpn_gateway(VpnGatewayId: str, DryRun: bool = None) -> None:
```

### Client().deprovision_byoip_cidr

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1125)

```python
def deprovision_byoip_cidr(Cidr: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Client().deregister_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1129)

```python
def deregister_image(ImageId: str, DryRun: bool = None) -> None:
```

### Client().describe_account_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1133)

```python
def describe_account_attributes(
    AttributeNames: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1139)

```python
def describe_addresses(
    Filters: List[Any] = None,
    PublicIps: List[Any] = None,
    AllocationIds: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_aggregate_id_format

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1149)

```python
def describe_aggregate_id_format(DryRun: bool = None) -> Dict[str, Any]:
```

### Client().describe_availability_zones

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1153)

```python
def describe_availability_zones(
    Filters: List[Any] = None,
    ZoneNames: List[Any] = None,
    ZoneIds: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_bundle_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1163)

```python
def describe_bundle_tasks(
    BundleIds: List[Any] = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_byoip_cidrs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1172)

```python
def describe_byoip_cidrs(
    MaxResults: int,
    DryRun: bool = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_capacity_reservations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1178)

```python
def describe_capacity_reservations(
    CapacityReservationIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_classic_link_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1189)

```python
def describe_classic_link_instances(
    Filters: List[Any] = None,
    DryRun: bool = None,
    InstanceIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_client_vpn_authorization_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1200)

```python
def describe_client_vpn_authorization_rules(
    ClientVpnEndpointId: str,
    DryRun: bool = None,
    NextToken: str = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_client_vpn_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1211)

```python
def describe_client_vpn_connections(
    ClientVpnEndpointId: str,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_client_vpn_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1222)

```python
def describe_client_vpn_endpoints(
    ClientVpnEndpointIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_client_vpn_routes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1233)

```python
def describe_client_vpn_routes(
    ClientVpnEndpointId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_client_vpn_target_networks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1244)

```python
def describe_client_vpn_target_networks(
    ClientVpnEndpointId: str,
    AssociationIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_conversion_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1256)

```python
def describe_conversion_tasks(
    ConversionTaskIds: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_customer_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1262)

```python
def describe_customer_gateways(
    CustomerGatewayIds: List[Any] = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_dhcp_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1271)

```python
def describe_dhcp_options(
    DhcpOptionsIds: List[Any] = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_egress_only_internet_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1282)

```python
def describe_egress_only_internet_gateways(
    DryRun: bool = None,
    EgressOnlyInternetGatewayIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_elastic_gpus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1292)

```python
def describe_elastic_gpus(
    ElasticGpuIds: List[Any] = None,
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_export_image_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1303)

```python
def describe_export_image_tasks(
    DryRun: bool = None,
    Filters: List[Any] = None,
    ExportImageTaskIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_export_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1314)

```python
def describe_export_tasks(ExportTaskIds: List[Any] = None) -> Dict[str, Any]:
```

### Client().describe_fleet_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1318)

```python
def describe_fleet_history(
    FleetId: str,
    StartTime: datetime,
    DryRun: bool = None,
    EventType: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_fleet_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1330)

```python
def describe_fleet_instances(
    FleetId: str,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_fleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1341)

```python
def describe_fleets(
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    FleetIds: List[Any] = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_flow_logs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1352)

```python
def describe_flow_logs(
    DryRun: bool = None,
    Filters: List[Any] = None,
    FlowLogIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_fpga_image_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1363)

```python
def describe_fpga_image_attribute(
    FpgaImageId: str,
    Attribute: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_fpga_images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1369)

```python
def describe_fpga_images(
    DryRun: bool = None,
    FpgaImageIds: List[Any] = None,
    Owners: List[Any] = None,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_host_reservation_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1381)

```python
def describe_host_reservation_offerings(
    Filters: List[Any] = None,
    MaxDuration: int = None,
    MaxResults: int = None,
    MinDuration: int = None,
    NextToken: str = None,
    OfferingId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_host_reservations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1393)

```python
def describe_host_reservations(
    Filters: List[Any] = None,
    HostReservationIdSet: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_hosts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1403)

```python
def describe_hosts(
    Filters: List[Any] = None,
    HostIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_iam_instance_profile_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1413)

```python
def describe_iam_instance_profile_associations(
    AssociationIds: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_id_format

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1423)

```python
def describe_id_format(Resource: str = None) -> Dict[str, Any]:
```

### Client().describe_identity_id_format

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1427)

```python
def describe_identity_id_format(
    PrincipalArn: str,
    Resource: str = None,
) -> Dict[str, Any]:
```

### Client().describe_image_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1433)

```python
def describe_image_attribute(
    Attribute: str,
    ImageId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1439)

```python
def describe_images(
    ExecutableUsers: List[Any] = None,
    Filters: List[Any] = None,
    ImageIds: List[Any] = None,
    Owners: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_import_image_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1450)

```python
def describe_import_image_tasks(
    DryRun: bool = None,
    Filters: List[Any] = None,
    ImportTaskIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_import_snapshot_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1461)

```python
def describe_import_snapshot_tasks(
    DryRun: bool = None,
    Filters: List[Any] = None,
    ImportTaskIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1472)

```python
def describe_instance_attribute(
    Attribute: str,
    InstanceId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_credit_specifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1478)

```python
def describe_instance_credit_specifications(
    DryRun: bool = None,
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1489)

```python
def describe_instance_status(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
    IncludeAllInstances: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1501)

```python
def describe_instances(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_internet_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1512)

```python
def describe_internet_gateways(
    Filters: List[Any] = None,
    DryRun: bool = None,
    InternetGatewayIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_key_pairs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1523)

```python
def describe_key_pairs(
    Filters: List[Any] = None,
    KeyNames: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_launch_template_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1529)

```python
def describe_launch_template_versions(
    DryRun: bool = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None,
    Versions: List[Any] = None,
    MinVersion: str = None,
    MaxVersion: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_launch_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1544)

```python
def describe_launch_templates(
    DryRun: bool = None,
    LaunchTemplateIds: List[Any] = None,
    LaunchTemplateNames: List[Any] = None,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_moving_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1556)

```python
def describe_moving_addresses(
    Filters: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    PublicIps: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_nat_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1567)

```python
def describe_nat_gateways(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NatGatewayIds: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_network_acls

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1577)

```python
def describe_network_acls(
    Filters: List[Any] = None,
    DryRun: bool = None,
    NetworkAclIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_network_interface_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1588)

```python
def describe_network_interface_attribute(
    NetworkInterfaceId: str,
    Attribute: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_network_interface_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1594)

```python
def describe_network_interface_permissions(
    NetworkInterfacePermissionIds: List[Any] = None,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_network_interfaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1604)

```python
def describe_network_interfaces(
    Filters: List[Any] = None,
    DryRun: bool = None,
    NetworkInterfaceIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_placement_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1615)

```python
def describe_placement_groups(
    Filters: List[Any] = None,
    DryRun: bool = None,
    GroupNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_prefix_lists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1624)

```python
def describe_prefix_lists(
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    PrefixListIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_principal_id_format

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1635)

```python
def describe_principal_id_format(
    DryRun: bool = None,
    Resources: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_public_ipv4_pools

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1645)

```python
def describe_public_ipv4_pools(
    PoolIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_regions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1651)

```python
def describe_regions(
    Filters: List[Any] = None,
    RegionNames: List[Any] = None,
    DryRun: bool = None,
    AllRegions: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1661)

```python
def describe_reserved_instances(
    Filters: List[Any] = None,
    OfferingClass: str = None,
    ReservedInstancesIds: List[Any] = None,
    DryRun: bool = None,
    OfferingType: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_instances_listings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1672)

```python
def describe_reserved_instances_listings(
    Filters: List[Any] = None,
    ReservedInstancesId: str = None,
    ReservedInstancesListingId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_instances_modifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1681)

```python
def describe_reserved_instances_modifications(
    Filters: List[Any] = None,
    ReservedInstancesModificationIds: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_instances_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1690)

```python
def describe_reserved_instances_offerings(
    AvailabilityZone: str = None,
    Filters: List[Any] = None,
    IncludeMarketplace: bool = None,
    InstanceType: str = None,
    MaxDuration: int = None,
    MaxInstanceCount: int = None,
    MinDuration: int = None,
    OfferingClass: str = None,
    ProductDescription: str = None,
    ReservedInstancesOfferingIds: List[Any] = None,
    DryRun: bool = None,
    InstanceTenancy: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    OfferingType: str = None,
) -> Dict[str, Any]:
```

### Client().describe_route_tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1711)

```python
def describe_route_tables(
    Filters: List[Any] = None,
    DryRun: bool = None,
    RouteTableIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_scheduled_instance_availability

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1722)

```python
def describe_scheduled_instance_availability(
    FirstSlotStartTimeRange: Dict[str, Any],
    Recurrence: Dict[str, Any],
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    MaxSlotDurationInHours: int = None,
    MinSlotDurationInHours: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_scheduled_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1736)

```python
def describe_scheduled_instances(
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    ScheduledInstanceIds: List[Any] = None,
    SlotStartTimeRange: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_security_group_references

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1748)

```python
def describe_security_group_references(
    GroupId: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1754)

```python
def describe_security_groups(
    Filters: List[Any] = None,
    GroupIds: List[Any] = None,
    GroupNames: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_snapshot_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1766)

```python
def describe_snapshot_attribute(
    Attribute: str,
    SnapshotId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1772)

```python
def describe_snapshots(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    OwnerIds: List[Any] = None,
    RestorableByUserIds: List[Any] = None,
    SnapshotIds: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_spot_datafeed_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1785)

```python
def describe_spot_datafeed_subscription(
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_spot_fleet_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1791)

```python
def describe_spot_fleet_instances(
    SpotFleetRequestId: str,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_spot_fleet_request_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1801)

```python
def describe_spot_fleet_request_history(
    SpotFleetRequestId: str,
    StartTime: datetime,
    DryRun: bool = None,
    EventType: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_spot_fleet_requests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1813)

```python
def describe_spot_fleet_requests(
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    SpotFleetRequestIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_spot_instance_requests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1823)

```python
def describe_spot_instance_requests(
    Filters: List[Any] = None,
    DryRun: bool = None,
    SpotInstanceRequestIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_spot_price_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1834)

```python
def describe_spot_price_history(
    Filters: List[Any] = None,
    AvailabilityZone: str = None,
    DryRun: bool = None,
    EndTime: datetime = None,
    InstanceTypes: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    ProductDescriptions: List[Any] = None,
    StartTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().describe_stale_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1849)

```python
def describe_stale_security_groups(
    VpcId: str,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_subnets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1859)

```python
def describe_subnets(
    Filters: List[Any] = None,
    SubnetIds: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1870)

```python
def describe_tags(
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_traffic_mirror_filters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1880)

```python
def describe_traffic_mirror_filters(
    TrafficMirrorFilterIds: List[Any] = None,
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_traffic_mirror_sessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1891)

```python
def describe_traffic_mirror_sessions(
    TrafficMirrorSessionIds: List[Any] = None,
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_traffic_mirror_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1902)

```python
def describe_traffic_mirror_targets(
    TrafficMirrorTargetIds: List[Any] = None,
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_transit_gateway_attachments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1913)

```python
def describe_transit_gateway_attachments(
    TransitGatewayAttachmentIds: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_transit_gateway_route_tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1924)

```python
def describe_transit_gateway_route_tables(
    TransitGatewayRouteTableIds: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_transit_gateway_vpc_attachments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1935)

```python
def describe_transit_gateway_vpc_attachments(
    TransitGatewayAttachmentIds: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_transit_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1946)

```python
def describe_transit_gateways(
    TransitGatewayIds: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_volume_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1957)

```python
def describe_volume_attribute(
    Attribute: str,
    VolumeId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_volume_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1963)

```python
def describe_volume_status(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    VolumeIds: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_volumes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1974)

```python
def describe_volumes(
    Filters: List[Any] = None,
    VolumeIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_volumes_modifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1985)

```python
def describe_volumes_modifications(
    DryRun: bool = None,
    VolumeIds: List[Any] = None,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L1996)

```python
def describe_vpc_attribute(
    Attribute: str,
    VpcId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_classic_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2002)

```python
def describe_vpc_classic_link(
    Filters: List[Any] = None,
    DryRun: bool = None,
    VpcIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_classic_link_dns_support

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2008)

```python
def describe_vpc_classic_link_dns_support(
    MaxResults: int = None,
    NextToken: str = None,
    VpcIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_endpoint_connection_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2014)

```python
def describe_vpc_endpoint_connection_notifications(
    DryRun: bool = None,
    ConnectionNotificationId: str = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_endpoint_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2025)

```python
def describe_vpc_endpoint_connections(
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_endpoint_service_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2035)

```python
def describe_vpc_endpoint_service_configurations(
    DryRun: bool = None,
    ServiceIds: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_endpoint_service_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2046)

```python
def describe_vpc_endpoint_service_permissions(
    ServiceId: str,
    DryRun: bool = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_endpoint_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2057)

```python
def describe_vpc_endpoint_services(
    DryRun: bool = None,
    ServiceNames: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2068)

```python
def describe_vpc_endpoints(
    DryRun: bool = None,
    VpcEndpointIds: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_vpc_peering_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2079)

```python
def describe_vpc_peering_connections(
    Filters: List[Any] = None,
    DryRun: bool = None,
    VpcPeeringConnectionIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_vpcs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2090)

```python
def describe_vpcs(
    Filters: List[Any] = None,
    VpcIds: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_vpn_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2101)

```python
def describe_vpn_connections(
    Filters: List[Any] = None,
    VpnConnectionIds: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_vpn_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2110)

```python
def describe_vpn_gateways(
    Filters: List[Any] = None,
    VpnGatewayIds: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().detach_classic_link_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2119)

```python
def detach_classic_link_vpc(
    InstanceId: str,
    VpcId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().detach_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2125)

```python
def detach_internet_gateway(
    InternetGatewayId: str,
    VpcId: str,
    DryRun: bool = None,
) -> None:
```

### Client().detach_network_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2131)

```python
def detach_network_interface(
    AttachmentId: str,
    DryRun: bool = None,
    Force: bool = None,
) -> None:
```

### Client().detach_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2137)

```python
def detach_volume(
    VolumeId: str,
    Device: str = None,
    Force: bool = None,
    InstanceId: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().detach_vpn_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2148)

```python
def detach_vpn_gateway(
    VpcId: str,
    VpnGatewayId: str,
    DryRun: bool = None,
) -> None:
```

### Client().disable_ebs_encryption_by_default

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2154)

```python
def disable_ebs_encryption_by_default(DryRun: bool = None) -> Dict[str, Any]:
```

### Client().disable_transit_gateway_route_table_propagation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2158)

```python
def disable_transit_gateway_route_table_propagation(
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().disable_vgw_route_propagation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2167)

```python
def disable_vgw_route_propagation(GatewayId: str, RouteTableId: str) -> None:
```

### Client().disable_vpc_classic_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2171)

```python
def disable_vpc_classic_link(
    VpcId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().disable_vpc_classic_link_dns_support

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2177)

```python
def disable_vpc_classic_link_dns_support(VpcId: str = None) -> Dict[str, Any]:
```

### Client().disassociate_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2181)

```python
def disassociate_address(
    AssociationId: str = None,
    PublicIp: str = None,
    DryRun: bool = None,
) -> None:
```

### Client().disassociate_client_vpn_target_network

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2187)

```python
def disassociate_client_vpn_target_network(
    ClientVpnEndpointId: str,
    AssociationId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().disassociate_iam_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2193)

```python
def disassociate_iam_instance_profile(AssociationId: str) -> Dict[str, Any]:
```

### Client().disassociate_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2197)

```python
def disassociate_route_table(AssociationId: str, DryRun: bool = None) -> None:
```

### Client().disassociate_subnet_cidr_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2201)

```python
def disassociate_subnet_cidr_block(AssociationId: str) -> Dict[str, Any]:
```

### Client().disassociate_transit_gateway_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2205)

```python
def disassociate_transit_gateway_route_table(
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().disassociate_vpc_cidr_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2214)

```python
def disassociate_vpc_cidr_block(AssociationId: str) -> Dict[str, Any]:
```

### Client().enable_ebs_encryption_by_default

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2218)

```python
def enable_ebs_encryption_by_default(DryRun: bool = None) -> Dict[str, Any]:
```

### Client().enable_transit_gateway_route_table_propagation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2222)

```python
def enable_transit_gateway_route_table_propagation(
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().enable_vgw_route_propagation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2231)

```python
def enable_vgw_route_propagation(GatewayId: str, RouteTableId: str) -> None:
```

### Client().enable_volume_io

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2235)

```python
def enable_volume_io(VolumeId: str, DryRun: bool = None) -> None:
```

### Client().enable_vpc_classic_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2239)

```python
def enable_vpc_classic_link(
    VpcId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().enable_vpc_classic_link_dns_support

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2245)

```python
def enable_vpc_classic_link_dns_support(VpcId: str = None) -> Dict[str, Any]:
```

### Client().export_client_vpn_client_certificate_revocation_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2249)

```python
def export_client_vpn_client_certificate_revocation_list(
    ClientVpnEndpointId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().export_client_vpn_client_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2255)

```python
def export_client_vpn_client_configuration(
    ClientVpnEndpointId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().export_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2261)

```python
def export_image(
    DiskImageFormat: str,
    ImageId: str,
    S3ExportLocation: Dict[str, Any],
    ClientToken: str = None,
    Description: str = None,
    DryRun: bool = None,
    RoleName: str = None,
) -> Dict[str, Any]:
```

### Client().export_transit_gateway_routes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2274)

```python
def export_transit_gateway_routes(
    TransitGatewayRouteTableId: str,
    S3Bucket: str,
    Filters: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2284)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_capacity_reservation_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2294)

```python
def get_capacity_reservation_usage(
    CapacityReservationId: str,
    NextToken: str = None,
    MaxResults: int = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().get_console_output

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2304)

```python
def get_console_output(
    InstanceId: str,
    DryRun: bool = None,
    Latest: bool = None,
) -> Dict[str, Any]:
```

### Client().get_console_screenshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2310)

```python
def get_console_screenshot(
    InstanceId: str,
    DryRun: bool = None,
    WakeUp: bool = None,
) -> Dict[str, Any]:
```

### Client().get_ebs_default_kms_key_id

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2316)

```python
def get_ebs_default_kms_key_id(DryRun: bool = None) -> Dict[str, Any]:
```

### Client().get_ebs_encryption_by_default

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2320)

```python
def get_ebs_encryption_by_default(DryRun: bool = None) -> Dict[str, Any]:
```

### Client().get_host_reservation_purchase_preview

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2324)

```python
def get_host_reservation_purchase_preview(
    HostIdSet: List[Any],
    OfferingId: str,
) -> Dict[str, Any]:
```

### Client().get_launch_template_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2330)

```python
def get_launch_template_data(
    InstanceId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2336)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_password_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2340)

```python
def get_password_data(InstanceId: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Client().get_reserved_instances_exchange_quote

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2344)

```python
def get_reserved_instances_exchange_quote(
    ReservedInstanceIds: List[Any],
    DryRun: bool = None,
    TargetConfigurations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_transit_gateway_attachment_propagations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2353)

```python
def get_transit_gateway_attachment_propagations(
    TransitGatewayAttachmentId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().get_transit_gateway_route_table_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2364)

```python
def get_transit_gateway_route_table_associations(
    TransitGatewayRouteTableId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().get_transit_gateway_route_table_propagations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2375)

```python
def get_transit_gateway_route_table_propagations(
    TransitGatewayRouteTableId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2386)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_client_vpn_client_certificate_revocation_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2390)

```python
def import_client_vpn_client_certificate_revocation_list(
    ClientVpnEndpointId: str,
    CertificateRevocationList: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().import_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2399)

```python
def import_image(
    Architecture: str = None,
    ClientData: Dict[str, Any] = None,
    ClientToken: str = None,
    Description: str = None,
    DiskContainers: List[Any] = None,
    DryRun: bool = None,
    Encrypted: bool = None,
    Hypervisor: str = None,
    KmsKeyId: str = None,
    LicenseType: str = None,
    Platform: str = None,
    RoleName: str = None,
) -> Dict[str, Any]:
```

### Client().import_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2417)

```python
def import_instance(
    Platform: str,
    Description: str = None,
    DiskImages: List[Any] = None,
    DryRun: bool = None,
    LaunchSpecification: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().import_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2428)

```python
def import_key_pair(
    KeyName: str,
    PublicKeyMaterial: bytes,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().import_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2434)

```python
def import_snapshot(
    ClientData: Dict[str, Any] = None,
    ClientToken: str = None,
    Description: str = None,
    DiskContainer: Dict[str, Any] = None,
    DryRun: bool = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    RoleName: str = None,
) -> Dict[str, Any]:
```

### Client().import_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2448)

```python
def import_volume(
    AvailabilityZone: str,
    Image: Dict[str, Any],
    Volume: Dict[str, Any],
    Description: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_capacity_reservation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2459)

```python
def modify_capacity_reservation(
    CapacityReservationId: str,
    InstanceCount: int = None,
    EndDate: datetime = None,
    EndDateType: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_client_vpn_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2470)

```python
def modify_client_vpn_endpoint(
    ClientVpnEndpointId: str,
    ServerCertificateArn: str = None,
    ConnectionLogOptions: Dict[str, Any] = None,
    DnsServers: Dict[str, Any] = None,
    Description: str = None,
    SplitTunnel: bool = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_ebs_default_kms_key_id

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2483)

```python
def modify_ebs_default_kms_key_id(
    KmsKeyId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2489)

```python
def modify_fleet(
    FleetId: str,
    TargetCapacitySpecification: Dict[str, Any],
    DryRun: bool = None,
    ExcessCapacityTerminationPolicy: str = None,
) -> Dict[str, Any]:
```

### Client().modify_fpga_image_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2499)

```python
def modify_fpga_image_attribute(
    FpgaImageId: str,
    DryRun: bool = None,
    Attribute: str = None,
    OperationType: str = None,
    UserIds: List[Any] = None,
    UserGroups: List[Any] = None,
    ProductCodes: List[Any] = None,
    LoadPermission: Dict[str, Any] = None,
    Description: str = None,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().modify_hosts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2515)

```python
def modify_hosts(
    HostIds: List[Any],
    AutoPlacement: str = None,
    HostRecovery: str = None,
) -> Dict[str, Any]:
```

### Client().modify_id_format

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2521)

```python
def modify_id_format(Resource: str, UseLongIds: bool) -> None:
```

### Client().modify_identity_id_format

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2525)

```python
def modify_identity_id_format(
    PrincipalArn: str,
    Resource: str,
    UseLongIds: bool,
) -> None:
```

### Client().modify_image_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2531)

```python
def modify_image_attribute(
    ImageId: str,
    Attribute: str = None,
    Description: Dict[str, Any] = None,
    LaunchPermission: Dict[str, Any] = None,
    OperationType: str = None,
    ProductCodes: List[Any] = None,
    UserGroups: List[Any] = None,
    UserIds: List[Any] = None,
    Value: str = None,
    DryRun: bool = None,
) -> None:
```

### Client().modify_instance_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2547)

```python
def modify_instance_attribute(
    InstanceId: str,
    SourceDestCheck: Dict[str, Any] = None,
    Attribute: str = None,
    BlockDeviceMappings: List[Any] = None,
    DisableApiTermination: Dict[str, Any] = None,
    DryRun: bool = None,
    EbsOptimized: Dict[str, Any] = None,
    EnaSupport: Dict[str, Any] = None,
    Groups: List[Any] = None,
    InstanceInitiatedShutdownBehavior: Dict[str, Any] = None,
    InstanceType: Dict[str, Any] = None,
    Kernel: Dict[str, Any] = None,
    Ramdisk: Dict[str, Any] = None,
    SriovNetSupport: Dict[str, Any] = None,
    UserData: Dict[str, Any] = None,
    Value: str = None,
) -> None:
```

### Client().modify_instance_capacity_reservation_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2569)

```python
def modify_instance_capacity_reservation_attributes(
    InstanceId: str,
    CapacityReservationSpecification: Dict[str, Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_instance_credit_specification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2578)

```python
def modify_instance_credit_specification(
    InstanceCreditSpecifications: List[Any],
    DryRun: bool = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().modify_instance_event_start_time

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2587)

```python
def modify_instance_event_start_time(
    InstanceId: str,
    InstanceEventId: str,
    NotBefore: datetime,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_instance_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2597)

```python
def modify_instance_placement(
    InstanceId: str,
    Affinity: str = None,
    GroupName: str = None,
    HostId: str = None,
    Tenancy: str = None,
    PartitionNumber: int = None,
) -> Dict[str, Any]:
```

### Client().modify_launch_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2609)

```python
def modify_launch_template(
    DryRun: bool = None,
    ClientToken: str = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None,
    DefaultVersion: str = None,
) -> Dict[str, Any]:
```

### Client().modify_network_interface_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2620)

```python
def modify_network_interface_attribute(
    NetworkInterfaceId: str,
    Attachment: Dict[str, Any] = None,
    Description: Dict[str, Any] = None,
    DryRun: bool = None,
    Groups: List[Any] = None,
    SourceDestCheck: Dict[str, Any] = None,
) -> None:
```

### Client().modify_reserved_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2632)

```python
def modify_reserved_instances(
    ReservedInstancesIds: List[Any],
    TargetConfigurations: List[Any],
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().modify_snapshot_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2641)

```python
def modify_snapshot_attribute(
    SnapshotId: str,
    Attribute: str = None,
    CreateVolumePermission: Dict[str, Any] = None,
    GroupNames: List[Any] = None,
    OperationType: str = None,
    UserIds: List[Any] = None,
    DryRun: bool = None,
) -> None:
```

### Client().modify_spot_fleet_request

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2654)

```python
def modify_spot_fleet_request(
    SpotFleetRequestId: str,
    ExcessCapacityTerminationPolicy: str = None,
    TargetCapacity: int = None,
    OnDemandTargetCapacity: int = None,
) -> Dict[str, Any]:
```

### Client().modify_subnet_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2664)

```python
def modify_subnet_attribute(
    SubnetId: str,
    AssignIpv6AddressOnCreation: Dict[str, Any] = None,
    MapPublicIpOnLaunch: Dict[str, Any] = None,
) -> None:
```

### Client().modify_traffic_mirror_filter_network_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2673)

```python
def modify_traffic_mirror_filter_network_services(
    TrafficMirrorFilterId: str,
    AddNetworkServices: List[Any] = None,
    RemoveNetworkServices: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_traffic_mirror_filter_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2683)

```python
def modify_traffic_mirror_filter_rule(
    TrafficMirrorFilterRuleId: str,
    TrafficDirection: str = None,
    RuleNumber: int = None,
    RuleAction: str = None,
    DestinationPortRange: Dict[str, Any] = None,
    SourcePortRange: Dict[str, Any] = None,
    Protocol: int = None,
    DestinationCidrBlock: str = None,
    SourceCidrBlock: str = None,
    Description: str = None,
    RemoveFields: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_traffic_mirror_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2701)

```python
def modify_traffic_mirror_session(
    TrafficMirrorSessionId: str,
    TrafficMirrorTargetId: str = None,
    TrafficMirrorFilterId: str = None,
    PacketLength: int = None,
    SessionNumber: int = None,
    VirtualNetworkId: int = None,
    Description: str = None,
    RemoveFields: List[Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_transit_gateway_vpc_attachment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2716)

```python
def modify_transit_gateway_vpc_attachment(
    TransitGatewayAttachmentId: str,
    AddSubnetIds: List[Any] = None,
    RemoveSubnetIds: List[Any] = None,
    Options: Dict[str, Any] = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2727)

```python
def modify_volume(
    VolumeId: str,
    DryRun: bool = None,
    Size: int = None,
    VolumeType: str = None,
    Iops: int = None,
) -> Dict[str, Any]:
```

### Client().modify_volume_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2738)

```python
def modify_volume_attribute(
    VolumeId: str,
    AutoEnableIO: Dict[str, Any] = None,
    DryRun: bool = None,
) -> None:
```

### Client().modify_vpc_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2744)

```python
def modify_vpc_attribute(
    VpcId: str,
    EnableDnsHostnames: Dict[str, Any] = None,
    EnableDnsSupport: Dict[str, Any] = None,
) -> None:
```

### Client().modify_vpc_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2753)

```python
def modify_vpc_endpoint(
    VpcEndpointId: str,
    DryRun: bool = None,
    ResetPolicy: bool = None,
    PolicyDocument: str = None,
    AddRouteTableIds: List[Any] = None,
    RemoveRouteTableIds: List[Any] = None,
    AddSubnetIds: List[Any] = None,
    RemoveSubnetIds: List[Any] = None,
    AddSecurityGroupIds: List[Any] = None,
    RemoveSecurityGroupIds: List[Any] = None,
    PrivateDnsEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_vpc_endpoint_connection_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2770)

```python
def modify_vpc_endpoint_connection_notification(
    ConnectionNotificationId: str,
    DryRun: bool = None,
    ConnectionNotificationArn: str = None,
    ConnectionEvents: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_vpc_endpoint_service_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2780)

```python
def modify_vpc_endpoint_service_configuration(
    ServiceId: str,
    DryRun: bool = None,
    AcceptanceRequired: bool = None,
    AddNetworkLoadBalancerArns: List[Any] = None,
    RemoveNetworkLoadBalancerArns: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_vpc_endpoint_service_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2791)

```python
def modify_vpc_endpoint_service_permissions(
    ServiceId: str,
    DryRun: bool = None,
    AddAllowedPrincipals: List[Any] = None,
    RemoveAllowedPrincipals: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_vpc_peering_connection_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2801)

```python
def modify_vpc_peering_connection_options(
    VpcPeeringConnectionId: str,
    AccepterPeeringConnectionOptions: Dict[str, Any] = None,
    DryRun: bool = None,
    RequesterPeeringConnectionOptions: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_vpc_tenancy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2811)

```python
def modify_vpc_tenancy(
    VpcId: str,
    InstanceTenancy: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_vpn_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2817)

```python
def modify_vpn_connection(
    VpnConnectionId: str,
    TransitGatewayId: str = None,
    CustomerGatewayId: str = None,
    VpnGatewayId: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_vpn_tunnel_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2828)

```python
def modify_vpn_tunnel_certificate(
    VpnConnectionId: str,
    VpnTunnelOutsideIpAddress: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_vpn_tunnel_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2834)

```python
def modify_vpn_tunnel_options(
    VpnConnectionId: str,
    VpnTunnelOutsideIpAddress: str,
    TunnelOptions: Dict[str, Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().monitor_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2844)

```python
def monitor_instances(
    InstanceIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().move_address_to_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2850)

```python
def move_address_to_vpc(PublicIp: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Client().provision_byoip_cidr

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2854)

```python
def provision_byoip_cidr(
    Cidr: str,
    CidrAuthorizationContext: Dict[str, Any] = None,
    Description: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().purchase_host_reservation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2864)

```python
def purchase_host_reservation(
    HostIdSet: List[Any],
    OfferingId: str,
    ClientToken: str = None,
    CurrencyCode: str = None,
    LimitPrice: str = None,
) -> Dict[str, Any]:
```

### Client().purchase_reserved_instances_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2875)

```python
def purchase_reserved_instances_offering(
    InstanceCount: int,
    ReservedInstancesOfferingId: str,
    DryRun: bool = None,
    LimitPrice: Dict[str, Any] = None,
    PurchaseTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().purchase_scheduled_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2886)

```python
def purchase_scheduled_instances(
    PurchaseRequests: List[Any],
    ClientToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().reboot_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2892)

```python
def reboot_instances(InstanceIds: List[Any], DryRun: bool = None) -> None:
```

### Client().register_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2896)

```python
def register_image(
    Name: str,
    ImageLocation: str = None,
    Architecture: str = None,
    BlockDeviceMappings: List[Any] = None,
    Description: str = None,
    DryRun: bool = None,
    EnaSupport: bool = None,
    KernelId: str = None,
    BillingProducts: List[Any] = None,
    RamdiskId: str = None,
    RootDeviceName: str = None,
    SriovNetSupport: str = None,
    VirtualizationType: str = None,
) -> Dict[str, Any]:
```

### Client().reject_transit_gateway_vpc_attachment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2915)

```python
def reject_transit_gateway_vpc_attachment(
    TransitGatewayAttachmentId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().reject_vpc_endpoint_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2921)

```python
def reject_vpc_endpoint_connections(
    ServiceId: str,
    VpcEndpointIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().reject_vpc_peering_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2927)

```python
def reject_vpc_peering_connection(
    VpcPeeringConnectionId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().release_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2933)

```python
def release_address(
    AllocationId: str = None,
    PublicIp: str = None,
    DryRun: bool = None,
) -> None:
```

### Client().release_hosts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2939)

```python
def release_hosts(HostIds: List[Any]) -> Dict[str, Any]:
```

### Client().replace_iam_instance_profile_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2943)

```python
def replace_iam_instance_profile_association(
    IamInstanceProfile: Dict[str, Any],
    AssociationId: str,
) -> Dict[str, Any]:
```

### Client().replace_network_acl_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2949)

```python
def replace_network_acl_association(
    AssociationId: str,
    NetworkAclId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().replace_network_acl_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2955)

```python
def replace_network_acl_entry(
    Egress: bool,
    NetworkAclId: str,
    Protocol: str,
    RuleAction: str,
    RuleNumber: int,
    CidrBlock: str = None,
    DryRun: bool = None,
    IcmpTypeCode: Dict[str, Any] = None,
    Ipv6CidrBlock: str = None,
    PortRange: Dict[str, Any] = None,
) -> None:
```

### Client().replace_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2971)

```python
def replace_route(
    RouteTableId: str,
    DestinationCidrBlock: str = None,
    DestinationIpv6CidrBlock: str = None,
    DryRun: bool = None,
    EgressOnlyInternetGatewayId: str = None,
    GatewayId: str = None,
    InstanceId: str = None,
    NatGatewayId: str = None,
    TransitGatewayId: str = None,
    NetworkInterfaceId: str = None,
    VpcPeeringConnectionId: str = None,
) -> None:
```

### Client().replace_route_table_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2988)

```python
def replace_route_table_association(
    AssociationId: str,
    RouteTableId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().replace_transit_gateway_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L2994)

```python
def replace_transit_gateway_route(
    DestinationCidrBlock: str,
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str = None,
    Blackhole: bool = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().report_instance_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3005)

```python
def report_instance_status(
    Instances: List[Any],
    ReasonCodes: List[Any],
    Status: str,
    Description: str = None,
    DryRun: bool = None,
    EndTime: datetime = None,
    StartTime: datetime = None,
) -> None:
```

### Client().request_spot_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3018)

```python
def request_spot_fleet(
    SpotFleetRequestConfig: Dict[str, Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().request_spot_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3024)

```python
def request_spot_instances(
    AvailabilityZoneGroup: str = None,
    BlockDurationMinutes: int = None,
    ClientToken: str = None,
    DryRun: bool = None,
    InstanceCount: int = None,
    LaunchGroup: str = None,
    LaunchSpecification: Dict[str, Any] = None,
    SpotPrice: str = None,
    Type: str = None,
    ValidFrom: datetime = None,
    ValidUntil: datetime = None,
    InstanceInterruptionBehavior: str = None,
) -> Dict[str, Any]:
```

### Client().reset_ebs_default_kms_key_id

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3042)

```python
def reset_ebs_default_kms_key_id(DryRun: bool = None) -> Dict[str, Any]:
```

### Client().reset_fpga_image_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3046)

```python
def reset_fpga_image_attribute(
    FpgaImageId: str,
    DryRun: bool = None,
    Attribute: str = None,
) -> Dict[str, Any]:
```

### Client().reset_image_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3052)

```python
def reset_image_attribute(
    Attribute: str,
    ImageId: str,
    DryRun: bool = None,
) -> None:
```

### Client().reset_instance_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3058)

```python
def reset_instance_attribute(
    Attribute: str,
    InstanceId: str,
    DryRun: bool = None,
) -> None:
```

### Client().reset_network_interface_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3064)

```python
def reset_network_interface_attribute(
    NetworkInterfaceId: str,
    DryRun: bool = None,
    SourceDestCheck: str = None,
) -> None:
```

### Client().reset_snapshot_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3070)

```python
def reset_snapshot_attribute(
    Attribute: str,
    SnapshotId: str,
    DryRun: bool = None,
) -> None:
```

### Client().restore_address_to_classic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3076)

```python
def restore_address_to_classic(
    PublicIp: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().revoke_client_vpn_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3082)

```python
def revoke_client_vpn_ingress(
    ClientVpnEndpointId: str,
    TargetNetworkCidr: str,
    AccessGroupId: str = None,
    RevokeAllGroups: bool = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().revoke_security_group_egress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3093)

```python
def revoke_security_group_egress(
    GroupId: str,
    DryRun: bool = None,
    IpPermissions: List[Any] = None,
    CidrIp: str = None,
    FromPort: int = None,
    IpProtocol: str = None,
    ToPort: int = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
) -> None:
```

### Client().revoke_security_group_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3108)

```python
def revoke_security_group_ingress(
    CidrIp: str = None,
    FromPort: int = None,
    GroupId: str = None,
    GroupName: str = None,
    IpPermissions: List[Any] = None,
    IpProtocol: str = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
    ToPort: int = None,
    DryRun: bool = None,
) -> None:
```

### Client().run_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3124)

```python
def run_instances(
    MaxCount: int,
    MinCount: int,
    BlockDeviceMappings: List[Any] = None,
    ImageId: str = None,
    InstanceType: str = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List[Any] = None,
    KernelId: str = None,
    KeyName: str = None,
    Monitoring: Dict[str, Any] = None,
    Placement: Dict[str, Any] = None,
    RamdiskId: str = None,
    SecurityGroupIds: List[Any] = None,
    SecurityGroups: List[Any] = None,
    SubnetId: str = None,
    UserData: str = None,
    AdditionalInfo: str = None,
    ClientToken: str = None,
    DisableApiTermination: bool = None,
    DryRun: bool = None,
    EbsOptimized: bool = None,
    IamInstanceProfile: Dict[str, Any] = None,
    InstanceInitiatedShutdownBehavior: str = None,
    NetworkInterfaces: List[Any] = None,
    PrivateIpAddress: str = None,
    ElasticGpuSpecification: List[Any] = None,
    ElasticInferenceAccelerators: List[Any] = None,
    TagSpecifications: List[Any] = None,
    LaunchTemplate: Dict[str, Any] = None,
    InstanceMarketOptions: Dict[str, Any] = None,
    CreditSpecification: Dict[str, Any] = None,
    CpuOptions: Dict[str, Any] = None,
    CapacityReservationSpecification: Dict[str, Any] = None,
    HibernationOptions: Dict[str, Any] = None,
    LicenseSpecifications: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().run_scheduled_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3165)

```python
def run_scheduled_instances(
    LaunchSpecification: Dict[str, Any],
    ScheduledInstanceId: str,
    ClientToken: str = None,
    DryRun: bool = None,
    InstanceCount: int = None,
) -> Dict[str, Any]:
```

### Client().search_transit_gateway_routes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3176)

```python
def search_transit_gateway_routes(
    TransitGatewayRouteTableId: str,
    Filters: List[Any],
    MaxResults: int = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().send_diagnostic_interrupt

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3186)

```python
def send_diagnostic_interrupt(InstanceId: str, DryRun: bool = None) -> None:
```

### Client().start_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3190)

```python
def start_instances(
    InstanceIds: List[Any],
    AdditionalInfo: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().stop_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3196)

```python
def stop_instances(
    InstanceIds: List[Any],
    Hibernate: bool = None,
    DryRun: bool = None,
    Force: bool = None,
) -> Dict[str, Any]:
```

### Client().terminate_client_vpn_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3206)

```python
def terminate_client_vpn_connections(
    ClientVpnEndpointId: str,
    ConnectionId: str = None,
    Username: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().terminate_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3216)

```python
def terminate_instances(
    InstanceIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().unassign_ipv6_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3222)

```python
def unassign_ipv6_addresses(
    Ipv6Addresses: List[Any],
    NetworkInterfaceId: str,
) -> Dict[str, Any]:
```

### Client().unassign_private_ip_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3228)

```python
def unassign_private_ip_addresses(
    NetworkInterfaceId: str,
    PrivateIpAddresses: List[Any],
) -> None:
```

### Client().unmonitor_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3234)

```python
def unmonitor_instances(
    InstanceIds: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().update_security_group_rule_descriptions_egress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3240)

```python
def update_security_group_rule_descriptions_egress(
    IpPermissions: List[Any],
    DryRun: bool = None,
    GroupId: str = None,
    GroupName: str = None,
) -> Dict[str, Any]:
```

### Client().update_security_group_rule_descriptions_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3250)

```python
def update_security_group_rule_descriptions_ingress(
    IpPermissions: List[Any],
    DryRun: bool = None,
    GroupId: str = None,
    GroupName: str = None,
) -> Dict[str, Any]:
```

### Client().withdraw_byoip_cidr

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/client.py#L3260)

```python
def withdraw_byoip_cidr(Cidr: str, DryRun: bool = None) -> Dict[str, Any]:
```
