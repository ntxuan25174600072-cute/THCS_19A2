year = int(input("Nhập năm: "))
result = ["Không phải năm nhuận", "Năm nhuận"]
is_leap = (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
print(result[is_leap])
