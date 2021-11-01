- Upgrade the version in the following files:  
    1. setup.py  
    2. requirements.py3.Darwin.txt  
    3. requirements.py3.Linux.txt  
    4. requirements.py3.windows.txt  
- azdev setup –c
- pip list to check the  installed package version 
- azdev test –no-exitfirst
- azdev test –no-exitfirst –live --lf  
Make sure the new api version do work in all regions  
azdev test –no-exitfirst  
Collect failed test name and files’path  
    - Check out to previous commit id  
    - Replace api version  
azdev test --no-existfirst  
Either find related author to test or you have to replace the api version in the folder  
    - Failed test  
    - azdev test --live --lf  

------------------------------------------------------------------
--lf               : Re-run the last tests that failed.  
--no-exitfirst     : Do not exit on first error or failed test.