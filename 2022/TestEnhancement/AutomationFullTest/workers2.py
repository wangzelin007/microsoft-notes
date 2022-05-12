from pprint import pprint

# 缺点新增module需要更新。 --是否可以解决？
# 只拆 module 不并行, 需要跑多久？

# Automation full test
jobs = {
    'acr': 195,
    'acs': 225,
    'advisor': 180,
    'ams': 302,
    'apim': 227,
    'appconfig': 203,
    'appservice': 272,  # series
    'aro': 202,
    'backup': 278,
    'batch': 188,
    'batchai': 189,
    'billing': 182,
    'botservice': 164,  # series
    'cdn': 198,
    'cloud': 159,  # series
    'cognitiveservices': 203,
    'config': 186,
    'configure': 180,
    'consumption': 183,
    'container': 185,
    'cosmosdb': 218,
    'databoxedge': 184,
    'deploymentmanager': 185,
    'dla': 211,
    'dls': 181,
    'dms': 191,
    'eventgrid': 192,
    'eventhubs': 218,
    # 'extension': 177,
    'feedback': 204,
    'find': 182,
    'hdinsight': 204,
    'identity': 170,
    'interactive': 168,
    'iot': 214,
    'keyvault': 210,
    'kusto': 184,
    'lab': 207,
    'managedservices': 184,
    'maps': 181,
    'marketplaceordering': 169,
    'monitor': 219,
    'natgateway': 186,
    'netappfiles': 205,
    'network': 472,  # series
    'policyinsights': 191,
    'privatedns': 202,
    'profile': 182,
    'rdbms': 220,
    'redis': 193,
    'relay': 211,
    'reservations': 196,
    'resource': 240,
    'role': 189,
    'search': 188,
    'security': 180,
    'servicebus': 192,
    'serviceconnector': 189,
    'servicefabric': 214,
    'signalr': 185,
    'sql': 240,
    'sqlvm': 192,
    'storage': 281,
    'synapse': 208,
    'util': 189,
    'vm': 396,
    'azure-cli-core': 178,
    'azure-cli-testsdk': 215,
    'azure-cli': 165,
    'azure-cli-telemetry': 171,
 }

def get_worker():
    for idx, worker in enumerate(works):
        tmp_time = sum(worker.values()) if sum(worker.values()) else 0
        if idx == 0:
            worker_time = tmp_time
            worker_num = idx
        if tmp_time < worker_time:
            worker_time = tmp_time
            worker_num = idx
    return worker_num

jobs = sorted(jobs.items(), key=lambda item:-item[1])
# pprint(jobs)
k = 4

works = []
for i in range(k):
    worker = {}
    works.append(worker)

for k, v in jobs:
    idx = get_worker()
    works[idx][k] = v
for idx, work in enumerate(works):
    work['summary'] = sum(work.values())
    works[idx] = sorted(work.items(), key=lambda item:-item[1])
pprint(works)

for idx, work in enumerate(works):
    print('\n\n')
    print('    maxParallel: {}'.format(len(work) - 1))
    print('    matrix:')
    for m, t in work:
        if m != 'summary':
            print('      ' + m + ':')
            print('        ' + 'Target: ' + m)

