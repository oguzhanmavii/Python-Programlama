import os 
komut=input('komutunuzu giriniz:')

result=os.system(komut) ## girdigimiz komut terminalde yazdığımız işi yapar

print(result)