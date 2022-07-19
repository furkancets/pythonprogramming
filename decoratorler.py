import time

def karaler_hesapla(sayilar):
    sonuc = list()
    baslama = time.time()
    for i in sayilar:
        sonuc.append(i**2)
    bitis = time.time()
    print(f"birinci döngü {bitis-baslama} sürdü")

    return sonuc
def kupleri_hesapla(sayilar):
    sonuc = list()
    baslama = time.time()
    for i in sayilar:
        sonuc.append(i ** 3)
    bitis = time.time()
    print(f"birinci döngü {bitis - baslama} sürdü")
    return sonuc

karaler_hesapla(range(100000))
kupleri_hesapla(range(100000))



#############



def zaman_hesapla(func):
    def wrapper(sayilar):
        baslama = time.time()

        sonuc = func(sayilar)

        bitis = time.time()

        print(func.__name__ + " " + str(bitis-baslama) + "saniye sürdü.")
        return sonuc
    return wrapper

@zaman_hesapla
def karaler_hesapla(sayilar):
    sonuc = list()

    for i in sayilar:
        sonuc.append(i**2)

    return sonuc

@zaman_hesapla
def kupleri_hesapla(sayilar):
    sonuc = list()

    for i in sayilar:
        sonuc.append(i ** 3)

    return sonuc

karaler_hesapla(range(100000))
kupleri_hesapla(range(100000))


#############

def ekstra(fonk):

    def wrapper(sayilar):
        ciftler_toplami = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0

        for i in sayilar:

            if i % 2 == 0:
                ciftler_toplami += i
                cift_sayilar += 1
            else:
                tekler_toplami += i
                tek_sayilar =+ 1

        print("Teklerin ortalamasi: ", tekler_toplami/tek_sayilar)

        print("Ciftelerin ortalmasi: ", ciftler_toplami/cift_sayilar)

        fonk(sayilar)
    return wrapper





@ekstra
def ortalamabul(sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    print("Genel Ortalama: ", toplam/len(sayilar))


ortalamabul([1, 2, 3, 4, 5, 6])





