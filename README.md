"""
Servicios API REST para el sandbox de https://sandbox.belvo.com/api

Los servicios implementados son:
•	Lista de transacciones de pagos
•	Listado de Usuarios 
•	Servicio de retorne montos agrupados por categorías de gastos.
•	Servicio que determine qué tan sanas son sus finanzas (análisis de ingresos y egresos)
•	Servicio que sume total de ingresos y egreso de las diferentes cuentas del usuario.

Los endpoints disponibles son:
    GET payment_transaction: 
        Devuelve una json que contiene las transacciones de pago
    
    GET users_list: 
        Devuelve un json que contiene los usuarios registrados en el sandbox
    
    GET payment_group: 
        Devuelve un json que contiene los pagos agrupados por tipo
    
    GET finance: 
        user_id: str
        Devuelve un json que contiene los datos financieros de un usuario en específico
    
    GET total_finance:
        user_id: str
        Devuelve un json que contiene los egresos acumulados de la cuenta de un usuario

    POST users:
        user : UserModel
        UserModel:
            name : str
            age : int
            password : str
            email : str

        Crea un usuario dentro de la base de datos finvero.

Los archivos para hacer test de servicios son:
    finvero_api/test/lista_transacciones.py 
    finvero_api/test/lista_usuarios.py 
    finvero_api/test/agrupar_pagos.py
    finvero_api/test/status_finanza.py
    finvero_api/test/pagos.py
"""


#CREACIÓN DEL DOCKER
sudo docker compose up -d 
sudo docker container ls


#Acceso al docker
sudo docker run -it finvero_api-finvero /bin/bash

#Comandos necesarios dentro del docker para el funcionamiento del api
systemctl start mysql
systemctl enable mysql
cd /finvero_api/infraestructure/
/usr/bin/mysql -u root -p < db_config.sql

cd /finvero_api/
python3 -m venv finveroapi-env

source finveroapi-env/bin/activate

pip install fastapi
pip install requests
pip install uvicorn
pip install python-multipart
pip install requests 
pip install python-dotenv python-decouple 
pip install mysql-connector-python 

uvicorn main:app --reload --access-log