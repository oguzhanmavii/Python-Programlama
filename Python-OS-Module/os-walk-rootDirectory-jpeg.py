import os 


print('JPEG Dosyaları')
print('-----------------------------')
for kökdizin,altdizinler,dosyalar in os.walk('anadizin'):# burada kökdizin yapisi olusturuluyor altinda altdizinler ve onun altında dosyalar folder yapisi yeralmaktadir
    for dosya in dosyalar: #dosyalar folderimize yani kökdizinin en tabanında olan elemamlari cagiriyoruz
        if dosya.endswith('.jpeg'):#burada elemanlari cagirirken hepsini degil uzantisi .jpeg olanlari istedigimizi belirtiyoruz
            print(dosya)#cektigimiz bütün elemanları ekranda gösteriyoruz
print('-----------------------------')




print('PDF Dosyaları')
for kökdizin,altdizinler,dosyalar in os.walk('anadizin'):# burada kökdizin yapisi olusturuluyor altinda altdizinler ve onun altında dosyalar folder yapisi yeralmaktadir
    for dosya in dosyalar: #dosyalar folderimize yani kökdizinin en tabanında olan elemamlari cagiriyoruz
        if dosya.endswith('.pdf'):#burada elemanlari cagirirken hepsini degil uzantisi .pdf olanlari istedigimizi belirtiyoruz
            print(dosya)#cektigimiz bütün elemanları ekranda gösteriyoruz
print('-----------------------------')



print('MP3 Dosyaları')
for kökdizin,altdizinler,dosyalar in os.walk('anadizin'):# burada kökdizin yapisi olusturuluyor altinda altdizinler ve onun altında dosyalar folder yapisi yeralmaktadir
    for dosya in dosyalar: #dosyalar folderimize yani kökdizinin en tabanında olan elemamlari cagiriyoruz
        if dosya.endswith('.mp3'):#burada elemanlari cagirirken hepsini degil uzantisi .mp3 olanlari istedigimizi belirtiyoruz
            print(dosya)#cektigimiz bütün elemanları ekranda gösteriyoruz
print('-----------------------------')



print('ZIP Dosyaları')
for kökdizin,altdizinler,dosyalar in os.walk('anadizin'):# burada kökdizin yapisi olusturuluyor altinda altdizinler ve onun altında dosyalar folder yapisi yeralmaktadir
    for dosya in dosyalar: #dosyalar folderimize yani kökdizinin en tabanında olan elemamlari cagiriyoruz
        if dosya.endswith('.zip'):#burada elemanlari cagirirken hepsini degil uzantisi .zip olanlari istedigimizi belirtiyoruz
            print(dosya)#cektigimiz bütün elemanları ekranda gösteriyoruz
print('-----------------------------')

print('DOC Dosyaları')
for kökdizin,altdizinler,dosyalar in os.walk('anadizin'):# burada kökdizin yapisi olusturuluyor altinda altdizinler ve onun altında dosyalar folder yapisi yeralmaktadir
    for dosya in dosyalar: #dosyalar folderimize yani kökdizinin en tabanında olan elemamlari cagiriyoruz
        if dosya.endswith('.doc'):#burada elemanlari cagirirken hepsini degil uzantisi .doc olanlari istedigimizi belirtiyoruz
            print(dosya)#cektigimiz bütün elemanları ekranda gösteriyoruz
print('-----------------------------')


print('OGG Dosyaları')
for kökdizin,altdizinler,dosyalar in os.walk('anadizin'):# burada kökdizin yapisi olusturuluyor altinda altdizinler ve onun altında dosyalar folder yapisi yeralmaktadir
    for dosya in dosyalar: #dosyalar folderimize yani kökdizinin en tabanında olan elemamlari cagiriyoruz
        if dosya.endswith('.ogg'):#burada elemanlari cagirirken hepsini degil uzantisi .ogg olanlari istedigimizi belirtiyoruz
            print(dosya)#cektigimiz bütün elemanları ekranda gösteriyoruz
print('-----------------------------')


print('XLS Dosyaları')
for kökdizin,altdizinler,dosyalar in os.walk('anadizin'):# burada kökdizin yapisi olusturuluyor altinda altdizinler ve onun altında dosyalar folder yapisi yeralmaktadir
    for dosya in dosyalar: #dosyalar folderimize yani kökdizinin en tabanında olan elemamlari cagiriyoruz
        if dosya.endswith('.xls'):#burada elemanlari cagirirken hepsini degil uzantisi .pdf olanlari istedigimizi belirtiyoruz
            print(dosya)#cektigimiz bütün elemanları ekranda gösteriyoruz
print('-----------------------------')