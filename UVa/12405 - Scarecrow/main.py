from sys import stdin

def solve(A, N):
    def phi(n):
        if n > N:
            ans = 0
        elif A[n - 1] == '#':
            ans = phi(n + 1)
        else:
            ans = 1 + phi(n + 3)

        return ans

    return phi(1)

def main():
    T = int(stdin.readline())
    for t in range(T):
        N = int(stdin.readline())
        A = stdin.readline().strip()
        print(f"Case {t + 1}: {solve(A, N)}")



main()