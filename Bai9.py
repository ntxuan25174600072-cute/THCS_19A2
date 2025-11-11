
so_kwh = int(input("Nhập số kWh đã tiêu thụ: "))

bac1 = min(so_kwh, 100)
bac2 = max(min(so_kwh - 100, 100), 0)
bac3 = max(so_kwh - 200, 0)

tien = bac1 * 1678 + bac2 * 1734 + bac3 * 2014

print("Tổng số tiền điện phải trả là:", tien, "VNĐ")
