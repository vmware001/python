import random
import math
pi=math.pi

def generateRandomLine():
    angle1 = random.random() * 2 * pi
    x1 = math.cos(angle1)
    y1 = math.sin(angle1)
    angle2 = random.random() * 2 * pi
    x2 = math.cos(angle2)
    y2 = math.sin(angle2)
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    return (A, B, C)


def calcIntersection(line1, line2):
    A1, B1, C1 = line1
    A2, B2, C2 = line2

    if A1 * B2 - A2 * B1 == 0:
        return None

    x = (B1 * C2 - B2 * C1) / (A1 * B2 - A2 * B1)
    y = (A2 * C1 - A1 * C2) / (A1 * B2 - A2 * B1)
    return (x, y)


def isIntersectionInCircle(pos):
    x, y = pos
    if x ** 2 + y ** 2 <= 1:
        return 1
    return 0


def simulationOnce(lineCount=3):
    line = []
    for i in range(lineCount):
        line.append(generateRandomLine())
    intersectionCount = 0
    for i in range(lineCount):
        for j in range(i + 1, lineCount):
            intersectionCount += isIntersectionInCircle(calcIntersection(line[i], line[j]))

    return intersectionCount

def main():
    simulationCount=1000000
    sum=0
    for i in range(0,simulationCount):
        sum+=simulationOnce(5)
    print(sum/simulationCount+4)

main()