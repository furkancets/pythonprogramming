import sys

#print("ok")

#print(dir(sys))

#sys.stderr.write("Bu bir hata mesajıdır\n")

#sys.stderr.flush()

#sys.stdout.write("Bu normal bir yazıdır\n")


#print(sys.argv)

#for i in sys.argv:
#    print(i)


def kok_bulma(a,b,c):
    delta = b ** 2 - 4 * a * c

    if (delta < 0):
        print("Reel Kök Yok.")
    else:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        return (x1,x2)


if len(sys.argv) == 4:
    print("Kök bulma", kok_bulma(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler girin")
    sys.stderr.flush()




