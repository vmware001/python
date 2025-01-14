def fibo(n):
    if n<=0:
        print("Please Check the number")
        return 0
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def main():
    n=int(input("Enter n:"))
    if n>=1:
        print(f"The {n}th fibbonacci number is {fibo(n)}")
        return 0
    else:
        return 1
    
main()
