def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []

    def backtracking(p, aux):
        for i in range(p, len(nums)):
            aux.append(nums[i])
            backtracking(i + 1, aux)
            aux.pop()

        if p <= len(nums):
            ans.append(list(aux))

    backtracking(0, [])

    return ans

def main():
    nums = [0]
    print(subsets(nums))

main()