def secondsBetweenTimes(startTime: str, endTime: str) -> int:
    return ((int(endTime[0:2]) * 60 * 60) + (int(endTime[3:5]) * 60) + int(endTime[6:8])) - (((int(startTime[0:2]) * 60 * 60) + (int(startTime[3:5]) * 60) + int(startTime[6:8])))

def main():
    startTime = "01:00:00"
    endTime = "01:00:25"

    print(secondsBetweenTimes(startTime, endTime))

main()