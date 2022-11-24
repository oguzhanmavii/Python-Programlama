import os
# os modülünün rename() adlı fonksiyonunu kullanarak dizinlerin adlarını değiştirebiliriz.
# Bu fonksiyon  iki parametre alır -> (mevcuttur folder,yeni folder ismi)
edit_folder=os.rename('dizinicindeolustur','degistirdim')


#os modülünün replace() fonksiyonu biraz önce öğrendiğimiz rename() fonksiyonu gibi çalışır:
edit_folder2=os.replace('olustur','degistir')

