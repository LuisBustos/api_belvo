import requests

user = '37b99625-6c35-438d-b807-3596d2b68093'

URL_FINANCES = 'http://127.0.0.1:8000/finance'



payment_list = requests.get('{}/{}'.format(URL_FINANCES,user)).json()

print(payment_list)