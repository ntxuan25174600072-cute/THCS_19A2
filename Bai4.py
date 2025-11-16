n = int(input("Nhập n: "))
for i in range(2, n):
    la_ngto = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            la_ngto = False
            break
    if la_ngto:
        print(i)
