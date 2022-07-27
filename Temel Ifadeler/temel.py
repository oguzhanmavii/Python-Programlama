
#if elif ve else kullanımı

#ogrenci not sistemi if elif ve else ile kontrol işlemleri
from re import X
from typing import final
vize_notu=input("Vize Notunuzu Giriniz:")
vize_notu=int(vize_notu)

final_notu=input("Final Notunuzu Giriniz:")
final_notu=int(final_notu)

ortalama=(vize_notu*40+final_notu*60)/100

if ortalama>=45:
    print("Tebrikler Dersi Geçtiniz")

else:
     print("Malesef Bu Dersten Kaldınız")
#----------------------------------------------------------#

#yas ortalamasına göre hesap yapma islemi
yas=input("Lütfen Yaşınızı Giriniz:")
yas=int(yas)

if yas<8:
    print("Siz daha çocuksunuz")

elif yas>=8 & yas<=30:
    print("Siz Şuanda Gençsiniz")

elif yas>30 & yas<=50:
    print("Siz Artık Olgun Bir İnsansınız")

elif yas>50 & yas<90:
    print("Siz Artık Bir Yaşlısınız")

else:
    print("Siz Belirtilen Aralıkların Dışında Çok Uzun Yıllar Yaşayan Bir İnsansınız")

#break ve continue kullanımı

for val in "python turkiye":
    if val =="t":
        break

    print(val)

print("break ile t harfini görünce döngüyü bitirdik.")



#while döngüsü kullanımı
a=1
b=15
while a<b:
    print(a)
    a+=1

#burada string içindeki deyimin tamanını alarak
# 1 eksilte eksilte içerideki ifade bitene kadar döngü çalışacak
strings="Merhaba"
while strings:
    print(strings)
    strings= strings[:-1]

#forve continue iç içe tanımlamak    
for val in "pythontr":
    if val == "t":
        continue
    print(val)
 
print("Bitti")

