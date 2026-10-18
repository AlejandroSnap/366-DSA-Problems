def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    ans = []
    aux = {}

    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if num in aux:
            return [i, aux[num]]
        else:
            aux[diff] = i

    return ans

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))