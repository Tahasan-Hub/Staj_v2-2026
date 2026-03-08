from flask import Flask,jsonify
import csv
from collections import Counter
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def anasayfa():
    return "<h1>GuardWatch AI Dashboard</h1><p>Sistem tıkır tıkır çalışıyor....</p>"

@app.route("/durum")
def durum():
    kisi_sayaci = Counter()
    toplam_ihlal_sayisi = 0

    try:
        with open("ihlaller.csv","r",encoding="utf-8") as dosya:
            oku = csv.DictReader(dosya)

            for satir in oku:
                kisi_sayaci[satir[" kisi_id"]] += 1
                toplam_ihlal_sayisi += 1
        farkli_kisi_sayisi = len(kisi_sayaci)
        suan = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

        return jsonify({
            "sistem":"aktif",
            "toplam_farkli_kisi":farkli_kisi_sayisi,
            "toplam_ihlal_sayisi":toplam_ihlal_sayisi,
            "son_guncelleme":suan
        })      
    except FileNotFoundError:
        return jsonify({"sistem": "beklemede", "mesaj": "Henuz ihlaller.csv dosyası oluşturulmadı."})
    
@app.route("/istatistik")
def istatistik():
    kisi_ihlalleri = Counter()
    toplam = 0
    try:
        with open("ihlaller.csv","r",encoding="utf-8") as dosya:
            oku = csv.DictReader(dosya)
            for satir in oku:
                kisi_ihlalleri[satir[" kisi_id"]] += 1
                toplam += 1
    except FileNotFoundError:
        pass            
    en_cok = max(kisi_ihlalleri,key=kisi_ihlalleri.get) if kisi_ihlalleri else "Yok"

    return jsonify({
        "toplam_ihlal":toplam,
        "kisi_sayisi":len(kisi_ihlalleri),
        "en_cok_ihlal":en_cok,
        "kisi_detay":dict(kisi_ihlalleri)
    })   
if __name__ == "__main__":
    app.run(debug=True,port=5050)

if __name__ == "__main__":
    #debug = True ise kodda bir harfi bile değiştirip kaydedersen otomatik güncellenir kapa/aç yapmana gerek kalmaz
    # port=5000 sunucumuzun pcde ki yayın kapısı(port)
    app.run(debug=True,port=5050)