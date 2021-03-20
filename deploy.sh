#!/bin/bash
# shellcheck disable=SC1091
set -euo pipefail
if [ ! -d '.venv' ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
set -x
pip install -U pip
pip install -U certbot certbot-plugin-gandi
