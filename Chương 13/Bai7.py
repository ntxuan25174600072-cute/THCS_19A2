import os

os.makedirs("thu_muc_test", exist_ok=True)

open("thu_muc_test/file1.txt", "w").close()
open("thu_muc_test/file2.txt", "w").close()

print(os.listdir("thu_muc_test"))
