SBOM Generation
An SBOM can be generated on ADO, CloudBuild, and custom build environments.

Generating SBOMs on ADO: [ADO Manifest Generator](https://eng.ms/docs/cloud-ai-platform/devdiv/one-engineering-system-1es/1es-docs/secure-supply-chain/ado-sbom-generator)
Generating SBOMs on CloudBuild: [Signed Build Manifest](https://eng.ms/docs/cloud-ai-platform/devdiv/one-engineering-system-1es/1es-build/cloudbuild/security/cloudbuild-sbom-generator)
Generating SBOMs in custom Windows-based build environments: [ManifestTool.exe](https://eng.ms/docs/cloud-ai-platform/devdiv/one-engineering-system-1es/1es-docs/secure-supply-chain/custom-sbom-generation-workflows)
Generating SBOMs in custom Linux/Mac-based build environments: [ManifestTool.dll](https://eng.ms/docs/cloud-ai-platform/devdiv/one-engineering-system-1es/1es-docs/secure-supply-chain/custom-sbom-generation-workflows)

What is the purpose of an SBOM?
One of the core expected scenarios is for enterprise organizations (e.g. Governments, Fortune 500 companies) to use SBOMs to do vulnerability lookups of the open source components embedded within. This gives organizations a better view into their true risk profile (shown below). OWASP created an open source tool, DependencyTrack, that does this.
开源漏洞查找 [DependencyTrack](https://dependencytrack.org/)

Can I share an SBOM with an external customer?
You may share your "manifest.spdx.json" file with customers. 
You CANNOT share the "bsi.json" or the "manifest.cat" files as these are intended for internal use only. 
You can include the manifest.spdx.json within the released bits as a way of transferring the SBOM from producer to consumer (ideal for on-prem software).

How to find sbom:
drop/_manifest/spdx_2.2/manifest.spdx.json

Why doesn't the SBOM include information about package dependencies?
Any open source used in your build must be detectable by Component Governance (OSS detection capabilities listed here). If you have OSS that isn't detectable by Component Governance, you must include a cgmanifest.json in your repository to tell Component Governance what OSS you are using - more info on this here.  
对于我们不自动检测的任何第 3 方软件，您需要声明它。 
为此，您必须创建一个 cgmanifest.json 文件并将其存储在您的存储库中。 
在 cgmanifest.json 中列出第 3 方软件，然后我们的 SBOM 工具将包含它。
[cgmanifest.json.example](https://dev.azure.com/mseng/AzureDevOps/_git/Governance.Specs?path=%2Fcgmanifest.json&_a=contents&version=GBmaster)  
```json
{"Registrations":[ 
    {
      "component": { 
       "type": "git", 
       "git": { 
         "repositoryUrl": "https://git.contoso.org/contoso-repo-1.3", 
         "commitHash": "a9ca2c9f4e1e0061075aa47cbb97201a43b0f66f" 
         }
       }
    },
    {
      "Component": {
         "Type": "npm",
         "Npm": {
           "Name": "growl",
           "Version": "1.10.2"
         }
       }
    },
    {
      "Component": {
         "Type": "Pip",
         "Pip": {
           "Name": "pandas",
           "Version": "0.23.4"
         }
       }
    },
    {
       "Component": {
         "Type": "other",
         "Other": {
           "Name": "example",
           "Version": "1.2.4",
           "DownloadUrl": "https://contoso.com/example.tar.gz"
         }
       }
    },
     {
      "Component": {
         "Type": "NuGet",
         "NuGet": {
           "Name": "Newtonsoft.Json",
           "Version": "1.10.2"
         }
       }
    },
      {
      "Component": {
         "Type": "Cargo",
         "Cargo": {
           "Name": "CargoPackage",
           "Version": "1.1.2"
         }
       }
    },
     {
      "Component": {
         "Type": "RubyGems",
         "RubyGems": {
           "Name": "gem",
           "Version": "3.1.0"
         }
       }
    },
     {
      "Component": {
         "Type": "Maven",
         "Maven": {
           "ArtifactId": "component.Maven.ArtifactId",
           "GroupId": "component.Maven.GroupId",
           "Version": "1.0.0"
         }
       }
    },
    {
      "Component": {
         "Type": "Go",
         "Go": {
           "Name": "GoComponent",
           "Version": "1.0.0"
         }
       }
    },
    {
      "Component": {
         "Type": "Pod",
         "Pod": {
           "Name": "AzureCore",
           "Version": "0.5.0"
         }
       }
    }
 ],
 "Version": 1
}
```

[include SBOMs as part of installers](https://microsoft.sharepoint.com/:w:/t/1ES2/EWbw3UkW7nhMpypzZe_kzPAB7IraUUkwhTnG9eyCLwm9ng?e=XMNC2i)
For windows

[pipeline assignments](https://msit.powerbi.com/groups/me/apps/f12906b3-7c40-4182-93ea-5e8bf157e544/reports/5ed32b93-08a8-4810-9904-a10d0e6e737d/ReportSection313b1107c0c30a37ca29?ctid=72f988bf-86f1-41af-91ab-2d7cd011db47&language=en-US)
[last mapped SBOMs](https://msit.powerbi.com/groups/me/apps/f12906b3-7c40-4182-93ea-5e8bf157e544/reports/5ed32b93-08a8-4810-9904-a10d0e6e737d/ReportSectiona4ffc51b61ad23911a78?ctid=72f988bf-86f1-41af-91ab-2d7cd011db47&language=en-US)

For ADO and GitHub repos, go to Product Catalog and manually map the pipeline generating the SBOM to your service. To do so, follow the steps [here](https://eng.ms/docs/cloud-ai-platform/devdiv/one-engineering-system-1es/1es-docs/product-catalog/how-to/assign-classify-engineering-artifacts#build-pipelines). Changes will be reflected in 24 hours.

BuildPythonWheel
DownloadPipelineArtifact@1
 
Q1:
最终生成的manifest.spdx.json 需要放到哪里 TODO
The Manifest Generator task should be positioned after the build step, but before the Publish/Deploy step.


Build 里面要加两个

- job: Test SBOM
  displayName: Test Python Wheels

  dependsOn: BuildPythonWheel
  condition: succeeded()
  pool:
    vmImage: 'ubuntu-20.04'
  steps:
  - task: AzureArtifacts.manifest-generator-task.manifest-generator-task.ManifestGeneratorTask@0
    displayName: 'SBOM'
    inputs:
      BuildDropPath: '$(System.ArtifactsDirectory)/buildOutput'
      PackageName: 'Azure Cli'
      PackageVersion: '2.33.0'

- task: AzureArtifacts.manifest-generator-task.manifest-generator-task.ManifestGeneratorTask@0
  displayName: 'SBOM'
  inputs:
    BuildDropPath: '$(System.ArtifactsDirectory)/buildOutput'
    PackageName: 'Azure Cli'
    PackageVersion: '2.33.0'

- task: AzureArtifacts.manifest-generator-task.manifest-generator-task.ManifestGeneratorTask@0
  displayName: 'SBOM for docker'
  inputs:
    BuildDropPath: '$(System.ArtifactsDirectory)/buildOutput'
    DockerImagesToScan: 'ubuntu:16.04, 56bab49eef2ef07505f6a1b0d5bd3a601dfc3c76ad4'

打开sign放哪里不清楚 TODO 猜测是放到打包里？
variables:
  Packaging.EnableSBOMSigning: true
BuildDropPath: '$(System.ArtifactsDirectory)/buildOutput' -> 路径确认 TODO
DockerImagesToScan: 'ubuntu:16.04, 56bab49eef2ef07505f6a1b0d5bd3a601dfc3c76ad4' -> 怎么拿到id呢 TODO


$(Build.ArtifactStagingDirectory)
'$(Build.ArtifactStagingDirectory)/metadata'
'build_scripts/windows/out/'
'$(Build.ArtifactStagingDirectory)/msi'
'$(Build.ArtifactStagingDirectory)/docker'
'$(Build.ArtifactStagingDirectory)/pypi'
'$(Build.ArtifactStagingDirectory)/homebrew'
'$(Build.ArtifactStagingDirectory)/yum'
'$(Build.ArtifactStagingDirectory)/debian'

AzureAD/microsoft-authentication-library-for-python
AzureAD/azure-activedirectory-library-for-python

1. manifest.spdx.json 需要跟随包一起发布出去嘛？
2. manifest.spdx.json 最终存放位置，需要给那些人？
3. 如何和 power bi 绑定起来，识别到？
4. 多个包是否需要打出来多个 还是可以公用一个？

- [] system diagnosis 开启
- [] 修改requirements.txt 如果支持pip
- [] 如何拆分 build 和 package