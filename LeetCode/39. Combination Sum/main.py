from sys import setrecursionlimit

setrecursionlimit(9999)

def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def backtraking(p, aux, candidates, target, rest):
            if rest == 0:
                 ans.append(aux.copy())                
            else:
                for i in range(p, len(candidates)):
                    if rest - candidates[i] < 0:
                         continue
                    aux.append(candidates[i])
                    n = i if rest - candidates[i]  > 0 else i + 1

                    backtraking(n, aux, candidates, target, rest - candidates[i])
                    aux.pop()

        backtraking(0, [], candidates, target, target)

        return ans 

def main():
    candidates = [2,22,4,17,28,13,39,27,24,37,12,30,5,23,29,8,16,34,15,36,14,10,31]
    target = 30

    print(combinationSum(candidates, target))


main()