n = int(input("nhập số "))
m = int(input("nhập số "))
tong=0
for i in range(n,m+1):
    if i%3==0:
        tong+=1
print("có ",tong,"chia hết cho 3" )