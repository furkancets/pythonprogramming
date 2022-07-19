def fonksiyon(*args):
    for i in args:
        print(i)


fonksiyon(1, 2, 3)

fonksiyon(1, 2, 3, 4, 5, 6)

def fonksiyon_1(isim, *args):
    print("İsim:", isim)

    print("-------------")
    for i in args:
        print(i)

fonksiyon_1("Murat",1,2,3,4,5)


def fonksiyon_2(**kwargs):
    print(kwargs)

fonksiyon_2(isim = "Murat",soyisim="Coşkun", numara=12345)


def fonkiyon_3(**kwargs):
    for i,j in kwargs.items():
        print("Argüman ismi",i,"Argüman Değeri",j)



fonkiyon_3(isim="Murat", soyisim= "Coşkun", numara= 12345)


def fonkiyon_4(*args,**kwargs):
    for i in args:
        print(i)
    print("-----")
    for i,j in kwargs.items():
        print(i,j)


fonkiyon_4(1,2,3,4,5,isim="Murat", soyisim= "Coşkun", numara= 12345)

#içiçe fonk
def selamla(isim):
    print("selam",isim)

selamla("Furkan")


merhaba = selamla

merhaba("Kemal")

del selamla

merhaba("Selim")


def fonksiyon_5():

    def fonksiyon_5_1():
        print("Küçük fonksiyondan herkese merhaba")
    fonksiyon_5_1()
    print("Büyük fonksiyondan herkese mehaba")


fonksiyon_5()


def fonksiyon_6(*args):

    def toplama(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(toplama(args))

fonksiyon_6(1,2,3,4,5,6)


#parametre olarak fonksiyonlar ve fonksiyon objesi dönen fonksiyonlar

def anafonksiyon(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplama
    else:
        return carpim

fonk = anafonksiyon("toplama")

fonk(1,2,3,4,5)

fonk2 = anafonksiyon("carpim")

fonk2(1,2,3,4)



def toplama(a, b):
    return a + b
def cikarma(a, b):
    return a-b
def carpma(a, b):
    return a*b
def bolme(a, b):
    return a/b

def anafonksiyon(func1,func2,func3,func4,islem_adi):
    if islem_adi == "toplama":
        print(func1(3, 4))
    elif islem_adi == "cikarma":
        print(func2(6, 10))
    elif islem_adi == "carpma":
        print(func3(7, 3))
    elif islem_adi == "bolme":
        print(func4(8, 4))
    else:
        print("geçersiz işlem")

anafonksiyon(toplama,cikarma,carpma,bolme,"toplama" )











