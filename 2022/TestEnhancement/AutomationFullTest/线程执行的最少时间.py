from typing import List

jobs = {
    'acr': 2334,
    'acs': 9715,
    'advisor': 308,
    'ams': 2080,
    'apim': 8868,
    'appconfig': 2185,
    'appservice': 2890,
    'aro': 2429,
    'backup': 12029,
    'batch': 1300,
    'batchai': 400,
    'billing': 305,
    'botservice': 397,
    'cdn': 1286,
    'cloud': 362,
    'cognitiveservices': 1533,
    'config': 308,
    'configure': 340,
    'comsumption': 312,
    'container': 484,
    'cosmosdb': 4142,
    'databoxedge': 571,
    'deploymentmanager': 408,
    'dla': 493,
    'dls': 418,
    'dms': 341,
    'eventgrid': 573,
    'eventhubs': 2402,
    'extension': 374,
    'feedback': 331,
    'find': 300,
    'hdinsight': 3446,
    'iot': 2228,
    'keyvault': 1919,
    'kusto': 3702,
    'lab': 282,
    'managedservices': 353,
    'maps': 377,
    'monitor': 1617,
    'natgateway': 388,
    'netappfiles': 518,
    'network': 13987,
    'policyinsights': 890,
    'privatedns': 922,
    'profile': 1270,
    'rdbms': 6567,
    'redis': 4397,
    # 'relay': 495,
    # 'reservations': 305,
    # 'resource': 1382,
    # 'role': 552,
    # 'search': 3738,
    # 'security': 452,
    # 'servicebus': 2622,
    # 'servicefabric': 12475,
    # 'signalr': 803,
    # 'sql': 2350,
    # 'sqlvm': 2625,
    # 'storage': 16006,
    # 'synapse': 3567,
    # 'util': 435,
    # 'vm': 6316,
    # 'ext-account': 82,
    # 'ext-aem': 106,
    # 'ext-ai-examples': 94,
    # 'ext-aks-preview': 87,
    # 'ext-alertsmanagement': 91,
    # 'ext-alias': 81,
    # 'ext-application-insights': 85,
    # 'ext-attestation': 78,
    # 'ext-azure-batch-cli-extensions': 84,
    # 'ext-azure-cli-iot-ext': 78,
    # 'ext-azure-cli-ml': 78,
    # 'ext-azure-devops': 78,
    # 'ext-azure-firewall': 74,
    # 'ext-azure-iot': 80,
    # 'ext-blockchain': 79,
    # 'ext-blueprint': 78,
    # 'ext-codespaces': 101,
    # 'ext-connectedk8s': 84,
    # 'ext-connectedmachine': 92,
    # 'ext-costmanagement': 76,
    # 'ext-csvmware': 77,
    # 'ext-custom-providers': 76,
    # 'ext-databox': 90,
    # 'ext-databricks': 81,
    # 'ext-datafactory': 93,
    # 'ext-datashare': 75,
    # 'ext-db-up': 88,
    # 'ext-deploy-to-azure': 75,
    # 'ext-desktopvirtualization': 80,
    # 'ext-dev-spaces': 83,
    # 'ext-dms-preview': 85,
    # 'ext-eventgrid': 86,
    # 'ext-express-route': 80,
    # 'ext-express-route-cross-connection': 84,
    # 'ext-footprint': 85,
    # 'ext-front-door': 77,
    # 'ext-fzf': 85,
    # 'ext-guestconfig': 84,
    # 'ext-hack': 78,
    # 'ext-hardware-security-modules': 85,
    # 'ext-healthcareapis': 83,
    # 'ext-hpc-cache': 82,
    # 'ext-image-copy-extension': 86,
    # 'ext-import-export': 88,
    # 'ext-interactive': 76,
    # 'ext-internet-analyzer': 79,
    # 'ext-ip-group': 88,
    # 'ext-k8sconfiguration': 87,
    # 'ext-keyvault-preview': 78,
    # 'ext-kusto': 78,
    # 'ext-log-analytics': 77,
    # 'ext-log-analytics-solution': 86,
    # 'ext-logic': 86,
    # 'ext-maintenance': 81,
    # 'ext-managementpartner': 76,
    # 'ext-mesh': 77,
    # 'ext-mixed-reality': 87,
    # 'ext-netappfiles-preview': 74,
    # 'ext-notification-hub': 85,
    # 'ext-peering': 76,
    # 'ext-portal': 92,
    # 'ext-powerbidedicated': 83,
    # 'ext-privatedns': 76,
    # 'ext-resource-graph': 76,
    # 'ext-sap-hana': 81,
    # 'ext-scheduled-query': 80,
    # 'ext-spring-cloud': 84,
    # 'ext-ssh': 76,
    # 'ext-stack-hci': 84,
    # 'ext-storage-blob-preview': 77,
    # 'ext-storage-or-preview': 77,
    # 'ext-storage-preview': 100,
    # 'ext-storagesync': 93,
    # 'ext-stream-analytics': 78,
    # 'ext-subscription': 75,
    # 'ext-support': 91,
    # 'ext-synapse': 75,
    # 'ext-timeseriesinsights': 86,
    # 'ext-virtual-network-tap': 77,
    # 'ext-virtual-wan': 91,
    # 'ext-vm-repair': 90,
    # 'ext-vmware': 84,
    # 'ext-webapp': 84,
 }

# 动态规划
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # k 代表线程数量
        #---------------------检查当前threshold是否能完成----------------------------#
        def check(threshold : int) -> bool:
            worker = [0 for _ in range(k)]
            #--------------回溯----------------#
            def backtrace(idx: int) -> bool:
                if idx == jobLen:
                    return True
                for i in range(k):
                    if worker[i] + jobs[idx] <= threshold:
                        worker[i] += jobs[idx]
                        if backtrace(idx + 1) == True:
                            return True
                        worker[i] -= jobs[idx]
                    if worker[i] == 0:      #如果当前的没分配上。后面的也分配不上。因为job从大到小
                        break
                    if worker[i] + jobs[idx] == threshold:  #当前就是最优，没必要再往后了
                        break
                return False

            return backtrace(0)

        jobs.sort(reverse = True)
        jobLen = len(jobs)
        # L = max(jobs)
        L = sum(jobs) // k
        R = sum(jobs)
        while L < R:
            mid = (L + R) // 2
            if check(mid) == True:
                R = mid
            else:
                L = mid + 1
        return L

if __name__ == '__main__':
    s = Solution()
    jobs = list(jobs.values())
    print(s.minimumTimeRequired(jobs, k=5))