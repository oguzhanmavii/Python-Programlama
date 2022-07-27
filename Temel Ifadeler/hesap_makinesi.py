import time
#Toplama Fonksiyonumuz Bu İşlemi Görecek 
def Sum(sayi1,sayi2):
    return sayi1+sayi2

#Çıkarma Fonksiyonumuz Bu İşlemi Görecek 
def Extraction(sayi1,sayi2):
    return sayi1-sayi2
#Çarpma Fonksiyonumuz Bu İşlemi Görecek 
def Multiplication(sayi1,sayi2):
    return sayi1*sayi2    

#Bölme Fonksiyonumuz Bu İşlemi Görecek 
def Divided(sayi1,sayi2):
    return sayi1/sayi2



print("-----------------------Hesap Makinesi Menüsüne Hoşgeldiniz-----------------------")
print("1.)Toplama")
print("2.)Çıkarma")
print("3.)Çarpma")
print("4.Bölme")
secim=input("Yapacağınız İşlemini Seçiniz :") # ilk başta yapılacak İşlemi Seçiyoruz !

s1=int(input("1.sayi :")) # ardından ilk sayiyi girmemiz için bir değer alınıyor...
s2=int(input("2.sayi :")) # ardından ikinci sayiyi girmemiz için bir değer alınıyor...

if secim =='1':
    print("Hesap Makinesi Toplama İşlemi Yapıyor Lütfen Bekleyiniz...")
    time.sleep(2)
    print(s1,"+",s2,"=",Sum(s1,s2))
    devam=input("1-)Tekrar İşlem Yap\n2-)Çıkış\n")
    if(devam=="1"):
        secim=input("Yapacağınız İşlemi Seçiniz :")


elif secim=='2':
    print("Hesap Makinesi Çıkarma İşlemi Yapıyor Lütfen Bekleyiniz...")
    time.sleep(2)
    print(s1,"-",s2,"=",Extraction(s1,s2)) 

elif secim=='3':
    print("Hesap Makinesi Çarpma İşlemi Yapıyor Lütfen Bekleyiniz...")
    time.sleep(2)
    print(s1,"*",s2,"=",Multiplication(s1,s2))

elif secim=='4':
    print("Hesap Makinesi Bölme İşlemi Yapıyor Lütfen Bekleyiniz...")
    time.sleep(2)
    print(s1,"/",s2,"=",Divided(s1,s2))
