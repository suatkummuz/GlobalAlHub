import random

name = input("isminiz")
print("adam asmaya hoşgeldiniz", name)
word = ["araba", "traktör", "motorsiklet", "bisiklet", "jip", "suv"]
new = list(random.choice(word))
ek = [" "] * len(new)
claim = 7
fnl = 0
snc = False

while claim != 0:
    chosen = input("lütfen kelime giriniz")
    for i in new:
        fnl += 1
        if i == chosen:
            snc = True
            ek[fnl - 1] = chosen
        if " " not in ek:
            print("tebrikler", name)
            cevap = input("çıkmak istiyormusunuz ?  ['e' veya 'h'] :")
            if cevap == "e":
                print("çıktınız")
                exit()
    if snc == False:
        claim -= 1
        print("hatalı kelime")
        print(claim, "doğru", name)

    if claim == 0 and " " in ek:
        print("oyunu kaybettiniz", name)
        cevap = input("çıkmak istiyormusunuz ?  ['e' veya 'h'] :")
        if cevap == "e":
            print("çıktınız")
        if cevap == "h":
            tahmin = input("Kelimenin tamamını yahmin edebilirsiniz. Bir hakkınız var")
            if tahmin == new:
                print("Tebrikler bildiniz")
                break
            else:
                print("Bilemediniz ve kaybettiniz")
                break

    fnl = 0
    snc = False
    print(ek)
