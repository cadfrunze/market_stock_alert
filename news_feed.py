"""Preluare date/informatii stiri relevante despre fluxul actiunilor (API)"""
from newsapi import NewsApiClient
from stock_trading import preturi


def afisare_news() -> dict:
    """Functie pt afisare stiri"""
    stire = NewsApiClient(api_key='test')
    date_liste = [data for data in preturi.keys()]
    articole = stire.get_everything(q='Tesla',
                                    from_param=date_liste[-1],
                                    to=date_liste[0],
                                    language='en',
                                    sort_by='publishedAt')
    stiri_dict: dict = {
        'stire1': {
            'titlu': articole['articles'][0]['title'],
            'continut': articole['articles'][0]['description']
        },
        'stire2': {
            'titlu': articole['articles'][1]['title'],
            'continut': articole['articles'][1]['description']
        }
    }
    return stiri_dict


news: dict = afisare_news()
