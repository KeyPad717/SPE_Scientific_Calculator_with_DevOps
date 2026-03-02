#include <bits/stdc++.h>
using namespace std;

long double factorial(int n) {
    long double fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
        if (isinf(fact)) {
            cout << "Error! Factorial result too large.\n";
            return -1;
        }
    }
    return fact;
}

void showUsage() {
    cout << "Usage:\n";
    cout << "./a.out <operation> [arguments]\n\n";

    cout << "Operations:\n";
    cout << "sqrt x       -> Square root of x\n";
    cout << "fact n       -> Factorial of n\n";
    cout << "ln x         -> Natural log of x\n";
    cout << "pow x y      -> Power x^y\n\n";

    cout << "Examples:\n";
    cout << "./a.out sqrt 49\n";
    cout << "./a.out fact 6\n";
    cout << "./a.out ln 4\n";
    cout << "./a.out pow 4 2\n";
}

void invalidArgs(string op) {
    cout << "Invalid arguments for operation: " << op << "\n\n";
    showUsage();
}

int main(int argc, char* argv[]) {

    if (argc < 2) {
        cout << "Error! No operation provided.\n\n";
        showUsage();
        return 0;
    }

    string op = argv[1];

    if (op == "sqrt") {
        if (argc != 3) {
            invalidArgs("sqrt (requires 1 argument)");
            return 0;
        }

        long double x;
        try { x = stold(argv[2]); }
        catch (...) {
            cout << "Error! Invalid input type.\n";
            return 0;
        }

        if (x < 0) {
            cout << "Error! Square root undefined for negative numbers.\n";
            return 0;
        }

        cout << sqrt(x) << endl;
    }

    else if (op == "fact") {
        if (argc != 3) {
            invalidArgs("fact (requires 1 integer argument)");
            return 0;
        }

        int n;
        try { n = stoi(argv[2]); }
        catch (...) {
            cout << "Error! Invalid input type.\n";
            return 0;
        }

        if (n < 0) {
            cout << "Error! Factorial defined only for non-negative integers.\n";
            return 0;
        }

        long double result = factorial(n);
        if (result == -1) return 0;

        cout << result << endl;
    }

    else if (op == "ln") {
        if (argc != 3) {
            invalidArgs("ln (requires 1 positive argument)");
            return 0;
        }

        long double x;
        try { x = stold(argv[2]); }
        catch (...) {
            cout << "Error! Invalid input type.\n";
            return 0;
        }

        if (x <= 0) {
            cout << "Error! ln(x) defined for x > 0.\n";
            return 0;
        }

        cout << log(x) << endl;
    }

    else if (op == "pow") {
        if (argc != 4) {
            invalidArgs("pow (requires 2 arguments)");
            return 0;
        }

        long double x, y;
        try {
            x = stold(argv[2]);
            y = stold(argv[3]);
        } catch (...) {
            cout << "Error! Invalid input type.\n";
            return 0;
        }

        if (x == 0 && y == 0) {
            cout << "Error! 0^0 is undefined.\n";
            return 0;
        }

        long double result = pow(x, y);

        if (isinf(result)) {
            cout << "Error! Result too large.\n";
            return 0;
        }

        cout << result << endl;
    }

    else {
        cout << "Error! Unknown operation.\n\n";
        showUsage();
    }

    return 0;
}