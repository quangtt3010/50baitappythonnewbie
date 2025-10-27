def so_nguyen_to(n):
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
x = int(input("nhập số đầu : "))
y = int(input("nhập số cuối : "))
list_a=[]
for num in range(x, y + 1):
    if so_nguyen_to(num):
        
        list_a.append(num)
print(f"Các số nguyên tố tìm thấy là: {list_a}")
