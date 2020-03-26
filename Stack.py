class stack_sequential_storage():
    def __init__(self,MAXSIZE):
        
        self.maxsize = MAXSIZE
        self.ptrs = []
        self.top = -1
    
    def push_element(self,x):
        if self.top+1 == self.maxsize:
            print('stack is full!')
        
        else:
            self.ptrs.append(x)
        
        self.top +=1

        print(self.ptrs)
        
    def pop_element(self):
        if self.top == -1:
            print('stack is empty!')
        
        else:
            return self.ptrs[self.top]
        
            del self.ptrs[self.top]
            
            self.top -=1

'''
linked storage
'''
class stack_linked_storage():
    def __init__(self):       
        self.Stack = headnode()
        self.store = []
    
    def headnode(self):
        Data = len(self.store)
        Next = None

    def Node(self,DATA):        
        self.store.append(DATA)
        
        data = DATA
        Next = self.store.index(data) -1
        
    def push_element(self,x):
        tmpnode = Node(x)
        Stack.next = self.store.index(tmpnode.data)

    def pop_element(self,x):
        if self.Stack.Next == None:
            print('stack is empty!')

        else:
            firstcell = self.Stack.next
            firstnode.next = firstcell.next
            topelement = firstcell.data
            del firstcell

            print(topelement)
        
