import random
import math
pi=math.pi

def randomDotsDistance():
    return math.sqrt(1+1-2*1*1*math.cos(random.random()*2*pi))

def calcAverageDistance(count=100000000):
    sum=0
    for i in range(0,count):
        sum+=randomDotsDistance()
    return sum/count

print(calcAverageDistance())
print(4/pi)
