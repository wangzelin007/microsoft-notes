issue: https://github.com/Azure/azure-cli/issues/19298
PR: 
2021-07 swagger: 

doc:
https://github.com/Azure/autorest.az/blob/master/doc/how-to-generate.md
https://github.com/Azure/autorest.az#generate-azure-cli-code

AutoRest Core	AutoRest CLI	Node.js
3.0.6370	    3.5.1	        12.20

install node js 12.20
[multi version manager](https://ourcodeworld.com/articles/read/1414/how-to-install-multiple-versions-of-nodejs-in-windows-using-node-version-manager)
switch version
nvm use 12.20.0

```shell
install virtual environment
# python -m venv env
cd ~/.autorest/@autorest_python@5.4.0/node_modules/@autorest/python/venv
source ./bin/activate // or .\Scripts\Activate.ps1 in windows
pip install azure-cli // This is must to have if for simple try out
pip install azdev // this is optional if for simple try out. 
pip install m2r
pip install mistune==0.8.4
```

install Autorest
npm install -g autorest@latest


main:
autorest --version=3.0.6370 --az --use=@autorest/az@latest <path-to-the-swagger-readme.md> --sdk-no-flatten --azure-cli-extension-folder=<path-to-the-azure-cli-extension-repo>


extension:
> autorest --version=3.0.6370 --az --use=@autorest/az@latest <path-to-the-swagger-readme.md> --sdk-no-flatten --azure-cli-extension-folder=<path-to-the-azure-cli-extension-repo>

> autorest --version=3.0.6370 --az --azure-cli-extension-folder={azure_cli_ext_folder} {swagger_folder}/specification/{service_name}/resource-manager/readme.md --tag=package-2021-07

> autorest --version=3.0.6370 --az --use=@autorest/az@latest --azure-cli-extension-folder=C:\Code\azure-cli-extensions C:\Code\azure-rest-api-specs\specification\desktopvirtualization\resource-manager\readme.md --tag=package-2021-07

> autorest --version=3.0.6370 --az --use=@autorest/az@latest --azure-cli-extension-folder=C:\Code\azure-cli-extensions C:\Code\azure-rest-api-specs\specification\desktopvirtualization\resource-manager\readme.md --tag=package-preview-2021-09

> autorest --version=3.0.6370 --az --use=@autorest/az@latest --azure-cli-extension-folder=C:\Code\azure-cli-extensions C:\Code\azure-rest-api-specs\specification\desktopvirtualization\resource-manager\readme.md --tag=package-preview-2022-02

# run this in the folder with generated code: {azure_cli_ext_folder}/src/{service_name}
> python setup.py sdist bdist_wheel
> az extension add --source={azure_cli_ext_folder}/src/{service_name}/dist/{generated .whl file}
# your az command is ready to use :)

``` shell
install code （use your azcli venv)
# cd <az-output-folder>  
cd C:\Code\azure-cli-extensions\src\desktopvirtualization
python setup.py sdist bdist_wheel 
az extension remove --name desktopvirtualization
az extension add --source=.\dist\desktopvirtualization-0.2.0-py3-none-any.whl
```


azdev test test_desktopvirtualization_scenario --discover
azdev test test_desktopvirtualization_scenario --discover --live
azdev test mymodule
azdev style desktopvirtualization
azdev linter desktopvirtualization
python scripts/ci/test_index.py -q
azdev linter --include-whl-extensions desktopvirtualization

C:\Users\zelinwang\.azdev\env_config\Code\azure-cli\env\test_index\latest.json
"test_desktopvirtualization_scenario": "c:\\code\\azure-cli-extensions\\src\\desktopvirtualization\\azext_desktopvirtualization\\tests\\latest\\test_desktopvirtualization_scenario.py"
