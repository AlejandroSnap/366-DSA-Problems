#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void dfsAux(int u, vector<vector<int>> &edges, vector<bool> &visited, int destination, bool &ans) {
    int i;
    visited[u] = true;
    for(i = 0; i < edges[u].size() && !ans; i++) {
        int v = edges[u][i];
        if(!visited[v]) {
            if(v == destination) {
                ans = true;
            } else {
                dfsAux(v, edges, visited, destination, ans);
            }
        }
    }
}

bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
    bool ans = false;
    if(source == destination) {
        ans = true;
    } else {
        vector<bool> visited(n, false);
        vector<vector<int>> adj(n);
        int i;
        for(i = 0; i < edges.size(); i++) {
            int u = edges[i][0];
            int v = edges[i][1];

            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        dfsAux(source, adj, visited, destination, ans);
    }

    return ans;
}

int main() {
    int n = 6, source = 0, destination = 5;
    vector<vector<int>> edges = {{0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3}};
    vector<vector<int>> adj(n);

    cout << validPath(n, edges, source, destination);
    return 0;
}