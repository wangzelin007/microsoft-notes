**Azure Resource Manager**
Moving Resources
https://aka.ms/immovableservices

**Identity**
Azure Subscription 1: n Resource Groups 1: n Resources
Authentication & Authorization
Azure Active Directory [Users, Groups, Service Principals]

Role [read, write, delete]
Scope: A set of resources that access applies to.

RBAC: Role Based Access Control
Manage which users or groups can perform which actions on which resources.

ARM Policies:
Manage what resources or configurations are available at the subscription, resource group or resource level.

**arm template**
incremental: RM leaves unchanged resources that exist in the rg but are not specified in the template.
complete: RM deletes resources that exist in the rg but are not specified in the template.

**VS code**
ctrl + P
ext install powershell
