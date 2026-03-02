#include <bits/stdc++.h>
using namespace std;

long long factorial(int n) {
    if (n < 0) return -1;
    long long fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int main() {
    int choice;
    double x, y, result;

    while (true) {
        cout << "\n--- Scientific Calculator ---\n";
        cout << "1. Square Root\n";
        cout << "2. Factorial\n";
        cout << "3. Natural Log (ln)\n";
        cout << "4. Power (x^y)\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {

            case 1: {
                cout << "Enter number: ";
                cin >> x;

                if (x < 0) {
                    cout << "Error! Square root is undefined for negative numbers.\n";
                } else {
                    result = sqrt(x);
                    cout << "Result: " << result << endl;
                }
                break;
            }

            case 2: {
                int n;
                cout << "Enter a non-negative integer: ";
                cin >> n;

                if (n < 0) {
                    cout << "Error! Factorial is defined only for non-negative integers.\n";
                } else {
                    long long fact = factorial(n);
                    cout << "Result: " << fact << endl;
                }
                break;
            }

            case 3: {
                cout << "Enter number: ";
                cin >> x;

                if (x <= 0) {
                    cout << "Error! Natural log is defined only for positive numbers.\n";
                } else {
                    result = log(x);
                    cout << "Result: " << result << endl;
                }
                break;
            }

            case 4: {
                cout << "Enter base: ";
                cin >> x;
                cout << "Enter exponent: ";
                cin >> y;

                if (x == 0 && y == 0) {
                    cout << "Error! 0^0 is undefined.\n";
                } else {
                    result = pow(x, y);
                    cout << "Result: " << result << endl;
                }
                break;
            }

            case 5: {
                cout << "Exiting...\n";
                return 0;
            }

            default:
                cout << "Invalid choice! Please try again.\n";
        }
    }
}