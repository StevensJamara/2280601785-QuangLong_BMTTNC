def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
# Sử dụng hàm và in kết quả:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd' : 4}
key_to_remove = 'b'
result = xoa_phan_tu(my_dict, key_to_remove)
if result:
    print(f"Đã xóa phần tử có khóa '{key_to_remove}' khỏi dictionary.", my_dict)
else:
    print(f"Không tìm thấy phần tử có khóa '{key_to_remove}' trong dictionary.")