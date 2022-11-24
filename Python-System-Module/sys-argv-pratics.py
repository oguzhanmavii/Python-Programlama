import sys

def cik():
    print('cikiliyor...')
    sys.exit()

if len(sys.argv) < 2:
    print('Gerekli parametreleri girmediniz!')
    cik()

elif len(sys.argv) > 2:
    print('cok fazla parametre girdiniz!')
    cik()

elif sys.argv[1] in ['-v', '-V']:
    print('Program sürümü: 0.8')

else:
    mesaj = 'Girdiğiniz parametre ({}) anlaşilamadi!'
    print(mesaj.format(sys.argv[1]))
    cik()