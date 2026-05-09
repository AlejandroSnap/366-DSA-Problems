#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve(string &s) {
    string subS = "";
    int i;
    
    while(i < s.size()) {
        if(s[i] == '.' && subS.size() == 0) {
            cout << "0";
        } else {
            subS.push_back(s[i]);
            if(subS.size() == 2) {
                if(subS == "-.") {
                    cout << "1";
                } else {
                    cout << "2";
                }
                
                subS = "";
            }
        }
        
        i++;
    }
    
    cout << endl;
}

int main() {
    string s;
    while(cin >> s) {
        solve(s);
    }

    return 0;
}