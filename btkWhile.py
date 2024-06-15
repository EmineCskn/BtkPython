# # # 1- 100 e kadar 
# x= 0
# while x<100:
#     if x % 2 == 1:
#         print(f'sayi tek: {x}')
#     else:
#         print(f'sayi cift: {x})')
#     x += 1

# name = ' ' #False 
# while not name.strip() :
#     name = input('adınızı giriniz: ')

# print(f'Merhaba ,{name}')

# sayilar = [1,3,5,7,9,12,19,21]

# # 1:sayilar listesini while ile ekrana yazdirin
# i=0

# while i < len(sayilar):
#     print(sayilar[i])
#     i+=1

# #2:Baslangic ve bitis degerlerinikullanicidan alip aradaki tum tek sayilari ekrana yazdirin 

# baslangic = int(input("Baslangic degerini giriniz: "))

# bitis = int(input("Bitis degerini giriniz: "))

# i= baslangic

# while i < bitis :
#     if i % 2 == 1 :
#         print(i)
#     i += 1

# #3:kullanicidan alacaginiz 5 sayiyi ekranda  sirali bir sekilde yazdirin

# sayilar = []

# for i in range(5):
#     sayi = int(input(f'lutfen {i+1}. sayiyi giriniz :'))
#     sayilar.append(sayi)

# sayilar.sort()
# print(sayilar)

# # 4:kullanicidan alacaginiz sinirsiz urun bilgisini urunler listesi icinde saklayin
# #  ** urun sayisini kullaniciya sorun
# #  ** dictionary listesi yapisi (name , price ) seklinde olsun
# #  ** urun ekleme islemi bittiginde urunleri ekranda while ile listeleyin

# urunler = []

# urunSayisi = int(input('urun sayisini giriniz: '))
# i=0
# while (i<urunSayisi):
#     urunAdi = input('urun adi :' )
#     urunFiyati = int(input('urun fiyati :'))
#     urunler.append({'name': urunAdi, 
#                     'price' : urunFiyati
#                     })
#     i += 1

# for  i in urunler:
#     print(f'urun adi: {i['name']} urun fiyati: {i['price']}')

# urunler = {}

# urunSayisi = int(input('urun sayisini giriniz: '))

# i=0
# while (i<urunSayisi):
#     urunAdi = input('urun adi :' )
#     urunFiyati = int(input('urun fiyati :'))
#     urunler[urunAdi] = urunFiyati
#     i += 1

# for urunAdi, urunFiyati in urunler.items():
#     print(f'urun adi: {urunAdi} urun fiyati: {urunFiyati}')

#1-100 kadar olan tek sayilarin toplami

x=1
result =0

while x<=100:
    x +=1
    if x % 2== 0:
        continue
    result +=x
print(f'toplam {result}')

for item in range(20,100,20): # range methodu burada bize elemanlari 20 den baslayan ve 20 ser artan bir liste dondurur [20,40,60,80]
    print(item)

#enumarete

index =0
greeting = 'Hello There'

for index,item in enumerate(greeting):   # enumer methodu bize string ifadeyi index numaralariyla beraber parcalar
    print(f'index: {index} item: {item}')

# Zip

list1 =[1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 =[100,200,300,400,500]
print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
    print(item)


numbers = [x*x for x in range(10) if x%3==0]
print(numbers)

myList =[]
myString = 'Hello'

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

result = [x if x%2==0 else 'TEK' for x in range(1, 10)]
print(result)

result =[]

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

result = [(x,y) for x in range(3) for y in range(3)]

print(result)

