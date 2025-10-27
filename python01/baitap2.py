thang = int(input("nhập tháng vào đây:"))
nam = int(input("nhập năm vào đây : "))
if thang in [1,3,5,7,8,10,12]:
    print("tháng có 31 ngày")
elif thang ==2 :
    if nam%4==0:
         print("tháng có 29 ngày")
    else:
        print("tháng có 28 ngày")
else:
    print("tháng có 30 ngày")