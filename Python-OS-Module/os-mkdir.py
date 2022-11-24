#os.mkdir()  os modülünün mkdir() fonksiyonu yeni dizinler oluşturabilmemizi sağlar.
import os
import sys
result=input("olusturulacak dosya adini giriniz:")

os.mkdir(result)
result2= os.listdir()
print(result2)
