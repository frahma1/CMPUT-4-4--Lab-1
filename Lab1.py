import requests


print(requests.__version__)

page = requests.get('https://www.google.com/')

url = "https://raw.githubusercontent.com/frahma1/CMPUT-404--Lab-1/master/Lab1.py"

res = requests.get(url)

print(res.text)