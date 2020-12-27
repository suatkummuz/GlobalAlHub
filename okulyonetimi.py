import random

ad = "suat"
soyad = "kummuz"
giris_hakki = 3
dersler = []

while True:

    giris_ad = input("Adınız: ")
    giris_soyad = input("Soyadınız: ")
    print("__________________")

    if giris_ad == ad and giris_soyad == soyad:
        print("Hoş Geldiniz.")
        print(" ")
        adet = int(input('Kaç ders almak istersiniz: '))
        i = 0
        if adet <= 5 and adet >= 3:
            while (i < adet):
                ders = input("Eklemek İstediğiniz Ders: ")
                dersler.append(ders)
                i += 1
                continue
            print(" ")
            print("Sorumlu Olduğunuz Dersler: ", dersler)
            print(" ")
        elif adet >= 5:
            print("En fazla 5 ders alabilirsiniz!")
            break
        else:
            print("Kaldınız! En az 3 ders almalısınız!")
            break

        secilen_ders = random.choice(dersler)
        print("Sorumlu Olduğunuz Ders:", secilen_ders)
        notlar = {"vize": 34, "final": 70, "proje": 87}
        derece = ((notlar["vize"] * 3 / 10) + (notlar["final"] * 5 / 10) + (notlar["proje"] * 2 / 10))

        if (derece >= 90):
            print("Ders notunuz: AA")
        elif (derece >= 89 and derece >= 70):
            print("Ders notunuz: BB")

        elif (derece >= 69 and derece >= 50):
            print("Ders notunuz: CC")

        elif (derece >= 49 and derece >= 30):
            print("Ders notunuz: DD")

        elif (derece >= 29):
            print("Ders notunuz FF, KALDINIZ. ")

        else:
            print("Dersten kaldınız, geçmiş olsun :(")
        break

    elif giris_ad != ad and giris_soyad != soyad:
        print("Yanlış giriş yaptınız... ")
        giris_hakki -= 1

        print("Kalan giriş hakkı: ", giris_hakki)
        print(" ")
    else:
        print("Yanlış giriş yaptınız... ")
        giris_hakki -= 1
        print("Kalan giriş hakkı: ", giris_hakki)
        print(" ")
    if giris_hakki == 0:
        print("Giriş Hakkınız kalmamıştır!")
        break