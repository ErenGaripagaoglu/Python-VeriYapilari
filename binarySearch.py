#------------------------Binary Search------------------------#

def binarySearch(list,target):
    left=0
    right=len(list)-1
    while (left<=right):
        middle=(left+right)//2
        print("[%2d - %d - %d], orta eleman: %d" % (left,middle,right,list[middle]))
        if (list[middle]==target):
            return True
        elif (list[middle]<target):
            left=middle+1
        else:
            right=middle-1
    return False

#-------------------------------------------------------------#

array=[10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29] #If array is not sorted, binary search won't work.
searching=5

answer=binarySearch(array,searching)
if(answer):
    print(searching," is included in the array.")
else:
    print(searching," is not included in the array.")

#------------------------------------------------------------#

array=[10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
array.sort()
searching=5

answer=binarySearch(array,searching)
if(answer):
    print(searching," is included in the array.")
else:
    print(searching," is not included in the array.")

#------------------------------------------------------------#