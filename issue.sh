#!/bin/bash
# shellcheck disable=SC1091
source .venv/bin/activate
set -x
NAME="$(cat CNAME)"
certbot certonly \
  --config "cli.ini" \
  --cert-name "$NAME" \
  --domain "$NAME" \
  --domain "*.$NAME"
