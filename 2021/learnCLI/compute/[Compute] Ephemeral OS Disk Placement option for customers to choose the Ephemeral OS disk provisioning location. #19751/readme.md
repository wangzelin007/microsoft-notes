Updates should be like  
For az vmss create, az vm create cmds, currently we have param called [--ephemeral-os-disk {false, true}] ,  
we should have another param called that goes together with this is [--ephemeral-os-disk-placement {CacheDisk,ResourceDisk}]  
which customer can set when customer selected the ephemeral-os-disk value as true.  
我们应该有另一个与此一起调用的参数是 [--ephemeral-os-disk-placement {CacheDisk,ResourceDisk}]，当客户将 ephemeral-os-disk 值选择为 true 时，客户可以设置该参数。  
如果设置CacheDisk 即使用缓存，In portal it shows with **OS cache placement**.
如果设置ResourceDisk 即使用本地磁盘, 需要保证 resourceDiskSizeInMb 足够大, In portal it shows with **Temp disk placement**.  

If a VM has sufficient cache and temp space, you will now also be able to specify where you want to store the ephemeral OS Disk by using a new property called DiffDiskPlacement  
如果 VM 有足够的缓存和临时空间，您现在还可以使用名为 DiffDiskPlacement 的新属性指定要存储临时 OS 磁盘的位置  
--ephemeral-os-disk-placement == DiffDiskPlacement  

```
    --ephemeral-os-disk                  [Preview] : Allows you to create an OS disk
                                                     directly on the host node, providing local disk
                                                     performance and faster VM/VMSS reimage time.
                                                     Allowed values: false, true.
        Argument '--ephemeral-os-disk' is in preview and under development. Reference and
        support levels: https://aka.ms/CLI_refstatus
```

swagger link PR: https://github.com/Azure/azure-rest-api-specs/pull/8847

Default: Ephemeral OS disk will be placed in the CacheDisk if one is configured for the VM size otherwise ResourceDisk is used,  
默认值：如果为 VM 大小配置了一个临时 OS 磁盘，则会将其放置在 CacheDisk 中，否则将使用 ResourceDisk  
refer to VM size documentation for Windows VM at https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes and  
Linux VM at https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes to check which VM sizes exposes a cache disk.  
------------------------------------------
[sizes](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes)  

|Type|Size|Description|
|---|---|---|
|General purpose|B, Dsv3, Dv3, Dasv4, Dav4, DSv2, Dv2, Av2, DC, DCv2, Dv4, Dsv4, Ddv4, Ddsv4|Balanced CPU-to-memory ratio. Ideal for testing and development, small to medium databases, and low to medium traffic web servers.|
|Compute optimized|F, Fs, Fsv2, FX|High CPU-to-memory ratio. Good for medium traffic web servers, network appliances, batch processes, and application servers.|
|Memory optimized|Esv3, Ev3, Easv4, Eav4, Ev4, Esv4, Edv4, Edsv4, Mv2, M, DSv2, Dv2|High memory-to-CPU ratio. Great for relational database servers, medium to large caches, and in-memory analytics.|
|Storage optimized|Lsv2|High disk throughput and IO ideal for Big Data, SQL, NoSQL databases, data warehousing and large transactional databases.|
|GPU|NC, NCv2, NCv3, NCasT4_v3, ND, NDv2, NV, NVv3, NVv4|Specialized virtual machines targeted for heavy graphic rendering and video editing, as well as model training and inferencing (ND) with deep learning. Available with single or multiple GPUs.|
|High performance compute|HB, HBv2, HBv3, HC, H|Our fastest and most powerful CPU virtual machines with optional high-throughput network interfaces (RDMA).|

