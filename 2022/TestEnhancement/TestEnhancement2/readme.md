IndexRefDocVerify
https://github.com/Azure/azure-cli-extensions/issues/4648

az self-test

scripts/release/rpm/test_rpm_in_docker.sh
scripts/release/debian/test_deb_in_docker.sh
scripts/ci/test_extensions.sh

Test Extensions Loading Python310 -> scripts/ci/test_extensions.sh

Test Rpm Package -> azure-cli/scripts/release/rpm/test_rpm_in_docker.sh -> azure-cli/scripts/release/rpm/test_rpm_package.py
Test Deb Packages Focal -> azure-cli/scripts/release/debian/test_deb_in_docker.sh -> azure-cli/scripts/release/debian/test_deb_package.py
Test Deb Packages Jammy -> azure-cli/scripts/release/debian/test_deb_in_docker.sh
Test Deb Packages Buster -> azure-cli/scripts/release/debian/test_deb_in_docker.sh
Test Deb Packages Bullseye -> azure-cli/scripts/release/debian/test_deb_in_docker.sh
Test Python Wheels 删除py3.7 az self-test
Test Homebrew Formula az self-test

现在共计63个测试任务
是否过度测试了？
如果要加快也要拆
那么有些任务可以删除或者合并
1. Verify src/azure-cli/requirements.*.Linux.txt 能不能合并到后面的test 中顺便做掉 -3
2. Unit Test for Core 和 Telemetry 可以合并 -3
3. Automation test 可以用 Automation full test 代替 -12
4. Test Extensions Loading Python310 优化 需要拆分
5. Build Package 优化： 共计12个
6. Check CLI Style, Check License, History, and DocMap, Check CLI Linter
7. Test xxx Package 共计五个，等于五个全量测试，是否有必要？
8. Integration Test -> azdev verify load-all 是不是也可以放一起？ -3
9. Test Homebrew Formula az self-test 为什么慢？

依赖关系梳理
Test Windows MSI -> Build Windows MSI -> Extract Metadata
Test Docker Image -> Build Docker Image -> Extract Metadata
Test Python Wheel -> Build Python Wheels -> Extract Metadata
# Integration Test against Profiles * 3 -> Build Python Wheels
Test Homebrew Formula -> Build Homebrew Formula -> Build Python Wheels
Test Homebrew Formula -> Build Homebrew Formula
Test Rpm Package -> Build Rpm Package CentOS 7 10min
Test Deb Packages * 4 最长30min -> Build Deb Packages * 8 最长21min

Build Rpm Package Red Hat Universal Base Image 8 40min+

azdev test - build -test docker(win-mac-linux-deb-centos) install run - 30min-10 -> build 40min 报错
azdev test - full vm - 10min ubantu 20.04 不报错
incremental azdev test diff main head 4min

daily run
PR Test（X） Build（）-> 30
PR Test（X） Build（X）-> 10

github repo 配置

1. 删除dev tool diff如果有core, 全量跑的逻辑。
2. github配置trigger full automation test。
3. credential scan 增量。
4. test extension load 优化。
5. build windows MSI 禁用。
6. Test xxx packages 只测试部分关键module。