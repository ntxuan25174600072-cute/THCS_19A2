def tinh_tong_duong_cheo_phu(ma_tran):
    tong_duong_cheo = 0
    n = len(ma_tran) 
    if n == 0:
        return 0
    for i in range(n):
        j = n - 1 - i
        phan_tu = ma_tran[i][j]
        tong_duong_cheo = tong_duong_cheo + phan_tu
    return tong_duong_cheo
ma_tran_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ma_tran_B = [
    [10, 20, 30, 40],
    [11, 22, 33, 44],
    [12, 24, 36, 48],
    [13, 26, 39, 52]
]

tong_A = tinh_tong_duong_cheo_phu(ma_tran_A)
tong_B = tinh_tong_duong_cheo_phu(ma_tran_B)

print(f"Tổng đường chéo phụ: {tong_A}")

print(f"Tổng đường chéo phụ: {tong_B}")