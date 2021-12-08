- 提取所有module-command
  - command_loader: <azure.cli.core.MainCommandsLoader object at 0x0000017BEBB274F0>
    - argument_registry.arguments
      - 'connectedmachine show'.'machine_name'.settings.'option_list'
      - --_DISK_xx
    - selected_mod_names: ['acr', 'acs', 'advisor', 'ams', 'apim', 'appconfig', 'appservice', 'aro', 'backup', 'batch', 'batchai', 'billing', 'botservice', 'cdn', 'cloud', 'cognitiveservices', 'config', 'configure', 'consumption', 'container', 'cosmosdb', 'databoxedge', 'deploymentmanager', 'dla', 'dls', 'dms', 'eventgrid', 'eventhubs', 'extension', 'feedback', 'find', 'hdinsight', 'interactive', 'iot', 'keyvault', 'kusto', 'lab', 'managedservices', 'maps', 'marketplaceordering', 'monitor', 'natgateway', 'netappfiles', 'network', 'policyinsights', 'privatedns', 'profile', 'rdbms', 'redis', 'relay', 'reservations', 'resource', 'role', 'search', 'security', 'servicebus', 'serviceconnector', 'servicefabric', 'signalr', 'sql', 'sqlvm', 'storage', 'synapse', 'util', 'vm', 'azure-cli', 'azure-cli-core', 'azure-cli-telemetry', 'azure-cli-testsdk']
    - selected_mod_paths: ['d:\\code\\azure-cli\\src\\azure-cli\\azure\\cli\\command_modules\\acr']
    - selected_modules: core: 4 ext: 0 mod: 65
  - help_file_entries: 
    - 'kusto operation-result show': {'type': 'command', 'short-summary': 'Returns operation results.', 'examples': [{'name': 'KustoOperationResultsGet', 'text': 'az kusto operation-result show --operation-id "30972f1b-b61d-4fd8-bd34-3dcfa24670f3" --location "westus"'}]}
  - loaded_help:
    - 'webpubsub update': <azure.cli.core._help.CliCommandHelpFile object at 0x0000019E813A1970>}
  - exclusions:
    - {}
  - rules: None
  - ci_exclusions: None
  - min_severity: None
  - update_global_exclusion: None
  - rule_types: None
  - loaded_help
    - 'xxx'.parameters 不一定存在挺好的~
    - 'xxx'.command_source.extension_name ['ad'] TODO
    - 'xxx'.preview_info.target ['afd'] TODO
    - 'xxx'.command_source ['ams']
    - 56975 条命令
    - exclude 
      - ['-h', '--help']
      - ['--verbose']
      - ['--debug']
      - ['--only-show-errors']
      - ['--output', '-o']
      - ['--query']
      - 'acr build <SOURCE_LOCATION>'
      - 'acr helm delete <CHART>'
      - 'acr helm push <CHART_PACKAGE>'

