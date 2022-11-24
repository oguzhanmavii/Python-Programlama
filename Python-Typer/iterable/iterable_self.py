#l1=[1,2,3,4,5]

# l2=iter(l1)
# print('l2 data variable')
# print(l2)

# print('--------------------------------------------')
# l3=iter(l2)
# print('l3 data variable')
# print(l3)


#print(l2==l4)



def fonk(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

fonk(isim="Oguzhan", soyisim="Mavi", yas="24")