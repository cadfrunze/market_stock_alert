# # cat este 20% din 15
# numarul = 100
# muncitori  = 10
#
# rezultat = (muncitori * 100) / numarul
# print(round(rezultat, 2))

from datetime import datetime

minute = datetime.now().minute
ora = datetime.now().hour
ziua = datetime.now().day
luna = datetime.now().month
an = datetime.now().year

with open('./work_log.txt', 'a') as fisier:
    fisier.writelines(f'\nData: {ziua}/{luna}/{an} | Ora: {ora}:{minute}')