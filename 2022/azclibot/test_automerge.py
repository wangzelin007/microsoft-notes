#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import requests
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

token = os.getenv('GH_AUTH')
headers = {'Authorization': 'token %s' % token,
           'Accept': 'application/vnd.github.v3+json'}

def auto_merge():
    # curl -X PUT -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/merge
    # curl -X PUT https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/merge
    merge_url = f'https://api.github.com/repos/Azure/azure-cli-extensions/pulls/4945/merge'
    logger.debug(merge_url)
    # merge, squash or rebase
    body = {
        'merge_method': 'squash'
    }
    try:
        r = requests.put(merge_url, json=body, headers=headers)
    except requests.RequestException as e:
        raise e
    if r.status_code != 200:
        logger.debug(r)
        logger.debug(r.text)
        sys.exit(1)


if __name__ == '__main__':
    auto_merge()