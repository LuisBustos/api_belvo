from pydantic import BaseModel
from typing import Optional,ClassVar
from datetime import datetime 

class TransactionModel(BaseModel):
    id : str
    name : str
    type : str
    created_at: datetime
    category :str
    balance : ClassVar

    def __init__(self,id : str,name : str,type : str,balance :[], created_at: datetime,category :str):
        super().__init__(
            id = id,
            name = name,
            type = type,
            created_at = created_at,
            category = category,
            balance=balance
        )