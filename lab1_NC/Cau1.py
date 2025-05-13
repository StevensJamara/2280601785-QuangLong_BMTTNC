def tinh_tong_chan(list):
    tong = 0
    for num in list:
        if num % 2 == 0:
            tong += num
    return tong
# Nhập danh sách số nguyên từ người dùng
input_list = input("Nhập danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(',')))
# Tính tổng các số chẵn trong danh sách
tong_chan = tinh_tong_chan(numbers)
print ("Tổng các số chẵn trong danh sách là:", tong_chan)