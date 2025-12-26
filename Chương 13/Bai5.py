with open("vanban.txt", "rb") as f_nguon:
    with open("ban_sao.txt", "wb") as f_dich:
        while True:
            data = f_nguon.read(1024)
            if not data:
                break
            f_dich.write(data)

print("Đã sao chép xong")
