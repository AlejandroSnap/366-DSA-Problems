def maxSubArray(nums):
    ans = best = nums[0]

    for i in range(1, len(nums)):
        best = max(best + nums[i], nums[i])
        ans = max(best, ans)
    return ans

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))

main()