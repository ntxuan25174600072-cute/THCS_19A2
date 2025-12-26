def tim_key_max_toi_gian(D):
    if not D:
        return None, None
    k_max = None  
    v_max = None  
    for k in D:
        v = D[k]
        if k_max is None:
            v_max = v
            k_max = k
        elif v > v_max:
            v_max = v
            k_max = k

    return k_max, v_max
# Ví dụ
diem_so = {
    "A": 18,
    "B": 36,
    "C": 67,
    "D": 80, 
    "E": 79
}
key, value = tim_key_max_toi_gian(diem_so)
print(f"Dictionary: {diem_so}")
print(f"Key có giá trị lớn nhất: '{key}' (Giá trị: {value})")
