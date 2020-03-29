# ENEO BILL
import os
import requests
from lxml import html
from bs4 import BeautifulSoup
from app.settings import *

print("[+] ENEO-BILL started!")

session_requests = requests.session()

# Get login _token
print("[+] Connecting to eneocameroon")
result = session_requests.get(LOGIN_URL)
tree = html.fromstring(result.text)

print("[+] Fetching token..")
_token = list(set(tree.xpath("//input[@name='_token']/@value")))[0]

print("[+] _token: ", _token)

# Create the payload for the submission form
payload = {
    "login": USERNAME,
    "password": PASSWORD,
    "_token": _token
}

def main():
    print("[+] Perform the Login...")
    # Perform login
    result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))

    if result.status_code != 404:
        print("[+] Login successfully !")
        
    
    bill_url = "https://my.eneocameroon.cm/"
    print("[+] Fetching bills on : ", bill_url)
    # Let's scrap the content
    r = session_requests.get(bill_url, headers=dict(referer=bill_url))

    # Let's use beautifullSoup to parse the content
    soup = BeautifulSoup(r.content, features="lxml")
    rows = soup.find("table", {"class": "table"}, border=1).find("tbody").find_all("tr")

    print("[+]List of bills :")
    for row in rows:
        cells = row.find_all("td")
        the_cell = cells[0].get_text()

        print("[+] >> ", the_cell)

main()
