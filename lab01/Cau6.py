#Nhập 2 số x , y
input_str = input("Nhập 2 số x , y: ")
dimension = [int(i) for i in input_str.split(',')]
rouwNum = dimension[0]
columnNum = dimension[1]
#Tạo ma trận rouwNum x columnNum
multilist = [[0 for i in range(columnNum)] for j in range(rouwNum)]
for i in range(0, rouwNum):
    for j in range(0, columnNum):
        multilist[i][j] = i * j
print(multilist)