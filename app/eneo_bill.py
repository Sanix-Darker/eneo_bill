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

def getreadme(project):
    URL = "https://gitrepo.variancetechnologies.io/" + project + "/raw/develop/README.md"
    result_README = session_requests.get(URL, headers=dict(referer=URL))
    return str(result_README.content).replace('\\n', ' \\n ')

def main():

    LIST_URL = [ "https://gitrepo.variancetechnologies.io/dashboard/projects?non_archived=true&page=2&sort=latest_activity_desc" ]
    # Scrape url
    for URL in LIST_URL:

        print("> Url:", URL)
        result = session_requests.get(URL, headers=dict(referer=URL))

        microservice = []
        microservice_links = []
        microservice_README = []
        soup = BeautifulSoup(result.content)
        for hitIT in soup.findAll("a", {"class": "text-plain"}):
            link = hitIT['href']
            group = hitIT['href'].split("/")[1]
            project_name = hitIT['href'].split("/")[2]
            print(">> project:", project_name)
            print(">> group:", group)

            resp = session_requests.get(
                "https://gitrepo.variancetechnologies.io" + link + "/-/archive/master/" + project_name + "-master.zip",
                headers=dict(referer=URL))

            if not os.path.exists("./" + group):
                os.system("mkdir " + group)
            if not os.path.exists(group + "/" + project_name + ".zip"):
                print("In progress ...")
                fd = open(group + "/" + project_name + ".zip", 'wb')
                fd.write(resp.content)
                fd.close()
            else:
                print("File allready downloaded !")

main()
