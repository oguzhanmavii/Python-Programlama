#file Handling 

#Dosya işleme, herhangi bir web uygulamasının önemli bir parçasıdır.
#Python'un dosya oluşturmak, okumak, güncellemek ve silmek için çeşitli işlevleri vardır.


#Dosya yönetimi
#Python'da dosyalarla çalışmanın temel işlevi open()işlevdir.

#Fonksiyon open()iki parametre alır; dosya adı ve mod .

#Bir dosyayı açmak için dört farklı yöntem (mod) vardır:

#"r"- Oku - Varsayılan değer. Okumak için bir dosya açar, dosya yoksa hata verir

#"a"- Ekle - Eklemek üzere bir dosya açar, mevcut değilse dosyayı oluşturur

#"w"- Yaz - Yazmak için bir dosya açar, yoksa dosyayı oluşturur

#"x"- Oluştur - Belirtilen dosyayı oluşturur, dosya varsa bir hata döndürür

#Ek olarak, dosyanın ikili veya metin modu olarak mı ele alınması gerektiğini belirleyebilirsiniz.

#"t"- Metin - Varsayılan değer. Metin modu

#"b"- İkili - İkili mod (örn. resimler)
import os ## dosya okuma işlemleri için kullanılan kütüphane bu kütüphane import edilmek zorundadır !
import glob
## file write
target_path=open("E://github/Python-Programlama-//Dosyalar_ile_Calismak//file.txt","w")#burada hedef klasöre gitmeniz gerekir yoksa program patlıyor o yüzden bütün dizinleri tek tek belirtiniz !
target_path.write("python file creation completed successfully")#oluşturuduğumuz txt dosyasına veri yazdık
target_path.close()#oluşturduğumuz dosya ile işlem yapılmayacağı için kapattık


## file read 
target_path=open("E://github/Python-Programlama-//Dosyalar_ile_Calismak//file.txt","r")
print(target_path.read())#burada oluşturduğumuz dosya içindeki veriyi python console üzerinden erişiyoruz 
print(target_path.read(5))#burada oluşturduğumuz dosya içindeki verinin 5 karakterini okuyoruz 
target_path.close()

## file append
target_path=open("E://github/Python-Programlama-//Dosyalar_ile_Calismak//file.txt","a")
target_path.write("\nPython Programming Learning Intro")#burada oluşturulan dosyanın içerisinde bulunan veri haricinde yeni bir veriyi dosyaya ekliyoruz
target_path.write("\nPython Programming Learning Advanced")
target_path.close()

## file delete
##burada ilk başta dosyayı oluşturduk o yüzden silme işlemi yapılmadı
##programı 2.kez çalıştırmadan önce target_path2=open() yazan satırı yorum satırı yapın dosya silinecektir
##programı 3.kez çalıştırdığınızda dosyayı sildiği için aşağıdaki "The file does not exist" tırnak içine aldığım yazıyı python console'da göreceksiniz
target_path2=open("E://github/Python-Programlama-//Dosyalar_ile_Calismak//file2.txt","w")## dosya oluşturuldu
if os.path.exists("E://github/Python-Programlama-//Dosyalar_ile_Calismak//file2.txt"):
  os.remove("E://github/Python-Programlama-//Dosyalar_ile_Calismak//file2.txt")
else:
  print("The file does not exist")



## Remove Folder

# import os
# os.rmdir("myfolder") 

##buradaki gibi yapılmaktadır
