# Ikan.py
from Animal import Animal

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, jenis_sirip):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.jenis_sirip = jenis_sirip

    def berenang(self):
        return f"{self.name} berenang lincah di {self.habitat}."
