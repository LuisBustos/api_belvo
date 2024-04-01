# -*- coding: utf-8 -*-


def get_json(arr):
    data = {}

    for _arr in arr:
        key = _arr.pop('id')
        data[key] = _arr
        

    return data


def porcent_balance(current,available):

    return current * 100 / available

def get_status_result(balance_account,next_payment):
    
    current = balance_account - next_payment

    porcent_current = current * 100 / balance_account

    if porcent_current <= 30:
        return 'Cuidado tus finanzas no están en su mejor momento.'
    elif porcent_current <= 60:
        return 'Tienes oportunidad de mejorar tus finanzas.'
    elif porcent_current <= 80:
        return 'Muy bien, tus finanzas son estables.'
    