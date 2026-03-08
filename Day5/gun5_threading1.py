import threading
import time

def is_1():
    print("1.iş başladı....")
    time.sleep(2)
    print("1.iş bitti!")
def is_2():   
    print("2.iş başladı...")
    time.sleep(3)
    print("2.iş bitti!")
def is_3():
    print("3.iş başladı.....")
    time.sleep(4)
    print("3.iş bitti!")
print("---- SIRALI ÇALIŞTIRMA BAŞLIYOR ----")
baslangic_zamani = time.time()
is_1()
is_2()
is_3()    #1.iş bitmeden 2'ye 2 bitmeden 3'e ASLA geçmez

bitis_zamani = time.time()
toplam_sure = bitis_zamani - baslangic_zamani
print(f"Sıralı çalıştırma toplam {toplam_sure:.2f} saniye sürdü.\n")

print("--- THREADING İLE ÇALIŞTIRMA BAŞLIYOR ---")
baslangic_zamani_thread = time.time()

t1 = threading.Thread(target=is_1)
t2 = threading.Thread(target=is_2)
t3 = threading.Thread(target=is_3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join() # join komutu ile ana programın bunlar bitirene kadar beklemesini sağlıyoruz
bitis_zamani_thread = time.time()
toplam_sure_thread = bitis_zamani_thread - baslangic_zamani_thread

print(f"Threading ile çalıştırma toplam {toplam_sure_thread:.2f} saniye sürdü.\n")

