#functions
#fonksiyon yalnızca çağrıldığında çalışan bir kod bloğudur.
#Parametre olarak bilinen verileri bir fonksiyon'a geçirebilirsiniz.
#Bir fonksiyon, sonuç olarak veri döndürebilir.
def functions():
    print("Merhaba Bu Benim Fonksiyonum")

functions()

print("--------------Parameters--------------")
def fonksiyon(ad,soyad): ## not bu fonksiyon parametre alır
    print(ad+" "+soyad)

fonksiyon("Oguzhan","Mavi") ##burada aldıgı parametreleri çağırmanız gerekir !


def fonksiyon2(*kids):
    print("En Küçük Çocuk"+kids[2])


fonksiyon2("Ali","Ayvazoğlu ","\tAyşe")
def hesapMakinesi(sayi1,sayi2):
     return sayi1+sayi2

sayi1=int(input("1.sayi :"))
sayi2=int(input("2.sayi :")) 

def hesapSonuc():
     print("Sonuc:",hesapMakinesi(sayi1,sayi2))

hesapSonuc()



def my_country(country = "***** Turkey *****"):
  print("I am from " + country)

my_country("Sweden")
my_country("India")
my_country()
my_country("Brazil")


print("--------------Argüments--------------")
#Bir Listeyi Argüman Olarak Geçmek


def function_arguments(food):
    for meal in food:
        print(meal)

fruits=["apple","strawberry","kiwi","banana","orange","melon"]

function_arguments(fruits)



def  multiplication(number):
    return 5 * number


print(multiplication(3))
print(multiplication(7))
print(multiplication(9))


#Boş Geçme işlemi yapılıyor
def bos_gec():
    pass



#functions Recursion özyineleme
 
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)