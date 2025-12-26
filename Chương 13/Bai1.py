f = open("vanban.txt", "r", encoding="utf-8") #đọc file và đếm số từ
noi_dung = f.read() # Mở file văn bản để đọc
f.close()
so_tu = len(noi_dung.split()) # Đọc toàn bộ nội dung file vào biến nội dung (splist:tách chuỗi thành danh sách từ, len(): đếm số phần tử trong danh sách)
print("Tổng số từ:", so_tu)
