for i in range(5):
    print(f"i'nin su anki degeri: {i}")

isimler = ['elma', 'muz', 'kiraz']
print("Meyveler listesi:")
for meyve in isimler:
    print(meyve)

while True:
    print("1-Ekle")
    print("2-Listele")
    print("3-Cikis")
    secim = input("Seciminizi yapiniz (1-3): ")

    if secim == '3':
        break

for sayi in range(1, 11):
    if sayi % 2 == 0:
        continue
    print(f"Tek sayi: {sayi}")