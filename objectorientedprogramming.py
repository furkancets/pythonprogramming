import random
import time

class Command():

    def __init__(self, tv_durum= "Kapalı", tv_ses= 0 , kanal_listesi = ["Trt"],kanal = "Trt"):

        self.tv_durum =tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):

        if (self.tv_durum =="Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):

        while True:
            cevap = input("Sesi Azalt:  '<'\nSesi Arttır: '>'\nÇıkış : çıkış")

            if (cevap == "<"):
                if(self.tv_ses != 0):

                    self.tv_ses -= 1
                    print("Ses",self.tv_ses)
            elif (cevap == ">"):
                if(self.tv_ses != 31):

                    self.tv_ses +=1

                    print("Ses:", self.tv_ses)
            else:
                print("Ses Güncellendi:", self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):

        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal eklendi...")

    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şuan ki kanal listesi:", self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return f"Tv Durumu: {self.tv_durum}\nTv Ses: {self.tv_ses}\nKanal_listesi: {self.kanal_listesi}\nŞuan ki kanal: {self.kanal}\n"

command = Command()

print("""

Televizyon Uygulaması


1.Tv Aç

2.Tv Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal Sayısını Öğrenme

6.Rastgele Kanala Geçme

7.Televizyon Bİlgileri

Çıkmak için 'q' ya basın.

""")

while True:

    işlem = input("İşlem Seçiniz:")

    if (işlem == 'q'):
        print("İşlem Sonlandırılıyor...")
        break

    elif (işlem == "1"):
        command.tv_ac()
    elif (işlem == "2"):
        command.tv_kapat()
    elif (işlem == "3"):
        command.ses_ayarları()
    elif (işlem == "4"):

        kanal_işlemleri = input("Kanal işlemlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_işlemleri.split(",")

        for eklenecekler in kanal_listesi:
            command.kanal_ekle(eklenecekler)

    elif (işlem == "5"):

        print("Kanal Sayısı:", len(command))

    elif (işlem == "6"):

        command.rastgele_kanal()

    elif (işlem == "7"):

        print(command)

    else:
        print("Geçersiz İşlem...")

