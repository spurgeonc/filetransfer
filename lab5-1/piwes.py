import requests
from bs4 import BeautifulSoup
s = requests.Session()
site = 'ac6a1fa31e3544568084279b00010023.web-security-academy.net'
SOU_id = 'spurgeonc'

site_url = f'https://{site}/'
resp = s.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')
exploit_html = f'''<h1>Hello {SOU_id}</h1>'''
formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}
resp = s.post(exploit_url, data=formData)