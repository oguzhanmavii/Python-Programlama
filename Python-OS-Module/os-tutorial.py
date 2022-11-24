import os
lists=['aylar','mayis','tested']

result=os.sep.join(lists)# burada listemiz içindeki elemanları sep ile directory mimarisinde nasil gösterildigini belirttik


print(result)
print("------------------------------")

get_folder=os.getcwd()#içinde bulundugumuz directory dizinin verir. 
print(get_folder)
print("------------------------------")
#get_change=os.chdir('/usr/bin/') # bulundugumuz /home/oguzhan/python-os dizininden /usr/bin e geçmemizi saglar
#get_folder=os.getcwd()
#print(get_folder)

#yöntem1
target_dict=os.getcwd() 
results=os.listdir(target_dict)#os modülünün listdir() fonksiyonu, dosya ve klasörleri listeleler
print(results)
print("------------------------------")
#yöntem2
for i in os.listdir(os.getcwd()):
    print(i)

print("------------------------------")
for i in os.listdir(os.getcwd()):
    if i.endswith('.py'): # biz burada dosyalarimizdan .py uzantili olanları seçip bu dosyalari listeleriz
        print(i)
# change2=os.chdir('/usr/bin/')
# get_folder=os.getcwd()
# result2=os.listdir(get_folder)
# print(result2)

print("------------------------------")

curdirs=os.listdir('.') # curdirs=os.listdir(os.getcwd()) ile ayni işlemi yapar 

print(curdirs)


print("------------------------------")

curdirs2=os.listdir(os.curdir)
print(curdirs2)

print("------------------------------")
print("------------------------------")

# pathPardirs=os.getcwd()
# print("Current directory:",pathPardirs)


# parent=os.path.join(pathPardirs,os.pardir)
# print("\nparent directory:",os.path.abspath(parent))


random_number=os.urandom(12)#os modülünün urandom() fonksiyonu rastgele bayt dizileri
#elde etmek için kullanılabilir
print(random_number)