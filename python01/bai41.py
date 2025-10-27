def dem_so_chan(x):
    return sum( 1 for y in x if y%2==0)


n = int(input("nhập số phần tử trong mảng: "))
mang = []
for i in range(n):
    gia_tri = int(input(f"phần tử thứ{i+1}: "))
    mang.append(gia_tri)
so_luong = dem_so_chan(mang)
print(so_luong)



    