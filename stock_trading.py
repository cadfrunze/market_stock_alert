"""Preluare date API pret actiune (https://www.alphavantage.co/documentation/)"""
import requests
from datetime import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_STOCK = 'GZVVFO8YXPAC9YLF'


def actualizare_actiune() -> dict:
    """ Functie preluare valori stock exchange"""
    ziua, luna, anul = str(datetime.now().day - 1), str(datetime.now().month), str(datetime.now().year)
    if int(ziua) < 10:
        ziua = '0' + ziua
    if int(luna) < 10:
        luna = '0' + luna

    parametrii: dict = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'outputsize': 'compact',
        'apikey': API_STOCK
    }
    while True:
        try:
            raspuns = requests.get(url='https://www.alphavantage.co/query?', params=parametrii)
        except requests.exceptions.ConnectTimeout:
            continue
        else:
            raspuns.raise_for_status()
            data_json: dict = raspuns.json()
            while True:
                try:
                    data_json['Time Series (Daily)'][f'{anul}-{luna}-{ziua}']
                except KeyError:
                    ziua = str(int(ziua) - 1)
                else:
                    break
            if int(ziua) < 10:
                ziua = '0' + ziua
            date_finalizate: dict = {f'{anul}-{luna}-{ziua}': data_json['Time Series (Daily)'] \
                [f'{anul}-{luna}-{ziua}']['4. close']}
            ziua = str(int(ziua) - 1)
            while True:
                try:
                    data_json['Time Series (Daily)'][f'{anul}-{luna}-{ziua}']
                except KeyError:
                    ziua = str(int(ziua) - 1)
                else:
                    break
            if int(ziua) < 10:
                ziua = '0' + ziua
            date_finalizate[f'{anul}-{luna}-{ziua}'] = data_json['Time Series (Daily)'] \
                [f'{anul}-{luna}-{ziua}']['4. close']
            return date_finalizate
