#!/bin/python3
import requests, json, os, time


API_BASE_URL = "https://api.godaddy.com"
API_ACCESS_KEY = "accessxyz"  # Godaddy API Access Key
API_SECRET = "secretxyz" # Godaddy API Secret Key
DOMAIN_NAME = "example.com" # Should be owned by you
CREATE_DOMAIN = "_acme-challenge." + os.environ["CERTBOT_DOMAIN"].split(".")[0] # environment variables are passed by certbot to this script
VALIDATION = os.environ["CERTBOT_VALIDATION"] # environment variables are passed by certbot to this script
path = "/v1/domains/"
domains_uri = API_BASE_URL + path + DOMAIN_NAME
records_uri = domains_uri + "/records/"
headers = {
    "Authorization": "sso-key" + " " + API_ACCESS_KEY + ":" + API_SECRET,
    "Content-Type": "application/json",
}

record_data = [{"type": "TXT", "name": CREATE_DOMAIN, "data": VALIDATION, "ttl": 600}]
records = requests.patch(
    records_uri, headers=headers, data=str(json.dumps(record_data)) # Follow Godaddy Documentation Domains API
)

time.sleep(60)
