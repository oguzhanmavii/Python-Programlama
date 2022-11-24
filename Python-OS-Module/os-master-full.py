import os

# uzantilar=['txt','doc','xls','jpeg','pdf','zip','mp3','pdf','zip','mp3','ogg','jpeg']


# sablon1=['{}.{}'.format('dosya',i) for i in  uzantilar[:4]]
# sablon2=['resim{}.{}'.format(i, uzantilar[-1]) for i in range(1, 5)]
# sablon3=['{}.{}'.format('dosya',i) for i in uzantilar[4:]]


# dosyalar = [('anadizin',  sablon1),
#             ('resimler', sablon2),
#             ('başkadosyalar', sablon3)]

# os.makedirs(os.sep.join([dosya[0] for dosya in dosyalar]))

# for dizin, sablon in dosyalar:
#     for s in sablon:
#         open(os.sep.join([dizin,s]),'w')
#     os.chdir(dizin)    


for i in os.walk('home/oguzhan/Desktop/python-os/anadizin'):
    print(i)