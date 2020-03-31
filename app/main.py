# ENEO BILL
# By Sanix-darker

from app.utils import *


def main():
    # We present the application with a banner
    present_app()

    # We perform the login
    session_requests = perform_login()

    # We print and get the list of fetched-bills
    fetched_list = fetch_bills(session_requests)

    # We save the bills in a file
    save_bills_in_file(fetched_list)


# if __name__ == "main":
main()
