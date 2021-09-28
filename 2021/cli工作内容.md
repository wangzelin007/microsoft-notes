1. cli 代码编写，主要涉及三个库：  
    azure-cli 最主要的  
    azure-cli-extensions 很少提交  
    azure-cli-dev-tools 很少提交  
2. cli test  
    azure-cli-extensions/src/command_modules/azure-cli-**[module name]**/tests  
3. cli help  
    感觉弃用了？  
    推荐使用 yaml 方式，src/command_modules/azure-cli-**[module name]**/azure/cli/command_modules/**[module name]**/help.yaml  
    注意 title 是自动生成，需要改 https://github.com/Azure/azure-docs-cli/blob/master/titleMapping.json  
    ---------------------
    2021/azure-cli/src/azure-cli/azure/cli/command_modules/natgateway/_help.py  
    2021/azure-cli/src/azure-cli/azure/cli/command_modules/natgateway/tests  

问题：  
1. core 和 extension
core 是正规版本，严格遵循发布时间，上线后需要遵循启用流程，不能随意更改。
extension 包含实验性功能，比较灵活。

找一个最小的模块学习：
1. 如果查看每个目录下的代码量？
```shell
#!/bin/bash  
for i in `ls`;  
do   
echo $i `find $i -name "*.py"|xargs cat|grep -v ^$|wc -l` ;  
done 
```
2. 学习 cloud 模块 350 行代码
3. 学习 azure-cli 整体架构

-------
1. Check code style (Pylint and PEP8):
    ```
    azdev style <extension-name/module-name>
    ```
2. Run static code checks of the CLI command table:
    ```
    azdev linter <extension-name/module-name>
    ```
3. Record or replay CLI tests:
    ```
    azdev test <extension-name/module-name>
    ```
----------
init  
git clone https://github.com/<your-github-name>/azure-cli.git  
cd azure-cli  
git remote add upstream https://github.com/Azure/azure-cli.git  
git remote -v  

python3 -m venv env3  
. env3/bin/activate  
deactivate  

pip install azdev -q  
azdev --version  
azdev setup -h  
az -h  
az --version  
azdev extension list -0 table  
azdev extension add azure-firewall  
az network firewall -h  

azdev -h  
azdev test redis  
azdev test -h  
azdev style redis  
azdev style redis cdn  
azdev linter redis  

azdev cli create -h  
azdev cli create test1 --required-sdk azure-mgmt-maps==0.1.0 --operation-name AccountsOperations --client-name MapsManagementClient --sdk-property account_name --github-alias wangzelin007  
az test1 -h  

azdev extension create -h  
azdev extension create test2 --local-sdk azure-mgmt-maps-0.1.0/ --operation-name AccountsOperations --client-name MapsManagementClient --sdk-property account_name --github-alias wangzelin007  
az test2 -h  

.azdev/env_config/Users/wangzelin/opt/anacode3/envs/py38/config  
```
[defaults]
storage_account = xxx
storage_container = extensions
storage_subscription = xxx
```
azdev extension publish test2 --update-index  
az login  

[comment]: <> (git fetch upstream)
[comment]: <> (git branch dev --set-upstream-to upstream/dev)
[comment]: <> (git checkout -b <feature_branch>)