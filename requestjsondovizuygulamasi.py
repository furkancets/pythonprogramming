#import requests
#
#import sys
#url = "http://api.fixer.io/latest?base="
#
#birinci_doviz = input("Birinci Döviz:")
#ikinci_döviz = input("İkinci Döviz:")
#miktar = float(input("Miktar:"))
#
#
#response = requests.get(url + birinci_doviz)
#
#json_verisi = response.json()
#try:
#    print(json_verisi["rates"][ikinci_döviz] * miktar)
#except KeyError:
#    sys.stderr.write("Lütfen para birimlerini doğru girin")
#    sys.stderr.flush()
import sys

import requests

birinci_doviz = input("Birinci Döviz:")
ikinci_döviz = input("İkinci Döviz:")
miktar = float(input("Miktar:"))

url = f"https://api.apilayer.com/currency_data/convert?to={ikinci_döviz}&from={birinci_doviz}&amount={miktar}"

payload = {}
headers= {
  "apikey": "cP6O6X2pAZOeRGGYDTdTazl10KynwMxw"
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response)

#status_code = response.status_code
#result = response.text

json_verisi = response.json()

try:

    print(json_verisi["result"])

except KeyError:
    sys.stderr.write("Lütfen Para Birimlerini Doğru Girin")
    sys.stderr.flush()
    print("ok")