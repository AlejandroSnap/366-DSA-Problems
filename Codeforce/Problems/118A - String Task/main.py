from sys import stdin

def main():
    for s in stdin:
        s = s.strip()
        ans = ""

        for char in s:
            if char in ['A', 'O', 'Y', 'E', 'U', 'I'] or char in ['a', 'o', 'y', 'e', 'u', 'i']:
                continue
            else:
                ans += f".{char.lower()}"

        print(ans)

main()