#!/bin/bash
set -euo pipefail
set -x
python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install certbot certbot-plugin-gandi
