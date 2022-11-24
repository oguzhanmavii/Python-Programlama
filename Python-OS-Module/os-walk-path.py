import os


# for anadizin,resimler,dosya.doc,dosya.jpeg,dosya.txt,dosya.xls in os.walk('anadizin'):
#     print(dosyalar)

#yöntem1
for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    print(dosyalar)


# for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):  #yöntem2
    

    