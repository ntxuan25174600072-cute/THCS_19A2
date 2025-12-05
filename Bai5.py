def so_doi_xung(n):
    n_str = str(n)           
    return n_str == n_str[::-1]   


print(so_doi_xung(121))   
print(so_doi_xung(353))   
print(so_doi_xung(123)) 