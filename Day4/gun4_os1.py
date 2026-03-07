import os

ana_klasor = os.path.join("proje")

alt_klasorler = ["veriler","ciktilar","loglar"]

for klasor_adi in alt_klasorler:
    tam_klasor_yolu = os.path.join(ana_klasor,klasor_adi)
    os.makedirs(tam_klasor_yolu,exist_ok=True)
    print(f"Klasör Hazır: {tam_klasor_yolu}")
    dosya_yolu = os.path.join(tam_klasor_yolu,".gitkeep")
    dosya = open(dosya_yolu,"w")
    dosya.close()
    print(f"Dosya oluşturuldu: {dosya_yolu}")