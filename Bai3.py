tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
a, b = tu, mau
while b != 0:
    a, b = b, a % b
ucln = a
print("Phân số tối giản")
