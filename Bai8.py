def tim_so_le_lon_nhat(a, b, c):
    so_le = [x for x in [a, b, c] if x % 2 != 0]
    return max(so_le) if so_le else -1
