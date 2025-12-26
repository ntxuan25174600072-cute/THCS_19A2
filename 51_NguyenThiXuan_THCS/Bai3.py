s = input("Nhập chuỗi: ")

ket_qua = ""
dang_space = False

for ch in s:
    if ch != " ":
        ket_qua += ch
        dang_space = False
    else:
        if not dang_space:
            ket_qua += " "
            dang_space = True

print(ket_qua)
