def selamla():
    print("Merhaba, nasılsın?")

selamla()

def toplama(a,b):
    print("Toplam:", a + b)
   
sonuc = toplama(5, 8)
print("Fonksiyonun döndürdüğü değer:", sonuc)

def topla(a, b):
    return a + b

sonuc = topla(5, 8)
print("Fonksiyonun döndürdüğü değer:", sonuc)


def selamlar(isim="Ziyaretçi"):
    print(f"Merhaba, {isim}!")

selamlar("Ahmet")
selamlar()  # Varsayılan parametre kullanımı

def topla(*sayilar):
    print("Toplam:", sum(sayilar))

topla(1, 2, 3)
topla(5, 10, 15, 20)
topla()  # Hiç argüman verilmediğinde

def bilgi_goster(**bilgiler):
    print(bilgiler)

bilgi_goster(ad="Ayşe", soyad="Kara", yas=30)

kare = lambda x: x * x
print("Kare:", kare(5))

x = 10

def test():
    x = 20
    print("Fonksiyon içindeki x:", x)

test()
print("Global:", x)

kullanicilar = []

def kullanici_ekle():
    ad = input("İsim gir: ")
    kullanicilar.append(ad)
    print("Kullanıcı eklendi.")

def listele():
    if len(kullanicilar) == 0:
        print("Kullanıcı listesi boş.")
    else:
        print("Kullanıcılar:")
        for kullanici in kullanicilar:
            print("-", kullanici)

def sil():
    listele()
    no = int(input("Silinecek kullanıcı numarasını gir: "))
    if 0 <= no <= len(kullanicilar):
        kullanicilar.pop(no - 1)
        print("Kullanıcı silindi.")
    else:
        print("Geçersiz numara.")


while True:
    print("\n1. Kullanıcı Ekle\n2. Kullanıcıları Listele\n3. Kullanıcı Sil\n4. Çıkış")
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        kullanici_ekle()
    elif secim == "2":
        listele()
    elif secim == "3":
        sil()
    elif secim == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim.")
        
