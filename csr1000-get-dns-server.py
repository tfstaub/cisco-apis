#!/usr/bin/env python3

import requests
import getpass

username = input("What is your username? ")
password = getpass()

requests.packages.urllib3.disable_warnings()

device = {
    "host": " {{ hostname or ip address }}",
    "port": "443",
    "user": username,
    "password": password
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

url = f"https://{device['host']}:{device['port']}/api/v1/global/dns-servers"

response = requests.get(
    url=url, headers=headers, auth=(device["user"], device["password"]), verify=False
)

response.raise_for_status()
print(response.text)
