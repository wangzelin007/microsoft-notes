def run_cli_cmd(cmd, retry=0):
    '''Run a CLI command
    :param cmd: The CLI command to be executed
    :param retry: The times to re-try
    '''
    import json
    import subprocess

    output = subprocess.run(cmd, shell=True, check=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    if output.returncode != 0:
        if retry:
            run_cli_cmd(cmd, retry - 1)
        else:
            raise Exception('Command execution failed, command is: '
                                   '{}, error message is: {}'.format(cmd, output.stderr))

    return json.loads(output.stdout) if output.stdout else None

output = run_cli_cmd('az ad sp show --id {}'.format('40309e42-3910-4617-b233-1887cc9cd92f'))