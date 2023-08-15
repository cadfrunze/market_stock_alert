"""Din acest fisier vom rula mecanismul de calculare, afisare a actiunilor (cazul de fata Tesla),
    conform cerintelor, vezi lectia 36. Day 36 - Intermediate+ Stock Trading News Alert Project"""
from stock_trading import preturi


suma_lista: list = [float(num) for num in preturi.values()]
yesterday_price: float = float(round(suma_lista[0], 2))
alaltaieri_price: float = float(round(suma_lista[-1], 2))
print(yesterday_price, alaltaieri_price)

if yesterday_price > alaltaieri_price:
    res_price: float = yesterday_price - alaltaieri_price
    # Calcularea procentului cu cat a urcat pretul actiunilor
    procent_price: int = int((res_price * 100) / yesterday_price)
    if procent_price > 5:
        pass
