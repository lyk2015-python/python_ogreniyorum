class Tarih:
    def __init__(self, yil=None, ay=None, gun=None, tarih=None):
        """
        __init__ constructor methodudur

        Tarih(yil=2015, ay=7, gun=3)
        Tarih(tarih="2015-7-3")
        Tarih(yil=2015, ay=7, gun=3, tarih="2015-7-3")  # ValueError
        """
        pass

    def __str__(self):
        """
        __str__ print(obje) dendiğinde çalışan methoddur ve string return eder.
        <Tarih yil=2015 ay=7 gun=3>
        """
        pass

    def __int__(self):
        """
        return self.yil*365 + self.ay*30 + self.gun
        """
        pass

    def __eq__(self, other):
        """
        __eq__ == denildiğinde çalışan methoddur
        """
        self_total_gun = self.yil * 365 + self.ay * 30 + self.gun
        other_total_gun = other.yil * 365 + other.ay * 30 + other.gun
        return self_total_gun == other_total_gun

    def __ne__(self, other):
        """
        __nq__ != denildiğinde çalışan methoddur
        """
        pass

    def __gt__(self, other):
        """
        __gt__ > denildiğinde çalışan methoddur
        """
        pass

    def __lt__(self, other):
        """
        __lt__ < denildiğinde çalışan methoddur
        """
        pass

    def __add__(self, other):
        """
        __add__ + denildiğinde çalışan methoddur

        yenitarihin_yili = self.yil + other.yil
        yenitarihin_ayi  = self.ay + other.ay  # 12'un üstüne çıkmamalı, çıkarsa yıl'ı arttırmak gerek
        yenitarihin_gunu = self.gun + other.gun  # 30'un üstüne çıkmamalı, çıkarsa ay'ı arttırmak gerek
        return Tarih(yil=yenitarihin_yili, ay=yenitarihin_ayi, gun=yenitarihin_gunu)

        """
        pass

    def __sub__(self, other):
        """
        __sub__ - denildiğinde çalışan methoddur
        """
        pass
