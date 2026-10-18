from collections import deque

def canReach(start: list[int], target: list[int]) -> bool:
    directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

    q = deque([start])
    dist = {tuple(start): 0}

    tt = tuple(target)

    while len(q) > 0:
        x, y = q.popleft() 

        if(tt in dist):
            return dist[tt] % 2 == 0

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            np = (nx, ny)

            if(0 <= nx < 8 and 0 <= ny < 8):
                if np not in dist:
                    dist[np] = dist[(x, y)] + 1
                    q.append(np)


    return False

def main():
    start = [1,1]
    target = [2,2]

    print(canReach(start, target))

main()