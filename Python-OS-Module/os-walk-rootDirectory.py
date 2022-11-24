import os

for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    print(kökdizin)