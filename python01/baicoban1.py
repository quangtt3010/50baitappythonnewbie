# 1. Khai báo các mệnh giá tiền (đã sắp xếp giảm dần)
MENH_GIA = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000]

# 2. Yêu cầu người dùng nhập số tiền
try:
    so_tien_can_doi = int(input("Nhập số tiền cần đổi (phải chia hết cho 1000): "))

    # Kiểm tra xem tiền có hợp lệ không
    if so_tien_can_doi <= 0:
        print("Số tiền phải là số dương.")
    elif so_tien_can_doi % 1000 != 0:
        print("Số tiền phải chia hết cho 1000.")
    else:
        print(f"--- Đổi {so_tien_can_doi:,} VND ---")
        
        # Biến này để giữ số tiền còn lại sau mỗi lần đổi
        so_tien_con_lai = so_tien_can_doi
        
        # 3. Bắt đầu vòng lặp (Thuật toán tham lam)
        for to_tien in MENH_GIA:
            # 4. Tính số tờ của mệnh giá hiện tại
            # Dùng phép chia lấy phần nguyên (//)
            so_to = so_tien_con_lai // to_tien
            
            # 5. Cập nhật số tiền còn lại
            # Dùng phép chia lấy phần dư (%)
            so_tien_con_lai = so_tien_con_lai % to_tien
            
            # 6. In kết quả nếu có tờ tiền nào được dùng
            if so_to > 0:
                print(f"{so_to} tờ {to_tien:,} VND")

except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
    

    
 