import os
#tanım:os.makedirs() ise os.mkdir() fonksiyonunun aksine,
#varolmayan üst ve alt dizinleri de oluşturma yeteneğine sahiptir. Örneğin /home/oguzhan/naber  

file_create=input('olusturacaginiz klasör ismini giriniz:')
os.makedirs(file_create)


