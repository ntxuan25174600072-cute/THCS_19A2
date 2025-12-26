def nhan_ma_tran(A, B):
    rows_A = len(A)
    if rows_A == 0:
        return []
    cols_A = len(A[0])
    rows_B = len(B)
    if rows_B == 0:
        return []
    cols_B = len(B[0])
    C = []
    for i in range(rows_A):
        hang_moi = []
        for j in range(cols_B):
            hang_moi.append(0) 
        C.append(hang_moi)
    for i in range(rows_A):
        for j in range(cols_B):
            tong_tich = 0
            for k in range(cols_A): 
                tich = A[i][k] * B[k][j]
                tong_tich = tong_tich + tich

            C[i][j] = tong_tich

    return C

# Ví dụ

A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
ket_qua = nhan_ma_tran(A, B)
if ket_qua is not None:
    print("--- MA TRẬN A ---")
    for row in A:
        print(row)
    print("\n--- MA TRẬN B ---")
    for row in B:
        print(row)   
    print("\n--- KẾT QUẢ A * B ---")
    for row in ket_qua:
        print(row)