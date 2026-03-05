import csv
import time
from datetime import datetime

csv_dosya = "ihlaller.csv"

print("Kayıt Başlıyor....")

for i in range(1,11):
    suanki_ts = time.time()
    formatli = datetime.fromtimestamp(suanki_ts).strftime("%Y-%m-%d %H:%M:%S")

    with open(csv_dosya ,"a",newline="") as f:
        yaz = csv.writer(f)
        yaz.writerow([formatli ,f"KID_{i}","deneme_ihlali",i])
    print(f"Satır {i} eklendi: {formatli}")
    time.sleep(1)
