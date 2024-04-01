import requests

user = '37b99625-6c35-438d-b807-3596d2b68093'

URL_TOTAL_FINANCES = 'http://127.0.0.1:8000/total_finance'

total_finance = requests.get('{}/{}'.format(URL_TOTAL_FINANCES,user)).json()

print(total_finance)