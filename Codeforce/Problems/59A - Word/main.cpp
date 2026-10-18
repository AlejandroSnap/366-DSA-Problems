#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

int main() {
    string s;
    while(cin >> s) {
        int l = 0, u = 0;
        for(char c: s) {
            if(islower(c)) {
                l++;
            } else {
                u++;
            }
        }

        for(char &c: s) {
            if(l == u || l > u) {
                c = tolower(c);
            } else {
                c = toupper(c);
            }
        }
        
        cout << s << endl;
    }
    return 0;
}