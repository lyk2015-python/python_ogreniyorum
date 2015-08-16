__author__ = 'lyk-py'
import dosyayonetim

dosya_adi = "lipsum.txt"
debug = False
try:
    dosyayonetim.DosyaYoneticisi
except AttributeError:
    print("DosyaYoneticisi bulunamadı!")
    exit()

try:
    dosyayonetim.DosyaYoneticisi(dosya_adi)
except TypeError:
    print("__init__ methodu düzgün çalışmıyor.")
    exit()

dy = dosyayonetim.DosyaYoneticisi(dosya_adi)

with open(dosya_adi) as f:
    gercek = f.read()

try:
    dosya = dy.oku()
    if debug:
        print(len(dosya), len(gercek))
    if len(dosya) != len(gercek):
        print("oku methodu hatalı cevap döndürdü")
        print("method'dan dönen:", len(dosya), "karakter")
        print("aslında dönmesi gereken:", len(gercek), "karakter")
        exit()
except AttributeError:
    print("oku methodu bulunamadı")
    exit()

with open(dosya_adi) as f:
    gercek = f.read()
    from collections import Counter

    skorlar = Counter(gercek.split())
    en_populer_uclu = dict(skorlar.most_common(3))

try:
    populerler = dy.populer(3)
    if debug:
        print(populerler, en_populer_uclu)
    if set(populerler.keys()) != set(en_populer_uclu.keys()):
        print("populer methodu yanlış cevap döndürdü")
        print("method'dan dönen:", set(populerler.keys()))
        print("aslında dönmesi gereken:", en_populer_uclu)
        exit()
except AttributeError:
    print("populer methodu bulunamadı")
    exit()

with open(dosya_adi) as f:
    gercek = f.read()
    gercek_harfler = [satir[0] for satir in gercek.split("\n")]

try:
    ilk_harfler = dy.ilk_harf()
    if debug:
        print(ilk_harfler, gercek_harfler)
    if ilk_harfler != gercek_harfler:
        print("ilk_harf methodu yanlış cevap döndürdü")
        print("method'dan dönen:", ilk_harfler)
        print("aslında dönmesi gereken:", gercek_harfler)
        exit()
except AttributeError:
    print("ilk_harf methodu bulunamadı")
    exit()

with open(dosya_adi) as f:
    gercek = f.read()
    gercek_sayimlar = [
        len(gercek),
        len(gercek.split()),
        len(gercek.split("\n"))
    ]

try:
    sayimlar = dy.wc()
    if debug:
        print(sayimlar, gercek_sayimlar)
    if sayimlar != gercek_sayimlar:
        print("wc yanlış cevap döndürdü")
        print("method'dan dönen:", sayimlar)
        print("aslında dönmesi gereken:", gercek_sayimlar)
        exit()
except AttributeError:
    print("ilk_harf methodu bulunamadı")
    exit()

print("HATA BULUNAMADI!")
