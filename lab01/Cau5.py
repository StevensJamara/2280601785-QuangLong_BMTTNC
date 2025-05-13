so_gio_lam = float(input("Nhập số giờ làm việc: "))
luong_mot_gio = float(input("Nhập lương một giờ làm việc: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_mot_gio + gio_vuot_chuan * luong_mot_gio * 1.5
print(f"Thực lĩnh là: {thuc_linh}")