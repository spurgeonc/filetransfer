import requests
s = requests.Session()

site = 'ac031f581e9191c68062bdb4004d00e2.web-security-academy.net'

download_url = f'https://{site}/download-transcript/1.txt'
resp = s.get(download_url, allow_redirects=False)
print(resp.text)