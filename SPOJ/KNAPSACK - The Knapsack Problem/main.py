from sys import stdin

MAX = 2005
W = [None] * MAX
V = [None] * MAX

def solve(S, N):
    mem = {}
    def phi(n, x):
        key = (n, x)
        if key in mem:
            ans = mem[key]
        else:
            if n == 0 or x == 0:
                ans = 0
            elif W[n - 1] > x:
                ans = phi(n - 1, x)
            else:
                ans = max(V[n - 1] + phi(n - 1, x - W[n - 1]), phi(n - 1, x))
            mem[key] = ans

        return ans

    return phi(N, S)

def main():
    for line in stdin:
        S, N = list(map(int, line.split()))
        for i in range(N):  
            w, v = list(map(int, stdin.readline().split()))
            W[i] = w
            V[i] = v

        print(solve(S, N))

main()