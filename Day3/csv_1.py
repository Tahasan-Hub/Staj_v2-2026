import csv

basliklar = ["isim","yas","not"]

with open("ogrenciler.csv","w",newline="") as dosya:
    yaz = csv.DictWriter(dosya,fieldnames=basliklar,delimiter=";")
    yaz.writeheader()
    yaz.writerow({"isim":"Taha","yas":20,"not":90})
    yaz.writerow({"isim":"Ayse","yas":14,"not":70})
    yaz.writerow({"isim":"Fatma","yas":34,"not":40})
    yaz.writerow({"isim":"Ayberk","yas":25,"not":55})
    yaz.writerow({"isim":"Buse","yas":69,"not":52})

print("CSV dosyası başarıyla oluşturuldu.")

with open("ogrenciler.csv","r") as dosya:
    oku = csv.DictReader(dosya,delimiter=";")
    for satir in oku:
        print(f"Isim: {satir['isim']} , Yas: {satir['yas']} , Not: {satir['not']}")
