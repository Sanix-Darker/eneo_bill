# utils.py
# All necessary methods

from lxml import html
from datetime import datetime
from app.settings import *
import requests
from bs4 import BeautifulSoup
import time


def present_app():
    """
    A simple banner of the application
    """
    print("")
    print(" _____ _   _ _____ ___        ____ ___ _     _     ____   ")
    print("| ____| \ | | ____/ _ \      | __ )_ _| |   | |   / ___|  ")
    print("|  _| |  \| |  _|| | | |_____|  _ \| || |   | |   \___ \  ")
    print("| |___| |\  | |__| |_| |_____| |_) | || |___| |___ ___) | ")
    print("|_____|_| \_|_____\___/      |____/___|_____|_____|____/  v0.1 ")
    print("                                   By github.com/sanix-darker")
    print(" - - - - - - - - - - - - -  - - - - - - - -- - - - - - - - - -")
    print("[+] ENEO-BILL started!")


def get_token(session_requests):
    """
    This method will fetch the token in the web-page and return it
    """
    # Get login _token
    print("[+] Connecting to eneocameroon")
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)

    print("[+] Fetching token..")
    _token = list(set(tree.xpath("//input[@name='_token']/@value")))[0]
    print("[+] _token: ", _token)

    return _token


def save_bills_in_file(fetched_list):
    """
    This method will save the list of bills in a file
    """
    bill_file_name = "eneo_bills_" + str(datetime.now()) + ".txt"
    # Saving the bills in a file
    with open(bill_file_name, "w") as file_:
        file_.write(fetched_list)

    print("[+] Bills saved in ", bill_file_name)


def perform_login():
    """
    This method will build a valid payload with a valid token and perform the login process
    """

    session_requests = requests.session()

    # Create the payload for the submission form
    payload = {
        "login": USERNAME,
        "password": PASSWORD,
        "_token": get_token(session_requests)  # This method will fetch the token on the page
    }
    print("[+] Perform the Login...")
    # Perform login
    result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))
    if result.status_code != 404:
        print("[+] Login successfully !")

    return session_requests


def print_bills(rows):
    """
    This method will just print the available bills in row in terminal screen
    """
    print("[+] List of bills :")
    print("[+] Date, N° Reçu, Montant payé, Mode, Agence, N° Facture, Mois, Montant facturé")
    print("[+] -")
    fetched_list = ""
    for row in rows:
        cells = row.find_all("td")

        line = "[+] "
        for cell in cells:
            line += ''.join(cell.get_text().split()) + ", "
        line += "\n----------------------------------------------------------------------"

        print(line)
        fetched_list += line + "\n"
        time.sleep(1)
    print("[+] -")
    return fetched_list


def fetch_bills(session_requests):
    """
    This method will fetch bills from the url
    """
    print("[+] Fetching bills on : ", BILLS_URL)
    # Let's scrap the content
    r = session_requests.get(BILLS_URL, headers=dict(referer=BILLS_URL))

    # Let's use beautifullSoup to parse the content
    soup = BeautifulSoup(r.text, features="lxml")

    # For Unpaids : #tab_impaye or for Bills : #tab_paiements
    rows = soup.find("div", {"id": "tab_paiements"}).find("table").find("tbody").find_all("tr")

    fetched_list = print_bills(rows)

    return fetched_list
