import csv

ogrenci_notlari = [
    {"isim":"Taha" , "not1":50,"not2":80,"not3":100},
    {"isim":"Buse" , "not1":37,"not2":62,"not3":80},
    {"isim":"Emirhan" , "not1":16,"not2":91,"not3":60},
    {"isim":"Ayşe" , "not1":20,"not2":70,"not3":75},
    {"isim":"Ali" , "not1":65,"not2":80,"not3":99},
    {"isim":"Zeynep" , "not1":85,"not2":70,"not3":100},
    {"isim":"Mehmet" , "not1":90,"not2":40,"not3":68},
    {"isim":"Elif" , "not1":40,"not2":30,"not3":37},
    {"isim":"Yusuf" , "not1":29,"not2":95,"not3":65},
    {"isim":"Fatma" , "not1":95,"not2":15,"not3":55}
]

basliklar = ["isim","not1","not2","not3"]

with open("ogrenci_veri.csv","w",newline="") as dosya:
    yaz = csv.DictWriter(dosya , fieldnames=basliklar,delimiter=";")
    yaz.writeheader()
    for ogrenci in ogrenci_notlari:
        yaz.writerow(ogrenci)
    #yaz.writerows(ogrenci_notlari) Bu yöntem daha profesyonel bir yol
print("3 notlu öğrenci verisi oluşturuldu.")       

hesaplanan_ogrenciler = []

with open("ogrenci_veri.csv","r") as dosya:
    oku = csv.DictReader(dosya,delimiter=";")

    for satir in oku:
        n1 = int(satir["not1"])
        n2 = int(satir["not2"])
        n3 = int(satir["not3"])

        ogrenci_ort = round((n1 + n2 + n3) / 3 , 2)

        hesaplanan_ogrenciler.append({
            "isim":satir["isim"],
            "ortalama": ogrenci_ort
        })
print("Öğrencilerin kendi ortalaması hesaplandı ve hafızaya alındı.")        

toplam_ort = 0
ogrenci_sayisi = len(hesaplanan_ogrenciler)

for ogrenci in hesaplanan_ogrenciler:
    toplam_ort = toplam_ort + ogrenci["ortalama"]
sinif_ort = round(toplam_ort / ogrenci_sayisi ,2)

print(f"Sınıfın genel ortalaması {sinif_ort} olarak hesaplanmıştır.")

print("\n----------SINIF ORTALAMASINI GECEN BASARILI OGRENCILER")

with open("basarılı_ogrenci.csv","w",newline="") as yeni_dosya:
    yeni_basliklar = ["isim","ortalama"]
    yeni_yazici = csv.DictWriter(yeni_dosya , fieldnames=yeni_basliklar,delimiter=";")
    yeni_yazici.writeheader()
    for ogrenci in hesaplanan_ogrenciler:
        if ogrenci["ortalama"] > sinif_ort:
            yeni_yazici.writerow({
                "isim":ogrenci["isim"],
                "ortalama":ogrenci['ortalama']
            })
            print(f"Başarılı bir şekilde dosyaya eklendi: {ogrenci['isim']}")
print("CSV Dosyası başarılı bir şekilde hazır.")            
         