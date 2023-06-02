#---------Single Linked List---------#

import random

class Bond:
    def __init__(self,number):
        self.data=number
        self.next=None

    def __str__(self):
        return str(self.data)
    
class SLinkedList: 
    def __init__(self):
        self.head=None
        self.end=None 

    def traversing(self):
        print("Traversing Started: ",end="")
        i=self.head
        while (i is not None):
            print(i,"->",end="")
            i=i.next
        print(".")

    def add(self,number):
        newBond=Bond(number)
        if (self.head is None):
            self.head=newBond 
            self.end=newBond  
        else:
            self.end.next=newBond
            self.end=newBond

    def addToHead(self,number):
        newBond=Bond(number)
        newBond.next=self.head
        self.head=newBond
    
    def addToMiddle(self,number):
        newBond=Bond(number)
        previous=None
        i=self.head
        while (i is not None and number>i.data):
            previous=i
            i=i.next
        newBond.next=i
        if (i==self.head):
            self.head=newBond
        else:
            previous.next=newBond

    def isExist(self,wanted):
        i=self.head
        while (i is not None and wanted != i.data):
            i=i.next
        return i is not None

    def search(self,wanted):
        i=self.head
        while(i is not None and wanted !=i.data):
            i=i.next
        print(wanted," is in the list ",end="")
        if (i is not None):
            print("Does Exist!")
        else:
            print("Doesn't Exist!")

    def delete(self,target):
        previous=None
        i=self.head
        while(i is not None and target != i.data):
            previous=i
            i=i.next
        if(i is None):
            print(target,"isn't in the list")
        else:
            if (i is self.head):
                self.head=self.head.next
            elif (i is self.end):
                self.end=previous
                self.end.next=None
            else:
                previous.next=i.next
            i=None
    
    def deleteMultiple(self,*targets):
        l=[]
        for j in targets:
            l.append(j)
        for i in l:
            if (SLList.isExist(i)):
                SLList.delete(i)
                print(i,"has been deleted.")

    def addRandom(self,steps):
        for j in range(steps):
            rndmNumber=random.randint(-256,256)
            newBond=Bond(rndmNumber)
            previous=None
            i=self.head
            while (i is not None and rndmNumber>i.data):
                previous=i
                i=i.next
            newBond.next=i
            if (i==self.head):
                self.head=newBond
            else:
                previous.next=newBond
            print(rndmNumber,"is added in to the list.")

    def deleteIndex(self,search): #Listenin belli indexini silme
        count=0
        p=self.head
        while (p is not None and count!=search):
            count+=1
            q=p
            p=p.next
        if (p is None):
            return
        q.next=p.next
        p.next=None

    def deleteAll(self):
        self.head=None
        self.end=None

#------------------------------------#

SLList=SLinkedList()
SLList.traversing()

for i in range(11):
    SLList.add(i**2)
SLList.traversing()

SLList.addRandom(3)
SLList.traversing()

SLList.addToHead(-10)
SLList.traversing()

SLList.addToMiddle(3)
SLList.traversing()

SLList.addToMiddle(4)
SLList.traversing()

SLList.addToMiddle(-20)
SLList.traversing()

SLList.deleteMultiple(3,16)
SLList.traversing()

SLList.addToMiddle(110)
SLList.traversing()

print("Does number 25 exist in the list? ",end="")
if (SLList.isExist(25)):
    print("Does Exist!")
else:
    print("Doesn't Exist!")

print("Does number 81 exist in the list? ",end="")
if (SLList.isExist(81)):
    print("Does Exist!")
else:
    print("Doesn't Exist!")

SLList.search(27)
SLList.search(100)

SLList.delete(-20)
SLList.traversing()

SLList.deleteIndex(2)
SLList.traversing()

SLList.deleteAll()
SLList.traversing()

#------------------------------------#