# ENEO BILL
# By Sanix-darker
import os
import json
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

# should contain while invoices history 
db = {'invoices': []}

def update_db_file(data):
    """
    update the db in the db by overiding it, {data} should contain the old values so nothing is loosed
    """
    _db_file = open('incoices_db.json', 'w')
    _db_file.write(json.dumps(data))
    _db_file.close()
        
def open_db_file():
    """
    return 2 values
    - the JSON representation of the file contain which should represent the DB
    DB structure :
    
    {
        "INVOICE_ID": [INVOICE_DATA]
    }
    
    like that it will be more easy later to check the existance of a invoice in the db (in case of a unpaid invoice)
    as explained here : https://twitter.com/tmpoudi/status/1244521777553907713
    """
    _db_data = {}
    f = None
    try:
        # try to read actuall db data
        _db_file = open('invoices_db.json', 'r')
        _temp = _db_file.read()
        _db_data = json.loads(_temp) # should contain a dict
        if type(_db_data) is not dict:
            # if not just back it up and raise an exception
            _copy_file = open('invoices_db.backup.json', 'w')
            _copy_file.write(json.dumps(_db_data))
            _copy_file.close()
            raise Exception('The data file is corrupted, new db creation operation. A backup file has been created here invoices_db.backup.json')
        _db_file.close()
    except:
        # if it doesn't exist create it
        _db_file = open('invoices_db.json', 'w')
        _db_file.write('{}')
        _db_file.close()
        _db_data = {}
    return _db_data

def main():
    print("[+] Performing the db extraction...")
    db_data = open_db_file()
    print("[+] Performing the Login...")
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
    fetched_data = {}
    fetched_list = ""
    
    js_rows = {}
    existing_row = {}
    for row in rows:
        cells = row.find_all("td")
        
        # a json representation of the table 
        # "invoice number": [cell data as a list]
        _inv_id = cells[5].get_text().split()
        _cell_data = [ cell.get_text().split() for cell in cells ]
        
        js_rows[_inv_id] = [ _cell_data ]
        if _inv_id in list(db_data.keys()):
            # this invoice is already in the db
            print('\n {} : invoice is already in the db ---------------------'.format(inv_id))
            existing_row.update({_inv_id: _cell_data})
        
        line = "[+] "
        for cell in cells:
            line += ''.join(cell.get_text().split()) + ", "
        line += "\n----------------------------------------------------------------------"
        print(line)
        fetched_list += line + "\n"
        
        time.sleep(1)
    print("[+] -")

    bill_file_name = "eneo_bills_{}.txt".format(str(datetime.now()))
    json_bill_file_name = "eneo_bills_{}.json".format(datetime.now())
    
    # Saving the bills in a file as a JSON file instead of a .txt file
    with open(json_bill_file_name, 'w') as js_file:
        js_file.write(json.dumps(fetched_data))
        js_file.close()
    
    # for potential backward compatibility 
    with open(bill_file_name, "w") as file_:
        file_.write(fetched_list)
        
    # we have the whole object set of new invoices, check if onw is comming a second time
    # update the db object here
    db_data.update(js_rows)
    # save to the file here
    update_db_file(db_data)
    
    print("[+] Bills saved in ", bill_file_name)

# if __name__ == "main":
main()
