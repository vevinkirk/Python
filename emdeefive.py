import requests
import hashlib
import re

url="http://docker.hackthebox.eu:42283/"

client = requests.session()
response = client.get(url)
response = re.search("<h3 align='center'>(.*)</h3>",response.text)
response = response.group(1)
response = hashlib.md5(response.encode('utf-8')).hexdigest()
data = {'hash' :  response}
response = client.post(url, data = data)
print(response.text)
