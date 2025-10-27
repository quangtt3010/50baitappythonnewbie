import math
def so_chinh_phuong(n):
    if n<0:
        return False
    if n==0:
        return True
    k = int(math.sqrt(n))
    return k*k==n



    