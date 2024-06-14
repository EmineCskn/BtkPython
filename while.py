# # 1- 100 e kadar 
x= 0
while x<100:
    if x % 2 == 1:
        print(f'sayi tek: {x}')
    else:
        print(f'sayi cift: {x})')
    x += 1

name = ' ' #False 
while not name.strip() :
    name = input('adınızı giriniz: ')

print(f'Merhaba ,{name}')

sayilar = [1,3,5,7,9,12,19,21]

# 1:sayilar listesini while ile ekrana yazdirin
i=0

while i < len(sayilar):
    print(sayilar[i])
    i+=1

#2:Baslangic ve bitis degerlerinikullanicidan alip aradaki tum tek sayilari ekrana yazdirin 

baslangic = int(input("Baslangic degerini giriniz: "))

bitis = int(input("Bitis degerini giriniz: "))

i= baslangic

while i < bitis :
    if i % 2 == 1 :
        print(i)
    i += 1

#3:kullanicidan alacaginiz 5 sayiyi ekranda  sirali bir sekilde yazdirin

sayilar = []

for i in range(5):
    sayi = int(input(f'lutfen {i+1}. sayiyi giriniz :'))
    sayilar.append(sayi)

sayilar.sort()
print(sayilar)

# 4:kullanicidan alacaginiz sinirsiz urun bilgisini urunler listesi icinde saklayin
#  ** urun sayisini kullaniciya sorun
#  ** dictionary listesi yapisi (name , price ) seklinde olsun
#  ** urun ekleme islemi bittiginde urunleri ekranda while ile listeleyin

urunler = []

urunSayisi = int(input('urun sayisini giriniz: '))
i=0
while (i<urunSayisi):
    urunAdi = input('urun adi :' )
    urunFiyati = int(input('urun fiyati :'))
    urunler.append({'name': urunAdi, 
                    'price' : urunFiyati
                    })
    i += 1

for  i in urunler:
    print(f'urun adi: {i['name']} urun fiyati: {i['price']}')

urunler = {}

urunSayisi = int(input('urun sayisini giriniz: '))

i=0
while (i<urunSayisi):
    urunAdi = input('urun adi :' )
    urunFiyati = int(input('urun fiyati :'))
    urunler[urunAdi] = urunFiyati
    i += 1

for urunAdi, urunFiyati in urunler.items():
    print(f'urun adi: {urunAdi} urun fiyati: {urunFiyati}')