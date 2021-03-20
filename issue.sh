#!/bin/bash
set -x
.venv/bin/certbot \
	certonly \
	--agree-tos \
	--register-unsafely-without-email \
	--authenticator dns-gandi \
	--dns-gandi-credentials "credentials.ini" \
	--server "https://acme-v02.api.letsencrypt.org/directory" \
	--domain "$(cat CNAME)" \
	--domain "*.$(cat CNAME)"
