import math
def findRoot(a,b,c):
    delta=b**2-4*a*c
    if delta>=0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return 1,x1,x2
    else:
        re=-b/(2*a)
        im=math.sqrt(-delta)/(2*abs(a))
        return 0,re,im

def main():
    a=float(input("Enter a:"))
    b=float(input("Enter b:"))
    c=float(input("Enter c:"))
    
    state,*roots=findRoot(a,b,c)

    if state:
        x1,x2=roots
        print(f"x1={x1},x2={x2}")
    else:
        re,im=roots
        print(f"x1={re}+{im}i,x2={re}-{im}i")
    
    return 0

if __name__=='__main__':
    main()
