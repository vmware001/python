def fac(n):
    n=int(n)
    if n<0:
        return -1
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)

def main():
    m=int(input("Enter m:"))
    n=int(input("Enter n:"))
    if n<m or n<=0 or m<=0:
        print("Invalid m and n!")
        return 1
    else:
        print(fac(n)//(fac(m)*fac(n-m)))

if __name__=='__main__':
    main()
