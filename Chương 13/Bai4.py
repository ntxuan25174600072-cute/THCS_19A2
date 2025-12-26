id_can_sua = input("Nhập ID sản phẩm: ")
gia_moi = input("Nhập giá mới: ")

f = open("san_pham.txt", "r", encoding="utf-8")
cac_dong = f.readlines()
f.close()

dong_moi = []

for dong in cac_dong:
    if dong.startswith(id_can_sua + ","):
        parts = dong.strip().split(",")
        parts[2] = gia_moi
        dong_moi.append(",".join(parts) + "\n")
    else:
        dong_moi.append(dong)

f = open("san_pham.txt", "w", encoding="utf-8")
f.writelines(dong_moi)
f.close()

print("Đã cập nhật xong")
