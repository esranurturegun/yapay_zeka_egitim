
"""1.1"""

# import math

# def hesap_makinesi():
#     print("Merhaba Hesap Makinesi Uygulamasına hoşgeldiniz")
#     print("İşlemler: +, -, *, /, ^ (üs), sqrt (karekök)")
    
#     islem = input("İşlemi seçiniz: ")
    
#     if islem == "sqrt":
#         sayi = float(input("Sayıyı giriniz: "))
#         print(f"Sonuç: {math.sqrt(sayi)}")
#     else:
#         sayi1 = float(input("Birinci sayıyı giriniz: "))
#         sayi2 = float(input("İkinci sayıyı giriniz: "))
        
#         if islem == "+":
#             print(f"Sonuç: {sayi1 + sayi2}")
#         elif islem == "-":
#             print(f"Sonuç: {sayi1 - sayi2}")
#         elif islem == "*":
#             print(f"Sonuç: {sayi1 * sayi2}")
#         elif islem == "/":
#             if sayi2 != 0:
#                 print(f"Sonuç: {sayi1 / sayi2}")
#             else:
#                 print("Hata: Sıfıra bölme hatası!")
#         elif islem == "^":
#             print(f"Sonuç: {math.pow(sayi1, sayi2)}")
#         else:
#             print("Geçersiz işlem!")

# hesap_makinesi()

"""1.2"""

# import my_modul.py
# def toplama(a, b):
#    
#     return a + b

# def cikarma(a, b):
#    
#     return a - b

# def carpma(a, b):
#     
#     return a * b

# def bolme(a, b):
#     
#     if b == 0:
#         raise ValueError("Hata: Sıfıra bölme işlemi yapılamaz!")
#     return a / b

# sayi1 = float(input("Birinci sayıyı girin: "))
# sayi2 = float(input("İkinci sayıyı girin: "))

# print(f"Toplama: {math_modul.toplama(sayi1, sayi2)}")
# print(f"Çıkarma: {math_modul.cikarma(sayi1, sayi2)}")
# print(f"Çarpma: {math_modul.carpma(sayi1, sayi2)}")

# try:
#     print(f"Bölme: {math_modul.bolme(sayi1, sayi2)}")
# except ValueError as e:
#     print(e)



"""2.1"""

# def bolme_islemi():
#     try:
#         sayi1 = float(input("Birinci sayıyı girin: "))
#         sayi2 = float(input("İkinci sayıyı girin: "))

#         sonuc = sayi1 / sayi2
#         print(f"Sonuç: {sonuc}")

#     except ZeroDivisionError:
#         print("Hata: Bir sayı sıfıra bölünemez!")
#     except ValueError:
#         print("Hata: Lütfen geçerli bir sayı girin!")
#     except Exception as e:
#         print(f"Bilinmeyen bir hata oluştu: {e}")

# bolme_islemi()

"""2.2"""
# class NegatifSayiHatasi(Exception):
#     """Negatif sayı girildiğinde fırlatılan özel hata sınıfı."""
#     def __init__(self, mesaj="Negatif sayı girişi yasaktır!"):
#         super().__init__(mesaj)

# def pozitif_sayi_kontrol(sayi):
#     """Negatif sayı girildiğinde özel hata fırlatan fonksiyon."""
#     if sayi < 0:
#         raise NegatifSayiHatasi(f"Hata: {sayi} negatif bir sayıdır!")
#     return f"Girilen sayı: {sayi}"

# try:
#     sayi = float(input("Bir sayı girin: "))
#     print(pozitif_sayi_kontrol(sayi))
# except NegatifSayiHatasi as e:
#     print(e)
# except ValueError:
#     print("Hata: Lütfen geçerli bir sayı girin!")

"""3.1"""
# def veri_kaydet():
#     with open("data.txt", "w", encoding="utf-8") as dosya:
#         veri = input("Kaydetmek istediğiniz veriyi girin: ")
#         dosya.write(veri)
#         print("Veri başarıyla kaydedildi!")

# def veri_oku():
#     try:
#         with open("data.txt", "r", encoding="utf-8") as dosya:
#             icerik = dosya.read()
#             print("Dosyadan okunan veri:")
#             print(icerik)
#     except FileNotFoundError:
#         print("Hata: data.txt dosyası bulunamadı!")

# while True:
#     print("\n1 - Veri Kaydet")
#     print("2 - Veriyi Oku ve Yazdır")
#     print("3 - Çıkış")
#     secim = input("Seçiminizi yapın: ")

