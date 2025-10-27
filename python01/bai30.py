def cac_so_chia_het(n,m):
    tong = 0
    for i in range(n,m+1):
        if i%3==0 or i%5==0:
            tong += 1
            
    return tong
def cac_so_chan(n,m):
    sum = 0
    for i in range(n,m+1):
        if i%2==0:
            sum += i
            
    return sum 
n = int(input("nhập số "))
m = int(input("nhập số "))
print(f"Số lượng số chia hết cho 3 hoặc 5 từ {n} đến {m} là: {cac_so_chia_het(n, m)}")
print(f"Tổng các số chẵn từ {n} đến {m} là: {cac_so_chan(n, m)}")



