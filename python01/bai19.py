
n = float(input("nhập số km vào đây : "))
tien = 0
if 0<n<=1:
        tien+=n*10.000
elif 1<n<=10:
        tien+=10.000+(n-1)*8.000
else:
    tien+=10.000+9*8.000+(n-10)*6.000
    if n>50:
        tien*=0.9
print(tien)