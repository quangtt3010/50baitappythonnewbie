import math
def so_chinh_phuong(n):
    if n<0:
        return False
    if n==0:
        return True
    k = int(math.sqrt(n))
    return k*k==n

k = int(input("nhập số vào:"))
dem =0
listk = []
while len(listk) < k :
    if so_chinh_phuong(dem):
        listk.append(dem)
    dem+=1
print(listk)

    