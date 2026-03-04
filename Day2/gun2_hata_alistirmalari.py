# try:
#     sayi = int(input("Lütfen bir sayı giriniz? "))
#     sonuc = 100 / sayi
#     print("Sonuç: ",sonuc)
# except ValueError:
#     print("Lütfen geçerli bir sayı giriniz! Harf kullanamazsınız.")

# except ZeroDivisionError:
#     print("Hata: Bir sayı 0'a bölünemez!!!")

#-----------------------------------------------------------------------------------

# try:
#     dosya = open("olmayan_belge.txt","r")
#     icerik = dosya.read()
#     print(icerik)

# except FileNotFoundError:
#     print("Yanlış dosya ismi girdiniz kontrol edin.")    

#------------------------------------------------------------------------------------

# meyveler = ["Armut","Karpuz","Muz","Kiraz"]
# try:
#     secilen = meyveler[10]
#     print("Seçilen meyve " ,secilen)
# except IndexError:
#     print("Hata: Girdiğiniz Indeks listede mevcut değil!!!")    

#-------------------------------------------------------------------------------

# sozluk = {
#     "isim":"Taha",
#     "yas": 20,
#     "dil":"python"
# }

# try:
#     print(sozluk["ya"])
# except KeyError:
#     print("Aradığınız anahtar sözlükte yok.")    

#------------------------------------------------------------------------------------

# dosya = None #Değişkeni başta boş tanımlıyoruz(Güvenlik için)
# try:
#     isim = input("Dosya adını girin: ")
#     dosya = open(isim,"r")
#     satirlar = dosya.readlines()
# except FileNotFoundError:
#     print("HATA: Girdiğiniz isimde bir dosya bulunamadı!")
# else:
#     sayi = len(satirlar)
#     print(f"Dosya başarıyla okundu.Toplam {sayi} satır var.")
# finally:
#     if dosya is not None:
#         dosya.close()
#         print("Dosya kapatıldı ve temizlik yapıldı.")            

#----------------------------------------------------------------------------------------


try:
    puan = int(input("Tüm sınavlarınızın not toplamını girin: "))
    sinav = int(input("Kaç tane sınava girdiniz: "))
    ort = puan / sinav
except ValueError:
    print("Lütfen sadece sayı giriniz!!!")
except ZeroDivisionError:
    print("Sınav sayısı 0 olamaz!!! Bir sayıyı 0'a bölemezsiniz...")
except Exception as hata_mesaji:
    print(f"Beklenmedik bir hata oluştu: {hata_mesaji}")
else:
    print("Hesaplama Başarılı!")
    print(f"Not Ortalaması: {ort:.1f}")                
