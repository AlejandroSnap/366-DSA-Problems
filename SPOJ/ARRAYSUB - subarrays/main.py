from sys import stdin

def solve(A, N, K):
    ans = []
    i = 0
    while i < N - K + 1:
        best = A[i]
        for j in range(i, i + K):
            best = max(best, A[j])
        ans.append(best)
        i += 1

    return ans


def main():
    for line in stdin:
        line = line.strip()
        N = int(line)
        A = list(map(int, stdin.readline().split()))
        K = int(stdin.readline())

        print(*solve(A, N, K))

main()