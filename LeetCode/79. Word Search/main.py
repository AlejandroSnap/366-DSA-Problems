def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    m, n = len(board), len(board[0])

    def backtrack(i, j, actual):
        ans = False
        if len(word) == actual:
            ans = True
        else:
            if 0 <= i < m and 0 <= j < n:
                char = board[i][j]
                isCorrect = board[i][j] == word[actual]

                if isCorrect:
                    board[i][j] = "#"       
                    if backtrack(i + 1, j, actual + 1) or backtrack(i, j + 1, actual + 1) or backtrack(i - 1, j, actual + 1) or backtrack(i, j - 1, actual + 1):
                        ans = True
                    else:
                        board[i][j] = char

        return ans

    r = 0
    ans = False
    while r < len(board) and ans == False:
        c = 0
        while c < len(board[0]) and ans == False:
            if board[r][c] == word[0]:
                ans = backtrack(r, c, 0)
            c += 1
        r += 1

    return ans

def main():
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "SEE"

    print(exist(board, word))

main()