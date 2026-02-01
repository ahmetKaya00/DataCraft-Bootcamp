ogrenciler = {}

ortalama_lambda = lambda notlar: sum(notlar) / len(notlar) if notlar else 0

def gecti_mi(ortalama):
    return ortalama >= 50

def harf_notu(ortalama):
    if ortalama >= 85:
        return 'A'
    elif ortalama >= 70:
        return 'B'
    elif ortalama >= 60:
        return 'C'
    elif ortalama >= 50:
        return 'D'
    else:
        return 'F'

def notlari_al():
    notlar = []

    for i in range(1,4):
        while True:
            giris = input(f"{i}. notu giriniz (0-100 arasi): ")
            if giris.isdigit():
                not_degeri = int(giris)
                if 0 <= not_degeri <= 100:
                    notlar.append(not_degeri)
                    break
                else:
                    print("Lutfen 0 ile 100 arasinda bir sayi giriniz.")
            else:
                print("Lutfen gecerli bir sayi giriniz.")
    return notlar

def ogrenci_ekle():
    numara = input("Ogrenci numarasini giriniz: ")
    ad = input("Ogrenci adini giriniz: ")
    soyad = input("Ogrenci soyadini giriniz: ")

    notlar = notlari_al()

    ogrenciler[numara] = {
        'ad': ad,   
        'soyad': soyad,
        'notlar': notlar
    }
    print(f"{ad} {soyad} basariyla eklendi.")

def ogrencileri_listele():
    if len(ogrenciler) == 0:
        print("Kayitli ogrenci yok.")
        return
    for numara, bilgi in ogrenciler.items():
        notlar = bilgi['notlar']
        ortalama = ortalama_lambda(notlar)
        durum = "Gecti" if gecti_mi(ortalama) else "Kaldi"
        harf = harf_notu(ortalama)
        print(f"Ogrenci No: {numara}, Ad: {bilgi['ad']}, Soyad: {bilgi['soyad']}, Notlar: {notlar}, Ortalama: {ortalama:.2f}, Durum: {durum}, Harf Notu: {harf}")

def ogrenci_sil():
    numara = input("Silinecek ogrenci numarasini giriniz: ")
    if numara in ogrenciler:
        del ogrenciler[numara]
        print(f"Ogrenci numarasi {numara} silindi.")
    else:
        print("Boyle bir ogrenci bulunamadi.")

while True:
    print("\nOgrenci Not Takip Sistemi")
    print("1. Ogrenci Ekle")
    print("2. Ogrencileri Listele")
    print("3. Ogrenci Sil")
    print("4. Cikis")

    secim = input("Seciminizi yapiniz (1-4): ")

    if secim == '1':
        ogrenci_ekle()
    elif secim == '2':
        ogrencileri_listele()
    elif secim == '3':
        ogrenci_sil()
    elif secim == '4':
        print("Cikis yapiliyor...")
        break
    else:
        print("Gecersiz secim, lutfen tekrar deneyiniz.")