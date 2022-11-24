import os
#os.stat() os modülünün stat() fonksiyonu dosyalar hakkında bilgi almamızı sağlar.
#Bu fonksiyonu kullanarak bir dosyanın boyutunu, oluşturulma tarihini,
#değiştirilme tarihini ve erişilme tarihini sorgulayabiliriz.
dosya= os.stat('/home/oguzhan/Desktop/python-os')

print(dosya)#dosyaya ait tüm bilgileri verir

#Burada özellikle işimize yarayacak olan nitelikler şunlardır:

#st_atime dosyaya en son erişilme tarihi

#st_ctime dosyanın oluşturulma tarihi (Windows’ta)

#st_mtime dosyanın son değiştirilme tarihi

#st_size dosyanın boyutu

print("------")
print('boyutu:',dosya.st_size,'byte')
print("------")
print('boyutu:',dosya.st_size/1024,'Kilobyte')
print("------")
print('olusturulma tarihi:',dosya.st_ctime)#oluşturulma tarihi
print("------")
print('erişilme tarihi:',dosya.st_atime)#erişilme tarihi
print("------")
print('erişilme tarihi:',dosya.st_mtime)#değiştirme tarihi


#not GNU/Linux’ta bir dosyanın ne zaman oluşturulduğunu öğrenmek mümkün değildir.
#Dolayısıyla dosya.st_ctime komutu yalnızca Windows’ta bir dosyanın oluşturulma tarihi verir.
#Bu komutu GNU/Linux’ta verdiğimizde elde edeceğimiz şey dosyanın son değiştirilme tarihidir.
