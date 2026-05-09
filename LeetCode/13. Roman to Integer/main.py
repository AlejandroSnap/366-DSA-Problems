def romanToInt(s: str) -> int:
    ans = 0
    romans = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }

    i = 0
    while i < len(s):
        a, b = romans.get(s[i]), romans.get(s[i + 1]) if i + 1 < len(s) else 0
        if a < b:
            ans -= a
        else:
            ans += a
        i += 1
    return ans