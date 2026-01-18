print("Merhaba, Dünya!")

"""Bu basit Python programı, ekrana 'Merhaba, Dünya!' mesajını yazdırır."""
#Merhaba Dünya! mesajını ekrana yazdırır

isim = "Ahmet"
yas = 25

sayi = "10"
sayi = int(sayi)

print(sayi + 15)

isim = input("Lütfen isminizi girin: ")
print("Merhaba, " + isim + "!")

a = 10
b = 3

print("Toplama:", a + b)
print("Çıkarma:", a - b),
print("Çarpma:", a * b)
print("Bölme:", a / b)
print("Tam Bölme:", a // b)
print("Kalan:", a % b)
print("Üs Alma:", a ** b)


""" = tek eşittir atamadır. == çift eşittir karşılaştırmadır. """
print(5 > 3)   # Doğru
print(2 < 1)   # Yanlış
print(4 >= 4)  # Doğru
print(3 <= 2)  # Yanlış
print(5 == 5)  # Doğru
print(4 != 4)  # Yanlış
print((3 > 2) and (5 > 4))  # Doğru
print((3 > 2) or (5 < 4))   # Doğru
print(not (3 > 2))          # Yanlış

yas = 18

if yas >= 18:
    print("Reşitsiniz.")    
else:
    print("Reşit değilsiniz.")

notu = 75

if notu >= 85:
    print("Notunuz: A")
elif notu >= 70:
    print("Notunuz: B")
elif notu >= 50:
    print("Notunuz: C")
else:
    print("Notunuz: F")

yas = 20
mezun = False

if yas >= 18 or mezun:
    print("İşe başvurabilirsiniz.")
else:
    print("İşe başvuramazsınız.")


for i in range(5):
    print("Sayı:", i)

sayi = 0
while sayi < 5:
    print("Sayı:", sayi)
    sayi += 1

for i in range(1, 11):
    if i == 5:
        break
    print("Sayı:", i)

for i in range(1, 11):
    if i == 3:
        continue
    print("Sayı:", i)

sayi1 = float(input("Bir sayı girin"))
sayi2 = float(input("Bir sayı girin"))

print("Toplama için +")
print("Çıkarma için -")
print("Çarpma için *")
print("Bölme için /")

islem = input("Yapmak istediğiniz işlemi seçin: ")

if islem == '+':
    print("Sonuç:", sayi1 + sayi2)
elif islem == '-':
    print("Sonuç:", sayi1 - sayi2)
elif islem == '*':
    print("Sonuç:", sayi1 * sayi2)
elif islem == '/':
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
            print("Hata: Bir sayı sıfıra bölünemez.")
