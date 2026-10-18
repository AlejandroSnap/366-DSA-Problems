#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;
int main() {
    string s;
    while(cin >> s) {
        s[0] = toupper(s[0]);
        cout << s << endl;
    }

    return 0;
}