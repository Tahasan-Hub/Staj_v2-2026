import argparse

parser = argparse.ArgumentParser(description='Argparse test etmek için bir test')
parser.add_argument("--isim") #Burda programa diyoruz ki Sana dışarıdan isim diye bir bilgi gelcek hazırlıklı ol
parser.add_argument("--yas" , type=int)
parser.add_argument("--ogrenci",action="store_true")
args = parser.parse_args() #Gelen bilgiyi yakalayıp 'args' paketine koyuyoruz
print(f"Adı: {args.isim}")
print(f"Yaşı: {args.yas}")

if args.ogrenci == True:
    print("Durum: Öğrenci")
else:
    print("Durum: Sivil")    
    