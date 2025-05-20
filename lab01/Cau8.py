#Hàm kiểm tra số nhị phân chia hết cho 5
def chia_het_cho_5(so_nhi_phan): 
    #Chuyển số nhị phân sang thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    #Kiểm tra số thập phân chia hết cho 5
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#Nhập số nhị phân từ người dùng
so_nhi_phan = input("Nhập một số nhị phân: (phân tích bởi dấu phẩy)")
