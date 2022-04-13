#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


#  https://github.com/Azure/azure-cli/blob/dev/.github/pull_request_template.md


import json
import logging
import re
import sys


# http://noyobo.com/2015/11/13/ANSI-escape-code.html
# Reset all to default: 0
# Bold or increased intensity: 1
# Fraktur (Gothic): 20
# red: 31
# green: 32
# yellow: 33
# grey: 38
reset = "\x1b[0m"
red = "\x1b[31;20m"
bold_red = "\x1b[31;1m"
green = "\x1b[32;20m"
yellow = "\x1b[33;20m"
grey = "\x1b[38;20m"
format = "%(message)s"
words_to_check = {
            'Add': r'\b(added|adding|adds)\b',
            'Allow': r'\b(allowed|allowing|allows)\b',
            'Change': r'\b(changed|changing|changes)\b',
            'Deprecate': r'\b(deprecated|deprecating|deprecates)\b',
            'Disable': r'\b(disabled|disabling|disables)\b',
            'Enable': r'\b(enabled|enabling|enables)\b',
            'Fix': r'\b(fixed|fixing|fixes)\b',
            'Improve': r'\b(improved|improving|improves)\b',
            'Make': r'\b(made|making|makes)\b',
            'Move': r'\b(moved|moving|moves)\b',
            'Rename': r'\b(renamed|renaming|renames)\b',
            'Replace': r'\b(replaced|replacing|replaces)\b',
            'Remove': r'\b(removed|removing|removes)\b',
            'Support': r'\b(supported|supporting|supports)\b',
            'Update': r'\b(updated|updating|updates)\b',
            'Upgrade': r'\b(upgraded|upgrading|upgrades)\b',
        }


class CustomFormatter(logging.Formatter):
    # logging with color
    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


def check_pull_request(title, body):
    if title.startswith('['):
        error_flag = regex_line(title)
        is_edit_history_note = False
        history_note_error_flag = False
        for line in body:
            if line.startswith('['):
                # get component name in []
                ref = re.findall(r'[\[](.*?)[\]]', line)
                if ref and ref[0] not in ['Component Name 1', 'Component Name 2']:
                    is_edit_history_note = True
                    history_note_error_flag = regex_line(line) or history_note_error_flag
		# If edit history notes, ignore title check result
        error_flag = error_flag if not is_edit_history_note else history_note_error_flag
    elif title.startswith('{'):
        error_flag = False
    else:
        logger.error('Pull Request title should start with [ or { , Please follow https://aka.ms/submitAzPR')
        error_flag = True
    return error_flag


