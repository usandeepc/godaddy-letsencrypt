#!/bin/bash
#Run this script to get certificates for test.example.com available at /etc/letsencrypt/live/test.example.com
# Replace with values of your own
sudo certbot certonly --manual --preferred-challenges=dns --manual-auth-hook ./manual_auth_hook.py --manual-cleanup-hook ./manual_cleanup_hook.py -d test.example.com
