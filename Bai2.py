<<<<<<< HEAD
def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Vô số nghiệm"
        else:
            return "Vô nghiệm"
    else:
        x = -b / a
        return x
=======
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
while b != 0:
    a, b = b, a % b
print("UCLN")
>>>>>>> b44e0059a0d7d3b701bbe32ea267550344fd4b60
