#----------Merge Sort----------#

def mergeSortedLists(list1,list2):
    newArray=[]
    i=0; j=0
    while (i < len(list1) and j < len(list2)):
        if (list1[i] < list2[j]):
            newArray.append(list1[i])
            i+=1
        else:
            newArray.append(list2[j])
            j+=1
    while (i < len(list1)): #Add remaining elements of the list that contains more elements than the other
        newArray.append(list1[i])
        i+=1
    while (j < len(list2)): #Add remaining elements of the list that contains more elements than the other
        newArray.append(list2[j])
        j+=1
    return newArray

def mergeSort(list):
    print("Incoming list: ",list)
    if (len(list)<=1):
        return list
    middle=len(list)//2
    leftList=mergeSort(list[:middle])
    rightList=mergeSort(list[middle:])
    newList=mergeSortedLists(leftList,rightList)
    print("Outgoing list: ",list)
    return newList

#------------------------------#

import random

dizi=[]
for i in range(0,10):
    dizi.append(random.randint(10,100))

newList=mergeSort(dizi)
print(newList)

mergeSort(newList)

#------------------------------#