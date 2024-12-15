# Burung.py
from Animal import Animal

class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_paruh, warna_bulu):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_paruh = jenis_paruh
        self.warna_bulu = warna_bulu

    def terbang(self):
        return f"{self.name} sedang terbang dan lagi nyantai di langit dengan bulu berwarna {self.warna_bulu}."
