def elevatorRequests(n: int, requests: list[int]) -> int:
    ans = 0
    actual = 0

    for floor in requests:
        secs = abs(actual - floor)
        if secs > 0:
            ans += secs
            actual = floor

    return ans

def main():
    n = 3 
    requests = [2,0,0]

    print(elevatorRequests(n, requests))

main()