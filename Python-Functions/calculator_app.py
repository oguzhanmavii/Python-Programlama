import time

def Menu()-> None:
    print("-----------------------Hesap Makinesi Menüsüne Hoşgeldiniz-----------------------")
    print("1.)Toplama")
    print("2.)Çıkarma")
    print("3.)Çarpma")
    print("4.Bölme")
    print("5.Çıkış")



def MenuLoop() -> str:
    while True:
        Menu()
        secim= input("Secim (1-5):")
        print("\n")

        if secim.isdigit() and int(secim)>=1 and int(secim)<=5:
            break
    return secim



def MainLoop() -> None:
    while True:
        secim=MenuLoop()
        if secim=="1":
            s1=int(input("1.sayi :"))
            s2=int(input("2.sayi :")) 
            print("Hesap Makinesi Toplama İşlemi Yapıyor Lütfen Bekleyiniz...")
            time.sleep(2)
            print(s1,"+",s2,"=",Sum(s1,s2))
        elif secim=="2":
            s1=int(input("1.sayi :"))
            s2=int(input("2.sayi :")) 
            print("Hesap Makinesi Çıkarma İşlemi Yapıyor Lütfen Bekleyiniz...")
            time.sleep(2)
            print(s1,"-",s2,"=",Extraction(s1,s2)) 
        elif secim=="3":
            s1=int(input("1.sayi :"))
            s2=int(input("2.sayi :")) 
            print("Hesap Makinesi Çarpma İşlemi Yapıyor Lütfen Bekleyiniz...")
            time.sleep(2)
            print(s1,"*",s2,"=",Multiplication(s1,s2))
        elif secim=="4":
            s1=int(input("1.sayi :"))
            s2=int(input("2.sayi :")) 
            print("Hesap Makinesi Bölme İşlemi Yapıyor Lütfen Bekleyiniz...")
            time.sleep(2)
            print(s1,"/",s2,"=",Divided(s1,s2))
        elif secim=="5":
            break


#Toplama Fonksiyonumuz Bu İşlemi Görecek    
def Sum(sayi1,sayi2)->int:
    return sayi1+sayi2    


#Çıkarma Fonksiyonumuz Bu İşlemi Görecek 
def Extraction(sayi1,sayi2)->int:
    return sayi1-sayi2    


#Çarpma Fonksiyonumuz Bu İşlemi Görecek 
def Multiplication(sayi1,sayi2)->int:
    return sayi1*sayi2    


#Bölme Fonksiyonumuz Bu İşlemi Görecek 
def Divided(sayi1,sayi2)->int:
    return sayi1/sayi2



MainLoop()