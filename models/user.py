from pydantic import BaseModel

RESOURCES = [
    'ACCOUNTS',
    'OWNERS',
    'TRANSACTIONS',
    'INCOMES',
    'RECURRING_EXPENSES',
    'RISK_INSIGHTS',
    'CREDIT_SCORE',
    'DEPOSITS']

class UserModel(BaseModel):
    name : str
    age : int
    password : str
    email : str

    def __init__(self, name : str,age : int, password :str,email :str):
        super().__init__(
            name = name,
            age = age,
            password = password,
            email = email
        )

    def _get_json(self):
        return {
            'name':self.name,
            'age':self.age,
            'password':self.password,
            'email':self.email
        }
    
