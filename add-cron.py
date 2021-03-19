#!/bin/env python3
import json
import os
from subprocess import check_output, list2cmdline, run

hook_path = os.path.abspath(os.path.dirname(__file__))
command = [
    os.path.join(hook_path, ".venv", "bin", "certbot"),
    "renew",
    "--post-hook",
    os.path.join(hook_path, "hook.py"),
]

configured = {
    "type": "userdefined",
    # see https://forum.openmediavault.org/index.php?thread/16752-api-cron/
    "uuid": "fa4b1c66-ef79-11e5-87a0-0002b3a176b4",
    "dayofmonth": "*",
    "dayofweek": "*",
    "enable": True,
    "everyndayofmonth": False,
    "everynhour": False,
    "everynminute": False,
    "execution": "daily",
    "hour": "13",
    "minute": "24",
    "month": "*",
    "username": "root",
    "command": list2cmdline(command),
    "sendemail": False,
    "comment": "Automatically Renew Certificate",
}


def rpc(service, method, params):
    run(["omv-rpc", service, method, json.dumps(params)], check=True)


def apply_changes(*modules):
    rpc("Config", "applyChanges", {"force": False, "modules": modules})


def get_cron():
    params = {
        "type": ["userdefined"],
        "start": 0,
        "limit": 25,
        "sortfield": "enable",
        "sortdir": "ASC",
    }
    command = ["omv-rpc", "Cron", "getList", json.dumps(params)]
    tasks = json.loads(check_output(command))
    for task in tasks["data"]:
        if task["comment"] == configured["comment"]:
            return task
    return configured


def main():
    task = get_cron()
    configured["uuid"] = task["uuid"]
    rpc("Cron", "set", configured)
    apply_changes("Cron")
    apply_changes()


if __name__ == "__main__":
    main()
