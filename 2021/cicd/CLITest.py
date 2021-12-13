import os
import subprocess
import sys


# ENV_COMMAND_COVERAGE = 'AZURE_CLI_TEST_COMMAND_COVERAGE'

# os.environ[ENV_COMMAND_COVERAGE] = "true" #  visible in this process + all children
# azdev test --no-exitfirst --profile latest --verbose --series
subprocess.check_call(['azdev', 'test', '--no-exitfirst', '--profile', 'latest', '--verbose', '--series'],
                      env=dict(os.environ, SQSUB_VAR="visible in this subprocess"))
# azdev test --live --mark serial --xml-path test_results.sequential.xml --no-exitfirst -a "-n 1 --capture=sys"
# os.environ[ENV_COMMAND_COVERAGE] = "true"
subprocess.check_call(['azdev', 'test', '--live', '--mark', 'serial', '--xml-path', 'test_results.sequential.xml',
                       '--no-exitfirst'],
                      env=dict(os.environ, SQSUB_VAR="visible in this subprocess"))
