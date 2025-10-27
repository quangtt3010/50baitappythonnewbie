n = int(input("nhập số:"))
m = int(input("nhập số:"))
tong = sum(i for i in range(n,m+1) if i%3==0 or i%5==0)
    
        
print(f"Tổng các số chia hết cho 3 hoặc 5 từ {n} đến {m}: {tong}")