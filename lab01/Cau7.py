#Nhập văn bản từ người dùng
print("Nhập các dòng văn bản: (Nhấn ENTER để kết thúc)")
van_ban = []
while True:
    dong = input()
    if dong.lower == "":
        break
    van_ban.append(dong)
#Chuyển dòng thành chữ hoa và chữ thường rồi in ra màn hình
print("\nDòng văn bản đã nhập:")
for i in van_ban:
    print(i.upper())