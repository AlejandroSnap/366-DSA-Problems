def climbStairs(n):
    if n <= 2:
        ans = n
    else:
        ans = climbStairs(n - 1) + climbStairs(n - 2)

    return ans


def solve(N):
    def phi(n, act):
        ans = 0
        if n == N:
            ans = act
        else:
            ans = max(phi(n + 1, act + 2), phi(n + 1, act))
        return ans

    return phi(0, 0)

for n in [1, 2, 3, 4]:
    print(climbStairs(n), solve(n))
