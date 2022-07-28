import pickle
import os
from typing import List
def Menu()-> None:
   print("1. Kayıtları Listele")
   print("2. Kayıt Ara")
   print("3. Kayıt Ekle")
   print("4. Kayıt Sil")
   print("5. Çıkış")


def MenuLoop()  -> str:
    while True:
        Menu()
        secim= input("Secim (1-5):")
        print("\n")

        if secim.isdigit() and int(secim)>=1 and int(secim)<=5:
            break
    return secim


def MainLoop() ->None:
    while True:
        secim=MenuLoop()
        if secim=="1":
            ListRecords()
        elif secim=="2":
            SearchRecord()
        elif secim=="3":
            AddRecord()
        elif secim=="4":
            DeleteRecord()
        elif secim=="5":
            break


def ListRecords() -> None:
    recordList= ReadFile()
    for record in recordList:
        print(f"{record.get('isim', ' ')}")


def SearchRecord() -> None:
    pass

def AddRecord() -> None:
    print("Yeni Kayıt Ekle")
    isim=input("İsim:")
    soyisim=input("Soyisim:")
    telnumber=input("Telefon Numarasi:")
    print(f"Yeni kayit: {isim},{soyisim},{telnumber}")
    if AreYouSure():
        AddRecordToFile(isim,soyisim,telnumber)
        print("Kayıt eklendi.\n")
        


def DeleteRecord() -> None:
    pass


def AreYouSure() ->bool:
    while True:
        sor = input("Eminmisiniz ?(E)vet/(H)ayır")
        print()
        if sor.upper() =="E":
            return True
        elif sor.upper() =="H":
            return False    


def ReadFile() -> list:
    if os.path.isfile("data.bin"):
        with open("data.bin","rb") as fileObject:
            recordsList=pickle.load(fileObject)

    else:
        recordsList = List()
    return recordsList


def WriteFile(recordListParam : list) -> None:
    with open("data.bin","wb") as fileObject:
        pickle.dump(recordListParam,fileObject)


def AddRecordToFile(isimParam : str, soyisimParam : str, telnumberParam : str) -> None:
    recordsList = ReadFile()
    recordDict = dict(isim = isimParam ,soyisim = soyisimParam ,telnumber = telnumberParam)
    recordsList.append(recordDict)
    WriteFile(recordsList)



MainLoop()