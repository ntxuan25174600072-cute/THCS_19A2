def dao_nguoc_dict_toi_gian(D):
    D_nguoc = {} 
    for k in D:
        v = D[k]
        D_nguoc[v] = k
    return D_nguoc

# Ví dụ
danh_ba = {
    "A": 5,
    "B": 19,
    "C": 8,
}
D_dao = dao_nguoc_dict_toi_gian(danh_ba)
print(f"Gốc: {danh_ba}")
print(f"Đảo ngược: {D_dao}")