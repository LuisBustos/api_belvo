
from fastapi import FastAPI, HTTPException
from typing import Union
from typing_extensions import Annotated
import json

from infraestructure.db import *

#Implement models
from models.user import UserModel,RESOURCES
from models.transaction import TransactionModel
from infraestructure.connection import ConnectAPI
import utils.utils as utils

from decouple import config
import requests

app = FastAPI()
conn = connect()
cursor = conn.cursor()

@app.on_event("startup")
async def startup_event():
    initialize_db()


@app.post("/users/")
async def add_user(user: UserModel):
    user_id = create_user(user.name,user.age,user.email,user.password)
    if user_id:
        return {"id": user_id, "name": user.name, "age": user.age, "email":user.email, "password": user.password}
    else:
        raise HTTPException(status_code=400, detail="User not created")



@app.get('/users_list/')
async def get_users_list():
    parameters = 'id,first_name,last_name,email'
    response , complete_url =  ConnectAPI()._get_response('owners',False,False,False,parameters)
    #return complete_url
    return json.loads(response.text)

@app.get('/links/')
async def get_links():
    parameters = 'id'
    response , complete_url =  ConnectAPI()._get_response('links',False,False,False,parameters)
    #return complete_url
    return json.loads(response.text)


@app.get('/payment_transaction/{link}')
async def get_payment_transactions(link: str):
    response , complete_url =  ConnectAPI()._get_response('transactions','link',link,False,False)
    #return complete_url
    return json.loads(response.text)

@app.get('/payment_group/')
async def get_payment_group():
    group = {}
    parameters = 'id'
    response , complete_url =  ConnectAPI()._get_response('links',False,False,False,parameters)
    links = json.loads(response.text)
    print('Termine links')
    for payment_id in links['results']:
        response , complete_url =  ConnectAPI()._get_response('transactions','link',payment_id['id'],False,False)
        payment = json.loads(response.text)
        for account in payment['results']:
            trasaction = TransactionModel(
                    account['account']['id'],
                    account['account']['name'],
                    account['account']['type'],
                    account['account']['balance'],
                    account['account']['created_at'],
                    account['account']['category']
                )
            if account['account']['category'] not in group:
                group[account['account']['category']] = []
            group[account['account']['category']].append(trasaction)
    
    return group


@app.get('/finance/{user_id}')
async def get_finances(user_id: str):
    parameters = 'id,link'
    response_owners , complete_url =  ConnectAPI()._get_response('owners',False,user_id,False,parameters)
    owners = json.loads(response_owners.text)
    print(owners)
    response_finances_list , complete_url =  ConnectAPI()._get_response('transactions','link',owners['link'],False,False)
    #return complete_url
    finances_list = json.loads(response_finances_list.text)
    
    next_payment = 0
    balance_account = 0
    for account in finances_list['results']:
        if account['account']['category'] == 'CREDIT_CARD':
            next_payment +=  account['account']['credit_data']['minimum_payment']
        elif account['account']['category'] == 'LOAN_ACCOUNT':
            if account['account']['loan_data']['monthly_payment']:
                next_payment +=  account['account']['loan_data']['monthly_payment']
        elif account['account']['category'] == 'CHECKING_ACCOUNT':
            balance_account += account['account']['balance']['available']

    status_result = utils.get_status_result(balance_account,next_payment)

    result = {
        'Total payment': next_payment,
        'Líquidez':balance_account,
        'Status':status_result
    }
    
    return result

@app.get('/total_finance/{user_id}')
async def total_finance(user_id: str):
    parameters = 'id,link'
    response_account , complete_url =  ConnectAPI()._get_response('accounts',False,user_id,False,parameters)
    accounts = json.loads(response_account.text)
    total_ingress = 0
    total_egress = 0
    for account in accounts['results']:
        if account['account']['category'] == 'CREDIT_CARD':
            total_egress +=  account['account']['credit_data']['minimum_payment']
        elif account['account']['category'] == 'LOAN_ACCOUNT':
            if account['account']['loan_data']['monthly_payment']:
                total_egress +=  account['account']['loan_data']['monthly_payment']
        
    return {
        'Ingresos': total_ingress,
        'Egresos': total_egress
    }


@app.get('/institutions')
async def get_all_institutions():
    response , complete_url=  ConnectAPI()._get_response('institutions',False,False,False,False)
    #return complete_url
    return json.loads(response.text)


@app.get('/institutions/{id}')
async def get_institutions(id: int):
    response , complete_url=  ConnectAPI()._get_response('institutions',False,id,False,False)
    #return complete_url
    return json.loads(response.text)


@app.get('/transactions_type/{link}&{payment_type}&{parameters}')
async def get_transactions_type(link: str, payment_type: str,parameters:str):
    
    if payment_type.upper() not in RESOURCES:
        return {'Error':'400','Message':'Tipo de dato no válido. {}'.format(payment_type)}

    query = 'category={}'.format(payment_type.upper())

    response , complete_url=  ConnectAPI()._get_response('transactions','link',link,query,parameters)
    
    json_response = json.loads(response.text)

    respuesta = utils.get_json(json_response['results'])
    #return complete_url
    #return json.loads(response.text)
    return respuesta
