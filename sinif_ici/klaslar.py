class Insan:
    def __init__(self, ad, yas, gizli=None):
        self.ad = ad
        self.yas = yas
        self._gizli = gizli

    def konus(self):
        print("Bla bla bla")

    def get_gizli(self):
        return self._gizli


class Ogrenci(Insan):
    def calis(self, saat=1):
        for i in range(saat):
            print("Bi saat çalıştım")

    def konus(self):
        print("Laga luga")


class Ogretmen(Insan):
    def ogret(self, saat=1):
        for i in range(saat):
            print("Bi saat öğrettim")


class Sinif:
    def __init__(self, isim, kat):
        self.isim = isim
        self.kat = kat
        self.isiklar_yaniyor = False
        self.ogrenciler = []
        self.ogretmenler = []

    def isiklar(self):
        if self.isiklar_yaniyor:
            print("Işıklar Söndü")
        else:
            print("Işıklar Yandı")

        self.isiklar_yaniyor = not self.isiklar_yaniyor

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)

    def ogretmen_ekle(self, ogretmen):
        self.ogretmenler.append(ogretmen)
