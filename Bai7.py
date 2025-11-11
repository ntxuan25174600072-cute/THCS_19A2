username = input("Nhập tên đăng nhập: ")
password = input("Nhập mật khẩu: ")

condition = (username == "admin") and (password != "password123")

result = ["Đăng nhập thất bại. Không được cấp quyền truy cập.",
          "Đăng nhập thành công. Quyền truy cập được cấp."]

print(result[condition])  
