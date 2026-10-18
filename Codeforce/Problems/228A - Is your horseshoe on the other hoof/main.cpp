#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    int ans = 0;
    unordered_set<int> aux;
    for(int i = 0; i < 4; i++) {
        int si;
        cin >> si;

        if(aux.find(si) == aux.end()) {
            aux.insert(si);
        } else {
            ans++;
        }
    }

    cout << ans << endl;;

    return 0;
}