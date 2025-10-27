def so_nguyen_to(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

k = int(input("nhập số vào : "))
listk = []
num =2
while len(listk) < k :

    if so_nguyen_to(num):
        listk.append(num)
    num +=1
print(f"{k} số nguyên tố đầu tiên là:")
print(listk)
