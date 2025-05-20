def dao_nguoc_list(lst):
    return lst[::-1]
# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(',')))
# Đảo ngược danh sách
lst_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược là:", lst_dao_nguoc)