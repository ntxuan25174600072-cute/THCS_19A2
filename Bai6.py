#la_so_nguyen_to
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#in_so_nguyen_to
def in_so_nguyen_to_trong_khoang(a, b):
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i)
