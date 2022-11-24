import os

for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    for dosya in dosyalar:
            print(os.sep.join([kökdizin, dosya]))