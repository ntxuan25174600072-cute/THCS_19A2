def dem_tan_suat_toi_gian(chuoi):
    ts = {} 
    for k in chuoi:
        if k == ' ':
            continue
        if k in ts:
            ts[k] = ts[k] + 1
        else:
            ts[k] = 1

    return ts

# Ví dụ
chuoi_mau = "Hello python" 
ket_qua = dem_tan_suat_toi_gian(chuoi_mau)
print(f"Chuỗi: '{chuoi_mau}'")
print(f"Tần suất: {ket_qua}")