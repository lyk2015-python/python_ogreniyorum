__author__ = 'lyk-py'


# 1- DosyaYoneticisi diye bir sınıf
# 2- dy = DosyaYoneticisi(-)
# 3- dy.oku()  # "dosya icinde yazan sey bu"
# 4- dy.populer(sayi=3)  # {"ali":7, "veli":3, "selami":1}
# 5- dy.ilk_harf()  # her satırın ilk harfi
# 6- dy.wc()  # [karakter_sayisi, kelime_sayisi, satir_sayisi]

# İpuçları
# #-----3
# f = open("dosya.adi")
# butunyazi = f.read()
# f.close()
#
# #-----4
# {
#     "ali": 15,
#     "aslı" :7,
#     "var": 3,
#     "python":1
# }
#
#  #-----5
# dosya_icerigi = self.oku()
# dosya_icerigi.split("\n")
#
#  #-----6
# [
#     len(self.oku())
#     len(self.oku().split())
#     len(self.oku().split("\n"))
# ]


class DosyaYoneticisi:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi

    def oku(self):
        f = open(self.dosya_adi)
        yazi = f.read()
        f.close()
        return yazi
        # Alternatif:
        # with open(self.dosya_adi) as f:
        #     return f.read()

    def populer(self, sayi):
        adetler = {}
        for kelime in self.oku().split():
            if kelime in adetler:
                adetler[kelime] += 1
            else:
                adetler[kelime] = 1

        yeni_sayilar = list(adetler.items())
        yeni_sayilar.sort(key=lambda x: x[1], reverse=True)

        return dict(yeni_sayilar[:sayi])
        # Alternatif:
        # from collections import Counter
        # skorlar = Counter(self.oku().split())
        # return dict(skorlar.most_common(3))

    def ilk_harf(self):
        dosya = self.oku()
        satirlar = dosya.split("\n")
        return [satir[0] for satir in satirlar]

    def wc(self):
        return [
            len(self.oku()),
            len(self.oku().split()),
            len(self.oku().split("\n"))
        ]
