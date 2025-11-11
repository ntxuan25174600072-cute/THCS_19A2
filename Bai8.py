
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

bmi = can_nang / (chieu_cao * chieu_cao)

print("Chỉ số BMI của bạn là:", round(bmi, 2))
