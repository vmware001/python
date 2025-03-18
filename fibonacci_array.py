def fibo(n):
    fiArray=[1,1]
    for i in range(2,n):
        fiArray.append(fiArray[i-1] + fiArray[i-2])
    return fiArray

def main():
    n=int(input("Enter n:"))
    if n>=2:
        fiArray=fibo(n)
        print(fiArray[n-1])
    else:
        print("1")
    return 0

main()