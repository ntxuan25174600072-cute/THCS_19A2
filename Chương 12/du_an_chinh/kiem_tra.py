import sys
sys.path.append("../thu_vien_chung")

import xu_ly_so

so = 7
if xu_ly_so.kiem_tra_so_nguyen_to(so):
    print(so, "là số nguyên tố")
else:
    print(so, "không phải số nguyên tố")
