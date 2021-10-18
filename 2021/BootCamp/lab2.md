nslookup
website_name
line:
clinet -> dns -> ip
firewall -> lb -> servers

1. Dynamic/Reserved public IP address
2. Direct VM access, Inbound/outbound rules for security
3. LB
4. DNS services: hosting, traffic management
5. Traffic Manager
performance, weighted, priority, geographic
性能(延迟)， 权重(比例)， 优先级(固定ip)， 地理位置(Geo绑定，服务挂了有影响)
可以同时指定多个。
www.contoso.com -> contosotm.trafficmanager.net
- contosoeast.eastus.azure.com
- contosowest.westus.azure.com
6. DDOS protection

A public IP address can be assigned directly to a network interface or to a lb.
Optionally supports specifying a DNS label.

```
# CLI
az login
az account set -s "<YourFTESubName>"
az network vnet create -g "<alias>-rg" -n "contosoads-vnet" --address-prefix 10.0.0.0/16 --subnet-name Apps --subnet-prefixes 10.0.0.0/24
az network vnet subnet create -g "<alias>-rg" --vnet-name "contosoads-vnet" -n Data --address-prefixes 10.0.1.0/24
az network vnet show -g "<alias>-rg" -n "contosoads-vnet"
az network vnet show -g "<alias>-rg" -n "contosoads-vnet" --query addressSpace
az network vnet subnet list -g "<alias>-rg" --vnet-name "contosoads-vnet" -o table

# ARM
az login
az account set -s "<YourFTESubName>"
cd "C:\StudentFiles\Introduction to Azure Networking with ARM templates"
az deployment group create -g "<alias>-rg" --template-file azuredeploy.json --parameters "alias=<alias>"
az network vnet show -g "<alias>-rg" -n "contosoads-vnet" --query addressSpace
az network vnet subnet list -g "<alias>-rg" --vnet-name "contosoads-vnet" -o table 

# Power shell
Connect-AzAccount

Set-AzContext -SubscriptionName "<YourFTESubName>"

Get-AzResourceGroup -Name <alias>-rg -ErrorVariable notPresent -ErrorAction SilentlyContinue
if ($notPresent)
{
    New-AzResourceGroup -Name <alias>-rg -Location "Central Us"
}

$appsSubnet = New-AzVirtualNetworkSubnetConfig -Name apps -AddressPrefix "10.0.0.0/24"
$dataSubnet  = New-AzVirtualNetworkSubnetConfig -Name data  -AddressPrefix "10.0.1.0/24"

$virtualNetwork = New-AzVirtualNetwork -ResourceGroupName <alias>-rg -Location CentralUs -Name contosoads-vnet -AddressPrefix 10.0.0.0/16 -Subnet $appsSubnet,$dataSubnet

Verify:
$virtualNetwork
$virtualNetwork.AddressSpace
$virtualNetwork.Subnets
```

LB 3/4/7
3 IP source/dest IP addresses
