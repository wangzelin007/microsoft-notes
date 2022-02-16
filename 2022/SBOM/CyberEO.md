Executive Order on Cyber Security 网络安全行政命令  
timeline: 2022-03-08  
[EO Contacts](https://eng.ms/docs/initiatives/executive-order/executive-order-requirements/executiveorderoncybersecurity/eocontacts)

An SBOM is a formal record containing the details and supply chain relationships of various components used in building software. Physically, an SBOM is usually a single file (such as .json) that captures this information about the software from the build.
SBOM 是一种正式记录，包含用于构建软件的各种组件的详细信息和供应链关系。从物理上讲，SBOM 通常是一个文件（例如 .json），它从构建中捕获有关软件的这些信息。

Microsoft has decided to use Software Package Data Exchange (SPDX) as its SBOM format of choice. All software produced from Microsoft will have an SPDX SBOM.
Microsoft 已决定使用软件包数据交换 (SPDX) 作为其选择的 SBOM 格式。 Microsoft 生产的所有软件都将具有 SPDX SBOM。  
[spdx](https://github.com/microsoft/dropvalidator/blob/323b0fa4ade1deb2c8c0f115e283c9ba10a6577b/Samples/manifest.spdx.json)

SBOM Signing	Not an EO requirement for March 8th	
SBOM Signature Validation	Not an EO requirement for March 8th	
Consuming 3rd-Party SBOMs	Not an EO requirement for March 8th 

CloudBuild/ADO/[OneBranch](https://dev.azure.com/onebranch/OneBranch/_build)
You’re on CloudBuild, an SBOM will be automatically be generated for each drop. Open source components detected by Component Governance will be included in the SBOM.

应该是ADO -> [ado-sbom-generator](https://eng.ms/docs/cloud-ai-platform/devdiv/one-engineering-system-1es/1es-docs/secure-supply-chain/ado-sbom-generator)
You’re on ADO, you must explicitly add ADO Manifest Generator task to your build pipelines - ADO SBOM Generator. Open source components detected by Component Governance will be included in the SBOM.

We generate an SPDX SBOM from our tool and upload it into the “SPDX Online Tool” to validate it is a good SPDX document. Upon successful validation, we are done. 
[SPDX Online Tool](https://tools.spdx.org/app/validate/)