[ephemeral-os-disks](https://docs.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks#size-requirements)  
Ephemeral 短暂的 -> 临时的  
Ephemeral OS disks are created on the local virtual machine (VM) storage and not saved to the remote Azure Storage.  
Ephemeral OS disks work well for stateless 无状态 workloads, where applications are tolerant of individual VM failures,  
but are more affected by VM deployment time or reimaging the individual VM instances. With Ephemeral OS disk,  
you get lower read/write latency 延迟 to the OS disk and faster VM reimage.  

The key features of ephemeral disks are:
1. Ideal for stateless applications.
2. They can be used with both Marketplace and custom images.
3. Ability to fast reset or reimage VMs and scale set instances to the original boot state.
4. Lower latency, similar to a temporary 临时 disk.
5. Ephemeral OS disks are free, you incur 导致 no storage cost for OS disk.
6. They are available in all Azure regions.
7. Ephemeral OS Disk is supported by Shared Image Gallery.

Premium 优质的  
Specialized 专门  
preserved 保存  
provisioned 提供  
denoted 表示  
insufficient 不足的  
greyed out 变灰  

Ephemeral disks also require that the VM size supports Premium storage.  
The sizes usually (but not always) have an s in the name, like DSv2 and EsV3.  
For more information, see Azure VM sizes for details around which sizes support Premium storage.  

Ephemeral OS Disks can now be stored on VM temp/resource disk in addition to the VM cache.  
除了 VM 缓存之外，临时 OS 磁盘现在还可以存储在 VM 临时资源磁盘上。  

CLI
To use an ephemeral disk for a CLI VM deployment, set the --ephemeral-os-disk parameter in az vm create to true and the --os-disk-caching parameter to ReadOnly.
```shell
az vm create \
  --resource-group myResourceGroup \
  --name myVM \
  --image UbuntuLTS \
  --ephemeral-os-disk true \
  --os-disk-caching ReadOnly \
  --admin-username azureuser \
  --generate-ssh-keys

az vmss create \
  --resource-group myResourceGroup \
  --name myVM \
  --image UbuntuLTS \
  --ephemeral-os-disk true \
  --os-disk-caching ReadOnly \
  --admin-username azureuser \
  --generate-ssh-keys
```

Q: What is the size of the local OS Disks?  
A: We support platform and custom images, up to the VM cache size, where all read/writes to the OS disk will be local on the same node as the Virtual Machine.  
答：我们支持平台和自定义映像，最高可达 VM 缓存大小，其中对 OS 磁盘的所有读写都将在与虚拟机相同的节点上进行。  

Q: Will all VM sizes be supported for ephemeral OS disks?  
A: No, most Premium Storage VM sizes are supported (**DS, ES, FS, GS, M**, etc.). To know whether a particular VM size supports ephemeral OS disks, you can:  
```shell
$vmSizes=Get-AzComputeResourceSku | where{$_.ResourceType -eq 'virtualMachines' -and $_.Locations.Contains('CentralUSEUAP')} 

foreach($vmSize in $vmSizes)
{
   foreach($capability in $vmSize.capabilities)
   {
       if($capability.Name -eq 'EphemeralOSDiskSupported' -and $capability.Value -eq 'true')
       {
           $vmSize
       }
   }
}
```

**调用逻辑：**
```
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\commands.py
g.custom_command('create', 'create_vm', transform=transform_vm_create_output, supports_no_wait=True, table_transformer=deployment_validate_table_format, validator=process_vm_create_namespace, exception_handler=handle_template_based_exception)
g.custom_command('create', 'create_vmss', transform=DeploymentOutputLongRunningOperation(self.cli_ctx, 'Starting vmss create'), supports_no_wait=True, table_transformer=deployment_validate_table_format, validator=process_vmss_create_namespace, exception_handler=handle_template_based_exception)
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\_validators.py
def process_vm_create_namespace(cmd, namespace):
    _validate_vm_create_storage_profile(cmd, namespace)
def process_vmss_create_namespace(cmd, namespace):
    _validate_vm_create_storage_profile(cmd, namespace, for_scale_set=True)

def _validate_vm_create_storage_profile(cmd, namespace, for_scale_set=False):
    namespace.disk_info = normalize_disk_info(size=vm_size,
                                              image_data_disks=image_data_disks,
                                              data_disk_sizes_gb=namespace.data_disk_sizes_gb,
                                              attach_data_disks=getattr(namespace, 'attach_data_disks', []),
                                              storage_sku=namespace.storage_sku,
                                              os_disk_caching=namespace.os_caching,
                                              data_disk_cachings=namespace.data_caching,
                                              ephemeral_os_disk=getattr(namespace, 'ephemeral_os_disk', None),
                                              data_disk_delete_option=getattr(
                                                  namespace, 'data_disk_delete_option', None))
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\_vm_utils.py
def normalize_disk_info(ephemeral_os_disk=False):
    # update os diff disk settings
    if ephemeral_os_disk:
        info['os']['diffDiskSettings'] = {'option': 'Local'}
        # local os disks require readonly caching, default to ReadOnly if os_disk_caching not specified.
        if not os_disk_caching:
            os_disk_caching = 'ReadOnly'
```

**modify**
```python
# 默认值：如果为 VM 大小配置了一个临时 OS 磁盘，则会将其放置在 CacheDisk 中，否则将使用 ResourceDisk  
def normalize_disk_info(ephemeral_os_disk=False, ephemeral_os_disk_placement=False):
    # update os diff disk settings
    if ephemeral_os_disk:
        info['os']['diffDiskSettings'] = {'option': 'Local'}
        # local os disks require readonly caching, default to ReadOnly if os_disk_caching not specified.
        if not os_disk_caching:
            os_disk_caching = 'ReadOnly'
        if ephemeral_os_disk_placement:
            info['os']['diffDiskSettings']['placement'] = ephemeral_os_disk_placement # ["ResourceDisk", "CacheDisk"]
# help 需要加上依赖说明，依赖 ephemeral_os_disk done
# validate 需要加上校验，必须提供 ephemeral_os_disk 参数 todo
# message = 'Secret is missing vaultCertificates array or it is empty at index 0'
# with self.assertRaisesRegexp(CLIError, message):
# vm create -g {rg} -n {vm_2} --image {image} --ssh-key-value '{ssh_key}' --location {loc} --ephemeral-os-disk-placement {placement2} --os-disk-caching ReadOnly --admin-username {user} --nsg-rule NONE
# 仅支持 enum ["ResourceDisk", "CacheDisk"] done
# 把关联的 test_vm_create_ephemeral_os_disk 也跑一下 done
```
```json
# example
D:\code\azure-rest-api-specs\specification\compute\resource-manager\Microsoft.Compute\stable\2021-07-01\examples\compute\CreateAVmWithADiffOsDiskUsingDiffDiskPlacementAsResourceDisk.json
"osDisk": {
  "osType": "Windows",
  "caching": "ReadOnly",
  "diffDiskSettings": {
    "option": "Local",
    "placement": "ResourceDisk"
  },
"osDisk": {
  "caching": "ReadOnly",
  "diffDiskSettings": {
    "option": "Local",
    "placement": "ResourceDisk"
  },
"osDisk": {
  "osType": "Windows",
  "caching": "ReadOnly",
  "diffDiskSettings": {
    "option": "Local",
    "placement": "ResourceDisk"
  },
D:\code\azure-rest-api-specs\specification\compute\resource-manager\Microsoft.Compute\stable\2021-07-01\examples\compute\CreateAVmWithADiffOsDiskUsingDiffDiskPlacementAsCacheDisk.json
"osDisk": {
            "caching": "ReadOnly",
            "diffDiskSettings": {
              "option": "Local",
              "placement": "CacheDisk"
            },
"osDisk": {
              "osType": "Windows",
              "caching": "ReadOnly",
              "diffDiskSettings": {
                "option": "Local",
                "placement": "CacheDisk"
              },
"osDisk": {
              "osType": "Windows",
              "caching": "ReadOnly",
              "diffDiskSettings": {
                "option": "Local",
                "placement": "CacheDisk"
              },
D:\code\azure-rest-api-specs\specification\compute\resource-manager\Microsoft.Compute\stable\2021-07-01\examples\compute\CreateAScaleSetWithDiffOsDiskUsingDiffDiskPlacement.json
"osDisk": {
              "caching": "ReadOnly",
              "diffDiskSettings": {
                "option": "Local",
                "placement": "ResourceDisk"
              },
"osDisk": {
                "caching": "ReadOnly",
                "diffDiskSettings": {
                  "option": "Local",
                  "placement": "ResourceDisk"
                },
"osDisk": {
                "caching": "ReadOnly",
                "diffDiskSettings": {
                  "option": "Local",
                  "placement": "ResourceDisk"
                },
```

**rest api spec**
```buildoutcfg
"DiffDiskPlacement": {
      "type": "string",
      "description": "Specifies the ephemeral disk placement for operating system disk. This property can be used by user in the request to choose the location i.e, cache disk or resource disk space for Ephemeral OS disk provisioning. For more information on Ephemeral OS disk size requirements, please refer Ephemeral OS disk size requirements for Windows VM at https://docs.microsoft.com/azure/virtual-machines/windows/ephemeral-os-disks#size-requirements and Linux VM at https://docs.microsoft.com/azure/virtual-machines/linux/ephemeral-os-disks#size-requirements",
      "enum": [
        "CacheDisk",
        "ResourceDisk"
      ],
      "x-ms-enum": {
        "name": "DiffDiskPlacement",
        "modelAsString": true
      }
    },
"DiffDiskSettings": {
      "properties": {
        "option": {
          "$ref": "#/definitions/DiffDiskOption",
          "description": "Specifies the ephemeral disk settings for operating system disk."
        },
        "placement": {
          "$ref": "#/definitions/DiffDiskPlacement",
          "description": "Specifies the ephemeral disk placement for operating system disk.<br><br> Possible values are: <br><br> **CacheDisk** <br><br> **ResourceDisk** <br><br> Default: **CacheDisk** if one is configured for the VM size otherwise **ResourceDisk** is used.<br><br> Refer to VM size documentation for Windows VM at https://docs.microsoft.com/azure/virtual-machines/windows/sizes and Linux VM at https://docs.microsoft.com/azure/virtual-machines/linux/sizes to check which VM sizes exposes a cache disk."
        }
      },
      "description": "Describes the parameters of ephemeral disk settings that can be specified for operating system disk. <br><br> NOTE: The ephemeral disk settings can only be specified for managed disk."
    },
```

**如何指定有依赖关系的argument？**
`c.argument('use_unmanaged_disk', action='store_true', help='Do not use managed disk to persist VM')`
`c.argument('storage_account', help="Only applicable when used with `--use-unmanaged-disk`. The name to use when creating a new storage account or referencing an existing one. If omitted, an appropriate storage account in the same resource group and location will be used, or a new one will be created.")`
`c.argument('storage_container_name', help="Only applicable when used with `--use-unmanaged-disk`. Name of the storage container for the VM OS disk. Default: vhds")`

**如何指定有排斥关系的argument？**
required = ['os_type', 'attach_os_disk', 'use_unmanaged_disk']
forbidden = ['os_disk_name', 'os_caching', 'image', 'storage_account', 'ephemeral_os_disk',
                     'storage_container_name', 'data_disk_sizes_gb', 'storage_sku'] + auth_params

**error**
```
azure.cli.core.azclierror.DeploymentError: 
{
  "status": "Failed",
  "error": {
    "code": "DeploymentFailed",
    "message": "At least one resource deployment operation failed. Please list deployment operations for details. Please see https://aka.ms/DeployOperations for usage details.",
    "details": [
      {
        "code": "BadRequest",
        "message": {
            "error": {
                "code": "NotSupported",
                "message": "OS disk of Ephemeral VM with size greater than 7 GB is not allowed for VM size Standard_DS1_v2 when the DiffDiskPlacement is ResourceDisk."
          }
        }
      }
    ]
  }
}
```

**try DS, ES, FS, GS, M**
1. OS disk of Ephemeral VM with size greater than 7 GB is not allowed for VM size Standard_DS1_v2 when the DiffDiskPlacement is ResourceDisk.
use `--size Standard_D4s_v2` to specify vm size  
use `--vm-sku Standard_DS4_v2` to specify vmss size
default is `Standard_DS1_v2 7168MB`
`Standard_DS4_v2 57344MB`
```
az vm list-sizes -l westus
--size Standard_D4s_v3
  {
    "maxDataDiskCount": 64,
    "memoryInMb": 2048000,
    "name": "Standard_M128",
    "numberOfCores": 128,
    "osDiskSizeInMb": 1047552,
    "resourceDiskSizeInMb": 16384000
  },
  {
    "maxDataDiskCount": 64,
    "memoryInMb": 3891200,
    "name": "Standard_M128m",
    "numberOfCores": 128,
    "osDiskSizeInMb": 1047552,
    "resourceDiskSizeInMb": 16384000
  },
    {
    "maxDataDiskCount": 64,
    "memoryInMb": 5836800,
    "name": "Standard_M416-208s_v2",
    "numberOfCores": 416,
    "osDiskSizeInMb": 1047552,
    "resourceDiskSizeInMb": 8388608
  },
  {
    "maxDataDiskCount": 64,
    "memoryInMb": 5836800,
    "name": "Standard_M416s_v2",
    "numberOfCores": 416,
    "osDiskSizeInMb": 1047552,
    "resourceDiskSizeInMb": 8388608
  },
  {
    "maxDataDiskCount": 64,
    "memoryInMb": 11673600,
    "name": "Standard_M416-208ms_v2",
    "numberOfCores": 416,
    "osDiskSizeInMb": 1047552,
    "resourceDiskSizeInMb": 8388608
  },
  {
    "maxDataDiskCount": 64,
    "memoryInMb": 11673600,
    "name": "Standard_M416ms_v2",
    "numberOfCores": 416,
    "osDiskSizeInMb": 1047552,
    "resourceDiskSizeInMb": 8388608
  }
```

**help**
```
trade-off
  - name: Create a VMSS choose the Ephemeral OS disk provisioning location.
    text: >
        az vmss create -n MyVmss -g MyResourceGroup --image {image} --vm-sku Standard_DS4_v2 --ephemeral-os-disk --ephemeral-os-disk-placement ResourceDisk
        az vmss create -n MyVmss -g MyResourceGroup --image {image} --ephemeral-os-disk --ephemeral-os-disk-placement CacheDisk 
  - name: Create a VM choose the Ephemeral OS disk provisioning location.
    text: >
        az vm create -n MyVm -g MyResourceGroup --image {image} --size Standard_DS4_v2 --location {loc} --ephemeral-os-disk --ephemeral-os-disk-placement ResourceDisk
        az vm create -n MyVm -g MyResourceGroup --image {image} --location {loc} --ephemeral-os-disk --ephemeral-os-disk-placement CacheDisk
```