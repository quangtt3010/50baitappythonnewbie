def tinh_trung_binh(data: list[float]):
    if len(data) <=2:
        return 0.0
    maxl = max(data)
    minl = min(data)
    if minl == maxl:
        return 0.0
    tong = 0
    dem = 0
    for x in data:
        if x != minl and x!=maxl:
            tong+=x
            dem+=1
    if dem ==0:
        return 0.0
    else:
        return tong/dem 
vi_du1 = [4,5,5,5,5,5,6]
ket_qua = tinh_trung_binh(vi_du1)
print(f"ví dụ 1 :{vi_du1}")
print(f"giá trị trung bình đã loại bỏ min max: {ket_qua}")