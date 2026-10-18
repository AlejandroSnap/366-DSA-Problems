from sys import stdin, setrecursionlimit

setrecursionlimit(9999)

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []

    def backtrack(p, aux):
        if p == len(nums):
            ans.append(aux.copy())
        else:
            s = set()
            for i in range(p, len(nums)):
                aux.append(nums[i])
                backtrack(i + 1, aux)
                aux.pop()

    backtrack(0, [])

    return ans


def main():
    nums = [1,2,3]

    print(permute(nums))

main()