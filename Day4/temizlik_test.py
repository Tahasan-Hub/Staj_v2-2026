import os
import time

def eski_kayitlari_temizle(klasor_yolu,gun_limiti=7):
    suan = time.time()
    silinen_sayisi = 0 # Kaç dosya sildiğimizi saymak için bir sayaç
    print(f"[{klasor_yolu}] klasorunde {gun_limiti} gunden eski dosyalar araniyor...\n")
    for dosya_adi in os.listdir(klasor_yolu):
        tam_dosya_yolu = os.path.join(klasor_yolu,dosya_adi)
        if os.path.isfile(tam_dosya_yolu):
            dosya_zamani = os.path.getmtime(tam_dosya_yolu)
            dosya_yasi_gun = (suan - dosya_zamani) / 86400
            if dosya_yasi_gun > gun_limiti:
                print(f"SİLİNECEK: {dosya_adi} (Yaş: {dosya_yasi_gun:.1f} gün)")

                os.remove(tam_dosya_yolu)

                silinen_sayisi += 1 # Sayacı 1 artır
    print(f"\nİşlem tamam! Toplam {silinen_sayisi} dosya tespit edildi/silindi.")            
            
eski_kayitlari_temizle("kayitlar/2026-03-06",gun_limiti=0)        