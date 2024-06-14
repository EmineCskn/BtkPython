#1-Kullanıcıdan isim ,yaş ve eğitim bilgilerinş isteyelim.
# Ehliyet alma durumunu kontrol edelim.
# Koşul:Yaş en az 18 ve eğitim durumu lise yada üni 


# isim = input('İsminizi giriniz: ').lower()
# yas = int(input('yaşınızı giriniz: '))
# egitim = input('eğitim durumunuzu giriniz\n ilkokul\n lise\n üniverste: ').lower()

# if yas >= 18:
#     if egitim=='lise' or egitim=='üniverste':
#         print('Ehliyet alabilirsiniz')
#     else:
#         print(f'{isim} Ehliyet alabilmek için en az lise mezunu olmalısınız.')
# else:
#     print(f'{isim} Ehliyet alabilmek için en az 18 yaşında olmalısınız.')

#YADA 

#if egitim=='lise' or egitim=='üniverste' and (yas>=18):
#         print('Ehliyet alabilirsiniz')
#     else:
#         print(' Ehliyet alamazsınız.')

#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ort 
# göre not aralığına karşılık gelen not bilgisini yazın.
# 0 -24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100=> 5

# birinciYazili=int(input('1.yazılı notunu giriniz: '))
# ikinciYazili=int(input('2.yazılı notunu giriniz: '))
# sözlüNotu=int(input('sözlü notunu giriniz: '))
# ort= (birinciYazili+ikinciYazili+sözlüNotu)/3
# print(ort)

# if ort <=24:
#     print('not ortalamanız 0 (sıfır)')
# elif ort >24 and ort<=44:
#     print('not ortalamanız 1 (bir)')
# elif ort >44 and ort<=54:
#     print('not ortalamanız 2 (iki)')
# elif ort >54 and ort<=69:
#     print('not ortalamanız 3 (üç)')
# elif ort >69 and ort<=84:
#     print('not ortalamanız 4 (dört)')
# elif ort >84 and ort<=100:
#     print('not ortalamanız 5 (beş)')

# 3-Trafiğe çıkış tarihi alınan bir aracın servis zamanını 
# aşağıdaki bilgilere göre hesaplayınız
# 1.Bakım =>1.yıl
# 2.Bakım =>2.yıl
# 3.Bakım =>3.yıl
# **Süre hesabını alınan gün ay yıl bilgisine göre gün bazlı hesaplayın
# **datetime modülünü kullanmanız gerekiyor.
import datetime

tarih =input('Trafiğe çıkış tarihinizi yazınız (2019/7/8).')
tarih.split('/')
print(tarih)

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi =datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days
if days <=365:
    print('1.Servis aralığı')
elif days >365 and trafigeCikis<=365*2:
    print('2.Servis aralığı')
elif days >365*2 and trafigeCikis<=365*3:
    print('3.Servis aralığı')
else:
    print('hatalı giriş yaptınız')

