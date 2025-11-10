tien = float(input("Nhập số tiền gửi ban đầu: "))
lai_suat = float(input("Nhập lãi suất hàng năm (%): "))
lai_suat /= 100
lai_1_thang = tien * lai_suat / 12
lai_2_quy = tien * lai_suat / 2
lai_3_nam = tien * lai_suat * 3
print("Lãi sau 1 tháng:", round(lai_1_thang, 2))
print("Lãi sau 2 quý:", round(lai_2_quy, 2))
print("Lãi sau 3 năm:", round(lai_3_nam, 2))