def isMiddleElementUnique(nums: list[int]) -> bool:
    ans = True
    n = len(nums)
    middle = nums[n // 2]

    i = 0
    while i < n // 2 and ans:
        if nums[i] == middle or nums[n - 1 - i] == middle:
            ans = False
        i += 1

    return ans

def main():
    nums = [1,2,3]
    print(isMiddleElementUnique(nums))

    nums = [1,2,2]
    print(isMiddleElementUnique(nums))


main()