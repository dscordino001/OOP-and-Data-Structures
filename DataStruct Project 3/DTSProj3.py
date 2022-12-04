# Dom Scordino
# CSC145B
# March 11, 2022
# Assignment 3

# Python Code to Make a Deque with append, pop, and peek options

# Start of Code

class Node:
   def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DTSDeque:
    #this method creates an empty deque
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        #this method adds data at the end of the deque
        node = Node(data)
        if self.head:
            node.prev = self.head.data
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
        print(f'Data now added to right')
    
    def appendleft(self, data):
        #this method addas data to the front of the deck
        node = Node(data)
        if self.tail:
            node.prev = self.tail.data
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
        print(f'Data now added to left')
    
    def pop(self):
        #this method deletes a node from the back of the list
        current = self.tail
        prev = self.tail
        while current:
            if current == self.tail:
                self.tail = current.next
            else:
                prev.next = current.next
            self.count -= 1
            return
        prev = current
        current = current.next

    def popleft(self):
        #This method deletes a node from the front of the list
        current = self.head
        prev = self.head
        while current:
            if current == self.head:
                self.head = current.next
            else:
                prev.next = current.next
            self.count -= 1
            return
        prev = current
        current = current.next

    def peek(self):
        #This method shows the node from the front of the list
        if not self.head:
            print('None')
        else:
            print('')
            print(f'PEEK AT RIGHT = {self.head.data}')
            print('')

    def peekleft(self):
        #This method shows the node from the front of the list      
        if not self.tail:
            print('None')
        else:
            print('')
            print(f'PEEK AT LEFT = {self.tail.data}')

def main():
    #this method makes a deque
    dq = DTSDeque()
    i=(99,55,88,77)
    for value in i:
        dq.append(value)

    def printdeque(deque):
        #this method prints the current node and then repeats itself
        curr=deque.tail
        while curr:
            print(f'{curr.data}')
            curr=curr.next

    printdeque(dq)
    dq.append(22)
    dq.peekleft()
    printdeque(dq)
    dq.peek()

    printdeque(dq)
    dq.pop()
    dq.append(44)
    dq.peekleft()
    printdeque(dq)
    dq.peek()

    printdeque(dq)
    dq.popleft()
    dq.append(11)
    dq.peekleft()
    printdeque(dq)
    dq.peek()

#call function main()
if __name__ == '__main__':
    main()