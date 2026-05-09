#include <iostream>
#include <vector>


using namespace std;

vector<int> findDegrees(vector<vector<int>>& matrix) {
    int n = matrix.size(), i, j;
    vector<int> ans(n, 0);
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            if(i != j) {
                if(matrix[i][j]) {
                    ans[i]++;
                }
            }
        }
    }

    return ans;
}

int main() {
    vector<vector<int>> matrix = {
        {0, 1, 1},
        {1, 0, 1},
        {1, 1, 0}
    };

    for(int num: findDegrees(matrix)) {
        cout << num << " ";
    }

    cout << endl;

    return 0;
}