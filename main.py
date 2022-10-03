import json
from pathlib import Path
import pandas as pd
from datetime import datetime
import requests
import csv


def add_addresses():
    Addresses = int(input('Ingrese el codigo del inversor:  \n'))
    if Addresses == 1450 or Addresses == 1451 or Addresses== 1452:
        date(Addresses)
    print('Marco un inversor incorrecto, vuelva a intentarlo \n')
    return add_addresses()

def date(Addresses):
    print('A continuacion ingresara la fecha donde inicia la busqueda, la fecha mas vieja, (from)')
    year_from = input('Escriba las dos ultimos digitos del año: ')
    moonth_from = input('Escriba el mes en digitos: ')
    day_from = input('Escriba el numero del dia: ')
    from_str = year_from + '-' + moonth_from + '-' + day_from
    print('La fecha de comienzo es:', from_str)

    print('A continuacion ingresara la fecha donde termina la busqueda, la fecha mas actual (to)')
    year_to = input('Escriba las dos ultimos digitos del año: ')
    moonth_to = input('Escriba el mes en digitos: ')
    day_to = input('Escriba el numero del dia: ')
    to_str = year_to + '-' + moonth_to + '-' + day_to
    print('La fecha de finalizacion es:', to_str)


    from_object = datetime.strptime(from_str, '%y-%m-%d')
    to_object = datetime.strptime(to_str, '%y-%m-%d')
    test_range = to_object - from_object

    if 0 <= test_range.days <= 180:
        start_date = '20' + from_str + 'T00:00:00'
        finish_date = '20' + to_str + 'T00:00:00'
        read_to_api(Addresses, start_date, finish_date)

    print('Las fechas exceden el limite de tiempo, ingrese fechas en un rango de tiempo de 6 meses')
    return date(Addresses)
def read_to_api(Addresses, start_date, finish_date):
    url =  'ingrese la url de la api' 
    headers = {
        'Content-Type': 'application/json',
         'Authorization': 'Bearer ingrese el token correspondiente'
        }
    payload = json.dumps({
                "Id_addresses": [Addresses],
                "From": start_date,
                "To": finish_date
            })

    response = requests.request("POST", url,headers=headers,data=payload)
    if response.status_code == 200:
        print(response)
        print(type(response.text))
        format_csv(response.text)
    print(response)
    print('Ha ocurrido un error, vuelva a intentarlo por favor.')
    return add_addresses()

def format_csv(api_json):
    print('Ha ingresado correctamente al csv')
    today = datetime.today()
    name_today = today.date()
    name_today_str = name_today.strftime('%y-%m-%d_solar.csv')
    file = open(name_today_str, "w")
    file.write(api_json)
    file.close
    question_continue=int(input('Marque 1 si desea ver un nuevo inversor, en caso contrario marqeu 2: '))
    if question_continue == 1:
        add_addresses()
    return exit()
if __name__ == '__main__':
    print('Bienvenido al consumo de la api neu.com')
    add_addresses()
