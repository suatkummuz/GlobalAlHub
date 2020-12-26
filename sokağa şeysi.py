isim        = input("isiminizi giriniz:")
soyisim     = input("soyadınızı giriniz:")
yas         = input("yaşınızı giriniz:")
dogumyili = input("doğum yılınızı giriniz:")

userInfo = [isim,soyisim,yas,dogumyili]
for ele in userInfo:
    print(ele,"\n")
if int(yas) >= 18:
    print("sokağa çıkabilirsin")
else:
    print("sokağa çıkamazsın çok tehlikeli")