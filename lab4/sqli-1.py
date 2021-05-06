import requests
'''from bs4 import BeautifulSoup'''

def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    print(url)
    print(resp.text)

random = 'ac301fe91ed694a18003616a00b100ee'
site = f'https://{random}.web-security-academy.net'
s = requests.Session()

try_category("""'""")


'''This code failed so I did it in-browser'''