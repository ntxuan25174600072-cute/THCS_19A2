s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))

tu = ""
for ch in s + " ":
    if ch != " ":
        tu += ch
    else:
        if len(tu) > n:
            print(tu)
        tu = ""


    