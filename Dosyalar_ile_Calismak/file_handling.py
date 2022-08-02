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

f=open("DosyalarİleCalismak/demofile.txt")

f = open("DosyalarİleCalismak/demofile.txt", "rt")


