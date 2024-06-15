'''
Soru : Girilen bir sayinin asal olup olmadigini bulun
'''

sayi = int(input('Bir sayi girin: '))

#sadece 1 e ve kendine bolumunden kalan 0 olmali

if sayi == 1:
      print(f'girdiginiz sayi : {sayi} asal degil')

else: 
      for  i in range(2,sayi):
            if sayi%i==0:
                  print(f'girdiginiz sayi : {sayi} asal degil')
                  i+=1
                  break
      else:
            print(f'girdiginiz sayi: {sayi} asaldir')

