def tong_so_chan(x):
    return sum(x[y] for y in range(0,len(x),2))
n = int(input("nhập số lượng phần tử : "))
mang=[]
for i in range(n):
    gia_tri = int(input(f"phần tử thứ{i+1}: "))
    mang.append(gia_tri)
tong_so = tong_so_chan(mang)
print(tong_so)
