website = "http://www.sadikturan.com"
course  = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1-www.sadikturan.com içindeki sadıkturan bilgisi haricindeki her karakteri silin.

result = 'www.sadikturan.com'.strip('w.com')
print(result)

#2-'website' içinde '.com' ifadesi var mı?
result = website.find('.com')
print(result) # true ise index döndürür.

#3-'course' içindeki karakterlerin hepsi alfabetik mi ?
result = course.isalpha()
result = 'Hello'.isalpha()
result = course.isdigit()
result = '123'.isdigit()

#4-Girilen sayının pozitif olma durumunu inceleyin.
girilenSayi = input('Girilen sayı: ')
pozitifMi = (girilenSayi>0) 
print(f'girilen sayının pozitif olma durumu: {pozitifMi}')

#5-Parola ve mail bilgisinin doğruluğunu kontrol ediniz.
email = 'email@eminecoskun.com'
parola = 'abc1234'
girilenEmail= input('email: ')
girilenParola= input('parola: ')

isEmail = (email==girilenEmail.lower().strip())
isParola = (parola==girilenParola.lower().strip())

print(f'Email bilgisi doğrumu: {isEmail} ve Parola doğru mu: {isParola}')

# #####LİSTELER#####
#1- "Bmw, Mercedes, Opel, Mazda" elemanlarıyla bir liste oluşturunuz.
arabalar = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

#2- Mazda değerini Toyota ile değiştirin.

arabalar[-1] = 'Toyota'
result = arabalar
print(result)
# 3- Mercedes listenin bir elemanımıdır?

result = 'Mercedes' in arabalar

# 4-Listenin ilk 3 elemanı 
result = arabalar[:3]
print(result)

# 5-Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
arabalar[-2:] = ['Toyota', 'Renault']
result = arabalar
print(result)
# 6-Listenin üzerine Audi ve Nissan değerlerini ekleyin.
result = arabalar + ['Audi', 'Nissan'] # bu şekilde yeni bir liste oluşturduk arabalar listemiz hala 4 elemanlı.
# #####Functions#####
#1-Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def döndür(kelime,adet):
        print(kelime * adet)

döndür('hello\n',10)

# #2-Gönderilen sınırsız sayıdaki bir listeye çeviren fonksiyonu yazınız.
def listeyeCevir(*params):
      liste = []

      for param in params:
            liste.append(param)

      return liste
result = listeyeCevir(10,20,30, 'Merhaba')
print(result)

# #3-Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

# print('+'*50)
def asalMi(a,b):
    asalEleman=[]
    i=a
    
    while i<b+1:
        j=2
        while j<i:
             if i%j==0:
                 break
             else:
                j+=1
        else:
             asalEleman.append(i)

        i+=1
    return asalEleman 
sayi1 = input('1.sayıyı giriniz.')   
sayi2 = input('2.sayıyı giriniz.')   
print(asalMi(sayi1,sayi2) )    
            
#4-Gönderilen sayının tam bölenlerini bir listede döndüren fonksiyonu yazınız.
def tamBolen(a):
    tamBolenlerListesi=[]
    i=2
    while i<a:
             if a%i==0:
                 tamBolenlerListesi.append(i)
             i+=1
    return tamBolenlerListesi       
print(tamBolen(28) )  








