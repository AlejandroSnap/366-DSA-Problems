#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main() {
    long long n, k;

    while(cin >> n >> k) {    
        long long odd = (n + 1) / 2;    
        if(k <= odd) {
            cout << 2*k - 1;
        } else {
            cout << 2*(k - odd);
        }

        cout << endl;
    }
    return 0;
}