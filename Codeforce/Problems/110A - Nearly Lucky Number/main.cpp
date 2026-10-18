#include <iostream>

using namespace std;

int main() {
    string num;
    while(cin >> num) {
        int lucky = 0;
        for(char &c: num){
            int d = c - '0';
            if(d == 7 || d == 4) {
                lucky++;
            }
        }

        if(lucky == 4 || lucky == 7) {
            cout << "YES";
        } else {
            cout << "NO";
        }

        cout << endl;
    }

    return 0;
}