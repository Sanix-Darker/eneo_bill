# ENEO BILL
import os
import requests
from lxml import html
from bs4 import BeautifulSoup
from app.settings import *

print("[+] ENEO-BILL started!")

session_requests = requests.session()

# Get login _token
result = session_requests.get(LOGIN_URL)
tree = html.fromstring(result.text)
_token = list(set(tree.xpath("//input[@name='_token']/@value")))[0]

# Create the payload for the submission form
payload = {
    "user[login]": USERNAME,
    "user[password]": PASSWORD,
    "_token": _token
}

# Perform login
result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))


def main():

    bill_url = "https://my.eneocameroon.cm/"
    # Let's scrap the content
    result_content = session_requests.get(bill_url, headers=dict(referer=bill_url))

    # Let's use beautifullSoup to parse the content
    soup = BeautifulSoup(result.content)
    rows = soup.find("table", {"class": "table"}, border=1).find("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all("td")
        the_cell = cells[0].get_text()

        print("the_cell : ", the_cell)

main()
