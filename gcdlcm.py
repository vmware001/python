def findGcd(a,b):
    if b!=0:
        gcd=findGcd(b,a%b)
    else:
        gcd=a
    return gcd

def main():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(f"gcd={int(findGcd(a,b))},lcm={int(a*b/findGcd(a,b))}")
    print("\U0001F600") 

if __name__=='__main__':
    main()
