def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    tmp = []
    for i in range(m):
        tmp.append(nums1[i])

    for i in range(n):
        tmp.append(nums2[i])

    l = 0
    r = m
    for i in range(m + n):
        if l == m:
            nums1[i] = tmp[r]
            r += 1
        elif r == n + m:
            nums1[i] = tmp[l]
            l += 1
        else:
            if tmp[l] >= tmp[r]:
                nums1[i], r = tmp[r], r + 1
            else:
                nums1[i], l = tmp[l], l + 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))
print(nums1)