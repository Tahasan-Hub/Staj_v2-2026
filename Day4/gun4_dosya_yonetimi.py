import os 
import csv
from datetime import datetime
import cv2
import numpy as np

print("----- DOSYA YÖNETİMİ TESTİ BAŞLIYOR ----------")
klasor_adi = "kayitlar"

if not os.path.exists(klasor_adi):
    #Klasör oluştur
    os.makedirs(klasor_adi)
    print(f"[BİLGİ] '{klasor_adi}' adında yeni bir klasör oluşturuldu.")
else:
    print(f"[BİLGİ] '{klasor_adi}' klasörü zaten var,üzerine yazılacak.")

csv_dosya_yolu = "sahte_ihlaller.csv"

print("\n[İŞLEM] Sahte veriler üretiliyor...")

with open(csv_dosya_yolu,"w",newline="") as dosya:
    yaz = csv.writer(dosya)
    yaz.writerow(["zaman","kisi_id","ihlal_turu","sure_sn","ear_degeri","frame_yolu"])
    for i in range(1,6):
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        kisi_id = f"Denek_{i}"
        ihlal_turu = "goz_kapali" if i % 2 == 0 else "hareketsiz"
        sure_sn = i * 2.5
        ear = 0.150
        dosya_adi = f"sahte_frame_{i}.jpg"
        frame_yolu = os.path.join(klasor_adi,dosya_adi)
        bos_resim = np.zeros((100,100,3),dtype=np.uint8)
        cv2.imwrite(frame_yolu,bos_resim)
        yaz.writerow([zaman,kisi_id,ihlal_turu,sure_sn,ear,frame_yolu])
print("[BİLGİ] 5 adet sahte ihlal kaydı ve siyah fotoğraf başarıyla oluşturuldu!")        

print("\n--------- GÜNLÜK İHLAL ÖZET RAPORU ----------")

toplam_ihlal = 0
uyku_sayisi = 0
hareketsiz_sayisi = 0

with open(csv_dosya_yolu,"r") as dosya:
    oku = csv.reader(dosya)
    basliklar = next(oku)
    for satir in oku:
        toplam_ihlal += 1 
        # satir[0] = zaman, satir[1] = kisi_id, satir[2] = ihlal_turu
        ihlal_turu = satir[2]
        if ihlal_turu == "goz_kapali":
            uyku_sayisi += 1
        elif ihlal_turu == "hareketsiz":
            hareketsiz_sayisi += 1
print(f"Toplam tespit edilen ihlal: {toplam_ihlal}")
print(f"Göz Kapalı (Uyku): {uyku_sayisi} adet")
print(f"Hareketsizlik: {hareketsiz_sayisi} adet")                

print("\n--- 'KAYITLAR' KLASÖRÜNÜN İÇİNDEKİLER ---")

klasor_icindekiler = os.listdir(klasor_adi)
if len(klasor_icindekiler) == 0:
    print("[BİLGİ] Klasör şu an tamamen boş.")
else:
    sayac = 1
    for dosya_ismi in klasor_icindekiler:
        print(f"{sayac}. {dosya_ismi}")
        sayac += 1
print("\n[BAŞARILI] Dosya Yönetimi laboratuvar görevi kusursuz bir şekilde tamamlandı!")            