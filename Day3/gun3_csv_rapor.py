import csv
import random
import time
from datetime import datetime

dosya_adi = "ihaller_test.csv"
ihlaller = ["goz_kapali","hareketsiz"]
kisiler = ["KID_1","KID_2","KID_3"]

print("20 adet sahte veri üretiliyor....")

with open(dosya_adi,"w",newline="") as f:
    yaz = csv.writer(f)
    yaz.writerow(["zaman","kisi_id","ihlal_turu","sure","ear"])

    for i in range(20):
        suan = datetime.now().strftime("%H:%M:%S")
        k_id = random.choice(kisiler) #Listeden rastgele bir ID seçer
        tur = random.choice(ihlaller) #Listeden rastgele bir ihlal seçer
        sure = round(random.uniform(2,10),2) #2 ile 10 sn arası rastgele süre
        ear = round(random.uniform(0.1,0.3),3) #Rastgele EAR değeri
        yaz.writerow([suan,k_id,tur,sure,ear])
        time.sleep(0.01) #Çok hızlı dolmasın diye minik bir bekleme
print("Veriler 'ihlaller_test.csv' dosyasına başarıyla kaydedildi.\n")
print("Veriler analiz ediliyor....\n")

toplam_ihlal = 0
en_uzun_sure = 0
toplam_ear = 0
kisi_bazli_sayim = {} # Hangi ID kaç ihlal yaptı
tur_bazli_sayim = {} # İhlal türlerini saymak için boş sözlük

with open(dosya_adi,"r") as f:
    oku = csv.DictReader(f)
    for satir in oku:
        toplam_ihlal += 1

        suanki_sure = float(satir["sure"])    
        if suanki_sure > en_uzun_sure:
            en_uzun_sure = suanki_sure

        toplam_ear  += float(satir["ear"])
        k_id = satir["kisi_id"]
        if k_id in kisi_bazli_sayim:
            kisi_bazli_sayim[k_id] += 1
        else:
            kisi_bazli_sayim[k_id] = 1    
        i_turu = satir["ihlal_turu"]
        if i_turu in tur_bazli_sayim:
            tur_bazli_sayim[i_turu] += 1
        else:
            tur_bazli_sayim[i_turu] = 1         
ort_ear = toplam_ear / toplam_ihlal if toplam_ihlal > 0 else 0
print("GUARDWATCH GELİŞMİŞ RAPOR")
print(f"Toplam İhlal Sayısı: {toplam_ihlal}")    
print(f"En Uzun İhlal Sayısı: {en_uzun_sure} sn")
print(f"Ortalama EAR Değeri: {ort_ear:.3f}")        
print("-" * 20)
print("Kişi Başına İhlal Sayıları: ")
for kisi,sayi in kisi_bazli_sayim.items():
    print(f" > {kisi}:{sayi} kez")
print("-" * 20)
print("İhlal Türü Dağılımı: ")
for tur,sayi in tur_bazli_sayim.items():
    print(f" > {tur}: {sayi} kez")
