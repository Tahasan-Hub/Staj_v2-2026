import requests

hedef_url = "https://api.ipify.org?format=json"

print("Sunucuya GET isteği gönderiliyor...")

cevap = requests.get(hedef_url)

print(f"Sunucudan dönen durum kodu: {cevap.status_code}")

veri = cevap.json()
print("Sunucudan gelen tam veri:",veri)

ip_adresim = veri['ip']
print(f"Ağdan başarıyla çekilen IP adresin: {ip_adresim}")

print("\n---- ŞİMDİ POST(VERİ GÖNDERME) İŞLEMİNE GEÇİYORUZ ------")

post_url = "https://httpbin.org/post"

gonderilecek_veri = {
    "kullanici_adi":"taha_backend",
    "meslek":"Yazılım Geliştirici",
    "mesaj": "Merhaba Sunucu,sana veri gönderiyorum!"
}
print("Sunucuya paket yollanıyor(POST).....")

post_cevap = requests.post(post_url,json=gonderilecek_veri)
print(f"POST İşlemi Durum Kodu: {post_cevap.status_code}")
sunucu_yaniti = post_cevap.json()
print("Sunucunun teslim aldığı veri:",sunucu_yaniti["json"])