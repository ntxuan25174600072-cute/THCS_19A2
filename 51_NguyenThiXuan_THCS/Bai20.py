def loc_dict_toi_gian(D, nguong):
    D_loc = {} 
    for k in D:
        v = D[k] 
        if v > nguong:
            D_loc[k] = v

    return D_loc
# Ví dụ-
ton_kho = {
    "A": 52,
    "B": 32,
    "C": 60,
    "D": 35,
    "E": 95
}
a = 50 
ket_qua = loc_dict_toi_gian(ton_kho, a)
print(f"Ngưỡng: {a}")
print(f"Lọc: {ket_qua}")