def regex_line(line):
    error_flag = False
    enclosed_begin = False
    enclosed_end = True
    # Check Fix #number in title, just give a warning here, because it is not necessarily.
    if 'Fix' in line:
        sub_pattern = r'#\d'
        ref = re.findall(sub_pattern, line)
        if not ref:
            logger.warning('If it\'s related to fixing an issue, put Fix #number in title\n')
    for idx, i in enumerate(line):
        # ] } : must be followed by a space
        if i in [']', '}', ':']:
            try:
                assert line[idx + 1] == ' '
            except:
                logger.info('%s%s: missing space after %s', line, yellow, i)
                logger.error(' ' * idx + '↑')
                error_flag = True
        # az xxx commands must be enclosed in `, e.g., `az vm`
        if i == 'a' and line[idx + 1] == 'z' and line[idx + 2] == ' ':
            command = 'az '
            index = idx + 3
            while index < len(line) and line[index] != ':':
                command += line[index]
                index += 1
            try:
                assert line[idx - 1] == '`'
            except:
                logger.info('%s%s: missing ` around %s', line, yellow, command)
                logger.error(' ' * idx + '↑' + ' ' * (index - idx - 2) + '↑')
                error_flag = True
        if i == ':':
            # check extra space character before colon
            if idx - 1 >= 0 and line[idx - 1] == ' ':
                logger.info('%s%s: please delete extra space character before :', line, yellow)
                logger.error(' ' * (idx - 1) + '↑')
                error_flag = True
            # First word after the colon must be capitalized
            index = 0
            if line[idx + 1] == ' ' and line[idx + 2].islower() and line[idx + 2: idx + 5] != 'az ':
                index = idx + 2
            elif line[idx + 1] != ' ' and line[idx + 1].islower() and line[idx + 1: idx + 4] != 'az ':
                index = idx + 1
            if index:
                logger.info('%s%s: should use capital letters after :', line, yellow)
                logger.error(' ' * index + '↑')
                error_flag = True
        # --xxx parameters must be enclosed in `, e.g., `--size`
        if line[idx] == '`' and not enclosed_begin:
            enclosed_begin = True
            enclosed_end = False
        elif line[idx] == '`' and enclosed_begin:
            enclosed_begin = False
            enclosed_end = True
        if i == '-' and (idx + 1) < len(line) and line[idx + 1] == '-':
            if not enclosed_begin:
                param = '--'
                index = idx + 2
                while index < len(line) and line[index] not in [' ', '/']:
                    param += line[index]
                    index += 1
                try:
                    assert line[idx - 1] == '`'
                except:
                    logger.info('%s%s: missing ` around %s', line, yellow, param)
                    logger.error(' ' * idx + '↑' + ' ' * (index - idx - 2) + '↑')
                    error_flag = True
        # verb check: only check the first word after ] or :
        if i in [']', ':']:
            word = ''
            c = index = idx + 1 if line[idx + 1] != ' ' else idx + 2
            while index < len(line) and line[index] != ' ':
                word += line[index]
                index += 1
            for k, v in words_to_check.items():
                if re.findall(v, word, re.IGNORECASE):
                    logger.info(line)
                    logger.error(' ' * c + '↑')
                    logger.warning(
                        'Please use the right verb of%s %s %swith %s(%s)%s simple present tense in base form '
                        'and capitalized first letter to describe what is done, '
                        'follow https://aka.ms/submitAzPR\n', red, word, yellow, green, k, yellow)
                    error_flag = True
                    break
        # check extra consecutive spaces
        if i == ' ' and (idx + 1) < len(line) and line[idx + 1] == ' ':
            logger.info('%s%s: please delete the extra space character', line, yellow)
            logger.error(' ' * (idx + 1) + '↑')
            error_flag = True

    # last character check
    if line[-1] in ['.', ',', ' ']:
        logger.info('%s%s: please delete the last character', line, yellow)
        logger.error(' ' * idx + '↑')
        error_flag = True

    # check the ending ` character
    if not enclosed_end:
        logger.info('%s%s: unable to find the ending ` character', line, yellow)
        error_flag = True

    return error_flag


def test_pull_request_template():
    body = "[Component Name 1] BREAKING CHANGE: `az command a`: Make some customer-facing breaking change\r\n" \
           "[Component Name 2] `az command b`: Add some customer-facing feature\r\n".split(
        '\r\n')
    title = "[App Service] BREAKING CHANGE: Use new web app and function app stacks APIs"
    if check_pull_request(title, body):
        logger.error("Test Template error, please fix !\n")
    else:
        logger.info("\n%sTest Template pass!\n" % green)

