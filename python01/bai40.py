def dem_so_duong(x):
    return sum(1 for y in x if y>0)



n = int(input("nhập số phần tử trong mảng: "))
mang = []
for i in range(n):
    gia_tri = int(input(f"số phần tử thứ {i+1}: "))
    mang.append(gia_tri)
so_luong_duong = dem_so_duong(mang)
print(so_luong_duong)