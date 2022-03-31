https://github.com/Azure/azure-cli/issues/19298
name: 24 -> 64

2019-review
> az desktopvirtualization hostpool create --host-pool-type "Pooled" --load-balancer-type "BreadthFirst" --personal-desktop-assignment-type "Automatic" --resource-group zelin63 --name abcdefghijklmnopqrstuvwxyz

2021-stable
> az desktopvirtualization hostpool create --host-pool-type "Pooled" --load-balancer-type "BreadthFirst" --preferred-app-group-type Desktop --resource-group zelin63 --name abcdefghijklmnopqrstuvwxyz

init pr: https://github.com/Azure/azure-cli-extensions/pull/1741

swagger pr: https://github.com/Azure/azure-rest-api-specs/pull/15155
