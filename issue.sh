#!/bin/bash
set -x
.venv/bin/certbot \
	certonly \
	--agree-tos \
	--register-unsafely-without-email \
	--authenticator dns-gandi \
	--dns-gandi-credentials "credentials.ini" \
	--domain "$(cat CNAME)"
