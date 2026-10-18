#include <iostream>
#include <queue>

using namespace std;

int main() {
    int n, m;
    while(cin >> n >> m) {
        int i;
        int candies[n + 1];
        queue<int> q;

        for(i = 1; i <= n; i++) {
            int c;
            cin >> c;
            q.push(i);
            candies[i] = c;
        }

        while(q.size() > 1) {
            int p = q.front();
            int &c = candies[p];

            q.pop();
            c -= m;

            if(c > 0) {
                q.push(p);
            }
        }

        cout << q.front() << endl;; 
    }

    return 0;
}