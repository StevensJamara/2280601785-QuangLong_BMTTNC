#Tạo 1 danh sách rỗng lưu kết quả
j=[]
#Duyệt tất cả các số trong đoạn từ 2000 - 3200 kiểm tra xem i chia hết cho 7 và không là bội số 5
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        j.append(str(i))
print(','.join(j))