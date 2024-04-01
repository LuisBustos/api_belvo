import requests


URL_LINKS = 'http://127.0.0.1:8000/links'
URL_PAYMENT = 'http://127.0.0.1:8000/payment_transaction'

payment_list = requests.get(URL_LINKS).json()


def get_transaction(account):

    return """[Identificador: {}, 
    Nombre: {}, 
    Tipo: {}, 
    Balance: {}, 
    Fecha de creación: {}, 
    Categoria: {}]
    """.format(account['id'],
               account['name'],
               account['type'],
               account['balance'],
               account['created_at'],
               account['category']
    )


for payment_id in payment_list['results']:
    print(payment_id['id'])
    payment = requests.get(
        '{}/&link={}&?page=1'.format(URL_PAYMENT,payment_id['id'])
    ).json()
    print('############')
    print('{}'.format(payment['results']))
    for account in payment['results']:
        print('{}'.format(
            get_transaction(account['account'])
            )
        )
    print('############')




