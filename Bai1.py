gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng: "))
tong_tien = gia * so_luong
vat = tong_tien * 0.1
tong_phai_tra = tong_tien + vat
print("Tổng tiền phải trả (đã gồm VAT):", round(tong_phai_tra, 2))