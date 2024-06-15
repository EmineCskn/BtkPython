'''
1- 100 arasinda rastgele uretilecek sayiyi asagi yukari ifadelerle buldurmaya calisin(hak = 5)
** random modulu icin  python random seklinde arama yapin
** 100 uzerinden puanlama yapin Her soru 20 puan
**Hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi uzerinden hesaplansin
'''
import random

sayi= random.randint(1,20)
can = int(input('Kac caniniz olsun: '))
hak =can 
sayac = 0

while hak >0:
    hak -= 1
    sayac +=1
    tahmin = int(input('tahmin'))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}.tahminde bildiniz.Toplam puaniniz : {100 - ((100/can)*(sayac-1))}')
        break
    elif sayi > tahmin:
        print('yukari')
    else:
        print('asagi')

    if hak == 0 :
        print(f'hakkiniz bitti.Tutulan Sayi {sayi}')


#Once random classini import ettik , sonrasinda sayi uretecegi araligi verdik ve baslangicta tahmin hakkini 5 ile sinirladik 
#tahmin hakki bitene kadar bir while dongusu olusturduk.Her tahminde esit puan (20 puan) azalacak sekilde hesaplama yaptik
# baslangicta ilk tahmin hakkimizi kullandigimiz icin donguye girer girmez hakkimizi 1 azalttik, 
# ve kullaniciya tahminini bu dongu icinde sorduk
# if bloguyla da kullaniciya komutlar verdik.Dogru tahmin edildiginde break komutuyla donguyu kirdik.
# son olarak kullaniciya hak sayisini sorduk ve basta belirledigimiz hak degiskenine kullanicinin belirledigi sayiyi atadik.
# Baslangicta 100 puani olan ve her bilemedigi tahminde esit sekilde puanini dusuren bir hesaplama yaptik...