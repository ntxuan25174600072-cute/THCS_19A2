def nhom_diem_toi_gian(D_goc):
    D_nhom = {} 
    for ten in D_goc:
        diem = D_goc[ten] 
        if diem in D_nhom:
            D_nhom[diem].append(ten) 
        else:
            D_nhom[diem] = [ten]
    return D_nhom

# Ví dụ
ket_qua = {
    "Nhat": 9.5,
    "Quyen": 8.0,
    "Linh": 9.5,
    "Khiem": 7.0,
    "Huy": 8.0   
}
D_nhom = nhom_diem_toi_gian(ket_qua)
print(f"Gốc: {ket_qua}")
print(f"Nhóm: {D_nhom}")