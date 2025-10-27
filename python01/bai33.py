def so_nguyen_to(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
x = int(input("nhập số :"))
y = int(input("nhập số :"))
lista=[]
tong = 0
soluong = 0
for num in range(x,y+1):

    if so_nguyen_to(num):
        tong+=num
        soluong+=1
        lista.append(num)
        tbc = tong/soluong
print(lista)
print(tbc)    
    