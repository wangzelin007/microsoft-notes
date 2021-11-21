一次安装 extension 找不到依赖的问题记录  
az: ['install', '--target', 'C:\\Users\\zelinwang\\.azure\\cliextensions\\k8sconfiguration', 'C:\\Users\\ZELINW~1\\AppData\\Local\\Temp\\tmps37w1529\\k8sconfiguration-0.2.4-py3-none-any.whl']  
az extension add -n k8sconfiguration --debug  
az extension remove -n k8sconfiguration  
pip list --path C:\Users\zelinwang\.azure\cliextensions\k8sconfiguration  
pip show -f pycryptodome 只会查找默认目录下的

azdev:  
pip install -e C:\Code\azure-cli-extensions\src\k8sconfiguration  