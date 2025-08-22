def mySqrt(x: int) -> int:
    ans, i = 0, 0

    while i * i <= x:
        ans += 1
        i += 1
    return ans