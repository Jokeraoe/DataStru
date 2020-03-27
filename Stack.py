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
class Node():
    def __init__(self,data):
        self.Data = data
        self.Next = None

class stack_linked_storage():
    def __init__(self):       
        self.Stack = Node(None)

        
    def push_element(self,x):
        tmpnode = Node(x)
        Stack.next = tmpnode

    def pop_element(self,x):
        if self.Stack.Next == None:
            print('stack is empty!')

        else:
            firstcell = self.Stack.next
            self.Stack.next = firstcell.next
            topelement = firstcell.data
            # free(firstcell)

            print(topelement)
        
