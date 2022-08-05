#base exceptions
from ast import Str


while True:
    sayi=input("Bir Sayi Giriniz:")
    if not sayi:
        break
    try:
        sayi2=float(sayi)
    except ValueError:##hata yakaladığımız noktada aşagıdaki uyarıyı verecektir
        print("Geçersiz değer")
        continue
    print("Karesi Alınan Sayi:",sayi2**2)


while True:
    x = input("Bir sayı girin: ")
    if not x:
        break
    try:
        y = 1/float(x)
    except:
        print("Geçersiz sayı")
        continue
    print(y)

while True:
    x = input("Bir sayı girin: ")
    if not x:
        break
    try:
        y = 1/float(x)
    except ValueError:
        print("Geçersiz sayı")
        continue
    except ZeroDivisionError:
        print("Sıfıra bölme")
        continue
    print(y)
    
try:
    2.5**1000
except OverflowError:
    print("İşlem çok büyük.")
except ZeroDivisionError:
    print("Sıfıra bölme.")


def faktoriel(x):
    x = int(x)    
    if x<0:
        raise ValueError("Negatif değer")
    p = 1
    for i in range(1,x+1):
        p *= i
    return p



def faktoriel(x):
    x = int(x)    
    if x<0:
        raise ValueError("Negatif değer")
    p = 1
    for i in range(1,x+1):
        p *= i
    return p

