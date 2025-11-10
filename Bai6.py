#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Nhap nam: ";
    cin >> year;

    // Kiểm tra năm nhuận
    if (year % 400 == 0) {
        cout << year << " la nam nhuan." << endl;
    }
    if (year % 4 == 0 && year % 100 != 0) {
        cout << year << " la nam nhuan." << endl;
    }
    if (year % 400 != 0 && !(year % 4 == 0 && year % 100 != 0)) {
        cout << year << " khong phai nam nhuan." << endl;
    }

    return 0;
}

