def kiem_tra_don_vi_toi_gian(A):
    N = len(A)
    if N == 0:
        return False
    if N != len(A[0]):
        return False
    for i in range(N):
        for j in range(N):
            phan_tu = A[i][j]
            if i == j:
                if phan_tu != 1: return False
            else:
                if phan_tu != 0: return False

    return True
I_3x3 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

M = [
    [1, 0, 5], 
    [0, 1, 0],
    [0, 0, 1]
]

print(f"I_3x3 là đơn vị: {kiem_tra_don_vi_toi_gian(I_3x3)}")
print(f"M là đơn vị: {kiem_tra_don_vi_toi_gian(M)}")