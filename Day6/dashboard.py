import csv
import matplotlib.pyplot as plt
from collections import Counter

kisi_ihlalleri = Counter()

with open("ihlaller.csv","r",encoding="utf-8") as dosya:
    oku = csv.DictReader(dosya)

    print("PYTHON'IN GÖRDÜĞÜ BAŞLIKLAR:", oku.fieldnames)

    for satir in oku:
        kisi_ihlalleri[satir[" kisi_id"]] += 1
print("Sayım Sonucu:",kisi_ihlalleri)     

kisiler = list(kisi_ihlalleri.keys())
sayilar = list(kisi_ihlalleri.values())

plt.figure(figsize=(8,5))

plt.bar(kisiler,sayilar,color="steelblue")

plt.title("Kişi Bazlı Toplam İhlal Sayısı")
plt.xlabel("Kişi ID")
plt.ylabel("İhlal Sayısı")

plt.savefig("dashboard_kisi.png",dpi=150,bbox_inches = "tight")
plt.close()

print("Dashboard grafiği başarıyla oluşturuldu ve 'dashboard_kisi.png' olarak kaydedildi!")