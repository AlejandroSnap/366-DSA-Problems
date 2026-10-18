#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool dfs(int r, int c, vector<vector<char>> &board, string &word, int actual) {
    bool ans = false;
    if(word.size() == actual) {
        ans = true;
    } else {
        if(!(r < 0 || r >= board.size() || c < 0 || c >= board[0].size())) {
            char isCorrect = board[r][c] == word[actual];
            char chr = board[r][c];
            if(isCorrect) {
                board[r][c] = '#';

                if(dfs(r + 1, c, board, word, actual + 1) || dfs(r - 1, c, board, word, actual + 1) || dfs(r, c + 1, board, word, actual + 1) || dfs(r, c - 1, board, word, actual + 1)) {
                    ans = true;
                } else {
                    board[r][c] = chr;
                }
            }
        }
    }

    return ans;
}

bool exist(vector<vector<char>>& board, string &word) {       
    bool ans = false;

    int u;
    for(u = 0; u < board.size() && !ans; u++) {
        int v;
        for(v = 0; v < board[u].size() && !ans; v++) {
            if(board[u][v] == word[0]) {
                if(dfs(u, v, board, word, 0)) {
                    ans = true;
                }
            }
        }
    }

    return ans;
}

int main() {
    vector<vector<char>> board = {
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'}
    };

    string word = "ABCCED";
    cout << exist(board, word);
    return 0;
}