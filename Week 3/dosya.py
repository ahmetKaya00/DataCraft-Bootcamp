dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.read()
print(icerik)
dosya.close()

dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.readlines()
print(icerik)
dosya.close()

dosya = open("yazi.txt", "w", encoding="utf-8")
dosya.write("Merhaba Yobodobo!\n")
dosya.write("Python ile dosya işlemlerini işliyoruz.\n")
dosya.close()

dosya = open("yazi.txt", "a", encoding="utf-8")
dosya.write("Merhaba!\n")
dosya.write("Python işliyoruz.\n")
dosya.close()

with open("ornek.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

try:
    with open("olmayan_dosya.txt", "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
        print(icerik)
except FileNotFoundError:
    print("Dosya bulunamadı.")

ad = input("Adınızı girin: ")

with open("kullanicilar.txt", "a", encoding="utf-8") as dosya:
    dosya.write(ad + "\n")


    