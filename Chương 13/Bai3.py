ds = [1, 3, 5, 7, 9]

f = open("so_nguyen.txt", "w", encoding="utf-8")

for so in ds:
    f.write(str(so) + "\n")

f.close()

print("Đã ghi xong file so_nguyen.txt")
