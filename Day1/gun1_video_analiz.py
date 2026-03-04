import cv2
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--kaynak",default="0",help="Kamera için 0,video için dosya yolu girin.")
args = parser.parse_args()

if args.kaynak == "0":
    cap = cv2.VideoCapture(0)
    print("Kamera Açılıyor...")
else:
    #Eğer 0 dışında birşey yazıldıysa onu dosya yolu olarak kaydet!!!
    cap = cv2.VideoCapture(args.kaynak)
    print(f"{args.kaynak} dosyası üzerinden işlem yapılıyor...")

if not cap.isOpened():
    print("HATA: Görüntü kaynağına ulaşılamadı! Lütfen kaynağı kontrol edin.")
    exit() #Program burda durur. Hata verilmesini engeller.

baslangic_zamani = time.time()
toplam_frame = 0

p_time = 0

while True:
    ret,frame = cap.read()

    if not ret:
        print("ULAŞILAMADI.Döngüden çıkılıyor.")
        break #Döngüyü sonlandırır

    toplam_frame += 1

    c_time = time.time()

    isleme_fps = 1 / (c_time - p_time)
    p_time = c_time

    cv2.putText(frame,f"FPS: {int(isleme_fps)}",(20,50),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2)
    

    cv2.imshow("Analiz Ekrani",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Kullanıcı 'q' tuşuna bastı,kapatılıyor...")
        break
cap.release()
cv2.destroyAllWindows()    

bitis_zamani = time.time()
gecen_sure = bitis_zamani - baslangic_zamani

if gecen_sure > 0:
    ortalama_fps = toplam_frame/gecen_sure
else:
    ortalama_fps = 0

print(f"Toplam Kare Sayısı: {toplam_frame} frame")
print(f"Toplam Geçen Süre: {gecen_sure:.2f} saniye")
print(f"Ortalama FPS: {ortalama_fps:.2f} FPS")

