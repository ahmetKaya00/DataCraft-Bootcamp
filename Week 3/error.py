#SyntaxError

if 5 > 3:
    print("Five is greater than three.")

print("This line is outside the if block.")

if 10 < 5:
    print("Ten is less than five.")

sayi = 10
print(sayi)

yas = 20
print("Yaşım:" + str(yas))

s = "123"
print(int(s))

liste = [10,20,30]
i = 3
if i < len(liste):
    print(liste[i])
else:
    print("Index out of range.")

kisi = {"ad": "Ali", "yas": 25}
print(kisi.get("meslek", "Anahtar bulunamadı."))


bolen = 0
if bolen != 0:
    print(10/bolen)
else:
    print("Bölme işlemi için bölen sıfır olamaz.")

x = "MERHABA"
print(x.lower())

fiyat = 150
indirim = 20

sonuc = fiyat * (1-indirim/100)
print("İndirimli fiyat:", sonuc)