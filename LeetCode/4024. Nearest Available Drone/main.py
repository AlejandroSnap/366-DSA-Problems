def nearestDrone(drones: list[list[int]], target: list[int]) -> int:
    ans = -1
    distance = None

    xj, yj = target

    for i in range(len(drones)):
        drone = drones[i]
        xi, yi, r = drone

        result = abs(xi - xj) + abs(yi - yj)
        if(result <= r):
            if distance == None or result < distance:
                distance = result   
                ans = i

            elif distance == result and i < ans:
                ans = i
                distance = result
    return ans


def main():
    drones = [[-18,4,10],[-16,23,29],[18,21,87],[0,10,47],[-20,25,51],[-25,-9,69]]
    target = [-18,4]

    print(nearestDrone(drones, target))

main()