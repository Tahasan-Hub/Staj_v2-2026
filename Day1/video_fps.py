import cv2
import time

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("video1.mp4")

#Eğer dosya açılmadıysa hata verip çıkalım
if not cap.isOpened():
    print("Hata: Video kaynağı açılamadı!")
    exit()

video_fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Orijinal FPS: {video_fps}")

prev_time = 0

while True:
    ret,frame = cap.read()

    if not ret:
        print("Video bitti veya okunamadı. Çıkılıyor...")
        break

    gri_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    current_time = time.time()

    isleme_fps = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(frame,f"ISLEME HIZI: {int(isleme_fps)} FPS",(10,30),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),2)
    cv2.putText(frame,f"VIDEO Orijinal: {int(video_fps)} FPS",(10,70),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,0,255),2)
    cv2.imshow("Video Analiz",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    