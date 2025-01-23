from datetime import datetime
Luong = int(input("Hay nhap tien luong tinh theo gio: "))
dieukien = True
DanhSach = []

while dieukien:
    Data = input("Nhap theo dang GioVao - GioRa: ")
    if (Data != "0"):
        DanhSach.append(Data)
    else:
        dieukien = False

def TinhGio(GioVao, GioRa):
    Vao = datetime.strptime(GioVao, "%H:%M")
    Ra = datetime.strptime(GioRa, "%H:%M")
    TongGio = (Ra-Vao).seconds/3600
    return TongGio

TongTienLuong = 0

for Data in DanhSach:
    GioVao, GioRa = Data.split("-")
    GioVao = GioVao.strip()
    GioRa = GioRa.strip()
    GioLamViec = TinhGio(GioVao, GioRa)
    TongTienLuong += GioLamViec * Luong

print(f"Tong tien luong cua ban la: {TongTienLuong:,.0f} VND")
