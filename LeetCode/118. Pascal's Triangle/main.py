def generate(numRows: int):
    if numRows == 0:
        return []
    
    ans = [[1]]

    i = len(ans)
    while i < numRows:
        j, aux = 0, [1]

        while j < i - 1:
            aux.append(ans[i - 1][j] + ans[i - 1][j + 1])
            j += 1

        aux.append(1)
        ans.append(aux)
        i += 1
    return ans
    