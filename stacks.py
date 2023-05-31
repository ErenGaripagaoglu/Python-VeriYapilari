#----------------------Stacks----------------------#

class stackBond:
    def __init__(self,num,connection):
        self.data=num
        self.next=connection

    def __str__(self):
        return str(self.data) + "->"

class stackModel:
    def __init__(self):
        self.top=None
        self.size=0
    
    def isEmpty(self):
        return self.top is None
    
    def __len__(self):
        return self.size
    
    def peak(self):
        assert not self.isEmpty(), "Stack is empty! peak() won't work."
        return self.top.data
    
    def push(self,number):
        bond=stackBond(number, self.top)
        self.top=bond
        self.size += 1

    def pop(self):
        assert not self.isEmpty(), "Stack is empty! pop() won't work."
        bond=self.top
        self.top=self.top.next
        self.size -= 1
        return bond.data
    
    def printer(self):
        i=self.top
        print("Stacks Peak: ",end="")
        while (i is not None):
            print(i,end="")
            i=i.next
        print("Stacks Floor.")

#--------------------------------------------------#

stack=stackModel()
print("Component Count: ",len(stack))

stack.push(2)
print("Component Count: ",len(stack))
print("Peak Component: ",stack.peak())

stack.push(8)
print("Component Count: ",len(stack))
print("Peak Component: ",stack.peak())

stack.push(-5)
print("Component Count: ",len(stack))
print("Peak Component: ",stack.peak())

stack.printer()
print("Popped Component: ", stack.pop())
stack.printer()

for i in range(1,10):
    stack.push(i**2)

stack.printer()
print("Component Count: ",len(stack))

for i in range(0,12):
    stack.pop()
    stack.printer()

#--------------------------------------------------#