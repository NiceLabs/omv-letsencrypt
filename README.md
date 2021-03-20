# Let's Encrypt on OpenMediaVault

## Usage

```bash
# initial configuration
wget -O - https://git.io/JmyB7 | tar zxv
mv omv-letsencrypt-master /opt/letsencrypt
cd /opt/letsencrypt
echo "your domain" > CNAME
echo "dns_gandi_api_key=your api key" > credentials.ini
chmod 400 credentials.ini
# deploy certbot
./deploy.sh
# issue certificate
./issue.sh
# import certificate
./hook.py
# add to scheduled job
./add-cron.py
```

## References

- <https://adrian.work/post/openmediavault-5-letsencrypt-certbot-dns-cloudflare/>
