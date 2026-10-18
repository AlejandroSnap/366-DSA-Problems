def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    ans = []

    def backtracking(p, aux, act):
        # print(p, aux, act)
        if act == len(s):
            ans.append(list(aux))
        for i in range(p, len(s)):
            if s[i] == s[act]:
                aux.append(s[i])
                backtracking(i + 1, aux, act + 1)

    backtracking(0, [], 0)
    
    return ans

def main():
    for s in ["aab", "a"]:
        print(partition(s))

main()