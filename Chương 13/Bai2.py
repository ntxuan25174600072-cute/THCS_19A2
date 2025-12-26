f = open("vanban.txt", "r", encoding="utf-8")
noi_dung = f.read()
f.close()

cac_tu = noi_dung.split()
tan_suat = {}

for tu in cac_tu: # Tạo từ điển rỗng để lưu {từ:số lần}
    if tu in tan_suat:      #Duyệt từng từ trong danh sách
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

for tu, so_lan in tan_suat.items():
    print(tu, ":", so_lan)
