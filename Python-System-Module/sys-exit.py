import sys
import time

sayi=input('Bir sayi girin:')

if int(sayi) < 0:
    print('cikiliyor..')
    time.sleep(2)
    sys.exit()

else:
    print(sayi)

        