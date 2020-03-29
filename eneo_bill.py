# ENEO BILL
# from werkzeug import secure_filename
import requests
from lxml import html
import json
import os
from bs4 import BeautifulSoup
from settings import *
from hashlib import sha256

print("ENEO_Bill started!")

session_requests = requests.session()

