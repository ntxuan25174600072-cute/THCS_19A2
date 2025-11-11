# Bài 10 - Tính lương không dùng if/else

luong_co_ban = float(input("Nhập mức lương cơ bản: "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))

luong_1_ngay = luong_co_ban / 22
luong = luong_1_ngay * so_ngay_cong

thuong = luong * 0.10 * (so_ngay_cong > 22)

phat = luong * 0.05 * (so_ngay_cong < 22)

luong_thuc_nhan = luong + thuong - phat

print("Lương thực nhận là:", round(luong_thuc_nhan, 2), "VNĐ")
