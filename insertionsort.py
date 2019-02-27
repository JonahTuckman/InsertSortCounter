def insertionSort(alist):
    count = 0;
    for index in range(1,len(alist)):
        
        currentvalue = alist[index]
        position = index
            
        while position>0 and alist[position-1]>currentvalue:
            count += 1
            alist[position]=alist[position-1]
            position = position-1
                    
            alist[position]=currentvalue
    print(count)
    return count;

half1half0 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,0 , 0, 0, 0]
half0half1 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
nothalf1 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0]
nothalf0 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
alternating1first = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
alternating0first = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
Onelotsof0 = [1,0, 0, 0, 0,0 ,0, 0, 0, 0, 0, 0, 0, 0 , 0, 0]

insertionSort(half1half0)
insertionSort(half0half1)
insertionSort(nothalf1)
insertionSort(nothalf0)
insertionSort(alternating1first)
insertionSort(alternating0first)
insertionSort(Onelotsof0)


