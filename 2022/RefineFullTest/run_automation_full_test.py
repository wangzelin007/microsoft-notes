import subprocess

modules = ['acr', 'acs', 'advisor', 'ams', 'apim', 'appconfig', 'appservice', 'aro', 'backup', 'batch', 'batchai',
           'billing', 'botservice', 'cdn', 'cloud', 'cognitiveservices', 'config', 'configure', 'consumption',
           'container', 'cosmosdb', 'databoxedge', 'deploymentmanager', 'dla', 'dls', 'dms', 'eventgrid', 'eventhubs',
           'extension', 'feedback', 'find', 'hdinsight', 'iot', 'keyvault', 'kusto', 'lab', 'managedservices', 'maps',
           'monitor', 'natgateway', 'netappfiles', 'network', 'policyinsights', 'privatedns', 'profile', 'rdbms',
           'redis', 'relay', 'reservations', 'resource', 'role', 'search', 'security', 'servicebus', 'servicefabric',
           'signalr', 'sql', 'sqlvm', 'storage', 'synapse', 'util', 'vm']

for module in modules:
    cmd = f"azdev test {module} --no-exitfirst --verbose --series --pytest-args \"--html={module}.report.parallel.html --durations=0\""
    # subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
    subprocess.run(cmd, stdout=subprocess.PIPE)
