#include <iostream>
using namespace std;

long long faktorijel(int n) {
    long faktorijel = 1.0;
    if (n < 0)
        cout << "Error";
    else {
        for (int i = 1; i <= n; ++i) {
            faktorijel *= i;
        }
        return faktorijel;
    }
}

int main() {

    int n;
    int a;
    int b;
    int c;
    
    for (n = 1; n < 21; n++) {                                                                                // 21! je vece od  2^64-1
        long long faktorijel_N = faktorijel(n);
        int max_abc = floor(pow(faktorijel_N, 1.0 / (n - 1)));                                                //velicina inta

        for (a = 1; a <= max_abc; a++) 
        {
            for (b = 1; b <= max_abc; b++) 
            {
                for (c = 1; c <= max_abc; c++) 
                {
                    int vrednost = faktorijel_N * 1.0;
                    if (pow(a, n - 1) + pow(b, n - 1) + pow(c, n - 1) == vrednost) {
                        cout << "n=" << n << " a=" << a << " b=" << b << " c=" << c;
                        cout << "\n";
                    }
                }
            }
        }
    }

    return 0;
}