def tim_ucln(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a
a = int(input("nhập số : "))
b = int(input("nhâp số : "))
c = (a/tim_ucln(a, b))/(b/tim_ucln(a, b))
print (c)