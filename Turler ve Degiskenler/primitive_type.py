#String Kullanimi
print("Merhaba Python Programlama Derslerine Hoşgeldiniz")
print("Bu Eğitimde Sıfırdan İleri Seviyeye Kadar Gideceğiz")

karakter="Bu Bir String İfadedir"

coklu_karakter="""Burda Birden Fazla Karakter kullanıp Alt Satırlara inme İşlemide Gerçekleştiriceğiz
Örnekte Olduğu gibi Cok Satirli bir Karakter Tanimlama İslemi Yaptık
Bunun Gibi Birden Fazla Örnek Vermek Mümkündür.
"""

slicess="Merhaba Dünya"

print(slicess[:3])


upper_string="Python Programlama Dili"
print(upper_string.upper)

lower_string="PYTHON OPENCV ISLEMLERI"
print(lower_string.lower)

strip_islemi="Deneme,islemi!"
print(strip_islemi.strip)


# replaces="Merhaba,Dünya"
# print(replaces("M","T"))

#String Concatenation

isim="Oguzhan"
soyisim="Mavi"
tamisim=isim+soyisim
print(tamisim)

metin_uzunlugu="Herhangi Bir Metin Uzunlugu"
print(len("Metin Uzunlugu:"+metin_uzunlugu))


#İnt İşlemleri
#burda string tipindeki 105 i tam sayı olarak çağırdık
tamsayi= int('105')
print(tamsayi)

#İnt İşlemleri2 float bir sayiyi int olarak çağırdık
tamsayi2=int(225.2555668494618489)
print(tamsayi2)



#float işlemleri
#int bir sayiyi float  olarak çağırdık
ondaliklisayi=float(8)
print(ondaliklisayi)


#complex kulanimi
#Verilen argümanları kullanarak complex sayılar
#üretmemize imkan tanıyan bir fonksiyon olduğunu resmi dokümantasyonda görebilmekteyiz.
#Bu fonksiyon gerçek ve hayali kısımları verildiği zaman size karmaşık bir sayı döndürür.
#Normalde iki parametre alır. Ancak birinci parametrenin string olduğu durumlarda
# 2. parametre gönderilmemelidir.

complexSayi=complex(3)
print(complexSayi)


complexSayi= complex(1,1)
print(complexSayi)

#+ yani toplama işaretini koymasaydık ne olurdu?
#Yani önceki örneklerde olduğu gibi virgül koysaydık? Aşağıdaki hatayı alırdık.
c2 = complex('1+1j')
print(c2)
#Çıktı olarak yukarıdaki hatanın aksine TypeError fırlatılacaktır.
c4 = complex('1+1j', 1)
print(c4)