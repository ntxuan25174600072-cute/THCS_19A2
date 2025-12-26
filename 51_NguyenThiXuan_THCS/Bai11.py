def kiem_tra_doi_xung(ma_tran):
    so_hang = len(ma_tran)
    if so_hang == 0:
        return True 
    so_cot = len(ma_tran[0])
    if so_hang != so_cot:
        return False
    N = so_hang 
    for i in range(N):
        for j in range(i + 1, N):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True
# Ví dụ
ma_tran_doi_xung = [
    [1, 2, 3],
    [2, 5, 8],
    [3, 8, 9]
]

ma_tran_khong_dx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ma_tran_khong_vuong = [
    [1, 2],
    [3, 4],
    [5, 6]
]

ket_qua_1 = kiem_tra_doi_xung(ma_tran_doi_xung)
print(f"Kết quả: {ket_qua_1}")

ket_qua_2 = kiem_tra_doi_xung(ma_tran_khong_dx)
print(f"Kết quả: {ket_qua_2}")

ket_qua_3 = kiem_tra_doi_xung(ma_tran_khong_vuong)
print(f"Kết quả: {ket_qua_3}")