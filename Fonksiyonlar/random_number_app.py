#Belirli Bir Aralıkta Rastgele Sayi Üretme Uygulaması
#1.yöntem Döngüsüz Keyword ile Kısayol Fonksiyonları ile 
import random
uretilecek_rastgele_sayi=int(input("Üretilecek Rastgele Sayi Miktarini Giriniz:"))
baslangic_degeri=int(input("Baslangic Sayisini Giriniz:"))
bitis_degeri=int(input("Bitis Degerini Giriniz:"))

rastgele_sayi_uretme=random.sample(range(baslangic_degeri,bitis_degeri),uretilecek_rastgele_sayi)
print("Üretilen Rastgele Sayilar:",rastgele_sayi_uretme)  

#Belirli Bir Aralıkta Rastgele Sayi Üretme Uygulaması
#2.yöntem Döngü ile Fonksiyon Kullanmadan 
baslangic=int(input("Baslangic Degeri:"))
bitis=int(input("Bitis Degeri:"))
random_sayi_miktari=int(input("Kaç Adet:"))
for elements in range(random_sayi_miktari):
    print(random.randint(baslangic,bitis))