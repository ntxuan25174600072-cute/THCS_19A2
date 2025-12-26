import csv

with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Ten", "Luong"])
    writer.writerow([1, "An", 60000])
    writer.writerow([2, "Binh", 45000])
    writer.writerow([3, "Cuong", 80000])

with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["Luong"]) > 50000:
            print(row["Ten"], "-", row["Luong"])
