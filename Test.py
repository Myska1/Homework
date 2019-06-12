import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

proxy = {"https": "http://webproxy-fra.deutsche-boerse.de:8080"}
url = "http://cernyrytir.cz/index.php3?akce=100&sekce=mtg&podsekce=display"
response = requests.get(url, proxies = proxy)
soup = BeautifulSoup(response.text, "html.parser")

