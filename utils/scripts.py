#create 1001 users
import requests

URL = 'http://127.0.0.1:8000/users'

for i in range(1,1000):
    data = {
    'name': 'Luis_{}'.format(i),
    'age': 31,
    'email': 'Luis_{}@example.com'.format(i),
    'password': '123qweASD{}'.format(i)
    }
    print(URL)
    print(data)
    print(requests.post(URL,json=data))
