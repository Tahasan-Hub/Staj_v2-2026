import cv2
import os
from datetime import datetime

def ihlal_frame_kaydet(frame,kisi_id,ear_degeri):
    bugunun_tarihi = datetime.now().strftime("%Y-%m-%d")
    klasor_yolu = os.path.join("kayitlar",bugunun_tarihi)
    os.makedirs(klasor_yolu,exist_ok=True)
    tam_zaman = datetime.now().strftime("%H-%M-%S")
    dosya_adi = f"ihlal_{kisi_id}_{tam_zaman}.jpg"
    tam_kayit_yolu = os.path.join(klasor_yolu,dosya_adi)
    print(f"Hazırlanan kayıt yolu: {tam_kayit_yolu}")

    bilgi_metni = f"EAR: {ear_degeri:.3f} | Kisi: {kisi_id} | Zaman: {tam_zaman}"
    cv2.putText(frame,bilgi_metni,(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imwrite(tam_kayit_yolu,frame)
    print(f"Ihlal basariyla kaydedildi: {tam_kayit_yolu}")
    return tam_kayit_yolu

# test_resmi = cv2.imread("kopek.jpg")

# if test_resmi is not None:
#     ihlal_frame_kaydet(test_resmi,"Kopek",0.15)
# else:
#     print("Test Resmi Bulunamadı.")


