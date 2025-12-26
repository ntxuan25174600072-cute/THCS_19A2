def phep_toan_set_toi_gian(A, B):
    A_khong_B = []
    B_khong_A = []
    A_giao_B = []
    A_hop_B = []
    for p_A in A:
        co_trong_B = False
        for p_B in B:
            if p_A == p_B:
                co_trong_B = True
                break

        if co_trong_B:
            A_giao_B.append(p_A)
            A_hop_B.append(p_A) 
        else:
            A_khong_B.append(p_A)
            A_hop_B.append(p_A)

    for p_B in B:
        co_trong_A = False
        for p_giao in A_giao_B:
            if p_B == p_giao:
                co_trong_A = True
                break
        if not co_trong_A:
            B_khong_A.append(p_B)
            A_hop_B.append(p_B) # Góp vào Hợp

    return A_khong_B, B_khong_A, A_giao_B, A_hop_B

# Ví dụ 
A = [1, 2, 3, 4, 5, 6, 7]
B = [5, 6, 7, 8, 9, 10]

A_hieu_B, B_hieu_A, Giao, Hop = phep_toan_set_toi_gian(A, B)

print(f"A: {A}, B: {B}")
print(f"Hiệu A: {A_hieu_B}")
print(f"Hiệu B: {B_hieu_A}")
print(f"Giao: {Giao}")
print(f"Hợp: {Hop}")
