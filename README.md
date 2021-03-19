# Let's Encrypt on OpenMediaVault

## Usage

```bash
# initial configuration
git clone https://github.com/NiceLabs/omv-letsencrypt /opt/letsencrypt
cd /opt/letsencrypt
echo "your domain" > CNAME
echo "dns_gandi_api_key=your api key" > credentials.ini
chmod 400 credentials.ini
# deploy
./deploy.sh
# issue certificate
./issue.sh
# import certificate
./hook.py
# add scheduled job
./add-cron.py
```

## References

- <https://adrian.work/post/openmediavault-5-letsencrypt-certbot-dns-cloudflare/>
