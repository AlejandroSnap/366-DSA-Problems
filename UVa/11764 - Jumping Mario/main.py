from sys import stdin

def main():
    for t in range(int(stdin.readline().strip())):
        n = int(stdin.readline())
        jumps = [int(x) for x in stdin.readline().split()]

        high_jump = 0
        low_jump = 0

        for i in range(n - 1):
            if jumps[i] < jumps[i + 1]:
                high_jump += 1
            elif jumps[i] > jumps[i + 1]:
                low_jump += 1

        print(f"Case {t + 1}: {high_jump} {low_jump}")
main()