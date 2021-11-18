What's Dogfood environment for?
Usually service will deploy their new features in Dogfood env for test. 
This is earlier than public preview(by then service will deploy to canary and we can test in some euap locations)

How to create or delete a subscription in Dogfood?
https://armwiki.azurewebsites.net/internals/release_management/DogfoodSubscriptionProvisioning.html

Dogfood Portal?
https://df.onecloud.azure-test.net/

CLI's Dogfood subscription?
https://df.onecloud.azure-test.net/#@MSFT.ccsctp.net/resource/subscriptions/e4ced903-171b-4a34-a408-1b7185ea530a/overview

How to test CLI in Dogfood env?
Dogfood endpoint config file:
					
[comment]: <> (register Dogfood Cloud)
az cloud register --name AzureDFCloud --cloud-config @cloud_DF.json

[comment]: <> (set Dogfood Cloud)
az cloud set --name AzureDFCloud

[comment]: <> (it's possible that you need to relogin)
az login

az cloud list
az cloud show --name AzureCloud
az cloud set --name AzureCloud