---
```
*cmd[(| = ]' And - 
        ipprefix_id = self.cmd('az network public-ip prefix create -g {rg} -n {ipprefix_name} --location {location} --length 29'). \
            get_output_in_json().get("id")
        
        create_cmd = 'aks create -g {resource_group} -n {name} -p {dns_name_prefix} --ssh-key-value {ssh_key_value} ' \
                     '-l {location} --service-principal {service_principal} --client-secret {client_secret} -k {k8s_version} ' \
                     '--node-vm-size {vm_size} ' \
                     '--tags scenario_test -c 1 --no-wait'
        update_cmd = 'aks update --resource-group={resource_group} --name={name} ' \
                     '--aad-admin-group-object-ids 00000000-0000-0000-0000-000000000002 ' \
                     '--aad-tenant-id 00000000-0000-0000-0000-000000000003 -o json'
        stop_cmd = 'aks stop --resource-group={resource_group} --name={name}'
        enable_cmd = 'aks enable-addons --addons confcom --resource-group={resource_group} --name={name} -o json'
        enable_autoscaler_cmd = 'aks update --resource-group={resource_group} --name={name} ' \
                                '--tags {tags} --enable-cluster-autoscaler --min-count 2 --max-count 5'
        disable_cmd = 'aks disable-addons --addons confcom --resource-group={resource_group} --name={name} -o json'
        disable_autoscaler_cmd = 'aks update --resource-group={resource_group} --name={name} ' \
                                 '--tags {tags} --disable-cluster-autoscaler'
        browse_cmd = 'aks browse --resource-group={resource_group} --name={name} --listen-address=127.0.0.1 --listen-port=8080 --disable-browser'
        install_cmd = 'aks install-cli --client-version={} --install-location={} --base-src-url={} ' \
                      '--kubelogin-version={} --kubelogin-install-location={} --kubelogin-base-src-url={}'.format(version, ctl_temp_file, "", version, login_temp_file, "")
        create_spot_node_pool_cmd = 'aks nodepool add ' \
                                    '--resource-group={resource_group} ' \
                                    '--cluster-name={name} ' \
                                    '-n {spot_node_pool_name} ' \
                                    '--priority Spot ' \
                                    '--spot-max-price {spot_max_price} ' \
                                    '-c 1'
        check_role_assignment_cmd = 'role assignment list --scope={vnet_subnet_id}'
        create_ppg_node_pool_cmd = 'aks nodepool add ' \
            '--resource-group={resource_group} ' \
            '--cluster-name={name} ' \
            '-n {node_pool_name} ' \
            '--ppg={ppg} '
        upgrade_node_image_only_cluster_cmd = 'aks upgrade ' \
                                              '-g {resource_group} ' \
                                              '-n {name} ' \
                                              '--node-image-only ' \
                                              '--yes'
        upgrade_node_image_only_nodepool_cmd = 'aks nodepool upgrade ' \
                                               '--resource-group={resource_group} ' \
                                               '--cluster-name={name} ' \
                                               '-n {node_pool_name} ' \
                                               '--node-image-only ' \
                                               '--no-wait'
        uptime_sla_cmd = 'aks update --resource-group={resource_group} --name={name} --uptime-sla --no-wait'
        get_nodepool_cmd = 'aks nodepool show ' \
                           '--resource-group={resource_group} ' \
                           '--cluster-name={name} ' \
                           '-n {node_pool_name} '
        no_uptime_sla_cmd = 'aks update --resource-group={resource_group} --name={name} --no-uptime-sla'
```

# azdev test aro --no-exitfirst --profile latest --verbose --series
azdev test --no-exitfirst --profile latest --verbose --series
# azdev test --no-exitfirst -a "-n 8"
# azdev test --live --lf --xml-path test_results.parallel.xml --no-exitfirst -a "-n 8 --json-report --json-report-summary --json-report-file=cli.report.parallel.json --html=cli.report.parallel.html --self-contained-html --reruns 3 --capture=sys"
# azdev test --live --lf --xml-path test_results.parallel.xml --no-exitfirst -a "-n 8 --capture=sys"
# azdev test --live --mark serial --xml-path test_results.sequential.xml --no-exitfirst -a "-n 1 --json-report --json-report-summary --json-report-file=cli.report.sequential.json --html=cli.report.sequential.html --self-contained-html --reruns 3 --capture=sys"
azdev test --live --mark serial --xml-path test_results.sequential.xml --no-exitfirst -a "-n 1 --capture=sys"
# azdev test --live --mark "not serial" --xml-path test_results.parallel.xml --no-exitfirst -a "-n 8 --json-report --json-report-summary --json-report-file=cli.report.parallel.json --html=cli.report.parallel.html --self-contained-html --reruns 3 --capture=sys"
# azdev test --live --mark "not serial" --xml-path test_results.parallel.xml --no-exitfirst -a "-n 8 --capture=sys"