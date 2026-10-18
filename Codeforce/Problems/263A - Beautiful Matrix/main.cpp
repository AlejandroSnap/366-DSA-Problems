#include <iostream>
#include <vector>

using namespace std;

int main() {
    int aux;
    int i, j;
    bool flag = false;
    while(cin >> aux) {
        int a = 1, b = 1;
            for(i = 1; i <= 5; i++) {
                j = 1;
                if(i == 1) {
                    j = 2;
                }

                for(j; j <= 5; j++) {
                    cin >> aux;
                    if(aux) {
                        a = i, b = j;
                    }
                }
            }

        cout << abs(a - 3) + abs(b - 3) << endl;

    }
    return 0;
}