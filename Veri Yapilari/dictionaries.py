#dictionary
#Sözlükler, veri değerlerini anahtar:değer çiftlerinde depolamak için kullanılır.
#Sözlük, sıralı*, değiştirilebilir ve kopyalara izin vermeyen bir koleksiyondur.
#Python 3.7 sürümünden itibaren sözlükler sıralanmıştır !.
#Python 3.6 ve önceki sürümlerde sözlükler sırasızdır.
#Sözlükler küme parantezleriyle yazılır ve anahtarlara ve değerlere sahiptir:

dict={
    "marka":"Bmw",
    "model":"520d",
    "yil":2017
}

print(dict)#tamamını görmek için print fonksiyonu ile  sözlük direkt çağırılır

#Ekranda sadece araba'nın markasını görmek istiyorsak
print(dict["marka"])
#araba'nın modelini görmek istiyorsak
print(dict["model"])
#araba'nın üretim yılını görmek istiyorsak
print(dict["yil"])

print(len(dict))#listemizin uzunluğunun elaman tipini görmek için 