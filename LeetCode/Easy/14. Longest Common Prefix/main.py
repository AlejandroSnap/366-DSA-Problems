def longestCommonPrefix(strs: list[str]) -> str:
    ans, i = "", 0
    shortest = min(strs, key=len)
    match = True
    while i < len(shortest) and match:
        k = 0
        count = 0
        while k < len(strs) and match:
            if strs[k][i] != shortest[i]:
                match = False
            else:
                count += 1

            if count == len(strs):
                ans += strs[k][i]
            k += 1
        i += 1
    return ans

cases = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
    [""],
    ["a"],
    ["ab", "a"],
    ["cir","car"]
]

for case in cases:
    print(longestCommonPrefix(case))