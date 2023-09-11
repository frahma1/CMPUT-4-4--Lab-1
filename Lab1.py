import requests

requests_version = requests.__version__



page = requests.get('https://www.google.com/')

print(requests_version)