#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;

        vector<vector<int>> G(N, vector<int>());
        while(M--){
            int u, v;
            cin >> u >> v;
            
            G[u].push_back(v);
        }

    }
    return 0;
}