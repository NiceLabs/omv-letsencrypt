#!/bin/bash
# shellcheck disable=SC1091
set -euo pipefail
set -x
if [ ! -d '.venv' ]; then
	python3 -m venv .venv
fi
source .venv/bin/activate
pip install -U pip
pip install -U certbot certbot-plugin-gandi
