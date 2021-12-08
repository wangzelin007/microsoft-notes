1. cdn 有一些没拿到？所以走 self.cmd 也有问题
2. 考虑从recording里面取，进一步增加覆盖率。
```yaml
      CommandName:
      - acr create
      CommandName: [group create]
      ParameterSetName:
      - -n -g -l --sku
      ParameterSetName: [--location --name --tag]
```

