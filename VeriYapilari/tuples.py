#Tuple'lar, birden çok öğeyi tek bir değişkende saklamak için kullanılır.

#Tuple, Python'da veri koleksiyonlarını depolamak için kullanılan 4 yerleşik veri türünden biridir, diğer 3'ü List , Set ve Dictionary olup tümü farklı niteliklere ve kullanıma sahiptir.

#Tuple, sıralı ve değiştirilemez bir koleksiyondur .

#Tuples yuvarlak parantez ile yazılır.

mytuple=("Öğrenci","Öğretmen","Müdür")

print(mytuple)



operationSystems=("Android","Linux","Unix","Windows","Pardus")
print(operationSystems)
print(len(operationSystems))


tuple1=("Bilgisayar","Çanta","Kitap","Kalem","Silgi")
tuple2=(1,3,5,7,9)
tuple3=(True,False,False,True,True)
mixedtuples=("abc",34,46,55,True,42.7,"male")

#acces tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)


#unpacktuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#loop through a tuples

tuples=("İphone","Xiaomi","Samsung","Huawei","Nokia","Lg","Motorolla","Siemens","Oppo")

for elements in tuples:
    print(elements)


#join two tuples

tuples1=("a","b","c")
tuples2=(1,2,4,8,16,32)
tuples3=tuples1+tuples2
print(tuples3) 


#Tuple Methods
#Python, tuple'larda kullanabileceğiniz iki yerleşik method'a sahiptir.
#->count() Bir tanımlama grubunda belirtilen bir değerin kaç kez oluştuğunu döndürür
#->index() Tuple'ı belirtilen bir değer için arar ve bulunduğu yerin konumunu döndürür

