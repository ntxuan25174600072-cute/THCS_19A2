def xu_ly_tuple_toi_gian(T):
    l1, l2 = [], []  
    so_chan, so_le = 0, 0    

    for so in T:
        if so % 2 == 0:
            l1.append(so)
            so_chan = so_chan + so
        else:
            l2.append(so)
            so_le = so_le + so
    tc = tuple(l1)
    tl = tuple(l2)
    return tc, so_chan, tl, so_le
# Ví dụ
T_goc = (1, 8, 3, 10, 5, 2, 7, 4, 9, 6)

t_chan, sum_chan, t_le, sum_le = xu_ly_tuple_toi_gian(T_goc)

print(f"Tuple gốc: {T_goc}")
print(f"Chẵn: {t_chan} (Tổng: {sum_chan})")
print(f"Lẻ: {t_le} (Tổng: {sum_le})")