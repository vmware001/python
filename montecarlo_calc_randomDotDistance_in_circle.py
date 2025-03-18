import random
import math
pi=math.pi

def randomDotsDistance():
    r1=math.sqrt(random.random())
    r2=math.sqrt(random.random())
    angle=random.random()*2*pi
    return math.sqrt(r1**2+r2**2-2*r1*r2*math.cos(angle))

def calcAverageDistance(count=10000000):
    sum=0
    for i in range(0,count):
        sum+=randomDotsDistance()
    return sum/count

print(calcAverageDistance())
print(128/(45*pi))