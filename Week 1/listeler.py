notlar = [70,80,90]
print(notlar)
notlar.append(100)
print(notlar)
notlar.remove(80)
print(notlar)
notlar.sort()
print(notlar)
notlar.reverse()
print(notlar)
notlar[0] = 95
print(notlar)
notlar[-1] = 85
print(notlar)
notlar.insert(1, 75)
print(notlar)

gunler = ("Pazartesi", "Sali", "Carsamba")
print(gunler)
#gunler[0] = "Pazar" HATA VERİR GÜNCELLEME EKLEME ÇIKARMA OLMAZ
#print(gunler)

kisi = {"ad": "Ali","soyad": "Veli", "yas": 25}

print(kisi)
kisi["yas"] = 26
print(kisi)
kisi["meslek"] = "Mühendis"
print(kisi)

s = {9,1,6,2,3,4,4,3,5,6,3}
print(s)