def test_check_pull_request():
    logger.info("Start check pull request ...\n")
    # title = "[CI Test]az test:add --check-pull-request to check pull request title and content"
    body = []
    title = "[App Service] BREAKING CHANGE:Use new web app and function app stacks APIs"
    body += ["[App Service] BREAKING CHANGE: `az webapp up`: Change supported runtimes"]
    body += ["[App Service] BREAKING CHANGE: `az webapp create`: Change supported runtimes"]
    body += ["[App Service] BREAKING CHANGE: `az webapp list-runtimes`: Add `--os`/`--os-type` argument, change runtimes, change default behavior to return both linux and windows stacks, and deprecate `--linux` argument"]
    body += ["[App Service] BREAKING CHANGE: `az functionapp create`: Take runtime names and versions from API instead of hardcoded list"]
    body += ["[App Service] add new command `az functionapp list-runtimes`"]
    body += ["[App Service] BREAKING CHANGE: `az webapp list-runtimes`: Add `--os`/`--os-type` argument, change runtimes, change default behavior to return both linux and windows stacks, and deprecate --linux argument"]
    body += ["[Keyvault] Fixed #21341: `az keyvault update`: Supported updating tags"]
    body += ["[Keyvault] Fix #21341: `az keyvault update`: Supported updating tags"]
    body += ["[Keyvault] Fix #21341: `az keyvault update`: Supported updating tags"]
    body += ["[Keyvault] fixed #21341: `az keyvault update`: Support updating tags"]
    body += ["[App Service] add new command az functionapp list-runtimes"]
    body += ["[App Service] add new command `az functionapp list-runtimes`."]
    body += ["[App Service] add new command `az functionapp list-runtimes`,"]
    body += ["[App Service] add new command `az  functionapp    list-runtimes`  "]
    body += ["[Keyvault] Fix #21341: `az keyvault update`: Support updating tags"]
    sys.exit(1) if check_pull_request(title, body) else sys.exit(0)


def test_fix_check_pr():
    title = '[ServiceBus] Add Filter Type parameter to az servicebus topic subscription rule create'
    body = []
    # body += ["[ServiceBus] az servicebus topic subscription rule create: Add filter_type parameter"]
    body += ["[ServiceBus] `az servicebus topic subscription rule create`: Add filter_type parameter"]
    sys.exit(1) if check_pull_request(title, body) else sys.exit(0)

def test_multiple_para():
    title = '[Storage] Add `--blob-endpoint/--file-endpoint/--table-endpoint/--queue-endpoint` for data service commands to support customized service endpoint'
    body = []
    body += ['[Storage] Add `--blob-endpoint`/`--file-endpoint`/`--table-endpoint`/`--queue-endpoint` for data service commands to support customized service endpoint']
    # body += ['[Storage] Add `--blob-endpoint`/`--file-endpoint/--table-endpoint`/`--queue-endpoint` for data service commands to support customized service endpoint']
    # body += ['[Storage] Add `--blob-endpoint`/`--file-endpoint`/--table-endpoint/`--queue-endpoint` for data service commands to support customized service endpoint']
    # body += ['[Storage] Add --blob-endpoint/--file-endpoint/--table-endpoint/--queue-endpoint for data service commands to support customized service endpoint']
    # body += ['[Storage] Add `--blob-endpoint/--file-endpoint/--table-endpoint/--queue-endpoint for data service commands to support customized service endpoint']
    # body += ['[Storage] Add `--blob-endpoint`/`--file-endpoint/--table-endpoint/--queue-endpoint for data service commands to support customized service endpoint']
    body += ['[Storage] Add `--blob-endpoint`/`--file-endpoint/`--table-endpoint`/`--queue-endpoint` for data service commands to support customized service endpoint']
    body += ['[Storage] `az Storage`: Add --blob-endpoint/--file-endpoint/--table-endpoint/--queue-endpoint']
    sys.exit(1) if check_pull_request(title, body) else sys.exit(0)

def test_tmp():
    title = '[AMS] az ams account identity assign: Added ability to assign managed identity to media services account'
    body = []
    body += ['[AMS] az ams account identity assign: Added ability to assign managed identity to media services account']
    body += ['[AMS] az ams account identity remove: Added ability to assign managed identity to media services account']
    body += ['[AMS] az ams transform create: Added new parameter blur-type for FaceDetector presets']
    body += ['[AMS] az ams account encryption set: Added new parameters system-assigned and user-assigned to allow users to set managed identities to their account encryption']
    body += ['[AMS] az ams account storage set-authentication: Added new parameters system-assigned and user-assigned to allow users to set managed identities for their storage account attached to Media Services']
    sys.exit(1) if check_pull_request(title, body) else sys.exit(0)

if __name__ == '__main__':
    # test_pull_request_template()
    # test_check_pull_request()
    # test_fix_check_pr()
    # test_multiple_para()
    test_tmp()