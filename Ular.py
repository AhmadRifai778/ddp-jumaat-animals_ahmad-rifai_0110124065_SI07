# Ular.py
from Animal import Animal

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, panjang, berbisa):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.berbisa = berbisa

    def melata(self):
        berbisa_status = "berbisa" if self.berbisa else "tidak berbisa"
        return f"{self.name} melata di tanah. Ular ini {berbisa_status}."
