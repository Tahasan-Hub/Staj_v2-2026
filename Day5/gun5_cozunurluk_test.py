def dinamik_mesafe_hesapla(kamera_genislik,kamera_yukseklik):
    referans_genislik = 640
    referans_mesafe = 50
    oran = kamera_genislik / referans_genislik
    yeni_max_mesafe = int(referans_mesafe * oran)
    print(f"Test Edilen Çözünürlük: {kamera_genislik}x{kamera_yukseklik}")
    print(f"Büyüme Oranı: {oran} kat")
    print(f"Kullanılması Gereken Yeni max_mesafe: {yeni_max_mesafe}")
dinamik_mesafe_hesapla(640,480)
dinamik_mesafe_hesapla(1280,720)
dinamik_mesafe_hesapla(1920,1080)    