s1 = input("Bir sayı giriniz: ") or None
s2 = input("Bir sayı daha giriniz: ")
try:
    s1 = int(s1)
    s2 = int(s2)
    print(s1 / s2)
except ZeroDivisionError:
    print("Sıfır sıfıra bölünmez")
except ValueError:
    print("Harf Girilmez")
else:
    print("Yehuuu hata yok")
finally:
    print("Bitti nihayet")

print("Bitti nihayet cidden")
# 10 / 2 == 5.0
#    / 2 == TypeError
# ab / 2 == ValueError
#  0 / 0 == ZeroDivisionError
