def chia_hai_so():
    try:
        a = int(input("Nhập số thứ nhất: "))
        b = int(input("Nhập số thứ hai: "))
        ket_qua = a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0.")
    except ValueError:
        print("Lỗi: Vui lòng nhập vào số nguyên.")
    else:
        print("Thương của hai số là:", ket_qua)
    finally:
        print("Kết thúc chương trình.")

chia_hai_so()
