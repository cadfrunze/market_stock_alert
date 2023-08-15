from stock_trading import actualizare_actiune

preturi: dict = actualizare_actiune()
suma_lista: list = [float(num) for num in preturi.values()]
res_price: float = round(suma_lista[0] - suma_lista[-1], 2)
print(res_price)
if res_price > 0:
    pass