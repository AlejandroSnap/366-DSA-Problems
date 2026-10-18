#include <iostream>

using namespace std;

int main() {
    int n;
    while(cin >> n) {
        int p = 0;
        for(int i = 0; i < n; i++) {
            int acc = 0;
            for(int j = 0; j < 3; j++) {
                int num;
                cin >> num;

                acc += num;
            }

            if(acc > 1) {
                p++;
            }
        }

        cout << p << endl;
    }
    return 0;
}