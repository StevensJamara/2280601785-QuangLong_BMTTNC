def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Nhập danh sách từ người dùng 
input_list = input("Nhập danh sách số nguyên (cách nhau bởi dấu cách): ")
world_list = input_list.split()

# Đếm số lần xuất hiện của từng phần tử
so_lan_xuat_hien = dem_so_lan_xuat_hien(world_list)
print("Số lần xuất hiện của từng phần tử là:", so_lan_xuat_hien)  