# main.py
from Burung import Burung
from Ikan import Ikan
from Ular import Ular

# Membuat objek untuk masing-masing kelas
# Objek Burung
burung1 = Burung("Elang", "Daging", "Darat", "Bertelur", "Paruh Tajam", "Coklat")
burung2 = Burung("Merpati", "Biji-bijian", "Darat", "Bertelur", "Paruh Pendek", "Putih")

# Objek Ikan
ikan1 = Ikan("Hiu", "Ikan kecil", "Air", "Bertelur", "Laut", "Sirip Tajam")
ikan2 = Ikan("Koi", "Pelet", "Air", "Bertelur", "Kolam", "Sirip Pendek")

# Objek Ular
ular1 = Ular("Kobra", "Hewan kecil", "Darat", "Bertelur", "2 meter", True)
ular2 = Ular("Sanca", "Hewan besar", "Darat", "Bertelur", "5 meter", False)

# Menampilkan informasi dari si hewannya

# Burung
print(burung1.info())
print(burung1.terbang())
print(burung2.info())
print(burung2.terbang())

# Ikan
print(ikan1.info())
print(ikan1.berenang())
print(ikan2.info())
print(ikan2.berenang())

# Ular
print(ular1.info())
print(ular1.melata())
print(ular2.info())
print(ular2.melata())
