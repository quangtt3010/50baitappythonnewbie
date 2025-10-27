def in_k_so_chinh_phuong(k):
    danh_sach_chinh_phuong = [i * i for i in range(1, k + 1)]
    return danh_sach_chinh_phuong
# Nhập số lượng số chính phương cần tìm

k = int(input("Nhập số k: "))
# Kiểm tra điều kiện đầu vào

if k <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    print(f"{k} số chính phương đầu tiên là: {in_k_so_chinh_phuong(k)}")