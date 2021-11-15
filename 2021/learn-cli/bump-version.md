- check azure-cli\src\azure-cli-core\azure\cli\core\profiles\_shared.py
- Upgrade the version in the following files:  
    1. src\azure-cli\setup.py  
    2. src\azure-cli\requirements.py3.Darwin.txt  
    3. src\azure-cli\requirements.py3.Linux.txt  
    4. src\azure-cli\requirements.py3.windows.txt  
- azdev setup --cli D:\code\azure-cli --repo D:\code\azure-cli-extensions
- pip list to check the  installed package version 
- azdev test vm --no-exitfirst
- azdev test --no-exitfirst --live --lf  

-------------------------------------------------------------------

Make sure the new api version do work in all regions  
azdev test --no-exitfirst 
Collect failed test name and files’path  
    - Check out to previous commit id  
    - Replace api version  
azdev test --no-exitfirst 
Either find related author to test or you have to replace the api version in the folder  
    - Failed test  
    - azdev test --live --lf  

------------------------------------------------------------------
--lf               : Re-run the last tests that failed.  
--no-exitfirst     : Do not exit on first error or failed test.