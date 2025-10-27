# dùng lệnh for
n = int(input("nhập số"))
m = int(input("nhập số"))
tong= sum( i for i in range(n,m+1) if i%2==0)

print(tong)