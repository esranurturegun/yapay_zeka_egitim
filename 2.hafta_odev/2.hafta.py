#1.SORU         
#Ortalama hesaplayan fonksiyon

#def sayi(*params):
#     toplam=0
#     for n in params:
#     toplam+=n 

#     return toplam/len(params)    
    
#print(sayi(50/70))
#print(sayi(30,40,25,89,5))
#print(sayi(35,47,50))

#En büyüğü gösteren fonksiyon

# def enBuyuk(x,y):

#     if x>y:
#         return f'{x} sayısı daha büyüktür. '
        
#     else:
#         return f'{y} sayısı daha büyüktür. '
        

# sayi1=int(input('ilk sayıyı girin: '))
# sayi2=int(input('ikinci sayıyı girin: '))
# print(enBuyuk(sayi1,sayi2))  

# print(enBuyuk(16,85))        



#Bir metindeki kelimelerin sayısını veren fonksiyon


# def kelimeSayısı(metin):
#     metin=metin.lower()
#     kelimeler=metin.split()
#     kelimeAdeti={}
#     for kelime in kelimeler:
#         kelimeAdeti[kelime]=kelimeAdeti.get(kelime,0)+1
#     return kelimeAdeti 
  
# metin=input('Bir metin giriniz: ')
# result=kelimeSayısı(metin)

# print ('Kelime adeti: ')
# for kelime,sayi in result.items():
#     print(f'{kelime}: {sayi}')

#2.SORU
#Tek sayıların karesini alan fonksiyon

# def square(num):
#  return num**2 
# numbers=[5,8,9,6,2,7,3,4,5]
# tekSayılar= filter(lambda num: num % 2 == 1, numbers)
# result=list(map(square,tekSayılar))

# print(result)
   


#0-50 arası çift sayıları filtrele

# ciftSayılar=list(filter(lambda x :x%2==0,range(51)))
# print(ciftSayılar)



#verilen iki sayı arasındaki tüm sayıların toplamını veren fonksiyon

# x=int(input('baslangıc degerini  giriniz: '))
# y=int(input('son degeri giriniz:'))

# result=sum(map(lambda x:x,range(a,b)))
# print(result)


#3.SORU
#Global ve yerel değişkenlerle çalışan uygulama

# age=8      
# def change_age(new_age):
#     age=new_age
#     print(age)
# change_age(20) 
# print(age)    


# sayac=0
# def change():
#     global sayac
#     sayac+=1
# change()
# change()
# print(sayac)   


#4.SORU
#hesap makinesi sınıfı oluşturun. Bu sınıf 4 işlem yapsın

# sayi1 = int(input('Birinci sayıyı giriniz: '))
# sayi2 = int(input('İkinci sayıyı giriniz: '))

# class HesapMakinesi:
#     def __init__(self, sayi1, sayi2):
#         self.sayi1 = sayi1
#         self.sayi2 = sayi2

#     def toplama(self):
#         return self.sayi1 + self.sayi2

#     def cikarma(self):
#         return self.sayi1 - self.sayi2

#     def carpma(self):
#         return self.sayi1 * self.sayi2

#     def bolme(self):
#         if self.sayi2 != 0:
#             return self.sayi1 / self.sayi2
#         else:
#             return "Bölme işlemi için ikinci sayıya 0 girmeyiniz."


# hesap = HesapMakinesi(sayi1, sayi2)

# print(f"Toplama: {hesap.toplama()}")
# print(f"Çıkarma: {hesap.cikarma()}")
# print(f"Çarpma: {hesap.carpma()}")
# print(f"Bölme: {hesap.bolme()}")




#Bir öğrenci sınıfı oluşturun. Öğrencinin adı notları sınıfını tutan özellikler ekleyin. Ortalama not hesaplayan bir metot yazın


# class Ogrenci:
#     def __init__(self, ad, sinif, notlar,kisi):
#         self.ad = ad
#         self.sinif = sinif
#         self.notlar = notlar
#         self.kisi=kisi

#     def ortalama(self):
#         if len(self.notlar) == 0:
#             return 0
#         else:
#             return sum(self.notlar) / len(self.notlar)


