#Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))
#Kiểm tra số chẵn hay lẻ
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "là số lẻ.")
#In ra số nguyên vừa nhập
print("Số nguyên vừa nhập là:", so)