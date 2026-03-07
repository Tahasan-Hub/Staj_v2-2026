from pathlib import Path

ana_klasor = Path("modern_proje")

print(f"Hedeflenen yol : {ana_klasor}")

ana_klasor.mkdir(parents=True,exist_ok=True) #parents =True en başta ki Patha bakar hangi dosya eksikse onu yaratır.  #exist_ok=True ise var olanı klasörü tekrar oluşturmaya kalkıp hata vermesin diye kullanırız

print("Klasör yapısı başarıyla oluşturuldu.")

dosya_yolu = ana_klasor / "ihlaller.csv"
dosya_yolu.touch(exist_ok=True)

print("\n------ DOSYA BİLGİLERİ -----------")
print(f"Tam İsim (.name): {dosya_yolu.name}") #Çıktı: ihlaller.csv
print(f"Uzantı (.suffix): {dosya_yolu.suffix}") #Çıktı: .csv
print(f"Sadece İsim (.stem): {dosya_yolu.stem}") #Çıktı: ihlaller
print(f"Dosya Var mı?: {dosya_yolu.exists()}") #Çıktı: True (Touch ile yarattık çünkü)

(ana_klasor / "hata_raporu.txt").touch(exist_ok=True)
(ana_klasor / "eski_ihlaller.csv").touch(exist_ok=True)

for dosya in ana_klasor.glob("*.csv"):
    print(f"Bulundu: {dosya.name}")