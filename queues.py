#--------------------Queues--------------------#

class queueBond:
    def __init__(self,num):
        self.data=num
        self.next=None

    def __str__(self):
        return str(self.data)
    
class queueModel:
    def __init__(self):
        self.qHead=None
        self.qEnd=None
        self.size=0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.qHead is None
    
    def enQueue(self,num):
        bond=queueBond(num)
        if (self.isEmpty()):
            self.qHead=bond
        else:
            self.qEnd.next=bond
        self.qEnd=bond
        self.size += 1
    
    def deQueue(self):
        assert not self.isEmpty(),"Queue is empty! DeQueue won't work!"
        bond=self.qHead
        if (self.qHead is self.qEnd):
            self.qEnd=None
        self.qHead=self.qHead.next
        self.size -= 1
        return bond.data
    
    def peak(self):
        assert not self.isEmpty(),"It doesnt work if queue is empty!"
        return self.qHead.data
    
    def printer(self):
        i=self.qHead
        print("Queue size: "+str(len(self)))
        print("Queue Front: ",end="")
        while (i is not None):
            print(i,"<-",end="")
            i=i.next
        print(":Queue Rear. ")

#----------------------------------------------#

queue=queueModel()
print(len(queue))
queue.printer()

print(queue.isEmpty())

queue.enQueue(6)
queue.printer()

queue.enQueue(34)
queue.printer()

queue.enQueue(58)
queue.printer()

queue.deQueue()
queue.printer()

print(queue.peak())

print(queue.isEmpty())

#----------------------------------------------#