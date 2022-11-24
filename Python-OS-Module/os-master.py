import os 

def dosya_tara(dizin):
    baslangic=os.getcwd()#bulundugumuz dizinin konumunu baslangic'a atadik
    dosyalar=[]#dosyalar isminde boş bir liste oluşturduk
    os.chdir(dizin)#Daha sonra, tara() fonksiyonuna parametre olarak verilen dizin adlı dizinin içine giriyoruz


    for nesne in os.listdir(os.curdir):#mevcut dizin içindeki bütün öğeleri listdir() fonksiyonu ile tek tek tarıyoruz
        if not os.path.isdir(nesne):#os.path.isdir() fonksiyonu. Bu fonksiyon, kendisine parametre olarak verilen bir değerin dizin olup olmadığını tespit etmemizi sağlıyor.
            dosyalar.append(nesne)
        else:
            dosyalar.extend(dosya_tara(nesne))

    os.chdir(baslangic)
    return dosyalar

test='/home/oguzhan/Desktop/python-os/'

dosya_tara(test)