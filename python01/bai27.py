def la_so_nguyen_to(n):
    if n <2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n = int(input("nhập số vào : "))
print(f"{n} là số nguyên tố " if la_so_nguyen_to(n) else f"{n} không phải là số nguyên tố")