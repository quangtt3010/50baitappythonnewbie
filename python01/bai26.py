
m = int(input("nhập số: "))
tong = sum(i for i in range(1,m+1) if i%3==0 and i%5==0)
print(tong)
 