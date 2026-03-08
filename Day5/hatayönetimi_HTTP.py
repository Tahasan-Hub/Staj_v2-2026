import requests

def guvenli_istek(url,timeout=5):
    try:
        response = requests.get(url,timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"UYARI {url} zaman aşımı!")
        return None
    except requests.exceptions.ConnectionError:
        print(f"UYARI:{url} bağlantı hatası!")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"UYARI: HTTP hatası: {e}")
        return None
veri = guvenli_istek("https://api.ipify.org?format=json")    
if veri:
    print(f"IP: {veri['ip']}")
else:
    print("Veri alınamadı!")    