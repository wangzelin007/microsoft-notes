Integrate pytest-cov into azdev test
[issue](https://github.com/Azure/azure-cli-dev-tools/pull/317)
[code](https://github.com/StrawnSC/azure-cli-dev-tools/tree/cli-test-coverage)

azdev test --coverage --open-coverage
--coverage
--no-htmlcov
--append-coverage
--coverage-path
--open-coverage

在当前目录下生成htmlcov

Hi @StrawnSC
I was wondering can we put the `--coverage` out of `azdev test` command to become a independent command like `azdev coverage`.
Because running `azdev test` is very time wasting, but only `azdev coverage` is very fast.
if I only want to generate the coverage report, I need to spend a lot of time waiting for the `azdev test`.
And a failed test will cause the coverage test terminate unexpected.
This is my experience of downloading the code and actually using it.

**install extensions**
az extension list-available
az extension add --name $(az extension list-available --query "[].name" -o tsv)
az vm resize --size Standard_DS3_v2 --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)