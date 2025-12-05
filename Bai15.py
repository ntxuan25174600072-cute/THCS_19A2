def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_trong_khoang():
    for n in range(100, 501):
        if la_so_nguyen_to(n):
            print(n)
