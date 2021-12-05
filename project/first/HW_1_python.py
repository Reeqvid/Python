# 1. Создать переменную типа String
a = "OLeg"
print(a, type(a))
# 2. Создать переменную типа Integer
b = 13
print(b, type(b))
# 3. Создать переменную типа Float
c = 13.3
print(c, type(c))
# 4. Создать переменную типа Bytes
d = b"sd123asddasd"
print(d, type(d))
# 5. Создать переменную типа List
f = ["ghbdtn", "Kak dela", "normal"]
print(f, type(f))
# 6. Создать переменную типа Tuple
g = ("Privet", "Poka", "Spisok")
print(g, type(g))
# 7. Создать переменную типа Set
h = {"a", 13, "C", "array"}
print(h, type(h))
# 8. Создать переменную типа Frozen Set
z = ["Array", "List"]
fz = frozenset(z)
print(z, type(fz))
# 9. Создать переменную типа Dict
x = {"Name": "Oleg", "age": "24"}
print(x, type(x))

# 10. Создать 2 переменные типа String и сканкатенировать в другой переменной
qw = "Oleg "
qe = "Tsaryuk"
qa = qw + qe
print(qa)
# 11 Вывести в одну строку переменные типа string и integer
# используя ','
print(str(b), qw)
# 12 Вывести в одну строку переменные типа string и integer
# используя '+'
print("String + integer --", str(b) + " " + qw)
