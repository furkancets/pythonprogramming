liste = [1,2,3,4,5]

dir(liste)


iterator = iter(liste)


next(iterator)

next(iterator)

next(iterator)

next(iterator)

next(iterator)

next(iterator) # error


liste = [1,2,3,4,5]

for i in liste:
    print(i)

iterator = iter(liste)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break



##

class Kumanda():
    def __init__(self, kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1

    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index < len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration


kumanda = Kumanda(["Atv","Trt","Fox","Kanal D","Bloombeg"])

iterator = iter(kumanda)

next(iterator)


for i in kumanda:
    print(i)


##Genaratorlerin Oluşturulması ve kullanılması


def kareleri_al():
    sonuc = []

    for i in range(1,6):
        sonuc.append(i**2)

    return sonuc

print(kareleri_al())


def kareleri_al():
    for i in range(1,6):
        yield i ** 2

generator = kareleri_al()

print(generator)

iterator = iter(generator)

next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)

iterator2 = iter(generator)

next(iterator2)


liste = [i * 3 for i in range(5)]

generator2 = (i * 3 for i in range(5))

print(generator2)

iterator = iter(generator2)


next(iterator)


def carpimtablosu():

    for i in range(1, 11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpimtablosu():
    print(i)


#iter generator fibonacci


class Kuvvet3():
    def __init__(self,max= 0):

        self.max = max
        self.kuvvet = 0

    def __iter__(self):

        return self

    def __next__(self):
        if(self.kuvvet <= self.max):
            sonuc = 3 ** self.kuvvet

            self.kuvvet += 1

            return sonuc

        else:
            self.kuvvet = 0

            raise StopIteration


kuvvet = Kuvvet3(6)

iterator = iter(kuvvet)

next(iterator)

for i in kuvvet:
    print(i)

for j in kuvvet:
    print(j)

##generatorler


def fibonacci():

    a = 1
    b = 1
    yield a
    yield b

    while True:

        a, b = b, a+b

        yield b

for sayi in fibonacci():

    if (sayi > 100000):
        break
    print(sayi)

    

















