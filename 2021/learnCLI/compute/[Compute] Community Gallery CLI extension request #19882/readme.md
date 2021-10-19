Resource Provider
Azure Compute
Description of Feature or Work Requested
We now support community sharing in Azure Shared Image Gallery. The feature allows you to share galleries with the public community, without having to use Azure RBAC sharing.
我们现在支持 Azure 共享图像库中的社区共享。该功能允许您与公共社区共享图库，而无需使用 Azure RBAC 共享。
We need to make changes in 'az sig' commands.

from sharer side:
1. create a gallery with community sharing info: az sig create --gallery-name --community-gallery-info publisherUri,publisherEmail,eual,publicNamePrefix
2. share a gallery to community: az sig update --permissions "private/groups/community"
3. reset a community gallery to private gallery(this is already done): az sig share reset (already supported)

[comment]: <> (from community side: Xing)

[comment]: <> (get community gallery/image/version:)

[comment]: <> (az sig community-gallery show --public-gallery-name --location)

[comment]: <> (az sig community-image-definition show --public-gallery-name --gallery-image-name --location)

[comment]: <> (az sig community-image-version show --public-gallery-name --gallery-image-name --gallery-image-version-name --location)

[comment]: <> (list community gallery images/versions&#40;this is rolling out, implementation of list can come after other operations&#41;)

[comment]: <> (az sig community-image-definition list --public-gallery-name --location)

[comment]: <> (az sig community-image-version list --public-gallery-name --gallery-image-name --location)

Minimum API Version Required
2021-07-01

Swagger Link
Azure/azure-rest-api-specs#16266

Target Date
before ignite
