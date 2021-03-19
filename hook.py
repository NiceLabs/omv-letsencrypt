#!/bin/env python3
import json
from subprocess import check_output, run


def rpc(service, method, params):
    run(["omv-rpc", service, method, json.dumps(params)], check=True)


def apply_changes(*modules):
    rpc("Config", "applyChanges", {"force": False, "modules": modules})


def get_certificate(name):
    command = ["omv-confdbadm", "read", "conf.system.certificate.ssl"]
    for certificate in json.loads(check_output(command)):
        if certificate["comment"] == name:
            return certificate
    return {
        "uuid": "fa4b1c66-ef79-11e5-87a0-0002b3a176b4",
        "certificate": None,
        "privatekey": None,
        "comment": name,
    }


def get_name():
    with open("CNAME", "r") as fp:
        return fp.read().strip()


def main():
    name = get_name()
    full_chain = "/etc/letsencrypt/live/%s/fullchain.pem" % name
    private_key = "/etc/letsencrypt/live/%s/privkey.pem" % name
    certificate = get_certificate(name)
    with open(full_chain, "r") as fp:
        certificate["certificate"] = fp.read()
    with open(private_key, "r") as fp:
        certificate["privatekey"] = fp.read()
    rpc("CertificateMgmt", "set", certificate)
    apply_changes("certificatemgmt")
    apply_changes()


if __name__ == "__main__":
    main()
