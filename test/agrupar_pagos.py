import requests

user = '37b99625-6c35-438d-b807-3596d2b68093'

URL_GROUP = 'http://127.0.0.1:8000/payment_group'

payment_group = requests.get('{}/{}'.format(URL_GROUP)).json()

print(payment_group)