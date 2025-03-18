def findMax(numArray):
    if(len(numArray))>0:
        max=numArray[0]
        order=0
    for i in range(len(numArray)):
        if numArray[i]>=max:
            max=numArray[i]
            order=i
    return order

def generateArray(n):
    numArray=[]
    for i in range(1,n+1):
        numArray.append(i**(n-i))
    return numArray
def main():
    numArray=generateArray(100)
    print(str(findMax(numArray)+1)+"\n"+str(numArray[findMax(numArray)]))

main()