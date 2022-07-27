#karakter uzunlugu bulma 
nesne="Araba"

uzunluk=len(nesne)

print(uzunluk)
print(nesne,uzunluk)

#girilen karakter e göre indislerine ayırıp karakterlerin pozisyonlarını belirleme
isim=input("isminiz :")

for i in range(len(isim)):
    print("İsminiz {}. harfi : {}".format(i+1,isim[i]))