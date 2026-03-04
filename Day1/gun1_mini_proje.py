import cv2
import time
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--kaynak",default="0",help="Kamera icin 0,dosya yolu icin ismini yazin.")
parser.add_argument("--confidence",type=float,default=0.5,help="YOLO guven orani")
args = parser.parse_args()

print(f"Kaynak: {args.kaynak}, Guven: {args.confidence}")

if args.kaynak == "0":
    print(f"Kamera Başlatılıyor... (Güven Eşiği: {args.confidence})")
    cap = cv2.VideoCapture(0)
else:
    if not os.path.exists(args.kaynak):
        print(f"HATA: '{args.kaynak}' dosyası bulunamadı!")
        print("Lütfen dosya ismini doğru yazdığından emin ol.")    
        exit() #Hata varsa programı burada durdur.
    print(f"Video dosyasıaçılıyor: {args.kaynak}")
    cap = cv2.VideoCapture(args.kaynak)
if not cap.isOpened():
    print("HATA: Kaynak açılamadı (Kamera meşgul yada dosya bozuk!!!).")
    exit()       

baslangic_zamani = time.time()
toplam_frame = 0 #Sayaç sıfırlandı

print("Döngü başlıyor...Çıkmak için 'q' tuşuna bas.")

while True:
    ret,frame = cap.read()
    if not ret:
        print("Video sonuna gelindi veya sinyal yok.")
        break
    frame_baslangic = time.time()
    frame_bitis = time.time()
    gecen_sure = (frame_bitis - frame_baslangic) * 1000
    toplam_frame += 1
    
    cv2.putText(frame,f"ISLEM: {gecen_sure:.2f} ms",(10,30),cv2.FONT_HERSHEY_PLAIN,0.8,(0,0,255),2)
    cv2.putText(frame,f"FRAME: {toplam_frame}",(10,frame.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    cv2.imshow("Mini Proje",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Kullanıcı isteğiyle kapatılıyor...")
        break
cap.release()
cv2.destroyAllWindows()    

bitis_zamani = time.time()
toplam_gecen_sure = bitis_zamani - baslangic_zamani

if toplam_gecen_sure > 0:
    ort_fps = toplam_frame / toplam_gecen_sure
else:
    ort_fps = 0

print(f"Toplam {toplam_frame} frame , {toplam_gecen_sure:.3f} saniyede , {ort_fps:.2f} FPS'te analiz edildi.")
print("Program başarı ile çalıştı.")