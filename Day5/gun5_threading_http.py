import threading
import time
import requests

def guvenli_istek(url,api_adi,timeout=5):
    try:
        cevap = requests.get(url,timeout=timeout)
        cevap.raise_for_status()
        return cevap.json()
    except requests.exceptions.Timeout:
        print(f"[HATA] {api_adi} sunucusu çok yavaş,zaman aşımı!")
        return None
    except requests.exceptions.ConnectionError:
        print(f"[HATA] {api_adi} sunucusuna bağlanılamadı (İnternet yok veya site kapalı!)")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"[HATA] {api_adi} sunucusu bozuk yanıt verdi: {e}")
        return None

def ip_getir():
    print("[İŞÇİ 1 BAŞLADI] IP adresi aranıyor....")
    veri = guvenli_istek("https://api.ipify.org?format=json","IP API")
    if veri:
        print(f"[İŞÇİ 1 BAŞARILI] IP Adresin: {veri['ip']}")
    print("[İŞÇİ 1 BİTTİ] IP işlemi tamamlandı.\n")

def aktivite_getir():
    print("[İŞÇİ 2 BAŞLADI] Rastgele aktivite aranıyor....")
    veri = guvenli_istek("https://www.boredapi.com/api/activity","Bored API")
    if veri:
        print(f"[İŞÇİ 2 BAŞARILI] Aktivite Önerisi: {veri['activity']}")
    print("[İŞÇİ 2 BİTTİ] Aktivite işlemi tamamlandı.\n")

def saka_getir():
    print("[İŞÇİ 3 BAŞLADI] Rastgele şaka aranıyor....")
    veri = guvenli_istek("https://official-joke-api.appspot.com/random_joke","Joke API")
    if veri:
        print(f"[İŞÇİ 3 BAŞARILI] Şaka: {veri['setup']} --- {veri['punchline']}")
    print("[İŞÇİ 3 BİTTİ] Şaka işlemi tamamlandı.\n")    
print("---------- SIRALI ÇALIŞTIRMA BAŞLIYOR -------------")
baslangic_zamani = time.time()

ip_getir()
aktivite_getir()
saka_getir()

bitis_zamani = time.time()
sirali_sure = bitis_zamani - baslangic_zamani
print("----------- SIRALI ÇALIŞTIRMA BİTTİ --------------")
print(f"Sıralı Çalıştırma Toplam Süresi: {sirali_sure:.2f} saniye\n")

print("----------- THREADING ÇALIŞTIRMA BAŞLIYOR --------------")
baslangic_zamani_thread = time.time()

t1 = threading.Thread(target=ip_getir)
t2 = threading.Thread(target=aktivite_getir)
t3 = threading.Thread(target=saka_getir)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

bitis_zamani_thread = time.time()

thread_sure = bitis_zamani_thread - baslangic_zamani_thread

print("------------- THREADING ÇALIŞTIRMA BİTTİ ---------------")
print(f"Sıralı Çalıştırma Süresi: {sirali_sure:.2f} saniye")
print(f"Threading Toplam Süresi: {thread_sure:.2f} saniye")

if thread_sure > 0:
    hiz_farki = sirali_sure / thread_sure
    print(f"SONUÇ: Threading ile tam {hiz_farki:.1f} kat DAHA HIZLI işlem yaptık.\n")