#python sets
#Kümeler, birden çok öğeyi tek bir değişkende saklamak için kullanılır.

#Set, Python'da veri koleksiyonlarını depolamak için kullanılan 4 yerleşik veri türünden biridir, diğer 3'ü List , Tuple ve Dictionary 'dir ve tümü farklı niteliklere ve kullanıma sahiptir.

#Küme, sıralanmamış , değiştirilemez* ve dizine eklenmemiş bir koleksiyondur .

#* Not: Set öğeleri değiştirilemez, ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.

#Kümeler küme parantezleri ile yazılır.

sets={"Mühendis","Mimar","Öğretmen","Hemşire","Doktor","Avukat","Sporcu","Oyuncu","Yazar"}

print(sets) #elemanlar

print(len(sets))#uzunlugu

print(type(sets))#veritipi

#--------------------------------------------------------------

## Not: set listesi sıralanmamıştır
# bu nedenle sonuç, öğeleri rastgele bir sırayla gösterecektir
thisset = set(("apple", "banana", "cherry"))
print(thisset)


#access set items
acces_set_items= {"apple", "banana", "cherry"}

for x in acces_set_items:
  print(x)


#add ıtems

add_sets={"Biber","Patlıcan","Domates","Pazates","Havuç","Maydanoz"}
add_sets.add("Sarımsak") #Added data in sets
print(add_sets)

#remove ıtems

remove_sets = {"apple", "banana", "cherry"}

remove_sets.remove("banana")#Removed data in sets

print(remove_sets)


#loop ıtems

loop_item_sets={"Telefon","Çanta","Kulaklık","Saat","Kolye"}

for items in loop_item_sets:
    print(items)


#join two sets Methods
#Python, tuple'larda kullanabileceğiniz iki yerleşik method'a sahiptir.
#->union()  her ikisinden de tüm öğeleri içeren yeni bir küme döndüren yöntem
#->update() tüm öğeleri bir kümeden diğerine ekleyen yöntem


#union
sets1={"x","y","z","t","p","g","h"}
sets2={1,3,9,27,81}

sets3=sets1.union(sets2)
print(sets3)

#update
sets1={"a","b","c"}
sets2={1,2,3,4,5}
sets1.update(sets2)
print(sets1)


#x = {"elma", "muz", "kiraz"},y = {"google", "microsoft", "elma"},z = x.kesişim(y),yazdır(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Her iki sette de bulunmayan eşyaları saklayın:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)