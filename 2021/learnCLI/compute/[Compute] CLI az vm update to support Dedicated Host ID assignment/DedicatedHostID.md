[Dedicated resource ARM] (https://github.com/Azure/azure-rest-api-specs/blob/master/specification/compute/resource-manager/Microsoft.Compute/stable/2021-07-01/compute.json)

[Dedicated Host Overview] (https://go.microsoft.com/fwlink/?linkid=2082596)  
Applies to: ✔️ Linux VMs ✔️ Windows VMs ✔️ Uniform scale sets  
Azure Dedicated Host is a service that provides physical servers - able to host one or more virtual machines - dedicated to one Azure subscription.  
Dedicated hosts are the same physical servers used in our data centers, provided as a resource.   
You can provision dedicated hosts within a region, availability zone, and fault domain.   
Then, you can place VMs directly into your provisioned hosts, in whatever configuration best meets your needs.  

A host group is a resource that represents a collection of dedicated hosts.   
You create a host group in a region and an availability zone, and add hosts to it.  

A host is a resource, mapped to a physical server in an Azure data center.   
The physical server is allocated when the host is created. A host is created within a host group.   
A host has a SKU describing which VM sizes can be created. Each host can host multiple VMs, of different sizes, as long as they are from the same size series.  

DedicatedHost:   
**一台专用主机。** a physical server in an Azure data center  
**物理服务器是在创建主机时分配的。主机是在主机组内创建的。** The physical server is allocated when the host is created. A host is created within a host group.   
**主机具有描述可以创建哪些 VM 大小的 SKU。每个主机都可以托管多个大小不同的 VM，只要它们来自相同大小的系列即可。**  
A host has a SKU describing which VM sizes can be created. Each host can host multiple VMs, of different sizes, as long as they are from the same size series.  
DedicatedHostGroups：  
**主机组是代表专用主机集合的资源。** a collection of dedicated hosts  

使用场景：  
**将应用部署在不同物理机上，高可用，类似关联性组**  

Availability zones -> one or more datacenters  
1:1 Availability zones <-> host group  
**如果要实现跨可用区的高可用，需要创建多个 host groups**： To achieve high availability across zones, you need to create multiple host groups (one per zone) and spread your hosts accordingly.  

**创建主机组需要容错域**  
**创建主机需要分配容错域**  
**创建vm不需要任何指定**  
**不同容错域的物理机会放置到数据中心的不同的物理机架上。**  
Use Fault Domains for fault isolation  
A host can be created in a specific fault domain.  
Just like VM in a scale set or availability set, hosts in different fault domains will be placed on different physical racks in the data center.   
When you create a host group, you are required to specify the fault domain count.   
When creating hosts within the host group, you assign fault domain for each host.   
The VMs do not require any fault domain assignment.  

Fault domains are not the same as colocation. Having the same fault domain for two hosts does not mean they are in proximity with each other.  
Fault domains are scoped to the host group. You should not make any assumption on anti-affinity between two host groups (unless they are in different availability zones).  
VMs deployed to hosts with different fault domains, will have their underlying managed disks services on multiple storage stamps, to increase the fault isolation protection.  

Using Availability Zones and Fault Domains  
You can use both capabilities together to achieve even more fault isolation. In this case, you will specify the availability zone and fault domain count in for each host group, assign a fault domain to each of your hosts in the group, and assign an availability zone to each of your VMs  
The Resource Manager sample template uses zones and fault domains to spread hosts for maximum resiliency in a region.  

**自动放置允许azure为您选择合适的host放置vm。**  
**即使为主机组选择了自动放置，您仍然可以明确选择主机。**  
Manual vs. automatic placement  
When creating a VM in Azure, you can select which dedicated host to use. You can also use the option to automatically place your VMs on existing hosts, within a host group.  
When creating a new host group, make sure the setting for automatic VM placement is selected. When creating your VM, select the host group and let Azure pick the best host for your VM.  
Host groups that are enabled for automatic placement do not require all the VMs to be automatically placed. You will still be able to explicitly pick a host, even when automatic placement is selected for the host group.  

自动分配限制：  
Limitations  
Known issues and limitations when using automatic VM placement:  

You will not be able to redeploy your VM.  
You will not be able to use Lsv2, NVasv4, NVsv3, Msv2, or M-series VMs with dedicated hosts  
Virtual machine scale set support  
Virtual machine scale sets let you treat a group of virtual machines as a single resource, and apply availability, management, scaling and orchestration policies as a group. Your existing dedicated hosts can also be used for virtual machine scale sets.  

When creating a virtual machine scale set you can specify an existing host group to have all of the VM instances created on dedicated hosts.  

**主机组中创建vmss的依赖：**  
**1. 主机组和规模集必须使用相同的可用区。**  
**2. 主机组级别的容错域计数应与规模集的容错域计数相匹配。**  
The following requirements apply when creating a virtual machine scale set in a dedicated host group:  
Automatic VM placement needs to be enabled.  
The availability setting of your host group should match your scale set.  
A regional host group (created without specifying an availability zone) should be used for regional scale sets.  
The host group and the scale set must be using the same availability zone.  
The fault domain count for the host group level should match the fault domain count for your scale set. The Azure portal lets you specify max spreading for your scale set, which sets the fault domain count of 1.  
Dedicated hosts should be created first, with sufficient capacity, and the same settings for scale set zones and fault domains.  
The supported VM sizes for your dedicated hosts should match the one used for your scale set.  
Not all scale-set orchestration and optimizations settings are supported by dedicated hosts. Apply the following settings to your scale set:  

Overprovisioning is not recommended, and it is disabled by default. You can enable overprovisioning, but the scale set allocation will fail if the host group does not have capacity for all of the VMs, including the overprovisioned instances.  
Use the ScaleSetVM orchestration mode  
Do not use proximity placement groups for co-location  

Maintenance control 维护控制  
The infrastructure supporting your virtual machines may occasionally be updated to improve reliability, performance, security, and to launch new features.   
The Azure platform tries to minimize the impact of platform maintenance whenever possible, but customers with maintenance sensitive workloads can't tolerate even few seconds that the VM needs to be frozen or disconnected for maintenance.  
Maintenance Control provides customers with an option to skip regular platform updates scheduled on their dedicated hosts, then apply it at the time of their choice within a 35-day rolling window.   
Within the maintenance window, you can apply maintenance directly at the host level, in any order. Once the maintenance window is over, Microsoft will move forward and apply the pending maintenance to the hosts in an order which may not follow the user defined fault domains.  
For more information, see Managing platform updates with Maintenance Control.  

Capacity considerations 容量注意事项  
Once a dedicated host is provisioned, Azure assigns it to physical server. This guarantees the availability of the capacity when you need to provision your VM.   
Azure uses the entire capacity in the region (or zone) to pick a physical server for your host. It also means that customers can expect to be able to grow their dedicated host footprint without the concern of running out of space in the cluster.  

Quotas 配额  
There are two types of quota that are consumed when you deploy a dedicated host.  
Dedicated host vCPU quota. The default quota limit is 3000 vCPUs, per region.  
VM size family quota. For example, a Pay-as-you-go subscription may only have a quota of 10 vCPUs available for the Dsv3 size series, in the East US region.  
To deploy a Dsv3 dedicated host, you would need to request a quota increase to at least 64 vCPUs before you can deploy the dedicated host.  
To request a quota increase, create a support request in the Azure portal.  
Provisioning a dedicated host will consume both dedicated host vCPU and the VM family vCPU quota, but it will not consume the regional vCPU.  
VMs placed on a dedicated host will not count against VM family vCPU quota. Should a VM be moved off a dedicated host into a multi-tenant environment, the VM will consume VM family vCPU quota.  
Screenshot of the usage and quotas page in the portal  
For more information, see Virtual machine vCPU quotas.  
Free trial and MSDN subscriptions do not have quota for Azure Dedicated Hosts.  

Pricing 定价  
Users are charged per dedicated host, regardless how many VMs are deployed. In your monthly statement you will see a new billable resource type of hosts. The VMs on a dedicated host will still be shown in your statement, but will carry a price of 0.  
The host price is set based on VM family, type (hardware size), and region. A host price is relative to the largest VM size supported on the host.  
Software licensing, storage and network usage are billed separately from the host and VMs. There is no change to those billable items.  
For more information, see Azure Dedicated Host pricing.  
You can also save on costs with a Reserved Instance of Azure Dedicated Hosts.  

SKU 代表 vm尺寸系列和类型  
Sizes and hardware generations   
A SKU is defined for a host and it represents the VM size series and type. You can mix multiple VMs of different sizes within a single host as long as they are of the same size series.  
The type is the hardware generation. Different hardware types for the same VM series will be from different CPU vendors and have different CPU generations and number of cores.  
The sizes and hardware types vary by region. Refer to the host pricing page to learn more.  

Note 专用主机无法修改大小和类型  
Once a Dedicated host is provisoned, you can't change the size or type. If you need a different size of type, you will need to create a new host.  

Host life cycle  
Azure monitors and manages the health status of your hosts. The following states will be returned when you query your host:  
HOST LIFE CYCLE  
Health State	Description  
Host Available	There are no known issues with your host.  
Host Under Investigation	We’re having some issues with the host which we’re looking into. This is a transitional state required for Azure to try and identify the scope and root cause for the issue identified. Virtual machines running on the host may be impacted.  
Host Pending Deallocate 解除分配	Azure can’t restore the host back to a healthy state and ask you to redeploy your virtual machines out of this host. If autoReplaceOnFailure is enabled, your virtual machines are service healed to healthy hardware.   
Otherwise, your virtual machine may be running on a host that is about to fail.  
Host deallocated	All virtual machines have been removed from the host. You are no longer being charged for this host since the hardware was taken out of rotation.  

Next steps  
To deploy a dedicated host, see Deploy VMs and scale sets to dedicated hosts.  
There is a sample template that uses both zones and fault domains for maximum resiliency in a region.  
You can also save on costs with a Reserved Instance of Azure Dedicated Hosts.  

[Dedicated Host How To] (https://docs.microsoft.com/en-us/azure/virtual-machines/dedicated-hosts-how-to?tabs=portal%2Cportal2)  
**# todo 感觉还需要支持vmss**  
**# todo 文档更新谁来做？**  
Limitations  
The sizes and hardware types available for dedicated hosts vary by region. Refer to the host pricing page to learn more.  
Create a host group  
A host group is a resource that represents a collection of dedicated hosts. You create a host group in a region and an availability zone, and add hosts to it. When planning for high availability, there are additional options. You can use one or both of the following options with your dedicated hosts:  

Span across multiple availability zones. In this case, you are required to have a host group in each of the zones you wish to use.  
Span across multiple fault domains which are mapped to physical racks.  
In either case, you are need to provide the fault domain count for your host group. If you do not want to span fault domains in your group, use a fault domain count of 1.  

You can also decide to use both availability zones and fault domains.  

Portal/CLI/PowerShell  
Not all host SKUs are available in all regions, and availability zones. You can list host availability, and any offer restrictions before you start provisioning dedicated hosts.  
`az vm list-skus -l eastus2 -r hostGroups/hosts -o table`

In this example, we will use az vm host group create to create a host group using both availability zones and fault domains.  
```
az vm host group create \
   --name myHostGroup \
   -g myDHResourceGroup \
   -z 1 \
   --platform-fault-domain-count 2
```
Add the `--automatic-placement` true parameter to have your VMs and scale set instances automatically placed on hosts, within a host group. For more information, see Manual vs. automatic placement .  

Other examples  
You can also use az vm host group create to create a host group in availability zone 1 (and no fault domains).  
```
az vm host group create \
   --name myAZHostGroup \
   -g myDHResourceGroup \
   -z 1 \
   --platform-fault-domain-count 1
```
The following uses az vm host group create to create a host group by using fault domains only (to be used in regions where availability zones are not supported).
```
az vm host group create \
   --name myFDHostGroup \
   -g myDHResourceGroup \
   --platform-fault-domain-count 2
```

Create a dedicated host  
Now create a dedicated host in the host group. In addition to a name for the host, you are required to provide the SKU for the host. Host SKU captures the supported VM series as well as the hardware generation for your dedicated host.  
For more information about the host SKUs and pricing, see Azure Dedicated Host pricing.  
If you set a fault domain count for your host group, you will need to specify the fault domain for your host.  

Portal/CLI/PowerShell  
Use az vm host create to create a host. If you set a fault domain count for your host group, you will be asked to specify the fault domain for your host.  
```
az vm host create \
   --host-group myHostGroup \
   --name myHost \
   --sku DSv3-Type1 \
   --platform-fault-domain 1 \
   -g myDHResourceGroup
```

Create a VM  
Now create a VM on the host.  
Portal/CLI/PowerShell  
Create a virtual machine within a dedicated host using az vm create. If you specified an availability zone when creating your host group, you are required to use the same zone when creating the virtual machine. Replace the values like image and host name with your own.   
If you are creating a Windows VM, remove --generate-ssh-keys to be prompted for a password. # 好奇，找找这个逻辑 todo  
Portal/CLI/PowerShell  
```
az vm create \
   -n myVM \
   --image myImage \
   --host-group myHostGroup \
   --admin-username azureuser \
   --generate-ssh-keys \
   --size Standard_D4s_v3 \
   -g myDHResourceGroup \
   --zone 1
```
To place the VM on a specific host, use `--host` instead of specifying the host group with `--host-group`.

Warning  
If you create a virtual machine on a host which does not have enough resources, the virtual machine will be created in a FAILED state.  

Create a scale set  
You can also create a scale set on your host.  
Portal/CLI/PowerShell  
When you deploy a scale set using az vmss create, you specify the host group using `--host-group`. In this example, we are deploying the latest Ubuntu LTS image. To deploy a Windows image, replace the value of `--image` and remove `--generate-ssh-keys` to be prompted for a password.  
```
az vmss create \
  --resource-group myResourceGroup \
  --name myScaleSet \
  --image UbuntuLTS \
  --upgrade-policy-mode automatic \
  --admin-username azureuser \
  --host-group myHostGroup \
  --generate-ssh-keys \
  --size Standard_D4s_v3 \
  -g myDHResourceGroup \
  --zone 1
```
If you want to manually choose which host to deploy the scale set to, add `--host` and the name of the host.

# very important  
Add an existing VM  
You can add an existing VM to a dedicated host, but the VM must first be Stop\Deallocated. Before you move a VM to a dedicated host, make sure that the VM configuration is supported:  
VM 大小必须与专用主机在同一大小系列中。例如，如果您的专用主机是 DSv3，则 VM 大小可以是 Standard_D4s_v3，但不能是 Standard_A4_v2。   
The VM size must be in the same size family as the dedicated host. For example, if your dedicated host is DSv3, then the VM size could be Standard_D4s_v3, but it could not be a Standard_A4_v2.  
VM 需要与专用主机位于同一区域。  
The VM needs to be located in same region as the dedicated host.  
VM 不能是邻近置放群组的一部分。将 VM 从邻近置放群组中移除，然后再将其移动到专用主机。有关详细信息，请参阅将 VM 移出邻近置放群组 VM 不能位于可用性集中。如果 VM 位于可用区，则它必须与主机组位于同一可用区。 VM 和主机组的可用区设置必须匹配。  
The VM can't be part of a proximity placement group. Remove the VM from the proximity placement group before moving it to a dedicated host. For more information, see Move a VM out of a proximity placement group  
The VM can't be in an availability set.  
If the VM is in an availability zone, it must be the same availability zone as the host group. The availability zone settings for the VM and the host group must match.  

Portal/PowerShell    
**# todo**   
Move the VM to a dedicated host using the portal.  
Open the page for the VM.  
Select Stop to stop\deallocate the VM.  
Select Configuration from the left menu.  
Select a host group and a host from the drop-down menus.  
When you are done, select Save at the top of the page.  
After the VM has been added to the host, select Overview from the left menu.  
At the top of the page, select Start to restart the VM.  
Check the status of the host  
If you need to know how much capacity is still available on a how, you can check the status.  

Portal/CLI/PowerShell  
**查看host健康状态和余量**  
You can check the host health status and how many virtual machines you can still deploy to the host using az vm host get-instance-view.  
```
az vm host get-instance-view \
   -g myDHResourceGroup \
   --host-group myHostGroup \
   --name myHost
```

The output will look similar to this:
```json

{
  "autoReplaceOnFailure": true,
  "hostId": "6de80643-0f45-4e94-9a4c-c49d5c777b62",
  "id": "/subscriptions/10101010-1010-1010-1010-101010101010/resourceGroups/myDHResourceGroup/providers/Microsoft.Compute/hostGroups/myHostGroup/hosts/myHost",
  "instanceView": {
    "assetId": "12345678-1234-1234-abcd-abc123456789",
    "availableCapacity": {
      "allocatableVms": [
        {
          "count": 31.0,
          "vmSize": "Standard_D2s_v3"
        },
        {
          "count": 15.0,
          "vmSize": "Standard_D4s_v3"
        },
        {
          "count": 7.0,
          "vmSize": "Standard_D8s_v3"
        },
        {
          "count": 3.0,
          "vmSize": "Standard_D16s_v3"
        },
        {
          "count": 1.0,
          "vmSize": "Standard_D32-8s_v3"
        },
        {
          "count": 1.0,
          "vmSize": "Standard_D32-16s_v3"
        },
        {
          "count": 1.0,
          "vmSize": "Standard_D32s_v3"
        },
        {
          "count": 1.0,
          "vmSize": "Standard_D48s_v3"
        },
        {
          "count": 0.0,
          "vmSize": "Standard_D64-16s_v3"
        },
        {
          "count": 0.0,
          "vmSize": "Standard_D64-32s_v3"
        },
        {
          "count": 0.0,
          "vmSize": "Standard_D64s_v3"
        }
      ]
    },
    "statuses": [
      {
        "code": "ProvisioningState/succeeded",
        "displayStatus": "Provisioning succeeded",
        "level": "Info",
        "message": null,
        "time": "2019-07-24T21:22:40.604754+00:00"
      },
      {
        "code": "HealthState/available",
        "displayStatus": "Host available",
        "level": "Info",
        "message": null,
        "time": null
      }
    ]
  },
  "licenseType": null,
  "location": "eastus2",
  "name": "myHost",
  "platformFaultDomain": 1,
  "provisioningState": "Succeeded",
  "provisioningTime": "2019-07-24T21:22:40.604754+00:00",
  "resourceGroup": "myDHResourceGroup",
  "sku": {
    "capacity": null,
    "name": "DSv3-Type1",
    "tier": null
  },
  "tags": null,
  "type": null,
  "virtualMachines": [
    {
      "id": "/subscriptions/10101010-1010-1010-1010-101010101010/resourceGroups/MYDHRESOURCEGROUP/providers/Microsoft.Compute/virtualMachines/MYVM",
      "resourceGroup": "MYDHRESOURCEGROUP"
    }
  ]
}
```

Deleting hosts  
You are being charged for your dedicated hosts even when no virtual machines are deployed. You should delete any hosts you are currently not using to save costs.  
You can only delete a host when there are no any longer virtual machines using it.  

Portal/CLI/PowerShell  
Delete the VMs using az vm delete.  
`az vm delete -n myVM -g myDHResourceGroup`
After deleting the VMs, you can delete the host using az vm host delete.  
`az vm host delete -g myDHResourceGroup --host-group myHostGroup --name myHost`
Once you have deleted all of your hosts, you may delete the host group using az vm host group delete.
`az vm host group delete -g myDHResourceGroup --host-group myHostGroup`
You can also delete the entire resource group in a single command. This will delete all resources created in the group, including all of the VMs, hosts and host groups.
`az group delete -n myDHResourceGroup`

[vm-dedicated-hosts-template](https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.compute/vm-dedicated-hosts/azuredeploy.json)  

[prepare-for-dedicated-hosts](https://docs.microsoft.com/en-us/azure/virtual-machines/prepay-dedicated-hosts-reserved-instances)  
Applies to: ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets  
When you commit to a reserved instance of Azure Dedicated Hosts, you can save money. The reservation discount is applied automatically to the number of running dedicated hosts that match the reservation scope and attributes. 
You don't need to assign a reservation to a dedicated host to get the discounts. A reserved instance purchase covers only the compute part of your usage and does include software licensing costs. See the Overview of Azure Dedicated Hosts for virtual machines.  

Determine the right dedicated host SKU before you buy  
Before you buy a reservation, you should determine which dedicated host you need. A SKU is defined for a dedicated host representing the VM series and type.   

Start by going over the supported sizes for Windows virtual machine or Linux to identify the VM series.  

Next, check whether it is supported on Azure Dedicated Hosts. Azure Dedicated Hosts pricing page has the complete list of dedicated hosts SKUs, their CPU information, and various pricing options (including reserved instances).
You may find several SKUs supporting your selected VM series (with different Types). Identify the best SKU by comparing the capacity of the host (number of vCPUs).   
Note that you will be able to apply your reservation to multiple dedicated hosts SKUs supporting the same VM series (for example DSv3_Type1 and DSv3_Type2) but not across different VM series (like DSv3 and ESv3).  

Purchase restriction considerations  
Reserved instances are available for most dedicated host sizes, with some exceptions.
Reservation discounts don't apply for the following:
Clouds - Reservations aren't available for purchase in Germany or China regions.  

Insufficient quota - A reservation that is scoped to a single subscription must have vCPU quota available in the subscription for the new reserved instance.   
For example, if the target subscription has a quota limit of 10 vCPUs for DSv3-Series, then you can't buy a reservation dedicated hosts supporting this series.   
The quota check for reservations includes the VMs and dedicated hosts already deployed in the subscription. You can create quota increase request to resolve this issue.  
Capacity restrictions - In rare circumstances, Azure limits the purchase of new reservations for subset of dedicated host SKUs, because of low capacity in a region.  

Buy a reservation  
You can buy a reserved instance of an Azure Dedicated Host instance in the Azure portal.  
Pay for the reservation up front or with monthly payments. These requirements apply to buying a reserved Dedicated Host instance:  
You must be in an Owner role for at least one EA subscription or a subscription with a pay-as-you-go rate.  
For EA subscriptions, the Add Reserved Instances option must be enabled in the EA portal. Or, if that setting is disabled, you must be an EA Admin for the subscription.  
For the Cloud Solution Provider (CSP) program, only the admin agents or sales agents can buy reservations.  

To buy an instance:  
Sign in to the Azure portal.  
Select All services > Reservations.  
Select Add to purchase a new reservation and then click Dedicated Hosts.  
Enter required fields. Running Dedicated Hosts instances that match the attributes you select qualify to get the reservation discount. The actual number of your Dedicated Host instances that get the discount depend on the scope and quantity selected.  
If you have an EA agreement, you can use the Add more option to quickly add additional instances. The option isn't available for other subscription types.  

TABLE 1  
Field	Description  
Subscription	The subscription used to pay for the reservation. The payment method on the subscription is charged the costs for the reservation.   
The subscription type must be an enterprise agreement (offer numbers: MS-AZR-0017P or MS-AZR-0148P) or Microsoft Customer Agreement or an individual subscription with pay-as-you-go rates (offer numbers: MS-AZR-0003P or MS-AZR-0023P).   
The charges are deducted from the Azure Prepayment (previously called monetary commitment) balance, if available, or charged as overage.   
For a subscription with pay-as-you-go rates, the charges are billed to the credit card or invoice payment method on the subscription.  
Scope	The reservation’s scope can cover one subscription or multiple subscriptions (shared scope). If you select:  
Region	The Azure region that’s covered by the reservation.  
Dedicated Host Size	The size of the Dedicated Host instances.  
Term	One year or three years.  
Quantity	The number of instances being purchased within the reservation. The quantity is the number of running Dedicated Host instances that can get the billing discount.  
Single resource group scope — Applies the reservation discount to the matching resources in the selected resource group only.  
Single subscription scope — Applies the reservation discount to the matching resources in the selected subscription.  
Shared scope — Applies the reservation discount to matching resources in eligible subscriptions that are in the billing context. For EA customers, the billing context is the enrollment.   
For individual subscriptions with pay-as-you-go rates, the billing scope is all eligible subscriptions created by the account administrator.  
Management group — Applies the reservation discount to the matching resource in the list of subscriptions that are a part of both the management group and billing scope.  

[what-is-fault-domains](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-manage-fault-domains)
Choosing the right number of fault domains for virtual machine scale set
Applies to: ✔️ Linux VMs ✔️ Windows VMs ✔️ Uniform scale sets  

Virtual machine scale sets are created with five fault domains by default in Azure regions with no zones. 
For the regions that support zonal deployment of virtual machine scale sets and this option is selected, the default value of the fault domain count is 1 for each of the zones. 
FD=1 in this case implies that the VM instances belonging to the scale set will be spread across many racks on a best effort basis.
You can also consider aligning the number of scale set fault domains with the number of Managed Disks fault domains. 
This alignment can help prevent loss of quorum if an entire Managed Disks fault domain goes down. 
The FD count can be set to less than or equal to the number of Managed Disks fault domains available in each of the regions.

REST API
You can set the property properties.platformFaultDomainCount to 1, 2, or 3 (default of 3 if not specified). Refer to the documentation for REST API here.

Azure CLI
You can set the parameter --platform-fault-domain-count to 1, 2, or 3 (default of 3 if not specified). Refer to the documentation for Azure CLI here.
```
az vmss create \
  --resource-group myResourceGroup \
  --name myScaleSet \
  --image UbuntuLTS \
  --upgrade-policy-mode automatic \
  --admin-username azureuser \
  --platform-fault-domain-count 3\
  --generate-ssh-keys
```
It takes a few minutes to create and configure all the scale set resources and VMs.

### Test Record
`azdev test test_update_dedicated_host_e2e --live --discover`
`azdev test test_update_dedicated_host_e2e --live`

### Get All Location
location="test_location"
location="test_mc_location"
location="eastus"
location="westus"
location="westus2"
location="centralus"
location="centraluseuap"

### check quota
quota: Standard DSv3 Family vCPUs
[increase quota](https://aka.ms/ProdportalCRP/#blade/Microsoft_Azure_Capacity/CapacityExperienceBlade/Parameters/%7B%22subscriptionId%22:%220b1f6471-1bf0-4dda-aec3-cb9272f09590%22,%22command%22:%22openQuotaApprovalBlade%22,%22quotas%22:[%7B%22location%22:%22westus2%22,%22providerId%22:%22Microsoft.Compute%22,%22resourceName%22:%22standardDSv3Family%22,%22quotaRequest%22:%7B%22properties%22:%7B%22limit%22:128,%22unit%22:%22Count%22,%22name%22:%7B%22value%22:%22standardDSv3Family%22%7D%7D%7D%7D]%7D)  
[increase quota portal](https://docs.microsoft.com/en-us/azure/azure-portal/supportability/per-vm-quota-requests)

### All Commands
az group create --location {} --name {} --tag
az vm host group create -n {host-group} -c 3 -g {rg} --tags "foo=bar"
az vm host group create -n {host2-group} -c 3 -g {rg} --tags "foo=bar"
az vm host create -n {host-name} --host-group {host-group} -d 2 -g {rg} --sku DSv3-Type1 --auto-replace false --tags "bar=baz"
az vm host create -n {host2-name} --host-group {host2-group} -d 2 -g {rg} --sku DSv3-Type1 --auto-replace false --tags "bar=baz"
az vm host get-instance-view --host-group {host-group} --name {host-name} -g {rg}
az vm host get-instance-view --host-group {host2-group} --name {host2-name} -g {rg}
az vm host group get-instance-view -g {rg} -n {host-group}
az vm host group get-instance-view -g {rg} -n {host2-group}
az vm host show -g {rg} -n {host-name} --host-group {host-group}
az vm host show -g {rg} -n {host2-name} --host-group {host2-group}
az vm create -n {vm-name} --image debian -g {rg} --size Standard_D4s_v3 --host {host_id} --generate-ssh-keys --admin-username azureuser --nsg-rule NONE
az vm show -n {vm-name} -g {rg}
az vm host show --name {host-name} --host-group {host-group} -g {rg}
az vm host group show --name {host-group} -g {rg}
az vm update -n {vm-name} -g {rg} --host {host2_id}
az vm show -n {vm-name} -g {rg}
az vm host show --name {host2-name} --host-group {host2-group} -g {rg}
az vm host group show --name {host2-group} -g {rg}

az vm delete --name {vm-name} -g {rg} --yes
az vm host delete --name {host-name} --host-group {host-group} -g {rg} --yes
az vm host delete --name {host2-name} --host-group {host2-group} -g {rg} --yes
az vm host group delete --name {host-group} -g {rg} --yes
az vm host group delete --name {host2-group} -g {rg} --yes
az group delete --name {} --yes --no-wait

az vm deallocate -n ded-host-vm --no-wait -g cli_test_dedicated_host_zm2hiz7dkfz56ppsb65qdqtfc5yxsdgercsdm3whcrmnc7torvs
az vm update -n ded-host-vm -g cli_test_dedicated_host_zm2hiz7dkfz56ppsb65qdqtfc5yxsdgercsdm3whcrmnc7torvs --host /subscriptions/0b1f6471-1bf0-4dda-aec3-cb9272f09590/resourceGroups/cli_test_dedicated_host_zm2hiz7dkfz56ppsb65qdqtfc5yxsdgercsdm3whcrmnc7torvs/providers/Microsoft.Compute/hostGroups/my-host2-group/hosts/my-host2 --debug
(PropertyChangeNotAllowed) Updating Host of VM 'ded-host-vm' is not allowed as the VM is currently allocated. Please Deallocate the VM and retry the operation.
az vm start -n ded-host-vm --no-wait -g cli_test_dedicated_host_zm2hiz7dkfz56ppsb65qdqtfc5yxsdgercsdm3whcrmnc7torvs

# todo 测试其他参数影响
# todo Dynamic/Static 应该使用Static 就不会有影响。
# --host 和 --host-group 基础测试 done
# ip 会改变 pub 20.112.81.247 pvt 10.0.0.4 -> pub 20.112.87.77 pvt 10.0.0.4 
# 描述 done
# 加例子: 三个命令。done