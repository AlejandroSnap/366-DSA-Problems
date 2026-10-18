#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        
        int i;
        for(i = 0; i < n; i++) {
            int j;
            string s = "";
            for(j = 0; j < n; j++) {
                if((i + j) % 2 == 0) {
                    s += "##";
                } else {
                    s += "..";
                }

            }
            cout << s << endl << s << endl;
        }

    }
    return 0;
}