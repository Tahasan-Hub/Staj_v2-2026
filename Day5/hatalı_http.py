import requests

hedef_url = "https://httpbin.org/status/120"
print("Sunucuya istek gönderiliyor....")

try:
    cevap = requests.get(hedef_url,timeout=5)
    if cevap.status_code == 200:
        print("Başarılı: Veri eksiksiz alındı!")
        print(cevap.json())
    elif cevap.status_code == 404:
        print("HATA 404: Aradığın sayfa veya kaynak bulunamadı! (URL'yi yanlış yazmış olabilirsin)")
    elif cevap.status_code == 403:
        print("HATA 403: Yasaklı Bölge! Bu veriyi çekmek için yetkin/şifren yok.")
    elif cevap.status_code == 500:
        print("HATA 500: Karşı sunucu ( backend) çökmüş,adamların kodunda hata var!")
    else:
        print(f"Beklenmeyen bir durum kodu geldi: {cevap.status_code}")
except requests.exceptions.Timeout:
    print("ZAMAN AŞIMI: Sunucu çok yavaş veya internetin koptu!")
except requests.exceptions.RequestException as e:
    print(f"Bağlantı sırasında ciddi bir hata oluştu: {e}")                            