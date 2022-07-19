from datetime import datetime

print(datetime.now())

su_an = datetime.now()

print(su_an.year)

print(su_an.month)

print(su_an.microsecond)

print(su_an.hour)

print(datetime.ctime(su_an))

print(datetime.strftime(su_an, "%Y"))

print(datetime.strftime(su_an, "%B"))

print(datetime.strftime(su_an, "%D"))

print(datetime.strftime(su_an, "%B %Y"))

print(datetime.strftime(su_an, "%Y %B %A"))

import locale

locale.setlocale(locale.LC_ALL,"")

su_an = datetime.now()

saniye = datetime.timestamp(su_an)

print(saniye)

su_an2 = datetime.fromtimestamp(saniye)

print(su_an2)

suan = datetime.fromtimestamp(0)

print(suan)


tarih = datetime(2019, 12, 1)

su_an = datetime.now()

print(su_an-tarih)











