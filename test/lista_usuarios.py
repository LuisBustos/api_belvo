import requests

URL = 'http://127.0.0.1:8000/users_list'


users = requests.get(URL).json()

for user in users['results']:
    print('############')
    print('ID: {}'.format(user['id']))
    print('Nombre: {} {}'.format(user['first_name'],user['last_name']))
    print('Correo electrónico: {}'.format(user['email']))
    print('############')