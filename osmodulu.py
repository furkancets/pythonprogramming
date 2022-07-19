import os
from datetime import datetime
dir(os)

print(dir(os))

print(os.getcwd())

os.chdir("C:/Users/Asus/Desktop")

print(os.listdir())

for i in os.listdir():
    print(i)

print(os.getcwd())

os.chdir("C:/Users/Asus/PycharmProjects/pythonprogramming/")

os.mkdir("Deneme1")

#os.mkdir("Deneme2/Deneme3")

os.makedirs("Deneme2/Deneme3")

os.rmdir("Deneme2/Deneme3")

os.mkdir("Deneme2/Deneme3")

os.rmdir("Deneme1")

os.removedirs("Deneme2/Deneme3")

os.rename("test.txt", "test1.txt")

print(os.stat("test1.txt").st_mtime)

print(datetime.fromtimestamp(os.stat("test1.txt").st_mtime))

print(os.walk("C:/Users/Asus/Desktop"))

for i in os.walk("C:/Users/Asus/Desktop"):
    print(i)

for klasor_yolu, klasor_isimleri, dosya_isimleri in os.walk("C:/Users/Asus/Desktop"):
    print("Klasor Yolu", klasor_yolu)
    print("Klasor isimleri", klasor_isimleri)
    print("Klasor dosya", dosya_isimleri)
    print("************************")

for klasor_yolu, klasor_isimleri, dosya_isimleri in os.walk("C:/Users/Asus/Desktop"):
    for i in dosya_isimleri:
        print(i)

for klasor_yolu, klasor_isimleri, dosya_isimleri in os.walk("C:/Users/Asus/Desktop"):
    for i in dosya_isimleri:
        if (i.endswith(".txt")):
            print(i)