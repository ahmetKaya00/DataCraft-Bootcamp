import hesaplama as h
from hesaplama import topla, cikar
from hesaplama import *
from araba import Araba
import sys

print("Toplama:", topla(10, 5))
print("Çıkarma:", cikar(10, 5))

a = Araba("Toyota", "Corolla", 2020)
print("Araba Bilgileri:", a.bilgileri_goster())

print(sys.path)