def sort(array):
    newArray=[]
    newArray.append(array[0])
    for i in range(1,len(array)):
        inserted=0
        for j in range(0,len(newArray)):
            if array[i]<=newArray[j]:
                newArray.insert(j,array[i])
                inserted=1
                break
        if inserted==0:
            newArray.append(array[i])
    array[:]=newArray

def main():
    array=[]
    while True:
        in_=input("Enter a number, enter \"exit\" to quit:")
        if in_=="exit":
            break
        array.append(float(in_))
    sort(array)
    print(array)
    return 0
    
if __name__=='__main__':
    main()



            
