[Origin] azdev linter --ci-exclusions --rule-types command_coverage --min-severity medium --repo=./ --src=HEAD --tgt=origin/dev
[Failed]       linter --ci-exclusions --rule-types command_coverage --min-severity medium --repo=C:\Code\azure-cli --src=HEAD --tgt=origin/cmdcov-demo-target
[Succeed]      linter --ci-exclusions --rule-types command_coverage --min-severity medium --repo=C:\Code\azure-cli --src=HEAD --tgt=cmdcov-demo-target
[Succeed]      linter --ci-exclusions --rule-types command_coverage --min-severity medium --repo=C:\Code\azure-cli --src=HEAD --tgt=upstream/cmdcov-demo-target
[Failed]       linter --ci-exclusions --rule-types command_coverage --min-severity medium --repo=C:\Code\azure-cli --src=HEAD --tgt=origin/dev
[Succeed]      linter --ci-exclusions --rule-types command_coverage --min-severity medium --repo=C:\Code\azure-cli --src=HEAD --tgt=dev
[Succeed]      linter --ci-exclusions --rule-types command_coverage --min-severity medium --repo=C:\Code\azure-cli --src=HEAD --tgt=upstream/dev

Fix bugs:
Can not find 'aks create', resource_type=ResourceType.MGMT_CONTAINERSERVICE, operation_group='managed_clusters --enable-fips-image' test case
Please add some scenario tests for the new parameter
Or add the parameter with missing_parameter_coverage rule in linter_exclusions.yml
