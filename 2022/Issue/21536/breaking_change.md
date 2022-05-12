version:

# az healthcareapis service:
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}
az healthcareapis service create
--access-policies
--authentication-configuration
--cors-configuration
--cosmos-db-configuration
--etag
--identity-type
--no-wait
--private-endpoint-connections
--public-network-access
--tags
--login-servers (az healthcareapis acr add --login-servers)
--oci-artifacts (new)
--export-configuration-storage-account-name (storage-account-name)

az healthcareapis service delete

az healthcareapis service list

az healthcareapis service show

az healthcareapis service update
--no-wait
--public-network-access
--tags

az healthcareapis service wait

# az healthcareapis acr： (same as az healthcareapis service)

az healthcareapis acr add
--login-servers

az healthcareapis acr list

az healthcareapis acr remove
--login-servers

az healthcareapis acr reset
--login-servers

# az healthcareapis operation-result:
/subscriptions/{subscriptionId}/providers/Microsoft.HealthcareApis/locations/{locationName}/operationresults/{operationResultId}

az healthcareapis operation-result show

# az healthcareapis private-endpoint-connection:
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}
az healthcareapis private-endpoint-connection create
--no-wait
--private-link-service-connection-state-actions-required (old)
--private-link-service-connection-state-description (old)
--private-link-service-connection-state-status (old)
--private-link-service-connection-state (new)

az healthcareapis private-endpoint-connection delete
  
az healthcareapis private-endpoint-connection list

az healthcareapis private-endpoint-connection show

az healthcareapis private-endpoint-connection update
--no-wait
--private-link-service-connection-state-actions-required (delete)
--private-link-service-connection-state-description (delete)
--private-link-service-connection-state-status (delete)
--private-link-service-connection-state (new)

az healthcareapis private-endpoint-connection wait


# az healthcareapis private-link-resource：
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}/privateLinkResources
az healthcareapis private-link-resource list
az healthcareapis private-link-resource show

# az healthcareapis workspace (new)
group workspace
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}
az healthcareapis workspace list
az healthcareapis workspace show
az healthcareapis workspace create
--tags
--etag
--public-network-access
az healthcareapis workspace update
--tags
az healthcareapis workspace delete
az healthcareapis workspace wait

# az healthcareapis workspace-private-endpoint-connection (new)
group workspace subgroup private-endpoint-connection
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/privateEndpointConnections
--workspace-name
az healthcareapis workspace-private-endpoint-connection list
az healthcareapis workspace-private-endpoint-connection show
az healthcareapis workspace-private-endpoint-connection create
--private_endpoint_connection_name --name
--private_link_service_connection_state
az healthcareapis workspace-private-endpoint-connection update
--private_endpoint_connection_name --name
--private_link_service_connection_state
az healthcareapis workspace-private-endpoint-connection delete
az healthcareapis workspace-private-endpoint-connection wait

# az healthcareapis workspace-private-link-resource (new)
group workspace subgroup private-link-resource
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/privateLinkResources
az healthcareapis workspace-private-link-resource list
az healthcareapis workspace-private-link-resource show

# az healthcareapis dicom-service (new)
group workspace subgroup dicom-service
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/dicomservices
--workspace-name
az healthcareapis dicom-service list
az healthcareapis dicom-service show
az healthcareapis dicom-service create
--tags
--etag
--identity-type
--user_assigned_identities
--public_network_access
az healthcareapis dicom-service update
--tags
--identity-type
--user_assigned_identities
az healthcareapis dicom-service delete
az healthcareapis dicom-service wait

# az healthcareapis fhir-service (new)
group workspace subgroup fhir-services
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/fhirservices
workspace_name
az healthcareapis fhir-service list
az healthcareapis fhir-service show
az healthcareapis fhir-service create
--tags
--etag
--identity-type
--user_assigned_identities
--access-policies
--authentication-configuration
--cors-configuration
--public-network-access
--default
--resource_type_overrides
--storage-account-name
--login-servers
--oci-artifacts

az healthcareapis fhir-service update
--tags
--identity-type
--user_assigned_identities

az healthcareapis fhir-service delete
az healthcareapis fhir-service wait

# az healthcareapis iot-connector (new)
group workspace subgroup iot-connector
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors
--workspace-name
az healthcareapis iot-connector list
az healthcareapis iot-connector show
az healthcareapis iot-connector create
--tags
--etag
--identity-type
--user_assigned_identities
--ingestion_endpoint_configuration
--content
az healthcareapis iot-connector update
--tags
--identity-type
--user_assigned_identities
az healthcareapis iot-connector delete
az healthcareapis iot-connector wait

# az healthcareapis iot-connector-fhir-destination (new) 
group workspace subgroup iot-connector subgroup fhirdestinations
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}
--workspace-name
--iot_connector_name
az healthcareapis iot-connector-fhir-destination show
az healthcareapis iot-connector-fhir-destination create
--etag
--resource_identity_resolution_type
--fhir_service_resource_id
--content
az healthcareapis iot-connector-fhir-destination update
--etag
--resource_identity_resolution_type
--fhir_service_resource_id
--content

az healthcareapis iot-connector-fhir-destination delete
az healthcareapis iot-connector-fhir-destination wait

# az healthcareapis fhir-destination (new)
group workspace subgroup iot-connector subgroup fhirdestinations
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations
az healthcareapis fhir-destination list

id_part= child_name_1
arg_group= 分类
c.ignore('iot_fhir_destination') sdk参数

nargs=*，和N类似，但是没有规定列表长度。
nargs=+，和*类似，但是给对应的项当没有传入参数时，会报错error: too few arguments。

https://portal.azure.com/#blade/Microsoft_Azure_Network/PrivateLinkCenterBlade/privateendpoints
