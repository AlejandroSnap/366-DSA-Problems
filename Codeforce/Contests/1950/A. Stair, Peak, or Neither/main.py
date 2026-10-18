from sys import stdin

def main():
    t = int(stdin.readline())

    for _ in range(t):
        a, b, c = list(map(int, stdin.readline().split()))
        if(a < b < c):
            print("STAIR")
        elif(a < b > c):
            print("PEAK")
        else:
            print("NONE")

main()