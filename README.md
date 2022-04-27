# Let's Encrypt on OpenMediaVault

## Usage

```bash
# download tarbell
wget -O - aka.pw/omv-letsencrypt-tarbell | tar zxv
mv omv-letsencrypt-master /opt/letsencrypt
cd /opt/letsencrypt
# initial configuration
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
