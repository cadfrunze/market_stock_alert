from stock_trading import actualizare_actiune

preturi: dict = actualizare_actiune()
suma_lista: list = [float(num) for num in preturi.values()]
yesterday_price: float = float(round(suma_lista[0], 2))
alaltaieri_price: float = float(round(suma_lista[-1], 2))
print(yesterday_price, alaltaieri_price)
if yesterday_price > alaltaieri_price:
    res_price: float = yesterday_price - alaltaieri_price
    procent_price: int = int((res_price * 100) / yesterday_price)
