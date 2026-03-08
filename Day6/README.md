GuardWatch AI - Akıllı Güvenlik Sistemi

PROJE HAKKINDA
GuardWatch AI,kamera üzerinden gerçek zamanlı olarak çalışan yapay zeka destekli bir güvenlik ve takip sistemidir.Sistem; kişilerin uyku durumunu(EAR Algoritması) ve hareketsizlik durumlarını tespit eder,tehlike anında sesli alarm verir ve bu ihlalleri kayıt altına alır.
Ayrıca elde edilen veriler,bir Dashboard üzerinden grafiklere dökülür ve Flask web sunucusu ile canlı olarak izlenebilir.

KULLANILAN TEKNOLOJİLER
*YOLOv8 & MediaPipe: Nesne,yüz ve göz takibi.
*OpenCV: Görüntü işleme ve kamera yönetimi.
*Matplotlib & CSV: Veri kaydetme ve grafik çizimi.
*Flask: Canlı istatistik web sunucusu (API).

KURULUM
Projeyi kendi bilgisayarınızda çalıştırmak için gerekli kütüphaneleri indirin:
```bash
pip install -r requirements.txt

NASIL ÇALIŞTIRILIR
Sadece Kamerayı Açmak İçin:
python guardwatch_v2.py

Kayıt Modunda Çalıştırmak:
python guardwatch_v2.py --kayit

İstatistikleri ve Grafikleri Çıkartmak İçin:
python dashboard.py

Canlı Web Sunucusunu Başlatmak İçin:
python server.py