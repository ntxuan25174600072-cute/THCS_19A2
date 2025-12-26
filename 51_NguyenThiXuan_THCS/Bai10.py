def tim_hang_tong_lon_nhat(ma_tran):
    if not ma_tran:
        return -1, 0  
    chi_so_hang_max = -1
    tong_lon_nhat = None
    i = 0
    for hang in ma_tran:
        tong_hien_tai = 0
        for phan_tu in hang:
            tong_hien_tai = tong_hien_tai + phan_tu
        if chi_so_hang_max == -1:
            tong_lon_nhat = tong_hien_tai
            chi_so_hang_max = i
        else:
            if tong_hien_tai > tong_lon_nhat:
                tong_lon_nhat = tong_hien_tai
                chi_so_hang_max = i

        i = i + 1 

    return chi_so_hang_max, tong_lon_nhat

# Ví dụ
ma_tran= [
    [10, 5, 20, 1],
    [2, 30, 4, 15],  
    [1, 1, 1, 1],    
    [5, 10, 15, 10]  
]

chi_so, tong_max = tim_hang_tong_lon_nhat(ma_tran)
print("--- MA TRẬN ĐẦU VÀO ---")
for row in ma_tran:
    print(row)
print("\n--- KẾT QUẢ ---")
if chi_so != -1:
    print(f"Tổng lớn nhất: {tong_max}")
    print(f"Chỉ số hàng (tính từ 0): {chi_so}")
    print(f"Hàng có tổng lớn nhất: {ma_tran[chi_so]}")
else:
    print("Ma trận rỗng.")