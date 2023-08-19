"""Din acest fisier vom rula mecanismul de calculare, afisare a actiunilor (cazul de fata Tesla),
    conform cerintelor, vezi lectia 36. Day 36 - Intermediate+ Stock Trading News Alert Project"""
from news_feed import news
from stock_trading import preturi
import os
from twilio.rest import Client

suma_lista: list = [float(num) for num in preturi.values()]
yesterday_price: float = float(round(suma_lista[0], 2))
alaltaieri_price: float = float(round(suma_lista[-1], 2))

print(yesterday_price, alaltaieri_price)

if yesterday_price > alaltaieri_price:
    res_price: float = yesterday_price - alaltaieri_price
    # Calcularea procentului cu cat a urcat pretul actiunilor
    procent_price: int = int((res_price * 100) / yesterday_price)
    print(procent_price)
    if procent_price > 5:
        # Trimiterea de mesaj, sub forma de SMS
        account_sid = 'test'
        aut_token = 'test'
        client = Client(account_sid, aut_token)
        mesaj = client.messages.create(
            from_='test',
            to='test',
            body=f'''Pretul actiunilor, ieri: {yesterday_price}, alataieri: {alaltaieri_price}\n
ultima stire de ieri: {news["stire1"]["titlu"]}\n
{news["stire1"]["continut"]}\n\n
Ultima stire de alaltaieri: {news["stire2"]["titlu"]}\n
{news["stire2"]["continut"]}''')
