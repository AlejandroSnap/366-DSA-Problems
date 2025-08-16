def hasSameDigits(s: str) -> bool:
    ans = False
    while len(s) > 2:
        i = 0
        temp = ""
        while i < len(s) - 1:
            temp = temp + str((int(s[i]) + int(s[i + 1])) % 10)
            i += 1

        s = str(temp)

        if len(s) <= 2:
            if s[0] == s[1]:
                ans = True

    return ans