# ogrenci1 = Ogrenci("Esra Cengiz", "12-B", [80,70,95],28)
# ogrenci2 = Ogrenci("Cemile Aygöz", "10-D", [68,55,79],30)

# print(f"{ogrenci1.ad}  not ortalaması: {ogrenci1.ortalaması(): }")
# print(f"{ogrenci2.ad}  not ortalaması: {ogrenci2.ortalaması(): }")


#5.SORU
#Bir hayvan sınıfı yazın bu sınıftan kedi köpek altsınıfı üret.Her alt sınıf için farklı ses çıkaran bir metot ekleyin.

#class Hayvanlar:
#    def __init__(self, isim):
#        self.isim = isim

#    def sesCikar(self):
#        pass

#    def yemek(self):
#        pass

#class Kedi(Hayvanlar):  # Doğru temel sınıf ismi kullanıldı
#    def sesCikar(self):
#        return f"{self.isim} miyavlar."
#
#    def yemek(self):
#        return f"{self.isim} süt içer."

#class Kopek(Hayvanlar):  # Doğru temel sınıf ismi kullanıldı
#    def sesCikar(self):
#        return f"{self.isim} havlar."

#    def yemek(self):
#        return f"{self.isim} et yer."

#kedi = Kedi("Pilav")
#kopek = Kopek("Boncuk")

#print(kedi.sesCikar(), kedi.yemek())  
#print(kopek.sesCikar(), kopek.yemek())  



#Bir araba sınıfından türeyen elektrikli araba sınıfı oluşturun. elektrikli araba sınıfına pil seviyesi ve şarj metotları ekleyin.

# class Araba:
#     def __init__(self, model , marka , yil):
#         self.marka = marka
#         self.model = model
#         self.yil = yil

#     def bilgileriGoster(self):
#         return f"{self.marka} {self.yil} {self.model}"

# class ElektrikliAraba(Araba):
#     def __init__(self, model ,marka , yil, pil):
#         super().__init__(marka, model, yil)
#         self.pil= pil 
#         self.pilseviyesi = 0 

#     def pildurumu(self):
#         return f"Pil seviyesi: %{self.pilseviyesi}"

#     def sarjet(self, miktar):
#         if miktar < 0:
#             return "Şarj miktarı negatif(-) olamaz."
#         yeniseviye = self.pilseviyesi + miktar
#         if yeniseviye >= 100:
#             self.pilseviyesi = 100
#             return "Pil tamamen şarj oldu."
#         else:
#             self.pilseviyesi = yeniseviye
#             return f"Pil %{self.pilseviyesi} seviyesine kadar şarj edildi."
        
        
# arabam = ElektrikliAraba("Model S", "BMW", 2025,100)


# print(arabam.bilgilerigoster())  

# print(arabam.pildurumu())  

# print(arabam.sarjet(40))  

# print(arabam.pildurumu())  

# print(arabam.sarjet(50)) 

# print(arabam.pildurumu())  

#6.SORU
#İki vektörü toplayan özel bir add metodu tanımlayın


# class Vektor:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, diger):
#         return Vektor(self.a+diger.a,self.b+ diger.b)

#     def __repr__(self):
#         return f"Vektor({self.a}, {self.b})"

# def vektor_degeri():
#     a = int(input("Vektörün a bileşenini girin: "))
#     b = int(input("Vektörün b bileşenini girin: "))
#     return Vektor(a, b)

# print("Birinci vektör:")
# d1 = vektordegeri()

# print("İkinci vektör:")
# d2 = vektordegeri()

# d3 = d1 + d2
# print(f"Toplam vektör: {d3}")



#Bir sınıfta nesnenin açıklamasını veren bir str metodu yazın
# class Bilgisayar:
#     def __init__(self, marka, model, fiyat):
#       
#         self.model = model
#         self.marka = marka
#         self.fiyat = fiyat

#     def __str__(self):
#         return f"bilgisayarın markası: {self.marka} {self.model}'dir ve fiyatı {self.fiyat} tl'dir."

# bilgisayar1 = Bilgisayar("dell", "inspiron", 320)

# print(bilgisayar1)

