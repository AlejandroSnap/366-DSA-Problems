#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

int main() {
    string s1, s2;
    while(cin >> s1 >> s2) {
        for(char &c: s1) {
            c = tolower(c);
        }

        for(char &c: s2) {
            c = tolower(c);
        }

        if(s1 < s2) {
            cout << "-1";
        } else if(s2 < s1) {
            cout << "1";
        } else {
            cout << "0";
        }

        cout << endl;
    }
    return 0;
}