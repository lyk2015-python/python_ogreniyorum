from tarihzaman import Tarih

test1 = Tarih(yil=2015, ay=8, gun=16)
test2 = Tarih(tarih="2014-7-13")
test3 = test1 + test2
test4 = test1 - test2

if test1 == test2:
    print("test1 ile test2 eşitmiş")

if test1 != test2:
    print("test1 ile test2 eşitdeğilmiş")

if test1 < test2:
    print("test2 büyükmüş")

if test1 > test2:
    print("test1 büyükmüş")

print(int(test1))
print(str(test1))
