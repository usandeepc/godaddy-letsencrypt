#!/bin/python3
import requests, json, os, time


API_BASE_URL = "https://api.godaddy.com"
API_ACCESS_KEY = "accessxyz"
API_SECRET = "secretxyz"
DOMAIN_NAME = "example.com"
DELETE_DOMAIN = "_acme-challenge." + os.environ["CERTBOT_DOMAIN"].split(".")[0]
VALIDATION = os.environ["CERTBOT_VALIDATION"]
path = "/v1/domains/"
domains_uri = API_BASE_URL + path + DOMAIN_NAME
records_uri = domains_uri + "/records/"+"TXT/"+DELETE_DOMAIN
headers = {
    "Authorization": "sso-key" + " " + API_ACCESS_KEY + ":" + API_SECRET,
    "Content-Type": "application/json",
}

record_data = [{"type": "TXT", "name": DELETE_DOMAIN}]
records = requests.delete(
    records_uri, headers=headers)

time.sleep(60)
