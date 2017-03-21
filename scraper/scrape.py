import requests
from bs4 import BeautifulSoup

# url = raw_input("Please enter the URL to collect data: ")
url = "www.hackthissite.org"

req = requests.get("http://" + url)

soup_data = BeautifulSoup(req.content, "html.parser")

login = soup_data.find_all("div", {"id":"ourlogin"})

for item in login:
    print item.contents
