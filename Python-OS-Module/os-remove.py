import os 
#os modülünün remove() adlı fonksiyonu, bilgisayarımızdaki dosyaları silmemizi sağlar
#Not:Yalnız bu komutu çok dikkatli kullanmalısınız. Çünkü bu komut, 
#silme işleminden önce herhangi bir soru sormadan, dosyayı doğrudan siler.
delete_folder=os.remove('created')

#os.rmdir()
#os modülünün rmdir() fonksiyonu, içi boş bir dizini silmek için kullanılır
rmdir_folder=os.rmdir('empty')

#not:Eğer silmeye çalıştığınız dizin içinde herhangi 
#başka bir dizin veya dosya varsa bu fonksiyon hata verecektir..
