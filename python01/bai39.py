n = int(input("nhập số phần tử trong mảng: "))
mang = []
for i in range(n):
    gia_tri = int(input(f"nhập phần tử thứ {i+1}: "))
    mang.append(gia_tri)
tong = sum(mang)
print(tong)