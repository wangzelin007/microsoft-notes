git remote add upstream https://github.com/microsoft/knack.git
git fetch upstream
git branch dev --set-upstream-to upstream/dev
git checkout -b wzl_test