**path**: azure-sdk / internal / Pipelines / cli / Azure CLI Live Test  
[**pipeline**:](https://dev.azure.com/azure-sdk/internal/_build?definitionId=1896)  
[knowledge transition](onenote:https://microsoft.sharepoint.com/teams/IoTToolingTeam/Shared%20Documents/Azure%20Management%20Experience/Azure%20Management%20Experience/AZ%20CLI/Transition.one#Live%20Test&section-id=%7BCADD4696-365A-48BD-80B4-0DF0B2451ECC%7D&page-id=%7B1B77ECCB-F1D1-4CE7-BF08-E89C1C85E1B3%7D&end)  
[edit pipeline](https://dev.azure.com/azure-sdk/internal/_apps/hub/ms.vss-build-web.ci-designer-hub?pipelineId=1896&nonce=06F4BUw0jgsxnvhRpSdnrQ%3D%3D&branch=dev)  

python /home/vsts/work/1/s/scripts/live_test/sendemail.py "$(SENDGRID_KEY)" "$(Build.BuildId)" "$(USER_REPO)" "$(USER_BRANCH)" "$(USER_TARGET)" "$(USER_LIVE)" "$(System.ArtifactsDirectory)" "$(Build.RequestedForEmail)" "$(ACCOUNT_KEY)" "$commit_id" "$(DB_PWD)"
SENDGRID_KEY = sys.argv[1] have
BUILD_ID = sys.argv[2] 
USER_REPO = sys.argv[3] https://github.com/Azure/azure-cli.git
USER_BRANCH = sys.argv[4] dev
USER_TARGET = sys.argv[5] have
USER_LIVE = sys.argv[6] --live
ARTIFACT_DIR = sys.argv[7]  
REQUESTED_FOR_EMAIL = sys.argv[8]
ACCOUNT_KEY = sys.argv[9] have
COMMIT_ID = sys.argv[10] 
DB_PWD = sys.argv[11] have

USER_BRANCH : dev
USER_LIVE : --live
USER_PARALLELISM : 8
USER_REPO : https://github.com/Azure/azure-cli.git
USER_TARGET : undefined

D:\code\azure-cli\scripts\live_test\CLITest.yml

**如何查看变量的值**

**邮件平台**
[sendgrid](https://github.com/sendgrid/sendgrid-python)
[api key申请](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Sendgrid.Email%2Faccounts)
SendGrid Accounts
azureclitest
https://signup.sendgrid.com/
**删除保护锁哈**

**权限申请**

**code**
```python
def send_email():
    print('Enter send_email()')
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    print('Sending email...')
    message = Mail(
        from_email='zelinwang@microsoft.com',
        to_emails='zelinwang@microsoft.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
```
