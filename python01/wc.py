def tinh_tong_vi_tri_chan(arr):
    return sum(arr[i] for i in range(0, len(arr), 2))
# Nhập số lượng phần tử của mảng
n = int(input("Nhập số phần tử của mảng: "))
# Nhập các phần tử của mảng từ người dùng
mang = []
for i in range(n):
    gia_tri = int(input(f"Nhập phần tử thứ {i+1}: "))
    mang.append(gia_tri)
# Tính tổng các phần tử ở vị trí chẵn
tong_vi_tri_chan = tinh_tong_vi_tri_chan(mang)
# Hiển thị kết quả
print(f"Tổng các phần tử ở vị trí chẵn trong mảng là: {tong_vi_tri_chan}")

