def tao_turple_tu_list(lst):
    return tuple(lst)
# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_turple_tu_list(numbers)
print("Lst: ", numbers)
print("Tuple được tạo từ danh sách là:", my_tuple)