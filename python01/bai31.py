def la_so_nguyen_to(x):
    if x <2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
n = int(input("nhập số: "))
m = int(input("nhập số: "))
count = 0
list_a=[]
for num in range(n, m + 1):
    if la_so_nguyen_to(num):
        count += 1
        list_a.append(num)
print(f"Các số nguyên tố tìm thấy là: {list_a}")
print(f"Tổng cộng có {count} số nguyên tố trong khoảng từ {n} đến {m}.")


