# def find_odd_numbers(lst):

#       odd_numbers = []  # Tek sayıları saklayacağımız yeni liste
#       for num in lst:
#         if num % 2 != 0:  # Eğer sayı 2'ye bölündüğünde kalan 0 değilse, tek sayıdır
#             odd_numbers.append(num)  # Listeye ekle
#       return odd_numbers  # Tek sayıların listesini döndür


# print(find_odd_numbers([10, 15, 22, 33, 40, 55]))

# girdi = [10, 15, 22, 33, 40, 55]
# tek_sayilar = []

# for i in girdi:
#     if i%2 != 0:
#         tek_sayilar.append(i)

# print(tek_sayilar)

#Soru 2: Verilen iki sayının en büyük ortak bölenini (EBOB) bulan bir fonksiyon yazın.

# say1 = 30
# say2 = 20
# ebob = []

# i=1
# while i <= say2:
#    if say2 %i ==0: 
#      if say1%i==0:
#        ebob.append(i)
#    i=i+1
# print(ebob)
# print(max(ebob))

#3Verilen bir listede tekrar eden elemanları 
# bulan ve bu elemanların kaç kez tekrar ettiğini gösteren bir fonksiyon yazın.

# girdi = [1, 2, 2, 3, 4, 4, 4, 5]

# checked = set()


# for i in girdi:
#   if i not in checked:
#     count = 0
#     for j in girdi:
#       if i==j:
#         count+=1
    
#     print(f'listedeki: {i} sayisi: {count} kere yazilmistir.')
#     checked.add(i)

# def count_duplicates(lst):
#     # Elemanların kaç kez geçtiğini tutmak için sözlük
#     counts = {}
    
#     # Listeyi tarayalım
#     for num in lst:
#         if num in counts:
#             counts[num] += 1  # Eğer eleman zaten varsa, sayacı arttır
#         else:
#             counts[num] = 1  # Yoksa, sayacı 1 yap

#     # Sadece tekrar eden elemanları döndürelim
#     duplicates = {key: value for key, value in counts.items() if value > 1}
    
#     return duplicates

# girdi = [1, 2, 2, 3, 4, 4, 4, 5]
# print(count_duplicates(girdi)) 


#4Bir cümledeki en uzun kelimeyi bulan bir fonksiyon yazın. 
# Eğer birden fazla en uzun kelime varsa, bunları bir liste halinde döndürün.

# def find_longest_word(sentence):
    
#     words = sentence.split()

#     max_len = len(max(words, key=len))

    # max(): Bu fonksiyon normalde, bir listedeki en büyük elemanı döndürür. Ancak biz burada, 
    # en büyük elemanı uzunluklarına göre bulmak istiyoruz.
    # key=len: Bu parametre, max() fonksiyonuna nasıl karşılaştırma yapacağını söyler. 
    # key=len demek, listedeki her bir elemanın uzunluğunu (len()) baz alarak karşılaştırma yapmasını sağlar.
    # Yani burada her kelimenin uzunluğuna göre max() işlemi yapılır.
    # max(words, key=len) ifadesi şu anlama gelir: Kelimeler arasından en uzun olanı döndür.
    # len(...):
    # Şimdi, max() fonksiyonunun döndürdüğü en uzun kelimenin uzunluğunu almak için len() fonksiyonunu 
    # kullanıyoruz. Yani önce en uzun kelimeyi buluyoruz, sonra onun karakter sayısını öğreniyoruz.

  
#     longest_wors = [word for word in words if len(word)== max_len]

#     return longest_wors

# print(find_longest_word("Bu sınav zor ama çok öğretici olacak"))

#5 Kullanıcıdan bir sayı alarak o sayıya kadar Fibonacci dizisini oluşturan bir Python fonksiyonu yazın.
# def fibonacci(n):
#     fib_list =[0,1]

#     while len(fib_list)<n :
#         next_eleman = fib_list[-1] + fib_list[-2]
#         fib_list.append(next_eleman)

#     return fib_list

# sayi= int(input('bir sayi giriniz: '))

# print(fibonacci(sayi))
  
# #6Kullanıcıdan bir sayı alarak o sayının faktöriyelini hesaplayan bir Python fonksiyonu yazın.
# def faktoriyel(n):
#     result = 1

#     for i in range(n,0,-1):
#         result*=i

#     return result

# sayi= int(input('bir sayi giriniz: '))

# print(faktoriyel(sayi))

#7 Kullanıcıdan bir sayı alın, bu sayıyı ters çevirin ve ters halini ekrana yazdırın.

def sayiyi_tersine_cevir(n):
    
    ters_sayi= int(str(n)[::-1])

    return ters_sayi

sayi = int(input('bir sayi giriniz : '))
print(sayiyi_tersine_cevir(sayi))


# sayi1 = int(input('Bir sayi giriniz : '))
# sayi2 = sayiyi_tersine_cevir(sayi1)

# if sayi1== sayi2 :
#     print(f'{sayi1} sayisi palindromdur')
# else:
#     print(f'{sayi1} sayisi palindrom degildir')

#8Bir Sayının Palindrom Olup Olmadığını Kontrol Etme
def palindrom_mu(n):
    # Sayıyı ters çeviriyoruz
    ters_sayi = str(n)[::-1]
    
    # Ters haliyle orijinal sayıyı kıyaslıyoruz
    if str(n) == ters_sayi:
        return f"{n} bir palindrom sayısıdır."
    else:
        return f"{n} bir palindrom sayısı değildir."

sayi1 = int(input('bir sayi giriniz : '))
print(palindrom_mu(sayi1))


def find_longest_word(sentence):

 words=sentence.split()

 max_words = len(max(words,key=len))

 longest_word = [word for word in words if len(word)==max_words]

 return longest_word

#9Kullanıcıdan bir liste alın ve bu listede tekrar eden elemanları döndüren bir 
# Python fonksiyonu yazın.

def tekrar_edenler(liste):
    tekrar_eden = []
    seen = set()  # Daha önce görülen elemanları tutacak bir set

    for eleman in liste:
        if eleman in seen:  # Eleman zaten görüldüyse
            if eleman not in tekrar_eden:  # Tekrar edenler listesine eklenmemişse
                tekrar_eden.append(eleman)  # Ekle
        else:
            seen.add(eleman)  # Elemanı daha önce görülenler setine ekle

    return tekrar_eden








     