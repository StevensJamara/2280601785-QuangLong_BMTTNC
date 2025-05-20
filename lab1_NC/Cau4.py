def truy_cap_phan_tu(turple_data):
    first_Ele = turple_data[0]
    last_Ele = turple_data[-1]
    return first_Ele, last_Ele

# Nhập danh sách từ người dùng và xử lý chuỗi
input_turple = input("Nhập danh sách số nguyên (cách nhau bởi dấu phẩy): ")
first, last = truy_cap_phan_tu(input_turple)

# In ra phần tử đầu tiên và cuối cùng
print("Phần tử đầu tiên là:", first)
print("Phần tử cuối cùng là:", last)