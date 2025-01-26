#1. soru
print("Merhaba Yapay Zeka!")
#kullanıcının adını alma
ad= input("adınızı giriniz")
print('merhaba' + " " + str(ad) + '!' + 'Python öğrenmeye hoş geldin.' )

#2.soru
#değişken tanımlama
c =" Esra"
b = 36
a = 21.1

print(str(a) + " " +  str(b) +" " + "c" )
#boolean
print( b < a)

#sayılarla işlemler

a = 0
b = 0


girdi = input("İki sayı giriniz (aralarında boşluk bırakın): ")
    
 
sayi1, sayi2 = map(int, girdi.split())
    

print(f"Birinci sayı: {sayi1}, İkinci sayı: {sayi2}")

print(sayi1 * sayi2 , sayi1 + sayi2 , sayi1 - sayi2) 

#değişken türleri değiştirme

print(str(sayi1))

stringsayi= "42"
int(stringsayi)
print(stringsayi)

#3. soru
#harfleri büyük hale getirme
cumle=input("bir cümle giriniz")
print(cumle.upper())

#listeye ekleme çıkarma
alisveris_listesi= list
alisveris_listesi = ['peynir','zeytin', 'ekmek', 'çikolata']
alisveris_listesi.append('süt')
alisveris_listesi.remove('zeytin')
del alisveris_listesi[0]
print(alisveris_listesi)

#4.soru
#ehliyet
yas=int(input("Yaşınızı giriniz"))
if (yas>=18):
    print("ehliyet alabilirsiniz")
else: print("Ehliyet almak için yaşınız tutmuyor.")

#tahmin oyunu

sayi= 5 
tahmin=int(input(" 1-10 arasında bir sayı tahmin edin"))
if(tahmin>0)and(tahmin<=10):
    if(tahmin==sayi):
        print("tebrikler doğru tahmin ettiniz." )
    else:
        print("üzgünüm yanlış tahmin ettiniz.")
else:
    print("Lütfen 1-10 arası bir sayı tahmin ediniz.")

#Amiral battı

import random

satir = random.randint(1, 5)
sutun = random.randint(1, 5)

print("Amiral battı oyununa hoş geldiniz")
print("Geminin nerde olduğunu 5X5 koordinatlarında satır ve sütunu tahmin ederek bulun.")

while True:
    tahmin_satiri = int(input("Bir satır tahmini yapın(5x5): "))
    tahmin_sutunu = int(input("Bir sütun tahmini yapın(5x5): "))
    
    if tahmin_satiri < 1 or tahmin_satiri > 5 or tahmin_sutunu < 1 or tahmin_sutunu > 5:
        print("Lütfen 1 ile 5 arasında bir sayı girin.")
        continue
    
    if tahmin_satiri == satir and tahmin_sutunu == sutun:
        print("Tebrikler! Gemiyi vurdunuz.")
        break
    else:
        print("Yanlış tahmin ettiniz lütfen tekrar deneyin!")
   

   
