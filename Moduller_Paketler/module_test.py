from imp import reload
import module
module.yaz("Python!!!")
#Bir modül, import sayısına bakılmaksızın yalnızca bir kez yüklenir.
#Birden fazla import gerçekleşse bile
#modül yürütmesinin tekrar tekrar gerçekleşmesini engeller.
# from … import ifadesi
#Python’un deyimiyle, bir modülden belirli öznitelikleri geçerli
#ad alanına import etmemize izin verir.
#from … import sözdizimi:
from fib import fibonacci
from modname import *


# Alan adları (Namespace) ve Kapsam Belirleme
#Değişkenler, nesnelere eşlenen tanımlayıcılardır
#Ad alanı, değişken adların (anahtarların) ve karşılık gelen
#nesnelerinin (değerleri) içeren bir sözlüktür.
#Bir Python ifadesi, yerel ad alanında ve global ad alanında değişkenlere
#erişebilir. Yerel ve genel değişken aynı ada sahipse,
#yerel değişken genel değişkeni gölgeler.
#Her fonksiyonun kendi yerel ad alanı vardır.
#Sınıf metotları, bir fonksiyonla aynı kapsam belirleme kuralını izler.
#Bir fonksiyonda bir değer atanmış herhangi bir değişkenin yerel olduğunu
#varsayar. Bu nedenle, bir fonksiyon içindeki bir global değişkene
#bir değer atamak için, önce genel ifadeyi kullanmalısınız.
#Bir örnek üzerinden görelim.
global Para

Para=2000
def ParaEkle(Para):
   Para =Para+1

print(Para)
print(ParaEkle(Para))

#dir() fonksiyonu
#Direkt Python içinde bulunan dir() fonksiyonu,
#bir modül tarafından tanımlanan adları içeren
#sıralanmış bir dizeler listesi döndürür.
#Liste, bir modülde tanımlanan tüm modüllerin,
#değişkenlerin ve fonksiyonların isimlerini içerir.
#Örneğin harici math kütüphanesi kodumuza import edelim
#ve bu modül içindeki modül, değişken ve fonksiyonlara ulaşalım.

import math
icerik=dir(math)
print(icerik)

#reload() fonksiyonu
#Modül bir koda import edildiğinde, bir modülün üst düzeyindeki kod
#sadece bir kez yürütülür. Eğer modülü yeniden yüklemek isterseniz,
#reload() fonksiyonunu kullanabilirsiniz.
#Kısacası, reload() fonksiyonu daha önceden yüklenen modülleri
#tekrar yüklemek için kullanılır.  Sözdizimi:

reload(math)



import dizin

from dizin import dosya1
dosya1.dosya1()

from dizin import dosya2
dosya2.dosya2("Deneme")

from dizin import dosya3
dosya3.dosya3("Test")
