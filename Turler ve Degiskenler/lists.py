benim_listem=["Araba","Ev","Helikopter","Tekne","TatilKoyu","Ucak","Spor Salonu"]
print(benim_listem)

eleman1=benim_listem[0]
print(eleman1)


eleman4=benim_listem[3]
print(eleman4)

eleman6=benim_listem[5]
print(eleman6)

elemansayisi=len(benim_listem)
print("Eleman Sayisi:",elemansayisi)

karmasik_listem=["abcdefg",34,True,False,"Male",'Pi Sayisi',3.14,"Oğuzhan Mavi","Kaptan"]

print(karmasik_listem)


#Type Of Lists Class Lists
benim_listem2=["Elma","Muz","Çilek","Kiraz"]
print(type(benim_listem2))


#listeyi tersten siralama
listeyi_negatif_sirala= ["apple", "banana", "cherry","strawberry","orange","lemon","raspberry","watermelon"]
print(listeyi_negatif_sirala[-2])


#list aralik
istedigim_araliktaki_elemanlar=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(istedigim_araliktaki_elemanlar[:4])

#list disardan eleman ekleme append() 
listeme_eleman_ekliyorum=["araba","ev","uçak"]
listeme_eleman_ekliyorum.append("motor")
print(listeme_eleman_ekliyorum)


#listeye eleman ekleme gelecegi konumu bildirme
eleman_ekle=["1","2","3","4"]
eleman_ekle.insert(3,"1")
print(eleman_ekle)

#listeden eleman kaldırma silme işlemi
eleman_kaldir=["ekle","güncelle","sil"]
eleman_kaldir.pop(2)
print(eleman_kaldir)

eleman_silme=["a","b","c","d","e","f","g","h"]
eleman_silme.pop()
print(eleman_silme)

#0.indis 1.eleman silinecektir
eleman_silme_index=["lemons","apple","banana","kiwi","orange","strawberry","lemon"]
del eleman_silme_index[0]
print(eleman_silme_index)

#clear ile bütün elemanlar silinir
butun_listeyi_temizlemek=["1","2","3","4"]
butun_listeyi_temizlemek.clear()
print(butun_listeyi_temizlemek)


#listelerde döngü işlemleri list with loops

dongu_listesi=["2","5","7","12","36","43","55","87","39","13","27","16","42","51","19","22","17","89"]

for i in dongu_listesi:
    print(i)
#lists with len
thislists = ["apple", "banana", "cherry"]
i = 0
while i < len(thislists):
  print(thislists[i])
  i = i + 1

#list with range  
thislist = ["car", "bus", "subway","plane"]
for i in range(len(thislist)):
  print(thislist[i])

#list of sort  alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#list of sort  numeric
sorts_of_lists=[100,50,64,83,82,23,17]
sorts_of_lists.sort()
print(sorts_of_lists)



#list of join listeleri birleştirmek
liste1=["a","b","c"]
liste2=[3,5,7,9]
liste_birlestir=liste1+liste2
print(liste_birlestir)



#list1 e list2 eklenmiş ve list1 çağırılmıştır

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
