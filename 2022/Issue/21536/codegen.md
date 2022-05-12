cd ~/.autorest/@autorest_python@5.4.0/node_modules/@autorest/python/venv
.\Scripts\Activate.ps1

提示缺少参数，需要补充：
readme.az.md
参考：
https://github.com/Azure/azure-rest-api-specs/pull/18669

- ERROR: Schema violation: Additional properties not allowed: x-ms-identifiers
--pass-thru:schema-validator-swagger

> autorest --version=3.0.6370 --az C:\Code\azure-rest-api-specs\specification\healthcareapis\resource-manager\readme.md --use=@autorest/az@latest --azure-cli-extension-folder=C:\Code\azure-cli-extensions --tag=package-2021-11 --pass-thru:schema-validator-swagger


> cd C:\Code\azure-cli-extensions\src\healthcareapis
python setup.py sdist bdist_wheel 
az extension remove --name healthcareapis
az extension add --source=.\dist\healthcareapis-0.2.0-py3-none-any.whl

``` shell
install code （use your azcli venv)
# cd <az-output-folder>  
cd C:\Code\azure-cli-extensions\src\healthcareapis
python setup.py sdist bdist_wheel 
az extension remove --name healthcareapis
az extension add --source=.\dist\healthcareapis-0.4.0-py3-none-any.whl
```

azdev test healthcareapis --discover
azdev test healthcareapis --discover --live
azdev style healthcareapis
azdev linter healthcareapis
python scripts/ci/test_index.py -q
azdev linter --include-whl-extensions healthcareapis

C:\Users\zelinwang\.azdev\env_config\Code\azure-cli\env\test_index\latest.json
"test_healthcareapis_scenario": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py"

"test_healthcare_acr": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_acr", "test_healthcare_parameter": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_parameter", "test_healthcare_service": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_service", "test_healthcare_private": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_private", "test_healthcare_workspace": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_workspace", "test_healthcare_workspace_dicom": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_workspace_dicom", "test_healthcare_workspace_fhir": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_workspace_fhir", "test_healthcare_workspace_iot_connector": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_workspace_iot_connector", "test_healthcare_workspace_private": "c:\\code\\azure-cli-extensions\\src\\healthcareapis\\azext_healthcareapis\\tests\\latest\\test_healthcareapis_scenario.py::HealthcareApisScenarioTest::test_healthcare_workspace_private"

https://login.microsoftonline.com/