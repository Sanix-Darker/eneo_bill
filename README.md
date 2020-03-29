<img src="./images/logo.png">

# ENEO-BILL

An implementation of a Bot that will fetch available bills on eneocameroon website and use kraken to buy them !

## DEMO

<img src="./images/demo.gif">

## Requirements

- Python (3.x recommended)
- pip3

## How to install

- Rename the `example.config.txt` to `config.txt` and put valid/good credentials !
```
[eneo-config]
USERNAME = 6999999 # This is your username on the website
PASSWORD = -------- # this is your password on the webSite
LOGIN_URl = https://my.eneocameroon.cm/login
```

- Hit this command to install all :
```shell
pip3 install -r requirements.txt
```

## How to launch

```shell
python3 -m app.main
```

- Expected output : 
```shell
 _____ _   _ _____ ___        ____ ___ _     _     ____   
| ____| \ | | ____/ _ \      | __ )_ _| |   | |   / ___|  
|  _| |  \| |  _|| | | |_____|  _ \| || |   | |   \___ \  
| |___| |\  | |__| |_| |_____| |_) | || |___| |___ ___) | 
|_____|_| \_|_____\___/      |____/___|_____|_____|____/  v0.1 
 - - - - - - - - - - - - -  - - - - - - - -- - - - - - - - - -
[+] ENEO-BILL started!
[+] Connecting to eneocameroon
[+] Fetching token..
[+] _token:  QVQWdFkL3slSpau9yl57GcXWAmaabaXYjMXeNlwg
[+] Perform the Login...
[+] Login successfully !
[+] Fetching bills on :  https://my.eneocameroon.cm/
[+] List of bills :
[+] Date, N° Reçu, Montant payé, Mode, Agence, N° Facture, Mois, Montant facturé
[+] -
[+] 20-03-2020, 5799140, 1250, CASH, ORANGE, CASH, Mar-2020, 1250, Reçu, 
----------------------------------------------------------------------
[+] 17-02-2020, 5799140, 750, CASH, ORANGE, CASH, Feb-2020, 750, Reçu, 
----------------------------------------------------------------------
[+] 20-01-2020, 578111, 800, CASH, PALMIERS, CASH, Jan-2020, 800, Reçu, 
----------------------------------------------------------------------
[+] 23-12-2019, 5799140, 1150, CASH, ORANGE, CASH, Dec-2019, 1150, Reçu, 
----------------------------------------------------------------------
[+] 23-11-2019, 5799140, 1750, CASH, ORANGE, CASH, Nov-2019, 1750, Reçu, 
----------------------------------------------------------------------
[+] 19-10-2019, 5799140, 1650, CASH, ORANGE, CASH, Oct-2019, 1650, Reçu, 
----------------------------------------------------------------------
[+] 23-10-2019, 579111, 20550, CASH, PALMIERS, CASH, Oct-2019, 20550, Reçu, 
----------------------------------------------------------------------
[+] 20-09-2019, 5799140, 1800, CASH, ORANGE, CASH, Sep-2019, 1800, Reçu, 
----------------------------------------------------------------------
[+] 17-08-2019, 5799140, 1400, CASH, ORANGE, CASH, Aug-2019, 1400, Reçu, 
----------------------------------------------------------------------
[+] 18-07-2019, 5799140, 1550, CASH, ORANGE, CASH, Jul-2019, 1550, Reçu, 
----------------------------------------------------------------------
[+] 15-06-2019, 5799140, 1500, CASH, ORANGE, CASH, Jun-2019, 1500, Reçu, 
----------------------------------------------------------------------
[+] 18-05-2019, 5799140, 1300, CASH, ORANGE, CASH, May-2019, 1300, Reçu, 
----------------------------------------------------------------------
[+] 19-04-2019, 5799140, 1200, CASH, ORANGE, CASH, Apr-2019, 1200, Reçu, 
----------------------------------------------------------------------
[+] -
[+] Bills saved in  eneo_bills_2020-03-29 16:12:57.872790.txt
```

## Author

- Sanix-darker