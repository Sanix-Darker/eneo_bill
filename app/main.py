# ENEO BILL
# By Sanix-darker
import os
import requests
from lxml import html
from bs4 import BeautifulSoup
import time
from datetime import datetime
from app.settings import *


print("")
print(" _____ _   _ _____ ___        ____ ___ _     _     ____   ")
print("| ____| \ | | ____/ _ \      | __ )_ _| |   | |   / ___|  ")
print("|  _| |  \| |  _|| | | |_____|  _ \| || |   | |   \___ \  ")
print("| |___| |\  | |__| |_| |_____| |_) | || |___| |___ ___) | ")
print("|_____|_| \_|_____\___/      |____/___|_____|_____|____/  v0.1 ")
print(" - - - - - - - - - - - - -  - - - - - - - -- - - - - - - - - -")
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
    soup = BeautifulSoup(r.text, features="lxml")

    # Unpaids : tab_impaye
    # Bills : tab_paiements
    rows = soup.find("div", {"id": "tab_paiements"}).find("table").find("tbody").find_all("tr")

    print("[+] List of bills :")
    print("[+] Date, N° Reçu, Montant payé, Mode, Agence, N° Facture, Mois, Montant facturé")
    print("[+] -")
    fetched_list = ""
    for row in rows:
        cells = row.find_all("td")

        line = "[+] "
        for cell in cells:
            line += ''.join(cell.get_text().split()) + ", "
        line += "\n------------------------------------------------------------"
        
        print(line)
        fetched_list += line + "\n"
        time.sleep(1)
    print("[+] -")
    
    bill_file_name = "eneo_bills_" + str(datetime.now()) + ".txt"
    # Saving the bills in a file
    with open(bill_file_name, "w") as file_:
        file_.write(fetched_list)

    print("[+] Bills saved in ", bill_file_name)

# if __name__ == "main":
main()