#     if secim == "1":
#         veri_kaydet()
#     elif secim == "2":
#         veri_oku()
#     elif secim == "3":
#         print("Programdan çıkılıyor...")
#         break
#     else:
#         print("Geçersiz seçim, lütfen tekrar deneyin!")
"""3.2"""
# {
#     "ad": "Ali",
#     "yas": 25,
#     "sehir": "İstanbul"
# }

# import json

# dosya_adi = "veri.json"

# # JSON dosyasını oku
# with open(dosya_adi, "r", encoding="utf-8") as dosya:
#     veri = json.load(dosya)

# print("Mevcut JSON Verisi:", veri)


# veri["ad"] = input("Yeni ad girin: ")
# veri["yas"] = int(input("Yeni yaş girin: "))
# veri["sehir"] = input("Yeni şehir girin: ")

# with open(dosya_adi, "w", encoding="utf-8") as dosya:
#     json.dump(veri, dosya, ensure_ascii=False, indent=4)

# print("Güncellenmiş JSON Verisi:", veri)

""" 4.1 """
# numbers = [1, 2, 3, 4, 5]

# squared_numbers = list(map(lambda x: x ** 2, numbers))

# print("Karesi alınmış liste:", squared_numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# print("Çift sayılar:", even_numbers)

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]


# sum_numbers = reduce(lambda x, y: x + y, numbers)

#print("Listedeki sayıların toplamı:", sum_numbers)

"""4.2"""
# numbers = [5, 2, 9, 1, 7]

# sorted_numbers = sorted(numbers, key=lambda x: x)  # Varsayılan olarak küçükten büyüğe sıralar

# print("Küçükten büyüğe sıralı liste:", sorted_numbers)

# numbers = [5, 2, 9, 1, 7]

# sorted_numbers_desc = sorted(numbers, key=lambda x: x, reverse=True)

# print("Büyükten küçüğe sıralı liste:", sorted_numbers_desc)

# words = ["elma", "armut", "kiraz", "muz", "karpuz"]

# sorted_words = sorted(words, key=lambda x: len(x))

# print("Kelime uzunluklarına göre sıralı liste:", sorted_words)

# people = [["Ali", 25], ["Zeynep", 22], ["Mehmet", 30]]

# sorted_people = sorted(people, key=lambda x: x[1])  # Yaşa göre sıralama

# print("Yaşa göre sıralı liste:", sorted_people)

# words = ["elma", "armut", "kiraz", "muz", "karpuz"]

# sorted_by_last_char = sorted(words, key=lambda x: x[-1])

# print("Son harfine göre sıralı liste:", sorted_by_last_char)

"""5.1"""
# class EvenNumbers:
#     def _init_(self, start=0, limit=None):
        
#         self.current = start if start % 2 == 0 else start + 1
#         self.limit = limit
    
#     def _iter_(self):
#         return self
    
#     def _next_(self):
#         if self.limit is not None and self.current > self.limit:
#             raise StopIteration
#         next_even = self.current
#         self.current += 2 
#         return next_even


# if _name_ == "_main_":
#     even_numbers = EvenNumbers(4, 30)  
#     for num in even_numbers:
#         print(num)
"""5.2"""
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# fib_gen = fibonacci()
# for _ in range(10):
#     print(next(fib_gen), end=" ")

"""2."""

# import datetime


# def log_hata(hata_mesaji):
#     with open("log.txt", "a", encoding="utf-8") as log_dosyasi:
#         zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         log_dosyasi.write(f"[{zaman}] Hata: {hata_mesaji}\n")


# def sayi_al():
#     while True:
#         try:
#             sayi = int(input("Bir sayı girin: "))
#             return sayi
#         except ValueError as e:
#             log_hata(f"Geçersiz sayı girişi: {e}")
#             print("Hata: Lütfen geçerli bir sayı girin.")

# while True:
#     try:
#         print("\n1. Sayı Al")
#         print("2. Çıkış")
#         secim = input("Bir seçenek girin: ")

#         if secim == "1":
#             sayi = sayi_al()
#             print(f"Girdiğiniz sayı: {sayi}")
#         elif secim == "2":
#             print("Programdan çıkılıyor...")
#             break
#         else:
#             raise ValueError("Geçersiz seçenek!")
#     except Exception as e:
#         log_hata(f"Beklenmedik hata: {e}")
#         print("Hata: Lütfen geçerli bir seçenek girin.")


