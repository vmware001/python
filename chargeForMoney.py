import time
import math
count=0
money=int(input("Enter the amount of money:"))
start_time = time.perf_counter()
for r50 in range(0,math.floor(money/50)+1):
    for r20 in range(0,math.floor(money/20)+1):
        for r10 in range(0,math.floor(money/10)+1):
            for r5 in range(0,math.floor(money/5)+1):
                for r1 in range(0,math.floor(money/1)+1):
                    if r50*50+r20*20+r10*10+r5*5+r1*1==money:
                        count+=1
print(count)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.4f} seconds")
