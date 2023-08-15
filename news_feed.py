"""Preluare date/informatii stiri relevante despre fluxul actiunilor (API)"""
from newsapi import NewsApiClient
from stock_trading import preturi
import json

stire = NewsApiClient(api_key='bc0e3640ec7e4cf09ebed342fb622a91')
date_liste = [data for data in preturi.keys()]
print(date_liste)
articole = stire.get_everything(q='Tesla',
                                from_param=date_liste[-1],
                                to=date_liste[0],
                                language='en',
                                sort_by='popularity')
print(articole)