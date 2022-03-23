# same with 1011
# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
# 请你将这些工作分配给 k 位工人。
# 所有工作都应该分配给工人，且每项工作只能分配给一位工人。
# 工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。
# 请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
# 返回分配方案中尽可能 最小 的 最大工作时间 。
# 示例 1：
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
# 示例 2：
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。
# 提示：
# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 10**7
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
    'relay': 495,
    'reservations': 305,
    'resource': 1382,
    'role': 552,
    'search': 3738,
    'security': 452,
    'servicebus': 2622,
    'servicefabric': 12475,
    'signalr': 803,
    'sql': 2350,
    'sqlvm': 2625,
    'storage': 16006,
    'synapse': 3567,
    'util': 435,
    'vm': 6316,
    'ext-account': 82,
    'ext-aem': 106,
    'ext-ai-examples': 94,
    'ext-aks-preview': 87,
    'ext-alertsmanagement': 91,
    'ext-alias': 81,
    'ext-application-insights': 85,
    'ext-attestation': 78,
    'ext-azure-batch-cli-extensions': 84,
    'ext-azure-cli-iot-ext': 78,
    'ext-azure-cli-ml': 78,
    'ext-azure-devops': 78,
    'ext-azure-firewall': 74,
    'ext-azure-iot': 80,
    'ext-blockchain': 79,
    'ext-blueprint': 78,
    'ext-codespaces': 101,
    'ext-connectedk8s': 84,
    'ext-connectedmachine': 92,
    'ext-costmanagement': 76,
    'ext-csvmware': 77,
    'ext-custom-providers': 76,
    'ext-databox': 90,
    'ext-databricks': 81,
    'ext-datafactory': 93,
    'ext-datashare': 75,
    'ext-db-up': 88,
    'ext-deploy-to-azure': 75,
    'ext-desktopvirtualization': 80,
    'ext-dev-spaces': 83,
    'ext-dms-preview': 85,
    'ext-eventgrid': 86,
    'ext-express-route': 80,
    'ext-express-route-cross-connection': 84,
    'ext-footprint': 85,
    'ext-front-door': 77,
    'ext-fzf': 85,
    'ext-guestconfig': 84,
    'ext-hack': 78,
    'ext-hardware-security-modules': 85,
    'ext-healthcareapis': 83,
    'ext-hpc-cache': 82,
    'ext-image-copy-extension': 86,
    'ext-import-export': 88,
    'ext-interactive': 76,
    'ext-internet-analyzer': 79,
    'ext-ip-group': 88,
    'ext-k8sconfiguration': 87,
    'ext-keyvault-preview': 78,
    'ext-kusto': 78,
    'ext-log-analytics': 77,
    'ext-log-analytics-solution': 86,
    'ext-logic': 86,
    'ext-maintenance': 81,
    'ext-managementpartner': 76,
    'ext-mesh': 77,
    'ext-mixed-reality': 87,
    'ext-netappfiles-preview': 74,
    'ext-notification-hub': 85,
    'ext-peering': 76,
    'ext-portal': 92,
    'ext-powerbidedicated': 83,
    'ext-privatedns': 76,
    'ext-resource-graph': 76,
    'ext-sap-hana': 81,
    'ext-scheduled-query': 80,
    'ext-spring-cloud': 84,
    'ext-ssh': 76,
    'ext-stack-hci': 84,
    'ext-storage-blob-preview': 77,
    'ext-storage-or-preview': 77,
    'ext-storage-preview': 100,
    'ext-storagesync': 93,
    'ext-stream-analytics': 78,
    'ext-subscription': 75,
    'ext-support': 91,
    'ext-synapse': 75,
    'ext-timeseriesinsights': 86,
    'ext-virtual-network-tap': 77,
    'ext-virtual-wan': 91,
    'ext-vm-repair': 90,
    'ext-vmware': 84,
    'ext-webapp': 84,
 }

class Solution1:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        if k == len(jobs):
            return max(jobs)
        def dfs(num, groups, target):
            if not num:
                return True
            v = num.pop()
            # print('groups', groups, 'target', target)
            for i, group in enumerate(groups):
                # print('i', i, 'num', num, 'v', v)
                if group + v <= target:
                    groups[i] +=v
                    if dfs(num,groups,target): return True
                    groups[i] -=v # todo 不太明白
                if not group:  # 剪枝按照顺序分配
                    # print('group', group)
                    break
            num.append(v) # todo 失败为什么要还原呢？还是不理解
            return False

        jobs.sort()
        i, j = jobs[-1],sum(jobs)
        while i < j :
            mid = i + (j-i)//2
            # print(i,j,mid)
            if dfs(jobs[:],[0]*k,mid): # 浅拷贝，只拷贝的外面的一层
                j = mid
            else:
                i = mid+1
        print(i)
        return i

# todo
class Solution2:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def check(limit):
            # 剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快
            arr = sorted(jobs)
            groups = [0] * k
            # 分成 K 组即 k 个工人，看看在这个limit 下 能不能安排完工作
            if backtrace(arr, groups, limit):
                return True
            else:
                return False

        def backtrace(arr, groups, limit):
            # 尝试每种可能性
            #print(arr, groups, limit)
            if not arr: return True #分完，则方案可行
            v = arr.pop()
            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v
                    # 剪枝，如果这个工人没分到活，那别人肯定得多干活了，那最后的结果必然不是最小的最大值，就不用继续试了。
                    if groups[i] ==0:
                        break

            arr.append(v)
            return False

        #每个人承担的工作的上限，最小为，job 里面的最大值，最大为 jobs 之和
        l, r  = max(jobs), sum(jobs)
        while l < r:
            mid = (l + r)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

# todo
class Solution3:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        #贪心求一个次优解
        from heapq import heapify,heappush,heappop
        heap = [0]*k
        heapify(heap)
        jobs = sorted(jobs)[::-1]
        for i in jobs:
            heappush(heap, heappop(heap)+i)
        m = max(heap)

        a = [0]*k  # k 个工人，每个工人的工作量，初始为 0
        def job(j):
            nonlocal m
            if j == len(jobs):
                m = min(m,max(a))   #记录已知最优解
                return
            for i in range(min(k,j+1)): #剪枝，第 j 个工作只能分配给前 j 个工人
                if a[i]+jobs[j]>m:  #如果工作 j 分配给工人 i 后，工人 i 工作量大于已知最优解 m ，跳过
                    continue
                a[i] += jobs[j]
                job(j+1)
                a[i] -= jobs[j]
        job(0)
        return m

if __name__ == '__main__':
    s = Solution1()
    # jobs = [3,2,3]; k = 3
    # s.minimumTimeRequired(jobs, k)
    # jobs = [1,2,4,7,8]; k = 2
    # s.minimumTimeRequired(jobs, k)
    jobs = list(jobs.values()); k = 4
    s.minimumTimeRequired(jobs, k)
    jobs = list(jobs.values()); k = 5
    s.minimumTimeRequired(jobs, k)