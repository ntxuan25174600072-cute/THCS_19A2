<<<<<<< HEAD
def so_doi_xung(n):
    n_str = str(n)           
    return n_str == n_str[::-1]   


print(so_doi_xung(121))   
print(so_doi_xung(353))   
print(so_doi_xung(123)) 
=======
n = int(input("Nhập n: "))
S1 = sum(range(1, n + 1))
print(S1)

S2 = 1
for i in range(1, n):
    S2 *= i
print(S2)

S3 = 0
for i in range(1, n + 1):
    S3 += ((-1)**(i + 1)) / i
print(S3)

S4 = 0
for k in range(n + 1):
    S4 += k / (k + 2)
print(S4)
>>>>>>> b44e0059a0d7d3b701bbe32ea267550344fd4b60
