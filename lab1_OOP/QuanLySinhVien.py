from SinhVien import SinhVien

class QuanLySinhVien:
    lstSinhVien = []

    def generateId(self):
        maxID = 1
        if (self.soLuongSinhVien() > 0):
            maxID = self.lstSinhVien[0]._id
            for sv in self.lstSinhVien:
                if (maxID < sv._id):
                    maxID = sv._id
                maxID += 1
        return maxID
    
    def soLuongSinhVien(self):
        return len(self.lstSinhVien.__len__())
    
    def nhapSinhVien(self):
        svID = self.generateId()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(svID, name, sẽ, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.lstSinhVien.append(sv)

    def updateSV(self, ID):
        sv: SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh sinh vien: ")
            diemTB = float(input("Nhap diem trung binh sinh vien: "))

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Khong tim thay sinh vien co ID: {}" .format(ID))

    def SortById(self):
        self.lstSinhVien.sort(key=lambda x: x._id, reverse=False)

    def SortByName(self):
        self.lstSinhVien.sort(key=lambda x: x._name, reverse=False)

    def SortByDiemTB(self):
        self.lstSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
    
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.lstSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult

    def findByName(self, name):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.lstSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.lstSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 7):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"

    def showSV(self, listSV):
        print(":{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
            .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("----------------------------------------------------------------\n")
