from sys import stdin, setrecursionlimit
from collections import deque


setrecursionlimit(9999)

def solve(G, N):
    ans = False
    visited = [-1 for _ in range(N + 1)]

    for i in range(1, N + 1):
        if visited[i] == -1:
            visited[i] = 0
            q = deque([i])

            while len(q) > 0 and not ans:
                u = q.popleft()

                for v in G[u]:
                    if visited[v] == -1:
                        visited[v] = 1 - visited[u]
                        q.append(v)

                    elif visited[v] == visited[u]:
                        ans = True

    return ans


def main():
    T = int(stdin.readline())

    for i in range(T):
        N, M = map(int, stdin.readline().split())

        G = [[] for _ in range(N + 1)]

        for _ in range(M):
            u, v = map(int, stdin.readline().split())

            G[u].append(v)
            G[v].append(u)

        ans = "Suspicious bugs found!" if solve(G, N) else "No suspicious bugs found!"

        print(f"Scenario #{i + 1}:")
        print(ans)


main()