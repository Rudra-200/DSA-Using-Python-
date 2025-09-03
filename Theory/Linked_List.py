
class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next
class LinkedList():
    def __init__(self):
        self.head = None
        self.n=0
        
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n +1
        
    def len (self):  # doubt
        return self.n
    
    def __str__(self):      # print the Linked List
        curr = self.head
        result=""
        while(curr!=None):
            result = result + str(curr.value) + "->"
            curr=curr.next
        return result[:-2]
    
    def append(self,value):
        new_node  = Node(value)
        curr= self.head
        if curr==None :
            self.head = new_node
            self.n=self.n +1   
        else:
            while(curr.next!=None):
                curr = curr.next
            curr.next = new_node
            self.n = self.n+1
        
    def insert_after(self,value,after):
        new_node = Node(value)
        curr = self.head
        while (curr!=None):
            if (curr.value == after):
                break
            curr=curr.next                                ##IMPORTANT
        if curr!= None:
            new_node.next = curr.next
            curr.next =  new_node
            self.n =self.n+1
        else:
            return "Item not found."
        
    '''def clear(self):
        self.head.next = None
        self.n = 0'''                  #doubt
        
    def delete_head(self):
        self.head = self.head.next
        self.n = self.n-1
        
    def pop(self):
        curr = self.head
        if self.head == None:
            return "Empty LL"                             ##IMPORTANT
        elif curr.next == None:
            self.n = self.n-1
            return self.delete_head()   
        else:
            while(curr.next.next != None):
                curr = curr.next
            curr.next = None
            self.n = self.n-1
            
    def remove (self ,ele):
        curr = self.head
        if self.head == None:
            return "Empty LL"
        elif self.head.value == ele:
            self.n = self.n-1
            return self.delete_head()
        else:
            while (curr.next!= None):
                if curr.next.value == ele:                    ##IMPORTANT
                    break
                curr = curr.next
            if curr.next == None:
                return "Not Found."
            else:
                curr.next = curr.next.next
                self.n = self.n - 1
    
    def search(self ,ele):
        curr = self.head
        pos = 0
        if self.head == None:
            return "Empty LL"  
        else:
            while (curr != None):
                if curr.value == ele:                    ##IMPORTANT
                    break
                pos = pos + 1
                curr = curr.next
            if curr == None:
                return "Not Found."
            else:
                return f"Data found at index {pos}"
            
    '''def search(self, ele):
    curr = self.head
    pos = 0
    if not curr:
        return "Empty LL"
    
    while curr:
        if curr.value == ele:
            return f"Data found at index {pos}"
        pos += 1
        curr = curr.next

    return "Not Found."   '''
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr:
            if pos == index:
                return curr.value                                      # Not working check
            pos = pos +1
            curr = curr.next
        raise IndexError("LinkedList index out of range")
        
   # def reverse(self):
        
        
        
                