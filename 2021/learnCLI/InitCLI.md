   1. pip install azdev
   2. azdev setup --cli D:\code\azure-cli --repo D:\code\azure-cli-extensions

**problem**
```
log:
subprocess.CalledProcessError: Command '['C:\\Users\\zelinwang\\Anaconda3\\envs\\azure-msal\\Scripts\\python', '-m', 'pip', 'install', '--upgrade', 'pip']' returned non-zero exit status 1
fix:
copy C:\Users\zelinwang\Anaconda3\envs\azure-msal\python.exe to C:\Users\zelinwang\Anaconda3\envs\azure-msal\Scripts
```