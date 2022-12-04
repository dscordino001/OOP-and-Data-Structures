#import SinglyLinkedList and Node classes from singly_linked_list.py
from singly_linked_list import SinglyLinkedList 
from singly_linked_list import Node

class DTSSortedList(SinglyLinkedList):#create subclass of SinglyLinkedList called DTSSortedList
    def append(self, data):#define append method with data attribute
        node = Node(data)#set the Node(data) to node
        if self.tail:#if tail pointer exists
            curr = self.tail#set tail pointer to point to curr
            prev = self.tail#set tail pointer to point to prev
            while curr:#if curr exists
                if curr.data > node.data:#if data in current node is greater than data in the current node
                    node.next = curr#set the next node to the current node
                    if prev == self.tail:#if prev equals the tail pointer
                        self.tail = node#set tail pointer to node
                        prev = node#set tail pointer to node
                    else:#else
                        prev.next = node#set the next pointer to node
                    break#break
                else:#else
                    prev = curr#set prev to curr
                    curr = curr.next#set next pointer to curr
        else:#else
            self.tail = node#set tail pointer to node
        self.count += 1#set node counter to increase by one when a new node is created

    def __setitem__(self, index, value):#create setitem method
        print('Set option not available')#set method to be disabled

def main():#define main method
    my_list = DTSSortedList()#create a new node list called my_list
    number = int(input("Enter a number. Enter '-1' to end list: "))#set a variable to be an integer input
    while number != -1:#when the input does not equal -1
        my_list.append(number)#append the new node to my_list
        number = int(input("Enter another number. Enter '-1' to end list: "))#set that same variable to be an integer input for another number
    curr = my_list.tail#set tail pointer of my_list to curr
    while curr:#while curr exists
        print(curr.data)#print the data inside the current variable
        curr = curr.next#set the next pointer to curr
    print(my_list)#print my_list

main()#call main method