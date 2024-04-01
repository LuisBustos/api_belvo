# -*- coding: utf-8 -*-
from decouple import config
import requests

class TransactionError(Exception):
    pass

class ConnectAPI:
    
    def __init__(self):
        self.secret_id = config('SECRET_ID')
        self.secret_key = config('SECRET_KEY')
        self.basic_url = config('BASIC_URL')

    def _post_response(self,model,data):
        try:
            complete_url = '{}/{}/'.format(self.basic_url,model)
            return requests.post(
                url= complete_url,
                auth=(self.secret_id,self.secret_key),
                json=data
            )
        except Exception as e:
            raise TransactionError(str(e)) 

    def _get_response(self,model,key,value,query,params):
        try:
            headers = {'Accept':'application/json'}
            complete_url = '{}/{}/'.format(self.basic_url,model)

            if key:
                complete_url = '{}?{}='.format(complete_url,key)
            if value:
                complete_url = '{}{}'.format(complete_url,value)
                # /id = 
                # /?link=

            if query:
                complete_url = '{}&{}'.format(complete_url,query)
            
            if params:
                if '?' in complete_url:
                    complete_url = '{}&fields={}'.format(complete_url,params)
                else:
                    complete_url = '{}?fields={}'.format(complete_url,params)

            response = requests.get(
                url= complete_url,
                auth=(self.secret_id,self.secret_key),
                headers=headers
                )
            
            return response, complete_url
        

        except Exception as e:
            raise TransactionError(str(e)) 
