# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module sends notification about the end of a workflow run
and its associated artifacts.
"""

import os
import requests
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
from urllib.parse import urlparse

API_REGION = os.environ.get("AWS_DEFAULT_REGION")
NOTIFICATION_ENDPOINT = os.environ.get("NOTIFICATION_ENDPOINT")

PAYLOAD = {}
PAYLOAD["solution_org"] = os.environ.get("GITHUB_REPOSITORY").split("/")[0]
PAYLOAD["solution_name"] = os.environ.get("GITHUB_REPOSITORY").split("/")[1]
PAYLOAD["branch"] = os.environ.get("BRANCH")
PAYLOAD["workflow_name"] = os.environ.get("WORKFLOW_NAME")
PAYLOAD["commit_id"] = os.environ.get("COMMIT_ID")
PAYLOAD["workflow_run_id"] = os.environ.get("WORKFLOW_RUN_ID")
PAYLOAD["version"] = os.environ.get("VERSION")
PAYLOAD["pipeline_type"] = os.environ.get("PIPELINE_TYPE")


def send_notification(parsed):
    auth = BotoAWSRequestsAuth(aws_host=parsed.netloc, aws_region=API_REGION, aws_service="execute-api")
    response = requests.post(NOTIFICATION_ENDPOINT, json=PAYLOAD, auth=auth, timeout=25)
    print(response.json())
    if response.status_code != 200:
        return 1
    else:
        return 0


def main():
    parsed = urlparse(NOTIFICATION_ENDPOINT)
    print(PAYLOAD)
    # TODO: placeholder: result=send_notification(parsed)
    # TODO: placeholder: print(f"{result=}")


if __name__ == "__main__":
    main()
