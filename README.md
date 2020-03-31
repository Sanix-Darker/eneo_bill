<img src="./images/logo.png">

# ENEO-BILL

An implementation of a Bot that will fetch available bills on eneocameroon website and use kraken to buy them !

## DEMO

<img src="./images/demo.gif">

## Requirements

- Python (3.x recommended)
- pip3

## How to install

- App tree

```shell script
.
├── app
│   ├── main.py
│   ├── settings.py
│   └── utils.py
├── example.config.txt
├── images
│   ├── demo.gif
│   └── logo.png
├── README.md
└── requirements.txt
```

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

- To launch hit this command :
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
......
........ 
----------------------------------------------------------------------
[+] -
[+] Bills saved in  eneo_bills_2020-03-29 16:12:57.872790.txt
```

## Author

- Sanix-darker